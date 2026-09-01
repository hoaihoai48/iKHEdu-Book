#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> a(n, vector<long long>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) cin >> a[i][j];
    }

    long long max_sum = -1e18;

    for (int r1 = 0; r1 < n; ++r1) {
        vector<long long> col_sum(m, 0);
        for (int r2 = r1; r2 < n; ++r2) {
            for (int c = 0; c < m; ++c) col_sum[c] += a[r2][c];

            long long cur_sum = 0;
            for (int c = 0; c < m; ++c) {
                cur_sum = max(col_sum[c], cur_sum + col_sum[c]);
                max_sum = max(max_sum, cur_sum);
            }
        }
    }

    cout << max_sum << "\n";
    return 0;
}
