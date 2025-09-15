#ifndef RECTANGLE_H
#define RECTANGLE_H

#include <string>
using namespace std;

class rectangle
{
    int width;
    int height;

public:
    rectangle();                      // 고정값
    rectangle(int width, int height); // 받는값
    int getArea();
    void ShowInfo();
};

#endif
