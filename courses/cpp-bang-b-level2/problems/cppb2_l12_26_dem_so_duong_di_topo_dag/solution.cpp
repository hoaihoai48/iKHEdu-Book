#include <bits/stdc++.h>
using namespace std;

// Đếm số đường đi từ S đến T trên đồ thị có hướng không chu trình DAG
const int MOD = 1000000007;
const int MAXN = 100005;

vector<int> adj[MAXN];
int in_degree[MAXN];
long long dp[MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        in_degree[v]++;
    }

    queue<int> q;
    for (int i = 1; i <= n; ++i) {
        if (in_degree[i] == 0) q.push(i);
    }

    dp[s] = 1;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            dp[v] = (dp[v] + dp[u]) % MOD;
            in_degree[v]--;
            if (in_degree[v] == 0) q.push(v);
        }
    }

    cout << dp[t] << "\n";
    return 0;
}
