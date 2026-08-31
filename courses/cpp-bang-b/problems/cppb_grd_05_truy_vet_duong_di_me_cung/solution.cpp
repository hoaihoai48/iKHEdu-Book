#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};
const char dir_char[] = {'U', 'D', 'L', 'R'};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> grid(n);
    int sr = -1, sc = -1, er = -1, ec = -1;

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == 'A' || grid[r][c] == 'S') { sr = r; sc = c; }
            if (grid[r][c] == 'B' || grid[r][c] == 'E') { er = r; ec = c; }
        }
    }

    vector<vector<int>> dist(n, vector<int>(m, -1));
    vector<vector<int>> prev_dir(n, vector<int>(m, -1));
    queue<pair<int, int>> q;

    dist[sr][sc] = 0;
    q.push({sr, sc});

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (r == er && c == ec) break;

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#' && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                prev_dir[nr][nc] = d;
                q.push({nr, nc});
            }
        }
    }

    if (dist[er][ec] == -1) {
        cout << "NO\n";
        return 0;
    }

    cout << "YES\n" << dist[er][ec] << "\n";
    string path = "";
    int curr_r = er, curr_c = ec;

    while (curr_r != sr || curr_c != sc) {
        int d = prev_dir[curr_r][curr_c];
        path += dir_char[d];
        curr_r -= dr[d];
        curr_c -= dc[d];
    }
    reverse(path.begin(), path.end());
    cout << path << "\n";
    return 0;
}
