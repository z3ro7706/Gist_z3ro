#include <iostream>
using namespace std;

class Rectangle
{
private:
    int width;
    int height;

public:
    Rectangle(int w, int h)
    {
        width = w;
        height = h;
    }

    int area() const
    {
        int area;
        area = width * height;
        return area;
    }

    friend void compareArea(const Rectangle &r1, const Rectangle &r2);
};

void compareArea(const Rectangle &r1, const Rectangle &r2)
{
    int area1 = r1.area();
    int area2 = r2.area();

    if (area1 > area2)
    {
        cout << "The first rectangle is larger" << endl;
    }
    else if (area1 < area2)
    {
        cout << "The second rectangle is larger." << endl;
    }
    else
    {
        cout << "Both rectangles have the smae area." << endl;
    }
}

int main()
{
    int w1, w2, h1, h2;

    cout << "Enter width and height of the first rectangle : ";
    cin >> w1 >> h1;

    cout << "Enter widht and height of the second rectangle : ";
    cin >> w2 >> h2;

    Rectangle shape1(w1, h1);
    Rectangle shape2(w2, h2);

    compareArea(shape1, shape2);
    return 0;
}