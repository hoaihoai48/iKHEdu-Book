# Khoảng thời gian giữa hai thời điểm trong ngày

## Bối cảnh
Bạn Minh bắt đầu học bài lúc $H_1$ giờ $M_1$ phút và kết thúc lúc $H_2$ giờ $M_2$ phút (trong cùng một ngày).

## Nhiệm vụ
Nhập 4 số nguyên $H_1, M_1, H_2, M_2$ trên 1 dòng. In ra khoảng thời gian học tính theo đơn vị phút.

## Input
Một dòng chứa 4 số nguyên ($0 \le H_1 \le H_2 \le 23$, $0 \le M_1, M_2 < 60$, thời điểm 2 không sớm hơn thời điểm 1).

## Output
In ra số phút chênh lệch.

## Sample 1
### Input
```text
8 30 10 15
```
### Output
```text
105
```
### Giải thích
Từ 8h30 đến 10h15 là 1 giờ 45 phút $= 60 + 45 = 105$ phút.

## Ràng buộc
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
