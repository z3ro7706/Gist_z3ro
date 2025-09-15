#include <iostream>
using namespace std;
class Student
{
private:
    string name;
    int id;

public:
    Student(string n = "UnKnown", int i = 0)
    {
        name = n;
        id = i;
    }

    bool operator==(const Student a)
    {
        return (name == a.name) && (id == a.id);
    }

    void display()
    {
        cout << name << "Id : " << id << endl;
    }
};

int main()
{
    Student s1("Alice", 101);
    Student s2("Alice", 101);
    Student s3("Bob", 102);

    cout << "Student 1 : ";
    s1.display();
    cout << "Student 2 : ";
    s2.display();
    cout << "Are the students the samne? : ";
    cout << (s1 == s2 ? "Yes" : "No") << endl
         << endl;

    cout << "Student 1 : ";
    s1.display();
    cout << "Student 3 : ";
    s3.display();
    cout << "Atre the stduent the smae? ";
    cout << (s1 == s3 ? "Yes" : "No") << endl;

    return 0;
}