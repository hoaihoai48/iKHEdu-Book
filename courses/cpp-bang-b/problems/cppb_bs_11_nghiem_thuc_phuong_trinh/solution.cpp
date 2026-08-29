#include <bits/stdc++.h>
using namespace std;

double f(double x) {
    return x * x * x + 2.0 * x * x + 10.0 * x;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double c;
    if (!(cin >> c)) return 0;

    double low = 0.0, high = 1000.0;
    for (int iter = 0; iter < 100; ++iter) {
        double mid = low + (high - low) / 2.0;
        if (f(mid) >= c) {
            high = mid;
        } else {
            low = mid;
        }
    }

    cout << fixed << setprecision(6) << low << "\n";
    return 0;
}
