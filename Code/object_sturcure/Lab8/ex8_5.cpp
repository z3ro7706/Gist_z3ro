#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#define PI 3.14
using namespace std;

class Shape
{
protected:
  int x, y;

public:
  Shape(int a, int b)
  {
    x = a;
    y = b;
  }
  virtual double getArea()
  {
    return 0;
  }
  virtual ~Shape()
  {
  }
};

class Rect : public Shape
{
public:
  int width;
  int height;

  Rect(int x, int y, int w, int h) : Shape(x, y)
  {
    width = w;
    height = h;
  }
  double getArea() override
  {
    return (width * height);
  }
  ~Rect()
  {
  }
};

class Circle : public Shape
{
public:
  int radius;

  Circle(int x, int y, int r) : Shape(x, y)
  {
    radius = r;
  }
  double getArea() override
  {
    return (radius * radius * PI);
  }
  ~Circle()
  {
  }
};

class Triangle : public Shape
{
public:
  int width;
  int height;
  Triangle(int x, int y, int w, int h) : Shape(x, y)
  {
    width = w;
    height = h;
  }
  double getArea() override
  {
    return (width * height / 2);
  }
  ~Triangle()
  {
  }
};

int main()
{
  srand(static_cast<unsigned int>(time(NULL)));
  Shape *shape[3];
  shape[0] = new Rect(rand() % 1000, rand() % 1000, rand() % 50 + 1, rand() % 50 + 1);
  shape[1] = new Circle(rand() % 1000, rand() % 1000, rand() % 50 + 1);
  shape[2] = new Triangle(rand() % 1000, rand() % 1000, rand() % 50 + 1, rand() % 50 + 1);
  for (int i; i < 3; i++)
  {
    cout << "Area of shape #" << i << " : " << shape[i]->getArea() << endl;
  }
  for (int i; i < 3; i++)
  {
    delete shape[i];
  }
  return 0;
}
