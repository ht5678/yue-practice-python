import cv2

def histAndBackProjection(pos):
    print(pos)




cv2.namedWindow('test')
cv2.createTrackbar('thrs1', 'test', 300, 800, histAndBackProjection)

# Do whatever you want with contours
cv2.imshow('test',cv2.imread("d://pics//151515.jpg"))
cv2.waitKey(0)


