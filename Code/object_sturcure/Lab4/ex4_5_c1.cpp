#include <iostream>
#include "Rectangle.h"

using namespace std;

int main()
{
    rectangle rect1;

    int w, h;
    cout << "Enter width : ";
    cin >> w;
    cout << "Enter height : ";
    cin >> h;

    rectangle rect2(w, h);

    cout << " " << endl;
    cout << "=== Rectangle Info ===" << endl;
    rect1.ShowInfo();
    rect2.ShowInfo();

    return 0;
}
