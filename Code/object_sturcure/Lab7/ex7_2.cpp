#include <iostream>
using namespace std;

class BankAccount
{
private:
	int balances;
	static int totalBalance;

public:
	BankAccount(int b)
	{
		balances = b;
		totalBalance = totalBalance + balances;
	}
	void showBalance()
	{
		cout << "Account Balance : " << balances << endl;
	}

	static void showTotalBalance()
	{
		cout << "Total Balance in Bank : " << totalBalance << endl;
	}
};
int BankAccount::totalBalance = 0;

int main()
{
	BankAccount wallet1(1000);
	BankAccount wallet2(2000);

	wallet1.showBalance();
	wallet2.showBalance();
	BankAccount::showTotalBalance();
	return 0;
}
