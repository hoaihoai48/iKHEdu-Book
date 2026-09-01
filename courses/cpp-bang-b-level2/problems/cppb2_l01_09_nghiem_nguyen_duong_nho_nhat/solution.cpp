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

    long long a, b, c;
    if (!(cin >> a >> b >> c)) return 0;

    long long x0, y0;
    long long g = extgcd(a, b, x0, y0);

    if (c % g != 0) {
        cout << "-1\n";
        return 0;
    }

    x0 *= (c / g);
    y0 *= (c / g);

    long long b_prime = b / g;
    long long a_prime = a / g;

    long long k = (-x0) / b_prime;
    while (x0 + k * b_prime <= 0) k++;
    while (x0 + (k - 1) * b_prime > 0) k--;

    long long x_min = x0 + k * b_prime;
    long long y_cor = (c - a * x_min) / b;

    cout << x_min << " " << y_cor << "\n";
    return 0;
}
