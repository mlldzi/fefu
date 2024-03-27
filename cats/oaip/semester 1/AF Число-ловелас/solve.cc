#include <iostream>
#include <string>

using namespace std;

string hex(unsigned long long int n) {
    string result = "";

    while (n > 0) {
        int digit = n % 16;
        char hexDigit;
        if (digit < 10) hexDigit = digit;
        else hexDigit = 'a' + digit - 10;
        result = hexDigit + result;
        n /= 16;
    }
    return result;
}


int main() {
    unsigned long long int number;
    cin >> number;
    string hex_num = hex(number);

    if (hex_num.find("babe") != string::npos) cout << "YES";
    else cout << "NO";

    return 0;
}