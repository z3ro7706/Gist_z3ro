#include <iostream>
#include <vector>
using namespace std;

float average_score(vector<int> &vec)
{
    int i;
    float totalscore, averagescore;
    totalscore = 0;
    averagescore = 0;
    for (i = 0; i < vec.size(); i++)
    {
        totalscore = totalscore + vec[i];
    }
    averagescore = totalscore / (vec.size());
    return averagescore;
}
int main()
{
    vector<int> vec = {};
    int i = 0, n;
    while (true)
    {
        cout << "Enter the socre(-1 to exit) : ";
        cin >> n;
        if (n == -1)
        {
            break;
        }
        else
        {
            vec.push_back(n);
        }
    }

    cout << "Average score : " << average_score(vec) << endl;
    cout << "" << endl;
    return 0;
}