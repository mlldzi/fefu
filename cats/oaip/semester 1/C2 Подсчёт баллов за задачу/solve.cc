#include "iostream"
#include "fstream"


using namespace std;

int main() {
    unsigned int N, result = 0;
    string third;

    ifstream inputFile("input.txt");
    inputFile >> N;
    unsigned int points[N];

    if (inputFile.is_open()) {
        for (int i = 0; i < N; i++) {
            inputFile >> points[i];
        }
        inputFile >> third;
        inputFile.close();

    }

    for (int i = 0; i < N; i++) {
        if (third[i] == '+') {
            result += points[i];
        }
    }

    ofstream outputFile("output.txt");
    outputFile << result;
    outputFile.close();
    return 0;

}