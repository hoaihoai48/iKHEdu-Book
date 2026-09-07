# Diện tích phủ bởi các hình chữ nhật rời rạc

## Bối cảnh

Trên sân trường, các lớp dựng gian hàng hội chợ hình chữ nhật, gian nọ có thể chờm lên gian kia. Ban tổ chức muốn biết tổng diện tích mặt sân thực sự bị các gian hàng che phủ.

Các bạn vẽ lại vị trí từng gian hàng lên giấy kẻ ô rồi tính phần diện tích bị phủ ít nhất một lần.

## Nhiệm vụ

Cho danh sách các hình chữ nhật rời rạc trên mặt phẳng. Hãy lập trình tính tổng diện tích bị phủ bởi ít nhất một hình chữ nhật.

## Input

- Dòng đầu tiên chứa số nguyên $n$ ($1 \le n \le 100$) — số hình chữ nhật.
- $n$ dòng tiếp theo, mỗi dòng chứa bốn số nguyên $x_1, y_1, x_2, y_2$ ($|x_i|, |y_i| \le 10^9$, $x_1 < x_2$, $y_1 < y_2$) là góc dưới-trái và góc trên-phải của một hình.

## Output

- In ra một dòng duy nhất là tổng diện tích của phần mặt phẳng bị phủ bởi ít nhất một hình chữ nhật.

## Sample 1
### Input
```text
2
0 0 2 2
1 1 3 3
```
### Output
```text
7
```
### Giải thích

Hình thứ nhất diện tích $2 \cdot 2 = 4$, hình thứ hai cũng $4$. Phần giao nhau là hình vuông từ $(1, 1)$ tới $(2, 2)$ diện tích $1$. Diện tích phủ bằng $4 + 4 - 1 = 7$.

## Ràng buộc

- $1 \le n \le 100$, tọa độ có trị tuyệt đối không quá $10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
