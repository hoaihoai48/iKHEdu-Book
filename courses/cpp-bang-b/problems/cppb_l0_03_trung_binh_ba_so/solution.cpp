#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double a, b, c;
    if (!(cin >> a >> b >> c)) return 0;

    double avg = (a + b + c) / 3.0;

    cout << fixed << setprecision(2) << avg << '\n';
    return 0;
}
