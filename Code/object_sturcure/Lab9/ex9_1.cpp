#include<iostream>

using namespace std;

class Point
{
	private:
		int x,y,z;
	public:
		Point(int a, int b, int c)
		{
			x=a;
			y=b;
			z=c;
		}
		~Point()
		{

		}
		friend ostream &operator<<(ostream &os, Point &p)	
		{
			
			os<<"("<<p.x<<", "<<p.y<<", "<<p.z<<")";
			return os;
		}

};

int main()
{
	Point p1(1,2,3);
	Point p2(4,5,6);

	cout<<p1<<" ~ "<<p2<<endl;
	return 0;
}
