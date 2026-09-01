#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    set<pair<long long, long long>> intervals;

    while (q--) {
        long long l, r;
        cin >> l >> r;

        auto it = intervals.lower_bound({l, -1e18});
        while (it != intervals.end() && it->second <= r) {
            l = min(l, it->second);
            r = max(r, it->first);
            it = intervals.erase(it);
        }
        intervals.insert({r, l});
    }

    long long total_len = 0;
    for (auto it : intervals) {
        total_len += (it.first - it.second);
    }
    cout << total_len << "\n";
    return 0;
}
