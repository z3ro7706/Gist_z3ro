#include <iostream>
#include "Brand.h"

using namespace std;

brand::brand() // 디폴트 삼각형
{
    Brand = "Unkwon";
    Year = 2000;
}

brand::brand(string b, int y)
{
    Brand = b;
    Year = y;
}

void brand::ShowInfo()
{
    cout << "Brand : " << Brand << ", year : " << Year << endl;
}
