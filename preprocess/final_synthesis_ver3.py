from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import math


# 얼굴 Detection 및 Landmark 생성
def faceDetection(img, detector, predictor):
  #h, w, ch = img.shape
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  rects = detector(gray,1)
  roi = rects[0]
  shape = predictor(gray, roi)
  shape = face_utils.shape_to_np(shape)
  return shape


#마스크부분 추출
def extractMask(landmark, img):
  h, w, ch = img.shape
  # extract jawline
  jawline = landmark[0:17]
  temp_face = landmark[1:16]
  lefteye = landmark[36:42]
  righteye = landmark[42:48]

  nose = landmark[27][1]

  top = nose
  bottom = max(jawline[:,1])
  side1 = min(jawline[:,0])
  side2 = max(jawline[:,0])
  side = side2-side1

  lefteyeline = max(lefteye[:,1])
  righteyeline = max(righteye[:,1])

  temp_face = np.insert(temp_face,0,[landmark[0][0],landmark[40][1]]).reshape(-1,2)
  temp_face = np.append(temp_face,[landmark[16][0],landmark[47][1]]).reshape(-1,2)
  # extend contour for masking
  jawline = np.append(jawline, [landmark[47][0],landmark[47][1]]).reshape(-1,2)
  temp_face = np.append(temp_face, [landmark[47][0],landmark[47][1]]).reshape(-1,2)
  jawline = np.append(jawline, [landmark[27][0],landmark[27][1]]).reshape(-1,2)
  temp_face = np.append(temp_face, [landmark[27][0],landmark[27][1]]).reshape(-1,2)
  jawline = np.append(jawline, [ w-1, nose]).reshape(-1,2)
  temp_face = np.append(temp_face, [w-1,nose]).reshape(-1,2)
  jawline = np.append(jawline, [ w-1, h-1 ]).reshape(-1, 2)
  temp_face = np.append(temp_face,[w-1,h-1]).reshape(-1,2)
  jawline = np.append(jawline, [ 0, h-1 ]).reshape(-1, 2)
  temp_face = np.append(temp_face,[0,h-1]).reshape(-1,2)
  jawline = np.append(jawline, [0, nose]).reshape(-1,2)
  temp_face = np.append(temp_face,[0,nose]).reshape(-1,2)
  jawline = np.append(jawline, [landmark[27][0],landmark[27][1]]).reshape(-1,2)
  temp_face = np.append(temp_face,[landmark[27][0],landmark[27][1]]).reshape(-1,2)
  jawline = np.append(jawline, [landmark[40][0],landmark[40][1]]).reshape(-1,2)
  temp_face = np.append(temp_face, [landmark[40][0],landmark[40][1]]).reshape(-1,2)
  jawline = np.append(jawline, [landmark[0][0], landmark[0][1] ]).reshape(-1, 2)
  temp_face = np.append(temp_face, [landmark[0][0], landmark[40][1]]).reshape(-1,2)
  contours = [jawline]
  temp_contours = [temp_face]

  # generate mask
  mask = np.ones((h,w,1), np.uint8) * 255 # times 255 to make mask 'showable'
  
  #cv2.drawContours(mask, contours, -1, 0, -1) # remove below jawline
  cv2.drawContours(mask, temp_contours, -1,0,-1)
  

  # apply to image
  result = cv2.bitwise_and(img, img, mask = mask)

  b,g,r = img[landmark[27][1],landmark[27][0]]
  result = result[nose:bottom, side1:side2] # crop ROI
  return result



