#include <iostream>
using namespace std;
template <typename T> // 함수의 타입을 나중에 결정
void swapValues(T &a, T &b)
{
    T value = a;
    a = b;
    b = value;
}
int main()
{
    int num1, num2;
    double double1, double2;
    char char1, char2;
    cout << "Enter two integers to swap : ";
    cin >> num1 >> num2;
    swapValues(num1, num2);
    cout << "Swaped values : " << num1 << " " << num2 << endl;
    cout << "Enter two double to swap : ";
    cin >> double1 >> double2;
    swapValues(double1, double2);
    cout << "Swaped values : " << double1 << " " << double2 << endl;
    cout << "Enter Two characters to swap : ";
    cin >> char1 >> char2;
    swapValues(char1, char2);
    cout << "Swaped valeus : " << char1 << " " << char2 << endl;
    ;
    return 0;
}
