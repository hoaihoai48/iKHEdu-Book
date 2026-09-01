#include <bits/stdc++.h>
using namespace std;

bool check(long long max_sum, const vector<vector<long long>> &pref, int n, int m, int k) {
    int cuts = 0;
    int last_r = 0;
    for (int r = 1; r <= n; ++r) {
        long long row_max = 0;
        int last_c = 0;
        for (int c = 1; c <= m; ++c) {
            long long sub = pref[r][c] - pref[last_r][c] - pref[r][last_c] + pref[last_r][last_c];
            row_max = max(row_max, sub);
        }
        if (row_max > max_sum) {
            cuts++;
            last_r = r - 1;
            if (last_r < 0) return false;
        }
    }
    return cuts <= k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<vector<long long>> a(n + 1, vector<long long>(m + 1, 0));
    vector<vector<long long>> pref(n + 1, vector<long long>(m + 1, 0));

    long long low = 0, high = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            cin >> a[i][j];
            low = max(low, a[i][j]);
            high += a[i][j];
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + a[i][j];
        }
    }

    long long ans = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, pref, n, m, k)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
