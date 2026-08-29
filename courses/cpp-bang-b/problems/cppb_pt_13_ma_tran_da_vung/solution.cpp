#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<vector<long long>> p(n + 1, vector<long long>(m + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            long long val;
            cin >> val;
            p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + val;
        }
    }

    auto query = [&](int x1, int y1, int x2, int y2) -> long long {
        return p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1];
    };

    while (q--) {
        int x1, y1, x2, y2, u1, v1, u2, v2;
        cin >> x1 >> y1 >> x2 >> y2 >> u1 >> v1 >> u2 >> v2;
        cout << query(x1, y1, x2, y2) + query(u1, v1, u2, v2) << "\n";
    }

    return 0;
}
