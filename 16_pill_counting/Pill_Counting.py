import cv2
import numpy as np


#1. Görüntüyü okuyalım
image = cv2.imread("sample.jpg")


#2. Görüntüyü gri tonlamaya çevirelim
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


#3. Gürültü azaltalım (hap kenarları yumuşatma)
gb = cv2.GaussianBlur(gray, ksize = (5,5), sigmaX = 0)


#4. Threshold uygulayalım
_, thresh_img = cv2.threshold(gb, thresh = 0, maxval = 255, type = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#5. Kontürleri bulalım
contours, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#6. Alan filtreleme ile hapları ayıklayalım 
min_area = 3000
max_area = 120000

pill_count = 0

for cnt in contours:
    area = cv2.contourArea(cnt)


    if min_area < area < max_area:
        pill_count += 1

        #Hap kontorunu çizelim
        cv2.drawContours(image, [cnt], -1, (0,255,0), 2)

print("Detected Pills:", pill_count)
    
 


 