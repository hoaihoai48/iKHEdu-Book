#include <bits/stdc++.h>
using namespace std;

// Tính xác suất có điều kiện P(A|B) qua phân phối nhị thức
double nCr_real(int n, int r) {
    if (r < 0 || r > n) return 0.0;
    double res = 1.0;
    for (int i = 1; i <= r; ++i) {
        res = res * (n - i + 1) / i;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, m;
    if (!(cin >> n >> k >> m)) return 0;

    // Tung n lần, biết có ít nhất m mặt ngửa, tính xác suất có đúng k mặt ngửa
    if (k < m) {
        cout << fixed << setprecision(6) << 0.0 << "\n";
        return 0;
    }

    double total_prob_m = 0.0;
    for (int i = m; i <= n; ++i) {
        total_prob_m += nCr_real(n, i);
    }

    double prob_k = nCr_real(n, k);
    double ans = prob_k / total_prob_m;

    cout << fixed << setprecision(6) << ans << "\n";
    return 0;
}
