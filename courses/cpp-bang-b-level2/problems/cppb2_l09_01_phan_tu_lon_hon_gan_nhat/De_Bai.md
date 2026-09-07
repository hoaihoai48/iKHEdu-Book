# Phần tử lớn hơn gần nhất (nge)

## Bối cảnh

Trạm quan trắc lũ đặt dọc bờ sông một dãy $N$ cảm biến, cảm biến thứ $i$ ghi lại mực nước $A_i$ vào cùng một thời điểm. Để dự báo dòng chảy, kỹ sư trực ca cần biết với mỗi cảm biến, đâu là cảm biến đầu tiên nằm về phía hạ lưu (bên phải) có mực nước cao hơn hẳn nó. Nếu từ vị trí đó nhìn sang phải mà không còn cảm biến nào cao hơn, hệ thống sẽ ghi nhận $-1$ để đánh dấu vùng nước rút cần theo dõi riêng.

## Nhiệm vụ

Cho dãy $N$ số nguyên $A_1, A_2, \dots, A_N$. Hãy lập trình tìm với mỗi vị trí $i$ giá trị của phần tử đầu tiên bên phải lớn hơn $A_i$ một cách nghiêm ngặt, rồi in $N$ kết quả trên một dòng, mỗi kết quả cách nhau một dấu cách.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số cảm biến.
- Dòng thứ hai chứa $N$ số nguyên $A_i$ ($1 \le A_i \le 10^9$), là mực nước tại mỗi cảm biến.

## Output

- In ra $N$ số nguyên trên một dòng, cách nhau bởi một dấu cách. Số thứ $i$ là giá trị của phần tử đầu tiên bên phải lớn hơn $A_i$; nếu không tồn tại thì ghi $-1$.

## Sample 1

### Input

```text
4
4 5 2 25
```

### Output

```text
5 25 25 -1
```

### Giải thích

- Vị trí $1$ có giá trị $4$: nhìn sang phải, số đầu tiên lớn hơn $4$ là $5$ ở vị trí $2$.
- Vị trí $2$ có giá trị $5$: các số bên phải là $2$ rồi $25$; số $2$ không lớn hơn $5$ nên bỏ qua, số đầu tiên thỏa mãn là $25$ ở vị trí $4$.
- Vị trí $3$ có giá trị $2$: số kề ngay bên phải là $25$ đã lớn hơn $2$ nên đáp án là $25$.
- Vị trí $4$ có giá trị $25$: bên phải không còn cảm biến nào nên đáp án là $-1$.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
