#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    long long max_val = a[0];
    int best_pos = 1; // 1-based index

    for (int i = 1; i < n; i++) {
        if (a[i] > max_val) {
            max_val = a[i];
            best_pos = i + 1;
        }
    }

    cout << max_val << ' ' << best_pos << '\n';
    return 0;
}
