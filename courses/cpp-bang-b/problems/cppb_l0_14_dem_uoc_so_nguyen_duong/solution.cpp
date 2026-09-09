#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int cnt = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            cnt++;
        }
    }

    cout << cnt << '\n';
    return 0;
}
