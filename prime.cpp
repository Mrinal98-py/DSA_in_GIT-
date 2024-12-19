#include<iostream>
using namespace std;
int main(){
    int a;
    cin>> a;
    for( int i= 2; i<a; i++)
    {
        if (a%i==0)
        {
            cout << "not prime";
            break;
        }
        else{
            cout<< "print prime";
            break;
         }
    }
    return 0;
}