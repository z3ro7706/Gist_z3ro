#include <iostream>
using namespace std;

int sum(int a, int b)
{
    return a + b;
}

int sum(int a, int b, int c)
{
    return a + b + c;
}

int sum(int a, int b, int c, int d)
{
    return a + b + c + d;
}

int main()
{
    cout << "sum(10, 15) = " << sum(10, 15) << endl;
    cout << "sum(10, 15, 25) = " << sum(10, 15, 25) << endl;
    cout << "sum(10, 15, 25, 30) = " << sum(10, 15, 25, 30) << endl;
    return 0;
}