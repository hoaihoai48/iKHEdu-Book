#include <bits/stdc++.h>
using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1; y = 0;
        return a;
    }
    long long x1, y1;
    long long g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, S;
    if (!(cin >> a >> b >> S)) return 0;

    long long x0, y0;
    long long g = extgcd(a, b, x0, y0);

    if (S % g != 0) {
        cout << "-1\n";
        return 0;
    }

    x0 *= (S / g);
    y0 *= (S / g);

    long long b_prime = b / g;
    long long a_prime = a / g;

    long long k_min = ceil((double)(-x0) / b_prime);
    long long k_max = floor((double)(y0) / a_prime);

    if (k_min > k_max) {
        cout << "-1\n";
        return 0;
    }

    long long min_coins = 2e18;
    for (long long k : {k_min, k_max}) {
        long long cur_x = x0 + k * b_prime;
        long long cur_y = y0 - k * a_prime;
        if (cur_x >= 0 && cur_y >= 0) {
            min_coins = min(min_coins, cur_x + cur_y);
        }
    }
    cout << min_coins << "\n";
    return 0;
}
