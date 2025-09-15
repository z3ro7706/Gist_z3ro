#include <iostream>
using namespace std;

// define the pi
const double pi = 3.14159;

// calculate rectangle Afrea
inline double rectangleArea(double weidth, double height)
{
    return weidth * height;
}

inline double circleArea(double radius)
{
    return pi * radius * radius;
}

int main()
{
    double weight, height, radius;

    cout << "Enter the width of the rectangle : ";
    cin >> weight;
    cout << "Enter the height of the rectangle : ";
    cin >> height;
    cout << "Enter the radius of the circle : ";
    cin >> radius;

    double Rectangle_Area = rectangleArea(weight, height);
    double Circle_area = circleArea(radius);
    cout << "Rectangle ARea :  " << Rectangle_Area << endl;
    cout << "Circle area : " << Circle_area << endl;

    return 0;
}