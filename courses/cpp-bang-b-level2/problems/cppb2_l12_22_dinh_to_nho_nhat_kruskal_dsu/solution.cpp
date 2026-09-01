#include <bits/stdc++.h>
using namespace std;

// Kruskal MST dùng vector<vector<long long>> {w, u, v} và mảng DSU nguyên bản
int parent_arr[200005];

int find_root(int i) {
    if (parent_arr[i] == i) return i;
    return parent_arr[i] = find_root(parent_arr[i]);
}

bool unite(int i, int j) {
    int root_i = find_root(i), root_j = find_root(j);
    if (root_i != root_j) {
        parent_arr[root_j] = root_i;
        return true;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> edges(m, vector<long long>(3));
    for (int i = 0; i < m; ++i) {
        int u, v; long long w;
        cin >> u >> v >> w;
        edges[i] = {w, u, v}; // {trọng số, u, v} để sort tăng dần
    }

    sort(edges.begin(), edges.end());

    for (int i = 1; i <= n; ++i) parent_arr[i] = i;

    long long mst_weight = 0;
    int edges_count = 0;

    for (const auto& e : edges) {
        long long w = e[0];
        int u = e[1], v = e[2];
        if (unite(u, v)) {
            mst_weight += w;
            edges_count++;
            if (edges_count == n - 1) break;
        }
    }

    if (edges_count != n - 1) cout << "IMPOSSIBLE\n";
    else cout << mst_weight << "\n";
    return 0;
}
