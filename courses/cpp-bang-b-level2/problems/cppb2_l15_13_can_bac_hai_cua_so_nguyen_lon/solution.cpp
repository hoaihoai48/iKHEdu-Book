#include <bits/stdc++.h>
using namespace std;

vector<int> build_sa(string s) {
    s += "$";
    int n = s.size();
    vector<int> p(n), c(n);
    vector<pair<char, int>> a(n);
    for (int i = 0; i < n; ++i) a[i] = {s[i], i};
    sort(a.begin(), a.end());
    for (int i = 0; i < n; ++i) p[i] = a[i].second;
    c[p[0]] = 0;
    for (int i = 1; i < n; ++i) {
        c[p[i]] = c[p[i - 1]] + (a[i].first != a[i - 1].first);
    }

    int k = 0;
    while ((1 << k) < n) {
        vector<pair<pair<int, int>, int>> b(n);
        for (int i = 0; i < n; ++i) {
            b[i] = {{c[i], c[(i + (1 << k)) % n]}, i};
        }
        sort(b.begin(), b.end());
        for (int i = 0; i < n; ++i) p[i] = b[i].second;
        c[p[0]] = 0;
        for (int i = 1; i < n; ++i) {
            c[p[i]] = c[p[i - 1]] + (b[i].first != b[i - 1].first);
        }
        k++;
    }
    return vector<int>(p.begin() + 1, p.end());
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    vector<int> sa = build_sa(s);
    for (int idx : sa) cout << idx << " ";
    cout << "\n";
    return 0;
}
