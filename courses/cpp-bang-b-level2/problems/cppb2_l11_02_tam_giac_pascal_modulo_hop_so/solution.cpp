#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    if (k > n || k < 0) {
        cout << "0\n";
        return 0;
    }

    long long ans = 1;
    for (int i = 0; i < k; ++i) {
        ans = (ans * (n - i)) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
