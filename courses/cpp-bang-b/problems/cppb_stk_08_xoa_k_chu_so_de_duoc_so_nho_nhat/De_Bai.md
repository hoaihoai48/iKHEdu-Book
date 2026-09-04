# Xóa K Chữ Số Để Được Số Nhỏ Nhất

## Bối cảnh
Một mã định danh số lớn gồm $N$ chữ số dạng chuỗi ký tự. Do yêu cầu rút gọn mã trong hệ thống lưu trữ, quản trị viên cần xóa bỏ đúng $K$ chữ số bất kỳ khỏi chuỗi sao cho các chữ số còn lại giữ nguyên thứ tự ban đầu và tạo thành một số nguyên có giá trị nhỏ nhất có thể (không để số 0 vô nghĩa đứng ở đầu nếu kết quả lớn hơn 0).

## Nhiệm vụ
Cho chuỗi số $S$ và số nguyên $K$. Hãy lập trình tìm số nguyên nhỏ nhất thu được sau khi xóa đúng $K$ chữ số.

## Input
- Dòng 1: Chứa chuỗi ký tự số $S$ ($1 \le |S| \le 10^5$).
- Dòng 2: Chứa số nguyên không âm $K$ ($0 \le K < |S|$).

## Output
- In ra chuỗi ký tự đại diện cho số nhỏ nhất tìm được.

## Sample 1
### Input
```text
1432219 3
```
### Output
```text
1219
```

### Giải thích
Với số ban đầu là "1432219" và cần xóa đi $K = 3$ chữ số:
Ta xóa các chữ số 4, 3, 2 tại các vị trí đầu để giữ lại số "1219". Đây là số nguyên nhỏ nhất có thể tạo thành.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
