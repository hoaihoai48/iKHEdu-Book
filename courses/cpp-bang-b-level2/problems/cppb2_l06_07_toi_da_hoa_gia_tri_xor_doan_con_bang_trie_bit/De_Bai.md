# Tối đa hóa giá trị xor đoạn con bằng Trie BIT

## Bối cảnh

Kỹ sư truyền thông của một đài phát thanh đang kiểm tra chất lượng các tuyến cáp nối tiếp nhau trên cùng một trục đường. Mỗi đoạn cáp được gán một con số đo nhiễu, và mã tín hiệu của một tuyến liên tục gồm nhiều đoạn cáp kề nhau được tính bằng phép XOR tất cả các con số trên tuyến đó. Để chọn ra tuyến cần ưu tiên thay cáp mới, anh cần tìm tuyến liên tục có mã tín hiệu lớn nhất, vì nơi nhiễu cao nhất chính là nơi cần được nâng cấp trước tiên.

## Nhiệm vụ

Cho $N$ số nguyên là chỉ số nhiễu của từng đoạn cáp theo thứ tự. Hãy lập trình tìm đoạn liên tục (gồm ít nhất một phần tử) có giá trị XOR tất cả các phần tử lớn nhất, rồi in ra giá trị lớn nhất đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số đoạn cáp.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($0 \le a_i \le 10^9$), là chỉ số nhiễu của từng đoạn.

## Output

- In ra một số nguyên duy nhất là giá trị XOR lớn nhất trên mọi đoạn liên tục.

## Sample 1

### Input

```text
3
1 2 3
```

### Output

```text
3
```

### Giải thích

- Liệt kê cả $6$ đoạn liên tục cùng giá trị XOR của từng đoạn.
- Ba đoạn một phần tử cho giá trị $1$, $2$, $3$.
- Đoạn $[1, 2]$ cho $1 \oplus 2 = 3$; đoạn $[2, 3]$ cho $2 \oplus 3 = 1$.
- Đoạn $[1, 2, 3]$ cho $1 \oplus 2 \oplus 3 = 0$.
- Giá trị lớn nhất trong sáu số $1, 2, 3, 3, 1, 0$ là $3$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
