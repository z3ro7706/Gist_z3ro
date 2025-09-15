#include <iostream>
#include <string>
using namespace std;

class BankAccount
{
private:
    string ownerName;
    double balance;

public:
    // 생성자
    BankAccount(string name, double amount)
        : ownerName(name), balance(amount) {}

    // 정보를 출력하는 함수
    void show() const
    {
        cout << "Owner: " << ownerName << ", Balance: $" << balance << endl;
    }

    // friend 함수 선언
    friend void compareBalance(const BankAccount &a1, const BankAccount &a2);
};

// friend 함수 정의
void compareBalance(const BankAccount &a1, const BankAccount &a2)
{
    if (a1.balance > a2.balance)
        cout << a1.ownerName << " has a higher balance." << endl;
    else if (a1.balance < a2.balance)
        cout << a2.ownerName << " has a higher balance." << endl;
    else
        cout << "Both have the same balance." << endl;
}

// 테스트용 main 함수
int main()
{
    BankAccount john("John", 5000);
    BankAccount alice("Alice", 7000);
    compareBalance(john, alice); // 출력: Alice has a higher balance.

    BankAccount mike("Mike", 5000);
    BankAccount lily("Lily", 5000);
    compareBalance(mike, lily); // 출력: Both have the same balance.

    return 0;
}
