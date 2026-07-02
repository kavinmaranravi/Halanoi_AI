# Halanoi AI Model Training Pipeline 🧠

This repository contains the dataset and training pipeline for the local **Edge AI Screen Sniper** used in the Halanoi Sovereign Android app and Halanoi Focus Guard browser extension. 

By open-sourcing this pipeline, developers can audit the classification logic, contribute new training samples, and train their own custom versions of the `halanoi_transformer.tflite` model.

---

## 📐 Project Structure

*   `training_data.csv`: The training dataset containing labeled text samples classified into categories: `safe`, `education`, `business`, `technology`, `sports`, `entertainment`, `nsfw`, `politics`.
*   `train_transformer_tf.py`: The core TensorFlow script to fine-tune a DistilBERT transformer model on the dataset.
*   `add_tricky_data.py`: A script to generate challenging, ambiguous training data (e.g. distinguishing between "playing sports" [sports] and "the physics of sports" [education]) to make the model robust against false positives.
*   `convert_tflite.py`: Converts the trained TensorFlow model into an optimized, lightweight `.tflite` file for edge devices.
*   `test_model.py`: Evaluates the model accuracy on a suite of pre-configured test strings.
*   `auto_retrain.py`: Automatically runs the dataset compilation, training, and conversion steps.

---

## 🛠️ Environment Setup & Training

### 1. Initialize Virtual Environment
It is highly recommended to use a virtual environment to prevent package version conflicts:
```bash
python -m venv transformer_env
# On Windows:
transformer_env\Scripts\activate
# On Linux/macOS:
source transformer_env/bin/activate
```

### 2. Install Dependencies
```bash
pip install numpy==1.24.3 pandas==2.0.3 tensorflow transformers
```

### 3. Generate Tricky Training Data
Run the helper script to append advanced conversational and short-phrase search queries to your dataset:
```bash
python add_tricky_data.py
```

### 4. Train the Model
Train the DistilBERT classifier model on the updated dataset:
```bash
python train_transformer_tf.py
```

### 5. Run Model Validation Tests
Test the newly trained model against validation queries to verify accuracy:
```bash
python test_model.py
```

### 6. Convert to TFLite
Convert the fine-tuned model into the optimized `.tflite` format ready to be placed into the Android app's `assets` folder or the extension backend:
```bash
python convert_tflite.py
```

---

## 🔒 Security & Privacy Notice
All scripts and training datasets in this repository are designed to run **100% locally**. There are no API keys, cloud secrets, or personal data files included. The dataset contains only generic labeled text examples used for NLP classification.