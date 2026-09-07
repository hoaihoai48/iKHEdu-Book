# Đếm tam giác tạo bởi N điểm trên mặt phẳng

## Bối cảnh

Đội tuyển học sinh giỏi hình học được phát N điểm đánh dấu trên mặt giấy, trong đó không có ba điểm nào thẳng hàng để đảm bảo mọi bài tập dựng hình đều có lời giải duy nhất. Cô giáo yêu cầu mỗi nhóm liệt kê tất cả các tam giác có ba đỉnh nằm trong số các điểm đã cho rồi nộp lại con số tổng cộng để chấm điểm thi đua. Vì N có thể lên tới hàng chục nghìn nên các nhóm cần một chương trình đếm nhanh thay vì vẽ tay từng hình.

## Nhiệm vụ

Cho số nguyên $N$ là số điểm trên mặt phẳng, không có ba điểm nào thẳng hàng. Hãy lập trình tính số tam giác phân biệt có ba đỉnh lấy từ $N$ điểm đã cho, tức $C(N,3)$, rồi in ra kết quả.

## Input

- Dòng duy nhất: số nguyên $N$ ($3 \le N \le 10^6$).

## Output

- In ra một dòng duy nhất là số tam giác, tức $N(N-1)(N-2)/6$.

## Sample 1

### Input

```text
5
```

### Output

```text
10```

### Giải thích

- Với $N = 5$: mỗi tam giác ứng với một cách chọn $3$ điểm trong $5$ điểm.
- Số cách chọn là $C(5,3) = 10$ (liệt kê tay: bỏ đi hai điểm, có $10$ cặp điểm bị bỏ khác nhau).
- Chương trình in ra $10$.

## Ràng buộc

- $3 \le N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
