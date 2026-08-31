#include <bits/stdc++.h>
using namespace std;

vector<string> results;

void genRec(int n, string &cur, char last_char) {
    if ((int)cur.size() == n) {
        results.push_back(cur);
        return;
    }
    // Luôn có thể thêm '0'
    cur.push_back('0');
    genRec(n, cur, '0');
    cur.pop_back();

    // Chỉ thêm '1' nếu ký tự trước không phải '1'
    if (last_char != '1') {
        cur.push_back('1');
        genRec(n, cur, '1');
        cur.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    string cur = "";
    genRec(n, cur, '0');
    cout << results.size() << "\n";
    for (const string &s : results) cout << s << "\n";
    return 0;
}
