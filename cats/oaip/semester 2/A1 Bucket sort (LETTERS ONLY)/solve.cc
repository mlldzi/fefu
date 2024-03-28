#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

void fill(std::string word, std::vector<std::vector<std::string>>& layer, int depth) {
    int index_of_chr;
    if (isupper(word[depth])) {
        index_of_chr = word[depth] - 'A';  // 0 - 25 (A - Z)
    } else {
        index_of_chr = word[depth] - 'a' + 26;  // 26 - 51 (a - z)
    }
    layer[index_of_chr].push_back(word);
}

std::vector<std::string> radix_sort(std::vector<std::string> words) {
    std::vector<std::string> res;
    std::vector<std::vector<std::string>> layer(52, std::vector<std::string>());
    for (const std::string& word : words) {
        fill(word, layer, 2);
    }
    std::vector<std::string> flat_layer;
    for (const auto& l : layer) {
        flat_layer.insert(flat_layer.end(), l.begin(), l.end());
    }

    for (int depth = 0; depth < 2; depth++) {
        std::vector<std::vector<std::string>> upper_layer(52, std::vector<std::string>());
        for (const std::string& word : flat_layer) {
            fill(word, upper_layer, 1 - depth);
        }
        flat_layer.clear();
        for (const auto& l : upper_layer) {
            flat_layer.insert(flat_layer.end(), l.begin(), l.end());
        }
    }
    return flat_layer;
}

int main() {
    std::ifstream file("input.txt");
    int n;
    file >> n;
    std::vector<std::string> data(n);
    for (int i = 0; i < n; i++) {
        file >> data[i];
    }
    file.close();

    std::vector<std::string> sorted_data = radix_sort(data);

    std::ofstream output_file("output.txt");
    for (const std::string& word : sorted_data) {
        output_file << word << "\n";
    }
    output_file.close();

    return 0;
}
