#include <iostream>
#include "person.h"

using namespace std;

int main()
{
    person person1;
    string n;
    int a;
    cout << "Enter name : ";
    cin >> n;
    cout << "Enter age : ";
    cin >> a;

    person person2(n, a);

    cout << " " << endl;
    cout << "=== Rerson Info ===" << endl;
    person1.ShowInfo();
    person2.ShowInfo();

    return 0;
}
