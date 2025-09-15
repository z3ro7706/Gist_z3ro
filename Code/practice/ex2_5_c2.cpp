#include <iostream>
using namespace std;

int sum(int a, int b)
{
    int i, sum;
    sum = 0;
    for (i = a; i <= b; i++)
    {
        sum = sum + i;
    }
    return sum;
}

int sum(int a)
{
    int i, sum;
    sum = 0;
    for (i = 0; i <= a; i++)
    {
        sum = sum + i;
    }
    return sum;
}

int main()
{
    cout << sum(3, 5) << endl;
    cout << sum(3) << endl;
    cout << sum(100) << endl;
}