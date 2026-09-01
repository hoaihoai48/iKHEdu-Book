#include <bits/stdc++.h>
using namespace std;

long long mul_mod(long long a, long long b, long long m) {
    return (long long)((__int128_t)a * b % m);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long a, b, m;
        cin >> a >> b >> m;
        cout << mul_mod(a, b, m) << "\n";
    }
    return 0;
}
