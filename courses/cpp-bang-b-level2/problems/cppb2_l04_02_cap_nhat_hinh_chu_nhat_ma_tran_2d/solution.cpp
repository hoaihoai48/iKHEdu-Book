#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<vector<long long>> diff(n + 2, vector<long long>(m + 2, 0));

    while (q--) {
        int x1, y1, x2, y2;
        long long val;
        cin >> x1 >> y1 >> x2 >> y2 >> val;
        diff[x1][y1] += val;
        diff[x1][y2 + 1] -= val;
        diff[x2 + 1][y1] -= val;
        diff[x2 + 1][y2 + 1] += val;
    }

    vector<vector<long long>> a(n + 1, vector<long long>(m + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            a[i][j] = a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1] + diff[i][j];
            cout << a[i][j] << (j == m ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}
