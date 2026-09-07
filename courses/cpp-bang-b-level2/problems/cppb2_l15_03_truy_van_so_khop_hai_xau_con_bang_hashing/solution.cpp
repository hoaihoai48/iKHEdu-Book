#include <bits/stdc++.h>
using namespace std;
const long long M1 = 1000000007, M2 = 1000000009, B = 9113823LL % 1000000007;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string S;
    if (!(cin >> S)) return 0;
    int n = (int)S.size(), Q;
    cin >> Q;
    const long long BB = 9113823LL;
    vector<long long> p1(n + 1, 1), p2(n + 1, 1), h1(n + 1, 0), h2(n + 1, 0);
    for (int i = 0; i < n; i++) {
        p1[i + 1] = p1[i] * (BB % M1) % M1;
        p2[i + 1] = p2[i] * (BB % M2) % M2;
        h1[i + 1] = (h1[i] * (BB % M1) + (S[i] - 'a' + 1)) % M1;
        h2[i + 1] = (h2[i] * (BB % M2) + (S[i] - 'a' + 1)) % M2;
    }
    auto get = [&](const vector<long long> &h, const vector<long long> &p, int l, int r, long long M) {
        long long v = (h[r] - h[l - 1] * p[r - l + 1]) % M;
        if (v < 0) v += M;
        return v;
    };
    while (Q--) {
        int l1, r1, l2, r2; cin >> l1 >> r1 >> l2 >> r2;
        bool ok = (r1 - l1 == r2 - l2)
            && get(h1, p1, l1, r1, M1) == get(h1, p1, l2, r2, M1)
            && get(h2, p2, l1, r1, M2) == get(h2, p2, l2, r2, M2);
        cout << (ok ? "YES" : "NO") << "\n";
    }
    return 0;
}
