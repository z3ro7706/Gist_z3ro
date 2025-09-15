#include<iostream>
#include<string>

using namespace std;

class Animal
{
	public:
		string name;
		Animal(string n)
		{
			name =n;
		}

		void speak()
		{
			cout<<name<<" make a sound."<<endl;
		}
};

class Cat : public Animal
{

	public:
		Cat(string n):Animal(n)
	{

	}
		void meow()
		{
			cout<<name<<" says meow!"<<endl;
		}
};

int main()
{
	Cat cat("Nabi");
	cat.speak();
	cat.meow();
	return 0;
}

