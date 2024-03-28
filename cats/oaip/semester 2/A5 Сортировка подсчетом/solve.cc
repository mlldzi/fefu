#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> counting_sort(vector<pair<int, int>> &arr) {
    int max_key = max_element(arr.begin(), arr.end(), [](const auto &a, const auto &b) {
        return a.first < b.first;
    })->first;

    vector<int> count(max_key + 1, 0);

    for (const auto &pair: arr) {
        count[pair.first]++;
    }

    for (int i = 1; i < count.size(); i++) {
        count[i] += count[i - 1];
    }

    vector<int> sorted_arr(arr.size(), 0);

    for (auto it = arr.rbegin(); it != arr.rend(); ++it) {
        count[it->first]--;
        sorted_arr[count[it->first]] = it->second;
    }

    return sorted_arr;
}

int main() {
    ifstream input_file("input.txt");
    int n;
    input_file >> n;

    vector<pair<int, int>> data(n);

    for (int i = 0; i < n; i++) {
        input_file >> data[i].first >> data[i].second;
    }

    input_file.close();

    vector<int> sorted_data = counting_sort(data);

    ofstream output_file("output.txt");

    for (const auto &num: sorted_data) {
        output_file << num << " ";
    }

    output_file.close();

    return 0;
}
