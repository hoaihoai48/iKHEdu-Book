# Đọc và in mảng số nguyên theo thứ tự ngược

## Bối cảnh
Trong trò chơi ghi nhớ chuỗi số, người quản trò đọc ra một dãy gồm $N$ số nguyên. Người chơi có nhiệm vụ đọc lại dãy số đó theo thứ tự ngược lại từ số cuối cùng về số đầu tiên. Bạn An muốn viết một chương trình sử dụng `vector` trong C++ để ghi lại dãy số và in ngược thật chính xác.

## Nhiệm vụ
Cho một dãy gồm $N$ số nguyên. Hãy lập trình đọc dữ liệu vào một `vector<int>` và in các phần tử theo thứ tự ngược lại từ phần tử cuối cùng về phần tử đầu tiên, cách nhau bởi một khoảng trắng.

## Input
- Dòng thứ nhất chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng thứ hai chứa $N$ số nguyên $a_1, a_2, \dots, a_N$ ($-10^9 \le a_i \le 10^9$), cách nhau bởi một khoảng trắng.

## Output
- In ra trên một dòng duy nhất $N$ số nguyên theo thứ tự từ cuối về đầu, cách nhau bởi một khoảng trắng.

## Sample 1
### Input
```text
5
1 3 5 7 9
```
### Output
```text
9 7 5 3 1
```

### Giải thích
Dãy số ban đầu là $[1, 3, 5, 7, 9]$.
Thứ tự in ngược lại từ cuối về đầu là: $9, 7, 5, 3, 1$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, -10^9 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
