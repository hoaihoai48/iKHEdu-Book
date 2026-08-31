#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    if (!(cin >> n)) return 0;
    long long s = 0, p = 1;
    for (int i = 1; i <= n; ++i) { s += i; p *= i; }
    cout << s << " " << p << "\n";
    return 0;
}
