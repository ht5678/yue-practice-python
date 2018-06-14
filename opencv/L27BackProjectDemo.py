
import cv2


src = cv2.imread("d://pics//151515.jpg");

windowImage = 'inputImage';
cv2.namedWindow( windowImage, cv2.WINDOW_NORMAL);
# cv2.namedWindow('backProject', cv2.WINDOW_NORMAL);
# cv2.namedWindow('histogram', cv2.WINDOW_NORMAL);


hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV);
nChannels = [0,1];
cv2.mixChannels(hsv , hsv , nChannels);
hue=hsv;

histBase = cv2.calcHist([hsv],[1],None,[180],[0,180]);
cv2.normalize(hsv,hue,0,255,cv2.NORM_MINMAX,-1,None);
hue = cv2.calcBackProject([hsv],[1],0,[0,180],1);



# def histAndBackProjection(pos , tmp):
#     cv2.calcHist(hue,[1],None,pos,[0,180]);
#     cv2.normalize(hue,hue,0,1,cv2.NORM_MINMAX,-1,None);
#
#     hue = cv2.calcBackProject([hue],1,0,[0,180],(0,255,255));
#
#
#     cv2.imshow('test', hue);
#     cv2.waitKey(0);
#     return;


# cv2.createTrackbar('HistogramBins' , windowImage,0 , 180 , histAndBackProjection)
# histAndBackProjection(0 , 0);


cv2.imshow(windowImage,hue);
cv2.waitKey(0);
