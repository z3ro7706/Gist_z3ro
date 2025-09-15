#include <stdio.h>
#include <stdlib.h>

// 정보구성
typedef struct
{
    char name[50];
    int ID;
    float score;
} Information;

int main()
{
    int i;
    Information *informations;
    informations = (Information *)malloc(3 * sizeof(Information));

    // 학생 정보 값 받기
    for (i = 0; i < 3; i++)
    {
        printf("Enter name of student %d : ", i + 1);
        scanf(" %49[^\n]", informations[i].name);
        printf("Enter ID of student %d : ", i + 1);
        scanf("%d", &informations[i].ID);
        printf("Enter score of student %d : ", i + 1);
        scanf("%f", &informations[i].score);
    }
    printf("\n");

    // 학생 정보값 출력
    for (i = 0; i < 3; i++)
    {
        printf("Student %d Info : \n", i + 1);
        printf("Name : %s\n", informations[i].name);
        printf("ID : %d\n", informations[i].ID);
        printf("Score : %.2f\n", informations[i].score);
        printf("\n");
    }
    Information(free);
    return 0;
}