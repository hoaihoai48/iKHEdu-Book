#include <bits/stdc++.h>
using namespace std;

// Đếm bộ ba (a, b, c) thỏa mãn bất đẳng thức tam giác: a + b > c
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());
    long long count_triangles = 0;

    for (int k = n - 1; k >= 2; --k) {
        int i = 0, j = k - 1;
        while (i < j) {
            if (a[i] + a[j] > a[k]) {
                count_triangles += (j - i);
                j--;
            } else {
                i++;
            }
        }
    }

    cout << count_triangles << "\n";
    return 0;
}
