#include <iostream>
#include <cstring>

using namespace std;

int main() {
    float number;
    long long int exponent;
    cin >> number;
    memcpy(&exponent, &number, sizeof(number));
    exponent = exponent >> 23;
    exponent = exponent % 256;

    if (number == 0) {
        cout << '0';
        return 0;
    }

    if (exponent == 0) exponent = -126;
    else exponent -= 127;

    cout << exponent;
    return 0;
}