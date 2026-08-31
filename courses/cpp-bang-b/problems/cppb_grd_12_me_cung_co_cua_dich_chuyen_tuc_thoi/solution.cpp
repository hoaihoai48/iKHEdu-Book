#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> grid(n);
    vector<vector<pair<int, int>>> teleports(26);

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            if (isupper(grid[r][c])) {
                teleports[grid[r][c] - 'A'].push_back({r, c});
            }
        }
    }

    vector<vector<int>> dist(n, vector<int>(m, -1));
    vector<bool> teleport_used(26, false);
    queue<pair<int, int>> q;

    dist[0][0] = 0;
    q.push({0, 0});

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (r == n - 1 && c == m - 1) {
            cout << dist[r][c] << "\n";
            return 0;
        }

        // Dịch chuyển tức thời
        if (isupper(grid[r][c])) {
            int ch = grid[r][c] - 'A';
            if (!teleport_used[ch]) {
                teleport_used[ch] = true;
                for (auto [tr, tc] : teleports[ch]) {
                    if (dist[tr][tc] == -1) {
                        dist[tr][tc] = dist[r][c];
                        q.push({tr, tc});
                    }
                }
            }
        }

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#' && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                q.push({nr, nc});
            }
        }
    }

    cout << dist[n - 1][m - 1] << "\n";
    return 0;
}
