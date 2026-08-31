#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    sort(a.begin(), a.end());
    cout << a[k - 1] << "\n";
    return 0;
}
