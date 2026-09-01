#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double p;
    if (!(cin >> p)) return 0;

    if (p <= 0.0) {
        cout << "-1\n";
    } else {
        cout << fixed << setprecision(6) << (1.0 / p) << "\n";
    }
    return 0;
}
