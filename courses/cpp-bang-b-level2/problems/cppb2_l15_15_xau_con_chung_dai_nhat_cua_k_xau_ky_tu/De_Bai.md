# Xâu con chung dài nhất của K xâu

## Bối cảnh

Trung tâm an ninh mạng so sánh K mẫu mã độc thu thập từ các máy chủ bị tấn công để tìm đoạn mã chung dài nhất xuất hiện trong mọi mẫu, từ đó viết chữ ký nhận diện cho tường lửa toàn hệ thống. Mỗi mẫu có thể dài tới hàng trăm nghìn ký tự nên việc so sánh từng cặp đoạn trích là bất khả thi. Thuật toán hậu tố chung kết hợp quy hoạch động giúp khoanh vùng đoạn mã độc đặc trưng trong thời gian chấp nhận được.

## Nhiệm vụ

Cho $K$ xâu ký tự. Hãy lập trình tìm độ dài của xâu con liên tiếp dài nhất xuất hiện trong tất cả $K$ xâu, rồi in ra kết quả.

## Input

- Dòng 1: số nguyên $K$ ($2 \le K \le 10$).
- $K$ dòng tiếp theo, mỗi dòng là một xâu chữ cái thường (tổng độ dài tới $2 \cdot 10^5$).

## Output

- In ra một dòng duy nhất là độ dài cần tìm ($0$ nếu không có).

## Sample 1

### Input

```text
2
ababa
baba
```

### Output

```text
4```

### Giải thích

- Hai xâu $ababa$ và $baba$: đoạn $baba$ xuất hiện ở cuối xâu thứ nhất và chiếm toàn bộ xâu thứ hai.
- Không có đoạn chung nào dài năm ký tự vì xâu thứ hai chỉ dài bốn.
- Độ dài lớn nhất là $4$ nên in ra $4$.

## Ràng buộc

- $2 \le K \le 10$; tổng độ dài tới $2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
