#
#反向投影:
#
#*反向投影是反应直方图模型在目标图像中的分布情况
#*简单点说就是用直方图模型去目标图像中寻找是否有相似的对象 . 通常用HSV色彩空间的HS两个通道直方图模型
#
#步骤:
#*建立直方图模型
#*计算机待测图像直方图并映射到模型中
#*从模型反向计算生成图像
#
#
#
#相关API:
#*加载图片imread
#*将图像从RGB色彩空间转换到HSV色彩空间  cvtColor
#*计算直方图和归一化 calcHist与normalize
#*Mat和MatND其中Mat表示二维数组 , MatND表示三维或者多维数据 , 此处均可以用Mat表示
#*计算反向投影图像  calcBackProject
#
#
#
#
#
#
#
#
#



import cv2


src = cv2.imread("d://pics//212121.jpg");

windowImage = 'inputImage';
cv2.namedWindow( windowImage, cv2.WINDOW_NORMAL);
cv2.namedWindow('backProject', cv2.WINDOW_NORMAL);
# cv2.namedWindow('histogram', cv2.WINDOW_NORMAL);


hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV);
nChannels = [0,0];
cv2.mixChannels(hsv , hsv , nChannels);
hue=hsv;
bins=12;

cv2.imshow(windowImage,src);

histBase = cv2.calcHist([hsv],[0],None,[bins],[0,180]);
cv2.normalize(hsv,hue,0,256,cv2.NORM_MINMAX,-1,None);
hue = cv2.calcBackProject([hue],[0],0,[0,180],1);



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

#bins:起始值 , 180:最大值
# cv2.createTrackbar('HistogramBins' , windowImage,bins , 180 , histAndBackProjection)
# histAndBackProjection(0 , 0);


cv2.imshow('backProject',hue);
cv2.waitKey(0);
