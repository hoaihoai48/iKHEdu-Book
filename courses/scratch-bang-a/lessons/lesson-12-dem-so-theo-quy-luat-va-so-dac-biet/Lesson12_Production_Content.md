# BÀI 12: ĐẾM SỐ THEO QUY LUẬT VÀ SỐ ĐẶC BIỆT

**Khóa học:** Scratch — Tư duy Khối lệnh, Đồ họa & Thuật toán Thi đấu (Bảng A)  
**Mã bài học:** `SCA-L12` | **Chương 4:** Số Học & Thuật Toán Tách Số  
**Thời lượng khuyến nghị:** 2 – 3 buổi học (90 phút/buổi)  
**Ánh xạ chuẩn:** Tương đương Bài 12 của Python Bảng A (`courses/python-bang-a/lessons/lesson-12`)  

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)

Sau khi hoàn thành bài học này, học sinh sẽ đạt được các chuẩn năng lực:
- **`LO-01` (Kỹ thuật Duyệt & Đếm theo điều kiện):** Sử dụng vòng lặp kết hợp khối `nếu <điều_kiện> thì thay đổi [dem] một lượng (1)`.
- **`LO-02` (Đếm số chia hết trong khoảng $[A, B]$):**
  - Cách 1 (Duyệt trâu): Duyệt từng số từ $A$ đến $B$, kiểm tra chia hết cho $K$.
  - Cách 2 (Toán học $\mathcal{O}(1)$): Công thức `floor(B / K) - floor((A - 1) / K)`.
- **`LO-03` (Số chính phương):** Số có căn bậc hai là một số nguyên:
  `([làm tròn] ([căn bậc hai] of (N))) * ([làm tròn] ([căn bậc hai] of (N))) = N`.
- **`LO-04` (Số may mắn / Số lộc phát):** Số chỉ chứa các chữ số $6$ và $8$.
- **`LO-05` (Bài toán đếm tổ hợp đơn giản):** Đếm số cách chọn, đếm số cặp thỏa mãn điều kiện tổng/tích.

---

## 2. Kỹ Thuật Đếm Trong Đoạn Bằng Vòng Lặp

```text
đặt [dem v] thành (0)
đặt [i v] thành (A)
lặp lại (((B) - (A)) + (1)) lần
    nếu < ((i) mod (K)) = (0) > thì
        thay đổi [dem v] một lượng (1)
    thay đổi [i v] một lượng (1)
nói (dem)
```

---

## 3. Công Thức Đếm Toán Học Siêu Tốc $\mathcal{O}(1)$

Khi khoảng cách giữa $A$ và $B$ lên tới hàng triệu, máy tính chạy vòng lặp sẽ bị lag. Ta dùng công thức toán học:
$$\text{Số lượng bội của } K \text{ trong } [1, N] = \lfloor N / K \rfloor$$
$$\text{Số lượng bội của } K \text{ trong } [A, B] = \lfloor B / K \rfloor - \lfloor (A - 1) / K \rfloor$$

Khối Scratch:
`(([làm tròn xuống] ((B) / (K))) - ([làm tròn xuống] (((A) - (1)) / (K))))`

---

## 4. Tử Huyệt & Các Bẫy Lỗi Thường Gặp (Bug Traps)

> **Bẫy 1: Quên trừ 1 ở đầu mút $A$**
> - *Hiện tượng:* Tính `floor(B / K) - floor(A / K)`.
> - *Hậu quả:* Nếu chính số $A$ chia hết cho $K$, phép trừ này sẽ làm mất luôn số $A$!
> - *Khắc phục:* Luôn là `floor((A - 1) / K)`.

> **Bẫy 2: Số lần lặp trong đoạn $[A, B]$**
> - *Hiện tượng:* Cho vòng lặp chạy `B - A` lần.
> - *Hậu quả:* Từ 3 đến 5 có 3 số ($3, 4, 5$), nhưng $5 - 3 = 2$ lần $\implies$ Bị thiếu mất 1 số!
> - *Khắc phục:* Số lần lặp luôn là `B - A + 1`.

---

## 5. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Từ số 1 đến số 10 có bao nhiêu số?**
   - A. 9
   - B. 10 *(Đáp án đúng: 10 - 1 + 1 = 10)*
   - C. 11
   - D. 8

2. **Từ 1 đến 100 có bao nhiêu số chia hết cho 5?**
   - A. 20 *(Đáp án đúng: 100 / 5 = 20)*
   - B. 19
   - C. 25
   - D. 10

3. **Số chính phương là số:**
   - A. Bằng bình phương của một số tự nhiên *(Đáp án đúng)*
   - B. Chia hết cho 4
   - C. Số lẻ
   - D. Số nguyên tố

4. **Số nào sau đây là số chính phương?**
   - A. 12
   - B. 16 *(Đáp án đúng: vì 4 * 4 = 16)*
   - C. 20
   - D. 27

5. **Số lộc phát chỉ chứa các chữ số:**
   - A. 6 và 8 *(Đáp án đúng)*
   - B. 0 và 1
   - C. 3 và 7
   - D. 9

6. **Số lần lặp để duyệt từ $A$ đến $B$ (với $A \le B$) là:**
   - A. `B - A`
   - B. `B - A + 1` *(Đáp án đúng)*
   - C. `B + A`
   - D. `B`

7. **Để kiểm tra số $N$ tận cùng bằng chữ số 6, điều kiện là:**
   - A. `(N mod 10) = 6` *(Đáp án đúng)*
   - B. `(N / 10) = 6`
   - C. `N = 6`
   - D. `N mod 6 = 0`

8. **Trong các số: 4, 9, 16, 25, 36, có bao nhiêu số chính phương?**
   - A. 3
   - B. 5 *(Đáp án đúng: tất cả đều là số chính phương)*
   - C. 4
   - D. 2

9. **Công thức đếm số lượng số chẵn trong đoạn $[1, N]$ là:**
   - A. `[làm tròn xuống] (N / 2)` *(Đáp án đúng)*
   - B. `N - 2`
   - C. `N * 2`
   - D. `N mod 2`

10. **Biến đếm `dem` cần được đặt giá trị ban đầu là:**
    - A. 0 *(Đáp án đúng)*
    - B. 1
    - C. -1
    - D. 100
