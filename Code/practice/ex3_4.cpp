#include <iostream>
using namespace std;
template <typename T>
class box
{
private:
    T value;

public:
    void setValue(T val)
    {
        value = val;
    }
    T getValue() const
    {
        return value;
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