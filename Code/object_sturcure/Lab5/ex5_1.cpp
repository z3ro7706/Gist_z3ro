#include <iostream>
#include <string>

int check_even(int n)
{
    if ((n % 2) == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

template <typename I, typename T>
int count_if(I begin, I end, int (*condition)(T))
{
    int count = 0;
    for (I i = begin; i != end; i++)
    {
        if (condition(*i) == 1)
        {
            count = count + 1;
        }
    }
    return count;
}

int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int even_count = count_if(arr, arr + 10, check_even);
    std::cout << "Number of even elements : " << even_count << std::endl;
    return 0;
}