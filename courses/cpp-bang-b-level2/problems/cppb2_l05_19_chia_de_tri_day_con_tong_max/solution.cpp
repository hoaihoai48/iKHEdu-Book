#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    long long max_so_far = a[0], cur_max = a[0];
    for (int i = 1; i < n; ++i) {
        cur_max = max(a[i], cur_max + a[i]);
        max_so_far = max(max_so_far, cur_max);
    }
    cout << max_so_far << "\n";
    return 0;
}
