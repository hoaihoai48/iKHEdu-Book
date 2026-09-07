# Khoảng cách dây cáp nhỏ nhất

## Bối cảnh

Trên công trường, đội thi công cần mắc một đường dây cáp nối qua các vị trí cột đã cắm sẵn. Kỹ sư muốn chọn vị trí đặt các điểm nối sao cho đoạn dây ngắn nhất vẫn đủ dài, tránh bị căng quá mức.

Tổ kỹ thuật đo đạc khoảng cách giữa các cột rồi bàn nhau phương án đặt điểm nối hợp lý.

## Nhiệm vụ

Cho $n$ điểm $(x_i, y_i)$ trên mặt phẳng. Một trạm nối dây được đặt tại điểm $(p, 0)$ nằm trên trục hoành. Hãy lập trình tìm vị trí đặt trạm sao cho tổng độ dài dây cáp từ trạm tới mọi điểm là nhỏ nhất.

## Input

- Dòng đầu tiên chứa số nguyên $n$ ($1 \le n \le 10^5$).
- $n$ dòng tiếp theo, mỗi dòng chứa hai số thực $x_i, y_i$ ($|x_i|, |y_i| \le 10^6$) là tọa độ một điểm.

## Output

- In ra một dòng duy nhất là tổng độ dài dây cáp nhỏ nhất, làm tròn tới $6$ chữ số thập phân.

## Sample 1
### Input
```text
2
0 0
4 0
```
### Output
```text
4.000000
```
### Giải thích

Đặt trạm tại $p = 2$: khoảng cách tới $(0, 0)$ là $2$, tới $(4, 0)$ cũng là $2$, tổng bằng $4$. Mọi vị trí $p$ nằm giữa $0$ và $4$ đều cho tổng đúng bằng $4$, còn đặt ngoài đoạn này tổng sẽ lớn hơn (ví dụ $p = 0$ cho tổng $0 + 4 = 4$, $p = -1$ cho tổng $1 + 5 = 6$). Vậy tổng nhỏ nhất là $4$.

## Ràng buộc

- $1 \le n \le 10^5$, $|x_i|, |y_i| \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
