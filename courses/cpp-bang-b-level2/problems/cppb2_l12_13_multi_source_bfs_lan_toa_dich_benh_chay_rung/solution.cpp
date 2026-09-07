#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int R, C;
    if (!(cin >> R >> C)) return 0;
    vector<string> g(R);
    for (int i = 0; i < R; i++) cin >> g[i];
    vector<vector<int>> d(R, vector<int>(C, -1));
    queue<pair<int,int>> q;
    for (int i = 0; i < R; i++) for (int j = 0; j < C; j++)
        if (g[i][j] == 'F') { d[i][j] = 0; q.push({i, j}); }
    const int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};
    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        for (int t = 0; t < 4; t++) {
            int nx = x + dx[t], ny = y + dy[t];
            if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
            if (g[nx][ny] == '#'|| d[nx][ny] != -1) continue;
            d[nx][ny] = d[x][y] + 1; q.push({nx, ny});
        }
    }
    int ans = 0;
    for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) {
        if (g[i][j] == '#') continue;
        if (d[i][j] == -1) { cout << -1 << "\n"; return 0; }
        ans = max(ans, d[i][j]);
    }
    cout << ans << "\n";
    return 0;
}
