#include <bits/stdc++.h>
using namespace std;

// Hàm kiểm tra mảng tăng dần, truyền tham chiếu hằng để tối ưu bộ nhớ
bool isSorted(const vector<int>& a) {
    int n = a.size();
    for (int i = 0; i < n - 1; i++) {
        if (a[i] > a[i + 1]) {
            return false; // Phát hiện cặp nghịch thế, kết luận ngay
        }
    }
    return true; // Tất cả các cặp kề nhau đều thỏa mãn
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    if (isSorted(a)) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}
