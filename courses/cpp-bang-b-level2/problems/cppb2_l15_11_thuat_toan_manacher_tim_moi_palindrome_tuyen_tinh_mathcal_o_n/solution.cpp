#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    int n = (int)s.size();
    vector<int> d1(n), d2(n);
    int l = 0, r = -1, best = 1;
    for (int i = 0; i < n; i++) {
        int k = (i > r) ? 1 : min(d1[l + r - i], r - i + 1);
        while (i - k >= 0 && i + k < n && s[i - k] == s[i + k]) k++;
        d1[i] = k;
        best = max(best, k * 2 - 1);
        if (i + k - 1 > r) { l = i - k + 1; r = i + k - 1; }
    }
    l = 0; r = -1;
    for (int i = 0; i < n; i++) {
        int k = (i > r) ? 0 : min(d2[l + r - i + 1], r - i + 1);
        while (i - k - 1 >= 0 && i + k < n && s[i - k - 1] == s[i + k]) k++;
        d2[i] = k;
        best = max(best, k * 2);
        if (i + k - 1 > r) { l = i - k; r = i + k - 1; }
    }
    cout << best << "\n";
    return 0;
}
