#include <bits/stdc++.h>
using namespace std;

int n, k;
vector<int> cur;

void backtrack(int step, int start_val) {
    if (step > k) {
        for (int i = 0; i < k; ++i) cout << cur[i] << (i + 1 == k ? "" : " ");
        cout << "\n";
        return;
    }
    for (int val = start_val; val <= n - (k - step); ++val) {
        cur.push_back(val);
        backtrack(step + 1, val + 1);
        cur.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n >> k)) return 0;
    backtrack(1, 1);
    return 0;
}
