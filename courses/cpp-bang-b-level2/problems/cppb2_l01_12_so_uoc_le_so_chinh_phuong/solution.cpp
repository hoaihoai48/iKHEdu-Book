#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long A, B;
    if (!(cin >> A >> B)) return 0;

    long long r = sqrt(B);
    long long l = ceil(sqrt(A));

    long long ans = max(0LL, r - l + 1);
    cout << ans << "\n";
    return 0;
}
