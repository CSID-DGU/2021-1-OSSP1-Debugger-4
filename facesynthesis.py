# 라이브러리 설정
import numpy as np
import cupy
import tensorflow as tf
import matplotlib.pyplot as plt
import random
import cv2
import gc
import glob
from tensorflow.keras.layers import Reshape
from keras.models import load_model
import keras
from imutils import face_utils
import imutils
import dlib
import math
from preprocess.final_synthesis_ver3 import *
from preprocess.video_framing import extract_image_one_fps

# 랜덤 시드 고정
SEED=2021
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)

def synthesis():
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
      try:
        # Currently, memory growth needs to be the same across GPUs
        for gpu in gpus:
          tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
      except RuntimeError as e:
        # Memory growth must be set before GPUs have been initialized
        print(e)
    strategy = tf.distribute.MirroredStrategy(devices=["/gpu:0","/gpu:1","/gpu:2","/gpu:3","/gpu:4","/gpu:5","/gpu:6","/gpu:7"])
    
    minsu = glob.glob('./preprocess/videoimage/*.png') #동영상 데이터 부분. 수정예정
    test = []
    for _ in range(0,80):
      img = cv2.imread(minsu[_])
      img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      test.append(img.astype("float32")/255.0)

    img = cv2.imread('./preprocess/faceimg.png')
    img = (cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    test.append(img.astype("float32")/255.0)
    test.append(img.astype("float32")/255.0)
    test.append(img.astype("float32")/255.0)
    test.append(img.astype("float32")/255.0)
    test.append(img.astype("float32")/255.0)

    val = []
    val.append(test[-1])
    test = np.array(test)
    val = np.array(val)
    np.random.shuffle(test)
    
    with strategy.scope():
        ae_model = load_model('./check/model3.h5') #배치정규화x + 300회 학습 모델
    ae_model.compile(optimizer=keras.optimizers.Adam(1e-5),loss='mean_squared_error', metrics=['acc'])
    
    #모델 체크포인트 설정
    checkpoint_path = 'checkpoint.ckpt'
    checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                save_weights_only = True,
                                                save_best_only = True,
                                                monitor='val_acc',
                                                verbose=1)
    #학습
    history = ae_model.fit(test,
                           test,
                           batch_size=5, 
                           epochs=50,
                           validation_data=(val, val),                                                        
                           callbacks=[checkpoint])  #모델 체크포인트 저장
    
    trans_imgs = ae_model.predict(val)
    cv2.imwrite('encode.jpg', cv2.cvtColor(trans_imgs[0]*255, cv2.COLOR_BGR2RGB))

def processing():
    detector = dlib.get_frontal_face_detector()
    pred = "./preprocess/shape_predictor_68_face_landmarks.dat"
    predictor = dlib.shape_predictor(pred)
    
    extract_image_one_fps('./preprocess/video.mp4',detector)

    img_path = "./preprocess/mask.jpg"  #마스크 낀 사진
    image = cv2.imread(img_path)
    #cv2_imshow(image)

    img_path2 = "./preprocess/original.png"  #마스크 안낀 사진
    image2 = cv2.imread(img_path2)

    landmark1 = np.empty((68,2),int)
    landmark2 = np.empty((68,2),int)

    landmark1 = faceDetection(image, detector, predictor)
    landmark2 = faceDetection(image2, detector, predictor)

    image2 = coloring(image,image2,landmark1,landmark2)
    show_mask = extractMask(landmark2, image2)
    show_mask,r = rotate(show_mask, landmark1[36],landmark1[45],landmark2[36], landmark2[45])

    if(r == "right"):
      merged_img, show_mask = func(landmark1[40][1],landmark1[0][0], show_mask, image, landmark1, landmark2, r)
    else:
      merged_img, show_mask = func(landmark1[40][1],landmark1[16][0], show_mask, image, landmark1, landmark2, r)
    
    #cv2.imshow(merged_img)
    face_img, xy_list = output(merged_img,detector)
    cv2.imwrite("./preprocess/faceimg.png",face_img)

    synthesis()
    
    img_encoded = cv2.imread("encode.jpg")
    merged_img = replace(merged_img, img_encoded, xy_list)
    cv2.imwrite("./preprocess/result.png",merged_img)

processing()




