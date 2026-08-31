#include <bits/stdc++.h>
using namespace std;
int main() {
    string s;
    if (!(cin >> s)) return 0;
    string t = s;
    reverse(t.begin(), t.end());
    cout << (s == t ? "YES\n" : "NO\n");
    return 0;
}
