#include <bits/stdc++.h>
using namespace std;

int board[9][9];
bool row_used[9][10], col_used[9][10], box_used[9][10];

bool solveSudoku(int r, int c) {
    if (r == 9) return true;
    if (c == 9) return solveSudoku(r + 1, 0);
    if (board[r][c] != 0) return solveSudoku(r, c + 1);

    int b = (r / 3) * 3 + (c / 3);
    for (int num = 1; num <= 9; ++num) {
        if (!row_used[r][num] && !col_used[c][num] && !box_used[b][num]) {
            board[r][c] = num;
            row_used[r][num] = col_used[c][num] = box_used[b][num] = true;
            if (solveSudoku(r, c + 1)) return true;
            row_used[r][num] = col_used[c][num] = box_used[b][num] = false;
            board[r][c] = 0;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            if (!(cin >> board[i][j])) return 0;
            int num = board[i][j];
            if (num != 0) {
                row_used[i][num] = col_used[j][num] = box_used[(i / 3) * 3 + (j / 3)][num] = true;
            }
        }
    }
    solveSudoku(0, 0);
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            cout << board[i][j] << (j == 8 ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}
