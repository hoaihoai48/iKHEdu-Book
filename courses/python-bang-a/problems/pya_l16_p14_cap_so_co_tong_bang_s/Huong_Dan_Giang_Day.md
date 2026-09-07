# Hướng Dẫn Giảng Dạy: Cặp số có tổng bằng S
Chuyên đề: **Chiếc Hộp Thần Kỳ list & Thao Tác Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán

- Lưu ý cho thầy cô: phần Bối cảnh trong đề bài viết chung chung về tính tổng, nhưng Nhiệm vụ và lời giải đều làm việc khác là đếm cặp có tổng bằng `S`. Khi dạy, bám theo Nhiệm vụ và lời giải.
- Bản chất của bài này là đếm các cặp vị trí `i < j` sao cho hai số cộng lại bằng `S`.
- Với số mẫu `N = 5`, `S = 10`, dãy `2 4 6 8 3`: các cặp đạt là `(2, 8)` và `(4, 6)` nên đáp án là `2`.
- Quy trình trong lời giải với các biến `line`, `n`, `s`, `a`, `seen`, `cnt`, `x`:
  - Tách dòng đầu thành `n = 5`, `s = 10`; đọc dãy `a = [2, 4, 6, 8, 3]`; đặt `seen` rỗng, `cnt = 0`.
  - Xét `2`: cần `8` chưa thấy nên ghi `2` vào `seen`. Xét `4`: cần `6` chưa thấy nên ghi `4`. Xét `6`: cần `4` đã thấy nên `cnt = 1`. Xét `8`: cần `2` đã thấy nên `cnt = 2`. Xét `3`: cần `7` chưa thấy.
  - In `2`.
- Giá trị biên cụ thể: dãy chỉ có 1 số thì không có cặp nào nên in `0`; đề bài cho các số đôi một khác nhau nên mỗi cặp chỉ bị đếm một lần.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 10 / 2 4 6 8 3)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Tách dòng 1 | `n = 5`, `s = 10` |
| 2 | Đọc dãy `a` | `a = [2, 4, 6, 8, 3]`, `seen = {}`, `cnt = 0` |
| 3 | Xét `x = 2` | cần `8` chưa thấy, ghi `2`, `cnt = 0` |
| 4 | Xét `x = 4` | cần `6` chưa thấy, ghi `4`, `cnt = 0` |
| 5 | Xét `x = 6` | cần `4` đã thấy nên `cnt = 1` |
| 6 | Xét `x = 8` | cần `2` đã thấy nên `cnt = 2` |
| 7 | Xét `x = 3` | cần `7` chưa thấy, `cnt` vẫn `2` |
| 8 | In kết quả | màn hình hiện `2` |

Kết quả cuối cùng khớp với đáp án mẫu: `2`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đếm cả cặp một số với chính nó:
```python
line = input().split()
n, s = int(line[0]), int(line[1])
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(n):
        if a[i] + a[j] == s:
            cnt += 1
print(cnt // 2)
```
Với mẫu trên vẫn ra `2`, nhưng nếu dãy chứa số bằng `s / 2` (ví dụ `5` khi `s = 10`) thì cặp `(5, 5)` bị tính oan. Cách sửa: chỉ xét `j` đứng sau `i`, hoặc ghi nhớ các số đã thấy như lời giải.
- Bẫy 2 — đếm mỗi cặp hai lần:
```python
line = input().split()
n, s = int(line[0]), int(line[1])
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(n):
        if i != j and a[i] + a[j] == s:
            cnt += 1
print(cnt)
```
Với mẫu trên in ra `4` vì `(2, 8)` và `(8, 2)` bị tính riêng. Cách sửa: mỗi cặp chỉ đếm một lần, ví dụ ghi `seen` rồi mới kiểm tra như lời giải.
- Bẫy 3 — so hai vòng lặp với `N = 10^4`:
```python
line = input().split()
n, s = int(line[0]), int(line[1])
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == s:
            cnt += 1
print(cnt)
```
Với mẫu 5 số vẫn ra `2`, nhưng với `N = 10^4` thì hai vòng lặp chạy tới năm chục triệu lượt, quá chậm. Cách sửa: duyệt một lượt kết hợp ghi nhớ `seen` như lời giải.

---

## 4. Lời giải tham khảo

```python
line = input().split()
n, s = int(line[0]), int(line[1])
a = list(map(int, input().split()))
seen = set()
cnt = 0
for x in a:
    if (s - x) in seen:
        cnt += 1
    seen.add(x)
print(cnt)
```
