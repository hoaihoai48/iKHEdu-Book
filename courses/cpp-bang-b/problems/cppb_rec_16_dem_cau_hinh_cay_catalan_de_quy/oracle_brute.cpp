#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> c(n + 1, 0);
    c[0] = 1;
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            c[i] += c[j] * c[i - 1 - j];
        }
    }
    cout << c[n] << "\n";
    return 0;
}
