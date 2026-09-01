#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        a[i] -= i; // Chuyển dãy tăng ngặt về dãy không giảm
    }

    priority_queue<long long> pq;
    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        pq.push(a[i]);
        if (pq.top() > a[i]) {
            ans += pq.top() - a[i];
            pq.pop();
            pq.push(a[i]);
        }
    }

    cout << ans << "\n";
    return 0;
}
