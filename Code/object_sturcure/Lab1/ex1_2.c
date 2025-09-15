#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    char name[50];
    float score;
} Student;

int main()
{
    int n, i;
    Student *student; // 포인터로 지정해주기
    float totalnumber, averagenumber;
    totalnumber = 0.0;
    printf("Enter the nuber of students : ");
    scanf("%d", &n);
    printf("\n");

    // maloc으로 받을 데이터 구성해주기(connect for typedef struct)
    if (n == 0)
    {
        printf("No Student in this class\n");
        return 1;
    }
    student = (Student *)malloc(n * sizeof(Student));

    // 학생들에게 데이터 받기
    for (i = 0; i < n; i++)
    {
        printf("Enter student name : ");
        scanf(" %49[^\n]", student[i].name);
        printf("Enter student score : ");
        scanf("%f", &student[i].score);
        printf("\n");
        totalnumber = totalnumber + student[i].score;
    }
    // 평균값 출력
    averagenumber = totalnumber / n;
    printf("Average score of all student : %.2f \n", averagenumber);
    printf("\n");

    // 평균값 이상 이상 출력
    printf("Student with scores above or eual to average : \n");
    for (i = 0; i < n; i++)
    {
        if (student[i].score >= averagenumber)
        {
            printf("%s - %.f\n", student[i].name, student[i].score);
        }
    }
    free(student);
    return 0;
}