#include <bits/stdc++.h>
using namespace std;

int n;
int a[10][10];
bool visited[10][10];
vector<string> paths;
string cur = "";

int dx[] = {1, 0, 0, -1};
int dy[] = {0, -1, 1, 0};
char step_char[] = {'D', 'L', 'R', 'U'};

void backtrack(int x, int y) {
    if (x == n - 1 && y == n - 1) {
        paths.push_back(cur);
        return;
    }
    for (int i = 0; i < 4; ++i) {
        int nx = x + dx[i], ny = y + dy[i];
        if (nx >= 0 && nx < n && ny >= 0 && ny < n && a[nx][ny] == 1 && !visited[nx][ny]) {
            visited[nx][ny] = true;
            cur.push_back(step_char[i]);
            backtrack(nx, ny);
            cur.pop_back();
            visited[nx][ny] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) cin >> a[i][j];

    if (a[0][0] == 1) {
        visited[0][0] = true;
        backtrack(0, 0);
    }
    if (paths.empty()) {
        cout << -1 << "\n";
    } else {
        for (const string &s : paths) cout << s << "\n";
    }
    return 0;
}
