#include <bits/stdc++.h>
using namespace std;

long long powerRec(long long a, long long b, long long m) {
    if (b == 0) return 1 % m;
    long long half = powerRec(a, b / 2, m);
    long long res = (1LL * (half % m) * (half % m)) % m;
    if (b % 2 == 1) res = (1LL * res * (a % m)) % m;
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;
    cout << powerRec(a, b, m) << "\n";
    return 0;
}
