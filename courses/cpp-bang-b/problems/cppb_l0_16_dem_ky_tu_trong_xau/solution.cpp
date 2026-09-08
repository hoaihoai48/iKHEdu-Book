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

    int best = 0;
    for (int i = 1; i < 26; i++) {
        if (freq[i] > freq[best]) best = i;
    }
    cout << (char)('a' + best) << ' ' << freq[best] << '\n';
    return 0;
}
