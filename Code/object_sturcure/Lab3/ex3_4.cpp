#include <iostream>
using namespace std;

template <typename T>

class box
{
private:     // class 내부에서만 작동하는 공간
    T value; // 사용되는 value값의 타입이 정해져 있지는 않음

public:                  // 다른곳에도 데이터를 오픈하여 사용 가능
    void setValue(T val) // 어떤 형태인지 모르는 값을 받음
    {
        value = val; // 받아낸 값을 Value에 지정
    }

    T getValue() const
    {
        return value; // 지정했떤 Value값을 retrun
    }
};

int main()
{
    box<int> intBox;      // 받아내는 타입을 int형으로 선언
    intBox.setValue(100); // Value값에 100이 들어가게됨
    cout << intBox.getValue() << endl;

    box<string> strBox;       // 받아내는 타입을 sting형으로 선언
    strBox.setValue("Hello"); // Value값에 "Hello"가 들어가게됨
    cout << strBox.getValue() << endl;
}
