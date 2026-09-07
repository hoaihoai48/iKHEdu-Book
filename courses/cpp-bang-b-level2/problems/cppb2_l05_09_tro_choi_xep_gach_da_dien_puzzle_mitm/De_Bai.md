# Trò chơi xếp gạch đa diện (puzzle mitm)

## Bối cảnh
Em bé có một bộ đồ chơi xếp gạch nhiều mảnh đang ở trạng thái ban đầu lộn xộn. Trên hộp có in hình mẫu hoàn chỉnh mà bé muốn xếp thành.

Bé muốn biết cần ít nhất bao nhiêu bước di chuyển để từ cách xếp ban đầu biến thành hình mẫu.

## Nhiệm vụ
Cho trạng thái ban đầu và trạng thái đích của bàn cờ xếp gạch. Hãy lập trình tìm số bước di chuyển ít nhất để biến trạng thái ban đầu thành trạng thái đích.

## Input

- Dòng đầu tiên chứa $9$ số nguyên (mỗi số từ $0$ tới $8$, mỗi số xuất hiện đúng một lần) mô tả trạng thái ban đầu của bảng $3 \times 3$ theo thứ tự từ trái sang phải, từ trên xuống dưới ($0$ là ô trống).
- Dòng thứ hai chứa $9$ số nguyên với cùng quy ước mô tả trạng thái đích.

## Output

- In ra một dòng duy nhất là số bước di chuyển ít nhất (mỗi bước trượt một ô kề với ô trống vào vị trí của nó) để biến trạng thái ban đầu thành trạng thái đích; in `-1` nếu không thể.

## Sample 1
### Input
```text
1 2 3 4 5 6 7 0 8
1 2 3 4 5 6 7 8 0
```
### Output
```text
1
```
### Giải thích

Hai trạng thái chỉ khác nhau ở hai ô cuối hàng $3$: ban đầu là `7 0 8`, đích là `7 8 0`. Trượt ô $8$ sang trái vào ô trống là bảng về đích ngay — đúng $1$ bước, và vì bảng ban đầu chưa phải đích nên không thể $0$ bước.

## Ràng buộc

- Hai dòng đều là hoán vị của $0$–$8$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
