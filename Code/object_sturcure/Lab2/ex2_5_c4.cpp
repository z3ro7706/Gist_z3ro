#include <iostream>
using namespace std;

const double PI = 3.141592;

// 사각형
inline int Square(int a)
{
    int Area;
    Area = a * a;
    return Area;
}

// 삼각형
inline float Rectangle(int width, int height)
{
    float Area;
    Area = width * height * 0.5;
    return Area;
}

// 원
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

    if (a == 1) // 사각형
    {
        cout << "Enter the side length of the square :  ";
        cin >> b;
        cout << "Square area (side = " << b << " ) : " << Square(b) << endl;
        cout << endl;
    }
    else if (a == 2) // 삼각형
    {
        cout << "Enter the wideth and height of the rectangle :  ";
        cin >> c >> d;
        cout << "Rectangle Area (width = " << c << " , height = " << d << " ) : " << Rectangle(c, d) << endl;
        cout << endl;
    }
    else if (a == 3) // 원
    {
        cout << "Enter the radius of the Circle :  ";
        cin >> e;
        cout << "Circle area (radius =" << e << " ) : " << Circle(e) << endl;
        cout << endl;
    }
    else // 입력 범위 안에 존재하지 않음
    {
        cout << "Invalid choice. Plase enter a number between 1 and 3." << endl;
        cout << endl;
    }
}
