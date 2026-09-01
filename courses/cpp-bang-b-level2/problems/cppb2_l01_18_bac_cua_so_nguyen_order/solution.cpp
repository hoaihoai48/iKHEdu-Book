#include <bits/stdc++.h>
using namespace std;

long long power(long long a, long long b, long long m) {
    long long res = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128)res * a % m;
        a = (__int128)a * a % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, p;
    if (!(cin >> a >> p)) return 0;

    long long phi = p - 1;
    vector<long long> divs;
    for (long long i = 1; i * i <= phi; ++i) {
        if (phi % i == 0) {
            divs.push_back(i);
            if (i * i != phi) divs.push_back(phi / i);
        }
    }
    sort(divs.begin(), divs.end());

    for (long long d : divs) {
        if (power(a, d, p) == 1) {
            cout << d << "\n";
            return 0;
        }
    }
    cout << phi << "\n";
    return 0;
}
