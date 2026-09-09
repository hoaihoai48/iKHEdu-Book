#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int y;
    if (!(cin >> y)) return 0;

    bool is_leap = (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);

    if (is_leap) {
        cout << "NHUAN 29\n";
    } else {
        cout << "KHONG NHUAN 28\n";
    }

    return 0;
}
