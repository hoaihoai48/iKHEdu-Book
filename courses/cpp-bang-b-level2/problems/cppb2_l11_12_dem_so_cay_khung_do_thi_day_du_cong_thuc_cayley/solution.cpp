#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long N;
    if (!(cin >> N)) return 0;
    if (N <= 2) { cout << 1 << "\n"; return 0; }
    long long a = N % MOD, e = N - 2, r = 1;
    while (e) { if (e & 1) r = r * a % MOD; a = a * a % MOD; e >>= 1; }
    cout << r << "\n";
    return 0;
}
