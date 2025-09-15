#include <iostream>
#include <string>
using namespace std;

class Movie
{
private:
    string title;
    string director;
    int year;
    double rating;

public:
    Movie(string t, string d = "Unkown", int y = 2020, double r = 0.0)
    {
        title = t;
        director = d;
        year = y;
        rating = r;
        if (1900 > y || y > 2020) // 오류 문장 출력
        {
            cout << "[Warning] Invalid year. Set to 2020." << endl;
            year = 2020;
        }
        if (r < 0.0 || r > 10.0)
        {
            cout << "[Warning] Invalid year. Set to 0.0" << endl;
            rating = 0.0;
        }
    }
    void print()
    {
        cout << "Title : " << title << endl;
        cout << "Director : " << director << endl;
        cout << "Year : " << year << endl;
        cout << "Rating : " << rating << endl;
        cout << "" << endl;
    }
};

int main()
{
    Movie m1("Interstellar", "Christopher", 2014, 8.6);
    Movie m2("Untitled", "John Doe", 1880, 12.5);
    Movie m3("Unknown Movie");

    m1.print();
    m2.print();
    m3.print();
}