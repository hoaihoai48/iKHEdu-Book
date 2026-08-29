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

    int l = 0, r = n - 1;
    long long best_diff = -1;
    long long ans_l = a[0], ans_r = a[1];

    while (l < r) {
        long long cur_sum = a[l] + a[r];
        long long cur_diff = abs(cur_sum - s);

        if (best_diff == -1 || cur_diff < best_diff || (cur_diff == best_diff && cur_sum < ans_l + ans_r)) {
            best_diff = cur_diff;
            ans_l = a[l];
            ans_r = a[r];
        }

        if (cur_sum == s) break;
        else if (cur_sum < s) ++l;
        else --r;
    }

    cout << ans_l << " " << ans_r << "\n";
    return 0;
}
