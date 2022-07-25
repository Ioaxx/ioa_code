#include <iostream>
#include <fstream>
using namespace std;
int n, nr;
int main()
{
    //freopen("arbo.in", "r", stdin);
   // freopen("arbo.out", "w", stdout);

    cin >> n;
    cout<<n;
    
    while (n % 2 == 0)
    {
        n = n / 2;
        nr++;
    }
    if (nr > 1)
    {
        cout << "2^" << nr << "*";
    }
    for (int i = 3; i * i <= n; i += 2)
    {
        int nr = 0;
        while (n % i == 0)
        {
            nr++;
            n = n / i;
        }
        if (nr > 1)
        {

            cout << i << "^" << nr;
            if (n != 1)
                cout << "*";
        }
        else if (nr == 1)
        {
            cout << i << "*";
            if (n != 1)
                cout << "*";
        }
    }
    if (n > 1)
    {
        cout << n;
    }

} 
