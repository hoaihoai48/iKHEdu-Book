#include <bits/stdc++.h>
using namespace std;

struct Interval {
    long long l, r;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<Interval> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].l >> a[i].r;

    sort(a.begin(), a.end(), [](const Interval& x, const Interval& y) {
        if (x.l != y.l) return x.l < y.l;
        return x.r < y.r;
    });

    vector<Interval> merged;
    merged.push_back(a[0]);

    for (int i = 1; i < n; ++i) {
        if (a[i].l <= merged.back().r) {
            merged.back().r = max(merged.back().r, a[i].r);
        } else {
            merged.push_back(a[i]);
        }
    }

    cout << merged.size() << "\n";
    for (const auto& iv : merged) {
        cout << iv.l << " " << iv.r << "\n";
    }
    return 0;
}
