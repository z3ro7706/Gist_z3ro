// this pointer
#include <iostream>
using namespace std;

class Rectangle
{
private:
    int width;
    int height;

public:
    void setDimensions(int width, int height)
    {
        this->width = width;
        this->height = height;
    }

    int area()
    {
        return width * height;
    }

    void show()
    {
        cout << "Width: " << width << ", Height: " << height << ", Area: " << area() << endl;
        cout << endl;
    }
};

int main()
{
    Rectangle rect;
    rect.setDimensions(10, 5);
    rect.show();

    return 0;
}
