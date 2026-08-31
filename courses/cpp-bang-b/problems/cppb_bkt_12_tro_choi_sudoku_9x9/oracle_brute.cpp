#include <bits/stdc++.h>
using namespace std;
int b[9][9];
bool r_u[9][10], c_u[9][10], b_u[9][10];
bool solve(int r, int c) {
    if (r == 9) return true;
    if (c == 9) return solve(r + 1, 0);
    if (b[r][c] != 0) return solve(r, c + 1);
    int bx = (r / 3) * 3 + (c / 3);
    for (int v = 1; v <= 9; ++v) {
        if (!r_u[r][v] && !c_u[c][v] && !b_u[bx][v]) {
            b[r][c] = v;
            r_u[r][v] = c_u[c][v] = b_u[bx][v] = true;
            if (solve(r, c + 1)) return true;
            r_u[r][v] = c_u[c][v] = b_u[bx][v] = false;
            b[r][c] = 0;
        }
    }
    return false;
}
int main() {
    for (int i = 0; i < 9; ++i)
        for (int j = 0; j < 9; ++j) {
            if (!(cin >> b[i][j])) return 0;
            int v = b[i][j];
            if (v != 0) r_u[i][v] = c_u[j][v] = b_u[(i/3)*3 + j/3][v] = true;
        }
    solve(0, 0);
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) cout << b[i][j] << (j == 8 ? "" : " ");
        cout << "\n";
    }
    return 0;
}
