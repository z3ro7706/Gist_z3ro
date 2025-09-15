#include <iostream>
#include <vector>

using namespace std;

class Shape
{
public:
	virtual void draw()
	{
		cout << "Drawing something" << endl;
	}
	virtual ~Shape()
	{
	}
};

class Circle : public Shape
{
public:
	void draw() override
	{
		cout << "Drwaing a circle" << endl;
	}
	~Circle()
	{
	}
};

class Rectangle : public Shape
{
public:
	void draw() override
	{
		cout << "Drwaing a Rectangle" << endl;
	}
	~Rectangle()
	{
	}
};
class Triangle : public Shape
{
public:
	void draw() override
	{
		cout << "Drwaing a Triangle" << endl;
	}
	~Triangle()
	{
	}
};

int main()
{
	vector<Shape *> shape;
	shape.push_back(new Circle());
	shape.push_back(new Rectangle());
	shape.push_back(new Triangle());

	for (auto v : shape)
	{
		v->draw();
	}
	for (auto v : shape)
	{
		delete v;
	}
	return 0;
}
