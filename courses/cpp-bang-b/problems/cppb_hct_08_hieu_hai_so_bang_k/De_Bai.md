# Tìm Cặp Có Hiệu Đúng Bằng K

## Bối cảnh
Trên trục đường đua mô tô mạo hiểm, hệ thống radar đo vận tốc ghi nhận N chỉ số tốc độ của các xe tham gia. Để trao giải cho màn rượt đuổi kịch tính nhất, trọng tài cần kiểm tra xem trong cuộc đua có tồn tại hai chiếc xe mà vận tốc của xe chạy sau vượt trội hơn xe chạy trước đúng một lượng chênh lệch chuẩn K hay không.

## Nhiệm vụ
Cho mảng gồm N số nguyên và số nguyên không âm K. Hãy kiểm tra xem có tồn tại cặp chỉ số (i, j) với i != j sao cho A[j] - A[i] = K hay không. Nếu có in ra YES, ngược lại in ra NO.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($2 \le N \le 10^5, 0 \le K \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra `YES` hoặc `NO`.

## Sample 1
### Input
```text
5 3
1 8 5 3 2
```
### Output
```text
YES
```
### Giải thích
Sắp xếp mảng tăng dần: [1, 2, 3, 5, 8] với K = 3. Sử dụng hai con trỏ cùng chiều: cặp số (2, 5) có hiệu 5 - 2 = 3 = K hoặc cặp (5, 8) có hiệu 8 - 5 = 3 = K. Vì tồn tại ít nhất một cặp thỏa mãn nên kết quả in ra là YES.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
