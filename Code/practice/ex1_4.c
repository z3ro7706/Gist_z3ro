#include <stdio.h>
#include <stdlib.h>

typedef struct // Information 지정
{
    char name[50];
    int ID;
    float score;
} Information;
void calculate_average(Information *informations, float *average_score) // 평균값 구하는 함수
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
    for (i = 0; i < 5; i++) // 값 받기
    {
        printf("Enter name of student %d : ", i + 1);
        scanf(" %49[^\n]", informations[i].name);
        printf("Enter ID of student %d : ", i + 1);
        scanf("%d", &informations[i].ID);
        printf("Enter score of student %d : ", i + 1);
        scanf("%f", &informations[i].score);
    }
    printf("\n");
    calculate_average(informations, &averageScore);
    printf("Average score of all students : %.2f\n", averageScore);
    free(informations);
    return 0;
}