#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, c;
    if (!(cin >> a >> b >> c)) return 0;

    double avg = 1.0 * (a + b + c) / 3;
    cout << fixed << setprecision(2) << avg << '\n';
    return 0;
}
