# python download_models.py - downloads all models for IIIT demo
from ultralytics import YOLO
import whisper
import os

os.makedirs("models", exist_ok=True)
print("Downloading YOLOv8 for PPE + Objects...")
YOLO("yolov8n.pt") # helmets, persons, mobile
YOLO("yolov8s.pt") # workstations
print("Downloading Whisper base for whisper analysis...")
whisper.load_model("base") # for disabled voice
print("Mediapipe models auto-download on first use")
print("Models ready in models/")
print("For regional translation: pip install googletrans==4.0.0-rc1")
