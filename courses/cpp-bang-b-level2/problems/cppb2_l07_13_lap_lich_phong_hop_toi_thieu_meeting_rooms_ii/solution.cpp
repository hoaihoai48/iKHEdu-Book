#include <bits/stdc++.h>
using namespace std;

struct Interval {
    long long s, e;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Interval> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].s >> a[i].e;

    sort(a.begin(), a.end(), [](const Interval &x, const Interval &y) {
        return x.s < y.s;
    });

    priority_queue<long long, vector<long long>, greater<long long>> min_end_pq;

    for (const auto &it : a) {
        if (!min_end_pq.empty() && min_end_pq.top() <= it.s) {
            min_end_pq.pop();
        }
        min_end_pq.push(it.e);
    }

    cout << min_end_pq.size() << "\n";
    return 0;
}
