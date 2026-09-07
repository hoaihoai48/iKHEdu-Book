#include <bits/stdc++.h>
using namespace std;

const long long BASE = 9113823;
const long long MOD1 = 1000000007;
const long long MOD2 = 1000000009;

long long getHash(const vector<long long> &h, const vector<long long> &pw, int l, int r, long long mod) {
    long long res = (h[r + 1] - h[l] * pw[r - l + 1] % mod + mod) % mod;
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    int n = (int)s.size();

    vector<long long> h1(n + 1, 0), pw1(n + 1, 1);
    vector<long long> h2(n + 1, 0), pw2(n + 1, 1);
    for (int i = 0; i < n; ++i) {
        long long v = (s[i] - 'a' + 1);
        h1[i + 1] = (h1[i] * BASE + v) % MOD1;
        pw1[i + 1] = (pw1[i] * BASE) % MOD1;
        h2[i + 1] = (h2[i] * BASE + v) % MOD2;
        pw2[i + 1] = (pw2[i] * BASE) % MOD2;
    }

    int q;
    cin >> q;
    for (int i = 0; i < q; ++i) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        --a; --b; --c; --d;
        if ((b - a) != (d - c)) {
            cout << "NO\n";
            continue;
        }
        bool ok = getHash(h1, pw1, a, b, MOD1) == getHash(h1, pw1, c, d, MOD1)
               && getHash(h2, pw2, a, b, MOD2) == getHash(h2, pw2, c, d, MOD2);
        cout << (ok ? "YES" : "NO") << "\n";
    }
    return 0;
}
