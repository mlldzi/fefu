#include <fstream>
#include <cmath>

using namespace std;

bool check(long long int num, long long int n, long long int p, long long int c) {
    int month = 0;
    long double credit = c;
    long double last_credit = c;

    while (month < 12 * n) {
        credit -= num;
        if (credit <= 0) return true;

        double long temp = credit * p / 100.0;
        long long int adding = ceil(temp);
        credit += adding;

        if (credit > last_credit) return false;
        else last_credit = credit;

        month++;
    }

    return credit <= 0;
}

int main() {
    ifstream inputFile("input.txt");
    long long int n, p, c;
    inputFile >> n >> p >> c;
    inputFile.close();

    long long int l = 0;
    long long int r = c;

    while ((r - l) > 1) {
        long long int m = (r + l) / 2;
        if (check(m, n, p, c)) r = m;
        else l = m;
    }

    ofstream outputFile("output.txt");
    outputFile << r;
    outputFile.close();

    return 0;
}
