#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
	// 데이터 input & output
	ifstream in("scores.txt"); // scores.txt 파일을 불러옴
	ofstream out("result.txt");

	if (!in) // 데이터가 들어왔다면
	{
		cout << "Error opening scores.txt" << endl;
		return 1;
	}

	string name;
	int scores;
	int count = 0;
	int total = 0;

	while (in >> name >> scores)
	{
		if (scores > 0 && scores < 100)
		{
			cout << name << " " << scores << endl;
			total = total + scores;
			count++;
		}
	}
	if (count > 0)
	{
		double avg = static_cast<double>(total) / count;
		out << fixed << setprecision(2);

		out << " Average scores : " << avg << endl;
	}
	return 0;
}
