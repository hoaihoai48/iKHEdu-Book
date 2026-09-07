#include <bits/stdc++.h>
using namespace std;
struct DSU {
    vector<int> p, r;
    DSU(int n = 0) { init(n); }
    void init(int n) { p.resize(n + 1); r.assign(n + 1, 0); for (int i = 1; i <= n; i++) p[i] = i; }
    int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
    bool unite(int a, int b) {
        a = find(a); b = find(b);
        if (a == b) return false;
        if (r[a] < r[b]) swap(a, b);
        p[b] = a;
        if (r[a] == r[b]) r[a]++;
        return true;
    }
};
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    if (!(cin >> N >> M)) return 0;
    vector<tuple<long long,int,int>> e;
    for (int i = 0; i < M; i++) { int u, v; long long w; cin >> u >> v >> w; e.push_back({w, u, v}); }
    sort(e.begin(), e.end());
    DSU dsu(N);
    long long sum = 0;
    int used = 0;
    for (auto &t : e) {
        long long w; int u, v; tie(w, u, v) = t;
        if (dsu.unite(u, v)) { sum += w; used++; }
    }
    if (N == 1) { cout << 0 << "\n"; return 0; }
    if (used != N - 1) cout << "IMPOSSIBLE\n";
    else cout << sum << "\n";
    return 0;
}
