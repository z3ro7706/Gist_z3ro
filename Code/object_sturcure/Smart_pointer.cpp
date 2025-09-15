#include <iostream>
#include <vector>
#include <memory>
using namespace std;

#if __cplusplus <= 201103L
#endif

class Test
{
    int data;

public:
    Test()
    {
        cout << "Input : ";
        cin >> data;
        cout << "Test constructor call (" << data << ")" << endl;
    }

    int get_data() const { return data; }

    ~Test()
    {
        cout << "Test delete constructor call (" << data << ")" << endl;
    }
};

unique_ptr<vector<shared_ptr<Test>>> make()
{
    return make_unique<vector<shared_ptr<Test>>>();
}

void fill(vector<shared_ptr<Test>> &vec, int num)
{
    for (int i = 0; i < num; ++i)
    {
        vec.push_back(make_shared<Test>());
    }
}

void display(const vector<shared_ptr<Test>> &vec)
{
    cout << "\ninput value :" << endl;
    for (const auto &t : vec)
    {
        cout << t->get_data() << endl;
    }
}

int main()
{
    auto vec_ptr = make(); // auto + make_unique 간결하게

    int num;
    cout << "Amount data : ";
    cin >> num;

    fill(*vec_ptr, num);
    display(*vec_ptr);

    return 0;
}
