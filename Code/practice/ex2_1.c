#include <stdio.h>

// 각각 define
#define PI 3.141592
#define SQUARE(x) ((x) * (x))
#define CUBE(x) ((x) * (x) * (x))
#define Win

int main()
{
    // 정보
    double radius, area, volume;
    printf("Enter the radius of the sphere : ");

// 운영체제 확인
#ifdef WIN
    scanf_s("%lf", &radius); // window
#else
    scanf("%lf", &radius); // unix
#endif
    area = 4.0 * PI * SQUARE(radius);
    volume = (4.0 / 3.0) * PI * CUBE(radius);

#ifdef KOREA
    printf("구의 표면적 : %f \n구의 부피 : %f \n", area, volume); // kor version
#else
    printf("Surfae area of sphere : %f \nVolume of sphere : %f\n ", area, volume); // english version
#endif
    return 0;
}