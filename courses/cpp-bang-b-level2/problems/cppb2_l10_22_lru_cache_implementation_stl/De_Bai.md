# Cài đặt bộ nhớ đệm LRU Cache bằng List và Unordered Map
## Mã bài toán: CPPB2-L10-22-LRU-CACHE-IMPLEMENTATION-STL

## Bối cảnh & Nhiệm vụ
Thực hiện các thao tác `get` và `put` trên bộ nhớ đệm dung lượng $C$ trong $\mathcal{O}(1)$.

## Đầu vào (Input)
Dung lượng $C$ và danh sách truy vấn.

## Đầu ra (Output)
In ra kết quả các lệnh get.

## Ví dụ mẫu
### Sample 1
Input:
```text
2
put 1 1
put 2 2
get 1
```
Output:
```text
1
```

## Ràng buộc dữ liệu
- Thời gian chạy: $\le 1.0\text{s}$
- Bộ nhớ: $\le 256\text{MB}$
