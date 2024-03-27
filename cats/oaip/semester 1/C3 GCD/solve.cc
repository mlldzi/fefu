#include <iostream>

using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    else return gcd(b, a % b);
}


int main() {
    int a, b, c, A, B, C;
    cin >> a >> b >> c;
    A = gcd(a, b);
    B = gcd(a, c);
    C = gcd(b, c);
    cout << A << " " << B << " " << C << endl;
    return 0;
}