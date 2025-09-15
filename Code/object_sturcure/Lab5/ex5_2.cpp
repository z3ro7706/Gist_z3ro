#include <iostream>
#include <string>

using namespace std;

class Airplane
{
private: // private으로 들어가 있어 class안에서만 작동함에 주의하자
    string name;
    int capacity;
    int speed;

public:
    Airplane()
    {
        name = "airbus 350";
        capacity = 400;
        speed = 1000;
        // 넣어지는 값정의(default value)
    }
    Airplane(string n, int c, int s) : name(n), capacity(c), speed(s) {} // 직접 입력하는 값에 대한 정의(input value)

    void set(string &n, int c, int s)
    {
        name = n;
        capacity = c;
        speed = s;
    }

    void printf(int object)
    {
        cout << "Object" << object << "(Airplane #" << object << ")" << endl;
        cout << "Name of the plane : " << name << endl;
        cout << "Capacity of Airplane : " << capacity << endl;
        cout << "Airplane's speed : " << speed << " Km/h" << endl;
        cout << "" << endl;
    }
};
int main()
{
    Airplane a1;
    Airplane a2("Boeing 787", 300, 900);
    a1.printf(1);
    a2.printf(2);
    return 0;
}