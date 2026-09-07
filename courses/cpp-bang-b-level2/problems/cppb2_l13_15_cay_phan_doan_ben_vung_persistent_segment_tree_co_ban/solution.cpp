#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, Q;
    if (!(cin >> N >> Q)) return 0;
    vector<long long> a(N + 1), pref(N + 1, 0);
    for (int i = 1; i <= N; i++) { cin >> a[i]; pref[i] = pref[i - 1] + a[i]; }
    while (Q--) {
        int v, l, r; cin >> v >> l >> r;
        cout << pref[r] - pref[l - 1] << "\n";
    }
    return 0;
}
