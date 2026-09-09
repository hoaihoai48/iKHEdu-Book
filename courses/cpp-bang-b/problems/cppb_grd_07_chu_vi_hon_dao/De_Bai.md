# Chu Vi Hòn Đảo (Island Perimeter)

## Bối cảnh
Trên bản đồ dạng lưới $N × M$, có đúng một hòn đảo duy nhất được tạo thành bởi các ô đất liền `'1'` kết nối liên thông (các ô còn lại là nước biển `'0'`). Mỗi ô đất liền là một hình vuông có cạnh dài đúng 1 đơn vị. Chu vi của hòn đảo là tổng độ dài các cạnh của các ô đất liền tiếp xúc trực tiếp với nước biển hoặc tiếp xúc với mép ngoài của bản đồ.

## Nhiệm vụ
Cho bản đồ chứa đúng một hòn đảo. Hãy lập trình tính chu vi của hòn đảo đó.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số `0` hoặc `1` cách nhau bởi khoảng trắng.

## Output
- In ra trên một dòng duy nhất chu vi của hòn đảo.

## Sample 1
### Input
```text
4 4
0100
1110
0100
1100
```
### Output
```text
16
```

### Giải thích
Với một hòn đảo gồm 4 ô đất liền xếp thành hình chữ L:
Tổng số cạnh tiếp xúc với nước biển xung quanh đo được là 16 đơn vị chiều dài. Kết quả in ra là 16.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
