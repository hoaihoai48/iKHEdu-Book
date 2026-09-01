#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n % 2 != 0) {
        cout << "0\n";
        return 0;
    }

    vector<long long> f(n + 1, 0), g(n + 1, 0);
    f[0] = 1; g[0] = 0;
    f[1] = 0; g[1] = 1;

    for (int i = 2; i <= n; ++i) {
        f[i] = (f[i - 2] + 2 * g[i - 1]) % MOD;
        g[i] = (f[i - 1] + g[i - 2]) % MOD;
    }

    cout << f[n] << "\n";
    return 0;
}
