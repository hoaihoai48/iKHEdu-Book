# TỐI ƯU HÓA QUY HOẠCH ĐỘNG BẰNG CONVEX HULL TRICK (CHT)
## Mã bài toán: `CPPB2-L08-16` | Khóa học C++ Bảng B (Level 2)

---

## 📖 1. Bối Cảnh & Nhiệm Vụ

Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tối Ưu Hóa Quy Hoạch Động Bằng Convex Hull Trick (CHT)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: CHT tối ưu $dp[i] = \min(dp[j] + m_j x_i + c_j)$ từ $\mathcal{O}(N^2) \to \mathcal{O}(N \log N)$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

---

## 📥 2. Định Dạng Đầu Vào (Input)

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

## 📤 3. Định Dạng Đầu Tra (Output)

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Quy Hoạch Động Bằng Convex Hull Trick (CHT).

---

## ⚙️ 5. Ràng Buộc Kỹ Thuật (Constraints)

* Giới hạn thời gian (Time Limit): $1.0\text{s}$.
* Giới hạn bộ nhớ (Memory Limit): $256\text{MB}$.
* Ràng buộc dữ liệu: $N \le 10^5$.
