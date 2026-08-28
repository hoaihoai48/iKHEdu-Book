# iKHEDU COURSES

> Registry điều hướng các khóa học trong project. Mỗi khóa học có một thư mục riêng và một `README.md` làm trang chủ quản lý.

## Danh sách khóa học

| Mã khóa học | Tên khóa học | Đối tượng | Phạm vi | Trang chủ | Status |
|---|---|---|---|---|---|
| `cpp-bang-b-level1` | iKHEDU C++ Bảng B – Level 1 | Học sinh xây nền tảng C++ và thuật toán | 21 chủ đề Level 1 | [Mở khóa học](cpp-bang-b/README.md) | `draft` |

## Quy ước tổ chức

Mỗi khóa học nên có cấu trúc tối thiểu:

```text
courses/<course-slug>/
├── README.md
├── source/
│   ├── level0/
│   └── level1/
├── lessons/
├── problems/
├── assessments/
└── assets/
```

`README.md` cấp khóa học chỉ làm nhiệm vụ điều hướng, learning path, file map, assessment map và quản lý trạng thái. Nội dung lý thuyết chi tiết phải nằm ở các file canonical tương ứng.

Một lesson package chuẩn giữ chuỗi:

```text
README.md → Ly_Thuyet.md → Bai_Tap.md → code/test
```

Một problem package chuẩn giữ chuỗi:

```text
De_Bai.md → Huong_Dan_Giang_Day.md → solution.cpp → test/
```

Các source nền của project như `IKHEDU_Knowledge_Base.md`, `ikhEdu_foundation_framework_report.md` và roadmap hình vẫn nằm ngoài thư mục khóa học và được giữ read-only.

## Trạng thái

- Registry version: `0.1.0`
- Status: `draft`
- Reviewer: TBD
