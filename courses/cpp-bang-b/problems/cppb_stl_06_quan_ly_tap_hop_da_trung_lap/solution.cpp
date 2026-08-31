#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    multiset<long long> ms;

    while (q--) {
        int type;
        long long x;
        cin >> type >> x;

        if (type == 1) { // Thêm x
            ms.insert(x);
        } else if (type == 2) { // Xóa đúng 1 bản sao của x nếu có
            auto it = ms.find(x);
            if (it != ms.end()) ms.erase(it);
        } else { // Đếm số lượng x
            cout << ms.count(x) << "\n";
        }
    }
    return 0;
}
