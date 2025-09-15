#include <iostream>
#include <string> // class 를 사용하기 위한 sting형
using namespace std;

class Book
{
public:            // 주로 class 안에는 private이 기본으로 되어있으므로 public으로 전체 사용가능
    string title;  // book title
    string author; // author of the book
    int pages;     // number of pages in the book

    void displayInfo()
    {
        cout << "Title : " << title << endl;
        cout << "Author : " << author << endl;
        cout << "pages : " << pages << endl;
    }
};
int main()
{
    Book inbook;

    // class 안에 정보 넣기
    inbook.title = "Alice's Adventures in Wonderland";
    inbook.author = "Lewis Carroll";
    inbook.pages = 176;

    inbook.displayInfo(); // 이미 class안에 정보가 들어가므로, 추가적인 정보를 넣어줄 필요 없음
    cout << "" << endl;
    return 0;
}
