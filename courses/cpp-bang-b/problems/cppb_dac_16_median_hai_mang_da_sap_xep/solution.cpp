#include <bits/stdc++.h>
using namespace std;

long long findKth(const vector<long long> &A, int a_l, const vector<long long> &B, int b_l, int k) {
    if (a_l >= (int)A.size()) return B[b_l + k - 1];
    if (b_l >= (int)B.size()) return A[a_l + k - 1];
    if (k == 1) return min(A[a_l], B[b_l]);

    int a_mid = a_l + k / 2 - 1;
    int b_mid = b_l + k / 2 - 1;

    long long a_val = (a_mid < (int)A.size()) ? A[a_mid] : 2e18;
    long long b_val = (b_mid < (int)B.size()) ? B[b_mid] : 2e18;

    if (a_val <= b_val) {
        return findKth(A, a_l + k / 2, B, b_l, k - k / 2);
    } else {
        return findKth(A, a_l, B, b_l + k / 2, k - k / 2);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int j = 0; j < m; ++j) cin >> b[j];
    int total = n + m;
    int k = (total % 2 == 1) ? (total / 2 + 1) : (total / 2);
    cout << findKth(a, 0, b, 0, k) << "\n";
    return 0;
}
