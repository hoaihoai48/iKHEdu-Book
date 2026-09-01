#include <bits/stdc++.h>
using namespace std;

double f(double x, double c) {
    return x * x + sqrt(x) - c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double c;
    if (!(cin >> c)) return 0;

    double low = 0, high = 1e5;
    for (int iter = 0; iter < 100; ++iter) {
        double mid = (low + high) / 2.0;
        if (f(mid, c) <= 0) low = mid;
        else high = mid;
    }

    cout << fixed << setprecision(6) << low << "\n";
    return 0;
}
