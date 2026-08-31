#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0 || k <= 0 || k > n) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    map<int, int> freq;
    for (int i = 0; i < k; ++i) freq[a[i]]++;

    cout << freq.size();

    for (int i = k; i < n; ++i) {
        // Xóa phần tử cũ
        freq[a[i - k]]--;
        if (freq[a[i - k]] == 0) freq.erase(a[i - k]);

        // Thêm phần tử mới
        freq[a[i]]++;

        cout << " " << freq.size();
    }
    cout << "\n";
    return 0;
}
