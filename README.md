# Team BIO : 재활용품 분리배출 도우미

<p align="center">
  <img src="./images/move_garbage.gif" alt="thumbnail" width="400"/>
</p>

## 프로젝트 소개

모바일 환경에서 YOLOv8기반 Object Detection으로 재활용 쓰레기를 탐지하여 사용자들에게 올바른 재활용 가이드 라인을 제공한다.

사용한 Dataset - [AI-HUB 생활폐기물 데이터 ](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71385)


<div align=center><h1>📚 OUR STACKS</h1></div>  <div align=center>  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/java-007396?style=for-the-badge&logo=java&logoColor=white">     <br>  
<img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"> <img src="https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white">  <img src="https://img.shields.io/badge/FASTAI-40AEF0?style=for-the-badge&logo=&logoColor=white"> <img src="https://img.shields.io/badge/yolo-21375A?style=for-the-badge&logo=yolo&logoColor=white"> <img src="https://img.shields.io/badge/ultralytics-2D50A5?style=for-the-badge&logo=ultralytics&logoColor=white">  <br>  
 <img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">  <img src="https://img.shields.io/badge/aws EC2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white">
<img src="https://img.shields.io/badge/aws S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white"> <br>  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">  <img src="https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"> <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white"> <br>  
<img src="https://img.shields.io/badge/android-68A51C?style=for-the-badge&logo=android&logoColor=white"> <img src="https://img.shields.io/badge/androidstudio-3DDC84?style=for-the-badge&logo=androidstudio&logoColor=white"> <br>  

</div>
  
## 구현 기능

### 기능 1 : 재활용품 탐지 - 모바일 서비스

&nbsp;&nbsp;&nbsp;&nbsp;사용자는 모바일 어플을 통해 재활용 쓰레기의 정확한 품목을 알 수 있다.

### 기능 2 : 재활용 가이드 제공 - 모바일 서비스

&nbsp;&nbsp;&nbsp;&nbsp;사용자에게 탐지된 재활용품의 처리 가이드 라인을 제공한다.


<p align="center">
  <img src="./images/Demo.gif" alt="thumbnail" width="400"/>
</p>



### 기능 3 : 데이터 시각화 - 개발자 도구

&nbsp;&nbsp;&nbsp;&nbsp;모델의 파이프라인을 수정하여 탐지한 물체의 이미지 벡터를 추출할 수 있다.

&nbsp;&nbsp;&nbsp;&nbsp;추출한 이미지 벡터로 T-SNE 및 PCA 시각화를 진행 후, 내부적으로 정성 평가를 위해 각 이미지를 비교할 수 있도록 도구를 개발하였다.

<table>
  <tr>
    <td>
      <div style="text-align: center;">
        <img src="./images/tsne_sameClass.gif" alt="thumbnail" width="400"/>
        <p>다른 공간 같은 Class 이미지 예시</p>
      </div>
    </td>
    <td>
      <div style="text-align: center;">
        <img src="./images/tsne_dffClass.gif" alt="thumbnail" width="400"/>
        <p>비슷한 공간 다른 Class 이미지 예시</p>
      </div>
    </td>
  </tr>
</table>

<br>

## 개발 과정 간략도

<p align="center">
  <img src="./images/development_process.png" alt="thumbnail" width="1000"/>
</p>

## 디렉토리 설명

Garbage-Classification<br>
┣ [Mobile_Develop](https://github.com/mindang/Garbage-Classification/tree/main/Mobile_Develop) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 어플리케이션 개발 폴더<br>
┃ ┗ [app](https://github.com/mindang/Garbage-Classification/tree/main/Mobile_Develop/app) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #  어플리케이션 코드<br>
┣ [Model_Develop](https://github.com/mindang/Garbage-Classification/tree/main/Model_Develop) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 모델 및 데이터셋 관련 폴더<br>
┃ ┣ [Custom_Model](https://github.com/mindang/Garbage-Classification/tree/main/Model_Develop/Custom_Model) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 기존 YOLO 패키지 수정 <br>
┃ ┣ [Dataset_Sampling](https://github.com/mindang/Garbage-Classification/tree/main/Model_Develop/Dataset_Sampling)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 데이터셋 샘플링 관련 코드<br>
┃ ┣ [Dataset_Visualization](https://github.com/mindang/Garbage-Classification/tree/main/Model_Develop/Dataset_Visualization)&nbsp;&nbsp;&nbsp;# 데이터셋 시각화 관련 코드<br>
┃ ┗ [Model_Train](https://github.com/mindang/Garbage-Classification/tree/main/Model_Develop/Model_Train) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 모델 가중치 및 결과<br><br><br><br>





## 현재 및 향후 기대 효과

<table>
  <tr>
    <td>
      <div style="text-align: center;">
        <img src="./images/expectation_effect1.png" alt="thumbnail" width="400"/>
      </div>
    </td>
    <td>
      <div style="text-align: center;">
        <img src="./images/expectation_effect2.png" alt="thumbnail" width="400"/>
      </div>
    </td>
  </tr>
</table>

**[배경]** 대한민국 가정에서 버린 쓰레기는 모두 각 지역구 선별장으로 이동하게 되며 일부 자동화 선별장을 제외한 대부분은 사람이 직접 수작업 분류를 진행하고 있다.
<br>

**<첫째>**

현재는 사용자가 직접 쓰레기를 비추며 안내문을 출력하지만 IOT서비스와 연결하여 SMART쓰레기통 , SMART주방 , SMART분리수거장으로 활용할 수 있다.

이렇게 가정에서 1차적으로 재활용품 분류가 잘 될수록 다음 처리단계인 선별장에서 노동자들의 업무 부담을 줄일 수 있으며 친환경 사회로 나아갈 수 있다.
<br>

**<둘째>**

선별장환경에 맞춰 모델을 학습한다면 로봇을 이용하여 적은 임금을 받으며 열약한 환경에서 근무하는 노동자의 노동환경을 개선할 수 있다.

로봇을 이용하여 선별장에서 대규모 , 오염된 쓰레기를 분류한다면 업체는 적은 임금비용으로 노동자는 쾌적한 환경에서 근무 가능할 것이다.
<br>

