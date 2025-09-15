#include <iostream>
#include <string>
using namespace std;
class Product
{
private:
    string name;
    int quantity;
    double price;

public:
    Product(string n, int q, double p)
    {
        name = n;
        quantity = q;
        price = p;
    }
    void displayInfo()
    {
        cout << "" << endl;
        cout << "Product Information : " << endl;
        cout << "Product Name : " << name << endl;
        cout << "Quantitiy : " << quantity << endl;
        cout << "Price : $" << price << endl;
        cout << "" << endl;
    }
};
int main()
{
    string n;
    int q;
    double p;
    cout << "Enter product name : ";
    cin >> n;
    cout << "Enter quantity : ";
    cin >> q;
    cout << "Enter price : ";
    cin >> p;
    Product P(n, q, p);
    P.displayInfo();
    return 0;
}