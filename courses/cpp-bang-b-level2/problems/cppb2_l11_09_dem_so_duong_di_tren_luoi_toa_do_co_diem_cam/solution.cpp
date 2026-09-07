#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int R, C, K;
    if (!(cin >> R >> C >> K)) return 0;
    vector<char> ban((size_t)R * C, 0);
    for (int i = 0; i < K; i++) {
        int x, y;
        cin >> x >> y;
        --x; --y;
        if (x >= 0 && x < R && y >= 0 && y < C) ban[(size_t)x * C + y] = 1;
    }
    vector<long long> dp(C, 0);
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (ban[(size_t)i * C + j]) { dp[j] = 0; continue; }
            if (i == 0 && j == 0) { dp[j] = 1; continue; }
            long long up = (i > 0) ? dp[j] : 0;
            long long lf = (j > 0) ? dp[j - 1] : 0;
            dp[j] = (up + lf) % MOD;
        }
    }
    cout << dp[C - 1] % MOD << "\n";
    return 0;
}
