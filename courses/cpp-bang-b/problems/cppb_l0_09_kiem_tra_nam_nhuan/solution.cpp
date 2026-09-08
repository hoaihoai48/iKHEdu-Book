#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int y;
    if (!(cin >> y)) return 0;

    if ((y % 4 == 0 && y % 100 != 0) || y % 400 == 0) {
        cout << "YES" << '\n';
    } else {
        cout << "NO" << '\n';
    }
    return 0;
}
