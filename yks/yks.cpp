#include <bits/stdc++.h>
using namespace std;

int main()
{
  ifstream fin;
  ofstream fout;

  fin.open("ykssis.txt");
  int n0, m0;
  fin >> n0 >> m0;
  int now = n0 + 10 * m0;
  int max = 0;

  for (int i = 0; i < 6; ++i) {
	int n,m;
	fin >> n >>m;
	if (n + 10 * m > max)
	  max = n + m * 10;
	  }

  fin.close();

  fout.open("yksval.txt");

  if (now > max)
	fout << 0;
  else
	fout << max - now +1;

  fout.close();
}
