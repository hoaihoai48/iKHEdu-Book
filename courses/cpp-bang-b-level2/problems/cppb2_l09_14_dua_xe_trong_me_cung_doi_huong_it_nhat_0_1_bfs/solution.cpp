#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<string> g(n);
    for (int i = 0; i < n; ++i) cin >> g[i];
    int sr = -1, sc = -1, tr = -1, tc = -1;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) {
            if (g[i][j] == 'S') { sr = i; sc = j; }
            if (g[i][j] == 'T') { tr = i; tc = j; }
        }
    if (sr == tr && sc == tc) {
        cout << 0 << "\n";
        return 0;
    }
    const int INF = (int)1e9;
    const int dr[4] = {-1, 1, 0, 0};
    const int dc[4] = {0, 0, -1, 1};
    vector<vector<array<int, 4>>> dist(n, vector<array<int, 4>>(m, {INF, INF, INF, INF}));
    deque<array<int, 3>> dq;
    for (int d = 0; d < 4; ++d) {
        dist[sr][sc][d] = 0;
        dq.push_front({sr, sc, d});
    }
    while (!dq.empty()) {
        auto [r, c, d] = dq.front();
        dq.pop_front();
        for (int nd = 0; nd < 4; ++nd) {
            int nr = r + dr[nd], nc = c + dc[nd];
            if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
            if (g[nr][nc] == '#') continue;
            int w = (nd == d ? 0 : 1);
            if (dist[nr][nc][nd] > dist[r][c][d] + w) {
                dist[nr][nc][nd] = dist[r][c][d] + w;
                if (w == 0) dq.push_front({nr, nc, nd});
                else dq.push_back({nr, nc, nd});
            }
        }
    }
    int ans = INF;
    for (int d = 0; d < 4; ++d) ans = min(ans, dist[tr][tc][d]);
    if (ans == INF) cout << -1 << "\n";
    else cout << ans << "\n";
    return 0;
}
