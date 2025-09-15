#include <stdio.h>
#include <stdlib.h>

// Information 지정
typedef struct
{
    char name[50];
    int ID;
    float score;
} Information;

// 평균값 구하는 함수
void calculate_average(Information *informations, float *average_score)
{
    int i;
    float total_score;
    total_score = 0;
    for (i = 0; i < 5; i++)
    {
        total_score = total_score + informations[i].score;
    }
    *average_score = total_score / 5;
}

int main()
{
    int i;
    Information *informations;
    float averageScore;
    informations = (Information *)malloc(5 * sizeof(Information));

    // 값 받기
    for (i = 0; i < 5; i++)
    {
        printf("Enter name of student %d : ", i + 1);
        scanf(" %49[^\n]", informations[i].name);
        printf("Enter ID of student %d : ", i + 1);
        scanf("%d", &informations[i].ID);
        printf("Enter score of student %d : ", i + 1);
        scanf("%f", &informations[i].score);
    }

    // 값 출력
    printf("\n");
    calculate_average(informations, &averageScore);
    printf("Average score of all students : %.2f\n", averageScore);
    free(informations);
    return 0;
}