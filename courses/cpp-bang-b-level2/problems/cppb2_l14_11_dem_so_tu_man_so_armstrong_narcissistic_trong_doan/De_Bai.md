# Đếm số Armstrong trong đoạn

## Bối cảnh

Bảo tàng toán học chuẩn bị triển lãm các số Armstrong là những số bằng tổng các lũy thừa bậc n của chính các chữ số của nó, với n là số chữ số, để minh họa vẻ đẹp số học cho học sinh tham quan. Ban tổ chức xét một đoạn số liên tiếp và cần liệt kê đếm có bao nhiêu số Armstrong trong đoạn để in catalogue giới thiệu từng số kèm lời giải thích. Vì số Armstrong rất hiếm nên chương trình tiền tính toàn bộ danh sách tới giới hạn rồi trả lời mỗi đoạn bằng tìm kiếm nhị phân.

## Nhiệm vụ

Cho hai số nguyên $L, R$. Hãy lập trình đếm các số Armstrong $x$ ($L \le x \le R$), tức $x$ bằng tổng lũy thừa bậc $n$ của các chữ số của nó ($n$ là số chữ số), rồi in ra kết quả.

## Input

- Dòng duy nhất: hai số nguyên $L, R$ ($0 \le L \le R \le 10^{18}$).

## Output

- In ra một dòng duy nhất là số lượng số Armstrong trong đoạn.

## Sample 1

### Input

```text
1 500
```

### Output

```text
13```

### Giải thích

- Các số một chữ số $1$ đến $9$ đều là Armstrong (chín số).
- Số $153 = 1^3+5^3+3^3$, $370 = 3^3+7^3+0^3$, $371$ và $407$ cũng thỏa mãn.
- Tổng $9 + 4 = 13$ nên chương trình in ra $13$.

## Ràng buộc

- $0 \le L \le R \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
