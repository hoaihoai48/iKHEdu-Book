#include <bits/stdc++.h>
using namespace std;

struct Station {
    long long dist, fuel;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long target, start_fuel;
    if (!(cin >> n >> target >> start_fuel)) return 0;

    vector<Station> st(n);
    for (int i = 0; i < n; ++i) cin >> st[i].dist >> st[i].fuel;

    sort(st.begin(), st.end(), [](const Station &a, const Station &b) {
        return a.dist < b.dist;
    });

    priority_queue<long long> max_fuel_pq;
    long long cur_fuel = start_fuel;
    int stops = 0;
    int idx = 0;

    while (cur_fuel < target) {
        while (idx < n && st[idx].dist <= cur_fuel) {
            max_fuel_pq.push(st[idx].fuel);
            idx++;
        }
        if (max_fuel_pq.empty()) {
            cout << "-1\n";
            return 0;
        }
        cur_fuel += max_fuel_pq.top();
        max_fuel_pq.pop();
        stops++;
    }

    cout << stops << "\n";
    return 0;
}
