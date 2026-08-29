#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> a(n + 1, vector<long long>(m + 1));
    vector<vector<long long>> p(n + 1, vector<long long>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            cin >> a[i][j];
            p[i][j] = p[i - 1][j] + a[i][j]; // Tiền tố theo cột
        }
    }

    long long max_sum = -4e18;

    for (int r1 = 1; r1 <= n; ++r1) {
        for (int r2 = r1; r2 <= n; ++r2) {
            long long current_kadane = 0;
            for (int c = 1; c <= m; ++c) {
                long long val = p[r2][c] - p[r1 - 1][c];
                current_kadane = max(val, current_kadane + val);
                max_sum = max(max_sum, current_kadane);
            }
        }
    }

    cout << max_sum << "\n";
    return 0;
}
