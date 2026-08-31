#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    long long mn = a[0];
    for (long long x : a) mn = min(mn, x);
    cout << mn << "\n";
    return 0;
}
