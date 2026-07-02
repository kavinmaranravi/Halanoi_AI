import pandas as pd
import tensorflow as tf
import random
import string
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification

# Load data
df = pd.read_csv("training_data.csv")

# Encode labels
labels = df["label"].unique().tolist()
label2id = {l:i for i,l in enumerate(labels)}
id2label = {i:l for l,i in label2id.items()}
df["label"] = df["label"].map(label2id)

# Split
train_df = df.sample(frac=0.8, random_state=42).copy()
val_df = df.drop(train_df.index)

# Dynamically generate typos for the training set
def generate_typos(text, typo_prob=0.15):
    if not isinstance(text, str) or len(text) < 3: return text
    words = text.split()
    for i in range(len(words)):
        # Only apply typos to words longer than 3 characters based on typo_prob
        if random.random() < typo_prob and len(words[i]) > 3:
            word = list(words[i])
            typo_type = random.choice(['swap', 'drop', 'insert', 'replace'])
            idx = random.randint(1, len(word) - 2)
            
            if typo_type == 'swap': word[idx], word[idx+1] = word[idx+1], word[idx]
            elif typo_type == 'drop': word.pop(idx)
            elif typo_type == 'insert': word.insert(idx, random.choice(string.ascii_lowercase))
            elif typo_type == 'replace': word[idx] = random.choice(string.ascii_lowercase)
            words[i] = "".join(word)
    return " ".join(words)

print("Applying random typos to training data for robustness...")
train_df["text"] = train_df["text"].apply(lambda x: generate_typos(x, typo_prob=0.15))

# Load tokenizer
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize(texts):
    return tokenizer(
        texts.tolist(),
        truncation=True,
        padding=True,
        max_length=128,
        return_tensors="tf"
    )

train_enc = tokenize(train_df["text"])
val_enc = tokenize(val_df["text"])

# Labels
train_labels = tf.convert_to_tensor(train_df["label"].values)
val_labels = tf.convert_to_tensor(val_df["label"].values)

# Load model
model = TFAutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=len(labels),
    id2label=id2label,
    label2id=label2id
)

# Compile
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=2e-5),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"]
)

# Train
model.fit(
    train_enc.data,
    train_labels,
    validation_data=(val_enc.data, val_labels),
    epochs=5,
    batch_size=8
)

# Save model
model.save_pretrained("halanoi_transformer")
tokenizer.save_pretrained("halanoi_transformer")

print("✅ Training complete")