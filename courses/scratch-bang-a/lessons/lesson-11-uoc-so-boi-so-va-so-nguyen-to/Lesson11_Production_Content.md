# Bài 11: ƯỚC SỐ, BỘI SỐ VÀ SỐ NGUYÊN TỐ

## 1. Thuật Toán Kiểm Tra Số Nguyên Tố Bằng Biến Đếm Ước

```text
đặt [dem_uoc v] thành (0)
đặt [i v] thành (1)
lặp lại (N) lần
    nếu < ((N) mod (i)) = (0) > thì
        thay đổi [dem_uoc v] một lượng (1)
    thay đổi [i v] một lượng (1)

nếu < (dem_uoc) = (2) > thì
    nói [LA SO NGUYEN TO]
nếu không thì
    nói [KHONG PHAI SO NGUYEN TO]
```

---

## 2. Thuật Toán Tối Ưu Bằng Biến Cờ Dừng Sớm

Khi $N$ lớn (ví dụ $N = 10007$), duyệt đến $N$ sẽ rất chậm. Ta tối ưu:
1. Nếu $N < 2 \implies$ Không phải số nguyên tố.
2. Đặt `la_snt = 1`.
3. Cho $i$ chạy từ $2$ đến căn bậc hai của $N$:
   - Nếu $N \pmod i = 0 \implies$ Đặt `la_snt = 0`, dừng vòng lặp ngay!

```text
nếu < (N) < (2) > thì
    nói [NO]
nếu không thì
    đặt [la_snt v] thành (1)
    đặt [i v] thành (2)
    lặp lại cho đến khi < ((i) * (i)) > (N) hoặc (la_snt = 0) >
        nếu < ((N) mod (i)) = (0) > thì
            đặt [la_snt v] thành (0)
        thay đổi [i v] một lượng (1)
    nếu < (la_snt) = (1) > thì
        nói [YES]
    nếu không thì
        nói [NO]
```

---

## 3. Tử Huyệt & Các Bẫy Lỗi Thường Gặp (Bug Traps)

> **Bẫy 1: Quên xét số 0 và số 1**
> - *Hiện tượng:* Số 0 và 1 không phải là số nguyên tố!
> - *Hậu quả:* Nếu không chặn điều kiện $N < 2$, số 1 có 1 ước cũng có thể bị thuật toán kết luận sai.
> - *Khắc phục:* Luôn kiểm tra $N < 2$ đầu tiên.

> **Bẫy 2: Nhầm lẫn giữa Số nguyên tố và Số lẻ**
> - Số 2 là **số nguyên tố chẵn duy nhất**!
> - Số 9, 15, 21, 25, 27 là số lẻ nhưng **không phải là số nguyên tố** (hợp số).

---

## 4. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Số nguyên tố nhỏ nhất là số nào?**
   - A. 0
   - B. 1
   - C. 2 *(Đáp án đúng)*
   - D. 3

2. **Số nào sau đây LÀ số nguyên tố?**
   - A. 9
   - B. 15
   - C. 17 *(Đáp án đúng)*
   - D. 21

3. **Số nào sau đây KHÔNG PHẢI là số nguyên tố?**
   - A. 2
   - B. 3
   - C. 5
   - D. 1 *(Đáp án đúng: số 1 không phải số nguyên tố)*

4. **Số 12 có tất cả bao nhiêu ước số?**
   - A. 4
   - B. 6 *(Đáp án đúng: 1, 2, 3, 4, 6, 12)*
   - C. 5
   - D. 3

5. **Số hoàn hảo $6$ có các ước nhỏ hơn nó là $1, 2, 3$. Tổng của chúng là:**
   - A. 6 *(Đáp án đúng: 1 + 2 + 3 = 6)*
   - B. 5
   - C. 7
   - D. 12

6. **Khi kiểm tra số nguyên tố, ta chỉ cần duyệt $i$ đến:**
   - A. Căn bậc hai của N *(Đáp án đúng)*
   - B. N / 2
   - C. N - 1
   - D. 100

7. **Điều kiện $d$ là ước số của $N$ viết trong Scratch là:**
   - A. `< ((N) mod (d)) = (0) >` *(Đáp án đúng)*
   - B. `< ((N) / (d)) = (0) >`
   - C. `< N = d >`
   - D. `< N > d >`

8. **Số chẵn duy nhất là số nguyên tố là:**
   - A. 0
   - B. 2 *(Đáp án đúng)*
   - C. 4
   - D. Không có số nào

9. **Nếu một số lớn hơn 1 và có nhiều hơn 2 ước số, số đó được gọi là:**
   - A. Hợp số *(Đáp án đúng)*
   - B. Số nguyên tố
   - C. Số lẻ
   - D. Số âm

10. **Ước số lớn nhất của số $N$ (khác chính nó) luôn nhỏ hơn hoặc bằng:**
    - A. $N / 2$ *(Đáp án đúng)*
    - B. $N - 1$
    - C. Căn bậc hai của N
    - D. 10
