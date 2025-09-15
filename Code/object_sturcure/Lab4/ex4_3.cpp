#include <iostream>
#include <string>
using namespace std;

class Product
{
private:
    string name;  // product name
    int quantity; // prodcut quantity
    double price; // product price

public:
    Product(string n, int q, double p) // 위의 값을 편한 문자로 변형 및 전체함수로 정의, product의 받아내는 형태 결정
    {
        name = n;
        quantity = q;
        price = p;
    }

    void displayInfo() // 받아낸 정보를 출력
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
    string name;
    int quantity;
    double price;

    cout << " Enter product name : ";
    cin >> name;

    cout << "Enter quantity : ";
    cin >> quantity;

    cout << "Enter price : ";
    cin >> price;

    Product p(name, quantity, price); // 값 넣기
    p.displayInfo();
    return 0;
}