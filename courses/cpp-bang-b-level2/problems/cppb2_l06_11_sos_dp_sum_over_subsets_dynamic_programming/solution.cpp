#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> f(1 << n);
    for (int i = 0; i < (1 << n); ++i) cin >> f[i];

    vector<long long> sos = f;
    for (int b = 0; b < n; ++b) {
        for (int mask = 0; mask < (1 << n); ++mask) {
            if ((mask >> b) & 1) {
                sos[mask] += sos[mask ^ (1 << b)];
            }
        }
    }

    for (int i = 0; i < (1 << n); ++i) {
        cout << sos[i] << (i + 1 == (1 << n) ? "" : " ");
    }
    cout << "\n";
    return 0;
}
