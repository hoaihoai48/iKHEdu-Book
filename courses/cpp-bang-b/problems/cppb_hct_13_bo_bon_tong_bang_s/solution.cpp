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

    for (int i = 0; i < n - 3; ++i) {
        for (int j = i + 1; j < n - 2; ++j) {
            long long target = s - a[i] - a[j];
            int l = j + 1, r = n - 1;
            while (l < r) {
                long long sum = a[l] + a[r];
                if (sum == target) {
                    cout << a[i] << " " << a[j] << " " << a[l] << " " << a[r] << "\n";
                    return 0;
                } else if (sum < target) {
                    ++l;
                } else {
                    --r;
                }
            }
        }
    }

    cout << -1 << "\n";
    return 0;
}
