#include <iostream>
#include "person.h"

using namespace std;

person::person() // 디폴트 삼각형
{
    name = "Unkwon";
    age = 0;
}

person::person(string n, int a)
{
    name = n;
    age = a;
}

void person::ShowInfo()
{
    cout << "Name : " << name << ", Age : " << age << endl;
}
