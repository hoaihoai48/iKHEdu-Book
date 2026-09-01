#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<double> x(n), y(n);
    for (int i = 0; i < n; ++i) cin >> x[i] >> y[i];

    auto dist_sum = [&](double cx) {
        double total = 0;
        for (int i = 0; i < n; ++i) {
            total += hypot(x[i] - cx, y[i]);
        }
        return total;
    };

    double low = -1e6, high = 1e6;
    for (int iter = 0; iter < 100; ++iter) {
        double m1 = low + (high - low) / 3.0;
        double m2 = high - (high - low) / 3.0;
        if (dist_sum(m1) < dist_sum(m2)) high = m2;
        else low = m1;
    }

    cout << fixed << setprecision(6) << dist_sum(low) << "\n";
    return 0;
}
