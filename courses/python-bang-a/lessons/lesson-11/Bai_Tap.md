# Hệ thống bài tập thực hành — bài 11: Danh sách và thao tác cơ bản

---

## Bảng ma trận bài tập (14 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L16-P01` | Nhập dãy số & in phần tử đầu - cuối | `Cơ bản` | $N \le 1000$ | Cú pháp `list(map(int, ...))` và index |
| 02 | `PYA-L16-P02` | Thêm điểm vào danh sách | `Cơ bản` | Số lượng phần tử $\le 100$ | Phương thức `append()` |
| 03 | `PYA-L16-P03` | Tính tổng các phần tử trong dãy | `Cơ bản` | $N \le 10^5, A_i \le 10^9$ | Duyệt `for x in a` cộng dồn |
| 04 | `PYA-L16-P04` | Đếm số lượng số chẵn trong mảng | `Cơ bản` | $N \le 10^5$ | Đếm phần tử thỏa mãn điều kiện |
| 05 | `PYA-L16-P05` | Tìm số lớn nhất & nhỏ nhất | `Cơ bản` | $N \le 10^5$ | Tìm min/max bằng thuật toán duyệt |
| 06 | `PYA-L16-P06` | In dãy số theo thứ tự đảo ngược | `Luyện tập` | $N \le 10^5$ | Đảo ngược mảng `a[::-1]` |
| 07 | `PYA-L16-P07` | Đếm số lần xuất hiện của x | `Luyện tập` | $N \le 10^5$ | Phương thức `a.count(x)` |
| 08 | `PYA-L16-P08` | Tìm vị trí đầu tiên của x | `Luyện tập` | $N \le 10^5$ | Tìm kiếm tuần tự trả về chỉ số index |
| 09 | `PYA-L16-P09` | Tách mảng chẵn và mảng lẻ | `Luyện tập` | $N \le 10^5$ | Phân loại dữ liệu vào 2 danh sách riêng |
| 10 | `PYA-L16-P10` | Xóa phần tử đầu tiên bằng x | `Luyện tập` | $N \le 10^5$ | Sử dụng `a.remove(x)` an toàn |
| 11 | `PYA-L16-P11` | Thay thế tất cả số âm bằng số 0 | `Luyện tập` | $N \le 10^5$ | Cập nhật mảng theo vị trí `a[i]` |
| 12 | `PYA-L16-P12` | Chèn số vào vị trí K | `Vận dụng` | $N \le 1000$ | Thao tác `a.insert(k, x)` |
| 13 | `PYA-L16-P13` | Xoay vòng danh sách sang phải | `Vận dụng` | $N \le 10^5, K \le N$ | Dịch mảng sang phải $K$ vị trí |
| 14 | `PYA-L16-P14` | Cặp số có tổng bằng s | `Thử thách` | $N \le 10^4$ | Tìm 2 phần tử $A_i + A_j = S$ |

---

### Bài 1 (Cơ bản): Nhập dãy số & in phần tử đầu - cuối (`PYA-L16-P01`)

* **Yêu cầu:** Cho một dãy gồm $N$ số nguyên. Hãy in ra phần tử đầu tiên và phần tử cuối cùng của dãy số đó.
* **Input:**
  * Dòng 1: Số nguyên dương $N$ ($1 \le N \le 1000$).
  * Dòng 2: Gồm $N$ số nguyên cách nhau bởi khoảng trắng.
* **Output:** In phần tử đầu tiên và phần tử cuối cùng trên một dòng, cách nhau một khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5`<br>`10 25 3 47 99` | `10 99` |

---

### Bài 2 (Cơ bản): Thêm điểm vào danh sách (`PYA-L16-P02`)

* **Bối cảnh:** Thầy giáo có một danh sách điểm kiểm tra ban đầu. Sau đó có thêm một bạn học sinh nộp bài muộn và được chấm điểm $X$.
* **Yêu cầu:** Cho danh sách các số nguyên ban đầu và số $X$. Hãy thêm $X$ vào cuối danh sách và in ra toàn bộ danh sách mới.
* **Input:**
  * Dòng 1: Danh sách các số nguyên cách nhau bởi khoảng trắng.
  * Dòng 2: Số nguyên $X$.
* **Output:** Danh sách các số sau khi thêm $X$, cách nhau bởi khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `8 9 7 10`<br>`9` | `8 9 7 10 9` |

---

### Bài 3 (Cơ bản): Tính tổng các phần tử trong dãy (`PYA-L16-P03`)

* **Yêu cầu:** Cho một dãy gồm $N$ số nguyên. Hãy tính tổng tất cả các phần tử trong dãy số.
* **Input:**
  * Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên ($|A_i| \le 10^9$).
* **Output:** Tổng các phần tử trong dãy.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `4`<br>`10 20 30 40` | `100` |

---

### Bài 4 (Cơ bản): Đếm số lượng số chẵn trong mảng (`PYA-L16-P04`)

* **Yêu cầu:** Cho một dãy gồm $N$ số nguyên dương. Hãy đếm xem có bao nhiêu số chẵn trong dãy.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Số lượng số chẵn.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5`<br>`2 5 8 10 13` | `3` |

---

### Bài 5 (Cơ bản): Tìm số lớn nhất & nhỏ nhất (`PYA-L16-P05`)

