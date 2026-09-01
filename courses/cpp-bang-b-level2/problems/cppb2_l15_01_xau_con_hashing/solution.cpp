#include <bits/stdc++.h>
using namespace std;

const long long BASE = 311;
const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string t, p;
    if (!(cin >> t >> p)) return 0;

    int n = t.size(), m = p.size();
    if (n < m) return 0;

    vector<long long> h(n + 1, 0), pw(n + 1, 1);
    for (int i = 0; i < n; ++i) {
        h[i + 1] = (h[i] * BASE + t[i]) % MOD;
        pw[i + 1] = (pw[i] * BASE) % MOD;
    }

    long long hash_p = 0;
    for (char c : p) hash_p = (hash_p * BASE + c) % MOD;

    for (int i = 0; i <= n - m; ++i) {
        long long cur_hash = (h[i + m] - h[i] * pw[m] % MOD + MOD) % MOD;
        if (cur_hash == hash_p) {
            cout << i + 1 << " ";
        }
    }
    cout << "\n";
    return 0;
}
