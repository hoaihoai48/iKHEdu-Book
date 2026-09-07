# Cắt băng rôn quảng cáo tối ưu bằng 2 deque

## Bối cảnh

Nhà thực vật học ghi lại thứ tự thăm các nút của một cây tìm kiếm nhị phân theo cách duyệt tiền thứ tự (thăm nút rồi mới thăm cây con trái và cây con phải). Về phòng thí nghiệm, trợ lý của ông muốn kiểm tra lại xem dãy số ghi trong sổ có thực sự là một thứ tự duyệt đúng hay không trước khi nhập vào cơ sở dữ liệu mẫu vật.

## Nhiệm vụ

Cho $N$ số nguyên phân biệt là dãy số cần kiểm tra. Hãy lập trình xác định xem dãy này có thể là thứ tự duyệt tiền thứ tự (nút, trái, phải) của một cây tìm kiếm nhị phân nào đó hay không, rồi in ra `YES` nếu đúng và `NO` nếu sai.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là độ dài dãy số.
- Dòng thứ hai chứa $N$ số nguyên phân biệt $a_i$ ($-10^9 \le a_i \le 10^9$), là dãy cần kiểm tra.

## Output

- In ra `YES` nếu là thứ tự duyệt đúng, ngược lại in ra `NO`.

## Sample 1

### Input

```text
5
5 2 1 3 6
```

### Output

```text
YES
```

### Giải thích

- Coi $5$ là gốc của cây: các số nhỏ hơn $5$ thuộc cây con trái, các số lớn hơn thuộc cây con phải.
- Dãy con trái $2, 1, 3$ có gốc $2$, với $1$ nằm trái $2$ và $3$ nằm phải $2$ nhưng vẫn nhỏ hơn $5$ nên hợp lệ.
- Dãy con phải chỉ gồm $6$ lớn hơn $5$ nên hợp lệ, toàn bộ dãy là một thứ tự duyệt đúng, đáp án `YES`.

## Ràng buộc

- $1 \le N \le 10^5$, các $a_i$ phân biệt, $-10^9 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
