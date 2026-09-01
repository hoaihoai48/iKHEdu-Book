#include <bits/stdc++.h>
using namespace std;

long long atMostKDistinct(const string& s, int k) {
    if (k <= 0) return 0;
    int n = s.size();
    vector<int> freq(26, 0);
    int distinct_count = 0, l = 0;
    long long ans = 0;

    for (int r = 0; r < n; ++r) {
        if (freq[s[r] - 'a'] == 0) distinct_count++;
        freq[s[r] - 'a']++;

        while (distinct_count > k) {
            freq[s[l] - 'a']--;
            if (freq[s[l] - 'a'] == 0) distinct_count--;
            l++;
        }
        ans += (r - l + 1);
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s; int k;
    if (!(cin >> s >> k)) return 0;

    cout << atMostKDistinct(s, k) - atMostKDistinct(s, k - 1) << "\n";
    return 0;
}
