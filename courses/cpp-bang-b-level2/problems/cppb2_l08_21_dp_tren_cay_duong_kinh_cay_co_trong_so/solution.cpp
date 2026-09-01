#include <bits/stdc++.h>
using namespace std;

// Tree DP tìm đường kính cây có trọng số O(N)
const int MAXN = 200005;
vector<pair<int, long long>> adj[MAXN];
long long dp[MAXN]; // Độ dài đường đi dài nhất từ u xuống cây con
long long max_diameter = 0;

void dfs(int u, int p) {
    dp[u] = 0;
    long long max1 = 0, max2 = 0;

    for (auto edge : adj[u]) {
        int v = edge.first;
        long long w = edge.second;
        if (v == p) continue;

        dfs(v, u);
        long long d = dp[v] + w;
        if (d > max1) {
            max2 = max1;
            max1 = d;
        } else if (d > max2) {
            max2 = d;
        }
    }

    dp[u] = max1;
    max_diameter = max(max_diameter, max1 + max2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < n - 1; ++i) {
        int u, v; long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    dfs(1, 0);

    cout << max_diameter << "\n";
    return 0;
}
