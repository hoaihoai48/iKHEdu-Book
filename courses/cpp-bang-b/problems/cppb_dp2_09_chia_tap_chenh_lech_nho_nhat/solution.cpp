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

    int half = total_sum / 2;
    vector<bool> dp(half + 1, false);
    dp[0] = true;

    for (int x : a) {
        for (int j = half; j >= x; --j) {
            if (dp[j - x]) dp[j] = true;
        }
    }

    int best_s1 = 0;
    for (int j = half; j >= 0; --j) {
        if (dp[j]) {
            best_s1 = j;
            break;
        }
    }

    int min_diff = total_sum - 2 * best_s1;
    cout << min_diff << "\n";
    return 0;
}
