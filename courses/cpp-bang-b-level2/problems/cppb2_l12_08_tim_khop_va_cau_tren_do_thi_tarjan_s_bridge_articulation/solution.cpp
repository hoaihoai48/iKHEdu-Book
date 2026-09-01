#include <bits/stdc++.h>
using namespace std;

int timer = 0, scc_count = 0;
void dfs_scc(int u, const vector<vector<int>> &adj, vector<int> &tin, vector<int> &low, stack<int> &st, vector<bool> &in_st) {
    tin[u] = low[u] = ++timer;
    st.push(u);
    in_st[u] = true;

    for (int v : adj[u]) {
        if (!tin[v]) {
            dfs_scc(v, adj, tin, low, st, in_st);
            low[u] = min(low[u], low[v]);
        } else if (in_st[v]) {
            low[u] = min(low[u], tin[v]);
        }
    }

    if (low[u] == tin[u]) {
        scc_count++;
        while (true) {
            int node = st.top(); st.pop();
            in_st[node] = false;
            if (node == u) break;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
    }

    vector<int> tin(n + 1, 0), low(n + 1, 0);
    vector<bool> in_st(n + 1, false);
    stack<int> st;

    for (int i = 1; i <= n; ++i) {
        if (!tin[i]) dfs_scc(i, adj, tin, low, st, in_st);
    }

    cout << scc_count << "\n";
    return 0;
}
