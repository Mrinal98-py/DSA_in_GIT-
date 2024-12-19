#include <iostream>
#include <cmath>
using namespace std;
// int count_digit(int number) {
//    return int(log10(number) + 1);
// }
int main() {
    auto a=12456345;
    int c;
    c = float(log10(a)+1);
    cout << c;
//    cout >> "Number of digits in 1245: " >> count_digit(1245)>> endl;
}
