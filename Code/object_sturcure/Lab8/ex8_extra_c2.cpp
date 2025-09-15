#include <iostream>

using namespace std;

class HomeAppliance
{
public:
	int price;

	HomeAppliance(int p)
	{
		price = p;
	}
	virtual ~HomeAppliance()
	{
	}
	virtual void getPrice()
	{
		cout << price << endl;
	}
};

class Television : public HomeAppliance
{
public:
	int price;
	Television(int p) : HomeAppliance(p)
	{
		price = p;
	}
	~Television()
	{
	}
	void getPrice() override
	{
		cout << "Price : " << price * 9 / 10 << endl;
	}
};
class Refrigerator : public HomeAppliance
{
public:
	int price;
	Refrigerator(int p) : HomeAppliance(p)
	{
		price = p;
	}
	~Refrigerator()
	{
	}
	void getPrice() override
	{
		cout << "Price : " << price * 95 / 100 << endl;
	}
};

int main()
{
	HomeAppliance *list[3];
	list[0] = new Television(100000);
	list[1] = new Refrigerator(200000);
	list[2] = new Television(300000);
	list[0]->getPrice();
	list[1]->getPrice();
	list[2]->getPrice();
	for (int i; i < 3; i++)
	{
		delete list[i];
	}
	return 0;
}
