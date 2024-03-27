#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    int num;

    ifstream inputFile("input.txt");
    inputFile >> num;
    long long numbers[num];

    for (int i = 0; i < num; i++) {
        long long sub;
        inputFile >> sub;
        numbers[i] = sub;
    }
    inputFile.close();

    long int localmax = INT_MIN;
    for (int i = 0; i < num; i++) {
        if (localmax < numbers[i]) {
            localmax = numbers[i];
        };
    }
    ofstream outputFile("output.txt");
    outputFile << localmax;
    outputFile.close();

    return 0;
}