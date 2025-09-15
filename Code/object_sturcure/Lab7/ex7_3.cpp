#include<iostream>
#include<string>
using namespace std;

class Book
{
	private:
		string title;
		string name;
	public:
		Book(string t, string n)
		{
			title=t;
			name=n;
		}

		void printInfo()
		{
			cout<<"Tittle : " << title<<endl;
			cout<<"Author : "<<name<<endl;
		}
};

class EBook : public Book
{
	private:
		double fileSizeMB;

	public:
		EBook(string t, string n, double s) : Book(t,n) //book함수를 끌어와야함
		{
			fileSizeMB = s;
		}
		void printAllInfo()
		{
			printInfo();
			cout<<"File Size : "<<fileSizeMB<<endl;
		}
};

int main()
{
	EBook ebook("C++ Primer", "Stanley B. Lippman", 5.2);
	ebook.printAllInfo();
	return 0;
}

