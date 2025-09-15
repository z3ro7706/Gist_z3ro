#include <stdio.h>

// 요일 지정 enum(열거형)
enum day_value
{
    SUNDAY = 1,
    MONDAY = 2,
    TUESDAY = 3,
    WEDNESDAY = 4,
    THURSDAY = 5,
    FRIDAY = 6,
    SATURDAY = 7
};

// 메인 함수
int main()
{
    int day;
    printf("Enter a number between 1 and 7 : ");
    scanf("%d", &day);
    switch (day) // 조건에 따라 출력값 지정
    {
    case SUNDAY:
    {
        printf("Sunday\n");
        break;
    }

    case TUESDAY:
    {
        printf("Tuesday\n");
        break;
    }

    case MONDAY:
    {
        printf("Monday\n");
        break;
    }

    case WEDNESDAY:
    {
        printf("Wednsday\n");
        break;
    }

    case THURSDAY:
    {
        printf("Thursday\n");
        break;
    }

    case FRIDAY:
    {
        printf("Friday\n");
        break;
    }

    case SATURDAY:
    {
        printf("Saturday\n");
        break;
    }
    default: // 이거 이외의 케이스 처리(유효하지 않은 값으로 처리)
    {
        printf("Invalid input ! please enter a number between 1 and 7 \n");
        break;
    }
    }

    return 0;
}
