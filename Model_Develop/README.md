# 모델 관련 코드

## Custom_model

- ultralytic에서 제공하는 YOLOv8모델 파이프라인을 수정하여 객체의 이미지 벡터를 추출하도록 수정

- 수정한 모델 예제 파일 수록

## Dataset_Sampling

- 학습계획에 맞춰 필요한 Dataset을 샘플링하는 코드

- Fastai의 warp 데이터 증강 포함

## Dataset_Visualization

- custom_model로 추출한 이미지 벡터를 T-SNE 및 PCA를 진행하여 2차원 시각화를 진행

- 내부적으로 모델 성능 및 결과를 설명하기 위해(XAI) 내부적인 시각화 개발 도구 구현

## Model_Train

- AWS EC2 LINUX환경에 맞춰 사용된 Config파일 및 훈련 코드

- 모델 결과도 수록


