#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    cout << result << '\n';
    return 0;
}
