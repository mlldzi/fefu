#include <iostream>
#include <set>
#include <fstream>

using namespace std;

int main() {
    int N;

    ifstream inputFile("input.txt");
    inputFile >> N;

    string str(1000000, 'Z');
    set<char> uniqueLetters;

    for (int i = 0; i < N; ++i) {
        char alpha;
        int start, end;
        inputFile >> alpha >> start >> end;

        for (int j = start - 1; j < end; j++) {
            str[j] = alpha;
        }
    }

    for (char letter : str) {
        uniqueLetters.insert(letter);
    }
    inputFile.close();

    ofstream outputFile("output.txt");
    outputFile << uniqueLetters.size() << endl;

    return 0;
}
