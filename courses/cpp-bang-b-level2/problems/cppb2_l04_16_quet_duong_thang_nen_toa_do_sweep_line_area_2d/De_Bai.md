# Quét đường thẳng nén tọa độ (sweep-line area 2d)

## Bối cảnh

Phường vẽ bản đồ các khu đất hình chữ nhật để tính tiền sử dụng đất. Cán bộ địa chính cần tính tổng diện tích bị phủ bởi ít nhất một khu đất, vì phần chồng lấn chỉ tính một lần.

Anh cán bộ kẻ các đường thẳng đứng qua mọi cạnh khu đất rồi tính diện tích từng dải một.

## Nhiệm vụ

Cho danh sách các hình chữ nhật trên mặt phẳng. Hãy lập trình tính tổng diện tích hợp bị phủ bởi ít nhất một hình chữ nhật.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Quét Đường Thẳng Nén Tọa Độ (Sweep-line Area 2D).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
