#include <iostream>
using namespace std;

class Person
{
	private:

	public:
		Person()
		{
			cout<<"Person construcor called"<<endl;
		}
		~Person()
		{
			cout<<"Person destrucor called"<<endl;
		}
};

class Student : public Person
{
	public:
		Student()
		{
			cout<<"Student constructor called"<<endl;
		}
		~Student()
		{
			cout<<"Student destructor called"<<endl;
		}

};

class GraduateStudent : public Student
{
	public:
		GraduateStudent()
		{
			cout<<"GraduateStudent constructor called"<<endl;

		}
		~GraduateStudent()
		{
			cout<<"GraudatStudent destructor called"<<endl;
		}
};

int main()
{
	cout<<"main begins"<<endl;
	GraduateStudent gs;
	cout<<"main ends"<<endl;
	return 0;
}

