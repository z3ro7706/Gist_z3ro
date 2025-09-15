#ifndef BOOK_H // Book.h
#define BOOK_H
#include <string>
using namespace std;
class book
{
    string title;
    string author;

public:
    book();                            // 고정값
    book(string brand, string author); // 받는값
    void ShowInfo();                   // 출력
};
#endif
