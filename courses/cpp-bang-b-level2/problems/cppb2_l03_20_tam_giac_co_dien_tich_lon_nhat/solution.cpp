#include <bits/stdc++.h>
using namespace std;

// Diện tích tam giác tính theo tọa độ không dùng struct
long long cross_product(long long x1, long long y1, long long x2, long long y2, long long x3, long long y3) {
    return abs((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> x(n), y(n);
    for (int i = 0; i < n; ++i) cin >> x[i] >> y[i];

    long long max_area2 = 0;
    for (int i = 0; i < n; ++i) {
        int k = (i + 2) % n;
        for (int j = (i + 1) % n; j != i; j = (j + 1) % n) {
            while (cross_product(x[i], y[i], x[j], y[j], x[(k + 1) % n], y[(k + 1) % n]) >
                   cross_product(x[i], y[i], x[j], y[j], x[k], y[k])) {
                k = (k + 1) % n;
            }
            max_area2 = max(max_area2, cross_product(x[i], y[i], x[j], y[j], x[k], y[k]));
        }
    }

    cout << fixed << setprecision(1) << max_area2 / 2.0 << "\n";
    return 0;
}
