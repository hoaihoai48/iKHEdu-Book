#include <bits/stdc++.h>
using namespace std;
long long powIter(long long a, long long b, long long m) {
    long long res = 1 % m;
    a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128)res * a % m;
        a = (__int128)a * a % m;
        b >>= 1;
    }
    return res;
}
int main() {
    long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;
    cout << powIter(a, b, m) << "\n";
    return 0;
}
