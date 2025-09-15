#include <stdio.h>

int Factorial(int n)
{
    if (n == 0)
    {
        return 1;
    }
    else
    {
        return n * Factorial(n - 1); // Recursive(점화적) 으로 작동하게 됨
    }
}
int main()
{
    int n;
    printf("Enter your n! : ");
    scanf("%d", &n);
    printf("%d! is %d \n ", n, Factorial(n));
    return 0;
}