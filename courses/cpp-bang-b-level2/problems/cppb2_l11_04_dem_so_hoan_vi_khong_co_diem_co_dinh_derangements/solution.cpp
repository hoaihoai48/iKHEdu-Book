#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n == 1) { cout << "0\n"; return 0; }
    if (n == 2) { cout << "1\n"; return 0; }

    vector<long long> D(n + 1);
    D[1] = 0; D[2] = 1;
    for (int i = 3; i <= n; ++i) {
        D[i] = (i - 1) * (D[i - 1] + D[i - 2]) % MOD;
    }

    cout << D[n] << "\n";
    return 0;
}
