#include <iostream>
#include <fstream>


using namespace std;

int main() {
    long long a, b, c, d;

    ifstream inputFile("input.txt");
    inputFile >> a >> b >> c >> d;
    inputFile.close();

    long long nums[4] = {a, b, c, d};
    int local_max = INT_MIN, local_min = INT_MAX;
    for (int elem: nums) {
        if (elem > local_max) local_max = elem;
        if (elem < local_min) local_min = elem;
    }

    int sum_of_evens = 0;
    for (int num: nums) {
        if (num % 2 == 0) {
            sum_of_evens += num;
        }
    }

    ofstream outputFile("output.txt");
    if ((a + b + c + d) % 2 == 0 && (a * b * c * d) >= 0) outputFile << local_max;
    if ((a + b + c + d) % 2 != 0 && (a * b * c * d) >= 0) outputFile << local_min;
    if ((a * b * c * d) < 0) outputFile << sum_of_evens;
    outputFile.close();
    return 0;
}