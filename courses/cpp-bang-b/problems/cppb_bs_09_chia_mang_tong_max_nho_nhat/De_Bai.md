# Chia Mảng Thành K Đoạn Có Tổng Max Nhỏ Nhất

## Bối cảnh
Một dự án phần mềm gồm N module công việc với thời gian thực hiện lần lượt là A1, A2, ..., An theo đúng quy trình tuần tự. Dự án được phân chia cho K nhóm lập trình viên độc lập làm việc song song, mỗi nhóm phụ trách một phân đoạn các module liên tiếp nhau. Để cả dự án hoàn thành sớm nhất, người quản lý cần phân chia sao cho thời gian làm việc của nhóm có khối lượng công việc lớn nhất (tổng thời gian lớn nhất) là nhỏ nhất có thể.

## Nhiệm vụ
Cho mảng N số nguyên dương và số nguyên K. Hãy chia mảng thành K đoạn con liên tiếp sao cho tổng lớn nhất trong các đoạn là nhỏ nhất có thể.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra giá trị tổng đoạn con lớn nhất nhỏ nhất có thể.

## Sample 1
### Input
```text
5 2
7 2 5 10 8
```
### Output
```text
18
```
### Giải thích
Chia thành 2 đoạn con: đoạn 1 là [7, 2, 5] có tổng 14; đoạn 2 là [10, 8] có tổng 18. Tổng lớn nhất giữa hai đoạn là 18. Không thể chia cách nào khác để có tổng cực đại nhỏ hơn 18. Vì vậy kết quả là 18.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
