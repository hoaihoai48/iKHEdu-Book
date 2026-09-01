#include <bits/stdc++.h>
using namespace std;

// Cài đặt LRU Cache bằng list + unordered_map O(1)
class LRUCache {
    int capacity;
    list<pair<int, int>> cache_list;
    unordered_map<int, list<pair<int, int>>::iterator> map_lookup;

public:
    LRUCache(int cap) : capacity(cap) {}

    int get(int key) {
        if (map_lookup.find(key) == map_lookup.end()) return -1;
        cache_list.splice(cache_list.begin(), cache_list, map_lookup[key]);
        return map_lookup[key]->second;
    }

    void put(int key, int value) {
        if (map_lookup.find(key) != map_lookup.end()) {
            map_lookup[key]->second = value;
            cache_list.splice(cache_list.begin(), cache_list, map_lookup[key]);
            return;
        }
        if ((int)cache_list.size() == capacity) {
            int old_key = cache_list.back().first;
            cache_list.pop_back();
            map_lookup.erase(old_key);
        }
        cache_list.emplace_front(key, value);
        map_lookup[key] = cache_list.begin();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int cap, q;
    if (!(cin >> cap >> q)) return 0;

    LRUCache lru(cap);
    while (q--) {
        string cmd;
        cin >> cmd;
        if (cmd == "SET") {
            int k, v;
            cin >> k >> v;
            lru.put(k, v);
        } else if (cmd == "GET") {
            int k;
            cin >> k;
            cout << lru.get(k) << "\n";
        }
    }
    return 0;
}
