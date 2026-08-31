#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size(), m = t.size();
    vector<int> prev_row(m + 1), curr_row(m + 1);

    for (int j = 0; j <= m; ++j) prev_row[j] = j;

    for (int i = 1; i <= n; ++i) {
        curr_row[0] = i;
        for (int j = 1; j <= m; ++j) {
            if (s[i - 1] == t[j - 1]) {
                curr_row[j] = prev_row[j - 1];
            } else {
                curr_row[j] = 1 + min({prev_row[j], curr_row[j - 1], prev_row[j - 1]});
            }
        }
        prev_row = curr_row;
    }

    cout << prev_row[m] << "\n";
    return 0;
}
