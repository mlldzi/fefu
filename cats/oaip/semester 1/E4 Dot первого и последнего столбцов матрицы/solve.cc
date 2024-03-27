#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<long double>> matrix;
    for (int i = 0; i < N; i++) {
        vector<long double> row;
        for (int j = 0; j < M; j++) {
            long double sub;
            cin >> sub;
            row.push_back(sub);
        }
        matrix.push_back(row);
    }
    long double result = 0;
    for (int i = 0; i < N; i++) {
        result += (matrix[i][0] * matrix[i][M - 1]);
    }
    cout << result << endl;
    return 0;
}