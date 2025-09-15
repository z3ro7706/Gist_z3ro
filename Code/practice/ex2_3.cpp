#include <iostream>
using namespace std;
#define PI 3.14159

inline double rectangleArea(double width, double height)
{
    double Area = width * height;
    return Area;
}

inline double circleArea(double radius)
{
    double Area = PI * radius * radius;
    return Area;
}

int main()
{
    double width, height, radius;
    width = 0;
    height = 0;
    radius = 0;
    cout << "Enter the width of the rectangle : ";
    cin >> width;
    cout << "Enter the height of the rectangle : ";
    cin >> height;
    cout << "Enter the radius of the circle : ";
    cin >> radius;
    cout << "Rectangle area : " << rectangleArea(width, height) << endl;
    cout << "Circle area : " << circleArea(radius) << endl;
    cout << "" << endl;
}