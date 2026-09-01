#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<vector<long long>> a(n + 1, vector<long long>(m + 1, 0));
    vector<vector<long long>> pref(n + 1, vector<long long>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            cin >> a[i][j];
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + a[i][j];
        }
    }

    int count = 0;
    int max_len = min(n, m);
    for (int len = 1; len <= max_len; ++len) {
        for (int i = len; i <= n; ++i) {
            for (int j = len; j <= m; ++j) {
                long long sum = pref[i][j] - pref[i - len][j] - pref[i][j - len] + pref[i - len][j - len];
                if (sum == k) count++;
            }
        }
    }

    cout << count << "\n";
    return 0;
}
