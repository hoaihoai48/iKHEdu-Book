#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    // Tiền tố có thể chạy từ -N đến +N, offset = n
    vector<int> first_pos(2 * n + 1, -2);
    first_pos[0 + n] = 0; // P[0] = 0 tại vị trí 0

    int current_sum = 0;
    int max_len = 0;

    for (int i = 1; i <= n; ++i) {
        int x;
        cin >> x;
        current_sum += (x == 1 ? 1 : -1);

        int idx = current_sum + n;
        if (first_pos[idx] != -2) {
            max_len = max(max_len, i - first_pos[idx]);
        } else {
            first_pos[idx] = i;
        }
    }

    cout << max_len << "\n";
    return 0;
}
