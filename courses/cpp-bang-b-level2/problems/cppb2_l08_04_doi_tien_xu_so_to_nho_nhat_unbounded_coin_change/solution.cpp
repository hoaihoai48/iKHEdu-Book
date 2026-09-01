#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long S;
    if (!(cin >> n >> S)) return 0;

    vector<long long> coins(n);
    for (int i = 0; i < n; ++i) cin >> coins[i];

    vector<long long> dp(S + 1, 1e9);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        for (long long j = coins[i]; j <= S; ++j) {
            dp[j] = min(dp[j], dp[j - coins[i]] + 1);
        }
    }

    cout << (dp[S] >= 1e9 ? -1 : dp[S]) << "\n";
    return 0;
}
