#include<iostream>
using namespace std;

class Point
{
	private:
		int x;
		int y;

	public:
		Point(int a, int b)
		{
			x=a;
			y=b;
		}
		bool operator!=(const Point p)
		{
			return(x!=p.x && y!= p.y);
		}

};

int main()
{
	Point p1(1, 2);
	Point p2(1, 2);
	Point p3(3, 4);
	
	if(p1 != p2)
		cout<<"p1 and p2 are different."<<endl;
	else
		cout<<"p1 and p2 are the same."<<endl;

	if(p1 != p3)
		cout<<"p1 and p3 are different." <<endl;
	else
		cout<<"p1 and p3 are the same."<<endl;
	return 0;	
}

