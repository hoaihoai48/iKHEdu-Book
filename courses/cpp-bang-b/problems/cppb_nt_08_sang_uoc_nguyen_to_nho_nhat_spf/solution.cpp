#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
vector<int> spf(MAXN + 1);

void sieveSPF() {
    for (int i = 1; i <= MAXN; ++i) spf[i] = i;
    for (int i = 2; 1LL * i * i <= MAXN; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXN; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieveSPF();

    int q;
    if (!(cin >> q)) return 0;

    for (int i = 0; i < q; ++i) {
        int n;
        cin >> n;
        cout << spf[n] << (i + 1 == q ? "" : " ");
    }
    cout << "\n";
    return 0;
}