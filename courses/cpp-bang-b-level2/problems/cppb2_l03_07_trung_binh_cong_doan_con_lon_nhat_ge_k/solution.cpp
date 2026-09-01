#include <bits/stdc++.h>
using namespace std;

bool check(double mid, const vector<long long> &a, int k) {
    int n = a.size();
    vector<double> pref(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + (a[i] - mid);
    }

    double min_pref = 0;
    for (int i = k; i <= n; ++i) {
        min_pref = min(min_pref, pref[i - k]);
        if (pref[i] - min_pref >= 0) return true;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    double low = 1e18, high = -1e18;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        low = min(low, (double)a[i]);
        high = max(high, (double)a[i]);
    }

    for (int iter = 0; iter < 100; ++iter) {
        double mid = (low + high) / 2.0;
        if (check(mid, a, k)) low = mid;
        else high = mid;
    }

    cout << fixed << setprecision(4) << low << "\n";
    return 0;
}
