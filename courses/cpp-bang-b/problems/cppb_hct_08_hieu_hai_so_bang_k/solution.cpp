#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int l = 0, r = 1;
    bool found = false;

    while (r < n) {
        if (l == r) {
            ++r;
            continue;
        }
        long long diff = a[r] - a[l];
        if (diff == k) {
            found = true;
            break;
        } else if (diff < k) {
            ++r;
        } else {
            ++l;
        }
    }

    if (found) cout << "YES\n";
    else cout << "NO\n";
    return 0;
}
