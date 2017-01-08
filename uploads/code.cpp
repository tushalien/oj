#include<bits/stdc++.h>
#include <unistd.h>
using namespae std;
int fib[40000000];
int main(){
int i=0;
	int a ;
while(i<100000000)
i++;
    cin >> a;
    //int fib[a] ;
    fib[0] = 1;
    fib[1] = 1;
    for(int i = 2;i < a ;i++){
    	fib[i] = fib[i-1] + fib[i-2];
    }
    for(int i = 0;i < a ;i++){
    	cout << fib[i] << endl ;
    }
}