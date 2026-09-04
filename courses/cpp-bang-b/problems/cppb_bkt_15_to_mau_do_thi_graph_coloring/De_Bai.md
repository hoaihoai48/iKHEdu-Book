# Tô Màu Đồ Thị (Graph K-Coloring)

**Phân loại bài toán:** `Challenge`

## Bối cảnh
Trong thiết kế vi mạch tích hợp và phân bổ tần số vô tuyến cho $V$ trạm phát sóng, các trạm có tầm phủ sóng giao thoa với nhau được kết nối bằng một đường biên xung đột (tương ứng với một cạnh trong đồ thị vô hướng $G = (V, E)$). Để ngăn chặn hiện tượng can nhiễu tín hiệu nghiêm trọng, cơ quan quản lý tần số quy định hai trạm phát sóng kề nhau bắt buộc phải sử dụng các kênh tần số (được mã hóa bởi các màu khác nhau) hoàn toàn độc lập.

## Nhiệm vụ
Cho đồ thị vô hướng $G = (V, E)$ gồm $V$ đỉnh và $E$ cạnh, cùng số lượng màu khả dụng $K$. Hãy áp dụng thuật toán Quay lui để kiểm tra xem có thể gán cho mỗi đỉnh của đồ thị một trong $K$ màu sao cho không có bất kỳ hai đỉnh kề nhau nào có cùng màu hay không. Nếu có thể tô màu hợp lệ in ra `YES`, ngược lại in ra `NO`.

## Input
- Dòng 1: Ba số nguyên $V, E, K$ ($1 \le V \le 12, 0 \le E \le \frac{V(V-1)}{2}, 1 \le K \le 4$).
- $E$ dòng tiếp theo: Mỗi dòng gồm hai số nguyên $u, v$ mô tả một cạnh kết nối giữa đỉnh $u$ và đỉnh $v$ ($1 \le u, v \le V$).

## Output
- In ra `YES` nếu có thể tô màu đồ thị thỏa mãn yêu cầu, ngược lại in `NO`.

## Sample 1
### Input
```text
4 5 3
1 2
2 3
3 4
4 1
1 3
```
### Output
```text
YES
```
### Giải thích
Với 4 đỉnh và 5 cạnh xung đột, đồ thị hoàn toàn có thể được tô hợp lệ bằng 3 màu: đỉnh 1 màu 1, đỉnh 2 màu 2, đỉnh 3 màu 3, đỉnh 4 màu 2. Khi đó mọi cặp đỉnh kề nhau đều mang màu sắc khác nhau. Do đó đáp án là `YES`.

## Ràng buộc
- 100% số test có $1 \le V \le 12, 1 \le K \le 4$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
