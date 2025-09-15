#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int count_i(vector<int> &integer, int target)
{
    if (integer.size() == 0)
    {
        return 0;
    }
    else
    {
        int sum = count_if(integer.begin(), integer.end(), [target](int x)
                           { return x == target; });
        return sum;
    }
}
int main()
{
    vector<int> integer;
    int value;
    int i;
    int target;
    cout << "Enter numbers (-1 to stop) : ";
    while (true)
    {
        cin >> value;
        if (value == -1)
        {
            break;
        }
        else
        {
            integer.push_back(value);
        }
    }
    cout << "Enter numbers to fin : ";
    cin >> target;
    int count = count_i(integer, target);
    if (count == 0)
    {
        cout << target << " is not in the vector" << endl;
    }
    else
    {
        cout << target << " is in the vector" << endl;
    }

    cout << "" << endl;
}
