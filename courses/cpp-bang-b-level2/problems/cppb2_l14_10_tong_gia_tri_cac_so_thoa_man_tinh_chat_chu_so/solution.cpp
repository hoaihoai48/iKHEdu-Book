#include <bits/stdc++.h>
using namespace std;

long long sum_all_digits(long long n) {
    if (n <= 0) return 0;
    long long total = 0;
    for (long long m = 1; m <= n; m *= 10) {
        long long a = n / m, b = n % m;
        int cur = a % 10;
        total += (a / 10) * 45 * m;
        for (int d = 0; d < cur; ++d) total += d * m;
        total += cur * (b + 1);
    }
    return total;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << sum_all_digits(R) - sum_all_digits(L - 1) << "\n";
    return 0;
}
