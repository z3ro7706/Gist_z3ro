#include <iostream>
#include "Rectangle.h"

using namespace std;

rectangle::rectangle() // 디폴트 삼각형
{
    width = 1;
    height = 1;
    cout << "Default constructor called" << endl;
}

rectangle::rectangle(int w, int h)
{
    width = w;
    height = h;
}

int rectangle::getArea()
{
    return width * height;
}

void rectangle::ShowInfo()
{
    cout << "Width : " << width << ", Height : " << height << ", Area : " << getArea() << endl;
}
