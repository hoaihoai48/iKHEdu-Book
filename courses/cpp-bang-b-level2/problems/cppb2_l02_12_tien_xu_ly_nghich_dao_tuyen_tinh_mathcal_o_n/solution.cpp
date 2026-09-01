#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
const long long MOD = 1000000007;

long long inv[MAXN + 1];

void precompute_inverses() {
    inv[1] = 1;
    for (int i = 2; i <= MAXN; ++i) {
        inv[i] = MOD - (MOD / i) * inv[MOD % i] % MOD;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute_inverses();

    int n;
    if (!(cin >> n)) return 0;
    for (int i = 1; i <= min(n, 20); ++i) {
        cout << inv[i] << (i == min(n, 20) ? "" : " ");
    }
    cout << "\n";
    return 0;
}
