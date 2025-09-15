#include <iostream>
using namespace std;

class Sample
{
private:
    int value;            // 멤버 변수
    static int copyCount; // 복사 생성자 호출 횟수

public:
    // 일반 생성자
    Sample(int v)
    {
        value = v;
        cout << "Constructor called: value = " << value << endl;
    }

    // 복사 생성자
    Sample(const Sample &other) // const + Class 이름 + &사용할 매개변수
    {
        value = other.value;
        copyCount++;
        cout << "Copy constructor called #" << copyCount << " (value = " << value << ")" << endl;
    }

    // 현재 값을 출력하는 함수
    void show() const
    {
        cout << "value = " << value << endl;
    }
};

// 정적 멤버 변수 정의
int Sample::copyCount = 0;

// 값을 복사해서 반환하는 함수 (복사 생성자 2번 호출됨)
Sample makeCopy(Sample s)
{
    return s;
}

int main()
{
    Sample a(10); // 일반 생성자 호출

    cout << "--- b = a ---" << endl;
    Sample b = a; // 복사 생성자 #1

    cout << "--- makeCopy(a) ---" << endl;
    Sample c = makeCopy(a); // 복사 생성자 #2 (전달), #3 (반환)

    cout << "--- End ---" << endl;

    return 0;
}
