#include <stdio.h>
#include <stdlib.h>

// 구조 설정
typedef struct
{
    char name[50];
    int ID;
    float scores[3];
} Student;

// 학생 정보 받기
void inputStudent(Student *students)
{
    printf("Enter name : ");
    scanf(" %49[^\n]", students[0].name);
    printf("Enter ID : ");
    scanf("%d", &students[0].ID);
    printf("Enter Scores for Subjects (e.g, Korean, English, Math) : ");
    scanf("%f %f %f", &students[0].scores[0], &students[0].scores[1], &students[0].scores[2]);
}

// 학생 평균값 계산하기
float calculateAverage(const Student *students)
{
    float total, average;
    total = 0;
    int i;
    for (i = 0; i < 3; i++)
    {
        total = total + students[0].scores[i];
    }
    average = total / 3;
    return average;
}

// 학생정보 출력
void outputStudent(Student *students)
{
    int i = 0;
    printf("[Student Information]\n");
    printf("Name : %s\n", students[i].name);
    printf("ID : %d\n", students[i].ID);
    printf("Score : %.2f %.2f %.2f\n", students[0].scores[0], students[0].scores[1], students[0].scores[2]);
    printf("Average Score : %.2f\n", calculateAverage(students));
}

int main()
{
    Student *students;
    students = (Student *)malloc(1 * sizeof(Student));

    inputStudent(students);
    printf("\n");
    outputStudent(students);
    return 0;
}