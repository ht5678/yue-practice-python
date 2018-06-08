
import cv2



def histAndBackProjection(pos , hue):
    cv2.calcHist(hue,[1],None,pos,[0,180]);
    cv2.normalize(hue,hue,0,1,cv2.NORM_MINMAX,-1,None);

    hue = cv2.calcBackProject([hue],1,0,[0,180],(0,255,255));


    cv2.imshow('test', hue);
    cv2.waitKey(0);
    return;

if __name__ == '__main__':
    src = cv2.imread("d://pics//151515.jpg");

    windowImage = 'inputImage';
    cv2.namedWindow( windowImage, cv2.WINDOW_NORMAL);
    # cv2.namedWindow('backProject', cv2.WINDOW_NORMAL);
    # cv2.namedWindow('histogram', cv2.WINDOW_NORMAL);


    hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV);
    hue = hsv;
    nChannels = [0,0];
    cv2.mixChannels(hsv , hue , nChannels);

    cv2.createTrackbar('HistogramBins' , windowImage,0 , 180 , histAndBackProjection)
    histAndBackProjection(0 , hue);


    cv2.imshow(windowImage,src);
    cv2.waitKey(0);



