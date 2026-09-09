#include <bits/stdc++.h>
using namespace std;

// Hàm kiểm tra xâu đối xứng bằng kỹ thuật hai con trỏ đối xứng
bool isPalindrome(const string& s) {
    int l = 0;
    int r = (int)s.size() - 1;
    while (l < r) {
        if (s[l] != s[r]) {
            return false; // Khác nhau tại vị trí đối xứng
        }
        l++;
        r--;
    }
    return true; // Tất cả các cặp đối xứng đều khớp
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    if (isPalindrome(s)) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}
