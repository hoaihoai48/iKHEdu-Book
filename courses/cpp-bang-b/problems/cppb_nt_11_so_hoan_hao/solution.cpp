#include <bits/stdc++.h>
using namespace std;

bool isPrime(long long p) {
    if (p < 2) return false;
    for (long long i = 2; i * i <= p; ++i) {
        if (p % i == 0) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    unsigned long long n;
    if (!(cin >> n)) return 0;

    // Theo Euclid-Euler, số hoàn hảo chẵn có dạng 2^(p-1) * (2^p - 1) với 2^p - 1 là số nguyên tố
    vector<unsigned long long> perfect_nums;
    int primes[] = {2, 3, 5, 7, 13, 17, 19, 31};
    for (int p : primes) {
        unsigned long long mersenne = (1ULL << p) - 1;
        if (isPrime(mersenne)) {
            unsigned long long perf = (1ULL << (p - 1)) * mersenne;
            perfect_nums.push_back(perf);
        }
    }

    for (auto v : perfect_nums) {
        if (v == n) {
            cout << "YES\n";
            return 0;
        }
    }
    cout << "NO\n";
    return 0;
}