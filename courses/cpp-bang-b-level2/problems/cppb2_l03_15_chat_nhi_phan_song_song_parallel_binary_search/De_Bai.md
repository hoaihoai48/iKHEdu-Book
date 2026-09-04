# Chặt nhị phân song song (parallel binary search)

## Bối cảnh

Trạm khí tượng có nhiều cảm biến gửi số liệu về theo từng đợt. Kỹ sư trực cần trả lời cùng lúc nhiều câu hỏi dạng: với ngưỡng cho trước, đợt đo thứ mấy thì số liệu tích lũy mới vượt ngưỡng.

Thay vì trả lời từng câu hỏi một, anh kỹ sư xử lý tất cả các câu hỏi song song theo từng đợt số liệu.

## Nhiệm vụ

Cho dữ liệu các đợt đo và nhiều câu hỏi ngưỡng tích lũy. Hãy lập trình trả lời với mỗi câu hỏi đợt đo sớm nhất mà tổng tích lũy vượt ngưỡng.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Chặt Nhị Phân Song Song (Parallel Binary Search).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
