#include <opencv2/opencv.hpp>

cv::BackgroundSubtractorMOG2 mog(100, 16, true);

extern "C" void getfg(int rows, int cols, unsigned char* imgData,
        unsigned char *fgD) {
    cv::Mat img(rows, cols, CV_8UC3, (void *) imgData);
    cv::Mat fg(rows, cols, CV_8UC1, fgD);
    mog(img, fg);
}

extern "C" void getbg(int rows, int cols, unsigned char *bgD) {
    cv::Mat bg = cv::Mat(rows, cols, CV_8UC3, bgD);
    mog.getBackgroundImage(bg);
}