def coloring(img, img2):
  img_c = cv2.cvtColor(face_img, cv2.COLOR_BGR2HSV)  
  img2_c = cv2.cvtColor(result, cv2.COLOR_BGR2HSV)

  lower = np.array([0,48,80], dtype = "uint8")
  upper = np.array([20,255,255], dtype = "uint8")
  skin_msk = cv2.inRange(img_c, lower, upper)	
  skin_msk2 = cv2.inRange(img2_c, lower, upper)
  skin1 = cv2.bitwise_and(img, img, mask = skin_msk)
  skin2 = cv2.bitwise_and(img2, img2, mask = skin_msk2)

  height, width, channel = skin1.shape
  tmp = 0
  black = 0
  b1 = 0
  g1 = 0
  r1 = 0

  for y in range(0, height):
    for x in range(0, width):
      b = skin1.item(y,x,0)
      g = skin1.item(y,x,1)
      r = skin1.item(y,x,2)

      if(b == 0 and g == 0 and r==0):
        black +=1
      else:
        tmp +=1
      b1 = b1+ b
      g1 = g1+ g
      r1 = r1+ r

  height2, width2, channel2 = skin2.shape
  tmp2 = 0
  black = 0
  b2 = 0
  g2 = 0
  r2 = 0

  for y in range(0, height2):
    for x in range(0, width2):
      b = skin2.item(y,x,0)
      g = skin2.item(y,x,1)
      r = skin2.item(y,x,2)

      if(b == 0 and g == 0 and r==0):
         black +=1
      else:
          tmp2 +=1
      b2 = b2+ b
      g2 = g2+ g
      r2 = r2+ r


  b1 = b1/tmp
  g1 = g1/tmp
  r1 = r1/tmp
  b2 = b2/tmp2
  r2 = r2/tmp2
  g2 = g2/tmp2

  b_gap = b1-b2
  g_gap = g1-g2
  r_gap = r1-r2
  
  M = np.ones(skin2.shape, dtype = "uint8") * (int)(min(abs(b_gap), abs(g_gap), abs(r_gap)))
  
  if b_gap+g_gap+r_gap <0:
    img2 = cv2.subtract(img2, M)
  else:
    img2 = cv2.add(img2, M)
  return img2

def rotate(img,p1,p2,p3,p4):
  w,h = img.shape[:2]

  tan1 = math.atan2(p1[1]-p2[1],p1[0]-p2[0])
  res1 = tan1 * 180 / math.pi

  tan2 = math.atan2(p3[1]-p4[1],p3[0]-p4[0])
  res2 = tan2 * 180 / math.pi

  if(res1<0): #오른쪽으로 돌아간 사진
    handle = "right"
  else:
    handle = "left"
  #cp = (img.shape[1]/2, img.shape[0]/2)
  if(handle == "right"):
    rot = cv2.getRotationMatrix2D((0,0), res2-res1,1)
  else:
    rot = cv2.getRotationMatrix2D((w,0), res2-res1,1)
  img = cv2.warpAffine(img, rot, (0, 0)) 
  return img, handle

    
