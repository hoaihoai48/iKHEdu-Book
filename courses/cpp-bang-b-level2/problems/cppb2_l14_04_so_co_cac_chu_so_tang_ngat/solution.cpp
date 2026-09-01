#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R, k;
    if (!(cin >> L >> R >> k)) return 0;

    cout << (R / k) - ((L - 1) / k) << "\n";
    return 0;
}
