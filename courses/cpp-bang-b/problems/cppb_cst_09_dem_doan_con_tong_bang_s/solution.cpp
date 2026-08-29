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

    int l = 0;
    long long cur_sum = 0;
    long long count = 0;

    for (int r = 0; r < n; ++r) {
        cur_sum += a[r];
        while (cur_sum > s) {
            cur_sum -= a[l];
            ++l;
        }
        if (cur_sum == s) {
            ++count;
        }
    }

    cout << count << "\n";
    return 0;
}
