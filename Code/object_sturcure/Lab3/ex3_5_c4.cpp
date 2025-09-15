#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void push_vector(vector<int> &scores, int value)
{
    scores.push_back(value);
}

double count_i(const vector<int> &scores)
{

    if (scores.empty())
    {
        return 0;
    }
    int sum = count_if(scores.begin(), scores.end(), [](int x)
                       { return x > 5; });

    return sum;
}
int main()
{
    vector<int> scores;
    int value;
    int i;
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
    double count = count_i(scores);
    cout << "Number of integers greater than 5: " << count << endl;
    cout << "" << endl;
}
