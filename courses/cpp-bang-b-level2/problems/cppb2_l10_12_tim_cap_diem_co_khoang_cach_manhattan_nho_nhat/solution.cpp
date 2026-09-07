#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> xs(n), ys(n);
    for (int i = 0; i < n; ++i) cin >> xs[i] >> ys[i];
    vector<pair<long long, long long>> p(n);
    for (int i = 0; i < n; ++i) p[i] = {xs[i] + ys[i], xs[i] - ys[i]};
    sort(p.begin(), p.end());
    for (int i = 1; i < n; ++i) {
        if (p[i] == p[i - 1]) {
            cout << 0 << "\n";
            return 0;
        }
    }
    long long d = llabs(p[1].first - p[0].first) + llabs(p[1].second - p[0].second);
    if (d == 0) d = 1;
    set<pair<long long, long long>> box;
    deque<int> win;
    const long long NEG = (long long)-4e18;
    for (int i = 0; i < n; ++i) {
        while (!win.empty() && p[win.front()].first < p[i].first - d) {
            box.erase({p[win.front()].second, p[win.front()].first});
            win.pop_front();
        }
        auto itlow = box.lower_bound({p[i].second - d, NEG});
        for (auto it = itlow; it != box.end() && it->first <= p[i].second + d; ++it) {
            long long du = llabs(p[i].first - it->second);
            long long dv = llabs(p[i].second - it->first);
            long long man = max(du, dv);
            if (man < d) d = man;
            if (d == 1) {
                cout << 1 << "\n";
                return 0;
            }
        }
        box.insert({p[i].second, p[i].first});
        win.push_back(i);
    }
    cout << d << "\n";
    return 0;
}
