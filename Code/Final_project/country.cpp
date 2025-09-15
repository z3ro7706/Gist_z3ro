#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

class City
{
public:
    string name;
    long population;
    double cost;
};

class Country
{
public:
    string name;
    vector<City> cities;
};

class Tours
{
public:
    string title;
    vector<Country> countries;
};

void ruler()
{
    cout << "\n1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890\n"
         << endl;
}

void print(ostream &stream, Tours &tours)
{
    const int country_width = 20;
    const int city_width = 25;
    const int population_width = 20;
    const int cost_width = 10;

    stream << fixed << setprecision(2);
    stream << setw((country_width + city_width + population_width + cost_width) / 2 + tours.title.size() / 2) << tours.title << endl;
    stream << left << setw(country_width) << "Country"
           << setw(city_width) << "City"
           << setw(population_width) << "Population"
           << setw(cost_width) << "Price" << endl;
    stream << string(country_width + city_width + population_width + cost_width, '-') << endl;

    for (const auto &country : tours.countries)
    {
        bool first = true;
        for (const auto &city : country.cities)
        {
            if (first)
            {
                stream << left << setw(country_width) << country.name;
                first = false;
            }
            else
            {
                stream << setw(country_width) << "";
            }
            stream << left << setw(city_width) << city.name
                   << right << setw(population_width) << city.population
                   << right << setw(cost_width) << city.cost << endl;
        }
    }
}

int print_in_file(Tours &tours)
{
    ofstream ofs("tours_output.txt");
    if (!ofs)
    {
        cerr << "File could not be opened." << endl;
        return 1;
    }
    print(ofs, tours);
    ofs.close();
    return 0;
}

int main()
{
    Tours tours{"Tour Ticket Prices from Miami",
                {{"Colombia", {
                                  {"Bogota", 876768686, 400.98},
                                  {"Cali", 22334455, 425.98},
                                  {"Medellin", 12328686, 300.89},
                                  {"Cartagena", 89788721, 350.98},
                              }},
                 {"Brazil", {
                                {"Rio De Janiero", 123580000, 600.00},
                                {"Sao Paulo", 180343000, 970.00},
                                {"Salvador", 18280000, 600.00},
                            }}}};

    print(cout, tours);
    print_in_file(tours);

    return 0;
}
