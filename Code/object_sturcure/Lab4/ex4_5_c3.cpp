#include <iostream>
#include "Brand.h"

using namespace std;

int main()
{
    brand car1;
    string b;
    int y;
    cout << "Enter Brand : ";
    cin >> b;
    cout << "Enter year : ";
    cin >> y;
    cout << "Car created with brand : " << b << ", year : " << y << endl;
    brand car2(b, y);

    cout << " " << endl;
    cout << "=== Car Info ===" << endl;
    car1.ShowInfo();
    car2.ShowInfo();
    cout << " " << endl;

    return 0;
}
