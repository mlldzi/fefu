#include <iostream>
#include <cmath>

using namespace std;

int main() {
    long double x;

    cin >> x;
    if (sqrt(x * 8 + 1) == int(sqrt(x * 8 + 1))) {
        cout << 1;
        return 0;
    }

    long double lower = 0;
    unsigned long long int n;
    n = (sqrt(8 * x + 1) - 1) / 2;
    for (unsigned long long int i = n; i > 0; --i) {
        lower = x - (i * (i + 1) / 2);
        if (sqrt(lower * 8 + 1) == int(sqrt(lower * 8 + 1))) {
            cout << 2;
            return 0;
        }
    }
    
    cout << 3;
    return 0;
}