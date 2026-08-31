#include <bits/stdc++.h>
using namespace std;

const long long P = 1000000007;

long long powerMod(long long a, long long b, long long m) {
    long long ans = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) ans = (ans * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a;
    if (!(cin >> a)) return 0;

    a %= P;
    if (a == 0) {
        cout << 0 << "\n";
        return 0;
    }

    if (powerMod(a, (P - 1) / 2, P) != 1) {
        cout << -1 << "\n";
        return 0;
    }

    long long x = powerMod(a, (P + 1) / 4, P);
    long long x2 = P - x;

    long long min_x = min(x, x2);
    cout << min_x << "\n";
    return 0;
}