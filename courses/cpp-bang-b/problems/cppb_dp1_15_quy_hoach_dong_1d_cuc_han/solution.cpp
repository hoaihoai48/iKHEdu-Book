#include <bits/stdc++.h>
using namespace std;

struct Item {
    long long v, c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<Item> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].v >> a[i].c;
    }

    // Sắp xếp theo v tăng dần
    sort(a.begin(), a.end(), [](const Item& x, const Item& y) {
        if (x.v != y.v) return x.v < y.v;
        return x.c > y.c;
    });

    vector<long long> dp(n);
    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        dp[i] = a[i].c;
        for (int j = 0; j < i; ++j) {
            if (a[j].v < a[i].v) {
                dp[i] = max(dp[i], dp[j] + a[i].c);
            }
        }
        ans = max(ans, dp[i]);
    }

    cout << ans << "\n";
    return 0;
}
