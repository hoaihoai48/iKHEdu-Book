#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> vals = a;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    for (int i = 0; i < n; ++i) {
        int rank = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin();
        cout << rank << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
