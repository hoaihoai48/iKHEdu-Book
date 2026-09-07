# Xâu con đối xứng dài nhất

## Bối cảnh

Công ty thiết kế quà tặng khắc tên lên vòng tay sao cho đoạn ký tự đối xứng dài nhất trong tên khách hàng được mạ vàng nổi bật để tạo điểm nhấn cá nhân hóa. Mỗi đơn hàng gửi một cái tên và xưởng cần xác định ngay đoạn đối xứng dài nhất, ưu tiên đoạn xuất hiện sớm nhất khi có nhiều đoạn cùng độ dài, để lập trình cho máy khắc laser. Thuật toán Manacher tìm đáp án trong thời gian tuyến tính kể cả với tên rất dài.

## Nhiệm vụ

Cho xâu $S$. Hãy lập trình tìm xâu con liên tiếp đối xứng dài nhất của $S$ (nếu nhiều đáp án thì lấy vị trí bắt đầu nhỏ nhất), rồi in ra xâu đó.

## Input

- Dòng duy nhất: xâu $S$ gồm chữ cái thường ($1 \le |S| \le 10^6$).

## Output

- In ra một dòng duy nhất là xâu con đối xứng dài nhất (sớm nhất).

## Sample 1

### Input

```text
babad
```

### Output

```text
bab```

### Giải thích

- Xâu $babad$: kiểm tra các xâu con dài ba ký tự thấy $bab$ (vị trí $1$ đến $3$) đối xứng.
- Không có xâu con nào dài bốn hoặc năm ký tự đối xứng (cả $baba$ lẫn $abad$ đều không đọc ngược giống xuôi).
- Đáp án sớm nhất độ dài ba là $bab$ nên in ra $bab$.

## Ràng buộc

- $1 \le |S| \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
