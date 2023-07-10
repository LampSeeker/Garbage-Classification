from ultralytics import YOLO
#YOLO CLI 제공
from clearml import Task
import os
import load_annotation
import train_model_yolov8
#머신러닝 학습 모니터링 데이터 버저닝 툴(https://app.clear.ml/dashboard)
#참고 영상 : https://www.youtube.com/watch?v=ZzC3SJJifMg
#2        : https://www.youtube.com/watch?v=em_lOAp8DJE



'''
task: Whether we want to detect, segment, or classify on the dataset of our choice.
mode: Mode can either be train, val, or predict. As we are running training, it should be train.
model: The model that we want to use. Here, we use the YOLOv8 Nano model pretrained on the COCO dataset.
imgsz: The image size. The default resolution is 640.
data: Path to the dataset YAML file.
epochs: Number of epochs we want to train for.
batch: The batch size for data loader. You may increase or decrease it according to your GPU memory availability.
name: Name of the results directory for runs/detect.

'''
'''
def main():
    # main 함수의 내용을 작성하세요
    results=train_model_yolov8.train_model()
    



if __name__ == "__main__":
    main()

'''
