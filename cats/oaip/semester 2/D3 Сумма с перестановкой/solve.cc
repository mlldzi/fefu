#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool checkNumber(int a, int b) {
    int flag = 0;
    string aStr = to_string(a);
    string bStr = to_string(b);
    vector<int> arr1(128), arr2(128);
    for (size_t i = 0; i < aStr.size(); i++) {
        arr1[aStr[i]]++;
        arr2[bStr[i]]++;
    }
    for (int i = 47; i < 59; i++) {
        if (arr1[i] != arr2[i]) {
            flag++;
        }
    }
    if (flag == 0) {
        return true;
    }
    return false;
}

void permuteAndCheck(const string& s, int b, int sum, int n, int h = 0) {
    static int counter = 1;
    if (h == n)
        counter++;
    if (h == n && s[0] != '0' && checkNumber(sum - stoi(s), b)) {
        ofstream fout("output.txt");
        fout << "YES" << endl;
        fout << stoi(s) << " " << sum - stoi(s) << endl;
        exit(0);
    }
    else {
        for (int thread = h; thread < n; thread++) {
            string temp = s;
            swap(temp[h], temp[thread]);
            permuteAndCheck(temp, b, sum, n, h + 1);
        }
    }
}

int main() {
    ifstream fin("input.txt");
    int a, b, sum;
    fin >> a >> b >> sum;
    string aStr = to_string(a);
    permuteAndCheck(aStr, b, sum, aStr.size(), 0);
    ofstream fout("output.txt");
    fout << "NO";
    return 0;
}
