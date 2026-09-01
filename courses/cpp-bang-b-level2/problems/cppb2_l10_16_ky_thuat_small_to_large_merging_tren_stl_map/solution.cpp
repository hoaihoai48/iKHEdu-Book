#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    map<string, vector<long long>> records;
    for (int i = 0; i < n; ++i) {
        string key; long long val;
        cin >> key >> val;
        records[key].push_back(val);
    }

    for (auto &pair : records) {
        sort(pair.second.begin(), pair.second.end());
        long long sum = 0;
        for (long long v : pair.second) sum += v;
        cout << pair.first << ": Count=" << pair.second.size() << ", Sum=" << sum << "\n";
    }
    return 0;
}
