#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int l = 0, r = n - 1;
    long long ans = 0;

    while (l < r) {
        long long sum = a[l] + a[r];
        if (sum == s) {
            if (a[l] == a[r]) {
                long long cnt = r - l + 1;
                ans += cnt * (cnt - 1) / 2;
                break;
            } else {
                long long c1 = 1, c2 = 1;
                while (l + 1 < r && a[l + 1] == a[l]) { ++c1; ++l; }
                while (r - 1 > l && a[r - 1] == a[r]) { ++c2; --r; }
                ans += c1 * c2;
                ++l;
                --r;
            }
        } else if (sum < s) {
            ++l;
        } else {
            --r;
        }
    }

    cout << ans << "\n";
    return 0;
}
