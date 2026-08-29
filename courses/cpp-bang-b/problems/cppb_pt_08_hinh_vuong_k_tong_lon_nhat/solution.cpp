#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<vector<long long>> p(n + 1, vector<long long>(m + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            long long val;
            cin >> val;
            p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + val;
        }
    }

    long long max_sum = -4e18; // Khởi tạo âm vô cùng
    for (int i = k; i <= n; ++i) {
        for (int j = k; j <= m; ++j) {
            long long current = p[i][j] - p[i - k][j] - p[i][j - k] + p[i - k][j - k];
            max_sum = max(max_sum, current);
        }
    }

    cout << max_sum << "\n";
    return 0;
}
