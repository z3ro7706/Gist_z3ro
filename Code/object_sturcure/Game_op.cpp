#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <windows.h>

using namespace std;

class Tool
{
public:
    int attack_bouns;
    int range;
    string name;

    Tool() : attack_bouns(0), range(0), name("Unknown") {}
};

class Guard
{
public:
    int defence_bouns;
    int reflection_damage;
    string name;

    Guard() : defence_bouns(0), reflection_damage(0), name("Unknown") {}
};

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

class Observer
{
public:
    virtual void onToolChanged(string tool_name) {}
    virtual void onGuardChanged(string guard_name) {}
    virtual void onStateRestored() {}
    virtual void onDamageTaken(int damage) {}
    virtual void onExperienceGained(int exp, int bonus) {}
    virtual void onLevelUp(int level) {}
    virtual void onGuardBroken() {}
};

class SoundManager : public Observer
{
public:
    void playSound()
    {
        MessageBeep(MB_OK);
    }

    void playBreakSound()
    {
        Beep(400, 300);
    }

    void onToolChanged(string tool_name) override { playSound(); }
    void onGuardChanged(string guard_name) override { playSound(); }
    void onStateRestored() override { playSound(); }
    void onGuardBroken() override { playBreakSound(); }
};

class Logger : public Observer
{
public:
    void onDamageTaken(int damage) override
    {
        Sleep(1000);
        ofstream log("log.txt", ios::app);
        log << "Damage taken: " << damage << endl;
    }

    void onExperienceGained(int exp, int bonus) override
    {
        Sleep(1000);
        ofstream log("log.txt", ios::app);
        log << "Experience gained: " << exp << ", Bonus: " << bonus << endl;
    }

    void onLevelUp(int level) override
    {
        Sleep(1000);
        ofstream log("log.txt", ios::app);
        log << "Level up! New level: " << level << endl;
    }

    void onGuardBroken() override
    {
        Sleep(1000);
        ofstream log("log.txt", ios::app);
        log << "Guard broken!" << endl;
    }
};

class Info
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
private:
    string name;
    int health;
    int experience;
    int level;
    Tool *tool;
    Guard *guard;
    Info *saved;
    vector<Observer *> observers;
    int guard_hit_count = 0;

public:
    Player(string player_name)
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

    void addObserver(Observer *obs)
    {
        observers.push_back(obs);
    }

    void save()
    {
        delete saved;
        saved = new Info(health, experience, level, tool, guard);
        cout << " Game saved." << endl;
    }

    void load()
    {
        if (saved != NULL)
        {
            health = saved->health;
            experience = saved->experience;
            level = saved->level;
            tool = saved->tool;
            guard = saved->guard;
            guard_hit_count = 0;
            cout << " Game loaded." << endl;
            for (auto obs : observers)
                obs->onStateRestored();
        }
        else
        {
            cout << " No saved data found." << endl;
        }
    }

    void set_tool(Tool *t)
    {
        tool = t;
        cout << " Get Weapon : " << tool->name << endl;
        for (auto obs : observers)
            obs->onToolChanged(tool->name);
    }

    void set_guard(Guard *g)
    {
        guard = g;
        guard_hit_count = 0;
        cout << " Get Guard : " << guard->name << endl;
        for (auto obs : observers)
            obs->onGuardChanged(guard->name);
    }

    void gain_experience(int point)
    {
        int bonus = 0;
        if (tool != NULL)
            bonus += tool->attack_bouns;
        bonus += level / 2;

        experience += point + bonus;

        cout << " Experience gained: " << point << " + bonus(" << bonus << ") = " << experience << endl;
        for (auto obs : observers)
            obs->onExperienceGained(point, bonus);

        while (experience >= 100)
        {
            experience = experience - 100;
            level = level + 1;
            cout << " Level up!, Now level = " << level << endl;
            for (auto obs : observers)
                obs->onLevelUp(level);
        }
    }

    void take_damage(int point)
    {
        int reduce = 0;
        if (guard != NULL)
            reduce += guard->defence_bouns;

        int real_damage = point - reduce;
        if (real_damage < 0)
            real_damage = 0;

        health = health - real_damage;
        cout << " Took damage: " << real_damage << " (Reduced by " << reduce << "), Health: " << health << endl;
        for (auto obs : observers)
            obs->onDamageTaken(real_damage);

        if (guard != NULL)
        {
            guard_hit_count++;
            if (guard_hit_count >= 5)
            {
                cout << " Guard broken!" << endl;
                for (auto obs : observers)
                    obs->onGuardBroken();
                guard = NULL;
                guard_hit_count = 0;
            }
        }

        if (health <= 0)
        {
            cout << " Wasted" << endl;
            experience = 0;
            tool = NULL;
            guard = NULL;
        }
    }

    void attack(Player &enemy)
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

    void show_status()
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
    Player player1("Z3RO");
    Diamond_sword sword;
    thornmail armor;

    SoundManager sound;
    Logger logger;
    player1.addObserver(&sound);
    player1.addObserver(&logger);

    cout << " [Initial Equipment Settings] " << endl;
    player1.set_tool(&sword);
    player1.set_guard(&armor);
    player1.gain_experience(50);
    player1.take_damage(10);
    player1.show_status();

    cout << "\n [Game save] " << endl;
    player1.save();

    cout << "\n [Additional Experience and Damage] " << endl;
    player1.gain_experience(60);
    for (int i = 0; i < 5; ++i)
        player1.take_damage(10);
    player1.show_status();

    cout << "\n [Saving Back] " << endl;
    player1.load();
    player1.show_status();

    return 0;
}