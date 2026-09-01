#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long power_mod(long long a, long long b, long long m = MOD) {
    long long res = 1; a %= m;
    while (b > 0) {
        if (b & 1) res = (res * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a;
    string b_str;
    if (!(cin >> a >> b_str)) return 0;

    long long b_reduced = 0;
    long long phi_m = MOD - 1;
    for (char c : b_str) {
        b_reduced = (b_reduced * 10 + (c - '0')) % phi_m;
    }

    cout << power_mod(a, b_reduced) << "\n";
    return 0;
}
