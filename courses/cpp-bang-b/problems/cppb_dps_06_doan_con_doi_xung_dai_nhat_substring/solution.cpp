#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    if (n == 0) return 0;

    vector<vector<bool>> dp(n, vector<bool>(n, false));
    int max_len = 1;
    int start_idx = 0;

    for (int i = 0; i < n; ++i) dp[i][i] = true;

    for (int i = 0; i < n - 1; ++i) {
        if (s[i] == s[i + 1]) {
            dp[i][i + 1] = true;
            if (max_len < 2) {
                max_len = 2;
                start_idx = i;
            }
        }
    }

    for (int len = 3; len <= n; ++len) {
        for (int i = 0; i <= n - len; ++i) {
            int j = i + len - 1;
            if (s[i] == s[j] && dp[i + 1][j - 1]) {
                dp[i][j] = true;
                if (len > max_len) {
                    max_len = len;
                    start_idx = i;
                }
            }
        }
    }

    cout << max_len << "\n";
    cout << s.substr(start_idx, max_len) << "\n";
    return 0;
}
