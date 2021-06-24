import cv2;
import numpy as np;

def detect_contour(img_dir):

    im_in = cv2.imread(img_dir, cv2.IMREAD_GRAYSCALE);

    th, im_th = cv2.threshold(im_in, 200, 255, cv2.THRESH_BINARY_INV);

    contours, hierarchy = cv2.findContours(im_th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    image = cv2.drawContours(im_in, contours, -1, (0, 255, 0), 2)

    return image

image = detect_contour('D:\src\y_pred\TCGA_CS_5396_20010302_13.jpg')    
cv2.imshow("img",image)
#cv2.imwrite("post_processing.jpg", image)

cv2.waitKey(0)