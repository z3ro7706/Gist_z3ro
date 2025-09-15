#include <iostream>
#include <string>
using namespace std;

class Student
{
private:         // class 안에서만 정의됨에 주의하자!
    string name; // Student's name
    int age;     // Student's age
    float grade; // Student's grade

public:
    void setName(string n)
    {
        name = n; // 받는 n 을 private name으로 넣음
    }
    void setAge(int a)
    {
        age = a; // 받는 a 을 private age으로 넣음
    }
    void setGrade(float g)
    {
        grade = g; // 받는 g 을 private grede으로 넣음
    }

    // private의 값을 출력
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
    Student s;

    s.setName("John"); // n의 John을 넣기
    s.setAge(20);      // a에 20을 넣기
    s.setGrade(89.5);  // G에 89.5을 넣기

    cout << "Name : " << s.getName() << endl;
    cout << "Age : " << s.getAge() << endl;
    cout << "Grade : " << s.getGrade() << endl;
    cout << "" << endl;
    return 0;
}
