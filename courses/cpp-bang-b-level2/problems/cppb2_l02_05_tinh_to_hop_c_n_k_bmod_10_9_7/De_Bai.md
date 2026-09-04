# Tính tổ hợp $c_n^k \bmod (10^9+7)$

## Bối cảnh
Đội văn nghệ của trường có $n$ bạn và cần chọn ra $k$ bạn vào đội hình biểu diễn. Số cách chọn có thể cực lớn nên thầy phụ trách chỉ cần biết phần dư của con số đó khi chia cho $10^9+7$. Vì danh sách đăng ký gửi về liên tục, thầy cần trả lời nhanh cho rất nhiều lượt hỏi khác nhau.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $Q$ truy vấn, mỗi truy vấn gồm hai số nguyên $n, k$. Hãy lập trình tính tổ hợp $C_n^k \bmod (10^9+7)$.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tính Tổ Hợp $C_n^k \bmod (10^9+7)$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
