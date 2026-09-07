#include <bits/stdc++.h>
using namespace std;
const long long M1 = 1000000007, M2 = 1000000009;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int K;
    if (!(cin >> K)) return 0;
    string dummy;
    getline(cin, dummy);
    vector<string> s(K);
    for (int i = 0; i < K; i++) getline(cin, s[i]);
    int bi = 0;
    for (int i = 1; i < K; i++) if (s[i].size() < s[bi].size()) bi = i;
    int n0 = (int)s[bi].size();
    if (n0 == 0) { cout << 0 << "\n"; return 0; }
    const long long BB = 9113823LL;
    int mx = 0;
    for (auto &t : s) mx = max(mx, (int)t.size());
    vector<long long> p1(mx + 1, 1), p2(mx + 1, 1);
    for (int i = 1; i <= mx; i++) { p1[i] = p1[i - 1] * (BB % M1) % M1; p2[i] = p2[i - 1] * (BB % M2) % M2; }
    vector<vector<long long>> h1(K), h2(K);
    for (int k = 0; k < K; k++) {
        int n = (int)s[k].size();
        h1[k].assign(n + 1, 0); h2[k].assign(n + 1, 0);
        for (int i = 0; i < n; i++) {
            h1[k][i + 1] = (h1[k][i] * (BB % M1) + (unsigned char)s[k][i] + 1) % M1;
            h2[k][i + 1] = (h2[k][i] * (BB % M2) + (unsigned char)s[k][i] + 1) % M2;
        }
    }
    auto get = [&](const vector<long long> &h, const vector<long long> &p, int l, int len, long long M) {
        long long v = (h[l + len] - h[l] * p[len]) % M;
        if (v < 0) v += M;
        return v;
    };
    auto ok = [&](int L) {
        if (L == 0) return true;
        unordered_set<unsigned long long> cur;
        cur.reserve(n0 - L + 1);
        for (int i = 0; i + L <= n0; i++) {
            unsigned long long key = (unsigned long long)get(h1[bi], p1, i, L, M1) << 32
                | (unsigned long long)get(h2[bi], p2, i, L, M2);
            cur.insert(key);
        }
        if (cur.empty()) return false;
        for (int k = 0; k < K; k++) {
            if (k == bi) continue;
            int n = (int)s[k].size();
            unordered_set<unsigned long long> nxt;
            nxt.reserve(n - L + 1 > 0 ? (size_t)(n - L + 1) : 0);
            for (int i = 0; i + L <= n; i++) {
                unsigned long long key = (unsigned long long)get(h1[k], p1, i, L, M1) << 32
                    | (unsigned long long)get(h2[k], p2, i, L, M2);
                if (cur.find(key) != cur.end()) nxt.insert(key);
            }
            cur.swap(nxt);
            if (cur.empty()) return false;
        }
        return !cur.empty();
    };
    int lo = 0, hi = n0;
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (ok(mid)) lo = mid; else hi = mid - 1;
    }
    cout << lo << "\n";
    return 0;
}
