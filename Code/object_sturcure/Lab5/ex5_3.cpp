#include <iostream>
using namespace std;

int main()
{
    int numerator, denominator;

    cout << "Enter numerator: ";
    cin >> numerator;

    cout << "Enter denominator: ";
    cin >> denominator;

    try // 예외가 발생하는 부분에 대한 트라이(오류를 따로 확인해준다.)
    {
        if (denominator == 0)               // if denominator =0
            throw "Cannot divide by zero!"; // throw를 통해서 문장을 catch로 넘겨줌

        cout << "Result: " << numerator / denominator << endl; // 아닌경우에 대한 출력
    }
    catch (const char *msg) // try에서 throw된 값을 받아서 사용한다.
    {
        cout << "Exception: " << msg << endl;
    }

    return 0;
}
