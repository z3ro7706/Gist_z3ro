#include <iostream>

// 합,차,곱의 주소값 출력(in inline) & 값 지정
inline void calculateOperation(int a, int b, int &sum, int &diff, int &product)
{
    std::cout << "sum : " << &sum << ", diff : " << &diff << ", product : " << &product << std::endl;
    sum = a + b;
    diff = a - b;
    product = a * b;
}

int main()
{
    // 변수 지정
    int sum, diff, product, num1, num2;

    // 값 input
    std ::cout << "Enter the first number : ";
    std ::cin >> num1;
    std ::cout << "ENter the second number : ";
    std ::cin >> num2;
    std ::cout << "Int main()" << std::endl;

    // 주소값 출력
    std ::cout << "Sum : " << &sum << ", diff : " << &diff << ", prodcut : " << &product << std::endl;
    std::cout << std::endl;

    calculateOperation(num1, num2, sum, diff, product);
    // 합,차,곱 출력
    std ::cout << "sum : " << sum << std::endl;
    std ::cout << "diff : " << diff << std::endl;
    std ::cout << "sum : " << product << std::endl;
    return 0;
}
