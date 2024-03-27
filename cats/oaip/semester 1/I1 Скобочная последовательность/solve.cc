#include <iostream>
#include <string>
#include <vector>

using namespace std;

int max_depth(const string& s) {
    vector<char> stack;
    int max_depth = 0;
    int current_depth = 0;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            stack.push_back(c);
            current_depth++;
            max_depth = max(max_depth, current_depth);
        } else if (c == ')' || c == ']' || c == '}') {
            if (stack.empty()) {
                return -1;
            }
            char top = stack.back();
            stack.pop_back();
            current_depth--;
            if ((c == ')' && top != '(') || (c == ']' && top != '[') || (c == '}' && top != '{')) {
                return -1;
            }
        }
    }
    if (!stack.empty()) {
        return -1;
    }
    return max_depth;
}

int main() {
    string s;
    cin >> s;
    int result = max_depth(s);
    cout << result << endl;
    return 0;
}
