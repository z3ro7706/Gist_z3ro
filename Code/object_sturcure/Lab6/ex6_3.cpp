#include <iostream>
using namespace std;

class Book
{
private:
    string title;
    string author;
    int year;

public:
    Book(string t = "Unkown", string a = "Unkown", int y = 0)
    {
        title = t;
        author = a;
        year = y;
    }
    friend ostream &operator<<(ostream &os, const Book &b);
};

ostream &operator<<(ostream &os, const Book &b) // 출력 역할을 할 os, 내가 사용할 정보 Book
{
    os << "Title : " << b.title << ", Author : " << b.author << ", Year : " << b.year << endl;
    return os;
}

int main()
{
    string t1, t2, a1, a2;
    int y1, y2;

    cout << "Enter the tittle of the first book : ";
    getline(cin, t1); // 공백이 있는 문장을 받을 때 (ex : Pride and potter)
    cout << "Enter the Author of the first book : ";
    getline(cin, a1);
    cout << "Enter the year of the first book : ";
    cin >> y1;
    cin.ignore(); // 줄 넘김 오류 방지

    cout << "Enter the tittle of the second book : ";
    getline(cin, t2); // 공백이 있는 문장을 받을 때 (ex : Pride and potter)
    cout << "Enter the Author of the second book : ";
    getline(cin, a2);
    cout << "Enter the year of the second book : ";
    cin >> y2;

    Book b1(t1, a1, y1);
    Book b2(t2, a2, y2);

    cout << "First book details : " << endl;
    cout << b1 << endl;
    cout << "second book details : " << endl;
    cout << b2 << endl;
}
