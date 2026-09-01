#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int to;
    long long cap, flow;
    int rev;
};

const int MAXN = 505;
vector<Edge> adj[MAXN];
int level[MAXN], ptr[MAXN];

void add_edge(int from, int to, long long cap) {
    adj[from].push_back({to, cap, 0, (int)adj[to].size()});
    adj[to].push_back({from, 0, 0, (int)adj[from].size() - 1});
}

bool bfs_dinic(int s, int t) {
    memset(level, -1, sizeof(level));
    level[s] = 0;
    queue<int> q; q.push(s);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (const auto &e : adj[u]) {
            if (e.cap - e.flow > 0 && level[e.to] == -1) {
                level[e.to] = level[u] + 1;
                q.push(e.to);
            }
        }
    }
    return level[t] != -1;
}

long long dfs_dinic(int u, int t, long long pushed) {
    if (pushed == 0 || u == t) return pushed;
    for (int &cid = ptr[u]; cid < (int)adj[u].size(); ++cid) {
        auto &e = adj[u][cid];
        int tr = e.to;
        if (level[u] + 1 != level[tr] || e.cap - e.flow == 0) continue;
        long long tr_pushed = dfs_dinic(tr, t, min(pushed, e.cap - e.flow));
        if (tr_pushed == 0) continue;
        e.flow += tr_pushed;
        adj[tr][e.rev].flow -= tr_pushed;
        return tr_pushed;
    }
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;

    for (int i = 0; i < m; ++i) {
        int u, v; long long c; cin >> u >> v >> c;
        add_edge(u, v, c);
    }

    long long flow = 0;
    while (bfs_dinic(s, t)) {
        memset(ptr, 0, sizeof(ptr));
        while (long long pushed = dfs_dinic(s, t, 1e18)) flow += pushed;
    }

    cout << flow << "\n";
    return 0;
}
