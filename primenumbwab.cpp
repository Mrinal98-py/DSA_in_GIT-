#include<iostream>
using namespace std;
int main(){
    
    int a,b;
    cin >>a>>b;
    for (a;a<=b;a++)
    {
        int i;
        for(i = 2 ; i <=b ; i++)
        {
            if (b%i==0 ){
                break;
            }

        }
        if (i==a){
            cout << a;
        }
    }



    return 0;
}