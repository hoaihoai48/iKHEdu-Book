#include <bits/stdc++.h>
using namespace std;
int N, Q;
vector<long long> b1, b2;
void add(vector<long long> &b, int i, long long v) { for (; i <= N; i += i & -i) b[i] += v; }
long long sum(const vector<long long> &b, int i) { long long s = 0; for (; i > 0; i -= i & -i) s += b[i]; return s; }
void rangeAdd(int l, int r, long long v) {
    add(b1, l, v); if (r + 1 <= N) add(b1, r + 1, -v);
    add(b2, l, v * (l - 1)); if (r + 1 <= N) add(b2, r + 1, -v * r);
}
__int128 pref(int p) { return (__int128)sum(b1, p) * p - sum(b2, p); }
void printInt(__int128 x) {
    if (x == 0) { cout << 0 << "\n"; return; }
    bool neg = false;
    if (x < 0) { neg = true; x = -x; }
    string s;
    while (x > 0) { s.push_back(char('0' + x % 10)); x /= 10; }
    if (neg) s.push_back('-');
    reverse(s.begin(), s.end());
    cout << s << "\n";
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> N >> Q)) return 0;
    b1.assign(N + 2, 0); b2.assign(N + 2, 0);
    while (Q--) {
        int t; cin >> t;
        if (t == 1) { int l, r; long long v; cin >> l >> r >> v; rangeAdd(l, r, v); }
        else { int l, r; cin >> l >> r; printInt(pref(r) - pref(l - 1)); }
    }
    return 0;
}
