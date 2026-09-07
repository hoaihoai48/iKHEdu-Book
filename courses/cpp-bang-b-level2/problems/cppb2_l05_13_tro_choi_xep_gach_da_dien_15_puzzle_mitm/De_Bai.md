# Trò chơi xếp gạch đa diện (15-puzzle mitm)

## Bối cảnh
Bé An có chiếc bảng trượt số với $15$ ô số đang xếp lộn xộn và một ô trống. Mỗi bước bé trượt một ô số kề bên vào ô trống.

Bé muốn biết cần ít nhất bao nhiêu bước trượt để đưa bảng về đúng thứ tự từ $1$ tới $15$.

## Nhiệm vụ

Cho trạng thái ban đầu của bảng trượt $3 \times 3$ gồm $9$ số ($0$ là ô trống), trạng thái đích chuẩn là `1 2 3 4 5 6 7 8 0`. Mỗi bước được trượt một ô kề với ô trống vào vị trí của nó. Hãy lập trình tìm số bước trượt ít nhất để đưa bảng về trạng thái đích; in `-1` nếu không thể.

## Input

- Gồm một dòng duy nhất chứa $9$ số nguyên (mỗi số từ $0$ tới $8$, mỗi số xuất hiện đúng một lần) mô tả bảng $3 \times 3$ theo thứ tự từ trái sang phải, từ trên xuống dưới.

## Output

- In ra một dòng duy nhất là số bước trượt ít nhất; in `-1` nếu bảng ban đầu không thể về đích.

## Sample 1
### Input
```text
1 2 3 4 5 6 7 0 8
```
### Output
```text
1
```
### Giải thích

Bảng ban đầu chỉ khác đích ở hai ô cuối hàng $3$: `7 0 8` trong khi đích là `7 8 0`. Trượt ô $8$ sang trái vào ô trống là bảng về đích ngay — đúng $1$ bước, và vì bảng chưa phải đích nên không thể $0$ bước.

## Ràng buộc

- $9$ số là một hoán vị của $0$–$8$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
