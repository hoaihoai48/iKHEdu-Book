#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
vector<int> phi(MAXN + 1);

void sievePhi() {
    for (int i = 0; i <= MAXN; ++i) phi[i] = i;
    for (int i = 2; i <= MAXN; ++i) {
        if (phi[i] == i) { // i là số nguyên tố
            for (int j = i; j <= MAXN; j += i) {
                phi[j] -= phi[j] / i;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sievePhi();

    int n;
    if (!(cin >> n)) return 0;

    long long sum_phi = 0;
    for (int i = 1; i <= n; ++i) {
        sum_phi += phi[i];
    }

    // Số cặp (x, y) với gcd(x, y) = 1 là 2 * sum(phi(i)) - 1 (do (1,1) tính 1 lần)
    long long ans = 2 * sum_phi - 1;
    cout << ans << "\n";
    return 0;
}