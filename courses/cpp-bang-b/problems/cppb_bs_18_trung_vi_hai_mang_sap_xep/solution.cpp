#include <bits/stdc++.h>
using namespace std;

double findMedianSortedArrays(vector<long long>& a, vector<long long>& b) {
    if (a.size() > b.size()) return findMedianSortedArrays(b, a);

    int n = (int)a.size();
    int m = (int)b.size();
    int low = 0, high = n;

    const long long INF = 2e18;

    while (low <= high) {
        int i = low + (high - low) / 2;
        int j = (n + m + 1) / 2 - i;

        long long maxLeftA = (i == 0) ? -INF : a[i - 1];
        long long minRightA = (i == n) ? INF : a[i];

        long long maxLeftB = (j == 0) ? -INF : b[j - 1];
        long long minRightB = (j == m) ? INF : b[j];

        if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
            if ((n + m) % 2 == 1) {
                return (double)max(maxLeftA, maxLeftB);
            } else {
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2.0;
            }
        } else if (maxLeftA > minRightB) {
            high = i - 1;
        } else {
            low = i + 1;
        }
    }
    return 0.0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];

    double median = findMedianSortedArrays(a, b);
    cout << fixed << setprecision(1) << median << "\n";

    return 0;
}
