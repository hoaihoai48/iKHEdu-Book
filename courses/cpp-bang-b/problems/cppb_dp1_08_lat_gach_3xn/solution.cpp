#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    if (n % 2 != 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<long long> a(n + 1, 0), b(n + 1, 0);
    a[0] = 1;
    b[0] = 0;
    if (n >= 1) b[1] = 1;

    for (int i = 2; i <= n; ++i) {
        a[i] = (a[i - 2] + 2LL * b[i - 1]) % MOD;
        b[i] = (a[i - 1] + b[i - 2]) % MOD;
    }

    cout << a[n] << "\n";
    return 0;
}
