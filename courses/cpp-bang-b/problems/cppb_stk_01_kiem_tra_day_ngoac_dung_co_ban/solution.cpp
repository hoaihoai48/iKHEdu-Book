#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int open_cnt = 0;
    for (char c : s) {
        if (c == '(') {
            open_cnt++;
        } else {
            if (open_cnt == 0) {
                cout << "NO\n";
                return 0;
            }
            open_cnt--;
        }
    }

    if (open_cnt == 0) cout << "YES\n";
    else cout << "NO\n";
    return 0;
}
