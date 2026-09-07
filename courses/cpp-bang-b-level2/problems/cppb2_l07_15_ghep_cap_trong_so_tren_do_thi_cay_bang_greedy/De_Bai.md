# Ghép cặp trọng số trên đồ thị cây bằng greedy

## Bối cảnh

Ban quản lý khu du lịch sinh thái muốn lắp các trạm quan sát chim dọc theo hệ thống đường mòn nối các điểm dừng chân, mà mạng đường mòn này tạo thành một cấu trúc cây không có chu trình. Mỗi trạm quan sát được đặt trên một đoạn đường nối hai điểm kề nhau, và hai trạm không được dùng chung một điểm dừng để tránh làm phiền đàn chim. Ban quản lý muốn đặt càng nhiều trạm càng tốt để du khách ở đâu cũng có chỗ ngắm cảnh mà không cần đi bộ quá xa.

## Nhiệm vụ

Cho một cây gồm $N$ đỉnh (đánh số từ $1$ đến $N$) và $N - 1$ cạnh. Hãy lập trình chọn ra nhiều cạnh nhất sao cho không có hai cạnh nào chung đỉnh (mỗi đỉnh thuộc tối đa một cạnh được chọn), rồi in ra số cạnh đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số điểm dừng chân.
- $N - 1$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $u, v$ ($1 \le u, v \le N$), là một đoạn đường mòn nối hai điểm.

## Output

- In ra một số nguyên duy nhất là số trạm quan sát nhiều nhất.

## Sample 1

### Input

```text
5
1 2
1 3
3 4
3 5
```

### Output

```text
2
```

### Giải thích

- Cây có năm đỉnh với điểm $1$ nối $2$ và $3$, điểm $3$ nối thêm $4$ và $5$.
- Chọn đoạn $1 - 2$ làm trạm thứ nhất, hai điểm $1$ và $2$ đã dùng nên các đoạn chạm vào chúng đều bỏ.
- Trong phần còn lại, chọn đoạn $3 - 4$ làm trạm thứ hai, điểm $5$ lẻ loi không còn đoạn nào để ghép.
- Được $2$ trạm và không thể đặt trạm thứ ba vì chỉ còn năm điểm mà mỗi trạm chiếm hai điểm rời nhau.

## Ràng buộc

- $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
