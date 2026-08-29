#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    bool first = true;
    for (long long sub = n; sub > 0; sub = (sub - 1) & n) {
        if (!first) cout << " ";
        cout << sub;
        first = false;
    }
    cout << "\n";

    return 0;
}
