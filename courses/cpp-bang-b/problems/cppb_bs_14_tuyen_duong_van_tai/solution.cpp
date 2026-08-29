#include <bits/stdc++.h>
using namespace std;

bool check(long long cap, const vector<long long>& a, int n, int m, int d) {
    int trucks = 0;
    int i = 0;
    while (i < n) {
        trucks++;
        if (trucks > m) return false;
        long long current_load = 0;
        int count_cities = 0;
        while (i < n && count_cities < d && current_load + a[i] <= cap) {
            current_load += a[i];
            count_cities++;
            i++;
        }
    }
    return trucks <= m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, d;
    if (!(cin >> n >> m >> d)) return 0;

    vector<long long> a(n);
    long long max_val = 0, sum_val = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
        sum_val += a[i];
    }

    long long low = max_val, high = sum_val, ans = sum_val;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, a, n, m, d)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
