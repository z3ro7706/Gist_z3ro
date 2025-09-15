// delegating Constructor

#include <iostream>
#include <string>
using namespace std;

class Book
{
private:
    string title;
    string author;
    int price;

public:
    Book(string t, string a, int p) : title(t), author(a), price(p) {}
    Book(string t, string a) : Book(t, a, 0) {}
    Book(string t) : Book(t, "None", 0) {}
    Book() : Book("None", "None", 0) {}

    void printInfo()
    {
        cout << "Title : " << title << ", Author : " << author << ", Price : " << price << endl;
    };
};

int main()
{
    Book b1;
    Book b2("C++ Primer");
    Book b3("Effective C++", "Scott Meyears");
    Book b4("Clean Code", "Robert C. Martin", 30000);
    b1.printInfo();
    b2.printInfo();
    b3.printInfo();
    b4.printInfo();
}