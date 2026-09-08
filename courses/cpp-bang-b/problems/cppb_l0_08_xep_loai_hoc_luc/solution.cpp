#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double d;
    if (!(cin >> d)) return 0;

    if (d >= 8.0) cout << "Gioi" << '\n';
    else if (d >= 6.5) cout << "Kha" << '\n';
    else if (d >= 5.0) cout << "Trung binh" << '\n';
    else cout << "Yeu" << '\n';
    return 0;
}
