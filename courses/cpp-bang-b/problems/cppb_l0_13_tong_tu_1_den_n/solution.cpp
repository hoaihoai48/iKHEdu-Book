#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    long long sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }

    cout << sum << '\n';
    return 0;
}
