#include <bits/stdc++.h>
using namespace std;

int prec(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*') return 2;
    return 0;
}

long long apply_op(long long a, long long b, char op) {
    if (op == '+') return a + b;
    if (op == '-') return a - b;
    return a * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    // insert 0 before unary minus
    string t;
    for (size_t i = 0; i < s.size(); ++i) {
        if (s[i] == '-' && (i == 0 || s[i - 1] == '(' || s[i - 1] == '+' || s[i - 1] == '-' || s[i - 1] == '*'))
            t.push_back('0');
        t.push_back(s[i]);
    }
    vector<long long> vals;
    vector<char> ops;
    auto calc = [&]() {
        long long b = vals.back(); vals.pop_back();
        long long a = vals.back(); vals.pop_back();
        char op = ops.back(); ops.pop_back();
        vals.push_back(apply_op(a, b, op));
    };
    for (size_t i = 0; i < t.size();) {
        if (isdigit(t[i])) {
            long long v = 0;
            while (i < t.size() && isdigit(t[i])) {
                v = v * 10 + (t[i] - '0');
                ++i;
            }
            vals.push_back(v);
        } else if (t[i] == '(') {
            ops.push_back('(');
            ++i;
        } else if (t[i] == ')') {
            while (!ops.empty() && ops.back() != '(') calc();
            ops.pop_back();
            ++i;
        } else {
            while (!ops.empty() && ops.back() != '(' && prec(ops.back()) >= prec(t[i])) calc();
            ops.push_back(t[i]);
            ++i;
        }
    }
    while (!ops.empty()) calc();
    cout << vals.back() << "\n";
    return 0;
}
