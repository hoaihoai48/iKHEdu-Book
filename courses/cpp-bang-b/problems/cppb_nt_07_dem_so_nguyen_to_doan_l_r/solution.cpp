#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
vector<bool> is_prime(MAXN + 1, true);
vector<int> pref(MAXN + 1, 0);

void sieve() {
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; 1LL * i * i <= MAXN; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j <= MAXN; j += i) {
                is_prime[j] = false;
            }
        }
    }
    for (int i = 1; i <= MAXN; ++i) {
        pref[i] = pref[i - 1] + (is_prime[i] ? 1 : 0);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve();

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << pref[r] - pref[l - 1] << "\n";
    }
    return 0;
}