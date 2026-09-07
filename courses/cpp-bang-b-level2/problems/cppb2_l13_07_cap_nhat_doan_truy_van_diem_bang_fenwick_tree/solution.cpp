#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, Q;
    if (!(cin >> N >> Q)) return 0;
    vector<long long> bit(N + 2, 0);
    auto add = [&](int i, long long v) { for (; i <= N; i += i & -i) bit[i] += v; };
    auto sum = [&](int i) { long long s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; };
    while (Q--) {
        int t; cin >> t;
        if (t == 1) { int l, r; long long v; cin >> l >> r >> v; add(l, v); if (r + 1 <= N) add(r + 1, -v); }
        else { int i; cin >> i; cout << sum(i) << "\n"; }
    }
    return 0;
}
