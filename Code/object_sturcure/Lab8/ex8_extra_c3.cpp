#include<iostream>
#include<vector>
using namespace std;

class Character
{
	public:
	Character()
	{

	}
	~Character()
	{

	}
	virtual void attack()
	{

	}
};

class Warrior : public Character
{
	public:
	Warrior()
	{

	}
	~Warrior()
	{

	}
	void attack() override
	{
		cout<< " Swing sword!"<<endl;
	}
};
class Archer : public Character
 {
	 public:
      Archer()
      {

      }
      ~Archer()
      {

      }
      void attack() override
      {
          cout<< " Shoot arrow!"<<endl;
      }
  };
class Mage : public Character
   {
	   public:
        Mage()
       {
  
        }
        ~Mage()
        {
  
        }
        void attack() override
        {
            
			cout<< " Cast fireball!"<<endl;
        }
    };

int main()
{
	vector<Character *> chara;
	chara.push_back(new Warrior());
	chara.push_back(new Archer());
	chara.push_back(new Mage());
	for( auto v : chara)
	{
		v->attack();
	}
	for(auto v : chara)
	{
		delete v;
	}
	return 0;
}
