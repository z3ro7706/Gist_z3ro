#include <iostream>
#include <string>
using namespace std;

class Student
{
private:
    string name;
    int id;
    static int totalStudents;

public:
    Student(string studentName, int studentId)
    {
        name = studentName;
        id = studentId;
        totalStudents++;
    }

    void showStudentInfo()
    {
        cout << "Student Name: " << name << ", ID: " << id << endl;
    }

    static void showTotalStudents()
    {
        cout << "Total Students: " << totalStudents << endl;
    }
};

int Student::totalStudents = 0;

int main()
{
    Student student1("John", 1001);
    Student student2("Alice", 1002);
    student1.showStudentInfo();
    student2.showStudentInfo();
    Student::showTotalStudents();
    return 0;
}
