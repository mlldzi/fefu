#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, m, r;
    cin >> N;
    vector<int> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    int mid_sum = -1;
    int l = -1;

    for (int i = 0; i < N; i++) {
        int left_sum = 0;
        int right_sum = arr[i];
        int mid_pos = i + 1;

        for (int j = i; j < N; j++) {
            right_sum -= arr[j];
            left_sum += arr[j];

            while (mid_pos < N && right_sum < left_sum) {
                right_sum += arr[mid_pos];
                mid_pos++;
            }

            if (left_sum == right_sum && mid_sum < left_sum) {
                mid_sum = left_sum;
                l = i;
                m = j;
                r = mid_pos;
            }
        }
    }

    if (l == -1) cout << "-1";
    else cout << l + 1 << " " << m + 1 << " " << r;

    return 0;
}