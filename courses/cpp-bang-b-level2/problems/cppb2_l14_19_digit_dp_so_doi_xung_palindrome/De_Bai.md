# Đếm số đối xứng palindrome

## Bối cảnh

Công viên trò chơi in vé số đối xứng đọc xuôi ngược đều giống nhau để du khách giữ làm kỷ niệm sau mỗi lần trải nghiệm tàu lượn siêu tốc. Mỗi đợt phát hành xét một đoạn vé liên tiếp và cần đếm có bao nhiêu vé đối xứng để đặt giấy in nhũ vàng cao cấp. Chương trình quy hoạch động so khớp hai đầu dãy chữ số giúp đếm nhanh cả đoạn dài mà không cần lật từng tấm vé.

## Nhiệm vụ

Cho hai số nguyên $L, R$. Hãy lập trình đếm các số $x$ ($L \le x \le R$) đọc xuôi ngược giống nhau, rồi in ra kết quả.

## Input

- Dòng duy nhất: hai số nguyên $L, R$ ($0 \le L \le R \le 10^{18}$).

## Output

- In ra một dòng duy nhất là số lượng số đối xứng trong đoạn.

## Sample 1

### Input

```text
1 20
```

### Output

```text
10```

### Giải thích

- Các số một chữ số từ $1$ đến $9$ đều đối xứng, tổng chín số.
- Trong các số hai chữ số tới $20$ chỉ có $11$ đọc ngược vẫn là $11$.
- Tổng $9 + 1 = 10$ nên chương trình in ra $10$.

## Ràng buộc

- $0 \le L \le R \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
