#include <bits/stdc++.h>
using namespace std;

const int MAXA = 1000000;
int spf[MAXA + 1];

void sieve_spf() {
    for (int i = 1; i <= MAXA; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXA; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXA; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve_spf();

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        int x;
        cin >> x;
        long long num_divisors = 1;
        long long sum_divisors = 1;

        while (x > 1) {
            int p = spf[x];
            int cnt = 0;
            long long p_pow = 1;
            long long cur_sum = 1;
            while (x % p == 0) {
                cnt++;
                p_pow *= p;
                cur_sum += p_pow;
                x /= p;
            }
            num_divisors *= (cnt + 1);
            sum_divisors *= cur_sum;
        }
        cout << num_divisors << " " << sum_divisors << "\n";
    }
    return 0;
}
