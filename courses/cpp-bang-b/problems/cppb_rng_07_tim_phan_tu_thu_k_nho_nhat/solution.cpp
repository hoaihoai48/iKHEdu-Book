#include <bits/stdc++.h>
using namespace std;

const int MAX_VAL = 200000;

struct FenwickTree {
    int bit[MAX_VAL + 5];
    FenwickTree() { memset(bit, 0, sizeof(bit)); }

    void update(int x, int val) {
        for (; x <= MAX_VAL; x += x & -x) bit[x] += val;
    }

    int findKth(int k) {
        int idx = 0;
        for (int i = 1 << 18; i > 0; i >>= 1) {
            if (idx + i <= MAX_VAL && bit[idx + i] < k) {
                idx += i;
                k -= bit[idx];
            }
        }
        return idx + 1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    FenwickTree ft;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int x;
            cin >> x;
            ft.update(x, 1);
        } else {
            int k;
            cin >> k;
            cout << ft.findKth(k) << "\n";
        }
    }
    return 0;
}
