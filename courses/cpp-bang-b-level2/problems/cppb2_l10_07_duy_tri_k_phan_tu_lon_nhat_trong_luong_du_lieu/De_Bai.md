# Duy trì k phần tử lớn nhất trong luồng dữ liệu

## Bối cảnh

Ban tổ chức cuộc thi chạy marathon nhận kết quả của từng vận động viên về đích theo thời gian thực, mỗi người có một điểm thành tích khác nhau. Sau mỗi vận động viên vừa về đích, ban tổ chức muốn biết ngay điểm chuẩn tạm thời của tốp $K$ người dẫn đầu, tức điểm thấp nhất trong $K$ người có điểm cao nhất tính đến lúc đó, để cập nhật lên bảng điện tử cho khán giả theo dõi. Nếu số người về đích chưa đủ $K$ thì bảng điện tử hiển thị $-1$.

## Nhiệm vụ

Cho số nguyên $K$ và $N$ số nguyên đến lần lượt theo thời gian. Sau mỗi số vừa đến, xét $K$ số lớn nhất trong các số đã thấy (nếu chưa đủ $K$ số thì đáp án là $-1$), lấy số nhỏ nhất trong $K$ số đó. Hãy lập trình in ra đáp án sau mỗi lần thêm một số.

## Input

- Dòng đầu tiên chứa hai số nguyên $N, K$ ($1 \le K \le N \le 10^5$), là số vận động viên và quy mô tốp đầu.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($1 \le a_i \le 10^9$), là điểm từng người theo thứ tự về đích.

## Output

- In ra $N$ dòng, dòng thứ $i$ là điểm chuẩn của tốp $K$ sau $i$ người đầu tiên ($-1$ nếu chưa đủ người).

## Sample 1

### Input

```text
5 3
1 5 3 7 2
```

### Output

```text
-1
-1
1
3
3
```

### Giải thích

- Sau người đầu ($1$): chưa đủ $3$ người nên đáp án $-1$; sau hai người ($1, 5$) vẫn $-1$.
- Sau ba người ($1, 5, 3$): tốp $3$ gồm $1, 5, 3$, điểm chuẩn là $\min(1, 5, 3) = 1$.
- Sau bốn người ($1, 5, 3, 7$): tốp $3$ gồm $7, 5, 3$, điểm chuẩn là $3$.
- Sau năm người ($1, 5, 3, 7, 2$): tốp $3$ vẫn gồm $7, 5, 3$, điểm chuẩn là $3$.

## Ràng buộc

- $1 \le K \le N \le 10^5$, $1 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
