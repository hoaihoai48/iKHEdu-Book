#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    int n = (int)s.size();
    vector<int> d1(n), d2(n);
    int l = 0, r = -1;
    for (int i = 0; i < n; i++) {
        int k = (i > r) ? 1 : min(d1[l + r - i], r - i + 1);
        while (i - k >= 0 && i + k < n && s[i - k] == s[i + k]) k++;
        d1[i] = k;
        if (i + k - 1 > r) { l = i - k + 1; r = i + k - 1; }
    }
    l = 0; r = -1;
    for (int i = 0; i < n; i++) {
        int k = (i > r) ? 0 : min(d2[l + r - i + 1], r - i + 1);
        while (i - k - 1 >= 0 && i + k < n && s[i - k - 1] == s[i + k]) k++;
        d2[i] = k;
        if (i + k - 1 > r) { l = i - k; r = i + k - 1; }
    }
    int bestLen = 1, bestPos = 0;
    for (int i = 0; i < n; i++) {
        int len = d1[i] * 2 - 1, pos = i - d1[i] + 1;
        if (len > bestLen || (len == bestLen && pos < bestPos)) { bestLen = len; bestPos = pos; }
        len = d2[i] * 2; pos = i - d2[i];
        if (len > bestLen || (len == bestLen && len > 0 && pos < bestPos)) { bestLen = len; bestPos = pos; }
    }
    cout << s.substr(bestPos, bestLen) << "\n";
    return 0;
}
