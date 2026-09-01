#include <bits/stdc++.h>
using namespace std;

// Palindrome Partitioning Min Cut DP O(N^2)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    vector<vector<bool>> is_pal(n, vector<bool>(n, false));

    for (int i = n - 1; i >= 0; --i) {
        for (int j = i; j < n; ++j) {
            if (s[i] == s[j] && (j - i <= 2 || is_pal[i + 1][j - 1])) {
                is_pal[i][j] = true;
            }
        }
    }

    vector<int> dp(n, 0);
    for (int i = 0; i < n; ++i) {
        if (is_pal[0][i]) {
            dp[i] = 0;
        } else {
            dp[i] = i;
            for (int j = 0; j < i; ++j) {
                if (is_pal[j + 1][i]) {
                    dp[i] = min(dp[i], dp[j] + 1);
                }
            }
        }
    }

    cout << dp[n - 1] << "\n";
    return 0;
}
