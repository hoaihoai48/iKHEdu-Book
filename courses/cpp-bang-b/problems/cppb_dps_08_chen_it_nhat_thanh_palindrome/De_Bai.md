# Chèn Ít Ký Tự Nhất Tạo Chuỗi Đối Xứng

## Bối cảnh
Một máy in nhãn hàng hóa bị lỗi chỉ in được một chuỗi ký tự khuyết thiếu. Để nhãn hàng có tính thẩm mỹ cân đối, kỹ thuật viên cần chèn thêm vào các vị trí bất kỳ trong chuỗi một số lượng ký tự ít nhất sao cho chuỗi thu được trở thành một chuỗi đối xứng hoàn hảo.

## Nhiệm vụ
Cho chuỗi ký tự $S$. Hãy lập trình tìm số lượng ký tự ít nhất cần phải chèn thêm vào chuỗi $S$ để biến nó thành một chuỗi đối xứng.

## Input
- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).

## Output
- In ra trên một dòng duy nhất số ký tự ít nhất cần chèn thêm.

## Sample 1
### Input
```text
zzazz
```
### Output
```text
0
```

### Giải thích
Với chuỗi $S = \text{"mbadm"}$:
Để chuỗi trở thành đối xứng, ta có thể chèn thêm 2 ký tự 'd' và 'b' vào các vị trí thích hợp để tạo thành chuỗi $\text{"mbdadbm"}$. Số ký tự chèn thêm ít nhất là 2.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
