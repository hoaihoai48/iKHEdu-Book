#include <bits/stdc++.h>
using namespace std;

long long gcd_val(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long G, L;
    if (!(cin >> G >> L)) return 0;

    if (L % G != 0) {
        cout << "0\n";
        return 0;
    }

    long long prod = L / G;
    long long count = 0;

    for (long long x = 1; x * x <= prod; ++x) {
        if (prod % x == 0) {
            long long y = prod / x;
            if (gcd_val(x, y) == 1) {
                count++;
            }
        }
    }

    cout << count << "\n";
    return 0;
}
