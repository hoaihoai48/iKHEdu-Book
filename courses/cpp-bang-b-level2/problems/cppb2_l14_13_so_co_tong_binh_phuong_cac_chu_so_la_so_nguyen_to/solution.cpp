#include <bits/stdc++.h>
using namespace std;

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    long long ans = 1;
    for (int i = 1; i <= r; ++i) ans = ans * (n - i + 1) / i;
    return ans;
}

long long count_k_bits(long long n, int k) {
    if (n <= 0) return 0;
    long long count = 0;
    int ones = 0;
    for (int b = 62; b >= 0; --b) {
        if ((n >> b) & 1) {
            count += nCr(b, k - ones);
            ones++;
            if (ones > k) break;
        }
    }
    if (ones == k) count++;
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R; int k;
    if (!(cin >> L >> R >> k)) return 0;

    cout << count_k_bits(R, k) - count_k_bits(L - 1, k) << "\n";
    return 0;
}
