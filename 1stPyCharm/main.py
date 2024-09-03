import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#writer object is created
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while True:
    ret, frame = cap.read()
    out.write(frame)

    img_gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("webcam",img_gray)

    #print(ret)

    if cv2.waitKey(1) & 0xFF==ord('x'):
        break

out.release()
cv2.destroyAllWindows()










# flag=False
# ix=-1
# iy=-1
#
# def crop(event,x,y,flags,params):
#     global flag,ix,iy
#
#     if event==1:
#         flag=True
#         ix=x
#         iy=y
#
#     elif event==4:
#         fx = x
#         fy = y
#
#         flag=False
#         cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), thickness=1, color=(0, 0, 0))
#         cropped = img[iy:fy,ix:fx]
#         cv2.imshow("new_window",cropped)
#         cv2.waitKey(0)
#
#
# img = cv2.imread("img/aeroplane.jpg")
#
# cv2.namedWindow(winname='window')
# cv2.setMouseCallback('window',crop)
#
# while True:
#     cv2.imshow("window",img)
#
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break











# def draw(event,x,y,flags,params):
#     if(event==1):
#         cv2.circle(img,center=(x,y),radius=50,color=(0,0,255),thickness=-1)
#
# cv2.namedWindow(winname="window")
# cv2.setMouseCallback('window',draw)
#
# img = np.zeros((512,512,3))
#
# while True:
#
#     cv2.imshow("window",img)
#
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break







# img = np.zeros((512,512,3))
#
# cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=-1)
# cv2.circle(img, center=(100,400), radius=50, color=(0,0,255),thickness=3)
# cv2.line(img, pt1=(0,0),pt2=(512,512), thickness=5, color=(0,255,0))
# cv2.putText(img,org=(100,100),fontScale=4, color=(0,255,255), thickness=2,lineType=cv2.LINE_AA, text="Hello", fontFace=cv2.FONT_ITALIC)
#
# cv2.imshow("window",img)
# cv2.waitKey(0)







# img= cv2.imread("img/fruits.jpeg")
# # print(type(img))
# # print(img.shape)
#
# # cv2.imshow('window',img)
# # cv2.waitKey(0)
#
# #img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # cv2.imshow('window',img_gray)
# # cv2.waitKey(0)
# # print(img_gray.shape)
#
# # imgBlue = img[:,:,0]
# # imgGreen = img[:,:,1]
# # imgRed = img[:,:,2]
#
# # new_img = np.hstack((imgBlue, imgGreen, imgRed))
#
# #img_resize = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
#
# #img_flip = cv2.flip(img,-1)
#
# img_crop = img[0:150,0:150]
# cv2.imwrite("img/fruits_cropped.png", img_crop)
#
# cv2.imshow("window",img_crop)
# cv2.waitKey(0)




