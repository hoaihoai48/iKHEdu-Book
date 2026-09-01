#include <bits/stdc++.h>
using namespace std;

long long findKth(const vector<long long> &A, const vector<long long> &B, int k) {
    int n = A.size(), m = B.size();
    if (n > m) return findKth(B, A, k);

    int low = max(0, k - m), high = min(k, n);
    while (low <= high) {
        int midA = low + (high - low) / 2;
        int midB = k - midA;

        long long leftA = (midA > 0) ? A[midA - 1] : -2e18;
        long long rightA = (midA < n) ? A[midA] : 2e18;
        long long leftB = (midB > 0) ? B[midB - 1] : -2e18;
        long long rightB = (midB < m) ? B[midB] : 2e18;

        if (leftA <= rightB && leftB <= rightA) {
            return max(leftA, leftB);
        } else if (leftA > rightB) {
            high = midA - 1;
        } else {
            low = midA + 1;
        }
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];

    cout << findKth(a, b, k) << "\n";
    return 0;
}
