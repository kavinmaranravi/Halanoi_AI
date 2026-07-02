from transformers import TFAutoModelForSequenceClassification

model = TFAutoModelForSequenceClassification.from_pretrained("halanoi_transformer")

print(model.config.id2label)