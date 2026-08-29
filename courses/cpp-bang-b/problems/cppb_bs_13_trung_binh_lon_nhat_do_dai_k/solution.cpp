#include <bits/stdc++.h>
using namespace std;

bool check(double mid, const vector<double>& a, int n, int k) {
    vector<double> p(n + 1, 0.0);
    for (int i = 1; i <= n; ++i) {
        p[i] = p[i - 1] + (a[i - 1] - mid);
    }

    double min_p = 0.0;
    for (int i = k; i <= n; ++i) {
        min_p = min(min_p, p[i - k]);
        if (p[i] - min_p >= -1e-9) {
            return true;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<double> a(n);
    double max_val = 0.0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
    }

    double low = 0.0, high = max_val;
    for (int iter = 0; iter < 80; ++iter) {
        double mid = low + (high - low) / 2.0;
        if (check(mid, a, n, k)) {
            low = mid;
        } else {
            high = mid;
        }
    }

    cout << fixed << setprecision(4) << low << "\n";
    return 0;
}
