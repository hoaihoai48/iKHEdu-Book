#include <bits/stdc++.h>
using namespace std;

bool isPalindromeRec(const string &s, int l, int r) {
    if (l >= r) return true;
    if (s[l] != s[r]) return false;
    return isPalindromeRec(s, l + 1, r - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    if (isPalindromeRec(s, 0, (int)s.size() - 1)) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
    return 0;
}
