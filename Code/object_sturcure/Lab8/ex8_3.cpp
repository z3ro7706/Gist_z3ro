#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Vehicle
{
public:
	virtual void move()
	{
		cout << "Vehicle is moving" << endl;
	}
	virtual ~Vehicle()
	{
		cout << "Vehicle close" << endl;
	}
};

class Car : public Vehicle
{
public:
	void move() override
	{
		cout << "Car is driving on the road" << endl;
	}

	~Car()
	{
		cout << "Car close" << endl;
	}
};
class Bicycle : public Vehicle
{
public:
	void move() override
	{
		cout << "Bicycle is pedaling  on the road" << endl;
	}
	~Bicycle()
	{
		cout << "Biycle close" << endl;
	}
};
class Motorcycle : public Vehicle
{
public:
	void move() override
	{
		cout << "Motorcycle  is racing  on the road" << endl;
	}
	~Motorcycle()
	{
		cout << "Motorcycle close" << endl;
	}
};

int main()
{
	vector<Vehicle *> vehicle;

	vehicle.push_back(new Car());
	vehicle.push_back(new Car());
	vehicle.push_back(new Bicycle());
	vehicle.push_back(new Bicycle());
	vehicle.push_back(new Motorcycle());
	vehicle.push_back(new Motorcycle());
	for (auto v : vehicle)
	{
		v->move();
	}
	for (auto v : vehicle)
	{
		delete v;
	}
	return 0;
}
