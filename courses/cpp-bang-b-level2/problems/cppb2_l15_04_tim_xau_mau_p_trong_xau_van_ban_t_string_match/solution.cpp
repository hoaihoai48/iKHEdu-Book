#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string T, P;
    if (!(cin >> T)) return 0;
    cin >> P;
    int n = (int)T.size(), m = (int)P.size();
    vector<int> pi(m, 0);
    for (int i = 1; i < m; i++) {
        int j = pi[i - 1];
        while (j > 0 && P[i] != P[j]) j = pi[j - 1];
        if (P[i] == P[j]) j++;
        pi[i] = j;
    }
    vector<int> ans;
    int j = 0;
    for (int i = 0; i < n; i++) {
        while (j > 0 && T[i] != P[j]) j = pi[j - 1];
        if (T[i] == P[j]) j++;
        if (j == m) { ans.push_back(i - m + 2); j = pi[j - 1]; }
    }
    if (ans.empty()) cout << -1 << "\n";
    else { for (size_t i = 0; i < ans.size(); i++) { if (i) cout << ' '; cout << ans[i]; } cout << "\n"; }
    return 0;
}
