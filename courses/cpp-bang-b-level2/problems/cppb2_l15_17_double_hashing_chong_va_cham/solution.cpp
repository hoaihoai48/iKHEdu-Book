#include <bits/stdc++.h>
using namespace std;

// Double Hashing (MOD1 = 10^9+7, MOD2 = 10^9+9, Base = 311)
const int MOD1 = 1000000007;
const int MOD2 = 1000000009;
const int BASE = 311;
const int MAXN = 200005;

long long h1[MAXN], h2[MAXN], p1[MAXN], p2[MAXN];

void init_hash(const string& s) {
    int n = s.size();
    p1[0] = p2[0] = 1;
    for (int i = 1; i <= n; ++i) {
        p1[i] = (p1[i - 1] * BASE) % MOD1;
        p2[i] = (p2[i - 1] * BASE) % MOD2;
    }
    for (int i = 1; i <= n; ++i) {
        h1[i] = (h1[i - 1] * BASE + s[i - 1]) % MOD1;
        h2[i] = (h2[i - 1] * BASE + s[i - 1]) % MOD2;
    }
}

pair<long long, long long> get_hash(int l, int r) {
    long long hash_val1 = (h1[r] - h1[l - 1] * p1[r - l + 1]) % MOD1;
    if (hash_val1 < 0) hash_val1 += MOD1;

    long long hash_val2 = (h2[r] - h2[l - 1] * p2[r - l + 1]) % MOD2;
    if (hash_val2 < 0) hash_val2 += MOD2;

    return {hash_val1, hash_val2};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s; int q;
    if (!(cin >> s >> q)) return 0;

    init_hash(s);

    while (q--) {
        int l1, r1, l2, r2;
        cin >> l1 >> r1 >> l2 >> r2;
        if (get_hash(l1, r1) == get_hash(l2, r2)) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
    return 0;
}
