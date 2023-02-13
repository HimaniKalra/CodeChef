#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

#define mod 1000000007
#define iloop(i,n) for(int i = n-1; i >= 0; i--)
#define loop(i,n) for(int i = 0; i < n; i++)
#define loop1(i,n) for(int i = 1; i < n; i++)
#define loopx(i,m,n) for(int i = m; i < n; i++)
#define loopjiplus1(j,i,n) for(int j = i+1; j < n; j++)
#define loopji1(j,i,n) for(int j = i; j < n; j++)
ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }
ll lcm(ll a, ll b) { return a * (b / gcd(a, b)); }

int main() {
  // Faster IO
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  ll t; 
  cin>>t;
  while(t--){
    ll n;
    cin>>n;
    ll a[n];
    loop(i,n){
        cin>>a[i];
    }
    ll mini = INT_MAX;
    sort(a,a+n);
    loop1(i,n){
        // cout<<"a[i]: "<<a[i]<<"a[i-1]: "<<a[i-1]<<endl;
        if(a[i]-a[i-1] < mini){
            // cout<<"MINI: "<<mini<<endl;
            mini= a[i]-a[i-1];
        }
    }
    cout<<mini<<endl;
  }
  return 0;
}
