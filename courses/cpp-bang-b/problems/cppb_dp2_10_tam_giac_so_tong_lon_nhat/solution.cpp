#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<vector<long long>> a(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= i; ++j) {
            cin >> a[i][j];
        }
    }

    // Quy hoạch động từ đáy tam giác lên đỉnh
    for (int i = n - 2; i >= 0; --i) {
        for (int j = 0; j <= i; ++j) {
            a[i][j] += max(a[i + 1][j], a[i + 1][j + 1]);
        }
    }

    cout << a[0][0] << "\n";
    return 0;
}