# 두 이미지 합하기, img_mask : 마스크부분만 자른 이미지, img : 마스크낀 이미지 landmark_1 : 마스크를 낀 사진의 landmark, landmark2 : 마스크를 안낀 사진의 landmark
def func(hpos, vpos, img_mask, img, landmark_1, landmark_2, handle):
  x1 = landmark_1[0][0] - landmark_1[16][0]
  y1 = landmark_1[0][1] - landmark_1[16][1]
  c = math.sqrt((x1**2)+(y1**2))

  x2 = landmark_2[0][0] - landmark_2[16][0]
  y2 = landmark_2[0][1] - landmark_2[16][1]
  c2 = math.sqrt((x2**2)+(y2**2))
  size_w = c/c2

  x3 = landmark_1[27][0] - landmark_1[8][0]
  y3 = landmark_1[27][1] - landmark_1[8][1]
  c3 = math.sqrt((x3**2)+(y3**2))

  x4 = landmark_2[27][0] - landmark_2[8][0]
  y4 = landmark_2[27][1] - landmark_2[8][1]
  c4 = math.sqrt((x4**2)+(y4**2))
  size_h = c3/c4
  
  src = img_mask
  #cv2_imshow(src)
  src = cv2.resize(src, dsize=(0,0), fx =size_w, fy= size_h, interpolation = cv2.INTER_LINEAR)
  rows, cols, channels = src.shape
  if handle=="right":
    roi = img[hpos:rows+hpos,vpos:cols+vpos]
  else:
    roi = img[hpos:rows+hpos,vpos-cols:vpos]
  
  background = np.ones((rows,cols,3), np.uint8)*0
  gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
  ret, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
  mask_inv = cv2.bitwise_not(mask)

  src_s = cv2.resize(src, dsize=(0,0), fx = 0.985, fy = 0.985, interpolation = cv2.INTER_LINEAR)
  row2, col2, ch2 = src_s.shape
  y = (int)((rows - row2)/2)
  x = (int)((cols -col2)/2)
  background[y:y+row2, x:x+col2] = src_s

  gray_s = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
  r, mask_s = cv2.threshold(gray_s, 0, 255, cv2.THRESH_BINARY)
  mask_inv = cv2.bitwise_not(mask_s)

  
  img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
  src_fg = cv2.bitwise_and(src, src, mask=mask_s)
  tmp = cv2.addWeighted(img_bg, 1, src_fg, 1,0)
  tmp = cv2.medianBlur(tmp,7)
  if handle == "right":
    img[hpos:rows+hpos, vpos:cols+vpos] = tmp
  else:
    img[hpos:rows+hpos, vpos-cols:vpos] = tmp
  return img, tmp


def output(img, detector):
    image = img
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    for i in rects:
        x1 = i.left()
        x2 = i.right()
        y1 = i.top()
        y2 = i.bottom()
    tmp = image[y1:y2, x1:x2]
    tmp = cv2.resize(tmp, dsize=(800, 800), interpolation=cv2.INTER_AREA)
    #cv2_imshow(tmp)
    list_xy = [x1,x2,y1,y2]
    return tmp,list_xy


#2차 합성
def replace(img, eimg,list_ab):
  h1, w1, ch1 = eimg.shape
  h = (list_ab[3]-list_ab[2])/h1
  w = (list_ab[1]-list_ab[0])/w1
  eimg = cv2.resize(eimg, dsize=(0,0),fx=w,fy=h, interpolation = cv2.INTER_LINEAR)
  #cv2_imshow(eimg)
  img[list_ab[2]:list_ab[3], list_ab[0]:list_ab[1]] = eimg
  return img


def main():
    detector = dlib.get_frontal_face_detector()
    pred = "shape_predictor_68_face_landmarks.dat"
    predictor = dlib.shape_predictor(pred)

    img_path = "mask.jpg"  #마스크 낀 사진
    image = cv2.imread(img_path)
    #cv2_imshow(image)

    img_path2 = "original.png"  #마스크 안낀 사진
    image2 = cv2.imread(img_path2)

    landmark1 = np.empty((68,2),int)
    landmark2 = np.empty((68,2),int)

    landmark1 = faceDetection(image, detector, predictor)
    landmark2 = faceDetection(image2, detector, predictor)

    image2 = coloring(image,image2)
    show_mask = extractMask(landmark2, image2)
    show_mask,r = rotate(show_mask, landmark1[36],landmark1[45],landmark2[36], landmark2[45])

    if(r == "right"):
      merged_img, show_mask = func(landmark1[40][1],landmark1[0][0], show_mask, image, landmark1, landmark2, r)
    else:
      merged_img, show_mask = func(landmark1[40][1],landmark1[16][0], show_mask, image, landmark1, landmark2, r)

    face_img, xy_list = output(merged_img)
    cv2.imwrite("faceimg.png",face_img)

    img_encoded = cv2.imread("encode.jpg")
    merged_img = replace(merged_img, img_encoded, xy_list)
    cv2.imwrite("result.png",merged_img)

if __name__ == '__main__':
    main()
