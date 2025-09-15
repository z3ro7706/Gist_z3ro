#include <iostream>
#include <stack> // STL stack 사용

class editor
{
public:
    editor(char c) : content(c) {}

    void setcontent(char c)
    {
        history.push(content); // 변경 전 상태 저장
        content = c;
    }

    void undo()
    {
        if (!history.empty())
        {
            content = history.top();
            history.pop();
        }
    }

    char getcontent() const
    {
        return content;
    }

private:
    char content;
    std::stack<char> history; // 이전 상태 저장용 스택
};

int main()
{
    editor editor1('a');                            // 초기 content = 'a'
    editor1.setcontent('b');                        // 'a' -> 'b'
    editor1.setcontent('c');                        // 'b' -> 'c'
    editor1.undo();                                 // 'c' -> 'b'
    std::cout << editor1.getcontent() << std::endl; // 출력: b
    editor1.undo();                                 // 'b' -> 'a'
    std::cout << editor1.getcontent() << std::endl; // 출력: a
    return 0;
}
