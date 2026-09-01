#include <bits/stdc++.h>
using namespace std;

// Kadane 2D tìm ma trận con có tổng lớn nhất O(N^3)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> a(n, vector<long long>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
        }
    }

    long long max_sum = LLONG_MIN;

    for (int top = 0; top < n; ++top) {
        vector<long long> temp(m, 0);
        for (int bottom = top; bottom < n; ++bottom) {
            for (int j = 0; j < m; ++j) {
                temp[j] += a[bottom][j];
            }

            // Kadane 1D
            long long current = 0;
            for (int j = 0; j < m; ++j) {
                current += temp[j];
                max_sum = max(max_sum, current);
                if (current < 0) current = 0;
            }
        }
    }

    cout << max_sum << "\n";
    return 0;
}
