#include <stdio.h>

int main()
{
    // array 구성
    int i, j;
    int a[4] = {2, 4, 0, 5};
    j = sizeof(a) / sizeof(a[0]); // sizeof(a)는 4*4로 16피트, sizeof(a[0])는 1개의 원소의 비트이므로 4
    printf("List of array : ");

    // 문제에서 주어지는 조건 추가
    a[1] = 2;

    // array 출력
    for (i = 0; i < j; i++)
    {

        printf(" %d ", a[i]);
    }
    printf("\n");
    return 0;
}
