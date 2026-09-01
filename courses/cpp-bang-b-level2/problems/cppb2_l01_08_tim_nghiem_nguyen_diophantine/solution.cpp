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
    long long g = extgcd(abs(a), abs(b), x0, y0);

    if (c % g != 0) {
        cout << "-1\n";
    } else {
        if (a < 0) x0 = -x0;
        if (b < 0) y0 = -y0;
        x0 *= (c / g);
        y0 *= (c / g);
        cout << x0 << " " << y0 << "\n";
    }
    return 0;
}
