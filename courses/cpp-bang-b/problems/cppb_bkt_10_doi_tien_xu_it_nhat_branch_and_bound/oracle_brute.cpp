#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, S;
    if (!(cin >> n >> S)) return 0;
    vector<int> c(n);
    for (int i = 0; i < n; ++i) cin >> c[i];
    vector<int> dp(S + 1, 1e9);
    dp[0] = 0;
    for (int i = 1; i <= S; ++i) {
        for (int coin : c) {
            if (i >= coin) dp[i] = min(dp[i], dp[i - coin] + 1);
        }
    }
    cout << (dp[S] > 1e8 ? -1 : dp[S]) << "\n";
    return 0;
}
