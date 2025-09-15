#include <iostream>
#include <string>

using namespace std;

class Tool
{
public:
    virtual int attack_bonus() const { return 0; } // 공격 보너스
    virtual string name() const { return "None"; } // 이름
};

class Guard
{
public:
    virtual int defence_bonus() const { return 0; } // 방어 보너스
    virtual string name() const { return "None"; }  // 이름
};

class Sword : public Tool
{
public:
    int attack_bonus() const { return 10; }
    string name() const { return "Sword"; }
};

class Bow : public Tool
{
public:
    int attack_bonus() const { return 7; }
    string name() const { return "Bow"; }
};

class WoodenGuard : public Guard
{
public:
    int defence_bonus() const { return 5; }
    string name() const { return "Wooden Guard"; }
};

class SteelGuard : public Guard
{
public:
    int defence_bonus() const { return 10; }
    string name() const { return "Steel Guard"; }
};

class Info // 플레이어의 상태를 저장
{
public:
    int health;     // 체력
    int experience; // 경험치
    int level;      // 레벨
    string weapon;  // 무기

    Info(int h, int e, int l, string w) : health(h), experience(e), level(l), weapon(w) {}
};

class Player
{
private:
    string name;
    int health;
    int experience;
    int level;
    string weapon;

    Tool *tool;   // 장착한 도구
    Guard *guard; // 장착한 방어구
    Info *savedState;

public:
    Player(string playerName)
        : name(playerName), health(100), experience(0), level(0), weapon("None"),
          tool(NULL), guard(NULL), savedState(NULL) {}

    ~Player()
    {
        delete savedState;
    }

    void set_tool(Tool *t)
    {
        tool = t;
        cout << "[Tool] Equipped: " << tool->name() << endl;
    }

    void set_guard(Guard *g)
    {
        guard = g;
        cout << "[Guard] Equipped: " << guard->name() << endl;
    }

    void gain_experience(int points)
    {
        int bonus = 0;
        if (tool != NULL)
            bonus = tool->attack_bonus();

        experience += points + bonus;

        while (experience >= 100)
        {
            experience -= 100;
            level++;
        }
    }

    void take_damage(int points)
    {
        int reduced = points;
        if (guard != NULL)
            reduced -= guard->defence_bonus();

        if (reduced < 0)
            reduced = 0;

        health -= reduced;
        if (health < 0)
            health = 0;

        if (health == 0)
        {
            cout << "[Info] Wasted." << endl;
        }
    }

    void set_weapon(const string &newWeapon)
    {
        weapon = newWeapon;
        cout << "[Weapon] " << weapon << " Get weapon" << endl;
    }

    void save()
    {
        delete savedState;
        savedState = new Info(health, experience, level, weapon);
        cout << "[Saved] Game saved." << endl;
    }

    void load()
    {
        if (savedState)
        {
            health = savedState->health;
            experience = savedState->experience;
            level = savedState->level;
            weapon = savedState->weapon;
            cout << "[Loaded] Game restored." << endl;
        }
        else
        {
            cout << "[Error] No saved data found." << endl;
        }
    }

    void show_status() const
    {
        cout << "Player: " << name << endl;
        cout << "Health: " << health << endl;
        cout << "Experience: " << experience << endl;
        cout << "Level: " << level << endl;
        cout << "Weapon: " << weapon << endl;
        if (tool != NULL)
            cout << "Tool: " << tool->name() << endl;
        if (guard != NULL)
            cout << "Guard: " << guard->name() << endl;
        cout << "------------------------------" << endl;
    }
};

int main()
{
    Player player("Z3RO");
    Sword sword;
    WoodenGuard guard;

    cout << "Initial actions:" << endl;
    player.set_weapon("Gun");
    player.set_tool(&sword);
    player.set_guard(&guard);
    player.gain_experience(30);
    player.take_damage(20);
    player.save();
    cout << "\n"
         << endl;

    cout << "After play:" << endl;
    player.gain_experience(80);
    player.take_damage(85);
    player.set_weapon("Arrow");
    player.show_status();
    cout << "\n"
         << endl;

    cout << "Loading saved game:" << endl;
    player.load();
    player.show_status();

    return 0;
}
