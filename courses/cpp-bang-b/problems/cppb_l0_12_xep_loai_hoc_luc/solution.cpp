#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double s;
    if (!(cin >> s)) return 0;

    if (s < 0.0 || s > 10.0) {
        cout << "DIEM KHONG HOP LE\n";
    } else if (s >= 8.0) {
        cout << "GIOI\n";
    } else if (s >= 6.5) {
        cout << "KHA\n";
    } else if (s >= 5.0) {
        cout << "TRUNG BINH\n";
    } else {
        cout << "CHUA DAT\n";
    }

    return 0;
}
