// 짝수 갯수 출력하기 (-1 넣으면 멈춤)
#include <iostream>
#include <vector>

using namespace std;

// 값을 하나씩 받아서 score에 추가하기(이래야 -1 감지 가능)
void push_vector(vector<int> &score, int value) // vector<자료형> &<자료구조>
{
    score.push_back(value);
}
// even판정 밑 오류 반정
double count_if(const vector<int> &score) // const(읽기전용)으로 하여 잘못된 값 반영 안함
{
    int i, sum;
    sum = 0;
    if (score.empty())
    {
        return 0.0;
    }
    for (i = 0; i < score.size(); i++)
    {
        if ((score[i] % 2) == 0) // even인지 확인
        {
            sum = sum + 1;
        }
    }
    return sum;
}
int main()
{
    vector<int> score;
    int input;

    cout << "Enter numbers (-1 to stop) : ";
    while (true) // 항상 루프로 들어가기 위함
    {
        cin >> input;
        if (input == -1)
        {
            break;
        }
        push_vector(score, input); // score과 입력값을 받아냄
    }
    int count = count_if(score); // sum 값이 even의 갯수를 표현해줌
    cout << "Number of even numbers : " << count << endl;
    return 0;
}