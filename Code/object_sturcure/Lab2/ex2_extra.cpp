#include <iostream>
using namespace std;

// 2개 일때
inline int Sum(int a, int b)
{
    int sum = a + b;
    return sum;
}

// 3개일 때
inline int Sum(int a, int b, int c)
{
    int sum = a + b + c;
    return sum;
}

// 4개일 떄
inline int Sum(int a, int b, int c, int d)
{
    int sum = a + b + c + d;
    return sum;
}

// 출력(메인 함수)
int main()
{
    cout << "sum(10, 15)=" << Sum(10, 15) << endl;
    cout << "sum(10, 15, 25)=" << Sum(10, 15, 25) << endl;
    cout << "sum(10, 15, 25, 30)=" << Sum(10, 15, 25, 30) << endl;
}