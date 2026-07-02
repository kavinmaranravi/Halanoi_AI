import subprocess
import sys

def main():
    scripts = [
        ("Step 1: Appending new tests to dataset", "append_failed_tests.py"),
        ("Step 2: Retraining the Transformer model", "train_transformer_tf.py"),
        ("Step 3: Converting model to TFLite", "convert_tflite.py"),
        ("Step 4: Running model tests", "test_model.py")
    ]

    for desc, script in scripts:
        print(f"\n{'='*60}\n🚀 {desc} ({script})\n{'='*60}")
        result = subprocess.run([sys.executable, script])
        
        if result.returncode != 0:
            print(f"\n❌ Error encountered while running {script}. Automation stopped.")
            sys.exit(result.returncode)

    print("\n✅ Automation complete! Your AI is successfully retrained, converted, and verified.")

if __name__ == "__main__":
    main()