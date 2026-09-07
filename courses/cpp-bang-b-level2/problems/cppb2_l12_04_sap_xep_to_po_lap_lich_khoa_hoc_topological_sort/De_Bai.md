# Sắp xếp topo lập lịch môn học

## Bối cảnh

Phòng đào tạo của trường đại học cần xếp lịch học cho N môn trong học kỳ mới, trong đó M cặp điều kiện tiên quyết yêu cầu môn này phải học trước môn kia thì sinh viên mới đủ kiến thức theo kịp bài giảng. Nếu các điều kiện mâu thuẫn tạo thành vòng tròn thì kế hoạch phải làm lại từ đầu. Phòng đào tạo cần chương trình đưa ra một thứ tự học hợp lệ, ưu tiên môn có số thứ tự nhỏ khi có nhiều lựa chọn.

## Nhiệm vụ

Cho đồ thị có hướng gồm $N$ đỉnh và $M$ cạnh $u \to v$ (môn $u$ học trước môn $v$). Hãy lập trình tìm một thứ tự topo bằng thuật toán Kahn với hàng đợi ưu tiên nhỏ nhất, rồi in ra dãy thứ tự (in ra $-1$ nếu đồ thị có chu trình).

## Input

- Dòng 1: hai số nguyên $N, M$ ($1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v$ là cạnh có hướng $u \to v$.

## Output

- In ra một dòng duy nhất: dãy $N$ đỉnh theo thứ tự topo (ưu tiên đỉnh nhỏ), hoặc $-1$ nếu có chu trình.

## Sample 1

### Input

```text
4 3
1 2
1 3
3 4
```

### Output

```text
1 2 3 4```

### Giải thích

- Ban đầu chỉ môn $1$ không có điều kiện tiên quyết nên xếp $1$ trước.
- Sau khi xong môn $1$, hai môn $2$ và $3$ đều đủ điều kiện, ưu tiên số nhỏ nên xếp $2$ rồi đến $3$.
- Cuối cùng môn $4$ đủ điều kiện và được xếp cuối, dãy in ra là $1\ 2\ 3\ 4$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
