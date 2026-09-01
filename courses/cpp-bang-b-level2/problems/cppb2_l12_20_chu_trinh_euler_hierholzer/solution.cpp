#include <bits/stdc++.h>
using namespace std;

// Thuật toán Hierholzer tìm chu trình Euler O(V + E)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<multiset<int>> adj(n + 1);
    vector<int> deg(n + 1, 0);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].insert(v);
        adj[v].insert(u);
        deg[u]++; deg[v]++;
    }

    for (int i = 1; i <= n; ++i) {
        if (deg[i] % 2 != 0) {
            cout << "IMPOSSIBLE\n";
            return 0;
        }
    }

    vector<int> circuit;
    stack<int> st;
    st.push(1);

    while (!st.empty()) {
        int u = st.top();
        if (!adj[u].empty()) {
            int v = *adj[u].begin();
            adj[u].erase(adj[u].begin());
            adj[v].erase(adj[v].find(u));
            st.push(v);
        } else {
            circuit.push_back(u);
            st.pop();
        }
    }

    if ((int)circuit.size() != m + 1) {
        cout << "IMPOSSIBLE\n";
        return 0;
    }

    for (int node : circuit) cout << node << " ";
    cout << "\n";
    return 0;
}
