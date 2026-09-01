#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    vector<int> freq(26, 0);
    for (char c : s) freq[c - 'a']++;

    priority_queue<pair<int, char>> pq;
    for (int i = 0; i < 26; ++i) {
        if (freq[i] > 0) pq.push({freq[i], (char)('a' + i)});
    }

    string res = "";
    pair<int, char> prev = {-1, '#'};

    while (!pq.empty()) {
        auto cur = pq.top(); pq.pop();
        res += cur.second;
        cur.first--;

        if (prev.first > 0) pq.push(prev);
        prev = cur;
    }

    if (res.size() != s.size()) cout << "-1\n";
    else cout << res << "\n";
    return 0;
}
