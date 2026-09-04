# Nhân modulo hai số cực lớn (nhân ấn độ)

## Bối cảnh
Hai kho hàng điện tử cần đối soát số lượng linh kiện: mỗi bên có một con số cực lớn, và hệ thống chỉ lưu được phần dư của tích hai số đó khi chia cho $m$. Phép nhân trực tiếp sẽ làm tràn bộ nhớ máy quét cũ, nên người ta nhân từng phần rồi cộng dồn phần dư — giống cách nhân đặt cột mà học sinh vẫn làm trên giấy.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $T$ bộ $(a, b, m)$. Hãy lập trình tính $(a \cdot b) \bmod m$ mà không để xảy ra tràn số.

## Input
- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

## Output
- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

## Sample 1
### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Nhân Modulo Hai Số Cực Lớn (Nhân Ấn Độ).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
