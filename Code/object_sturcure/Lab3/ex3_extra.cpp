#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void push_vector(vector<int> &scores, int value)
{
    scores.push_back(value);
}

double count_i(const vector<int> &scores, int target)
{

    if (scores.empty())
    {
        return 0;
    }
    int sum = count_if(scores.begin(), scores.end(), [target](int x)
                       { return x == target; });

    return sum;
}
int main()
{
    vector<int> scores;
    int value;
    int i;
    int target = 0;
    cout << "Generated numbers : ";
    while (true)
    {
        cin >> value;

        if (value == -1)
        {
            break;
        }
        push_vector(scores, value);
    }
    cout << "Enter the nubmer to find : ";
    cin >> target;
    double count = count_i(scores, target);
    if (count == 0)
    {
        cout << target << " is not in the vector. " << endl;
    }
    else
    {
        cout << target << " is in the vector. " << endl;
    }
    cout << "" << endl;
    return 0;
}
