# TỔNG CẤP SỐ NHÂN $S_N = \SUM_{I=0}^N A^I \BMOD M$
## Mã bài toán: `CPPB2-L02-08` | Khóa học C++ Bảng B (Level 2)

---

## 📖 1. Bối Cảnh & Nhiệm Vụ

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tổng Cấp Số Nhân $S_N = \sum_{i=0}^N A^i \bmod M$** là bài toán trọng tâm thuộc cấp độ **P3** nhằm rèn luyện: Chia để trị tính tổng cấp số nhân $\mathcal{O}(\log N)$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

---

## 📥 2. Định Dạng Đầu Vào (Input)

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

## 📤 3. Định Dạng Đầu Ra (Output)

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

## 📌 4. Ví Dụ Mẫu (Sample)

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Cấp Số Nhân $S_N = \sum_{i=0}^N A^i \bmod M$.

---

## ⚙️ 5. Ràng Buộc Kỹ Thuật (Constraints)

* Giới hạn thời gian (Time Limit): $1.0\text{s}$.
* Giới hạn bộ nhớ (Memory Limit): $256\text{MB}$.
* Ràng buộc dữ liệu: $A, N \le 10^{18}, M = 10^9+7$.
