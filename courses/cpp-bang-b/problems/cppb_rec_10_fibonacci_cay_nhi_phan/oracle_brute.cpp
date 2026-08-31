#include <bits/stdc++.h>
using namespace std;
long long cnt = 0;
long long f(int n) {
    cnt++;
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return f(n - 1) + f(n - 2);
}
int main() {
    int n;
    if (!(cin >> n)) return 0;
    long long ans = f(n);
    cout << ans << " " << cnt << "\n";
    return 0;
}
