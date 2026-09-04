# Xóa Ít Ký Tự Nhất Để Chuỗi Đối Xứng

## Bối cảnh
Một thiết bị viễn thông thu nhận một chuỗi tín hiệu bị nhiễu chứa một số ký tự rác. Để khôi phục lại tính toàn vẹn của tín hiệu đối xứng nguyên bản, kỹ sư cần loại bỏ bớt một số lượng ký tự ít nhất từ chuỗi thu được sao cho chuỗi còn lại trở thành một chuỗi đối xứng.

## Nhiệm vụ
Cho chuỗi ký tự $S$. Hãy lập trình tìm số lượng ký tự ít nhất cần xóa bỏ để chuỗi còn lại là một chuỗi đối xứng.

## Input
- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).

## Output
- In ra trên một dòng duy nhất số ký tự ít nhất cần xóa.

## Sample 1
### Input
```text
aebcbda
```
### Output
```text
2
```

### Giải thích
Với chuỗi $S = \text{"aebcbda"}$:
Chuỗi con đối xứng dài nhất có thể giữ lại là $\text{"abcba"}$ (độ dài 5). Để thu được chuỗi này, ta chỉ cần xóa đi đúng 2 ký tự là 'e' và 'd'. Số ký tự cần xóa ít nhất là 2.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
