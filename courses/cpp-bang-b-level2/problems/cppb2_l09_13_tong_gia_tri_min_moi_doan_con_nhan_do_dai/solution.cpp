#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int k;
    if (!(cin >> s >> k)) return 0;

    string res = "";
    for (char c : s) {
        while (!res.empty() && res.back() > c && k > 0) {
            res.pop_back();
            k--;
        }
        res.push_back(c);
    }

    while (k > 0 && !res.empty()) {
        res.pop_back();
        k--;
    }

    // Xóa số 0 ở đầu
    int start = 0;
    while (start < (int)res.size() && res[start] == '0') start++;
    res = res.substr(start);

    cout << (res.empty() ? "0" : res) << "\n";
    return 0;
}
