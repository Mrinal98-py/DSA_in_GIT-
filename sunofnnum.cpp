//sum of n number 
#include<iostream>
using namespace std;
int main (){
    int a , sum = 0 , i =0 ;
    cin >> a;
    for (i ; i <a+1 ; i++)
    {
        sum = sum + i;
    }
    cout << sum;
    return 0;
}