# Đoạn con ngắn nhất chứa đầy đủ bảng chữ cái

## Bối cảnh

Bạn Hoa chơi trò tìm đoạn văn ngắn nhất chứa đủ mọi chữ cái trong bảng chữ cái. Bạn có một xâu ký tự dài và muốn cắt ra đoạn liên tiếp ngắn nhất mà trong đó mỗi chữ cái đều xuất hiện ít nhất một lần.

Hoa mở rộng khung chọn từng chút một, khi đã đủ chữ cái thì thu hẹp lại để tìm đoạn ngắn nhất.

## Nhiệm vụ

Cho xâu ký tự. Hãy lập trình tìm độ dài đoạn con liên tiếp ngắn nhất chứa đầy đủ mọi chữ cái trong bảng chữ cái.

## Input

- Gồm một dòng duy nhất chứa xâu $s$ (chỉ gồm chữ cái thường, $1 \le |s| \le 10^6$).

## Output

- In ra một dòng duy nhất là độ dài của xâu con liên tiếp ngắn nhất chứa đủ cả $26$ chữ cái `a`–`z`; in `-1` nếu không tồn tại xâu con như vậy.

## Sample 1
### Input
```text
abcdefghijklmnopqrstuvwxyzabc
```
### Output
```text
26
```
### Giải thích

Xâu dài $29$ ký tự, $26$ ký tự đầu đã chứa đủ `a` tới `z` nên đoạn $[0, 25]$ dài $26$ thỏa mãn. Mọi đoạn ngắn hơn $26$ ký tự không thể chứa đủ $26$ chữ cái phân biệt. Vậy đáp án là $26$.

## Ràng buộc

- $1 \le |s| \le 10^6$, chỉ gồm `a`–`z`.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
