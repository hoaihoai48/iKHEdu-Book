#include <bits/stdc++.h>
using namespace std;

long long count_significant(vector<long long> &a, int l, int mid, int r) {
    int j = mid + 1;
    long long count = 0;
    for (int i = l; i <= mid; ++i) {
        while (j <= r && a[i] > 2LL * a[j]) j++;
        count += (j - (mid + 1));
    }

    vector<long long> temp;
    int i1 = l, i2 = mid + 1;
    while (i1 <= mid && i2 <= r) {
        if (a[i1] <= a[i2]) temp.push_back(a[i1++]);
        else temp.push_back(a[i2++]);
    }
    while (i1 <= mid) temp.push_back(a[i1++]);
    while (i2 <= r) temp.push_back(a[i2++]);
    for (int i = 0; i < (int)temp.size(); ++i) a[l + i] = temp[i];

    return count;
}

long long sort_and_count(vector<long long> &a, int l, int r) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    long long cnt = sort_and_count(a, l, mid);
    cnt += sort_and_count(a, mid + 1, r);
    cnt += count_significant(a, l, mid, r);
    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    cout << sort_and_count(a, 0, n - 1) << "\n";
    return 0;
}
