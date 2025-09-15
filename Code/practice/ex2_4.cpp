#include <iostream>
using namespace std;

inline void calculateOperations(int a, int b, int &sum, int &diff, int &product)
{
    cout << "Sum : " << &sum << ", Diff : " << &diff << ", Product : " << &product << endl;
    sum = a + b;
    diff = a - b;
    product = a * b;
}

int main()
{
    int sum, diff, product, num1, num2;
    cout << "Enter the first nubmer : ";
    cin >> num1;
    cout << "Enter the second number : ";
    cin >> num2;

    cout << "In main()" << endl;
    cout << "Sum : " << &sum << ", Diff : " << &diff << ", Product : " << &product << endl;
    cout << "" << endl;
    cout << "In calculateOperation)" << endl;

    calculateOperations(num1, num2, sum, diff, product);
    cout << "Sum : " << sum << endl;
    cout << "Difference : " << diff << endl;
    cout << "Product : " << product << endl;
    cout << "" << endl;
    return 0;
}