# Ghép ngày tháng năm định dạng chuẩn

## Bối cảnh
Hệ thống cần nhận 3 số nguyên là Ngày, Tháng, Năm và in ra dạng chuẩn hiển thị trên lịch.

## Nhiệm vụ
Nhập 3 số nguyên $D, M, Y$ trên cùng một dòng. In ra theo định dạng: `D/M/Y`.

## Input
Một dòng chứa 3 số nguyên $D, M, Y$ cách nhau dấu cách ($1 \le D \le 31$, $1 \le M \le 12$, $1900 \le Y \le 2100$).

## Output
In ra dạng `D/M/Y`.

## Sample 1
### Input
```text
4 9 2026
```
### Output
```text
4/9/2026
```
### Giải thích
Tận dụng lệnh `print(d, m, y, sep="/")`.
