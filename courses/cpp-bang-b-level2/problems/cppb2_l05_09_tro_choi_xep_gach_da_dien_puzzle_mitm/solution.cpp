#include <bits/stdc++.h>
using namespace std;

void gen_signs(int idx, int end_idx, long long cur, const vector<long long> &a, vector<long long> &res) {
    if (idx == end_idx) {
        res.push_back(cur);
        return;
    }
    gen_signs(idx + 1, end_idx, cur + a[idx], a, res);
    gen_signs(idx + 1, end_idx, cur - a[idx], a, res);
    gen_signs(idx + 1, end_idx, cur, a, res);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int mid = n / 2;
    vector<long long> sum1, sum2;
    gen_signs(0, mid, 0, a, sum1);
    gen_signs(mid, n, 0, a, sum2);

    unordered_map<long long, int> freq2;
    for (long long x : sum2) freq2[x]++;

    long long count = 0;
    for (long long s1 : sum1) {
        if (freq2.count(-s1)) count += freq2[-s1];
    }

    cout << count - 1 << "\n"; // trừ tập rỗng
    return 0;
}
