// 값을 받고 이를 Stl을 이용하여 정렬, 오름차순 & 내림차순 출력
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void push_vector(vector<int> &numbers, int value)
{
    numbers.push_back(value);
}
int main()
{
    vector<int> numbers;
    int value;
    int i;

    cout << "Enter number (-1 to stop) : ";
    while (true)
    {
        cin >> value;
        if (value == -1)
        {
            break;
        }
        push_vector(numbers, value);
    }
    sort(numbers.begin(), numbers.end());
    cout << "Sorted in ascending order : ";
    for (i = 0; i < numbers.size(); i++)
    {
        cout << numbers[i] << " ";
    }
    cout << "" << endl;
    cout << "Sorted in descending order : ";
    for (i = (numbers.size()) - 1; i >= 0; i--)
    {
        cout << numbers[i] << " ";
    }
    cout << "" << endl;
    cout << "" << endl;
    return 0;
}