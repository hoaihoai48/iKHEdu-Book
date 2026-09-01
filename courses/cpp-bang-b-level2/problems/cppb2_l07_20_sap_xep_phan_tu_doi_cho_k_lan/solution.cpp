#include <bits/stdc++.h>
using namespace std;

// Tìm mảng lớn nhất có thể đạt được sau tối đa K lần đổi chỗ kề nhau
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    for (int i = 0; i < n && k > 0; ++i) {
        int max_idx = i;
        for (int j = i + 1; j < n && j - i <= k; ++j) {
            if (a[j] > a[max_idx]) {
                max_idx = j;
            }
        }
        for (int j = max_idx; j > i; --j) {
            swap(a[j], a[j - 1]);
        }
        k -= (max_idx - i);
    }

    for (int val : a) cout << val << " ";
    cout << "\n";
    return 0;
}
