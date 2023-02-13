#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
       int n;
       cin>>n;
       long long a[n];
        long long sum = 0;
        bool getAns = false;
       for(int i=0;i<n;i++) {
           cin>>a[i];
           sum += a[i];
           if(a[i] == 1) {
               getAns = true;
           }
       }
        if(getAns) {
            cout<<"CHEF"<<endl;
        }
        else {    
        if(sum % 2 != 0) {
            cout<<"CHEF"<<endl;
        }
        else {
            cout<<"CHEFINA"<<endl;
        }  
        }

    }
    return 0;
}
