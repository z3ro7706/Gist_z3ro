#include <iostream>
class MyClass
{
private:
public:
    int *data;
    MyClass(int value)
    {
        data = new int(value);
    }
    ~MyClass()
    {
        delete data;
    }
    MyClass(const MyClass &other)
    {
        data = new int(*other.data);
    }
    bool operator==(const MyClass other) const
    {
        return *data == *(other.data);
    }
    void setData(int value)
    {
        *data = value;
    }
};
int main()
{
    MyClass obj1(10);
    MyClass obj2 = obj1;
    MyClass obj3(obj1);
    obj1.setData(20);
    if (obj1 == obj3)
        std::cout << "obj1 and obj2 are equal" << std::endl;
    else
        std::cout << "obj1 and obj2 are not equal" << std::endl;
    return 0;
}
