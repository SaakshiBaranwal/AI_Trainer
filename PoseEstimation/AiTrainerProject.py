# import cv2
# import numpy as np
# import time
# import PoseModule as pm
#
# cap = cv2.VideoCapture("curls.mp4")
#
# detector = pm.poseDetector()
# count = 0
# # 0->up 1->down
# dir = 0
#
# while True:
#     success, img =cap.read()
#     img = cv2.resize(img, (600,720))
#     #img = cv2.imread("img.jpg")
#     img = detector.findPose(img, False)
#     lmList = detector.findPosition(img, False)
#     #print(lmList)
#     if len(lmList) != 0:
#         # # Right arm
#         # detector.findAngle(img,12,14,16)
#         # Left arm
#         angle = detector.findAngle(img, 11, 13, 15)
#         per = np.interp(angle, (225,340), (0,100))
#         #print(angle, per)
#
#         #Check for the dumbell curls
#         if per==100:
#             if dir==0:
#                 count+=0.5
#                 dir=1
#         if per==0:
#             if dir==1:
#                 count+=0.5
#                 dir=0
#         print(count)
#
#         cv2.putText(img, str(int(count)), (50,100), cv2.FONT_HERSHEY_PLAIN,4,(255,0,0), 5)
#
#     cv2.imshow("image", img)
#     cv2.waitKey(1)


import cv2
import numpy as np
import PoseModule as pm

cap = cv2.VideoCapture(0)  # Use 0 for webcam

detector = pm.poseDetector()
count = 0
# 0->up 1->down
dir = 0

while True:
    success, img = cap.read()
    img = cv2.resize(img, (600, 720))

    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)

    if len(lmList) != 0:
        # Left arm
        angle = detector.findAngle(img, 11, 13, 15)
        per = np.interp(angle, (225, 340), (0, 100))

        # Check for the dumbbell curls
        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)

        cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 5)

    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

