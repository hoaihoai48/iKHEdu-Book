#include <bits/stdc++.h>
using namespace std;
long long atMost(string s, int k) { int n = s.size(); vector<int> cnt(256, 0); int distinct = 0, l = 0; long long res = 0; for (int r = 0; r < n; ++r) { if (cnt[s[r]]++ == 0) distinct++; while (distinct > k) { if (--cnt[s[l++]] == 0) distinct--; } res += r - l + 1; } return res; }
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); string s; int k; if (!(cin >> s >> k)) return 0; cout << atMost(s, k) - atMost(s, k - 1) << "
"; return 0; }
