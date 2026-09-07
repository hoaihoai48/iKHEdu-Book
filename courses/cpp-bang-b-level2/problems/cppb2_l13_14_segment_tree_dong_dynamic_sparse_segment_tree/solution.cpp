#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q;
    if (!(cin >> Q)) return 0;
    struct Op { int t; long long x, y; };
    vector<Op> ops(Q);
    vector<long long> coords;
    for (int i = 0; i < Q; i++) {
        int t; cin >> t; ops[i].t = t;
        if (t == 1) { long long id, v; cin >> id >> v; ops[i].x = id; ops[i].y = v; coords.push_back(id); }
        else { long long l, r; cin >> l >> r; ops[i].x = l; ops[i].y = r; }
    }
    sort(coords.begin(), coords.end());
    coords.erase(unique(coords.begin(), coords.end()), coords.end());
    int M = (int)coords.size();
    vector<long long> bit(M + 2, 0);
    auto add = [&](int i, long long v) { for (; i <= M; i += i & -i) bit[i] += v; };
    auto sum = [&](int i) { long long s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; };
    for (auto &op : ops) {
        if (op.t == 1) {
            int i = (int)(lower_bound(coords.begin(), coords.end(), op.x) - coords.begin()) + 1;
            add(i, op.y);
        } else {
            int R = (int)(upper_bound(coords.begin(), coords.end(), op.y) - coords.begin());
            int L = (int)(lower_bound(coords.begin(), coords.end(), op.x) - coords.begin());
            cout << sum(R) - sum(L) << "\n";
        }
    }
    return 0;
}
