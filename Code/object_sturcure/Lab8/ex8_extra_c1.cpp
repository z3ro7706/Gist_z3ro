#include <iostream>
#include <vector>
using namespace std;

class Weapon
{
public:
	virtual void load()
	{
	}
	 Weapon()
	{
	}
	virtual ~Weapon()
	{
	}
};

class Gun : public Weapon
{
public:
	void load() override
	{
		cout << "Loading gun" << endl;
	}
	~Gun()
	{
	}
};

class Bomb : public Weapon
{
public:
	void load() override
	{
		cout << "Loading bomb" << endl;
	}
	~Bomb()
	{
	}
};
int main()
{
	Weapon *weapon[3];
	Bomb b;
	weapon[0] = new Gun();
	weapon[1] = new Bomb();
	weapon[2] = &b;
	weapon[0]->load() ;
	weapon[1]->load() ;
	weapon[2] -> load();
	return 0;
}
