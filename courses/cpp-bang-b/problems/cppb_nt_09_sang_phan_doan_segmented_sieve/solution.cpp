#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long l, r;
    if (!(cin >> l >> r)) return 0;

    int lim = sqrt(r);
    vector<bool> is_prime(lim + 1, true);
    vector<int> primes;
    for (int i = 2; i <= lim; ++i) {
        if (is_prime[i]) {
            primes.push_back(i);
            for (int j = i * 2; j <= lim; j += i) is_prime[j] = false;
        }
    }

    vector<bool> is_prime_range(r - l + 1, true);
    for (int p : primes) {
        long long start = max(1LL * p * p, ((l + p - 1) / p) * p);
        for (long long j = start; j <= r; j += p) {
            is_prime_range[j - l] = false;
        }
    }

    if (l == 1) is_prime_range[0] = false;

    int count_primes = 0;
    for (int i = 0; i <= r - l; ++i) {
        if (is_prime_range[i]) count_primes++;
    }

    cout << count_primes << "\n";
    return 0;
}