#include <fstream>

using namespace std;

int main() {

    ifstream input_file("input.txt");
    ofstream output_file("output.txt");

    int n, res = 0;
    char a, b;

    input_file >> n;
    input_file >> a;

    for (int i = 1; i < n; ++i) {

        input_file >> b;
        if (a != b) {
            res++;
            a = b;
        }
    }
    if (b == 'B') res++;

    output_file << res;
}