#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n < 5) {
        cout << 0 << "\n";
        return 0;
    }

    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; 1LL * i * i <= n; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) is_prime[j] = false;
        }
    }

    int count_twin = 0;
    for (int p = 3; p + 2 <= n; p += 2) {
        if (is_prime[p] && is_prime[p + 2]) count_twin++;
    }

    cout << count_twin << "\n";
    return 0;
}