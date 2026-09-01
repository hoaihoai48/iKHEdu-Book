#include <bits/stdc++.h>
using namespace std;

void gen_xors(int idx, int end_idx, long long cur, const vector<long long> &a, vector<long long> &res) {
    if (idx == end_idx) {
        res.push_back(cur);
        return;
    }
    gen_xors(idx + 1, end_idx, cur, a, res);
    gen_xors(idx + 1, end_idx, cur ^ a[idx], a, res);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int mid = n / 2;
    vector<long long> xor1, xor2;
    gen_xors(0, mid, 0, a, xor1);
    gen_xors(mid, n, 0, a, xor2);

    unordered_map<long long, int> freq2;
    for (long long x : xor2) freq2[x]++;

    long long count = 0;
    for (long long x1 : xor1) {
        long long need = k ^ x1;
        if (freq2.count(need)) count += freq2[need];
    }

    cout << count << "\n";
    return 0;
}
