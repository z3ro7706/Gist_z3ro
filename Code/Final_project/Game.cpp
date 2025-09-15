#include <iostream>
#include <string>
using namespace std;

class Tool // 무기 추가 기본 설정
{
public:
    int attack_bouns;
    int range;
    string name;

    Tool() : attack_bouns(0), range(0), name("Unknown") {}
};

class Guard // 방어 추가 기본 설정
{
public:
    int defence_bouns;
    int reflection_damage;
    string name;

    Guard() : defence_bouns(0), reflection_damage(0), name("Unknown") {}
};

// 공격무기 종류
class wooden_sword : public Tool
{
public:
    wooden_sword()
    {
        attack_bouns = 2;
        range = 1;
        name = "Wooden_Sword";
    }
};

class iron_sword : public Tool
{
public:
    iron_sword()
    {
        attack_bouns = 4;
        range = 1;
        name = "Iron_Sword";
    }
};

class Diamond_sword : public Tool
{
public:
    Diamond_sword()
    {
        attack_bouns = 7;
        range = 1;
        name = "Diamond_Sword";
    }
};

class Bow : public Tool
{
public:
    Bow()
    {
        attack_bouns = 3;
        range = 5;
        name = "Bow";
    }
};

// 방어구 종류
class cloth_armor : public Guard
{
public:
    cloth_armor()
    {
        defence_bouns = 1;
        name = "Cloth_armor";
    }
};

class iron_armor : public Guard
{
public:
    iron_armor()
    {
        defence_bouns = 3;
        name = "Iron_armor";
    }
};

class diamond_armor : public Guard
{
public:
    diamond_armor()
    {
        defence_bouns = 6;
        name = "Diamond_armor";
    }
};

class thornmail : public Guard
{
public:
    thornmail()
    {
        defence_bouns = 1;
        reflection_damage = 2;
        name = "Thornmail_armor";
    }
};

// 사용자 지정

class Info // 사용자 save할 데이터 보관용
{
public:
    int health;
    int experience;
    int level;
    Tool *tool;
    Guard *guard;

    Info(int h, int e, int l, Tool *t, Guard *g)
    {
        health = h;
        experience = e;
        level = l;
        tool = t;
        guard = g;
    }
};

class Player
{
private: // 플레이어에 배정될 정보
    string name;
    int health;
    int experience;
    int level;
    Tool *tool;
    Guard *guard;
    Info *saved; // 데이터 세이브

public:
    Player(string player_name) // 기본 캐릭터 생성
    {
        name = player_name;
        health = 100;
        experience = 0;
        level = 0;
        tool = NULL;
        guard = NULL;
        saved = NULL;
    }

    ~Player()
    {
        delete saved;
    }
    void save() // 현재 상태 저장
    {
        delete saved;
        saved = new Info(health, experience, level, tool, guard);
        cout << " Game saved." << endl;
    }

    void load() // 저장된 상태 불러오기
    {
        if (saved != NULL)
        {
            health = saved->health;
            experience = saved->experience;
            level = saved->level;
            tool = saved->tool;
            guard = saved->guard;
            cout << " Game loaded." << endl;
        }
        else
        {
            cout << " No saved data found." << endl;
        }
    }

    void set_tool(Tool *t) // 무기 가지기
    {
        tool = t;
        cout << " Get Weapon : " << tool->name << endl;
    }

    void set_guard(Guard *g) // 갑옷 가지기
    {
        guard = g;
        cout << " Get Guard : " << guard->name << endl;
    }

    void gain_experience(int point) // 레벨에 따른 완화된 추가 공격
    {
        int bonus = 0;
        if (tool != NULL)
            bonus += tool->attack_bouns;
        bonus += level / 2;

        experience += point + bonus;

        cout << " Experience gained: " << point << " + bonus(" << bonus << ") = " << experience << endl;

        while (experience >= 100)
        {
            experience = experience - 100;
            level = level + 1;
            cout << " Level up!, Now level = " << level << endl;
        }
    }

    void take_damage(int point) // 피해 입기
    {
        int reduce = 0;
        if (guard != NULL)
            reduce += guard->defence_bouns;

        int real_damage = point - reduce;
        if (real_damage < 0)
            real_damage = 0;

        health = health - real_damage;
        cout << " Took damage: " << real_damage << " (Reduced by " << reduce << "), Health: " << health << endl;

        if (health <= 0)
        {
            cout << " Wasted" << endl;
            experience = 0;
            tool = NULL;
            guard = NULL;
        }
    }

    void attack(Player &enemy) // 다른 플레이어 공격
    {
        if (tool == NULL)
        {
            cout << " No weapon to attack." << endl;
            return;
        }

        int power = tool->attack_bouns + level;
        cout << " Attack " << enemy.name << " with " << tool->name << " (Power: " << power << ")" << endl;

        enemy.take_damage(power);

        if (enemy.guard != NULL && enemy.guard->reflection_damage > 0)
        {
            health = health - enemy.guard->reflection_damage;
            cout << " Reflected damage taken: " << enemy.guard->reflection_damage << ", Health: " << health << endl;

            if (health <= 0)
            {
                cout << " Wasted" << endl;
                experience = 0;
                tool = NULL;
                guard = NULL;
            }
        }
    }

    void show_status() // 현재 상태 출력
    {
        cout << " ==============================" << endl;
        cout << " Name : " << name << endl;
        cout << " Health : " << health << endl;
        cout << " Experience : " << experience << endl;
        cout << " Level : " << level << endl;
        cout << " Weapon : " << (tool != NULL ? tool->name : "None") << endl;
        cout << " Guard : " << (guard != NULL ? guard->name : "None") << endl;
        cout << " ==============================" << endl;
    }
};

int main()
{
    Player player1("Z3RO"); // 플레이어 생성
    Diamond_sword sword;    // 무기 생성
    thornmail armor;        // 가시 갑옷 생성

    cout << " [Initial Equipment Settings] " << endl;
    player1.set_tool(&sword);    // 무기 장착
    player1.set_guard(&armor);   // 갑옷 장착
    player1.gain_experience(50); // 경험치 획득
    player1.take_damage(10);     // 데미지 받기
    player1.show_status();

    cout << "\n [Game save] " << endl;
    player1.save(); // 상태 저장

    cout << "\n [Additional Experience and Damage] " << endl;
    player1.gain_experience(60); // 레벨업 발생
    player1.take_damage(120);    // 체력 0 이하 → Wasted
    player1.show_status();

    cout << "\n [Saving Back] " << endl;
    player1.load(); // 저장된 상태 불러오기
    player1.show_status();

    return 0;
}
