#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    vector<int> isvowel(256, 0);
    string vowels = "aeiouyAEIOUY";
    for (char i : vowels) {
        isvowel[int(i)] = 1;
    }

    int N, M;
    fin >> N >> M;

    vector<pair<int, bool>> arrN;
    vector<pair<int, bool>> arrM;

    string line;
    getline(fin, line);

    for (int i = 0; i < N; i++) {
        getline(fin, line);
        int num = 0;
        bool exclamation = false;
        for (char j : line) {
            if (isvowel[int(j)]) {
                num++;
            }
            if (j == '!') {
                exclamation = true;
            }
        }
        arrN.push_back(make_pair(num, exclamation));
    }

    for (int i = 0; i < M; i++) {
        getline(fin, line);
        int num = 0;
        bool exclamation = false;
        for (char j : line) {
            if (isvowel[int(j)]) {
                num++;
            }
            if (j == '!') {
                exclamation = true;
            }
        }
        arrM.push_back(make_pair(num, exclamation));
    }

    vector<vector<int>> dp(M, vector<int>(N, 0));

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            if (arrN[j] == arrM[i]) {
                dp[i][j] = arrN[j].first;
            } else {
                dp[i][j] = 0;
            }

            if (i > 0 && j > 0) {
                dp[i][j] += dp[i - 1][j - 1];
                int max_val = max(dp[i - 1][j], dp[i][j - 1]);
                dp[i][j] = max(dp[i][j], max_val);
            } else {
                if (i > 0 && dp[i][j] <= dp[i - 1][j]) {
                    dp[i][j] = dp[i - 1][j];
                }
                if (j > 0 && dp[i][j] <= dp[i][j - 1]) {
                    dp[i][j] = dp[i][j - 1];
                }
            }
        }
    }

    fout << dp[M - 1][N - 1] << endl;

    fin.close();
    fout.close();

    return 0;
}
