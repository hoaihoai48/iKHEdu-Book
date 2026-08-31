#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> prime_count(n + 1, 0);
    for (int i = 2; i <= n; ++i) {
        if (prime_count[i] == 0) { // i là số nguyên tố
            for (int j = i; j <= n; j += i) {
                prime_count[j]++;
            }
        }
    }

    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        if (prime_count[i] == 2) ans++;
    }

    cout << ans << "\n";
    return 0;
}