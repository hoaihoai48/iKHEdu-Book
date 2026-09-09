#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    long long perimeter = 2 * (a + b);
    long long area = a * b;

    cout << perimeter << ' ' << area << '\n';
    return 0;
}
