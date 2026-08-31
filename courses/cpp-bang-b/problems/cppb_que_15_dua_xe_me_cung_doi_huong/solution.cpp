#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

struct State {
    int r, c, dir;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0 || m <= 0) return 0;

    vector<string> grid(n);
    int sr = -1, sc = -1, er = -1, ec = -1;

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == 'S') { sr = r; sc = c; }
            if (grid[r][c] == 'E') { er = r; ec = c; }
        }
    }

    vector<vector<vector<int>>> dist(n, vector<vector<int>>(m, vector<int>(4, INF)));
    deque<State> dq;

    for (int d = 0; d < 4; ++d) {
        dist[sr][sc][d] = 0;
        dq.push_back({sr, sc, d});
    }

    while (!dq.empty()) {
        auto [r, c, dir] = dq.front();
        dq.pop_front();

        for (int nd = 0; nd < 4; ++nd) {
            int nr = r + dr[nd];
            int nc = c + dc[nd];
            int cost = (nd == dir ? 0 : 1);

            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#') {
                if (dist[r][c][dir] + cost < dist[nr][nc][nd]) {
                    dist[nr][nc][nd] = dist[r][c][dir] + cost;
                    if (cost == 0) {
                        dq.push_front({nr, nc, nd});
                    } else {
                        dq.push_back({nr, nc, nd});
                    }
                }
            }
        }
    }

    int ans = INF;
    for (int d = 0; d < 4; ++d) ans = min(ans, dist[er][ec][d]);

    if (ans == INF) cout << -1 << "\n";
    else cout << ans << "\n";
    return 0;
}
