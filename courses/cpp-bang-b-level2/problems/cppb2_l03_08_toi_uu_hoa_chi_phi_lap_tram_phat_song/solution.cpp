#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<double> x(n), cost(n);
    for (int i = 0; i < n; ++i) cin >> x[i] >> cost[i];

    auto total_cost = [&](double p) {
        double sum = 0;
        for (int i = 0; i < n; ++i) {
            sum += cost[i] * abs(x[i] - p);
        }
        return sum;
    };

    double low = -1e9, high = 1e9;
    for (int iter = 0; iter < 100; ++iter) {
        double m1 = low + (high - low) / 3.0;
        double m2 = high - (high - low) / 3.0;
        if (total_cost(m1) < total_cost(m2)) high = m2;
        else low = m1;
    }

    cout << fixed << setprecision(4) << total_cost(low) << "\n";
    return 0;
}
