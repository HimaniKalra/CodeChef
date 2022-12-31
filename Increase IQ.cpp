#include<iostream>
#define ll long long
using namespace std;

void solve()
{
	ll n;
	cin >> n;
	ll t;
	t = n + 7;
	if (t > 170)
		cout << "YES\n";
	else
		cout << "NO\n";
}

int main()
{
	solve();
	return 0;
}
