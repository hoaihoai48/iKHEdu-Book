import os
import build_lesson01
import build_lesson02
import build_lesson03

BASE_DIR = "/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/problems"
os.makedirs(BASE_DIR, exist_ok=True)

# Override IKH-0110, 0112, 0113, 0114 in Lesson 01 to remove struct/pair
REPLACEMENTS = {
    "IKH-0110": {
        "guide": """# Hướng Dẫn Giảng Dạy: Lưu Vị Trí Ban Đầu
- Sử dụng `vector<vector<long long>> a(n, vector<long long>(2))` lưu `{giá_trị, chỉ_số_gốc}`.
- Sắp xếp tăng dần theo cột 0 (mặc định của `std::sort`).
- Độ phức tạp: $\\mathcal{O}(N \\log N)$.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(2));
    for (int i = 0; i < n; ++i) {
        cin >> a[i][0];
        a[i][1] = i + 1;
    }

    sort(a.begin(), a.end());

    for (int i = 0; i < n; ++i) {
        cout << a[i][0] << " " << a[i][1] << "\\n";
    }
    return 0;
}
"""
    },
    "IKH-0112": {
        "guide": """# Hướng Dẫn Giảng Dạy: Bảng Điểm Học Sinh
- Sử dụng `vector<vector<long long>>` lưu `[id, math, info]`.
- Comparator so sánh 3 cấp độ: tổng điểm giảm dần, điểm tin giảm dần, id tăng dần.
- Độ phức tạp: $\\mathcal{O}(N \\log N)$.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

bool cmp(const vector<long long> &a, const vector<long long> &b) {
    long long total_a = a[1] + a[2];
    long long total_b = b[1] + b[2];
    if (total_a != total_b) return total_a > total_b;
    if (a[2] != b[2]) return a[2] > b[2];
    return a[0] < b[0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(3));
    for (int i = 0; i < n; ++i) {
        cin >> a[i][0] >> a[i][1] >> a[i][2];
    }

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i][0] << " " << a[i][1] << " " << a[i][2] << "\\n";
    }
    return 0;
}
"""
    },
    "IKH-0113": {
        "guide": """# Hướng Dẫn Giảng Dạy: Bảng Xếp Hạng Thể Thao
- Sử dụng `vector<vector<long long>>` lưu `[id, pts, diff, goals]`.
- Sắp xếp 4 tiêu chí rõ ràng, tuân thủ Strict Weak Ordering.
- Độ phức tạp: $\\mathcal{O}(N \\log N)$.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

bool cmp(const vector<long long> &a, const vector<long long> &b) {
    if (a[1] != b[1]) return a[1] > b[1];
    if (a[2] != b[2]) return a[2] > b[2];
    if (a[3] != b[3]) return a[3] > b[3];
    return a[0] < b[0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(4));
    for (int i = 0; i < n; ++i) {
        cin >> a[i][0] >> a[i][1] >> a[i][2] >> a[i][3];
    }

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i][0] << (i == n - 1 ? "" : " ");
    }
    cout << "\\n";
    return 0;
}
"""
    },
    "IKH-0114": {
        "guide": """# Hướng Dẫn Giảng Dạy: Sắp Xếp Đoạn Thẳng Không Giao Lỗi
- Sử dụng `vector<vector<long long>>` lưu `[l, r]`.
- Sử dụng `std::stable_sort` kết hợp Comparator chuẩn `<` và `>`. Tuyệt đối không dùng `<=` khi so sánh hai phần tử bằng nhau.
- Độ phức tạp: $\\mathcal{O}(N \\log N)$.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

bool cmp(const vector<long long> &a, const vector<long long> &b) {
    if (a[0] != b[0]) return a[0] < b[0];
    return a[1] > b[1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(2));
    for (int i = 0; i < n; ++i) {
        cin >> a[i][0] >> a[i][1];
    }

    stable_sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i][0] << " " << a[i][1] << "\\n";
    }
    return 0;
}
"""
    }
}

lessons_data = [
    ("SX", "cppb_sx", build_lesson01.LESSON01_PROBLEMS),
    ("HCT", "cppb_hct", build_lesson02.LESSON02_PROBLEMS),
    ("CST", "cppb_cst", build_lesson03.LESSON03_PROBLEMS),
]

count = 0
for tag, prefix, probs in lessons_data:
    for idx, p in enumerate(probs, 1):
        old_id = p["id"]
        new_id = f"CPPB-{tag}-{idx:02d}"
        
        # strip old prefix from slug (e.g. cpp1_01_xep_hang_diem_danh -> xep_hang_diem_danh)
        old_slug = p["slug"]
        parts = old_slug.split("_")[2:] # drop cpp1, 01
        clean_slug = "_".join(parts)
        new_slug = f"{prefix}_{idx:02d}_{clean_slug}"

        title = p["title"]
        statement = p["statement"]
        guide = REPLACEMENTS.get(old_id, {}).get("guide", p["guide"])
        solution_cpp = REPLACEMENTS.get(old_id, {}).get("solution_cpp", p["solution_cpp"])

        pdir = os.path.join(BASE_DIR, new_slug)
        os.makedirs(pdir, exist_ok=True)

        with open(os.path.join(pdir, "De_Bai.md"), "w", encoding="utf-8") as f:
            f.write(statement)

        with open(os.path.join(pdir, "Huong_Dan_Giang_Day.md"), "w", encoding="utf-8") as f:
            f.write(guide)

        with open(os.path.join(pdir, "solution.cpp"), "w", encoding="utf-8") as f:
            f.write(solution_cpp)

        count += 1
        print(f"[{count:02d}/42] Built: {new_id} ({new_slug}) - {title}")

print(f"\n🎉 Successfully created all {count} problem packages in {BASE_DIR} with new ID format!")
