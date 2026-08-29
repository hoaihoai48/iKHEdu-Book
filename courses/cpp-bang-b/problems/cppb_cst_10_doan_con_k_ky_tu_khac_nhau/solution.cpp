#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    string s;
    cin >> s;

    vector<int> freq(26, 0);
    int distinct = 0;
    int l = 0, max_len = 0;

    for (int r = 0; r < n; ++r) {
        int c = s[r] - 'a';
        if (freq[c] == 0) ++distinct;
        ++freq[c];

        while (distinct > k) {
            int lc = s[l] - 'a';
            --freq[lc];
            if (freq[lc] == 0) --distinct;
            ++l;
        }

        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\n";
    return 0;
}
