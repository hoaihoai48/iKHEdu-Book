# Cái túi chia nhỏ được (fractional knapsack)

## Bối cảnh

Bác nông dân thu hoạch cà phê mang ra chợ bán nhưng chiếc xe thồ của bác chỉ chở được một khối lượng giới hạn. Nhà bác có nhiều bao cà phê với khối lượng và giá trị khác nhau, và bác được phép xúc bớt từng phần của bao ra để xếp vừa xe, miễn là tổng khối lượng không vượt quá sức chở. Bác muốn chọn cách xúc cà phê sao cho tổng giá trị chuyến hàng mang ra chợ là cao nhất, để tiền bán đủ trang trải học phí cho con trong học kỳ mới.

## Nhiệm vụ

Cho sức chở $W$ của xe và $N$ bao cà phê, mỗi bao có giá trị $v_i$ và khối lượng $w_i$ (được phép lấy một phần của bao theo đúng tỉ lệ giá trị). Hãy lập trình chọn khối lượng lấy từ mỗi bao sao cho tổng khối lượng không vượt quá $W$ và tổng giá trị lớn nhất, rồi in ra tổng giá trị đó với $4$ chữ số thập phân.

## Input

- Dòng đầu tiên chứa số nguyên $N$ và số thực $W$ ($1 \le N \le 10^5$, $0 < W \le 10^9$), là số bao và sức chở của xe.
- $N$ dòng tiếp theo, mỗi dòng chứa hai số thực $v_i, w_i$ ($0 < v_i, w_i \le 10^6$), là giá trị và khối lượng của một bao.

## Output

- In ra tổng giá trị lớn nhất với đúng $4$ chữ số sau dấu chấm thập phân.

## Sample 1

### Input

```text
3 50
60 10
100 20
120 30
```

### Output

```text
240.0000
```

### Giải thích

- Tính đơn giá (giá trị trên mỗi đơn vị khối lượng) của ba bao: $60 / 10 = 6$, $100 / 20 = 5$, $120 / 30 = 4$.
- Lấy trọn bao thứ nhất ($10$ khối lượng, được $60$) và bao thứ hai ($20$ khối lượng, được $100$), xe còn chở thêm được $50 - 10 - 20 = 20$.
- Lấy thêm $20$ trên $30$ khối lượng của bao thứ ba, được thêm $20 \times 4 = 80$.
- Tổng giá trị là $60 + 100 + 80 = 240$, in ra $240.0000$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 < W \le 10^9$, $0 < v_i, w_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
