#include <bits/stdc++.h>
using namespace std;

struct LRUCache {
    int cap;
    list<pair<int, int>> lru_list;
    unordered_map<int, list<pair<int, int>>::iterator> cache_map;

    LRUCache(int capacity) : cap(capacity) {}

    int get(int key) {
        if (!cache_map.count(key)) return -1;
        lru_list.splice(lru_list.begin(), lru_list, cache_map[key]);
        return cache_map[key]->second;
    }

    void put(int key, int value) {
        if (cache_map.count(key)) {
            cache_map[key]->second = value;
            lru_list.splice(lru_list.begin(), lru_list, cache_map[key]);
            return;
        }
        if ((int)lru_list.size() == cap) {
            int old_key = lru_list.back().first;
            lru_list.pop_back();
            cache_map.erase(old_key);
        }
        lru_list.push_front({key, value});
        cache_map[key] = lru_list.begin();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int cap, q;
    if (!(cin >> cap >> q)) return 0;

    LRUCache lru(cap);
    while (q--) {
        string op; cin >> op;
        if (op == "SET") {
            int k, v; cin >> k >> v;
            lru.put(k, v);
        } else {
            int k; cin >> k;
            cout << lru.get(k) << "\n";
        }
    }
    return 0;
}
