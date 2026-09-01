#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    long long xor_sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        xor_sum ^= a[i];
    }

    long long lsb = xor_sum & (-xor_sum);
    long long x = 0, y = 0;

    for (long long val : a) {
        if (val & lsb) x ^= val;
        else y ^= val;
    }

    if (x > y) swap(x, y);
    cout << x << " " << y << "\n";
    return 0;
}
