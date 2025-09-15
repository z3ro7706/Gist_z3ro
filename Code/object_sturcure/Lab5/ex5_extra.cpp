#include <iostream>
#include <string>

using namespace std;

class Engine
{
private:
    int horsepower;

public:
    Engine(int hp)
    {
        horsepower = hp;
    }
    void show()
    {
        cout << "Engine horsepower : " << horsepower << endl;
    }
};

class Car
{
private:
    string model_Name;
    Engine engine; // 함수에 Engine을 포함해준다

public:
    Car(string n, int hp) : model_Name(n), engine(hp) {} // 직접 호출해서 초기화 해야하므로 engine = hp 사용하면 안됨

    void show()
    {
        cout << "Car model : " << model_Name << endl;
        engine.show();
    }
};

int main()
{
    Car myCar("Sonata", 200);
    myCar.show();
}