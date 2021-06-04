from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import math

#detector = dlib.get_frontal_face_detector()

def extract_image_one_fps(video_source_path,detector):
    vidcap = cv2.VideoCapture(video_source_path)
    count = 0
    real_count = 0
    success = True
    while success:
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*64))
      success,image = vidcap.read()
      #image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
      
      
      if real_count == 0:
        cv2.imwrite("./preprocess/original.png",image)

      ## Stop when last frame is identified
      image_last = cv2.imread("frame{}.png".format(real_count-1))
      if np.array_equal(image,image_last):
          break

      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      rects = detector(gray, 1)

      try:  #검출에 성공시,
        roi = rects[0]
        
      except: #검출 실패시, img 번호 출력
        print(f"Error!! Passing the image")
        count += 1
        continue
        

      (x, y, w, h) = face_utils.rect_to_bb(roi)
      image = image[y:y+h,x:x+w]
      if image.shape[1] == 0:
        count+=1
        continue
      #if(real_count > 32):
        #cv2_imshow(image)
      image = cv2.resize(image,(800,800))
      cv2.imwrite("./preprocess/videoimage/frame%d.png" % real_count, image)     # save frame as PNG file
      print('{}.sec reading a new frame: {} '.format(real_count,success))
      real_count += 1
      count += 1

#extract_image_one_fps('/gdrive/My Drive/video4.mp4')