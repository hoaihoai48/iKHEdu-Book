#include <bits/stdc++.h>
using namespace std;

// Giả lập Inversion count qua merge sort
long long merge_count(vector<int> &a, int l, int mid, int r) {
    vector<int> left(a.begin() + l, a.begin() + mid + 1);
    vector<int> right(a.begin() + mid + 1, a.begin() + r + 1);
    int i = 0, j = 0, k = l;
    long long inv = 0;

    while (i < (int)left.size() && j < (int)right.size()) {
        if (left[i] <= right[j]) a[k++] = left[i++];
        else {
            a[k++] = right[j++];
            inv += (left.size() - i);
        }
    }
    while (i < (int)left.size()) a[k++] = left[i++];
    while (j < (int)right.size()) a[k++] = right[j++];
    return inv;
}

long long merge_sort(vector<int> &a, int l, int r) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    return merge_sort(a, l, mid) + merge_sort(a, mid + 1, r) + merge_count(a, l, mid, r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    cout << merge_sort(a, 0, n - 1) << "\n";
    return 0;
}
