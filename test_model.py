from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
import tensorflow as tf
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("halanoi_transformer")
model = TFAutoModelForSequenceClassification.from_pretrained("halanoi_transformer")
id2label = model.config.id2label

tests = [
    ("Gemini Hi maran What should we do next?", "safe"),
    ("What's a totally different career where you could see me thriving?", "safe"),
    ("Recommend a documentary based on what I've been curious about", "safe"),
    ("Actually this feature", "safe"),
    ("who was b", "safe"),
    ("Wait b", "safe"),
    ("So 45 m", "safe"),
    ("So 45 minutes is no", "safe"),
    ("So then who the man 3xsit", "safe"),
    ("neet pg dates", "education"),
    ("13% (2m left) • 20 MB", "safe"),
    ("no more quality 5est", "safe"),
    ("here lau", "safe"),
    ("doesn't ubd", "safe"),
    ("080 6217 8718", "safe"),
    ("How download f", "safe"),
    ("GATE Phase 2 Cheat Sheet PDF 3.pdf", "education"),
    ("I am ready for Phase 2: The GATE Wrap-Up Cheat Sheet", "education"),
    ("Search ticket", "safe"),
    ("Ready for set 5", "safe"),
    ("Now it is time switch next role that is from", "safe"),
    ("Okay this grand finale o", "safe"),
    ("It is my mistake 6", "safe"),
    ("Sorry my mistake 5hr", "safe"),
    ("6 pdf sorry", "safe"),
    ("Share screen with Live", "safe"),
    ("56/2,268 Share Edit Delete More", "safe"),
    ("Hi sir, recently I call you for the fiappointment", "business"),
    ("Copy Edit Retry", "safe"),
    ("What's on your mind? What impact does dew have on T20 matches?", "sports"),
    ("dc songs", "entertainment"),
    ("song download app", "entertainment"),
    ("Search Google Photos Photos Collections May 2 Preview Done", "safe"),
    ("View Model Card on Hugging Face", "technology"),
    ("npu p", "technology"),
    ("wynk music", "entertainment"),
    ("i wan", "safe"),
    ("See the screenshot please", "safe"),
    ("Sorry ocr to odf", "technology"),
    ("Describe your video", "safe"),
    ("I want this type of monochrome on behalf my photo attached", "safe"),
    ("Today 9:41 PM Share Edit Delete More", "safe"),
    ("Share Copy Save", "safe"),
    ("But i want same clothes and same face from the original", "safe"),
    ("Can I get photo same angle from the monochrome reference photo", "safe"),
    ("gemma 3 download", "technology"),
    ("Then why youtube channel i am", "safe"),
    ("windows update stuck at 99%", "technology"),
    ("ERR_CONNECTION_TIMED_OUT how to fix", "technology"),
    ("why is my laptop screen flickering", "technology"),
    ("bluetooth mouse keeps disconnecting windows 11", "technology"),
    ("dns_probe_finished_nxdomain fix", "technology"),
    ("what is the weather like today", "safe"),
    ("nearest grocery store open now", "safe"),
    ("directions to the nearest gas station", "safe"),
    ("is it going to rain tomorrow", "safe"),
    ("coffee shops near me", "safe")
]

correct = 0
print("\n--- RUNNING MODEL TESTS ---")
for text, expected in tests:
    inputs = tokenizer(text, return_tensors="tf", truncation=True, padding=True)
    outputs = model(inputs)
    probs = tf.nn.softmax(outputs.logits, axis=-1)
    pred_id = int(np.argmax(probs.numpy()[0]))
    prediction = id2label[pred_id]
    score = float(probs.numpy()[0][pred_id])
    
    if prediction == expected:
        correct += 1
        print(f"✅ [RIGHT] {text[:40]:<40}... -> Pred: {prediction} ({score:.2f})")
    else:
        print(f"❌ [WRONG] {text[:40]:<40}... -> Pred: {prediction} (Expected: {expected})")

print("-" * 60)
print(f"Accuracy: {correct}/{len(tests)} ({correct/len(tests)*100:.2f}%)")