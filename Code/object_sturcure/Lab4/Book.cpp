#include <iostream> //Book.cpp
#include "Book.h"
using namespace std;
book::book() // 디폴트 삼각형
{
    title = "UnTitled";
    author = "Unkwon";
}
book::book(string t, string a)
{
    title = t;
    author = a;
}
void book::ShowInfo()
{
    cout << "Title : " << title << ", Author : " << author << endl;
}
