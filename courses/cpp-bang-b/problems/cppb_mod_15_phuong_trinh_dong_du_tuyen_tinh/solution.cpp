#include <bits/stdc++.h>
using namespace std;

long long extGCD(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long d = extGCD(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;

    long long x, y;
    long long g = extGCD(a, m, x, y);

    if (b % g != 0) {
        cout << -1 << "\n";
        return 0;
    }

    x = (x % m + m) % m;
    long long m_prime = m / g;
    long long ans = (x * ((b / g) % m_prime)) % m_prime;
    ans = (ans % m_prime + m_prime) % m_prime;

    cout << ans << "\n";
    return 0;
}