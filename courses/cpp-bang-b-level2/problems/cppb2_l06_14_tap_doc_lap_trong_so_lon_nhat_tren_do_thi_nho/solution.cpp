#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> val(n);
    for (int i = 0; i < n; ++i) cin >> val[i];

    vector<int> adj_mask(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v; u--; v--;
        adj_mask[u] |= (1 << v);
        adj_mask[v] |= (1 << u);
    }

    long long max_val = 0;
    for (int mask = 0; mask < (1 << n); ++mask) {
        bool valid = true;
        long long sum = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                if (mask & adj_mask[i]) { valid = false; break; }
                sum += val[i];
            }
        }
        if (valid) max_val = max(max_val, sum);
    }

    cout << max_val << "\n";
    return 0;
}
