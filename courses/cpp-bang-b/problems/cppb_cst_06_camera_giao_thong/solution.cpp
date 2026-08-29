#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int cur_broken = 0;
    for (int i = 0; i < k; ++i) {
        if (a[i] == 0) ++cur_broken;
    }

    int min_broken = cur_broken;
    for (int i = k; i < n; ++i) {
        if (a[i] == 0) ++cur_broken;
        if (a[i - k] == 0) --cur_broken;
        min_broken = min(min_broken, cur_broken);
    }

    cout << min_broken << "\n";
    return 0;
}
