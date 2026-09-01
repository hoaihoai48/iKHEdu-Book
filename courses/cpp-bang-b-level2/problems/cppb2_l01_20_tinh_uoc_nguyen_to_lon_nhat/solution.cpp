#include <bits/stdc++.h>
using namespace std;

long long get_max_prime_factor(long long n) {
    long long max_p = -1;
    while (n % 2 == 0) { max_p = 2; n /= 2; }
    for (long long i = 3; i * i <= n; i += 2) {
        while (n % i == 0) {
            max_p = i;
            n /= i;
        }
    }
    if (n > 1) max_p = max(max_p, n);
    return max_p;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    long long ans = -1;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        ans = max(ans, get_max_prime_factor(x));
    }
    cout << ans << "\n";
    return 0;
}
