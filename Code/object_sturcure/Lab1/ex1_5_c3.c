#include <stdio.h>
#include <stdlib.h>

#include <stdio.h>
#include <stdlib.h>

// 구조 설정
typedef struct
{
    char name[50];
    int age;
    float grade;
} Student;

// 학생 정보 받기
void inputStudent(Student *students)
{
    int i;
    i = 0;
    printf("Enter initial name, age, and grade : ");
    scanf(" %49[^ ] %d %f", students[i].name, &students[i].age, &students[i].grade);
}

// 학생정보 출력
void outputStudent(Student *students)
{
    int i = 0;
    printf("Before Update : \n");
    printf("Name : %s", students[i].name);
    printf(", Age : %d", students[i].age);
    printf(", Grade : %.2f\n", students[i].grade);
}
void updateStudent(Student *students)
{
    int i;
    i = 0;
    printf("Enter initial name, age, and grade : ");
    scanf(" %49[^ ] %d %f", students[i].name, &students[i].age, &students[i].grade);
}

// 학생정보 출력
void replaceStudent(Student *students)
{
    int i = 0;
    printf("After Update : \n");
    printf("Name : %s", students[i].name);
    printf(", Age : %d", students[i].age);
    printf(", Grade : %.1f\n", students[i].grade);
}

int main()
{
    Student *students;
    students = (Student *)malloc(3 * sizeof(Student));

    inputStudent(students);
    printf("\n");
    outputStudent(students);
    printf("\n");
    updateStudent(students);
    printf("\n");
    replaceStudent(students);
    return 0;
}