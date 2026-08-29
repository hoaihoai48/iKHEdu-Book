#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q, k;
    if (!(cin >> n >> q >> k)) return 0;

    vector<int> d(n + 2, 0);
    while (q--) {
        int l, r;
        cin >> l >> r;
        d[l]++;
        d[r + 1]--;
    }

    int count_ge_k = 0;
    int current = 0;
    for (int i = 1; i <= n; ++i) {
        current += d[i];
        if (current >= k) {
            count_ge_k++;
        }
    }

    cout << count_ge_k << "\n";
    return 0;
}
