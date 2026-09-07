#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    if (!(cin >> N >> M)) return 0;
    vector<vector<pair<int,int>>> adj(N + 1);
    for (int i = 0; i < M; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back({v, i}); adj[v].push_back({u, i});
    }
    if (M == 0) { cout << 1 << "\n"; return 0; }
    for (int v = 1; v <= N; v++) if (adj[v].size() % 2 == 1) { cout << "IMPOSSIBLE\n"; return 0; }
    vector<char> seen(N + 1, 0);
    vector<int> st; st.push_back(1); seen[1] = 1;
    while (!st.empty()) {
        int v = st.back(); st.pop_back();
        for (auto [to, id] : adj[v]) if (!seen[to]) { seen[to] = 1; st.push_back(to); }
    }
    for (int v = 1; v <= N; v++) if (!adj[v].empty() && !seen[v]) { cout << "IMPOSSIBLE\n"; return 0; }
    vector<char> used(max(1, M), 0);
    vector<size_t> ptr(N + 1, 0);
    vector<int> stack2; stack2.push_back(1);
    vector<int> circ;
    while (!stack2.empty()) {
        int v = stack2.back();
        while (ptr[v] < adj[v].size() && used[adj[v][ptr[v]].second]) ptr[v]++;
        if (ptr[v] == adj[v].size()) { circ.push_back(v); stack2.pop_back(); }
        else { auto [to, id] = adj[v][ptr[v]++]; used[id] = 1; stack2.push_back(to); }
    }
    if ((int)circ.size() != M + 1) { cout << "IMPOSSIBLE\n"; return 0; }
    for (int i = (int)circ.size() - 1; i >= 0; i--) {
        if (i != (int)circ.size() - 1) cout << ' ';
        cout << circ[i];
    }
    cout << "\n";
    return 0;
}
