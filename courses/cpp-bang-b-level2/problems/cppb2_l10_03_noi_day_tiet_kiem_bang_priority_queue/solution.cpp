#include <bits/stdc++.h>
using namespace std;

struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }
    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    unordered_map<long long, int, custom_hash> freq;
    long long best_val = 0;
    int max_cnt = 0;

    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        freq[x]++;
        if (freq[x] > max_cnt) {
            max_cnt = freq[x];
            best_val = x;
        }
    }

    cout << best_val << " " << max_cnt << "\n";
    return 0;
}
