#include <bits/stdc++.h>
using namespace std;

string addBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    string res = "";
    int carry = 0;
    int n = max(a.size(), b.size());
    for (int i = 0; i < n || carry; ++i) {
        int sum = carry;
        if (i < (int)a.size()) sum += a[i] - '0';
        if (i < (int)b.size()) sum += b[i] - '0';
        res.push_back((sum % 10) + '0');
        carry = sum / 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<vector<string>> c(n + 1, vector<string>(k + 1, "0"));
    for (int i = 0; i <= n; ++i) {
        c[i][0] = "1";
        for (int j = 1; j <= min(i, k); ++j) {
            if (j == i) c[i][j] = "1";
            else c[i][j] = addBig(c[i - 1][j - 1], c[i - 1][j]);
        }
    }

    cout << c[n][k] << "\n";
    return 0;
}