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

    int groups = 1;
    long long min_val = a[0];

    for (int i = 1; i < n; ++i) {
        if (a[i] - min_val > k) {
            ++groups;
            min_val = a[i];
        }
    }

    cout << groups << "\n";
    return 0;
}
