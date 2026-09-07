# Dãy con tăng dài nhất bằng Segment Tree

## Bối cảnh

Trung tâm tuyển chọn vận động viên năng khiếu lưu hồ sơ chiều cao của N thí sinh theo thứ tự đăng ký để tìm đội hình biểu diễn có chiều cao tăng dần ấn tượng nhất. Huấn luyện viên muốn chọn ra nhiều thí sinh nhất sao cho chiều cao của họ tăng nghiêm ngặt theo đúng thứ tự đã đăng ký, và cần biết con số tối đa này để may đồng phục trình diễn. Cây đoạn trên dãy đã nén tọa độ giúp tính độ dài dãy con tăng dài nhất trong thời gian N log N.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$. Hãy lập trình tính độ dài dãy con tăng nghiêm ngặt dài nhất (không cần liên tiếp), rồi in ra kết quả.

## Input

- Dòng 1: số nguyên $N$ ($1 \le N \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).

## Output

- In ra một dòng duy nhất là độ dài LIS.

## Sample 1

### Input

```text
6
3 1 2 1 5 4
```

### Output

```text
3
```

### Giải thích

- Dãy $3\ 1\ 2\ 1\ 5\ 4$: thử nối các số tăng dần theo thứ tự xuất hiện.
- Dãy con $1, 2, 5$ (vị trí $2, 3, 5$) tăng nghiêm ngặt và không thể thêm số nào khác vào mà vẫn tăng.
- Độ dài lớn nhất là $3$ nên chương trình in ra $3$.

## Ràng buộc

- $1 \le N \le 2 \cdot 10^5$; $|a_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
