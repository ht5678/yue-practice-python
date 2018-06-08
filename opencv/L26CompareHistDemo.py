# /**
#  *
#  * 直方图比较方法:
#  * 对输入的两张图像计算得到的直方图H1和H2,归一化到相同的尺度空间,
#  * 然后可以通过计算H1和H2之间的距离得到两个直方图的相似程度进而
#  * 比较图像本身的相似程度.opencv提供的比较方法有4中,
#  * -Correlation  相关性比较						***计算结果越大,相似度越高
#  * -Chi-Square	卡方比较
#  * -Intersection	 十字交叉性
#  * -Bhattacharyya distance 巴氏距离		***计算结果越小,相似度越高  ,  效果比较好
#  *
#  *
#  * 步骤:
#  * *首先把图像从RGB色彩空间转换到HSV色彩空间cvtColor
#  * *计算图像的直方图,然后归一化到[0~1]之间calcHist和normalize
#  * *使用上述四种比较方法之一进行比较compareHist
#  *
#  *
#  * compareHist:
#  * -InputArray h1 , //直方图数据 , 下同
#  * -InputArray h2,	//
#  * -int method,		//比较方法,上述四种方法之一
#  *
#  *
#  * @author sdwhy
#  *
#  */



import cv2

# print(cv2.__version__)


if __name__ == '__main__':
    src = cv2.imread("d://pics/131313.jpg");
    src1 = cv2.imread("d://pics/121212.jpg");

    src=cv2.cvtColor(src, cv2.COLOR_BGR2HSV);
    src1 = cv2.cvtColor(src1, cv2.COLOR_BGR2HSV);

    channels = [0,1];
    hRanges = [0, 180];
    sRanges = [0, 256];
    ranges = [hRanges, sRanges];
    histSize = [180,256];


    histBase = cv2.calcHist([src], channels, None, histSize, [0, 180,0,256]);
    cv2.normalize(histBase, histBase, 0, 1, cv2.NORM_MINMAX, -1, None);

    histBase1 = cv2.calcHist([src1], channels, None, histSize, [0, 180, 0, 256]);
    cv2.normalize(histBase1, histBase1, 0, 1, cv2.NORM_MINMAX, -1, None);

    basebase = cv2.compareHist(histBase, histBase1, cv2.HISTCMP_CORREL);

    print(basebase);

    img = cv2.putText(src, str(basebase), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1.2, (0, 0, 255), 2, cv2.LINE_AA, False);

    cv2.imshow("test", img);
    cv2.waitKey(0);


