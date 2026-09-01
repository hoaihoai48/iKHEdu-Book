#include <bits/stdio.h>
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<vector<long long>> E(n + 1, vector<long long>(k + 1, 0));
    E[1][0] = 1;

    for (int i = 2; i <= n; ++i) {
        for (int j = 0; j <= k; ++j) {
            E[i][j] = ((j + 1) * E[i - 1][j] + (j > 0 ? (i - j) * E[i - 1][j - 1] : 0)) % MOD;
        }
    }

    cout << E[n][k] << "\n";
    return 0;
}
