#include <iostream>
#include <fstream>
#include <cmath>


using namespace std;

int main() {
    long double a, b, c;
    long double x1, x2;
    ifstream inputFile("input.txt");
    inputFile >> a >> b >> c;
    inputFile.close();

    ofstream outputFile("output.txt");
    if (a == 0) {
        if (b == 0) {
            outputFile << "-1";
            outputFile.close();
            return 0;
        }
        x1 = -c / b;
        x2 = x1;
        outputFile << x1 << " " << x2;
        outputFile.close();
        return 0;
    }

    long double diskr;
    diskr = b * b - 4 * a * c;

    if (diskr < 0) {
        outputFile << -1;
        outputFile.close();
        return 0;
    }

    x1 = (-b + sqrt(diskr)) / (2 * a);
    x2 = (-b - sqrt(diskr)) / (2 * a);

    long double sub = x1;
    x1 = max(x1, x2);
    x2 = min(x2, sub);
    outputFile << x1 << " " << x2;
    outputFile.close();
    return 0;
}