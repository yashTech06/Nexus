# Nexus Object Detection - Duality AI Hackathon

This project trains a YOLOv8 model on synthetic space station data generated from Duality AI's Falcon digital twin platform.

## 👨‍🚀 Team Nexus
- Muskan Kushwaha
- Khushi Chouhan
- Khush Bhati
- Yashwardhan Purohit

## 🧠 Features
- YOLOv8 object detection for toolbox, fire extinguisher, and oxygen tank
- Synthetic dataset from Falcon
- Evaluation using mAP@0.5, confusion matrix
- Lightweight and modular code

## 🛠️ How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Train the model:

```bash
python scripts/train.py
```

3. Run inference:

```bash
python scripts/predict.py
```

## 📁 Folder Structure

- `data/` - dataset folder (train/val/test)
- `models/` - trained YOLOv8 weights
- `scripts/` - training and prediction scripts
- `results/` - predictions, metrics, and graphs

## 🛰️ Powered by
- Duality Falcon
- YOLOv8 by Ultralytics

## 📄 License
Open source for educational and non-commercial use.
