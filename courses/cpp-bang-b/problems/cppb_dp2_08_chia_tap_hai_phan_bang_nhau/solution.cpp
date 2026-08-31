#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<int> a(n);
    int total_sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total_sum += a[i];
    }

    if (total_sum % 2 != 0) {
        cout << "NO\n";
        return 0;
    }

    int target = total_sum / 2;
    vector<bool> dp(target + 1, false);
    dp[0] = true;

    for (int x : a) {
        for (int j = target; j >= x; --j) {
            if (dp[j - x]) dp[j] = true;
        }
    }

    if (dp[target]) cout << "YES\n";
    else cout << "NO\n";
    return 0;
}
