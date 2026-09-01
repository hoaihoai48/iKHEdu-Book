#include <bits/stdc++.h>
using namespace std;

long long gcd_val(long long a, long long b) {
    while (b) { a %= b; swap(a, b); }
    return a;
}

long long lcm_val(long long a, long long b) {
    return (a / gcd_val(a, b)) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> primes(k);
    for (int i = 0; i < k; ++i) cin >> primes[i];

    long long count = 0;
    for (int mask = 1; mask < (1 << k); ++mask) {
        long long cur_lcm = 1;
        int bits = 0;
        bool overflow = false;

        for (int i = 0; i < k; ++i) {
            if ((mask >> i) & 1) {
                bits++;
                cur_lcm = lcm_val(cur_lcm, primes[i]);
                if (cur_lcm > n) { overflow = true; break; }
            }
        }

        if (overflow) continue;

        if (bits % 2 == 1) count += n / cur_lcm;
        else count -= n / cur_lcm;
    }

    cout << count << "\n";
    return 0;
}
