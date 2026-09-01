#include <bits/stdc++.h>
using namespace std;

// Thuật toán Kruskal tìm cây khung nhỏ nhất MST bằng DSU O(E log E)
struct Edge {
    int u, v;
    long long w;
    bool operator<(const Edge& other) const {
        return w < other.w;
    }
};

struct DSU {
    vector<int> parent, rank_val;
    DSU(int n) {
        parent.resize(n + 1);
        rank_val.assign(n + 1, 0);
        for (int i = 1; i <= n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i), root_j = find(j);
        if (root_i != root_j) {
            if (rank_val[root_i] < rank_val[root_j]) swap(root_i, root_j);
            parent[root_j] = root_i;
            if (rank_val[root_i] == rank_val[root_j]) rank_val[root_i]++;
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
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    sort(edges.begin(), edges.end());
    DSU dsu(n);
    long long mst_weight = 0;
    int edges_count = 0;

    for (const auto& e : edges) {
        if (dsu.unite(e.u, e.v)) {
            mst_weight += e.w;
            edges_count++;
            if (edges_count == n - 1) break;
        }
    }

    if (edges_count != n - 1) cout << "IMPOSSIBLE\n";
    else cout << mst_weight << "\n";
    return 0;
}
