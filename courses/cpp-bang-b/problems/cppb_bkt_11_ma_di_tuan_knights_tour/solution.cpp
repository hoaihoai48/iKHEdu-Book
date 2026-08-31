#include <bits/stdc++.h>
using namespace std;

int n;
int board[10][10];
int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};
bool found = false;

int countDegree(int x, int y) {
    int deg = 0;
    for (int i = 0; i < 8; ++i) {
        int nx = x + dx[i], ny = y + dy[i];
        if (nx >= 1 && nx <= n && ny >= 1 && ny <= n && board[nx][ny] == 0) deg++;
    }
    return deg;
}

void solveKnight(int x, int y, int step) {
    if (step == n * n) {
        found = true;
        return;
    }

    vector<pair<int, int>> next_moves;
    for (int i = 0; i < 8; ++i) {
        int nx = x + dx[i], ny = y + dy[i];
        if (nx >= 1 && nx <= n && ny >= 1 && ny <= n && board[nx][ny] == 0) {
            next_moves.push_back({countDegree(nx, ny), i});
        }
    }
    sort(next_moves.begin(), next_moves.end());

    for (auto &p : next_moves) {
        int idx = p.second;
        int nx = x + dx[idx], ny = y + dy[idx];
        board[nx][ny] = step + 1;
        solveKnight(nx, ny, step + 1);
        if (found) return;
        board[nx][ny] = 0;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int r, c;
    if (!(cin >> n >> r >> c)) return 0;
    memset(board, 0, sizeof(board));
    board[r][c] = 1;
    solveKnight(r, c, 1);
    if (!found) {
        cout << -1 << "\n";
    } else {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                cout << board[i][j] << (j == n ? "" : " ");
            }
            cout << "\n";
        }
    }
    return 0;
}
