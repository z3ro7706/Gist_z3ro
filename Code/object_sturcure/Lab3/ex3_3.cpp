#include <iostream>
#include <vector>
using namespace std;

inline float average(vector<int> &vec)
{
    int i;
    float sum = 0, average = 0;
    for (i = 0; i < vec.size(); i++)
    {
        sum += vec[i];
    }
    average = sum / (vec.size());
    return average;
}

int main()
{
    vector<int> vec = {};
    int i = 0, num;
    float value;
    for (;;)
    {
        cout << "Enter the score(-1 to exit) : ";
        cin >> num;
        if (num == -1)
        {
            break;
        }
        else
        {
            vec.push_back(num);
        }
    }
    value = average(vec);
    cout << "Average score : " << value << endl;
    return 0;
}