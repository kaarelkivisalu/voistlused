#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    long long n;
    long long k[1000000];
    long long summa = 0;
    long long vastus = 0;
    long long uussumma;
    long long poolsumma;

    fin.open("jagasis.txt");
    fin >> n;

    for(int i=0; i<n; i++)
    {
        fin >> k[i];
        summa += k[i];
    }

    fin.close();

    fout.open("jagaval.txt");

    poolsumma = summa / 2 + 1;
    uussumma = 0;
    if(summa == 0)
        vastus = n/2;
    else
    {
        while(uussumma < poolsumma)
        {
            uussumma += k[vastus];
            vastus++;
        }

        if(abs(summa - 2 * uussumma) <= abs(summa - 2 * uussumma + 2 * k[vastus-1]))
        {
            vastus = vastus;
        }
        else
        {
            vastus = max(vastus - 1, (long long) 1);
        }
    }

    fout << vastus;
    fout.close();
}
