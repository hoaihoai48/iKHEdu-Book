#include <bits/stdc++.h>
using namespace std;

// Triển khai cây tìm kiếm nhị phân cân bằng thủ công hoặc multiset giả lập PBDS
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    vector<long long> dynamic_arr;

    while (q--) {
        int type; long long x;
        cin >> type >> x;
        if (type == 1) {
            auto it = lower_bound(dynamic_arr.begin(), dynamic_arr.end(), x);
            dynamic_arr.insert(it, x);
        } else {
            auto it = lower_bound(dynamic_arr.begin(), dynamic_arr.end(), x);
            cout << (it - dynamic_arr.begin()) << "\n";
        }
    }
    return 0;
}
