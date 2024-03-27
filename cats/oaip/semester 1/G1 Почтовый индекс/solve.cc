#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Index {
public:
    string buffer;
    int size;

    Index(string buffer = "", int size = 0) : buffer(buffer), size(size) {}
};

void init_buffer_to(Index& dist, char c) {
    if (dist.size > 0) {
        return;
    }
    dist.buffer = c;
    dist.size = 1;
}

void try_replace_index(Index& which, Index& src) {
    if (src.size == 0 || src.buffer[0] == '0') {
        src.buffer = "";
        return;
    }
    if (which.size == 0 || which.buffer[0] == '0' || which.size > src.size || (which.size == src.size && which.buffer > src.buffer)) {
        which.buffer = src.buffer;
        which.size = src.size;
        src.buffer = "";
    }
}

int main() {
    int straight[] = {6, 2, 3, 2, 4, 5, 4, 2, 7, 4};
    int slope[] = {0, 1, 1, 2, 0, 0, 1, 1, 0, 1};
    int a, b;
    cin >> a >> b;

    if (a == 6 && b == 0 || b > a) {
        cout << "Wrong" << endl;
        return 0;
    }

    int rows = a + 7;
    int cols = b + 3;
    vector<Index> matrix(rows * cols);

    for (int k = 0; k < 10; k++) {
        init_buffer_to(matrix[straight[k] * cols + slope[k]], '0' + k);
    }

    for (int row = 0; row < a; row++) {
        for (int col = 0; col <= b; col++) {
            Index& current_index = matrix[row * cols + col];

            if (current_index.size > 0) {
                for (int k = 0; k < 10; k++) {
                    Index next_index;
                    next_index.buffer = current_index.buffer + to_string(k);
                    next_index.size = current_index.size + 1;
                    try_replace_index(matrix[(straight[k] + row) * cols + slope[k] + col], next_index);

                    next_index.buffer = "";
                    next_index.size = 0;
                }

                current_index.buffer = "";
                current_index.size = 0;
            }
        }
    }

    Index& result_index = matrix[a * cols + b];

    if (result_index.size > 0) {
        cout << result_index.buffer.substr(0, result_index.size) << endl;
    } else {
        cout << "Wrong" << endl;
    }

    return 0;
}
