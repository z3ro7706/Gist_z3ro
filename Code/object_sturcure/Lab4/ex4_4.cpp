#include <iostream>
#include "Student.h" //student.cpp의 내용을 끌고 들어옴

using namespace std;

int main()
{
    string name;
    int age;
    double gpa;

    cout << "Enter student name : ";
    cin >> name;
    cout << "Enter student age : ";
    cin >> age;
    cout << "Enter Student GPA : ";
    cin >> gpa;
    cout << "" << endl;

    Student s(name, age, gpa);
    s.displayinfo();

    return 0;
}