#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> primes;
    long long temp = m;
    for (long long p = 2; p * p <= temp; ++p) {
        if (temp % p == 0) {
            primes.push_back(p);
            while (temp % p == 0) temp /= p;
        }
    }
    if (temp > 1) primes.push_back(temp);

    int k = primes.size();
    long long coprime_cnt = 0;

    for (int mask = 0; mask < (1 << k); ++mask) {
        long long prod = 1;
        int bits = 0;
        for (int i = 0; i < k; ++i) {
            if ((mask >> i) & 1) {
                bits++;
                prod *= primes[i];
            }
        }
        if (bits % 2 == 1) coprime_cnt -= n / prod;
        else coprime_cnt += n / prod;
    }

    cout << coprime_cnt << "\n";
    return 0;
}
