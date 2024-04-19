#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>

const int MAX = 1000000;

class Condition {
public:
    int l, r, op;

    Condition(int l, int r, int op) : l(l), r(r), op(op) {}
};

std::vector<Condition> Conditions;
std::vector<int> Number(7);

Condition to_cond(std::string l) {
    std::unordered_map<std::string, int> normal = {
            {"=",  1},
            {">",  2},
            {"<",  3},
            {"<>", 4},
            {">=", 5},
            {"<=", 6}
    };
    std::unordered_map<std::string, int> html = {
            {"&gt;",     2},
            {"&lt;",     3},
            {"&lt;&gt;", 4},
            {"&gt;=",    5},
            {"&lt;=",    6}
    };
    std::string operand = l.substr(1, l.size() - 2);
    int temp;
    try {
        temp = normal.at(operand);
    } catch (...) {
        temp = html.at(operand);
    }
    return Condition(l[0] - '0', l[l.size() - 1] - '0', temp);
}

bool is_right(int j) {
    int op = Conditions[j].op;
    int l = Conditions[j].l;
    int r = Conditions[j].r;
    switch (op) {
        case 1:
            return Number[l] == Number[r];
        case 2:
            return Number[l] > Number[r];
        case 3:
            return Number[l] < Number[r];
        case 4:
            return Number[l] != Number[r];
        case 5:
            return Number[l] >= Number[r];
        case 6:
            return Number[l] <= Number[r];
        default:
            return false;
    }
}

void increment() {
    int k = 6;
    Number[k]++;
    while (Number[k] == 10) {
        Number[k] = 0;
        k--;
        Number[k]++;
    }
}

int main() {
    std::ifstream fin("input.txt");
    std::ofstream fout("output.txt");

    std::string line;
    while (std::getline(fin, line)) {
        Conditions.push_back(to_cond(line));
    }

    int count = 0;
    Number.assign(7, 0);
    for (int i = 0; i < MAX; ++i) {
        count++;
        for (int j = 0; j < Conditions.size(); ++j) {
            if (!is_right(j)) {
                count--;
                break;
            }
        }
        increment();
    }

    fout << count;

    return 0;
}