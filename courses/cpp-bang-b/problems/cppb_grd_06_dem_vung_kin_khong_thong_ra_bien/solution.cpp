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
    for (int i = 0; i < n; ++i) cin >> grid[i];

    queue<pair<int, int>> q;

    for (int r = 0; r < n; ++r) {
        if (grid[r][0] == '0') { grid[r][0] = '1'; q.push({r, 0}); }
        if (grid[r][m - 1] == '0') { grid[r][m - 1] = '1'; q.push({r, m - 1}); }
    }
    for (int c = 0; c < m; ++c) {
        if (grid[0][c] == '0') { grid[0][c] = '1'; q.push({0, c}); }
        if (grid[n - 1][c] == '0') { grid[n - 1][c] = '1'; q.push({n - 1, c}); }
    }

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == '0') {
                grid[nr][nc] = '1';
                q.push({nr, nc});
            }
        }
    }

    int closed_zeros = 0;
    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == '0') closed_zeros++;
        }
    }

    cout << closed_zeros << "\n";
    return 0;
}
