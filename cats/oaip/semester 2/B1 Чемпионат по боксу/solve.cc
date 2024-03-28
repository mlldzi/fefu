#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int get_position(vector<int>& data, int size, int value) {
    int left = 0, right = size - 1;
    int position = 0;
    while (left <= right) {
        int middle = left + (right - left) / 2;
        if (data[middle] < value) {
            position = middle + 1;
            left = middle + 1;
        } else {
            right = middle - 1;
        }
    }
    return position;
}

struct Boxer {
    int pwr;
    int ctg;
    int impact;
};

int main() {
    ifstream inputFile("input.txt");
    int N, M;
    inputFile >> N >> M;
    vector<Boxer> pahom_boxers(N);
    vector<vector<int>> other_boxers_data(M, vector<int>());
    vector<int> other_boxers_index(M, 0);

    for (int i = 0; i < N; ++i) {
        int p, c;
        inputFile >> p >> c;
        pahom_boxers[i] = {p, c, 0};
    }

    for (int i = 0; i < N; ++i) {
        int p, c;
        inputFile >> p >> c;
        other_boxers_data[c - 1].push_back(p);
        other_boxers_index[c - 1]++;
    }

    sort(pahom_boxers.begin(), pahom_boxers.end(), [](const Boxer& a, const Boxer& b) {
        return a.pwr < b.pwr;
    });

    for (auto& cat : other_boxers_data) {
        sort(cat.begin(), cat.end());
    }

    int default_wins = 0;
    int mx_delta_wins = 0;

    for (auto& cur_boxer : pahom_boxers) {
        auto& cat = other_boxers_data[cur_boxer.ctg - 1];
        int pos = get_position(cat, other_boxers_index[cur_boxer.ctg - 1], cur_boxer.pwr);
        cur_boxer.impact = pos - (other_boxers_index[cur_boxer.ctg - 1] - pos);
        default_wins += cur_boxer.impact;
    }

    for (size_t i = 0; i < other_boxers_data.size(); ++i) {
        int enemy_p = other_boxers_index[i];
        auto& data = other_boxers_data[i];
        for (int pahom_p = N - 1; pahom_p >= 0; --pahom_p) {
            auto& cur_boxer = pahom_boxers[pahom_p];
            if (cur_boxer.ctg == i + 1) {
                continue;
            }
            while (enemy_p - 1 >= 0 && data[enemy_p - 1] > cur_boxer.pwr) {
                enemy_p--;
            }
            int new_impact = enemy_p - (other_boxers_index[i] - enemy_p);
            if (new_impact - cur_boxer.impact > mx_delta_wins) {
                mx_delta_wins = new_impact - cur_boxer.impact;
            }
        }
    }

    ofstream outputFile("output.txt");
    outputFile << default_wins + mx_delta_wins;

    return 0;
}