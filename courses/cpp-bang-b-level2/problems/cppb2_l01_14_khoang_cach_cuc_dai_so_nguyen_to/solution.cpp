#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    long long lim = sqrt(R);
    vector<bool> is_prime_small(lim + 1, true);
    vector<long long> primes;
    for (long long i = 2; i <= lim; ++i) {
        if (is_prime_small[i]) {
            primes.push_back(i);
            for (long long j = i * i; j <= lim; j += i) is_prime_small[j] = false;
        }
    }

    vector<bool> is_prime_range(R - L + 1, true);
    for (long long p : primes) {
        long long start = max(p * p, ((L + p - 1) / p) * p);
        for (long long j = start; j <= R; j += p) {
            is_prime_range[j - L] = false;
        }
    }
    if (L == 1 && R >= 1) is_prime_range[0] = false;

    vector<long long> seg_primes;
    for (long long i = 0; i <= R - L; ++i) {
        if (is_prime_range[i]) seg_primes.push_back(L + i);
    }

    if (seg_primes.size() < 2) {
        cout << "-1\n";
        return 0;
    }

    long long max_gap = 0;
    for (size_t i = 1; i < seg_primes.size(); ++i) {
        max_gap = max(max_gap, seg_primes[i] - seg_primes[i - 1]);
    }
    cout << max_gap << "\n";
    return 0;
}
