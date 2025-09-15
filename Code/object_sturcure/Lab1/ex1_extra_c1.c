#include <stdio.h>
#include <stdlib.h>

// struct 구성
typedef struct
{
    char name[50];
    int ID;
    float salary;
} Employee;

// employee 값 받기
void InputEmployee(Employee *e)
{
    int i;
    for (i = 0; i < 5; i++)
    {
        printf("Enter details for Employee %d : \n", i + 1);
        printf("Enter name : ");
        scanf(" %49[^\n]", e[i].name);
        printf("Enter ID : ");
        scanf("%d", &e[i].ID);
        printf("Enter details for Employee : ");
        scanf("%f", &e[i].salary);
    }
}

// employee값 출력
void printEmployee(Employee *e)
{
    int i;
    for (i = 0; i < 5; i++)
    {
        printf("Employee %d : \n", i + 1);
        printf("Name : %s\n", e[i].name);
        printf("ID : %d\n", e[i].ID);
        printf("Salary : %.2f\n", e[i].salary);
        printf("\n");
    }
}

int main()
{
    Employee *e;
    e = (Employee *)malloc(5 * sizeof(Employee));
    InputEmployee(e);
    printf("\n");
    printf("[Employee Information]\n");
    printf("\n");
    printEmployee(e);
    return 0;
}
