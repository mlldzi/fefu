#include <fstream>
#include <iostream>

using namespace std;

int main() {
    unsigned int N;
    int nums[2001];

    for (int &num: nums) {
        num = 0;
    };

    ifstream inputFile("input.txt");
    inputFile >> N;
    for (int i = 0; i < N; i++) {
        int sub;
        inputFile >> sub;
        nums[1000 + sub] += 1;
    }
    inputFile.close();

    ofstream outputFile("output.txt");
    for (int i = 0; i < 2001; i++) {
        if (nums[i] != 0) outputFile << (i - 1000) << " " << nums[i] << endl;
    }
    outputFile.close();
    return 0;
}