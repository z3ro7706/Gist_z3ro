#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    char name[50];
    float score;
} Student;

int main()
{
    int i, n, s, j, a;
    Student *student;
    float totalscore, averagescore;
    totalscore = 0;
    averagescore = 0;
    printf("Enter the number of student : ");
    scanf("%d", &n);
    printf("\n");
    if (n == 0)
    {
        return 1;
    }
    student = (Student *)malloc(n * sizeof(Student)); // dynamic memory
    for (i = 0; i < n; i++)                           // 값 받기
    {
        printf("Enter student name : ");
        scanf("%s", student[i].name);
        printf("Enter student score : ");
        scanf("%f", &student[i].score);
        printf("\n");
        totalscore = totalscore + student[i].score;
    }
    averagescore = totalscore / n;
    printf("Average socre of all stduent : %.2f\n", averagescore);
    printf("\n");
    printf("Students with scores above or euqal to average : \n");
    for (i = 0; i < n; i++)
    {
        if (averagescore < student[i].score)
        {
            printf("%s - %.f\n", student[i].name, student[i].score);
        }
    }
    free(student);
    return 0;
}
