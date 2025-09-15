#include <iostream>
#include <string>

using namespace std;

class Info // 플레이어의 상태를 저장할 클래스 (saving point)
{
public:
    int health;     // 체력
    int experience; // 경험치
    int level;      // 레벨
    string weapon;  // 무기

    // 디폴트값
    Info(int h, int e, int l, string w) : health(h), experience(e), level(l), weapon(w) {}
};

// 실제 게임 플레이어 클래스
class Player
{
private:
    string name;    // 플레이어 이름
    int health;     // 현재 체력
    int experience; // 현재 경험치
    int level;      // 현재 레벨
    string weapon;  // 현재 장착 무기

    Info *savedState; // 저장된 상태

public:
    // 생성자: 기본 체력 100, 경험치 0, 레벨 0, 무기 없음
    Player(string playerName)
        : name(playerName), health(100), experience(0), level(0), weapon("None"), savedState(nullptr) {}

    ~Player()
    {
        delete savedState;
    }

    // 경험치를 얻고, 100 이상이면 레벨업
    void gain_experience(int points)
    {
        experience += points;
        while (experience >= 100)
        {
            experience -= 100;
            level++;
        }
    }

    // hp가 0 이하면 0으로 고정하고, wasted 출력
    void take_damage(int points)
    {
        health -= points;
        if (health < 0)
            health = 0;

        if (health == 0)
        {
            cout << "[Info] Wasted." << endl; // 체력 0 이하일 경우 사망 출력
        }
    }

    // 무기 장착
    void set_weapon(const string &newWeapon)
    {
        weapon = newWeapon;
        cout << "[Weapon] " << weapon << "Get weapon " << endl; // 무기 장착 출력
    }

    // 현재 상태를 저장
    void save()
    {
        // 이전에 저장된 상태가 있다면 메모리 해제
        delete savedState;

        // 현재 상태를 기반으로 새로운 Info 객체 생성 및 저장
        savedState = new Info(health, experience, level, weapon);
        cout << "[Saved] Game saved." << endl;
    }

    // 저장된 상태 불러오기
    void load()
    {
        if (savedState) // 저장된 상태가 있는 경우
        {
            health = savedState->health;               // 값 불러오기
            experience = savedState->experience;       // 값 불러오기
            level = savedState->level;                 // 값 불러오기
            weapon = savedState->weapon;               // 값 불러오기
            cout << "[Loaded] Game restored." << endl; // 값 불러오기 출력
        }
        else // 오류
        {
            cout << "[Error] No saved data found." << endl; // 값이 없을때 오류 출력
        }
    }

    // 현재 상태 출력하기
    void show_status() const // 처음상태를 출력하기 & 기본 틀
    {
        cout << "Player: " << name << endl;
        cout << "Health: " << health << endl;
        cout << "Experience: " << experience << endl;
        cout << "Level: " << level << endl;
        cout << "Weapon: " << weapon << endl; // 무기 출력
        cout << "------------------------------" << endl;
    }
};

int main()
{
    Player player("Z3RO"); // 새로운 플레이어 생성

    cout << "Initial actions:" << endl;
    player.set_weapon("Gun");   // 무기 장착
    player.gain_experience(30); // exp 30
    player.take_damage(20);     // hp -20
    player.save();              // 저장
    cout << "\n"
         << endl;

    cout << "After play:" << endl;
    player.gain_experience(80); // exp +80 => 레벨업
    player.take_damage(85);     // hp -85 => 체력 0으로 사망 출력
    player.set_weapon("arrow"); // 무기 변경
    player.show_status();       // 현재 상태 출력
    cout << "\n"
         << endl;

    cout << "Loading saved game:" << endl;
    player.load();        // 저장 상태 복원
    player.show_status(); // 복원 상태 출력

    return 0;
}
