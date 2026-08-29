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
    long long count = 0;

    while (l < r) {
        if (a[l] + a[r] <= s) {
            count += (r - l);
            ++l;
        } else {
            --r;
        }
    }

    cout << count << "\n";
    return 0;
}
