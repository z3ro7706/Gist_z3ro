#include <iostream> //ex4_5_c4.cpp
#include "Book.h"
using namespace std;
int main()
{
    book book1;
    string b;
    string y;
    cout << "Enter book Title : ";
    cin.ignore();    // 공백이 있는 문장을 받는법
    getline(cin, b); // cin을 무시하며 받기
    cout << "Enter Author : ";
    getline(cin, y);
    cout << "Book created with tile :  : " << b << ", author : " << y << endl;
    book book2(b, y);
    cout << " " << endl;
    cout << "=== bok Info ===" << endl;
    book1.ShowInfo();
    book2.ShowInfo();
    cout << " " << endl;

    return 0;
}
