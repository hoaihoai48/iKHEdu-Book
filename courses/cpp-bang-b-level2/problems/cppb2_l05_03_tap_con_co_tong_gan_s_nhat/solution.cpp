#include <bits/stdc++.h>
using namespace std;

void gen_sums(int idx, int end_idx, long long cur, const vector<long long> &a, vector<long long> &res) {
    if (idx == end_idx) {
        res.push_back(cur);
        return;
    }
    gen_sums(idx + 1, end_idx, cur, a, res);
    gen_sums(idx + 1, end_idx, cur + a[idx], a, res);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long w;
    if (!(cin >> n >> w)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int mid = n / 2;
    vector<long long> sum1, sum2;
    gen_sums(0, mid, 0, a, sum1);
    gen_sums(mid, n, 0, a, sum2);

    sort(sum2.begin(), sum2.end());

    long long max_w = 0;
    for (long long s1 : sum1) {
        if (s1 <= w) {
            auto it = upper_bound(sum2.begin(), sum2.end(), w - s1);
            if (it != sum2.begin()) {
                --it;
                max_w = max(max_w, s1 + *it);
            }
        }
    }

    cout << max_w << "\n";
    return 0;
}
