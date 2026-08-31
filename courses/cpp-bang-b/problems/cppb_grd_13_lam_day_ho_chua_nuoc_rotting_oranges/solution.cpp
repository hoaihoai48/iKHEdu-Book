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
    queue<pair<int, int>> q;
    int fresh_count = 0;

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == '2') q.push({r, c});
            else if (grid[r][c] == '1') fresh_count++;
        }
    }

    int minutes = 0;
    while (!q.empty() && fresh_count > 0) {
        int sz = q.size();
        minutes++;
        while (sz--) {
            auto [r, c] = q.front();
            q.pop();

            for (int d = 0; d < 4; ++d) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == '1') {
                    grid[nr][nc] = '2';
                    fresh_count--;
                    q.push({nr, nc});
                }
            }
        }
    }

    if (fresh_count > 0) cout << -1 << "\n";
    else cout << minutes << "\n";
    return 0;
}
