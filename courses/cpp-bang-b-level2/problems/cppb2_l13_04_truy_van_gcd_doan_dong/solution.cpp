#include <bits/stdc++.h>
using namespace std;
int mygcd(int x, int y) { while (y) { int t = x % y; x = y; y = t; } return x; }
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, Q;
    if (!(cin >> N >> Q)) return 0;
    vector<int> a(N + 1);
    for (int i = 1; i <= N; i++) cin >> a[i];
    vector<int> lg(N + 1);
    lg[1] = 0;
    for (int i = 2; i <= N; i++) lg[i] = lg[i / 2] + 1;
    int K = lg[N] + 1;
    vector<vector<int>> st(K, vector<int>(N + 1));
    for (int i = 1; i <= N; i++) st[0][i] = a[i];
    for (int k = 1; k < K; k++)
        for (int i = 1; i + (1 << k) - 1 <= N; i++)
            st[k][i] = mygcd(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
    while (Q--) {
        int l, r; cin >> l >> r;
        int k = lg[r - l + 1];
        cout << mygcd(st[k][l], st[k][r - (1 << k) + 1]) << "\n";
    }
    return 0;
}
