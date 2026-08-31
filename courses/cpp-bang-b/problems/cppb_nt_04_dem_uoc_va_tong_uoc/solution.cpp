#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    long long count_div = 1;
    long long sum_div = 1;

    for (long long i = 2; i * i <= n; ++i) {
        if (n % i == 0) {
            int a = 0;
            long long p_pow = 1;
            long long cur_sum = 1;
            while (n % i == 0) {
                a++;
                n /= i;
                p_pow *= i;
                cur_sum += p_pow;
            }
            count_div *= (a + 1);
            sum_div *= cur_sum;
        }
    }
    if (n > 1) {
        count_div *= 2;
        sum_div *= (1 + n);
    }

    cout << count_div << " " << sum_div << "\n";
    return 0;
}