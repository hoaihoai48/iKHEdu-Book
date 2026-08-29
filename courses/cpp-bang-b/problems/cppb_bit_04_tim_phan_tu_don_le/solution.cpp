#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total_elements = 2 * n + 1;
    long long ans = 0;
    for (int i = 0; i < total_elements; ++i) {
        long long x;
        cin >> x;
        ans ^= x;
    }

    cout << ans << "\n";
    return 0;
}
