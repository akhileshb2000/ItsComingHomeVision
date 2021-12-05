import cv2
import numpy as np 

def nothing(x):
    # any operation
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("test")

while True:
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow("test", frame)

    # ## Color detection 
    # low_red = np.array([0,0,0])
    # high_red = np.array([180, 255,255])
    # mask = cv2.inRange(hsv_frame, low_red, high_red)
    # kernel = np.ones((5, 5), np.uint8)
    # mask = cv2.erode(mask, kernel)

    # cv2.imshow("Frame", frame)
    # cv2.imshow("Mask", mask )
    # ## Find contours 
    # contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # ## Detect shapes 
    # area = cv2.contourArea(cnt)
    # approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
    # x = approx.ravel()[0]
    # y = approx.ravel()[1]

    # ## Shape detection 
    # if area > 400:
    #     cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
    #     if len(approx) == 3:
    #         cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
    #     elif len(approx) == 4:
    #         cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
    #     elif 10 < len(approx) < 20:
    #         cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))

cam.release()
cv2.destroyAllWindows()