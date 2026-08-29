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
    bool found = false;

    while (l < r) {
        long long sum = a[l] + a[r];
        if (sum == s) {
            cout << a[l] << " " << a[r] << "\n";
            found = true;
            break;
        } else if (sum < s) {
            ++l;
        } else {
            --r;
        }
    }

    if (!found) cout << -1 << "\n";
    return 0;
}
