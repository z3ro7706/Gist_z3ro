#include <stdio.h>

int Summation(int n)
{
    if (n == 0)
    {
        return 0;
    }
    else
    {
        return n + Summation(n - 1);
    }
}

int main()
{
    int n;
    printf("Enter your value : ");
    scanf("%d", &n);
    printf("%d Summation is %d \n", n, Summation(n));
    return 0;
}