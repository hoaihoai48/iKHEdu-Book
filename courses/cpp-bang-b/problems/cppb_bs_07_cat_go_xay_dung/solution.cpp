#include <bits/stdc++.h>
using namespace std;

bool check(long long h, const vector<long long>& a, long long m) {
    long long wood = 0;
    for (long long x : a) {
        if (x > h) {
            wood += (x - h);
        }
    }
    return wood >= m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n);
    long long max_val = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
    }

    long long low = 0, high = max_val, ans = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, a, m)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
