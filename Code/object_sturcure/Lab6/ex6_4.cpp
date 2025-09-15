#include <iostream>
using namespace std;

class Complex
{
private:
    double real;
    double imag;

public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}

    Complex operator-() const
    {
        return Complex(-real, -imag);
    }

    bool operator!() const
    {
        return (real == 0 && imag == 0);
    }

    void display() const
    {
        cout << "(" << real << ", " << imag << ")" << endl;
    }
};

int main()
{
    Complex num1(3.5, 4.2);
    Complex num2(0, 0);

    cout << "Original Complex number: ";
    num1.display();
    cout << "After applying unary minus: ";
    (-num1).display();
    cout << "Is complex number zero? ";
    cout << (!num1 ? "Yes" : "No") << endl
         << endl;

    cout << "Original Complex number: ";
    num2.display();
    cout << "Is complex number zero? ";
    cout << (!num2 ? "Yes" : "No") << endl;

    return 0;
}
