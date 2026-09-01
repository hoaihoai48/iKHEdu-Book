#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    deque<int> dq;
    vector<long long> dp(n, 0);

    dp[0] = a[0];
    dq.push_back(0);

    for (int i = 1; i < n; ++i) {
        if (!dq.empty() && dq.front() < i - k) dq.pop_front();
        dp[i] = dp[dq.front()] + a[i];
        while (!dq.empty() && dp[dq.back()] <= dp[i]) dq.pop_back();
        dq.push_back(i);
    }

    cout << dp[n - 1] << "\n";
    return 0;
}
