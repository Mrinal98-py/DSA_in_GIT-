#include<iostream>
#include<string>
#include<vector>
using namespace std;

vector<int> decToBinary(int n) {
    vector<int> vect;
    while (n > 0) {
        vect.push_back(n % 2);
        n = n / 2;
    }
    reverse(vect.begin(), vect.end());
    return vect;
}

int maxSignal(vector<char> strInput) {
    int max_diff_bits = 0;

    // Convert binary string to integer
    int num = 0;
    for (char bit : strInput) {
        num = num * 2 + (bit - '0');
    }

    // Compare with all possible numbers with same number of bits
    vector<int> binary_rep = decToBinary(num);
    int num_bits = binary_rep.size();

    for (int i = 0; i < (1 << num_bits); ++i) {
        vector<int> current_bits;
        for (int j = 0; j < num_bits; ++j) {
            if (i & (1 << j))
                current_bits.push_back(1);
            else
                current_bits.push_back(0);
        }

        int diff_bits = 0;
        for (int j = 0; j < num_bits; ++j) {
            if (current_bits[j] != binary_rep[j])
                diff_bits++;
        }

        max_diff_bits = max(max_diff_bits, diff_bits);
    }

    return max_diff_bits;
}

int main() {
    //input for strInput
    int strInput_size;
    cin >> strInput_size;
    vector<char> strInput;
    for (int idx = 0; idx < strInput_size; idx++) {
        char temp;
        cin >> temp;
        strInput.push_back(temp);
    }

    int result = maxSignal(strInput);
    cout << result;

    return 0;
}
