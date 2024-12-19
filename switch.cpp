#include<iostream>
using namespace std;
int main(){
    char n;
    cin>>n;

    switch(n)
    {
    case 'a':
        cout  << "a is the button";
        break;

    case 'b':
        cout  << "b is the button";
        break;  
                                           
    default:
        cout <<"key out of range";
        break;
    }

    return 0;
       }
