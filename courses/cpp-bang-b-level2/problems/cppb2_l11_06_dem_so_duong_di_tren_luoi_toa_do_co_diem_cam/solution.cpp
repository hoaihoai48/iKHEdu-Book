#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> dp0(n + 1, 0), dp12(n + 1, 0);
    dp0[1] = 1; dp12[1] = 2;

    for (int i = 2; i <= n; ++i) {
        dp0[i] = dp12[i - 1];
        dp12[i] = (2 * dp0[i - 1] + 2 * dp12[i - 1]) % MOD;
    }

    cout << (dp0[n] + dp12[n]) % MOD << "\n";
    return 0;
}
