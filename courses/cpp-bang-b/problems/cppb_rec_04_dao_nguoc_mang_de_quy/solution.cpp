#include <bits/stdc++.h>
using namespace std;

void reverseRec(vector<long long> &a, int l, int r) {
    if (l >= r) return;
    swap(a[l], a[r]);
    reverseRec(a, l + 1, r - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    reverseRec(a, 0, n - 1);
    for (int i = 0; i < n; ++i) cout << a[i] << (i + 1 == n ? "" : " ");
    cout << "\n";
    return 0;
}
