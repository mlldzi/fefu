#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    vector<pair<int, int>> p;
    int n, s;
    fin >> n >> s;

    for (int i = 0; i < n; i++) {
        int x, y;
        fin >> x >> y;
        p.push_back({x, y});
    }

    sort(p.begin(), p.end());

    vector<int> x(n, 0);
    int best_c = 0;
    int xa, ya, xb, yb;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (p[i].second <= p[j].second) {
                int l = (p[j].second - p[i].second > 0) ? s / (p[j].second - p[i].second) : 2 * (p[n - 1].first - p[0].first);
                int m = 0;

                for (int k = 0; k < n; k++) {
                    if (p[i].second <= p[k].second && p[k].second <= p[j].second) {
                        x[m] = p[k].first;
                        m++;
                    }
                }

                int k1 = 0;
                int k2 = -1;
                int c = 0;

                while (k2 < m - 1) {
                    k2++;
                    c++;

                    while (x[k2] - x[k1] > l) {
                        k1++;
                        c--;
                    }

                    if (c > best_c) {
                        best_c = c;
                        xa = x[k1];
                        ya = p[i].second;
                        xb = x[k2];
                        yb = p[j].second;
                    }
                }
            }
        }
    }

    fout << xa << " " << ya << " " << xb << " " << yb;

    fin.close();
    fout.close();

    return 0;
}