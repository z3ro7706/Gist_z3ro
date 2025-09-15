#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void push_vector(vector<int> &scores, int value)
{
    scores.push_back(value);
}

double count_if(const vector<int> &scores)
{
    {
        if (scores.empty())
        {
            return 0;
        }
        int i, sum = 0;
        for (i = 0; i < 10; i++)
        {
            if ((scores[i] % 2) == 0)
            {
                sum = sum + 1;
            }
        }
        return sum;
    }
}
int main()
{
    vector<int> scores;
    int value;
    int i;
    cout << "Generated numbers : ";
    for (i = 0; i < 10; i++)
    {
        cin >> value;
        push_vector(scores, value);
    }
    double count = count_if(scores);
    cout << "Number of even numbers : " << count << endl;
    cout << "" << endl;
}
