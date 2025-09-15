#include <iostream>
#define PI 3.141592
using namespace std;

int area(int side)
{
    return (side * side);
}
int area(int width, int height)
{
    return width * height;
}
double area(double radius)
{
    return radius * radius * PI;
}
void printArea(int side, int result)
{
    cout << "Square area (side = " << side << ") : " << area(side) << endl;
}
void printArea(int width, int height, int result)
{
    cout << "Rectangle area (height = " << height << ", width =" << width << ") : " << area(width, height) << endl;
}
void printArea(double radius, int result)
{
    cout << "Circle area (radius = " << radius << ") : " << area(radius) << endl;
}

int main()
{
    int n, i, w, h, s;
    double r;
    cout << "Choose a shape to calculate the area : " << endl;
    cout << "1. Square" << endl;
    cout << "2. Rectangle" << endl;
    cout << "3. Circle" << endl;
    cout << "Enter you choice (1-3) : ";
    cin >> n;
    if (n == 1)
    {
        cout << "Enter the side length of the square : ";
        cin >> s;
        printArea(s, n);
        cout << "" << endl;
    }
    else if (n == 2)
    {
        cout << "Enter the width and height of the rectangle : ";
        cin >> w >> h;
        printArea(w, h, n);
        cout << "" << endl;
    }
    else if (n == 3)
    {
        cout << "Enter the side length of the square : ";
        cin >> r;
        printArea(r, n);
        cout << "" << endl;
    }
    else
    {
        cout << "Invlaid chocie. Please enter a nubmer between 1 and 3." << endl;
        cout << "" << endl;
    }
}
