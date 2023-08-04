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
  
<br>

## 구현 기능

### 기능1. 재활용품 탐지 - 모바일 서비스

&nbsp;&nbsp;&nbsp;&nbsp;사용자는 모바일 어플을 통해 쓰레기의 중심좌표 , 크기 , 품목을 알 수 있다.

### 기능 2 : 재활용 가이드 제공 - 모바일 서비스

&nbsp;&nbsp;&nbsp;&nbsp;사용자에게 탐지된 재활용품의 처리 가이드 라인을 제공한다.

### 기능 3 : 데이터 시각화 - 개발자 도구

&nbsp;&nbsp;&nbsp;&nbsp;모델의 파이프라인을 수정하여 탐지한 물체의 이미지 벡터를 추출할 수 있다.

&nbsp;&nbsp;&nbsp;&nbsp;추출한 이미지 벡터로 T-SNE 및 PCA 시각화를 진행하였고,
&nbsp;&nbsp;&nbsp;&nbsp;내부적으로 정성 평가를 위해 각 이미지를 비교할 수 있도록 도구를 개발하였다.

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

## 디렉토리 설명

Garbage-Classification<br>          
┣ Mobile_Develop <br>
┣ Model_Develop  <br>
┃ ┣ Custom_Model <br>
┃ ┃ ┗ ultralytics <br>
┃ ┣ Dataset_Sampling <br>
┃ ┣ Dataset_Visualization <br>
┃ ┗ Model_Train





## 활용방안 및 기대효과

<p align="justify">

</p>

<br>

## 라이센스

MIT &copy; [NoHack](mailto:lbjp114@gmail.com)

<!-- Stack Icon Refernces -->
