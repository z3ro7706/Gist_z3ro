#include <iostream>
using namespace std;

class Counter
{
private:
    int count;

public:
    Counter()
    {
        count = 0;
    }
    Counter(int c)
    {
        count = c;
    }

    Counter operator++() // prefix increase
    {
        ++count;
        return *this;
    }
    Counter operator++(int) // postfix increase
    {
        count++;
        return *this;
    }

    void display()
    {
        cout << "Count : " << count << endl;
    }
};
int main()
{
    Counter c(5);

    cout << "Initial ";
    c.display();

    ++c;
    cout << "After prefix increment ";
    c.display();

    c++;
    cout << "After postfix increment ";
    c.display();

    return 0;
}