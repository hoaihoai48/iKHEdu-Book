#include <bits/stdc++.h>
using namespace std;

long long count_digit(long long n, int d) {
    long long count = 0;
    for (long long m = 1; m <= n; m *= 10) {
        long long a = n / m, b = n % m;
        int cur = a % 10;
        if (d > 0) {
            count += (a / 10) * m + (cur > d ? m : (cur == d ? b + 1 : 0));
        } else {
            if (a / 10 > 0) count += (a / 10 - 1) * m + (cur > 0 ? m : b + 1);
        }
    }
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R; int d;
    if (!(cin >> L >> R >> d)) return 0;

    cout << count_digit(R, d) - count_digit(L - 1, d) << "\n";
    return 0;
}
