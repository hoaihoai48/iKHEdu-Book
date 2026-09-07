# Xóa k chữ số để được số nhỏ nhất

## Bối cảnh

Bạn An viết số báo danh dự thi của mình lên bảng nhưng viết thừa ra vài chữ số, và giám thị yêu cầu xóa bớt đúng $K$ chữ số (giữ nguyên thứ tự các chữ còn lại) để được số nhỏ nhất có thể mà vẫn giữ nguyên ý nghĩa dự thi. Số mới không được có chữ số $0$ ở đầu trừ khi bản thân số đó bằng $0$, vì số báo danh in thừa số $0$ đầu sẽ bị máy chấm hiểu nhầm.

## Nhiệm vụ

Cho một chuỗi chữ số $s$ và số nguyên $K$. Được xóa đúng $K$ chữ số (giữ nguyên thứ tự còn lại) rồi loại bỏ các số $0$ ở đầu (nếu còn lại toàn số $0$ thì kết quả là `0`). Hãy lập trình tìm số nhỏ nhất có thể tạo được, rồi in ra số đó.

## Input

- Dòng đầu tiên chứa chuỗi $s$ ($1 \le |s| \le 10^5$) gồm các chữ số và số nguyên $K$ ($0 \le K < |s|$).

## Output

- In ra chuỗi chữ số nhỏ nhất (không có số $0$ ở đầu, trừ số `0`).

## Sample 1

### Input

```text
1432219 3
```

### Output

```text
1219
```

### Giải thích

- Đọc chữ `1` giữ lại được `1`; đọc chữ `4` giữ lại được `14`.
- Đọc chữ `3`: chữ `4` đứng trước lớn hơn nên xóa `4` (còn $2$ lượt), giữ lại được `13`.
- Đọc chữ `2`: chữ `3` đứng trước lớn hơn nên xóa `3` (còn $1$ lượt), giữ lại được `12`.
- Đọc chữ `2` giữ lại được `122`; đọc chữ `1`: chữ `2` đứng trước lớn hơn nên xóa một chữ `2` (hết lượt), giữ lại được `121`.
- Đọc chữ `9` giữ lại, kết quả cuối cùng là `1219` và đã dùng hết $3$ lượt xóa.

## Ràng buộc

- $1 \le |s| \le 10^5$, $0 \le K < |s|$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
