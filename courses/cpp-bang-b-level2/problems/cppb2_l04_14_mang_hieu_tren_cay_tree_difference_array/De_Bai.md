# Mảng hiệu trên cây (Tree difference array)

## Bối cảnh

Trường học trồng cây theo sơ đồ hình cây, mỗi phòng học là một nút. Mỗi đợt, nhà trường cộng thêm một lượng sách vào tất cả các phòng trên đường đi giữa hai phòng cho trước, cuối cùng cần biết mỗi phòng có bao nhiêu sách.

Bác thủ thư ghi lại từng đợt điều chuyển rồi tổng hợp số sách của mỗi phòng một lần.

## Nhiệm vụ

Cho cây với $N$ nút và các phép cộng trên đường đi $(u, v)$. Hãy lập trình tính giá trị cuối cùng của mỗi nút sau mọi phép cập nhật.

## Input
- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

## Output
- In ra kết quả trên một dòng.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Mảng Hiệu Trên Cây (Tree Difference Array).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
