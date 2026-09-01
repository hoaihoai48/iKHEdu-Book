#include <bits/stdc++.h>
using namespace std;

const long long BASE = 311;
const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int q;
    if (!(cin >> s >> q)) return 0;

    int n = s.size();
    vector<long long> h(n + 1, 0), pw(n + 1, 1);
    for (int i = 0; i < n; ++i) {
        h[i + 1] = (h[i] * BASE + s[i]) % MOD;
        pw[i + 1] = (pw[i] * BASE) % MOD;
    }

    auto get_hash = [&](int l, int r) {
        return (h[r] - h[l - 1] * pw[r - l + 1] % MOD + MOD) % MOD;
    };

    while (q--) {
        int i, j; cin >> i >> j;
        int low = 1, high = n - max(i, j) + 1, ans = 0;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (get_hash(i, i + mid - 1) == get_hash(j, j + mid - 1)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}
