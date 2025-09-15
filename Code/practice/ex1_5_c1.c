#include <stdio.h>
#include <stdlib.h>

// 구조 설정
typedef struct
{
    char name[50];
    int ID;
    float score;
} Student;

// 학생 정보 받기
void inputStudent(Student *students)
{
    int i;
    i = 0;
    printf("Enter name : ");
    scanf(" %49[^\n]", students[i].name);
    printf("Enter ID : ");
    scanf("%d", &students[i].ID);
    printf("Enter Score : ");
    scanf("%f", &students[i].score);
}

// 학생정보 출력
void outputStudent(Student *students)
{
    int i = 0;
    printf("[Student Information]\n");
    printf("Name : %s\n", students[i].name);
    printf("ID : %d\n", students[i].ID);
    printf("Score : %.2f\n", students[i].score);
}

int main()
{
    Student *students;
    students = (Student *)malloc(3 * sizeof(Student));

    inputStudent(students);
    printf("\n");
    outputStudent(students);
    return 0;
}