#include <bits/stdc++.h>
using namespace std;

bool check(long long cap, const vector<long long> &w, int days) {
    int d = 1;
    long long cur = 0;
    for (long long x : w) {
        if (x > cap) return false;
        if (cur + x > cap) {
            d++;
            cur = x;
        } else {
            cur += x;
        }
    }
    return d <= days;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, days;
    if (!(cin >> n >> days)) return 0;

    vector<long long> w(n);
    long long low = 0, high = 0;
    for (int i = 0; i < n; ++i) {
        cin >> w[i];
        low = max(low, w[i]);
        high += w[i];
    }

    long long ans = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, w, days)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
