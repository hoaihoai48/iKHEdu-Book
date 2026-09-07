# Cái túi đổi trục trạng thái (value-based knapsack)

## Bối cảnh

Nhà sưu tầm tem có một cuốn album chỉ còn chứa được một khối lượng tem giới hạn và một danh sách dài các con tem quý muốn mua, mỗi con có khối lượng và giá trị sưu tầm khác nhau. Thay vì xét từng mức khối lượng, ông quyết định xét từng mức giá trị: với mỗi mức giá trị, ông tính khối lượng nhẹ nhất cần dùng để đạt được nó, rồi chọn ra bộ tem giá trị cao nhất mà album vẫn chứa vừa.

## Nhiệm vụ

Cho sức chứa $W$ và $N$ con tem, mỗi con có khối lượng $w_i$ và giá trị $v_i$ (mỗi con lấy tối đa một lần). Hãy lập trình chọn các con tem sao cho tổng khối lượng không vượt quá $W$ và tổng giá trị lớn nhất, rồi in ra tổng giá trị đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ và số nguyên $W$ ($1 \le N \le 100$, $1 \le W \le 10^9$), là số con tem và sức chứa của album.
- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $w_i, v_i$ ($1 \le w_i \le 10^9$, $1 \le v_i \le 1000$), là khối lượng và giá trị của một con tem.

## Output

- In ra một số nguyên duy nhất là tổng giá trị lớn nhất.

## Sample 1

### Input

```text
3 50
10 60
20 100
30 120
```

### Output

```text
220
```

### Giải thích

- Album chứa được $50$ đơn vị với ba con tem $(10, 60)$, $(20, 100)$, $(30, 120)$.
- Chọn tem $(20, 100)$ và tem $(30, 120)$: tổng khối lượng $20 + 30 = 50$ vừa khít, tổng giá trị $100 + 120 = 220$.
- Mọi cách chọn khác đều kém hơn: lấy cả ba tem thì vượt sức chứa, lấy một tem thì tối đa $120$, lấy cặp $(10, 60)$ với $(20, 100)$ chỉ được $160$.

## Ràng buộc

- $1 \le N \le 100$, $1 \le W \le 10^9$, $1 \le w_i \le 10^9$, $1 \le v_i \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
