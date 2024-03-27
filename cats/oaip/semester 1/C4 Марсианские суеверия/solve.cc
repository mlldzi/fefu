#include <fstream>
#include <iostream>

using namespace std;

int main() {
    ifstream inputFile("input.txt");
    long N, M, K, result;
    inputFile >> N >> M >> K;
    inputFile.close();

    ofstream outputFile("output.txt");
    if (K == 4 || K == 13) {outputFile << "-1"; outputFile.close(); return 0;}

    if (K >= 5) K -= 1;
    if (K >= 13) K -= 1;

    if (K > N*M) {outputFile << "-1"; outputFile.close(); return 0;}
    else {
        if (K % M == 0) result = K / M;
        else result = K / M + 1;

        if (result >= 12) result += 2;
        else if (result >= 4) result += 1;
    }

    outputFile << result;
    outputFile.close();
    return 0;
}