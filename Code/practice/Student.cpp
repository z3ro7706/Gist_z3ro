#include <iostream>  //Student.cpp
#include "Student.h" //Student.h 헤더파일에 있는 정보 사용
using namespace std;
Student::Student(string n, int a, double g) // Student 헤더파일에 있는 Student class 함수 이용
{
    name = n;
    age = a;
    gpa = g;
}
void Student::displayinfo() // Student에 존재하는 displayinfo 사용
{
    cout << "Student Information : " << endl;
    cout << "Name : " << name << endl;
    cout << "Age : " << age << endl;
    cout << "GPA : " << gpa << endl;
    cout << "" << endl;
}