#include <bits/stdc++.h>
using namespace std;
int n, b[10][10];
int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};
bool found = false;
int deg(int x, int y) {
    int cnt = 0;
    for (int i = 0; i < 8; ++i) {
        int nx = x + dx[i], ny = y + dy[i];
        if (nx >= 1 && nx <= n && ny >= 1 && ny <= n && b[nx][ny] == 0) cnt++;
    }
    return cnt;
}
void bkt(int x, int y, int step) {
    if (step == n * n) { found = true; return; }
    vector<pair<int, int>> nexts;
    for (int i = 0; i < 8; ++i) {
        int nx = x + dx[i], ny = y + dy[i];
        if (nx >= 1 && nx <= n && ny >= 1 && ny <= n && b[nx][ny] == 0) nexts.push_back({deg(nx, ny), i});
    }
    sort(nexts.begin(), nexts.end());
    for (auto &p : nexts) {
        int idx = p.second;
        int nx = x + dx[idx], ny = y + dy[idx];
        b[nx][ny] = step + 1;
        bkt(nx, ny, step + 1);
        if (found) return;
        b[nx][ny] = 0;
    }
}
int main() {
    int r, c;
    if (!(cin >> n >> r >> c)) return 0;
    b[r][c] = 1;
    bkt(r, c, 1);
    if (!found) cout << -1 << "\n";
    else {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) cout << b[i][j] << (j == n ? "" : " ");
            cout << "\n";
        }
    }
    return 0;
}
