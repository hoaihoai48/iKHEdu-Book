#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> inc(n, 1), dec(n, 1);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (a[j] < a[i]) inc[i] = max(inc[i], inc[j] + 1);
        }
    }

    for (int i = n - 1; i >= 0; --i) {
        for (int j = n - 1; j > i; --j) {
            if (a[j] < a[i]) dec[i] = max(dec[i], dec[j] + 1);
        }
    }

    int max_len = 0;
    for (int i = 0; i < n; ++i) {
        max_len = max(max_len, inc[i] + dec[i] - 1);
    }

    cout << max_len << "\n";
    return 0;
}
