#include <bits/stdc++.h>
using namespace std;

long long getMinRec(const vector<long long> &a, int l, int r) {
    if (l == r) return a[l];
    int mid = l + (r - l) / 2;
    return min(getMinRec(a, l, mid), getMinRec(a, mid + 1, r));
}

long long getMaxRec(const vector<long long> &a, int l, int r) {
    if (l == r) return a[l];
    int mid = l + (r - l) / 2;
    return max(getMaxRec(a, l, mid), getMaxRec(a, mid + 1, r));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    cout << getMinRec(a, 0, n - 1) << " " << getMaxRec(a, 0, n - 1) << "\n";
    return 0;
}
