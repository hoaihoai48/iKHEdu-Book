#include <bits/stdc++.h>
using namespace std;

int n;
long long target;
vector<long long> a;
bool possible = false;

void backtrack(int idx, long long cur_sum) {
    if (possible) return;
    if (cur_sum == target) {
        possible = true;
        return;
    }
    if (idx >= n || cur_sum > target) return;

    for (int i = idx; i < n; ++i) {
        if (cur_sum + a[i] <= target) {
            backtrack(i + 1, cur_sum + a[i]);
            if (possible) return;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    a.resize(n);
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total += a[i];
    }
    if (total % 2 != 0) {
        cout << "NO\n";
        return 0;
    }
    target = total / 2;
    sort(a.rbegin(), a.rend());
    backtrack(0, 0);
    cout << (possible ? "YES\n" : "NO\n");
    return 0;
}
