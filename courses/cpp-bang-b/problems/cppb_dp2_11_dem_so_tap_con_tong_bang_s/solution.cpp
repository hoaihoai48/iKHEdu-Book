#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    if (!(cin >> n >> s)) return 0;
    if (n <= 0 || s < 0) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> dp(s + 1, 0);
    dp[0] = 1;

    for (int x : a) {
        for (int j = s; j >= x; --j) {
            dp[j] = (dp[j] + dp[j - x]) % MOD;
        }
    }

    cout << dp[s] << "\n";
    return 0;
}
