#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string find(int x, int y, int numerator1 = 0, int denominator1 = 1, int numerator2 = 1, int denominator2 = 0) {
    int m = numerator1 + numerator2;
    int n = denominator1 + denominator2;
    
    if (x == m && y == n) {
        return "";
    } else if (x * n < y * m) {
        return "L" + find(x, y, numerator1, denominator1, m, n);
    } else {
        return "R" + find(x, y, m, n, numerator2, denominator2);
    }
}

int main() {
    ifstream inputFile("input.txt");
    int x, y;
    inputFile >> x >> y;
    inputFile.close();
    
    ofstream outputFile("output.txt");
    outputFile << find(x, y);
    outputFile.close();
    return 0;
}