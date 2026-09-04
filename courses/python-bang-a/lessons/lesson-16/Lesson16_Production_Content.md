# Bài 16: Đề thi thử Tin học trẻ Bảng A

Mỗi đề thi chuẩn gồm 4 bài toán phân bổ theo thời gian 90 phút:

## ĐỀ THI THỬ SỐ 01 (MÔ PHỎNG ĐỀ THT THÀNH PHỐ)

### Bài 1 (30 điểm): Mua dụng cụ học tập
- **Yêu cầu:** Mua $N$ quyển vở giá $P$ đồng/quyển. Mua từ 10 quyển trở lên giảm $10\%$. Tính số tiền phải trả (số nguyên).
- **Code mẫu:**
  ```python
  n, p = map(int, input().split())
  tong = n * p
  if n >= 10:
      tong = int(tong * 0.9)
  print(tong)
  ```

### Bài 2 (30 điểm): Số lộc phát đối xứng
- **Yêu cầu:** Số lộc phát đối xứng là số đối xứng và chỉ chứa các chữ số 6 hoặc 8. Kiểm tra số $N$.
- **Code mẫu:**
  ```python
  s = input()
  if s == s[::-1] and all(c in '68' for c in s):
      print("YES")
  else:
      print("NO")
  ```

### Bài 3 (25 điểm): Đếm từ độc nhất trong văn bản
- **Yêu cầu:** Cho câu văn. Đếm xem có bao nhiêu từ khác nhau xuất hiện (không phân biệt hoa thường).
- **Code mẫu:**
  ```python
  s = input().lower()
  tu = s.split()
  print(len(set(tu)))
  ```

### Bài 4 (15 điểm - Phân loại): Bước nhảy chú cào cào
- **Yêu cầu:** Chú cào cào xuất phát từ 0 nhảy đến vị trí $X$. Mỗi bước nhảy xa tối đa $K$ mét. Hỏi số bước nhảy ít nhất?
- **Code mẫu:**
  ```python
  x, k = map(int, input().split())
  ans = (x + k - 1) // k
  print(ans)
  ```
