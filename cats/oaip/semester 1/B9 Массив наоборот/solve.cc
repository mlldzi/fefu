#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    int num;
    ifstream inputFile("input.txt");
    string line;
    inputFile >> num;
    long long numbers[num];
    for (int i = 0; i < num; i++) {
        long long sub;
        inputFile >> sub;
        numbers[i] = sub;
    }
    inputFile.close();

    ofstream outputFile("output.txt");
    for (int i = num - 1; i >= 0; i--) {
            outputFile << numbers[i] << " ";
        }
    outputFile.close();

    return 0;
}