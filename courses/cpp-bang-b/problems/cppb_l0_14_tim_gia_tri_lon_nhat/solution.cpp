#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int mx;
    cin >> mx;
    for (int i = 1; i < n; i++) {
        int x;
        cin >> x;
        mx = max(mx, x);
    }
    cout << mx << '\n';
    return 0;
}
