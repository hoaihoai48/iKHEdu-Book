#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int freq[26] = {};
    for (char c : s) {
        freq[c - 'a']++;
    }

    int best_char_idx = 0;
    for (int i = 1; i < 26; i++) {
        if (freq[i] > freq[best_char_idx]) {
            best_char_idx = i;
        }
    }

    char ans_char = (char)('a' + best_char_idx);
    cout << ans_char << ' ' << freq[best_char_idx] << '\n';
    return 0;
}
