#include <bits/stdc++.h>
using namespace std;

const double PI = acos(-1.0);

bool check(double area, const vector<double> &pies, int k) {
    int count = 0;
    for (double p : pies) {
        count += (int)(p / area);
    }
    return count >= k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<double> pies(n);
    double high = 0;
    for (int i = 0; i < n; ++i) {
        double r;
        cin >> r;
        pies[i] = PI * r * r;
        high = max(high, pies[i]);
    }

    double low = 0;
    for (int iter = 0; iter < 100; ++iter) {
        double mid = (low + high) / 2.0;
        if (check(mid, pies, k)) {
            low = mid;
        } else {
            high = mid;
        }
    }

    cout << fixed << setprecision(6) << low << "\n";
    return 0;
}
