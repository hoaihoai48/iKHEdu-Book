#include <bits/stdc++.h>
using namespace std;

void gen(int idx, int end_idx, long long cur, const vector<long long> &a, vector<long long> &res) {
    if (idx == end_idx) {
        res.push_back(cur);
        return;
    }
    gen(idx + 1, end_idx, cur, a, res);
    gen(idx + 1, end_idx, cur + a[idx], a, res);
    gen(idx + 1, end_idx, cur - a[idx], a, res);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long T;
    if (!(cin >> n >> T)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int mid = n / 2;
    vector<long long> s1, s2;
    gen(0, mid, 0, a, s1);
    gen(mid, n, 0, a, s2);
    sort(s2.begin(), s2.end());

    long long ans = 0;
    for (long long x : s1) {
        auto r = equal_range(s2.begin(), s2.end(), T - x);
        ans += (long long)(r.second - r.first);
    }
    cout << ans << "\n";
    return 0;
}
