#include <iostream>
#include <fstream>
using namespace std;

class Point
{
private:
    int x, y, z;

public:
    Point(int x, int y, int z) : x(x), y(y), z(z) {}
    friend ostream &operator<<(ostream &os, const Point &p)
    {
        os << "(" << p.x << "," << p.y << "," << p.z << ")";
        return os;
    }
};

int main()
{
    ofstream of("Out.txt");
    Point p1(1, 2, 3);
    Point p2(4, 5, 6);
    cout << p1 << "~" << p2 << endl;
    of << p1 << "~" << p2 << endl;
}