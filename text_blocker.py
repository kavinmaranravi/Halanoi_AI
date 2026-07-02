import time
import ctypes
import tkinter as tk
import threading
import numpy as np

# Note: You will need to install transformers alongside tensorflow
# pip install tensorflow transformers
import tensorflow as tf
from transformers import AutoTokenizer

class TextDistractionBlocker:
    def __init__(self, model_dir, tflite_path):
        self.overlay_active = False
        self.root = None
        
        print("Loading Tokenizer...")
        # Loads the tokenizer_config.json, vocab, etc. from your halanoi_transformer folder
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
        
        print(f"Loading TFLite Model from {tflite_path}...")
        self.interpreter = tf.lite.Interpreter(model_path=tflite_path)
        
        # --- FIX: Resize input tensors for Dimension Mismatch ---
        # TFLite models often export with shape [1, 1] for dynamic inputs.
        # We need to resize them to [1, 128] before allocating memory.
        for detail in self.interpreter.get_input_details():
            self.interpreter.resize_tensor_input(detail['index'], [1, 128])
            
        self.interpreter.allocate_tensors()
        
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        print("AI Model & Tokenizer successfully loaded!")

    def get_active_window_title(self):
        """Uses Windows built-in API to read the title of the current active window."""
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
        buf = ctypes.create_unicode_buffer(length + 1)
        ctypes.windll.user32.GetWindowTextW(hwnd, buf, length + 1)
        return buf.value

    def block_screen(self):
        """Spawns a full-screen, unclosable overlay."""
        if self.overlay_active:
            return
            
        self.overlay_active = True
        self.root = tk.Tk()
        self.root.title("BLOCKED")
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg='black')
        self.root.protocol("WM_DELETE_WINDOW", lambda: None) 
        
        warning = tk.Label(self.root, text="ENTERTAINMENT DETECTED.\nGET BACK TO WORK BRO!", 
                           font=("Helvetica", 40, "bold"), fg="red", bg="black")
        warning.pack(expand=True)
        self.root.mainloop()

    def unblock_screen(self):
        """Removes the block overlay."""
        if self.overlay_active and self.root:
            self.root.destroy()
            self.overlay_active = False

    def predict_text(self, text):
        """Tokenizes the window title and runs it through your .tflite model."""
        if not text.strip():
            return 0.0 # Ignore empty window titles
            
        # 1. Tokenize the text based on your model's vocab
        # Adjust max_length if your model was trained on a different sequence length (e.g., 64 or 128)
        inputs = self.tokenizer(text, return_tensors="tf", padding='max_length', truncation=True, max_length=128)
        
        # 2 & 3. Feed the tokens into the TFLite model safely
        # We loop through input details to handle input_ids AND attention_mask (if the model expects it)
        for detail in self.input_details:
            expected_dtype = detail['dtype']
            
            if 'attention_mask' in detail['name'].lower() and 'attention_mask' in inputs:
                mask = tf.cast(inputs['attention_mask'], expected_dtype)
                self.interpreter.set_tensor(detail['index'], mask)
            else:
                # Default main input is input_ids
                input_ids = tf.cast(inputs['input_ids'], expected_dtype)
                self.interpreter.set_tensor(detail['index'], input_ids)
        
        # 4. Run the prediction
        self.interpreter.invoke()
        
        # 5. Get the result (these are raw negative/positive logits)
        output = self.interpreter.get_tensor(self.output_details[0]['index'])[0]
        
        # 6. Apply Softmax math to convert raw numbers into percentages (0.0 to 1.0)
        probabilities = np.exp(output) / np.sum(np.exp(output))
        
        print(f"   [Debug] Probabilities Array: {probabilities}")
        
        # If your model outputs 2 classes (e.g., [Safe, Entertainment])
        if len(probabilities) > 1:
            # We assume index 1 is Entertainment. 
            # Note: If it blocks the wrong stuff, change this to probabilities[0]!
            prediction_score = float(probabilities[1]) 
        else:
            # If the model only outputs 1 number, use Sigmoid math instead
            prediction_score = float(1 / (1 + np.exp(-output[0]))) 
            
        return prediction_score

    def run(self):
        """Main loop that continuously checks the active window."""
        print("Starting Window Monitor... Press Ctrl+C in the terminal to stop.")
        last_title = ""
        
        while True:
            current_title = self.get_active_window_title()
            
            # Only run the AI if the user switched to a new window (saves CPU)
            if current_title and current_title != last_title:
                print(f"\n[Scanned Window]: {current_title}")
                
                try:
                    score = self.predict_text(current_title)
                    print(f"[AI Distraction Score]: {score:.4f} ({(score*100):.1f}%)")
                    
                    # If the AI says it's entertainment (e.g., > 80% confident)
                    if score > 0.8:
                        print("🚨 BLOCKED! 🚨")
                        if not self.overlay_active:
                            threading.Thread(target=self.block_screen, daemon=True).start()
                    else:
                        self.unblock_screen()
                        
                except Exception as e:
                    print(f"Error making prediction: {e}")
                    
                last_title = current_title
                
            time.sleep(1) # Check every 1 second

if __name__ == "__main__":
    # Point this to your folder from the screenshot
    MODEL_FOLDER = "halanoi_transformer"
    
    # FIXED: Adjusted path to look in the current directory since the .tflite file is here
    TFLITE_FILE = "halanoi_transformer.tflite" 
    
    blocker = TextDistractionBlocker(model_dir=MODEL_FOLDER, tflite_path=TFLITE_FILE)
    blocker.run()