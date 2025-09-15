#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    char name[50];
    int ID;
    float score;
} Student;

int main()
{
    int i, n, s, j, a;
    Student *student;
    n = 3;
    if (n == 0)
    {
        return 1;
    }
    student = (Student *)malloc(3 * sizeof(Student)); // dynamic memory
    for (i = 0; i < n; i++)                           // 값 받기
    {
        printf("Enter name of student %d : ", i + 1);
        scanf("%s", student[i].name);
        printf("Enter ID of Student %d : ", i + 1);
        scanf("%d", &student[i].ID);
        printf("Enter score of Student %d : ", i + 1);
        scanf("%f", &student[i].score);
        printf("\n");
    }
    for (i = 0; i < n; i++)
    {
        printf("Student %d Info : \n", i + 1);
        printf("Name : %s \n", student[i].name);
        printf("Id : %d\n", student[i].ID);
        printf("Score : %.2f\n", student[i].score);
        printf("\n");
    }
    free(student);
    return 0;
}
