#include <bits/stdc++.h>
using namespace std;
#define int int64_t
#define pb push_back
#define vec vector<int>
#define vpl vector<pair<int, int>>
#define fastInOut ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define F first
#define S second
#define flush cout<<endl;
#define endl "\n" 
#define yes cout<<"YES"<<endl; 
#define no cout<<"NO"<<endl; 
#define all(v) v.begin(),v.end()



void solve()
{
  int x;
  string s;
  cin>>x>>s;
  int c=0,C=0;
  for(int i=0;i<14;i++)if(s[i]=='C')c++;else if(s[i]=='N')C++;
  if(c==C)cout<<55*x<<endl;
  else if(c>C)cout<<60*x<<endl;
  else cout<<40*x<<endl;
}


int32_t main()
{
  fastInOut;
  int t=1;
  cin >> t;
  for(int i=1;i<=t;i++)
   {
      solve();
   }

}
