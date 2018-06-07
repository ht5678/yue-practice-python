import cv2

# print(cv2.__version__)


if __name__ == '__main__':
    src = cv2.imread("d://pics/131313.jpg");

    src=cv2.cvtColor(src, cv2.COLOR_BGR2HSV);

    channels = [0];
    hRanges = [0, 180];
    sRanges = [0, 256];
    ranges = [hRanges, sRanges];
    histSize = [50];

    print(ranges);

    histBase = cv2.calcHist([src], channels, None, histSize, [0, 256]);
    cv2.normalize(histBase, histBase, 0, 1, cv2.NORM_MINMAX, -1, None);
    basebase = cv2.compareHist(histBase, histBase, cv2.HISTCMP_CORREL);

    img = cv2.putText(histBase, str(basebase), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1.2, (0, 0, 255), 2, cv2.LINE_AA, False);

    cv2.imshow("test", img);
    cv2.waitKey(0);
