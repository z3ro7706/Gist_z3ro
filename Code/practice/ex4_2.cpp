#include <iostream>
using namespace std;

class Student
{
private:
    string name;
    int age;
    float grade;

public:
    void setName(string n)
    {
        name = n;
    }
    void setAge(int a)
    {
        age = a;
    }
    void setGrade(float g)
    {
        grade = g;
    }
    string getName()
    {
        return name;
    }
    int getAge()
    {
        return age;
    }
    float getGrade()
    {
        return grade;
    }
};

int main()
{
    Student student;

    student.setName("John");
    student.setAge(20);
    student.setGrade(89.5);
    cout << "Name : " << student.getName() << endl;
    cout << "age : " << student.getAge() << endl;
    cout << "Name : " << student.getGrade() << endl;
    return 0;
}