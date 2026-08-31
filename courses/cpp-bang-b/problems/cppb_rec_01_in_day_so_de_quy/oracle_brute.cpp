#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    if (!(cin >> n)) return 0;
    for (int i = 1; i <= n; ++i) cout << i << " ";
    cout << "\n";
    for (int i = n; i >= 1; --i) cout << i << " ";
    cout << "\n";
    return 0;
}
