#include <bits/stdc++.h>
using namespace std;

long long count_pal(long long n) {
    if (n < 0) return 0;
    if (n == 0) return 1;

    string s = to_string(n);
    int len = s.size();
    long long ans = 0;

    // Palindromes có độ dài < len
    for (int l = 1; l < len; ++l) {
        int half = (l + 1) / 2;
        ans += 9 * pow(10, half - 1);
    }

    // Palindromes có độ dài đúng bằng len
    int half = (len + 1) / 2;
    long long first_half = stoll(s.substr(0, half));
    long long min_half = pow(10, half - 1);

    ans += (first_half - min_half);

    string pal = to_string(first_half);
    string second_half = pal.substr(0, len / 2);
    reverse(second_half.begin(), second_half.end());
    pal += second_half;

    if (stoll(pal) <= n) ans++;
    return ans + 1; // gồm số 0
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    cout << count_pal(R) - count_pal(L - 1) << "\n";
    return 0;
}
