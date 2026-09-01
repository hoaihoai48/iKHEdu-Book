#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    vector<int> freq(26, 0);
    int unique_chars = 0;
    int min_len = s.size() + 1;
    int l = 0;

    for (int r = 0; r < (int)s.size(); ++r) {
        if (freq[s[r] - 'a'] == 0) unique_chars++;
        freq[s[r] - 'a']++;

        while (unique_chars == 26) {
            min_len = min(min_len, r - l + 1);
            freq[s[l] - 'a']--;
            if (freq[s[l] - 'a'] == 0) unique_chars--;
            l++;
        }
    }

    cout << (min_len > (int)s.size() ? -1 : min_len) << "\n";
    return 0;
}
