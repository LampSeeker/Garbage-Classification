import ultralytics
from ultralytics import YOLO
import cv2
import torch

model = YOLO('yolov8s.pt')


model.train(data='train_bigdata.yaml', epochs=60, batch=-1, plots=True, imgsz=640, patience=10, save_period=5, mixup=0.25, label_smoothing=0.1, project='final', name='final')