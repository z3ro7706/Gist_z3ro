#ifndef BRAND_H
#define BRAND_H

#include <string>
using namespace std;

class brand
{
    string Brand;
    int Year;

public:
    brand();                       // 고정값
    brand(string Brand, int Year); // 받는값
    void ShowInfo();               // 출력
};

#endif
