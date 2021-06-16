## 프로젝트 소개
<b>Face-Mask-Synthesis System</b><br><br>
이미지에서 마스크로 가려진 얼굴 부분을 본래의 얼굴로 채워주는 시스템 "FMS".<br>
실외에서 마스크를 끼고 촬영한 사진을 기존의 사용자 데이터를 활용하여
마스크로 가려진 부분의 얼굴을 합성하여 마스크 없는 사진으로 만든다.<br>

## 팀원 소개
- 송민수
- 강영서
- 박교녕
- 박민수
- 이원정
- 임준엽

## 개발 환경
- Python 3.7.10
- Tensorflow 2.4.1
- Ubuntu 18.04.5 LTS
- Anaconda 4.10.1
- CUDA 11.2
- OpenCV 4.5.2
- Jupyter Notebook


## Input Data 준비
해당 어플리케이션을 통해 합성된 결과물을 얻기 위해서 두 개의 Input Data가 필요하다. <br>
첫 번째로, 마스크를 착용한 채로 정면을 보고 있는 이미지 파일이 필요하다. <br><br>
<img src = "https://im3.ezgif.com/tmp/ezgif-3-f04a7d8828a9.gif"><br><br>
두 번째로, 정면에서 양 측면의 얼굴까지 천천히 회전시키며 보여주는 약 5초 정도의 영상 파일이 필요하다.<br><br> 
<img src = "https://im3.ezgif.com/tmp/ezgif-3-f04a7d8828a9.gif"><br><br>
위 두가지의 파일이 준비되었다면, 아래의 방법대로 FMS 어플리케이션을 실행하면 된다.


