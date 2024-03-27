#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>



using namespace std;

int main() {
    long double result = 0;
    int num;

    ifstream inputFile("input.txt");
    if (inputFile.is_open()) {
        string line;
        inputFile >> num;
        for (int i = 0; i < num; i++) {
            long double sub;
            inputFile >> sub;
            result += sub;

        }
        inputFile.close();
    }

    ofstream outputFile("output.txt");
    if (outputFile.is_open()) {
        outputFile << result / num << endl;
        outputFile.close();
    }
    return 0;
}