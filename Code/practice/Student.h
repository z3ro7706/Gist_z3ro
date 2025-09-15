
#ifndef STUDENT_H // Student.h
#define STUDENT_H
// 헤더파일에 해당되는 내용을 넣음(private, public) 이걸 나머지 파일에서 동일하게 사용
#include <string>
using namespace std;
class Student
{
private:
    string name;
    int age;
    double gpa;

public:
    Student(string n, int a, double g);
    void displayinfo();
};
#endif