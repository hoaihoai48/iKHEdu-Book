#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int u, v;
    long long w;
};

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i), root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            return true;
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) cin >> edges[i].u >> edges[i].v >> edges[i].w;

    sort(edges.begin(), edges.end(), [](const Edge &a, const Edge &b) {
        return a.w < b.w;
    });

    DSU dsu(n);
    long long mst_weight = 0;
    int edge_count = 0;

    for (const auto &e : edges) {
        if (dsu.unite(e.u, e.v)) {
            mst_weight += e.w;
            edge_count++;
            if (edge_count == n - 1) break;
        }
    }

    cout << (edge_count == n - 1 ? mst_weight : -1) << "\n";
    return 0;
}
