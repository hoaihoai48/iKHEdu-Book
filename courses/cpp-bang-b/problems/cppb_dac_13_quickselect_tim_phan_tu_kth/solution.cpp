#include <bits/stdc++.h>
using namespace std;

int partition(vector<long long> &a, int l, int r) {
    int pivot_idx = l + rand() % (r - l + 1);
    swap(a[pivot_idx], a[r]);
    long long pivot = a[r];
    int i = l;
    for (int j = l; j < r; ++j) {
        if (a[j] <= pivot) {
            swap(a[i], a[j]);
            i++;
        }
    }
    swap(a[i], a[r]);
    return i;
}

long long quickSelect(vector<long long> &a, int l, int r, int k) {
    if (l == r) return a[l];
    int p = partition(a, l, r);
    int rank = p - l + 1;
    if (rank == k) return a[p];
    if (k < rank) return quickSelect(a, l, p - 1, k);
    return quickSelect(a, p + 1, r, k - rank);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    srand(42);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    cout << quickSelect(a, 0, n - 1, k) << "\n";
    return 0;
}
