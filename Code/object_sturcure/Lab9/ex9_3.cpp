#include<iostream>
#include<string>
#include<fstream>
using namespace std;

class Student
{	private:
	string name;
	int id;
	double average;

	public:
	Student(string n, int i, double a)
	{
	name = n;
	id = i;
	average=a;
	}
	~Student()
	{

	}
	friend ostream &operator <<(ostream &os, Student &s)
	{
		os<<"Name : "<<s.name<<", ID : "<<s.id<<", Average : "<<s.average;
		return os;
	}

};

int main()
{
	ofstream of("Student.txt");
	Student s1("Alice", 1001, 91.5);
	Student s2("Bob", 1002, 85.7);
	cout << s1<<endl;
	cout<<s2<<endl;
	of<<s1<<endl;
	of<<s2<<endl;
	return 0;
}

