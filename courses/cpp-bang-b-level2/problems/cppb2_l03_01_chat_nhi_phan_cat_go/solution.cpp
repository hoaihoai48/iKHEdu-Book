#include <bits/stdc++.h>
using namespace std;

bool check(long long h, const vector<long long> &trees, long long m) {
    long long wood = 0;
    for (long long tree : trees) {
        if (tree > h) wood += (tree - h);
    }
    return wood >= m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> trees(n);
    long long high = 0;
    for (int i = 0; i < n; ++i) {
        cin >> trees[i];
        high = max(high, trees[i]);
    }

    long long low = 0, ans = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, trees, m)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
