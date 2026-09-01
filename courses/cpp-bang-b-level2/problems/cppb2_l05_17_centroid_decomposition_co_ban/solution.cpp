#include <bits/stdc++.h>
using namespace std;

// Tìm trọng tâm cây (Centroid) để chia để trị trên cây O(N log N)
const int MAXN = 100005;
vector<int> adj[MAXN];
int sz[MAXN];
bool removed[MAXN];

void get_sz(int u, int p) {
    sz[u] = 1;
    for (int v : adj[u]) {
        if (v != p && !removed[v]) {
            get_sz(v, u);
            sz[u] += sz[v];
        }
    }
}

int get_centroid(int u, int p, int total_size) {
    for (int v : adj[u]) {
        if (v != p && !removed[v] && sz[v] > total_size / 2) {
            return get_centroid(v, u, total_size);
        }
    }
    return u;
}

int decompose(int u) {
    get_sz(u, 0);
    int c = get_centroid(u, 0, sz[u]);
    removed[c] = true;
    for (int v : adj[c]) {
        if (!removed[v]) decompose(v);
    }
    return c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int root_centroid = decompose(1);
    cout << root_centroid << "\n";
    return 0;
}
