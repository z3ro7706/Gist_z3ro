#include <iostream>
using namespace std;

const double PI = 3.141592;

inline int Square(int a)
{
    int Area;
    Area = a * a;
    return Area;
}

inline float Rectangle(int width, int height)
{
    float Area;
    Area = width * height;
    return Area;
}

inline float Circle(int radius)
{
    float Area;
    Area = PI * radius * radius;
    return Area;
}

int main()
{
    int a, b, c, d, e;
    cout << "Choose a shape to calculae the area : " << endl;
    cout << "1. Square " << endl;
    cout << "2. Rectangle " << endl;
    cout << "3. Circle " << endl;
    cout << "Enter your Choice (1~3) :  ";
    cin >> a;
    if (a == 1)
    {
        cout << "Enter the side length of the square :  ";
        cin >> b;
        cout << "Square area (side = " << b << " ) : " << Square(b) << endl;
        cout << endl;
    }
    else if (a == 2)
    {
        cout << "Enter the wideth and height of the rectangle :  ";
        cin >> c >> d;
        cout << "Rectangle Area (width = " << c << " , height = " << d << " ) : " << Rectangle(c, d) << endl;
        cout << endl;
    }
    else if (a == 3)
    {
        cout << "Enter the radius of the rectangle :  ";
        cin >> e;
        cout << "Circle area (radius =" << e << " ) : " << Circle(e) << endl;
        cout << endl;
    }
    else
    {
        cout << "Invalid choice. Plase enter a number between 1 and 3." << endl;
        cout << endl;
    }
}
