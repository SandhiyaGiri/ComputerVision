# 🦴 Fracture Detection with RF-DETR

This project provides an interactive Gradio interface for detecting fractures in X-ray images using the RF-DETR model (Base or Large variants). It loads pretrained weights and visualizes predictions with bounding boxes and class labels.

## 🚀 Features
- Upload an X-ray image and select the model variant (Base or Large).
- View annotated predictions and confidence scores.
- Supports inference on CPU/GPU.
- Visualizes both predictions and ground truth.

## 🧠 Model Options
- **Base**: Lightweight RF-DETR model.
- **Large**: High-accuracy RF-DETR model with larger backbone (DINOv2).

## 🛠️ Setup

```bash
# Create environment and install dependencies
conda create -n rfdetr_env python=3.10 -y
conda activate rfdetr_env
pip install -r requirements.txt
