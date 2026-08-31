#include <bits/stdc++.h>
using namespace std;
int n;
string cur = "";
void bkt(int o, int c) {
    if (o == n && c == n) { cout << cur << "\n"; return; }
    if (o < n) { cur.push_back('('); bkt(o + 1, c); cur.pop_back(); }
    if (c < o) { cur.push_back(')'); bkt(o, c + 1); cur.pop_back(); }
}
int main() {
    if (!(cin >> n)) return 0;
    bkt(0, 0);
    return 0;
}
