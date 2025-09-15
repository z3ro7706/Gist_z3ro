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

void gcd_lcm_by_pointer(int a, int b, int *gcd, int *lcm)
{ // 최대공약수 최소공배수 코드
    int c, d;
    d = a * b;
    if (a < b)
    {
        swap_by_pointer(&a, &b); // 크기 정렬
    }
    while (b != 0)
    {
        c = a % b;
        a = b;
        b = c;
    }
    *gcd = a;
    *lcm = d / *gcd; // 포인터로 값 돌려주기
}

int main()
{
    int a, b;
    int gcd, lcm; // 사용할 변수 지정
    printf("Enter two integers : ");
    scanf("%d %d", &a, &b);

    printf("\n");
    printf("Using Call by Value : \n");
    printf("Sum = %d\n\n", sum_by_value(a, b));
    printf("Using Call by Pointer : \n");
    printf("Before swapping : a = %d, b = %d\n", a, b);
    swap_by_pointer(&a, &b);
    printf("Before swapping : a = %d, b = %d\n\n", a, b);
    printf("Using Call by Pointer for GCD & LCM : \n");
    gcd_lcm_by_pointer(a, b, &gcd, &lcm); // 포인터로 넣기
    printf("GCD = %d, LCM = %d\n", gcd, lcm);
    return 0;
}