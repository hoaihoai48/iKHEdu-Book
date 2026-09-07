#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> A(n), B(n), C(n), D(n);
    for (int i = 0; i < n; ++i) cin >> A[i];
    for (int i = 0; i < n; ++i) cin >> B[i];
    for (int i = 0; i < n; ++i) cin >> C[i];
    for (int i = 0; i < n; ++i) cin >> D[i];

    vector<long long> ab, cd;
    ab.reserve((size_t)n * n);
    cd.reserve((size_t)n * n);
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) ab.push_back(A[i] + B[j]);
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) cd.push_back(C[i] + D[j]);
    sort(cd.begin(), cd.end());

    long long ans = 0;
    for (long long x : ab) {
        auto r = equal_range(cd.begin(), cd.end(), -x);
        ans += (long long)(r.second - r.first);
    }
    cout << ans << "\n";
    return 0;
}
