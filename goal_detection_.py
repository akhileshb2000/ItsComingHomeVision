import cv2
import numpy as np

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

def nothing(x):
    # any op
    pass

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 0, 180, nothing)
# cv2.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
# cv2.createTrackbar("L-V", "Trackbars", 0, 255, nothing)
# cv2.createTrackbar("U-H", "Trackbars", 0, 180, nothing)
# cv2.createTrackbar("U-S", "Trackbars", 0, 255, nothing)
# cv2.createTrackbar("U-V", "Trackbars", 0, 255, nothing)

while True:
    ret, frame = cam.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos("L-H", "Trackbars")

    
    ## Color detection 
    low_red = np.array([0, 13, 155])
    high_red = np.array([180, 255, 240])
    mask = cv2.inRange(hsv_frame, low_red, high_red)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)

    # Contours Detection
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        if area > 400:
            cv2.drawContours(frame, [approx], 0, (0,0,0), 5)
            if len(approx)==4:
                print("ITS A RECT")

    if not ret:
        print("failed to grab frame")
        break



    cv2.imshow("test", frame)
    cv2.imshow("Mask", mask)
     

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
