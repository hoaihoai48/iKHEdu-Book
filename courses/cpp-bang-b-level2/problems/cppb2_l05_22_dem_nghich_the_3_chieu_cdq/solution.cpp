#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    long long ans = 0;
    for (int j = 0; j < n; ++j) {
        int left_greater = 0, right_smaller = 0;
        for (int i = 0; i < j; ++i) if (a[i] > a[j]) left_greater++;
        for (int k = j + 1; k < n; ++k) if (a[k] < a[j]) right_smaller++;
        ans += 1LL * left_greater * right_smaller;
    }
    cout << ans << "\n";
    return 0;
}
