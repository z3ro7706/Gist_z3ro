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
			count=c;
		}

		Counter operator--(int)
		{
			count--;
			return *this;
		}

		Counter operator--()
		{
			--count;
			return *this;
		}
		void display()
		{
			cout<<"Count : " << count<<endl;
		}

};

int main()
{
	Counter c(5);

	cout<<"Initail ";
   c.display()	;

   --c;
   cout<<"After prefix decrement - ";
  c.display();

 c--;
cout<<"After posfix decrement - ";
c.display();
return 0;
}
