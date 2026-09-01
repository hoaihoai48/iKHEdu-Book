#include <bits/stdc++.h>
using namespace std;

// Triển khai cây nhị phân tìm kiếm cân bằng duy trì thứ hạng
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    vector<int> elements;

    while (q--) {
        int type, x;
        cin >> type >> x;
        if (type == 1) {
            // Chèn x
            auto it = lower_bound(elements.begin(), elements.end(), x);
            elements.insert(it, x);
        } else if (type == 2) {
            // Xóa x
            auto it = lower_bound(elements.begin(), elements.end(), x);
            if (it != elements.end() && *it == x) {
                elements.erase(it);
            }
        } else if (type == 3) {
            // Đếm số phần tử nhỏ hơn x (Order of Key)
            int rank_val = lower_bound(elements.begin(), elements.end(), x) - elements.begin();
            cout << rank_val << "\n";
        } else if (type == 4) {
            // Tìm phần tử thứ k (0-indexed)
            if (x >= 0 && x < (int)elements.size()) {
                cout << elements[x] << "\n";
            } else {
                cout << -1 << "\n";
            }
        }
    }
    return 0;
}
