# 마스크로 가려진 얼굴 합성 시스템
2021-1-OSSP1-Debugger-4
실외에서 마스크를 끼고 촬영을 하게 되면 기존의 사용자 데이터를 활용하여 마스크로 가려진 부분의 얼굴을 합성한다.

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

## 실행 전 파일 추가
http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 다음 링크를 이용하여 파일의 압축을 푼 후, <br>
main폴더의 preprocess에 추가한 뒤 다음 프로그램을 진행한다.


## Input Data 준비
해당 어플을 실행시키고 나면, 두 개의 Input Data가 필요하다. <br>
첫 번째로, 정면으로 보고 있는 마스크를 낀 사진이 필요하다. <br>
두 번째로, 정면에서 시작한 5초 정도의 영상이 필요하다. <img src = "https://im3.ezgif.com/tmp/ezgif-3-f04a7d8828a9.gif">
