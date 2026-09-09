#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int tram = n / 100;
    int chuc = (n / 10) % 10;
    int don_vi = n % 10;

    cout << tram + chuc + don_vi << '\n';
    return 0;
}
