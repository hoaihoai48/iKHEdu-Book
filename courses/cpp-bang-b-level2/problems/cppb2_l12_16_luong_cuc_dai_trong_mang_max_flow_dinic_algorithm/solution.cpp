#include <bits/stdc++.h>
using namespace std;
struct Dinic {
    struct Edge { int to, rev; long long cap; };
    int n;
    vector<vector<Edge>> g;
    vector<int> level, it;
    Dinic(int n = 0) { init(n); }
    void init(int n_) { n = n_; g.assign(n + 1, {}); }
    void addEdge(int u, int v, long long c) {
        Edge a{v, (int)g[v].size(), c}, b{u, (int)g[u].size(), 0};
        g[u].push_back(a); g[v].push_back(b);
    }
    bool bfs(int s, int t) {
        level.assign(n + 1, -1);
        queue<int> q; q.push(s); level[s] = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (auto &e : g[u]) if (e.cap > 0 && level[e.to] < 0) {
                level[e.to] = level[u] + 1; q.push(e.to);
            }
        }
        return level[t] >= 0;
    }
    long long dfs(int u, int t, long long f) {
        if (u == t) return f;
        for (int &i = it[u]; i < (int)g[u].size(); i++) {
            Edge &e = g[u][i];
            if (e.cap > 0 && level[e.to] == level[u] + 1) {
                long long r = dfs(e.to, t, min(f, e.cap));
                if (r > 0) { e.cap -= r; g[e.to][e.rev].cap += r; return r; }
            }
        }
        return 0;
    }
    long long maxflow(int s, int t) {
        long long flow = 0, f;
        while (bfs(s, t)) {
            it.assign(n + 1, 0);
            while ((f = dfs(s, t, (long long)4e18)) > 0) flow += f;
        }
        return flow;
    }
};
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M, S, T;
    if (!(cin >> N >> M >> S >> T)) return 0;
    Dinic dinic(N);
    for (int i = 0; i < M; i++) {
        int u, v; long long c; cin >> u >> v >> c;
        dinic.addEdge(u, v, c);
    }
    cout << dinic.maxflow(S, T) << "\n";
    return 0;
}
