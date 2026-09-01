#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> adj_mask(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        adj_mask[u] |= (1 << v);
        adj_mask[v] |= (1 << u);
    }

    vector<bool> is_independent(1 << n, true);
    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                if (mask & adj_mask[i]) {
                    is_independent[mask] = false;
                    break;
                }
            }
        }
    }

    vector<int> dp(1 << n, 1e9);
    dp[0] = 0;

    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int sub = mask; sub > 0; sub = (sub - 1) & mask) {
            if (is_independent[sub]) {
                dp[mask] = min(dp[mask], dp[mask ^ sub] + 1);
            }
        }
    }

    cout << dp[(1 << n) - 1] << "\n";
    return 0;
}
