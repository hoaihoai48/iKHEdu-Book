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

    long long p;
    if (!(cin >> p)) return 0;

    long long phi = p - 1;
    vector<long long> factors;
    long long temp = phi;
    for (long long i = 2; i * i <= temp; ++i) {
        if (temp % i == 0) {
            factors.push_back(i);
            while (temp % i == 0) temp /= i;
        }
    }
    if (temp > 1) factors.push_back(temp);

    for (long long g = 2; g < p; ++g) {
        bool ok = true;
        for (long long f : factors) {
            if (power(g, phi / f, p) == 1) {
                ok = false;
                break;
            }
        }
        if (ok) {
            cout << g << "\n";
            return 0;
        }
    }
    return 0;
}
