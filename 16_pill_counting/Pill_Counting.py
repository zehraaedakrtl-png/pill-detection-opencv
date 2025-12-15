import cv2
import numpy as np
import os
os.makedirs("output", exist_ok=True)

#1. Load/Read image
image = cv2.imread("input/sample.jpg")


#2.  Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


#3. Reduce noise
gb = cv2.GaussianBlur(gray, ksize = (5,5), sigmaX = 0)


#4. Apply thresholding
_, thresh_img = cv2.threshold(gb, thresh = 0, maxval = 255, type = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#5. Find contours
contours, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#6. Area thresholds (empirically determined)
min_area = 3000
max_area = 120000

pill_count = 0

for cnt in contours:
    area = cv2.contourArea(cnt)


    if min_area < area < max_area:
        pill_count += 1
        cv2.drawContours(image, [cnt], -1, (0,255,0), 2)

expected_count = 4

status = "PASS" if pill_count == expected_count else "FAIL"

cv2.putText(
    image,
    f"Count: {pill_count} | Status: {status}",
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0) if status == "PASS" else (0, 0, 255),
    2)

cv2.imwrite("output/result.jpg", image)



 
