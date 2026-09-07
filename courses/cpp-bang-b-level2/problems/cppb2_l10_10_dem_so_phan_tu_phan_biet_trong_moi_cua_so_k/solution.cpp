#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    unordered_map<long long, int> cnt;
    bool first = true;
    for (int i = 0; i < n; ++i) {
        cnt[a[i]]++;
        if (i >= k) {
            if (--cnt[a[i - k]] == 0) cnt.erase(a[i - k]);
        }
        if (i >= k - 1) {
            if (!first) cout << ' ';
            first = false;
            cout << cnt.size();
        }
    }
    cout << "\n";
    return 0;
}
