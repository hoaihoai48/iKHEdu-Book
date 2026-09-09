#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    char c;
    if (!(cin >> s >> c)) return 0;

    int count_c = 0;
    for (char x : s) {
        if (x == c) {
            count_c++;
        }
    }

    cout << count_c << '\n';
    return 0;
}
