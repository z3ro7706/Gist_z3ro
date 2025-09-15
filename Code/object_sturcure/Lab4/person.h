#ifndef PERSON_H
#define PERSON_H

#include <string>
using namespace std;

class person
{
    string name;
    int age;

public:
    person();                     // 고정값
    person(string name, int age); // 받는값
    void ShowInfo();              // 출력
};

#endif
