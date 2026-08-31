#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    int lim = sqrt(n);
    vector<bool> is_prime(lim + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; 1LL * i * i <= lim; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j <= lim; j += i) is_prime[j] = false;
        }
    }

    int count_3div = 0;
    for (int i = 2; i <= lim; ++i) {
        if (is_prime[i] && 1LL * i * i <= n) count_3div++;
    }

    cout << count_3div << "\n";
    return 0;
}