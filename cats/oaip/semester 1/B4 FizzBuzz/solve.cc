#include <iostream>

using namespace std;

int main() {
    int num;
    cin >> num;
    if (num % 5 == 0 and num % 3 == 0) {
        cout << "FizzBuzz";
    }
    if (num % 5 != 0 and num % 3 == 0) {
        cout << "Fizz";
    }
    if (num % 5 == 0 and num % 3 != 0) {
        cout << "Buzz";
    }
    if (num % 5 != 0 and num % 3 != 0) {
        cout << "\n";
    }
}