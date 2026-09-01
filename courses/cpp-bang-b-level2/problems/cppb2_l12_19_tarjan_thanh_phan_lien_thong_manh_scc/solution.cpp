#include <bits/stdc++.h>
using namespace std;

// Tarjan tìm các thành phần liên thông mạnh SCC O(V + E)
const int MAXN = 100005;
vector<int> adj[MAXN];
int tin[MAXN], low[MAXN], timer;
bool on_stack[MAXN];
vector<int> st;
int scc_count = 0;

void dfs(int u) {
    tin[u] = low[u] = ++timer;
    st.push_back(u);
    on_stack[u] = true;

    for (int v : adj[u]) {
        if (!tin[v]) {
            dfs(v);
            low[u] = min(low[u], low[v]);
        } else if (on_stack[v]) {
            low[u] = min(low[u], tin[v]);
        }
    }

    if (low[u] == tin[u]) {
        scc_count++;
        while (true) {
            int v = st.back();
            st.pop_back();
            on_stack[v] = false;
            if (u == v) break;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }

    for (int i = 1; i <= n; ++i) {
        if (!tin[i]) dfs(i);
    }

    cout << scc_count << "\n";
    return 0;
}
