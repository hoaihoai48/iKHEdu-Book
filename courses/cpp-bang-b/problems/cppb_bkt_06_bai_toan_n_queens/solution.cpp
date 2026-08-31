#include <bits/stdc++.h>
using namespace std;

int n;
long long ans = 0;
vector<bool> col_used, diag1, diag2;

void backtrack(int row) {
    if (row > n) {
        ans++;
        return;
    }
    for (int col = 1; col <= n; ++col) {
        if (!col_used[col] && !diag1[row - col + n] && !diag2[row + col]) {
            col_used[col] = diag1[row - col + n] = diag2[row + col] = true;
            backtrack(row + 1);
            col_used[col] = diag1[row - col + n] = diag2[row + col] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    col_used.assign(n + 1, false);
    diag1.assign(2 * n + 1, false);
    diag2.assign(2 * n + 1, false);
    backtrack(1);
    cout << ans << "\n";
    return 0;
}
