#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    vector<int> numbers;
    int value, i;
    cout << "Enter numbers(-1 to stop) : ";
    while (true)
    {
        cin >> value;
        if (value == -1)
        {
            break;
        }
        else
        {
            numbers.push_back(value);
        }
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