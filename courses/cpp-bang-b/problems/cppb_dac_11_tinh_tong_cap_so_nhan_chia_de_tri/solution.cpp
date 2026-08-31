#include <bits/stdc++.h>
using namespace std;

long long powerMod(long long a, long long b, long long m) {
    long long res = 1 % m;
    a %= m;
    while (b > 0) {
        if (b & 1) res = (res * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return res;
}

long long sumGeoDac(long long a, long long n, long long m) {
    if (n == 0) return 1 % m;
    if (n % 2 == 1) {
        long long k = n / 2;
        long long half_sum = sumGeoDac(a, k, m);
        long long mult = (1 + powerMod(a, k + 1, m)) % m;
        return (half_sum * mult) % m;
    } else {
        long long prev = sumGeoDac(a, n - 1, m);
        return (prev + powerMod(a, n, m)) % m;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long a, n, m;
    if (!(cin >> a >> n >> m)) return 0;
    cout << sumGeoDac(a, n, m) << "\n";
    return 0;
}
