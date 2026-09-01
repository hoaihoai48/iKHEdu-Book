#include <bits/stdc++.h>
using namespace std;

const int MAXA = 1000000;
int spf[MAXA + 1];

void sieve_spf() {
    for (int i = 1; i <= MAXA; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXA; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXA; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve_spf();

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        int x;
        cin >> x;
        vector<pair<int, int>> factors;
        while (x > 1) {
            int p = spf[x];
            int cnt = 0;
            while (x % p == 0) {
                cnt++;
                x /= p;
            }
            factors.push_back({p, cnt});
        }
        for (int i = 0; i < (int)factors.size(); ++i) {
            cout << factors[i].first << "^" << factors[i].second << (i + 1 == (int)factors.size() ? "" : " * ");
        }
        cout << "\n";
    }
    return 0;
}
