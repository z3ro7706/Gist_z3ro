#include <stdio.h>
int sum_by_value(int a, int b)
{
    int sum = a + b;
    return sum;
}

void swap_by_pointer(int *x, int *y)
{
    int swap = *x;
    *x = *y;
    *y = swap;
}

void gcd_lcm_by_ponter(int a, int b, int *gcd, int *lcm)
{
    int c, d;
    d = a * b;
    if (a < b)
    {
        swap_by_pointer(&a, &b);
    }
    while (b != 0)
    {
        c = a % b;
        a = b;
        b = c;
    }
    *gcd = a;
    *lcm = d / *gcd;
}

int main()
{
    int a, b;
    // 값 입력
    printf("Enter two integers : ");
    scanf("%d %d", &a, &b);
    printf("\n");

    // sum
    printf("Using Call by value : \n");
    printf("Sum = %d \n", sum_by_value(a, b));
    printf("\n");

    // swap
    printf("Using Call by pointer : \n");
    printf("Before swapping : a = %d, b= %d\n", a, b);
    swap_by_pointer(&a, &b);
    printf("After swapping : a = %d, b = %d\n", a, b);
    printf("\n");

    // GCD & LCM
    int gcd, lcm;
    printf("Using call by pointer for GCD & LCM : \n");
    gcd_lcm_by_ponter(a, b, &gcd, &lcm);
    printf("GCD = %d, LCM = %d \n", gcd, lcm);
    return 0;
}
