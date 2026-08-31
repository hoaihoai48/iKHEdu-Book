#include <bits/stdc++.h>
using namespace std;
int n;
long long S;
vector<long long> a, cur;
bool found = false;
void bkt(int idx, long long sum) {
    if (sum == S) {
        found = true;
        for (int i = 0; i < (int)cur.size(); ++i) cout << cur[i] << (i + 1 == (int)cur.size() ? "" : " ");
        cout << "\n";
        return;
    }
    if (idx >= n || sum > S) return;
    for (int i = idx; i < n; ++i) {
        if (sum + a[i] <= S) {
            cur.push_back(a[i]);
            bkt(i + 1, sum + a[i]);
            cur.pop_back();
        }
    }
}
int main() {
    if (!(cin >> n >> S)) return 0;
    a.resize(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    sort(a.begin(), a.end());
    bkt(0, 0);
    if (!found) cout << -1 << "\n";
    return 0;
}
