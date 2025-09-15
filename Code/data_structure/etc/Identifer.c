#include <stdio.h>
int main()
{
    float tem, ori;
    tem = 98.6;
    printf("%f", tem);
    ori = tem;
    printf("%f", ori);
    tem = tem + 5;
    printf("%f", ori);
    return 0;
}