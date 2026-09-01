#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long d;
    if (!(cin >> d)) return 0;

    long long m = 0, d_val = 1, a0 = sqrt(d), a = a0;
    if (a0 * a0 == d) return 0;

    __int128 p0 = a0, p1 = 1, q0 = 1, q1 = 0;
    __int128 p = p0, q = q0;

    while (p * p - (__int128)d * q * q != 1) {
        m = d_val * a - m;
        d_val = (d - m * m) / d_val;
        a = (a0 + m) / d_val;
        p = a * p0 + p1;
        q = a * q0 + q1;
        p1 = p0; p0 = p;
        q1 = q0; q0 = q;
    }

    cout << (long long)p << " " << (long long)q << "\n";
    return 0;
}
