# Độ dài đối xứng dài nhất (Manacher)

## Bối cảnh

Đội bảo trì đường ống dẫn khí đốt mã hóa nhật ký áp suất thành chuỗi ký tự và cần phát hiện nhanh đoạn đối xứng dài nhất vì đó là dấu hiệu của chu kỳ vận hành ổn định của toàn tuyến ống. Mỗi ngày hàng triệu ký tự được ghi nhận nên thuật toán thử từng tâm một không thể đáp ứng, đội kỹ thuật triển khai Manacher để quét toàn bộ trong thời gian tuyến tính. Kết quả giúp điều độ viên quyết định có cần dừng tuyến để kiểm tra hay không.

## Nhiệm vụ

Cho xâu $S$. Hãy lập trình tính độ dài của xâu con liên tiếp đối xứng dài nhất của $S$ bằng thuật toán Manacher, rồi in ra kết quả.

## Input

- Dòng duy nhất: xâu $S$ ($1 \le |S| \le 10^6$).

## Output

- In ra một dòng duy nhất là độ dài cần tìm.

## Sample 1

### Input

```text
babad
```

### Output

```text
3
```

### Giải thích

- Xâu $babad$: đoạn $bab$ (vị trí $1$ đến $3$) đối xứng và dài ba ký tự.
- Mọi đoạn dài bốn hoặc năm ký tự đều không đối xứng.
- Độ dài lớn nhất là $3$ nên in ra $3$.

## Ràng buộc

- $1 \le |S| \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
