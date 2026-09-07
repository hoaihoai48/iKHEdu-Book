#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    if (!(cin >> n >> W)) return 0;
    vector<long long> w(n), v(n);
    for (int i = 0; i < n; ++i) cin >> w[i] >> v[i];

    int n1 = n / 2;
    vector<pair<long long, long long>> A;
    A.reserve(1u << min(n1, 22));
    for (long long mask = 0; mask < (1LL << n1); ++mask) {
        long long sw = 0, sv = 0;
        for (int i = 0; i < n1; ++i) if (mask & (1LL << i)) {
            sw += w[i]; sv += v[i];
        }
        if (sw <= W) A.push_back({sw, sv});
    }
    sort(A.begin(), A.end());
    vector<long long> bw, bv;
    long long best = -1;
    for (auto &p : A) {
        if (p.second > best) {
            best = p.second;
            bw.push_back(p.first);
            bv.push_back(best);
        }
    }
    long long ans = 0;
    int n2 = n - n1;
    for (long long mask = 0; mask < (1LL << n2); ++mask) {
        long long sw = 0, sv = 0;
        for (int i = 0; i < n2; ++i) if (mask & (1LL << i)) {
            sw += w[n1 + i]; sv += v[n1 + i];
        }
        if (sw > W) continue;
        long long rem = W - sw;
        int idx = (int)(upper_bound(bw.begin(), bw.end(), rem) - bw.begin()) - 1;
        long long cur = sv + (idx >= 0 ? bv[idx] : 0);
        ans = max(ans, cur);
    }
    cout << ans << "\n";
    return 0;
}
