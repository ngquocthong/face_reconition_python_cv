import numpy as np
import cv2
import face_recognition

imgThongBig = face_recognition.load_image_file('ImageBasic/Quoc Thong Big.jpg');
imgThongBig = cv2.cvtColor(imgThongBig,cv2.COLOR_BGR2RGB);

imgThongTest = face_recognition.load_image_file('ImageBasic/Quoc Thong Test.jpg');
imgThongTest = cv2.cvtColor(imgThongTest,cv2.COLOR_BGR2RGB);

faceLoc = face

cv2.imshow('Thong Big', imgThongBig);
cv2.imshow('Thong Test', imgThongTest);
cv2.waitKey(0);