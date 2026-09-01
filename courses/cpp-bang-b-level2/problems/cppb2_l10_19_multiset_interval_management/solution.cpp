#include <bits/stdc++.h>
using namespace std;

// Quản lý đoạn không dùng struct, dùng set<vector<int>> hoặc set<pair<int, int>>
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    set<vector<int>> intervals; // Mỗi đoạn là {l, r}

    while (q--) {
        int type, l, r;
        cin >> type >> l >> r;
        if (type == 1) {
            auto it = intervals.lower_bound({l, 0});
            if (it != intervals.begin() && prev(it)->at(1) >= l) it--;

            while (it != intervals.end() && it->at(0) <= r) {
                l = min(l, it->at(0));
                r = max(r, it->at(1));
                it = intervals.erase(it);
            }
            intervals.insert({l, r});
        } else {
            auto it = intervals.upper_bound({l, INT_MAX});
            if (it != intervals.begin() && prev(it)->at(1) >= r) {
                cout << "YES\n";
            } else {
                cout << "NO\n";
            }
        }
    }
    return 0;
}
