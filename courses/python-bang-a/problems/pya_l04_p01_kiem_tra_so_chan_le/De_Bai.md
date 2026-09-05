# Kiểm tra số chẵn lẻ


## Bối cảnh

Trong thuật toán phân nhánh xử lý luồng dữ liệu mạng, các gói tin mang số định danh chẵn và lẻ được chuyển tiếp qua hai kênh truyền tải khác nhau.

## Nhiệm vụ

Cho số tự nhiên $N$. Hãy kiểm tra nếu $N$ là số chẵn in ra `CHAN`, ngược lại in ra `LE`.

## Input

Một số tự nhiên $N$ ($0 \le N \le 10^9$).
## Output

Chuỗi `CHAN` hoặc `LE`.
## Sample 1

### Input
```text
18
```
### Output
```text
CHAN
```
### Giải thích

Số đầu vào là $18$. Vì $18$ chia hết cho $2$ ($18 \% 2 = 0$), nên đây là số chẵn. Kết quả in ra: `CHAN`.

## Sample 2

### Input
```text
7
```
### Output
```text
LE
```
