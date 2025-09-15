#include <iostream>
#include <vector>
using namespace std;

// 가지고 있는 함수값에 3을 더하는 void
void add3(vector<int> &vec)
{
    int i;
    for (i = 0; i < vec.size(); i++)
    {
        vec[i] += 3;
    }
}

int main()
{
    // 크기의 변경이 가능한 배열 vec생성
    vector<int> vec = {10, 20, 30, 40, 50};

    // value 값 받기
    int i;
    int input1, input2;
    cout << "Enter an integer value : ";
    cin >> input1;
    cout << "Enter an integer  value : ";
    cin >> input2;

    // vec 배열 뒤에 push_back을 이용하여 값 추가
    vec.push_back(input1);
    vec.push_back(input2);

    // 값들에 3추가
    add3(vec);

    // 출력
    cout << "Vector elements : ";
    for (i = 0; i < vec.size(); i++)
    {
        cout << vec[i] << " ";
    }
    cout << endl;

    return 0;
}