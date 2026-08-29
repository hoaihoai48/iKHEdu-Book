#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int cnt = 1;
    for (int i = 1; i < n; ++i) {
        if (a[i] != a[i - 1]) ++cnt;
    }

    cout << cnt << "\n";
    return 0;
}
