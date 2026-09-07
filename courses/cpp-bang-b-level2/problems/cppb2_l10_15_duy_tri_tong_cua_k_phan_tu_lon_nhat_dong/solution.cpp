#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    priority_queue<long long, vector<long long>, greater<long long>> pq;
    long long sum = 0;
    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        if ((int)pq.size() < k) {
            pq.push(x);
            sum += x;
        } else if (k > 0 && x > pq.top()) {
            sum += x - pq.top();
            pq.pop();
            pq.push(x);
        }
        cout << sum << "\n";
    }
    return 0;
}
