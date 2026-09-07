#include <bits/stdc++.h>
using namespace std;
vector<int> buildSA(const string &s) {
    int n = (int)s.size();
    vector<int> sa(n), rnk(n), tmp(n);
    for (int i = 0; i < n; i++) { sa[i] = i; rnk[i] = (unsigned char)s[i]; }
    for (int k = 1; k < n; k <<= 1) {
        auto key2 = [&](int i) { return i + k < n ? rnk[i + k] + 1 : 0; };
        int m = max(256, n) + 2;
        vector<int> cnt(m, 0);
        for (int i = 0; i < n; i++) cnt[key2(i)]++;
        for (int i = 1; i < m; i++) cnt[i] += cnt[i - 1];
        vector<int> sa2(n);
        for (int i = n - 1; i >= 0; i--) sa2[--cnt[key2(sa[i])]] = sa[i];
        fill(cnt.begin(), cnt.end(), 0);
        for (int i = 0; i < n; i++) cnt[rnk[i] + 1]++;
        for (int i = 1; i < m; i++) cnt[i] += cnt[i - 1];
        for (int i = n - 1; i >= 0; i--) sa[--cnt[rnk[sa2[i]] + 1]] = sa2[i];
        tmp[sa[0]] = 0;
        int r = 0;
        for (int i = 1; i < n; i++) {
            int a = sa[i - 1], b = sa[i];
            if (rnk[a] != rnk[b] || key2(a) != key2(b)) r++;
            tmp[b] = r;
        }
        rnk = tmp;
        if (r == n - 1) break;
    }
    return sa;
}
vector<int> buildLCP(const string &s, const vector<int> &sa) {
    int n = (int)s.size();
    vector<int> rankv(n), lcp(max(0, n - 1));
    for (int i = 0; i < n; i++) rankv[sa[i]] = i;
    int h = 0;
    for (int i = 0; i < n; i++) {
        if (rankv[i] == 0) continue;
        int j = sa[rankv[i] - 1];
        while (i + h < n && j + h < n && s[i + h] == s[j + h]) h++;
        lcp[rankv[i] - 1] = h;
        if (h) h--;
    }
    return lcp;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    vector<int> sa = buildSA(s);
    for (size_t i = 0; i < sa.size(); i++) { if (i) cout << ' '; cout << sa[i]; }
    cout << "\n";
    return 0;
}
