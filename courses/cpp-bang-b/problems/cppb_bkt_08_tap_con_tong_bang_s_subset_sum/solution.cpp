#include <bits/stdc++.h>
using namespace std;

int n;
long long S;
vector<long long> a;
vector<long long> cur;
bool found = false;

void backtrack(int idx, long long current_sum) {
    if (current_sum == S) {
        found = true;
        for (int i = 0; i < (int)cur.size(); ++i) cout << cur[i] << (i + 1 == (int)cur.size() ? "" : " ");
        cout << "\n";
        return;
    }
    if (idx >= n || current_sum > S) return;

    for (int i = idx; i < n; ++i) {
        if (current_sum + a[i] <= S) {
            cur.push_back(a[i]);
            backtrack(i + 1, current_sum + a[i]);
            cur.pop_back();
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n >> S)) return 0;
    a.resize(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    sort(a.begin(), a.end());
    backtrack(0, 0);
    if (!found) cout << -1 << "\n";
    return 0;
}
