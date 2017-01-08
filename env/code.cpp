#include<bits/stdc++.h>
using namespace std;
int fib[4];
int main(){
	int a ;
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