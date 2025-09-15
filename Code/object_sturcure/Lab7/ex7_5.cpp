#include <iostream>
#include <string>

using namespace std;

class Base
{
public:
	string name;
	int age;

	Base(string n, int a)
	{
		name = n;
		age = a;
	}
	void show()
	{
		cout << "Name : " << name << ", Age : " << age << endl;
	}
};

class Professor : public Base
{
private:
	string subject;

public:
	Professor(string n, int a, string s) : Base(n, a)
	{
		subject = s;
	}
	void show()
	{
		cout << "Name : " << name << ", Age : " << age << ", Subject : " << subject << endl;
	}
};

class Student : public Base
{
private:
	int studentID;

public:
	Student(string n, int a, int i) : Base(n, a)
	{
		studentID = i;
	}
	void showStudentInfo()
	{
		cout << "Student : " << name <<  " - ID : " << studentID << endl;
	}
};

int main()
{
	Professor p("Dr. Kim", 45, "Physics");
	Student s("Alice", 20, 20231234);
	p.show();
	s.showStudentInfo();
	return 0;
}
