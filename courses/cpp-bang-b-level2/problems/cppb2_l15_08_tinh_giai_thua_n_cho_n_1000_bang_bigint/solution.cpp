#include <bits/stdc++.h>
using namespace std;
const int BASE = 1000000000;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    if (!(cin >> N)) return 0;
    vector<int> a(1, 1);
    for (int k = 2; k <= N; k++) {
        long long carry = 0;
        for (size_t i = 0; i < a.size(); i++) {
            long long v = (long long)a[i] * k + carry;
            a[i] = int(v % BASE); carry = v / BASE;
        }
        while (carry) { a.push_back(int(carry % BASE)); carry /= BASE; }
    }
    cout << a.back();
    char buf[16];
    for (int i = (int)a.size() - 2; i >= 0; i--) {
        // print with leading zeros (9 digits)
        long long v = a[i];
        string t;
        for (int z = 0; z < 9; z++) { t.push_back(char('0' + v % 10)); v /= 10; }
        reverse(t.begin(), t.end());
        cout << t;
    }
    cout << "\n";
    (void)buf;
    return 0;
}
