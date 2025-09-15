#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int count_i(vector<int> &integer)
{
    if (integer.size() == 0)
    {
        return 0;
    }
    else
    {
        int sum = count_if(integer.begin(), integer.end(), [](int x)
                           { return x > 5; });
        return sum;
    }
}
int main()
{
    vector<int> integer;
    int value;
    int i;
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
    int count = count_i(integer);
    cout << "Number of integers greater than 5 : " << count << endl;
    cout << "" << endl;
}
