#include <bits/stdc++.h>
using namespace std;

struct Delivery {
    int deadline;
    long long profit;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Delivery> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].deadline >> a[i].profit;

    sort(a.begin(), a.end(), [](const Delivery &x, const Delivery &y) {
        return x.deadline < y.deadline;
    });

    priority_queue<long long, vector<long long>, greater<long long>> pq;

    for (const auto &d : a) {
        if ((int)pq.size() < d.deadline) {
            pq.push(d.profit);
        } else if (!pq.empty() && pq.top() < d.profit) {
            pq.pop();
            pq.push(d.profit);
        }
    }

    long long total_profit = 0;
    while (!pq.empty()) {
        total_profit += pq.top();
        pq.pop();
    }

    cout << total_profit << "\n";
    return 0;
}
