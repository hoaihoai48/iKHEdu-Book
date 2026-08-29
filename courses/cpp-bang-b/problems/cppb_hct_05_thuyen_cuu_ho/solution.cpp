#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long c;
    if (!(cin >> n >> c)) return 0;

    vector<long long> w(n);
    for (int i = 0; i < n; ++i) cin >> w[i];

    sort(w.begin(), w.end());

    int l = 0, r = n - 1;
    int boats = 0;

    while (l <= r) {
        if (l == r) {
            ++boats;
            break;
        }
        if (w[l] + w[r] <= c) {
            ++l;
            --r;
        } else {
            --r;
        }
        ++boats;
    }

    cout << boats << "\n";
    return 0;
}
