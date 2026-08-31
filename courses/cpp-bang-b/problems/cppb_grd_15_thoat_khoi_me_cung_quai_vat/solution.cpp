#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> grid(n);
    queue<pair<int, int>> mq;
    vector<vector<int>> monster_dist(n, vector<int>(m, INF));
    int ar = -1, ac = -1;

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == 'M') {
                monster_dist[r][c] = 0;
                mq.push({r, c});
            } else if (grid[r][c] == 'A') {
                ar = r; ac = c;
            }
        }
    }

    while (!mq.empty()) {
        auto [r, c] = mq.front();
        mq.pop();

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#' && monster_dist[nr][nc] == INF) {
                monster_dist[nr][nc] = monster_dist[r][c] + 1;
                mq.push({nr, nc});
            }
        }
    }

    vector<vector<int>> player_dist(n, vector<int>(m, -1));
    queue<pair<int, int>> pq;

    player_dist[ar][ac] = 0;
    pq.push({ar, ac});

    while (!pq.empty()) {
        auto [r, c] = pq.front();
        pq.pop();

        if (r == 0 || r == n - 1 || c == 0 || c == m - 1) {
            cout << "YES\n";
            return 0;
        }

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#' && player_dist[nr][nc] == -1) {
                if (player_dist[r][c] + 1 < monster_dist[nr][nc]) {
                    player_dist[nr][nc] = player_dist[r][c] + 1;
                    pq.push({nr, nc});
                }
            }
        }
    }

    cout << "NO\n";
    return 0;
}
