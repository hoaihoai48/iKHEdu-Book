#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<vector<long long>> S(n + 1, vector<long long>(k + 1, 0));
    S[0][0] = 1;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= min(i, k); ++j) {
            S[i][j] = (S[i - 1][j - 1] + j * S[i - 1][j]) % MOD;
        }
    }

    cout << S[n][k] << "\n";
    return 0;
}
