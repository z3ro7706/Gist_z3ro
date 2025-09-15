#include <iostream>
using namespace std;

class Book
{
public:
    string title;
    string author;
    int pages;

    void displayInfo()
    {

        cout << "Title : " << title << endl;
        cout << "Author : " << author << endl;
        cout << "Pages : " << pages << endl;
    }
};

int main()
{
    Book book;
    book.title = "Alice's Adventures in Wonderland";
    book.author = "Lewis carroll";
    book.pages = 176;
    book.displayInfo();
    cout << "" << endl;
    return 0;
}
