# Trò Chơi Oẳn Tù Tì


## Bối cảnh

Hai bạn Tí và Tèo chơi trò Oẳn Tù Tì. Quy ước các lựa chọn bằng số:
  * `1`: Búa (Đấm)
  * `2`: Kéo
  * `3`: Bao (Lá)
* **Luật chơi:** Búa (1) thắng Kéo (2); Kéo (2) thắng Bao (3); Bao (3) thắng Búa (1). Nếu ra cùng số thì hòa nhau.
## Nhiệm vụ

Nhập vào lựa chọn của Tí và Tèo. Hãy in ra kết quả: `TI THANG`, `TEO THANG` hoặc `HOA`.
## Input

Hai số tự nhiên lần lượt là lựa chọn của Tí và Tèo ($1, 2, 3$).
## Output

`TI THANG`, `TEO THANG` hoặc `HOA`.
## Sample 1

### Input
```text
1
2
```
### Output
```text
TI THANG
```
### Giải thích

Tí ra Búa (1), Tèo ra Kéo (2) $\to$ Tí thắng.
## Sample 2

### Input
```text
1
3
```
### Output
```text
TEO THANG
```
### Giải thích

Tí ra Búa (1), Tèo ra Bao (3) $\to$ Tèo thắng.
## Sample 3

### Input
```text
2
2
```
### Output
```text
HOA
```
### Giải thích

Cả hai cùng ra Kéo.

## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
