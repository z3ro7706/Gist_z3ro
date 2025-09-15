#include <iostream>
using namespace std;
template <typename T> // 함수의 타입을 나중에 결정한다.

// 특정 타입에 대한 SWAP
inline void SwapValues(T &a, T &b)
{
    T value = a;
    a = b;
    b = value;
}

int main()
{
    int int_1, int_2;
    double double_1, double_2;
    char char_1, char_2;

    // integers 입력
    cout << "Enter two integers to swap : ";
    cin >> int_1 >> int_2;
    SwapValues(int_1, int_2);
    cout << "Swapped values : " << int_1 << " " << int_2 << endl;

    // double 입력
    cout << "Enter two double to swap : ";
    cin >> double_1 >> double_2;
    SwapValues(double_1, double_2);
    cout << "Swapped values : " << double_1 << " " << double_2 << endl;

    // character 입력
    cout << "Enter two characters to swap : ";
    cin >> char_1 >> char_2;
    SwapValues(char_1, char_2);
    cout << "Swapped values : " << char_1 << " " << char_2 << endl;

    return 0;
}