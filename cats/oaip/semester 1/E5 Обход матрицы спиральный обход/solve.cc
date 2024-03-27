#include <fstream>
#include <iostream>

using namespace std;

int main() {
    int n;
    ifstream inputFile("input.txt");
    inputFile >> n;
    inputFile.close();

    int matrix[n][n];
    int iStart = 0, iEnd = 0, jStart = 0, jEnd = 0;
    int i = 0, j = 0, current = 1;
    while (current <= n * n) {
        matrix[i][j] = current;
        if (i == iStart && j < n - jEnd - 1) ++j; // right
        else if (j == n - jEnd - 1 && i < n - iEnd - 1) ++i; // down
        else if (i == n - iEnd - 1 && j > iStart) --j; // left
        else --i;

        if ((i == iStart + 1) && (j == jStart)) {
            ++iStart;
            ++jStart;
            ++iEnd;
            ++jEnd;
        }
        ++current;
    }

    ofstream outputFile("output.txt");
    for (int I = 0; I < n; ++I) {
        for (int J = 0; J < n; ++J) {
            outputFile << matrix[I][J] << " ";
        }
        outputFile << "\n";
    }
    outputFile.close();

    return 0;
}
