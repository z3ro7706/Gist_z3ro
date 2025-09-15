#include <iostream>
using namespace std;

int big(int a, int b)
{
    if (a >= b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

int big(int a[], int size)
{
    int i;
    if (size == 0)
    {
        cout << "There's no number" << endl;
        return 1;
    }
    int max = a[0];
    for (i = 0; i < size; i++)
    {
        if (a[i] > max)
        {
            max = a[i];
        }
    }
    return max;
}

int main()
{
    int array[5] = {1, 9, -2, 10, 6};
    cout << big(4, 7) << endl;
    cout << big(array, 5) << endl;
    return 0;
}