#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    long long x;
    if (!(cin >> n >> x)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    int pos = -1;
    for (int i = 0; i < n; ++i) {
        if (a[i] == x) { pos = i + 1; break; }
    }
    cout << pos << "\n";
    return 0;
}
