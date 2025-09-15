#include <iostream>
#include <vector>
using namespace std;

int count_if(vector<int> vec)
{
    int i, count; // even 갯수 카운트
    count = 0;
    for (i = 0; i < vec.size(); i++)
    {
        if (vec[i] % 2 == 0)
        {
            count = count + 1;
        }
    }
    return count;
}
int main()
{
    vector<int> score;
    int input;
    cout << "Enter numbers (-1 to stop) : ";
    while (true) // 10 15 20 -1 이렇게 들어오는거 하나식 감지
    {
        cin >> input;
        if (input == -1)
        {
            break;
        }
        else
        {
            score.push_back(input);
        }
    }
    int count = count_if(score);
    cout << "Number of even numbers : " << count << endl;
    cout << endl;
}