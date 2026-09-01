#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, p;
    if (!(cin >> s >> p)) return 0;

    if (s.size() < p.size()) {
        cout << "0\n";
        return 0;
    }

    vector<int> freq_p(26, 0), freq_s(26, 0);
    for (char c : p) freq_p[c - 'a']++;

    int k = p.size();
    for (int i = 0; i < k; ++i) freq_s[s[i] - 'a']++;

    int ans = 0;
    if (freq_s == freq_p) ans++;

    for (size_t i = k; i < s.size(); ++i) {
        freq_s[s[i] - 'a']++;
        freq_s[s[i - k] - 'a']--;
        if (freq_s == freq_p) ans++;
    }

    cout << ans << "\n";
    return 0;
}