* **Yêu cầu:** Cho dãy $N$ số nguyên. Hãy tìm giá trị lớn nhất và giá trị nhỏ nhất trong dãy số.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Giá trị lớn nhất, theo sau là giá trị nhỏ nhất, cách nhau một khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5`<br>`12 5 89 3 45` | `89 3` |

---

### Bài 6 (Luyện tập): In dãy số theo thứ tự đảo ngược (`PYA-L16-P06`)

* **Yêu cầu:** Cho dãy $N$ số nguyên. Hãy in ra dãy số theo thứ tự ngược lại (từ phần tử cuối cùng về phần tử đầu tiên).
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Dãy số sau khi đảo ngược trên một dòng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `4`<br>`1 2 3 4` | `4 3 2 1` |

---

### Bài 7 (Luyện tập): Đếm số lần xuất hiện của x (`PYA-L16-P07`)

* **Yêu cầu:** Cho dãy $N$ số nguyên và một số nguyên $X$. Hãy đếm xem số $X$ xuất hiện bao nhiêu lần trong dãy số.
* **Input:**
  * Dòng 1: Hai số nguyên $N$ và $X$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Số lần xuất hiện của $X$.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `6 5`<br>`5 2 5 7 5 9` | `3` |

---

### Bài 8 (Luyện tập): Tìm vị trí đầu tiên của x (`PYA-L16-P08`)

* **Yêu cầu:** Cho dãy $N$ số nguyên và số $X$. Hãy tìm vị trí (chỉ số index từ 0) xuất hiện **đầu tiên** của số $X$ trong dãy. Nếu số $X$ không có trong dãy, in ra `-1`.
* **Input:**
  * Dòng 1: Hai số nguyên $N$ và $X$.
  * Dòng 2: $N$ số nguyên.
* **Output:** Vị trí index đầu tiên của $X$, hoặc `-1`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5 7`<br>`3 5 7 9 7` | `2` |
  | `4 10`<br>`1 2 3 4` | `-1` |

---

### Bài 9 (Luyện tập): Tách mảng chẵn và mảng lẻ (`PYA-L16-P09`)

* **Yêu cầu:** Cho dãy $N$ số nguyên. Hãy tách dãy thành 2 danh sách: một danh sách gồm các số chẵn, một danh sách gồm các số lẻ (giữ nguyên thứ tự xuất hiện ban đầu).
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:**
  * Dòng 1: Các số chẵn (cách nhau bởi khoảng trắng).
  * Dòng 2: Các số lẻ (cách nhau bởi khoảng trắng).
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `6`<br>`1 4 7 8 2 9` | `4 8 2`<br>`1 7 9` |

---

### Bài 10 (Luyện tập): Xóa phần tử đầu tiên bằng x (`PYA-L16-P10`)

* **Yêu cầu:** Cho dãy $N$ số nguyên và số $X$. Nếu $X$ có trong dãy, hãy xóa phần tử đầu tiên có giá trị bằng $X$ và in ra dãy số còn lại. Nếu $X$ không có trong dãy, in ra `KHONG CO`.
* **Input:**
  * Dòng 1: Hai số $N, X$.
  * Dòng 2: $N$ số nguyên.
* **Output:** Dãy số sau khi xóa, hoặc `KHONG CO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5 3`<br>`1 3 5 3 7` | `1 5 3 7` |

---

### Bài 11 (Luyện tập): Thay thế tất cả số âm bằng số 0 (`PYA-L16-P11`)

* **Yêu cầu:** Cho dãy $N$ số nguyên gồm cả số âm và số dương. Hãy thay thế toàn bộ các số âm trong dãy bằng số 0 và in ra dãy mới.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Dãy số sau khi thay thế.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5`<br>`3 -5 8 -2 0` | `3 0 8 0 0` |

---

### Bài 12 (Vận dụng): Chèn số vào vị trí K (`PYA-L16-P12`)

* **Yêu cầu:** Cho dãy $N$ số nguyên, số nguyên $X$ và vị trí index $K$ ($0 \le K \le N$). Hãy chèn số $X$ vào đúng vị trí $K$ của dãy số và in ra dãy mới gồm $(N + 1)$ phần tử.
* **Input:**
  * Dòng 1: Số nguyên $N$.
  * Dòng 2: $N$ số nguyên.
  * Dòng 3: Hai số nguyên $X$ và $K$.
* **Output:** Dãy số sau khi chèn.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `4`<br>`10 20 30 40`<br>`99 1` | `10 99 20 30 40` |

---

### Bài 13 (Vận dụng): Xoay vòng danh sách sang phải (`PYA-L16-P13`)

* **Bối cảnh:** Phép xoay phải danh sách $K$ vị trí là thao tác nhấc $K$ phần tử cuối cùng của mảng đem gắn lên đầu mảng.
* **Yêu cầu:** Cho dãy $N$ số nguyên và số $K$ ($1 \le K \le N \le 10^5$). Hãy in ra dãy số sau khi xoay phải $K$ vị trí.
* **Input:**
  * Dòng 1: Hai số $N$ và $K$.
  * Dòng 2: $N$ số nguyên.
* **Output:** Dãy số sau khi xoay phải.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5 2`<br>`1 2 3 4 5` | `4 5 1 2 3` | Hai phần tử cuối là 4, 5 được đưa lên đầu. |

---

### Bài 14 (Thử thách): Cặp số có tổng bằng s (`PYA-L16-P14`)
*(Đề thi Tin học trẻ Bảng A)*

* **Yêu cầu:** Cho dãy gồm $N$ số nguyên đôi một khác nhau và một số nguyên mục tiêu $S$. Hãy đếm xem có bao nhiêu cặp chỉ số $(i, j)$ với $i < j$ thỏa mãn:
  $$A_i + A_j = S$$
* **Input:**
  * Dòng 1: Hai số nguyên $N$ và $S$ ($1 \le N \le 10^4, |S| \le 10^9$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Số lượng cặp thỏa mãn.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5 10`<br>`2 4 6 8 3` | `2` | Có 2 cặp là $(2, 8)$ và $(4, 6)$. |
