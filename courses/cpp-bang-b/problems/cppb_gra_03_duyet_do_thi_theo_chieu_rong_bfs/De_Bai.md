# Duyệt Đồ Thị Theo Chiều Rộng (BFS Traversal)

## Bối cảnh
Một thông điệp cảnh báo khẩn cấp cần được lan truyền qua một mạng xã hội gồm $N$ người dùng và $M$ mối quan hệ bạn bè. Xuất phát từ người dùng $S$, thông điệp sẽ được gửi đồng thời tới tất cả những người bạn trực tiếp của $S$ trước (tầng 1), sau đó mới tiếp tục lan truyền tới bạn của bạn (tầng 2) theo nguyên tắc loang theo chiều rộng (ưu tiên người có số hiệu nhỏ hơn).

## Nhiệm vụ
Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh và đỉnh xuất phát $S$. Hãy lập trình in ra thứ tự các đỉnh nhận được thông điệp theo chiến lược duyệt theo chiều rộng.

## Input
- Dòng 1: Chứa 3 số nguyên $N, M, S$ ($1 \le N \le 10^5, 0 \le M \le 2 × 10^5, 1 \le S \le N$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.

## Output
- In ra trên một dòng thứ tự các đỉnh được ghé thăm, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
4 3 1
1 2
1 3
2 4
```
### Output
```text
1 2 3 4
```

### Giải thích
Với đồ thị có các cạnh (1, 2), (1, 3), (2, 4) xuất phát từ đỉnh 1:

- Tầng 1 (kề trực tiếp với 1): thăm đỉnh 2 và đỉnh 3 theo thứ tự tăng dần.
- Tầng 2: từ đỉnh 2 thăm tiếp đỉnh 4.
Thứ tự ghé thăm là: 1 2 3 4.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
