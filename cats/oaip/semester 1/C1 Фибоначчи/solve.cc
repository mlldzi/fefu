#include iostream
#include fstream
#include string
#include vector


using namespace std;

int main() {
    vectorunsigned long long int numbers = {0, 1};
    int num;

    ifstream inputFile(input.txt);
    if (inputFile.is_open()) {
        string line;
        inputFile  num;
        inputFile.close();
    }
    for (int i = 2; i  num; i++) {
        unsigned long long int q = numbers[i - 1] + numbers[i - 2];
        numbers.push_back(q);
    }
    ofstream outputFile(output.txt);
    if (outputFile.is_open()) {
        for (int i = 0; i  num; i++) {
            outputFile  numbers[i]   ;
        }
        outputFile.close();
    }
    return 0;
}