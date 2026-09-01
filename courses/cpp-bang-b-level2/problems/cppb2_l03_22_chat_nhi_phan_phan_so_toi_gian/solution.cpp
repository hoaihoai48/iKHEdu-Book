#include <bits/stdc++.h>
using namespace std;

// Tìm phân số tối giản thứ K trong đoạn (0, 1) có mẫu <= N
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; long long k;
    if (!(cin >> n >> k)) return 0;

    double low = 0.0, high = 1.0;
    int best_p = 0, best_q = 1;

    for (int iter = 0; iter < 60; ++iter) {
        double mid = (low + high) / 2.0;
        long long count = 0;
        int p_curr = 0, q_curr = 1;

        for (int q = 1; q <= n; ++q) {
            int p = (int)(mid * q);
            count += p;
            if (p > 0 && 1.0 * p / q > 1.0 * p_curr / q_curr) {
                p_curr = p;
                q_curr = q;
            }
        }

        if (count < k) {
            low = mid;
        } else {
            best_p = p_curr;
            best_q = q_curr;
            high = mid;
        }
    }

    cout << best_p << " " << best_q << "\n";
    return 0;
}
