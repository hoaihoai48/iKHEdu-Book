#include <bits/stdc++.h>
using namespace std;

int n;
string cur = "";

void backtrack(int open_cnt, int close_cnt) {
    if (open_cnt == n && close_cnt == n) {
        cout << cur << "\n";
        return;
    }
    if (open_cnt < n) {
        cur.push_back('(');
        backtrack(open_cnt + 1, close_cnt);
        cur.pop_back();
    }
    if (close_cnt < open_cnt) {
        cur.push_back(')');
        backtrack(open_cnt, close_cnt + 1);
        cur.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    backtrack(0, 0);
    return 0;
}
