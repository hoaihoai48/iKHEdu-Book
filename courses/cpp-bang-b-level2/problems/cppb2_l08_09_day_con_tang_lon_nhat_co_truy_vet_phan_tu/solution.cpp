#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> dp(n, 1), parent(n, -1);
    int max_len = 1, best_idx = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (a[j] < a[i] && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                parent[i] = j;
            }
        }
        if (dp[i] > max_len) {
            max_len = dp[i];
            best_idx = i;
        }
    }

    vector<long long> lis;
    int cur = best_idx;
    while (cur != -1) {
        lis.push_back(a[cur]);
        cur = parent[cur];
    }
    reverse(lis.begin(), lis.end());

    cout << max_len << "\n";
    for (size_t i = 0; i < lis.size(); ++i) {
        cout << lis[i] << (i + 1 == lis.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}
