# Độ dài đối xứng dài nhất (Manacher)

## Bối cảnh

Trạm quan trắc tín hiệu vũ trụ thu được chuỗi ký tự mã hóa từ vệ tinh và nghi ngờ thông điệp quan trọng nằm trong đoạn đối xứng dài nhất của chuỗi thu được. Mỗi ca trực ghi nhận một chuỗi dài tới hàng triệu ký tự nên thuật toán kiểm tra từng tâm một sẽ quá chậm, đội kỹ thuật triển khai Manacher để tìm độ dài lớn nhất trong thời gian tuyến tính. Kết quả giúp ăng ten định hướng lại để thu trọn vẹn thông điệp trong lần quét tiếp theo.

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
3```

### Giải thích

- Xâu $babad$: đoạn $bab$ (vị trí $1$ đến $3$) đối xứng và dài ba ký tự.
- Mọi đoạn dài bốn hoặc năm ký tự đều không đối xứng.
- Độ dài lớn nhất là $3$ nên in ra $3$.

## Ràng buộc

- $1 \le |S| \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
