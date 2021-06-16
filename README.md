# 프로젝트 소개
<b>Face-Mask-Synthesis System</b><br><br>
이미지에서 마스크로 가려진 얼굴 부분을 본래의 얼굴로 채워주는 시스템 "FMS".<br><br>
마스크를 착용하고 촬영한 사진을 기존의 사용자 데이터를 이용해
마스크로 가려진 부분의 얼굴을 합성하여 준다.<br><br>

# 팀원 소개
- 송민수
- 강영서
- 박교녕
- 박민수
- 이원정
- 임준엽

# 개발 환경
- Python 3.7.10
- Tensorflow 2.4.1
- Ubuntu 18.04.5 LTS
- Anaconda 4.10.1
- CUDA 11.2
- OpenCV 4.5.2
- Jupyter Notebook
- Ionic 5.4.16
- Node Js 14.17.0

<br>

# How to Run

### 1. Input Data 준비
해당 어플리케이션을 통해 합성된 결과물을 얻기 위해서 두 가지의 Input Data가 필요하다. <br><br>
(1) 마스크를 착용한 채, 정면을 보고 있는 이미지 파일이 필요하다. <br><br>
<img src = "https://user-images.githubusercontent.com/71958885/122261491-6c197980-cf0f-11eb-9cfd-c6796c71facb.jpg" width = "60%" height = "60%"><br><br><br>
(2) 정면에서 양 측면의 얼굴까지 천천히 회전시키며 보여주는, 약 5초 정도의 영상 파일이 필요하다.<br><br> 
<img src = "https://user-images.githubusercontent.com/71958885/122261382-4ee4ab00-cf0f-11eb-9391-7cb62ee91124.gif"><br><br>



### 2. 애플리케이션 실행
```bash
$ git clone https://github.com/CSID-DGU/2021-1-OSSP1-Debugger-4.git
$ cd 2021-1-OSSP1-Debugger-4/FMS
$ npm install --save-dev @angular-devkit/build-angular
```
<br>

```bash
$ ionic serve //Local에서 실행.
```
<br>
자체 서버에서 Model 을 두고 Service 하기 때문에 서버 가동 중이 아닐 시, 정상 실행이 안될 수도 있음.

<br><br>



## 애플리케이션 구성도
<img src = "https://user-images.githubusercontent.com/71958885/122260136-e0531d80-cf0d-11eb-9ae8-6b3a7ae25fe6.PNG"><br><br><br>


## Model Structure
<img src = "https://im3.ezgif.com/tmp/ezgif-3-f04a7d8828a9.gif"><br><br><br>

## 데모영상
<img src = "https://user-images.githubusercontent.com/71958885/122260531-59eb0b80-cf0e-11eb-96cf-a4c93c0828ff.gif"><br><br><br>

## 문의
```
송민수 sooya233@dgu.ac.kr
강영서 22019112024@gmail.com
임준엽 dunebi1030123@gamil.com
박민수 pms1139@gmail.com
이원정 wonjung1015@dgu.ac.kr
박교녕 rysud0125@dgu.ac.kr
```
