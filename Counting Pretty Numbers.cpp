#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	     int a,b;
	     cin>>a>>b;
	     int c=0;
	     for(int i=a;i<=b;i++){
	         if(i%10==2 || i%10==3 || i%10==9){
	             c++;
	         }
	     }cout<<c<<endl;
	}
	return 0;
}