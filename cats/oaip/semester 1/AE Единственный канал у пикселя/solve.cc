#include <iostream>

using namespace std;
int main() {
    int n, result;
    char m;
    cin >> n >> m;
    if (m == 'r') {
        result = n & 0xFF0000;
    }
    else if (m == 'g') {
        result = n & 0x00FF00;
    }
    else if (m == 'b') {
        result = n & 0x0000FF;
    }
    cout << result;
    return 0;
}