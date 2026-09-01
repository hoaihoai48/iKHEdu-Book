#include <bits/stdc++.h>
using namespace std;

// Biến đổi tọa độ quay 45 độ: u = x + y, v = x - y + N
const int MAXN = 2005;
long long diff[MAXN][MAXN], pref[MAXN][MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    while (q--) {
        int x, y, d; long long val;
        cin >> x >> y >> d >> val;
        int u1 = max(1, x + y - d), u2 = min(2 * n, x + y + d);
        int v1 = max(1, x - y + n - d), v2 = min(2 * n, x - y + n + d);

        diff[u1][v1] += val;
        diff[u1][v2 + 1] -= val;
        diff[u2 + 1][v1] -= val;
        diff[u2 + 1][v2 + 1] += val;
    }

    for (int i = 1; i <= 2 * n; ++i) {
        for (int j = 1; j <= 2 * n; ++j) {
            pref[i][j] = diff[i][j] + pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1];
        }
    }

    long long max_val = 0;
    for (int x = 1; x <= n; ++x) {
        for (int y = 1; y <= n; ++y) {
            int u = x + y;
            int v = x - y + n;
            max_val = max(max_val, pref[u][v]);
        }
    }

    cout << max_val << "\n";
    return 0;
}
