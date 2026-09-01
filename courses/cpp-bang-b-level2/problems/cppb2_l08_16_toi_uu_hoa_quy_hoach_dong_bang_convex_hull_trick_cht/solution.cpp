#include <bits/stdc++.h>
using namespace std;

struct Line {
    long long m, c;
    long long eval(long long x) const {
        return m * x + c;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    vector<long long> dp(n, 0);
    for (int i = 1; i < n; ++i) {
        dp[i] = 1e18;
        for (int j = 0; j < i; ++j) {
            dp[i] = min(dp[i], dp[j] + (h[i] - h[j]) * (h[i] - h[j]));
        }
    }

    cout << dp[n - 1] << "\n";
    return 0;
}
