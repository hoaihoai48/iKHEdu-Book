#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    string s, t;
    cin >> s >> t;

    vector<int> need(26, 0);
    for (char c : t) need[c - 'a'] = 1;

    vector<int> have(26, 0);
    int matched = 0;
    int l = 0, min_len = n + 1;

    for (int r = 0; r < n; ++r) {
        int c = s[r] - 'a';
        if (need[c]) {
            if (have[c] == 0) ++matched;
            ++have[c];
        }

        while (matched == m) {
            min_len = min(min_len, r - l + 1);
            int lc = s[l] - 'a';
            if (need[lc]) {
                --have[lc];
                if (have[lc] == 0) --matched;
            }
            ++l;
        }
    }

    if (min_len > n) cout << -1 << "\n";
    else cout << min_len << "\n";
    return 0;
}
