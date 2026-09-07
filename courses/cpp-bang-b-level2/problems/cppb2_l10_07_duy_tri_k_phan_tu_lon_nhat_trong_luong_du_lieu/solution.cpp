#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    priority_queue<long long, vector<long long>, greater<long long>> pq;
    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        pq.push(x);
        if ((int)pq.size() > k) pq.pop();
        if ((int)pq.size() < k) cout << -1 << "\n";
        else cout << pq.top() << "\n";
    }
    return 0;
}
