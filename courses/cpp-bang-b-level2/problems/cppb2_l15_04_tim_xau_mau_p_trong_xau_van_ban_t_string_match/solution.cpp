#include <bits/stdc++.h>
using namespace std;

const long long BASE = 311;
const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    vector<long long> hf(n + 1, 0), hb(n + 2, 0), pw(n + 1, 1);

    for (int i = 0; i < n; ++i) {
        hf[i + 1] = (hf[i] * BASE + s[i]) % MOD;
        pw[i + 1] = (pw[i] * BASE) % MOD;
    }
    for (int i = n - 1; i >= 0; --i) {
        hb[i + 1] = (hb[i + 2] * BASE + s[i]) % MOD;
    }

    auto get_f = [&](int l, int r) {
        return (hf[r] - hf[l - 1] * pw[r - l + 1] % MOD + MOD) % MOD;
    };
    auto get_b = [&](int l, int r) {
        return (hb[l] - hb[r + 1] * pw[r - l + 1] % MOD + MOD) % MOD;
    };

    int max_len = 1;
    for (int i = 1; i <= n; ++i) {
        // Lẻ
        int low = 1, high = min(i, n - i + 1), best_odd = 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (get_f(i - mid + 1, i + mid - 1) == get_b(i - mid + 1, i + mid - 1)) {
                best_odd = 2 * mid - 1;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        max_len = max(max_len, best_odd);

        // Chẵn
        if (i < n && s[i - 1] == s[i]) {
            low = 1; high = min(i, n - i); int best_even = 2;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (get_f(i - mid + 1, i + mid) == get_b(i - mid + 1, i + mid)) {
                    best_even = 2 * mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            max_len = max(max_len, best_even);
        }
    }

    cout << max_len << "\n";
    return 0;
}
