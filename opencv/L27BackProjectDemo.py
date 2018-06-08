
import cv2

if __name__ == '__main__':
    src = cv2.imread("d://pics//151515.jpg");

    windowImage = 'inputImage';
    cv2.namedWindow( windowImage, cv2.CV_WINDOW_NORMAL);
    cv2.namedWindow('backProject', cv2.CV_WINDOW_NORMAL);
    cv2.namedWindow('histogram', cv2.CV_WINDOW_NORMAL);


    hsv = cv2.cvtColor(src,cv2.CV_BGR2HSV);
    hue = hsv;
    nChannels = [0,0];
    cv2.mixChannels(hsv , hue , nChannels);

    cv2.createTrackbar('HistogramBins' , windowImage,[50] , 180 , )



    cv2.imshow('test',src);
    cv2.waitKey(0);



def histAndBackProjection():
    cv2.calcHist()