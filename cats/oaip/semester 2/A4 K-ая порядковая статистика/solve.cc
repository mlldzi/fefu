#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

int quick_select(vector<int>& arr, int low, int high, int k) {
    while (low < high) {
        int pi = partition(arr, low, high);
        if (pi == k - 1) {
            return arr[pi];
        } else if (pi > k - 1) {
            high = pi - 1;
        } else {
            low = pi + 1;
        }
    }
    return arr[low];
}

int main() {
    ifstream input("input.txt");
    int Q, V, P, N, K;
    input >> Q >> V >> P >> N >> K;
    
    vector<int> A(N);
    A[0] = P;
    for (int i = 1; i < N; i++) {
        A[i] = (A[i-1] * Q) % V;
    }

    int result = quick_select(A, 0, N - 1, K);

    ofstream output("output.txt");
    output << result;
    return 0;
}