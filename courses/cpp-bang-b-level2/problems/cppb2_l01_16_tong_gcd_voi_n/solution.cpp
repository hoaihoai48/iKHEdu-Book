#include <bits/stdc++.h>
using namespace std;

long long get_phi(long long n) {
    long long res = n;
    for (long long p = 2; p * p <= n; ++p) {
        if (n % p == 0) {
            while (n % p == 0) n /= p;
            res -= res / p;
        }
    }
    if (n > 1) res -= res / n;
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    long long total_sum = 0;
    for (long long d = 1; d * d <= n; ++d) {
        if (n % d == 0) {
            total_sum += d * get_phi(n / d);
            if (d * d != n) {
                long long other_d = n / d;
                total_sum += other_d * get_phi(n / other_d);
            }
        }
    }
    cout << total_sum << "\n";
    return 0;
}
