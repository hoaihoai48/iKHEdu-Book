# Tối ưu hóa trò chơi nim tổng quát (sprague-grundy BIT)

## Bối cảnh

Hai bạn nhỏ trong xóm chơi trò bốc sỏi với nhiều đống sỏi xếp trên sân. Luật chơi rất đơn giản: hai bạn thay phiên nhau đi, mỗi lượt người chơi chọn một đống bất kỳ rồi bốc đi bao nhiêu viên tùy ý, miễn là ít nhất một viên. Bạn nào bốc viên sỏi cuối cùng trên sân thì thắng cuộc. Trước khi chơi, cả hai đều muốn biết với thế sỏi ban đầu thì người đi trước hay người đi sau nắm chắc phần thắng nếu đôi bên đều đi khôn ngoan nhất.

## Nhiệm vụ

Cho $N$ số nguyên là số viên sỏi trong từng đống. Hai người chơi tối ưu, người đi trước đi trước. Hãy lập trình xác định người thắng cuộc, rồi in ra `FIRST` nếu người đi trước thắng và `SECOND` nếu người đi sau thắng.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số đống sỏi.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($1 \le a_i \le 10^9$), là số viên sỏi trong từng đống.

## Output

- In ra `FIRST` nếu người đi trước thắng, ngược lại in ra `SECOND`.

## Sample 1

### Input

```text
3
1 2 4
```

### Output

```text
FIRST
```

### Giải thích

- Tính giá trị XOR của cả ba đống: $1 \oplus 2 \oplus 4 = 7$, khác $0$.
- Người đi trước bốc $1$ viên từ đống $4$ viên, sân còn ba đống $1, 2, 3$ với $1 \oplus 2 \oplus 3 = 0$.
- Từ thế cân bằng $1, 2, 3$ này, bất kỳ nước bốc nào của người đi sau cũng phá vỡ số $0$, và người đi trước luôn bốc trả lại về thế có XOR bằng $0$.
- Cuối cùng người đi sau hết nước đi trước nên người đi trước bốc viên cuối cùng, đáp án là `FIRST`.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
