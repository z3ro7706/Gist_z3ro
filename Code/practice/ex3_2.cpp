#include <iostream>
#include <vector>
using namespace std;

void add3(vector<int> &vec)
{ // templete vector
    int i;
    for (i = 0; i < vec.size(); i++)
    {
        vec[i] = vec[i] + 3;
    }
}
int main()
{
    vector<int> vec = {10, 20, 30, 40, 50};
    int i;
    int input1, input2;
    cout << "Enter an integer value : ";
    cin >> input1;
    cout << "Enter an integer value : ";
    cin >> input2;
    vec.push_back(input1); // 뒤에 값 넣기
    vec.push_back(input2);
    add3(vec);
    cout << "Vetor elements :";
    for (i = 0; i < vec.size(); i++)
    {
        cout << " " << vec[i];
    }
    cout << "" << endl;
    cout << "" << endl;
    return 0;
}
