#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double long a, b, c, alpha;
    char X;
    cin >> a >> b >> c >> X >> alpha;

    double long num = a * alpha + c * b - alpha * alpha;
    double long den = a - alpha;

    if (num == 0 && den == 0) cout << "INF";
    else if (den == 0) cout << "NO";
    else cout << "YES" << endl << fixed << setprecision(4) << num / den;

    return 0;
}
