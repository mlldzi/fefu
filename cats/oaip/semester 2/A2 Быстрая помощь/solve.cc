#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int partition(vector<int> &arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] > pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(vector<int> &arr, int low, int high) {
    if (low < high) {
        int pivotIndex = partition(arr, low, high);

        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);
    }
}

int main() {
    int N, L;
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    fin >> N >> L;

    vector<int> flight_times(N);
    for (int i = 0; i < N; i++) {
        fin >> flight_times[i];
    }

    quickSort(flight_times, 0, N - 1);

    int max_time = 0;
    for (int i = 0; i < N; i++) {
        int current_time = flight_times[i] + i * L;
        max_time = max(max_time, current_time);
    }

    fout << max_time + L << endl;

    return 0;
}
