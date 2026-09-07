# Chu kỳ ngắn nhất của xâu ký tự

## Bối cảnh

Nhà máy dệt lập trình cho khung cửi tự động với họa tiết được lặp đi lặp lại từ một mẫu cơ sở ngắn nhất để tiết kiệm bộ nhớ điều khiển của máy thêu công nghiệp. Mỗi mẫu thêu là một xâu ký tự và kỹ thuật viên cần xác định độ dài của khối lặp cơ sở, với điều kiện độ dài xâu chia hết cho độ dài khối và toàn bộ xâu được tạo thành bằng cách lặp khối đó. Mảng tiền tố KMP giúp tìm chu kỳ ngắn nhất trong thời gian tuyến tính.

## Nhiệm vụ

Cho xâu $S$. Hãy lập trình tìm độ dài chu kỳ ngắn nhất $p$ sao cho $|S|$ chia hết cho $p$ và $S$ được tạo thành bằng cách lặp lại khối $p$ ký tự đầu, rồi in ra $p$.

## Input

- Dòng duy nhất: xâu $S$ ($1 \le |S| \le 10^6$).

## Output

- In ra một dòng duy nhất là độ dài chu kỳ ngắn nhất.

## Sample 1

### Input

```text
abcabcabc
```

### Output

```text
3```

### Giải thích

- Xâu $abcabcabc$ dài chín ký tự: thử khối $abc$ dài ba thì lặp ba lần được đúng xâu ban đầu.
- Khối độ dài một ($a$) hay độ dài hai ($ab$) khi lặp đều cho ra xâu khác.
- Chu kỳ ngắn nhất là $3$ nên in ra $3$.

## Ràng buộc

- $1 \le |S| \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
