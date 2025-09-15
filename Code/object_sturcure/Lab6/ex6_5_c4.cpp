#include<iostream>
using namespace std;

class Counter
{
	private:
		int count;
	public:
		Counter()
		{
			count=0;
		}
		Counter(int c)
		{
			count =c;
		}

		Counter operator++(int)
		{
			count++;
			return count;
		}

		Counter operator++()
		{
			++count;
			return count;
		}

		void display()
		{
			cout<<"Count : "<<count<<endl;
		}
};

int main()
{
	Counter c(5);

	cout<<"Initial ";
	c.display();

	++c;
	cout<<"After Prefix increment ";
	c.display();

	c++;
	cout<<"After postfix increment ";
	c.display();
	return 0;
}


