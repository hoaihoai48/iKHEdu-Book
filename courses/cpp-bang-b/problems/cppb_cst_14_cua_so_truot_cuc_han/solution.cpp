#include <bits/stdc++.h>
using namespace std;

long long count_at_most(const vector<long long> &x, long long limit) {
    if (limit <= 0) return 0;
    int n = x.size();
    int l = 0;
    long long cur_sum = 0;
    long long count = 0;

    for (int r = 0; r < n; ++r) {
        cur_sum += x[r];
        while (cur_sum > limit) {
            cur_sum -= x[l];
            ++l;
        }
        count += (r - l + 1);
    }
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long a, b;
    if (!(cin >> n >> a >> b)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) cin >> x[i];

    long long ans = count_at_most(x, b) - count_at_most(x, a - 1);
    cout << ans << "\n";
    return 0;
}
