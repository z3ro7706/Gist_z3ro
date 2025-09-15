#include<iostream>
#include<fstream>
#include<iomanip>
#include<string>
using namespace std;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	string name;
	if(!in)
	{
		cout<<"Not Copy complete."<<endl;
	}
	cout<<"Copy complete."<<endl;

	while(in>>name)
	{
		out<<"Hello, world!"<<endl;
		out<<name<<" Object Oriented Programming"<<endl;
	}
	return 0;
}
