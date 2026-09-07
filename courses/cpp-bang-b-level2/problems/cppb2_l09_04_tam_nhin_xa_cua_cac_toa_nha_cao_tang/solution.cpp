#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];
    long long mx = -1;
    int ans = 0;
    for (int i = n - 1; i >= 0; --i) {
        if (h[i] > mx) {
            ++ans;
            mx = h[i];
        }
    }
    cout << ans << "\n";
    return 0;
}
