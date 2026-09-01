#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    unordered_map<int, int> count_map;
    int max_len = 0;
    int l = 0;

    for (int r = 0; r < n; ++r) {
        count_map[a[r]]++;
        while ((int)count_map.size() > k) {
            count_map[a[l]]--;
            if (count_map[a[l]] == 0) count_map.erase(a[l]);
            l++;
        }
        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\n";
    return 0;
}
