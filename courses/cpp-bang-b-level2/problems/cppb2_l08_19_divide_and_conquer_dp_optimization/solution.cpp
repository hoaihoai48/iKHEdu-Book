#include <bits/stdc++.h>
using namespace std;

// Chia để trị tối ưu hóa DP: dp[g][i] = min_{j < i}(dp[g-1][j] + cost(j+1, i))
const long long INF = 1e18;
long long dp_cur[5005], dp_next[5005];
long long pref[5005];

long long cost(int j, int i) {
    long long len = i - j + 1;
    return (pref[i] - pref[j - 1]) * len;
}

void compute(int l, int r, int opt_l, int opt_r) {
    if (l > r) return;
    int mid = (l + r) / 2;
    int opt = -1;
    dp_next[mid] = INF;

    for (int j = opt_l; j <= min(mid, opt_r); ++j) {
        long long cur = dp_cur[j] + cost(j + 1, mid);
        if (cur < dp_next[mid]) {
            dp_next[mid] = cur;
            opt = j;
        }
    }

    compute(l, mid - 1, opt_l, opt);
    compute(mid + 1, r, opt, opt_r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    for (int i = 1; i <= n; ++i) {
        long long x; cin >> x;
        pref[i] = pref[i - 1] + x;
    }

    for (int i = 1; i <= n; ++i) dp_cur[i] = cost(1, i);

    for (int g = 2; g <= k; ++g) {
        compute(1, n, 1, n);
        for (int i = 1; i <= n; ++i) dp_cur[i] = dp_next[i];
    }

    cout << dp_cur[n] << "\n";
    return 0;
}
