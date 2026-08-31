#include <bits/stdc++.h>
using namespace std;
int n, k;
vector<int> cur;
void bkt(int step, int start) {
    if (step > k) {
        for (int i = 0; i < k; ++i) cout << cur[i] << (i + 1 == k ? "" : " ");
        cout << "\n";
        return;
    }
    for (int v = start; v <= n; ++v) {
        cur.push_back(v);
        bkt(step + 1, v + 1);
        cur.pop_back();
    }
}
int main() {
    if (!(cin >> n >> k)) return 0;
    bkt(1, 1);
    return 0;
}
