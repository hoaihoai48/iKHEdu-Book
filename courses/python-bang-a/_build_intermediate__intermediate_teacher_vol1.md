# Lời nói đầu

Cuốn **Giáo trình Python — Sách giáo viên — Quyển 1** được biên soạn đồng bộ cùng bộ giáo trình lập trình Python cơ bản iKHEDU, dành riêng cho quý thầy cô giáo và các huấn luyện viên chuyên trách. Tài liệu này cung cấp toàn bộ lời giải chi tiết, chuẩn mực và hệ thống **hướng dẫn sư phạm thực chiến chuyên sâu** (ý tưởng và phân tích thuật toán, bảng mô phỏng chạy tay từng bước trên số liệu mẫu thực tế, lưu ý và các bẫy lỗi kinh điển thường gặp) cho toàn bộ **157 bài toán thực hành** thuộc Chương 01 và Chương 02.

Mỗi bài toán trong sách đều được cấu trúc thống nhất từ đề bài học sinh, phân tích tư duy giải pháp, bảng theo dõi biến số trực quan đến mã nguồn tham khảo tối ưu nhất, giúp thầy cô dễ dàng tổ chức giờ học chất lượng cao và đồng hành hiệu quả cùng học sinh.

# CHƯƠNG 01: TÍNH TOÁN CƠ BẢN

### Bài 01 [pya_l01_p01_loi_chao_robot]: Lời chào robot

Bối cảnh: Khi một hệ thống tự hành hoặc robot công nghiệp được khởi động trong phòng thực hành lập trình, hệ thống cần gửi thông điệp chào mừng đầu tiên ra thiết bị đầu ra tiêu chuẩn.

Nhiệm vụ: Viết chương trình in ra chính xác dòng thông điệp: `Xin chao cac ban! Toi la Robot Python.`

**Đầu vào (Input):**

Không có dữ liệu vào.

**Đầu ra (Output):**

In ra một dòng chứa câu chào đúng mẫu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
|  | Xin chao cac ban! Toi la Robot Python. |

**Giải thích:** In chính xác câu chào ra màn hình theo đúng quy định.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là in ra một câu chữ cố định: `Xin chao cac ban! Toi la Robot Python.` Thầy cô giải thích cho các con rằng chương trình không cần đọc gì từ bàn phím, chỉ cần hiện đúng câu chào ra màn hình.
- Quy trình chỉ có một bước duy nhất: gọi lệnh `print(...)` với đúng chuỗi chữ trong ngoặc kép, gồm chữ hoa ở đầu `Xin`, dấu chấm than sau `ban!`, chữ `Toi`, chữ `Robot Python` và dấu chấm cuối câu.
- Xử lý biên: bài này không có số liệu vào nên không có giá trị biên. Thầy cô nhắc các con sao chép từng chữ cái cho khớp, vì thiếu hay thừa một dấu cách cũng làm kết quả khác đi.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: (không có dữ liệu vào))

| Bước | Lệnh chạy | Màn hình hiện ra |
|------|-----------|------------------|
| 1 | `print("Xin chao cac ban! Toi la Robot Python.")` | `Xin chao cac ban! Toi la Robot Python.` |
| 2 | Kết thúc chương trình | Kết quả cuối cùng: `Xin chao cac ban! Toi la Robot Python.` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: quên dấu ngoặc kép quanh câu chữ, ví dụ viết `print(Xin chao cac ban! Toi la Robot Python.)`. Chương trình báo lỗi và không in ra gì cả. Cách sửa: luôn đặt câu chữ trong cặp dấu ngoặc kép `"..."`.
- Bẫy 2: gõ sai một chữ, ví dụ `print("Xin chao cac ban! Toi la Robot python.")` (chữ `p` thường). Màn hình hiện `... Robot python.` thay vì `... Robot Python.` nên bị tính là kết quả sai. Cách sửa: đối chiếu từng chữ với đề bài trước khi chạy.
- Bẫy 3: thêm lệnh `input()` ở đầu vì tưởng bài nào cũng phải nhập. Khi chạy, chương trình cứ đứng chờ các con gõ thêm, không in ra câu chào ngay. Cách sửa: bài này không có dữ liệu vào nên xóa dòng `input()`, chỉ giữ một dòng `print(...)`.

#### 4. Lời giải tham khảo

```python
print("Xin chao cac ban! Toi la Robot Python.")
```

### Bài 02 [pya_l01_p02_cau_doi_tet]: Câu đối ngày tết

Bối cảnh: Trong ứng dụng hiển thị bảng điện tử chào mừng năm mới, hệ thống cần in hai vế câu đối truyền thống trên hai dòng riêng biệt.

Nhiệm vụ: In ra đúng hai dòng chữ, mỗi dòng là một vế câu đối:
  - Dòng 1: `Chuc mung nam moi`
  - Dòng 2: `Van su nhu y`

**Đầu vào (Input):**

Không có dữ liệu vào.

**Đầu ra (Output):**

In ra hai dòng theo đúng quy định.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
|  | Chuc mung nam moi <br> Van su nhu y |

**Giải thích:** Sử dụng hai lệnh `print()` liên tiếp để in trên hai dòng riêng biệt.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là in hai dòng chữ cố định: dòng 1 là `Chuc mung nam moi`, dòng 2 là `Van su nhu y`. Thầy cô giải thích mỗi lệnh `print()` tự xuống dòng một lần sau khi in xong.
- Quy trình gồm hai bước nối tiếp: lệnh `print("Chuc mung nam moi")` in vế đối thứ nhất, rồi lệnh `print("Van su nhu y")` in vế đối thứ hai xuống dòng dưới.
- Xử lý biên: bài này không có số liệu vào nên không có giá trị biên. Thầy cô nhắc các con giữ đúng thứ tự hai dòng, vì đổi chỗ hai dòng cho nhau cũng bị tính là kết quả sai.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: (không có dữ liệu vào))

| Bước | Lệnh chạy | Màn hình hiện ra |
|------|-----------|------------------|
| 1 | `print("Chuc mung nam moi")` | Dòng 1: `Chuc mung nam moi` |
| 2 | `print("Van su nhu y")` | Dòng 2: `Van su nhu y` |
| 3 | Kết thúc chương trình | Kết quả cuối cùng đúng hai dòng như trên. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: dồn cả hai vế vào một lệnh như `print("Chuc mung nam moi Van su nhu y")`. Màn hình chỉ hiện một dòng dài thay vì hai dòng riêng biệt. Cách sửa: tách thành hai lệnh `print()` riêng.
- Bẫy 2: viết liền hai lệnh trên cùng một logic in một dòng, ví dụ dùng `print("Chuc mung nam moi", end=" ")` rồi in tiếp vế hai. Kết quả ra `Chuc mung nam moi Van su nhu y` trên một dòng, không đúng yêu cầu. Cách sửa: để `print()` mặc định xuống dòng, không thêm `end=" "`.
- Bẫy 3: gõ sai chữ hoa thường, ví dụ `print("Chuc Mung Nam Moi")`. Màn hình hiện khác mẫu `Chuc mung nam moi` nên bị tính là kết quả sai. Cách sửa: sao chép đúng từng chữ trong đề bài.

#### 4. Lời giải tham khảo

```python
print("Chuc mung nam moi")
print("Van su nhu y")
```

### Bài 03 [pya_l01_p05_doc_in_so_nguyen]: Đọc và in số nguyên

Bối cảnh: Máy đếm vé tham quan cần nhận vào mã số may mắn của khách và hiển thị lại mã số đó.

Nhiệm vụ: Nhập một số nguyên $N$ từ bàn phím và in số nguyên đó ra màn hình.

**Đầu vào (Input):**

Một dòng duy nhất chứa số nguyên $N$ ($-10^9 \le N \le 10^9$).

**Đầu ra (Output):**

In ra số nguyên $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 2026 | 2026 |

**Giải thích:** Nhập vào số 2026 và in lại đúng số 2026.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là đọc lại mã số may mắn `N` rồi hiện lại đúng số đó. Thầy cô ví biến `n` như một chiếc hộp đựng con số mà máy đếm vé vừa nhận được.
- Quy trình gồm hai bước với biến `n` trong lời giải: đọc dòng chữ `"2026"` từ bàn phím rồi đổi thành số nguyên bằng `int(...)` và cất vào `n`, sau đó `print(n)` hiện giá trị của `n` ra màn hình, với số mẫu cho ra `2026`.
- Xử lý biên: ràng buộc cho `N` từ `-10^9` tới `10^9`, nên thầy cô cho các con thử thêm hai đầu biên `-1000000000` và `1000000000` để thấy chương trình vẫn đọc và in lại đúng, kể cả số âm có dấu trừ đằng trước.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2026)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `n = int(input())` với bàn phím gõ `2026` | `n = 2026` | (chưa in gì) |
| 2 | `print(n)` | `n = 2026` | `2026` |
| 3 | Kết thúc chương trình | — | Kết quả cuối cùng: `2026`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: quên đổi sang số, viết `n = input()` rồi `print(n * 2)` ở bài khác thì với mẫu `2026` sẽ ra `20262026` do nối chữ. Ngay trong bài này tuy in lại vẫn đúng, nhưng thói quen thiếu `int()` sẽ gây sai ở bài tính toán. Cách sửa: luôn viết `n = int(input())`.
- Bẫy 2: in kèm chữ trang trí, ví dụ `print("N =", n)` thì với mẫu `2026` màn hình hiện `N = 2026` thay vì `2026`. Cách sửa: chỉ viết `print(n)`.
- Bẫy 3: đọc thừa một dòng, ví dụ gọi `input()` hai lần thì chương trình cứ chờ nhập thêm sau khi đã gõ `2026`. Cách sửa: bài này chỉ có một số nên chỉ gọi `input()` một lần.

#### 4. Lời giải tham khảo

```python
n = int(input())
print(n)
```

### Bài 04 [pya_l01_p03_in_so_sep]: In số trên một hàng với sep

Bối cảnh: Thầy giáo yêu cầu in 5 chữ số đầu tiên từ 1 đến 5 được nối với nhau bằng dấu gạch ngang `-`.

Nhiệm vụ: Viết chương trình in ra dòng chữ: `1-2-3-4-5`.

**Đầu vào (Input):**

Không có dữ liệu vào.

**Đầu ra (Output):**

In ra dòng chữ `1-2-3-4-5` bằng cách tận dụng tham số `sep`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
|  | 1-2-3-4-5 |

**Giải thích:** Các số từ 1 đến 5 được in cách nhau bằng dấu `-`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là in năm số `1 2 3 4 5` trên cùng một hàng, nhưng giữa các số là dấu gạch ngang `-` thay vì dấu cách. Thầy cô giải thích tham số `sep="-"` chính là sợi dây nối các số lại với nhau.
- Quy trình chỉ có một bước: gọi `print(1, 2, 3, 4, 5, sep="-")`, máy sẽ đặt dấu `-` vào giữa mỗi cặp số kề nhau rồi in ra `1-2-3-4-5`.
- Xử lý biên: bài này không có số liệu vào nên không có giá trị biên. Thầy cô nhắc các con đếm đủ năm số từ 1 tới 5, thiếu số 5 hay thừa số 6 đều làm kết quả khác đi.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: (không có dữ liệu vào))

| Bước | Lệnh chạy | Màn hình hiện ra |
|------|-----------|------------------|
| 1 | `print(1, 2, 3, 4, 5, sep="-")` | `1-2-3-4-5` |
| 2 | Kết thúc chương trình | Kết quả cuối cùng: `1-2-3-4-5`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: quên tham số `sep`, viết `print(1, 2, 3, 4, 5)` thì màn hình hiện `1 2 3 4 5` với dấu cách thay vì `1-2-3-4-5`. Cách sửa: thêm `sep="-"` vào trong lệnh `print`.
- Bẫy 2: đặt dấu nối sai, ví dụ `print(1, 2, 3, 4, 5, sep="_")` thì màn hình hiện `1_2_3_4_5` thay vì `1-2-3-4-5`. Cách sửa: dùng đúng dấu gạch ngang `"-"`.
- Bẫy 3: in từng số trên từng dòng bằng năm lệnh `print(1)` ... `print(5)` thì màn hình hiện năm dòng rời nhau thay vì một hàng `1-2-3-4-5`. Cách sửa: gom cả năm số vào một lệnh `print` duy nhất.

#### 4. Lời giải tham khảo

```python
print(1, 2, 3, 4, 5, sep="-")
```

### Bài 05 [pya_l01_p25_nhan_doi_gia_tri]: Nhân đôi giá trị

Bối cảnh: Bác Tư là một nông dân giỏi nổi tiếng ở vùng Đồng Tháp Mười. Năm đầu tiên bác trồng thử nghiệm một giống cây ăn trái mới và thu hoạch được $N$ quả. Nhờ áp dụng kỹ thuật chăm sóc tiên tiến, mỗi năm tiếp theo sản lượng lại tăng gấp đôi so với năm trước. Bác muốn dự đoán sản lượng thu hoạch sau đúng một năm tới để lên kế hoạch bán hàng cho đại lý.

Nhiệm vụ: Nhập số nguyên $N$ từ bàn phím. In ra giá trị gấp đôi của $N$ (tức $N \times 2$).

**Đầu vào (Input):**

Một dòng chứa số nguyên $N$ ($0 \le N \le 10^9$).

**Đầu ra (Output):**

In ra giá trị $N \times 2$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 75 | 150 |

**Giải thích:** Gấp đôi của 75 là $75 \times 2 = 150$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là dự đoán sản lượng năm sau gấp đôi năm nay: lấy `N` nhân với 2. Thầy cô kể câu chuyện bác Tư thu hoạch 75 quả năm nay thì năm sau được 150 quả.
- Quy trình gồm hai bước với biến `n` trong lời giải: đọc số `75` vào `n` bằng `int(input())`, rồi tính `n * 2` tức `75 * 2 = 150` và in ra.
- Xử lý biên: ràng buộc cho `N` từ 0 tới `10^9`. Thầy cô cho các con thử giá trị biên `0` cho ra `0`, và giá trị biên `1000000000` cho ra `2000000000` để thấy chương trình vẫn đúng ở hai đầu.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 75)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `n = int(input())` với bàn phím gõ `75` | `n = 75` | (chưa in gì) |
| 2 | `print(n * 2)` tức `print(75 * 2)` | `n = 75` | `150` |
| 3 | Kết thúc chương trình | — | Kết quả cuối cùng: `150`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: quên `int()`, viết `n = input()` rồi `print(n * 2)` thì với mẫu `75` máy hiểu `"75"` là chữ nên lặp chữ hai lần, hiện `7575` thay vì `150`. Cách sửa: viết `n = int(input())`.
- Bẫy 2: in ra `n` mà quên nhân, viết `print(n)` thì với mẫu `75` màn hình hiện `75` thay vì `150`. Cách sửa: viết `print(n * 2)`.
- Bẫy 3: cộng thay vì nhân, viết `print(n + 2)` thì với mẫu `75` màn hình hiện `77` thay vì `150`. Cách sửa: nhớ gấp đôi nghĩa là nhân với 2, viết `n * 2`.

#### 4. Lời giải tham khảo

```python
n = int(input())
print(n * 2)
```

### Bài 06 [pya_l01_p19_in_end_cung_dong]: In không xuống dòng với end

Bối cảnh: Máy tính cần in hai từ ghép thành một khẩu hiệu trên cùng một dòng bằng hai lệnh `print()` riêng biệt.

Nhiệm vụ: Viết chương trình dùng hai lệnh `print()` có tham số `end` để in ra trên một dòng: `Lap trinh rat vui!`

**Đầu vào (Input):**

Không có dữ liệu vào.

**Đầu ra (Output):**

In khẩu hiệu trên một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
|  | Lap trinh rat vui! |

**Giải thích:** Lệnh thứ nhất in `Lap trinh ` có `end=" "`, lệnh thứ hai in `rat vui!`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là ghép khẩu hiệu `Lap trinh rat vui!` từ hai mảnh bằng hai lệnh `print()` nhưng vẫn nằm trên cùng một dòng. Thầy cô giải thích `end=" "` nghĩa là sau khi in xong thì dừng lại bằng một dấu cách thay vì xuống dòng.
- Quy trình gồm hai bước: lệnh thứ nhất `print("Lap trinh", end=" ")` in `Lap trinh` kèm một dấu cách ở cuối và giữ con trỏ ở lại, lệnh thứ hai `print("rat vui!")` in tiếp `rat vui!` ngay sau dấu cách đó, tạo thành `Lap trinh rat vui!`.
- Xử lý biên: bài này không có số liệu vào nên không có giá trị biên. Thầy cô nhắc các con giữ đúng một dấu cách giữa `trinh` và `rat`, vì thiếu dấu cách sẽ dính thành `Lap trinhrat vui!`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: (không có dữ liệu vào))

| Bước | Lệnh chạy | Màn hình hiện ra |
|------|-----------|------------------|
| 1 | `print("Lap trinh", end=" ")` | `Lap trinh ` (con trỏ vẫn ở cùng dòng, chưa xuống dòng) |
| 2 | `print("rat vui!")` | nối tiếp thành `Lap trinh rat vui!` rồi xuống dòng |
| 3 | Kết thúc chương trình | Kết quả cuối cùng: `Lap trinh rat vui!`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: quên `end=" "`, viết hai lệnh `print("Lap trinh")` và `print("rat vui!")` thì màn hình hiện hai dòng rời nhau thay vì một dòng `Lap trinh rat vui!`. Cách sửa: thêm `end=" "` vào lệnh thứ nhất.
- Bẫy 2: viết `end=""` không có dấu cách thì màn hình hiện `Lap trinhrat vui!` bị dính chữ. Cách sửa: viết đúng `end=" "` có một dấu cách ở giữa.
- Bẫy 3: gộp dấu cách sai chỗ, ví dụ `print("Lap trinh ", end=" ")` kèm thêm cách sẽ tạo hai dấu cách liên tiếp thành `Lap trinh  rat vui!`. Cách sửa: chỉ để một dấu cách duy nhất, hoặc trong chữ hoặc trong `end`.

#### 4. Lời giải tham khảo

```python
print("Lap trinh", end=" ")
print("rat vui!")
```

### Bài 07 [pya_l01_p11_hoan_doi_hai_bien]: Hoán đổi vị trí hai biến

Bối cảnh: Hai bạn An và Bình có hai thẻ số mang giá trị $A$ và $B$. Hai bạn muốn đổi thẻ cho nhau.

Nhiệm vụ: Nhập hai số nguyên $A$ và $B$ trên 2 dòng. Thực hiện hoán đổi giá trị của hai biến, sau đó in ra $A$ và $B$ sau khi hoán đổi trên cùng một dòng cách nhau dấu cách.

**Đầu vào (Input):**

Hai dòng chứa hai số nguyên $A$ và $B$ ($-10^9 \le A, B \le 10^9$).

**Đầu ra (Output):**

Một dòng in ra giá trị mới của $A$ và $B$ cách nhau dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 <br>  99 | 99 10 |

**Giải thích:** Ban đầu $A = 10, B = 99$. Sau khi đổi chỗ, $A = 99$ và $B = 10$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là hai bạn An và Bình đổi thẻ cho nhau: thẻ `A = 10` sang tay bạn kia và thẻ `B = 99` sang tay bạn này. Thầy cô ví lệnh `a, b = b, a` như hai bàn tay bắt chéo nhau đổi thẻ cùng một lúc.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `10` vào `a` và `99` vào `b` bằng hai lệnh `int(input())`, đổi chỗ cùng lúc bằng `a, b = b, a` để được `a = 99` và `b = 10`, rồi `print(a, b)` in ra `99 10`.
- Xử lý biên: ràng buộc cho `A, B` từ `-10^9` tới `10^9`. Thầy cô cho các con thử cặp biên `-1000000000` và `1000000000` để thấy lệnh đổi chỗ vẫn đúng cả với số âm.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10 và 99)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input())` với dòng 1 gõ `10` | `a = 10` | (chưa in gì) |
| 2 | `b = int(input())` với dòng 2 gõ `99` | `b = 99` | (chưa in gì) |
| 3 | `a, b = b, a` | `a = 99`, `b = 10` | (chưa in gì) |
| 4 | `print(a, b)` | `a = 99`, `b = 10` | `99 10` |
| 5 | Kết thúc chương trình | — | Kết quả cuối cùng: `99 10`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: đổi từng dòng lệch thứ tự như `a = b` rồi `b = a` thì sau dòng đầu `a` đã thành `99`, dòng sau `b` cũng thành `99` nên in ra `99 99` thay vì `99 10`. Cách sửa: đổi cùng lúc bằng `a, b = b, a`.
- Bẫy 2: quên đổi mà in luôn, viết `print(a, b)` ngay sau khi đọc thì với mẫu `10` và `99` màn hình hiện `10 99` thay vì `99 10`. Cách sửa: thêm dòng `a, b = b, a` trước lệnh in.
- Bẫy 3: in mỗi số một dòng bằng hai lệnh `print(a)` và `print(b)` thì màn hình hiện `99` rồi `10` xuống hai dòng thay vì `99 10` trên một dòng. Cách sửa: viết gọn `print(a, b)` trên một lệnh.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
a, b = b, a
print(a, b)
```

### Bài 08 [pya_l01_p21_tong_hai_so_2_dong]: Tổng hai số nguyên 2 dòng

Bối cảnh: Bạn Minh có $A$ viên bi, bạn Nam có $B$ viên bi. Cần tính tổng số bi của cả hai bạn.

Nhiệm vụ: Nhập hai số nguyên $A$ và $B$ lần lượt trên 2 dòng riêng biệt. In ra tổng $A + B$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $A$ ($0 \le A \le 10^9$).
 - Dòng 2: Số nguyên $B$ ($0 \le B \le 10^9$).

**Đầu ra (Output):**

In ra một số nguyên duy nhất là tổng $A + B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 15 <br>  25 | 40 |

**Giải thích:** Tổng $15 + 25 = 40$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là cộng số bi của Minh và Nam: `A = 15` cộng `B = 25` được `40`. Thầy cô cho các con đếm gộp 15 viên rồi thêm 25 viên nữa.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `15` vào `a`, đọc `25` vào `b`, rồi tính `a + b` tức `15 + 25 = 40` và in ra.
- Xử lý biên: ràng buộc cho `A, B` từ 0 tới `10^9`. Thầy cô cho các con thử cặp biên `0` và `0` cho ra `0`, cặp `1000000000` và `1000000000` cho ra `2000000000` để thấy chương trình vẫn đúng.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 15 và 25)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input())` với dòng 1 gõ `15` | `a = 15` | (chưa in gì) |
| 2 | `b = int(input())` với dòng 2 gõ `25` | `b = 25` | (chưa in gì) |
| 3 | `print(a + b)` tức `print(15 + 25)` | `a = 15`, `b = 25` | `40` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng: `40`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: quên `int()`, viết `a = input()` và `b = input()` rồi `print(a + b)` thì với mẫu `15` và `25` máy nối chữ thành `1525` thay vì `40`. Cách sửa: viết `a = int(input())` và `b = int(input())`.
- Bẫy 2: trừ thay vì cộng, viết `print(a - b)` thì với mẫu `15` và `25` màn hình hiện `-10` thay vì `40`. Cách sửa: nhớ bài hỏi tổng nên viết dấu `+`.
- Bẫy 3: đọc hai số trên một dòng bằng `map(int, input().split())` trong khi đề cho hai dòng riêng thì với mẫu nhập từng số một dòng chương trình sẽ chờ thiếu số. Cách sửa: đọc hai lần `int(input())` cho đúng hai dòng.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
print(a + b)
```

### Bài 09 [pya_l01_p22_hieu_hai_so]: Hiệu hai số nguyên

Bối cảnh: Bác thợ may có cuộn vải dài $A$ mét, đã cắt may hết $B$ mét. Cần tính độ dài vải còn lại.

Nhiệm vụ: Nhập hai số nguyên $A$ và $B$ trên 2 dòng. In ra hiệu $A - B$.

**Đầu vào (Input):**

Hai dòng, mỗi dòng chứa một số nguyên $A, B$ ($0 \le B \le A \le 10^9$).

**Đầu ra (Output):**

In ra số nguyên là kết quả của $A - B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 100 <br>  35 | 65 |

**Giải thích:** Vải còn lại là $100 - 35 = 65$ mét.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tính vải còn lại: cuộn vải dài `A = 100` mét trừ đi `B = 35` mét đã cắt, còn `65` mét. Thầy cô cho các con hình dung cắt bớt một đoạn thì độ dài ngắn lại.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `100` vào `a`, đọc `35` vào `b`, rồi tính `a - b` tức `100 - 35 = 65` và in ra.
- Xử lý biên: ràng buộc cho `0 <= B <= A <= 10^9` nên hiệu không bao giờ âm. Thầy cô cho các con thử cặp biên bằng nhau như `100` và `100` cho ra `0`, và cặp `1000000000` và `0` cho ra `1000000000`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 100 và 35)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input())` với dòng 1 gõ `100` | `a = 100` | (chưa in gì) |
| 2 | `b = int(input())` với dòng 2 gõ `35` | `b = 35` | (chưa in gì) |
| 3 | `print(a - b)` tức `print(100 - 35)` | `a = 100`, `b = 35` | `65` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng: `65`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: viết ngược thứ tự `print(b - a)` thì với mẫu `100` và `35` màn hình hiện `-65` thay vì `65`. Cách sửa: nhớ lấy số lớn trừ số nhỏ, viết `a - b`.
- Bẫy 2: cộng thay vì trừ, viết `print(a + b)` thì với mẫu `100` và `35` màn hình hiện `135` thay vì `65`. Cách sửa: bài hỏi phần còn lại nên viết dấu `-`.
- Bẫy 3: quên `int()` khiến `a - b` báo lỗi vì không trừ được chữ. Cách sửa: viết `a = int(input())` và `b = int(input())`.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
print(a - b)
```

### Bài 10 [pya_l01_p23_tich_hai_so]: Tích hai số nguyên

Bối cảnh: Tại nhà máy sản xuất bánh kẹo xuất khẩu Đại Phát, dây chuyền đóng gói hoạt động tự động theo quy trình nghiêm ngặt. Mỗi thùng carton tiêu chuẩn chứa đúng $A$ hộp sản phẩm, và bên trong mỗi hộp lại được xếp gọn gàng $B$ chiếc kẹo thơm ngon. Trước mỗi ca xuất hàng, hệ thống quản lý kho cần tính toán chính xác tổng số lượng kẹo thực tế có trong một thùng để đối soát với phiếu giao hàng.

Nhiệm vụ: Nhập hai số nguyên $A$ và $B$ trên 2 dòng. In ra tích $A \times B$.

**Đầu vào (Input):**

Hai dòng, mỗi dòng chứa một số nguyên $A, B$ ($0 \le A, B \le 10^4$).

**Đầu ra (Output):**

In ra số nguyên là tích $A \times B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 12 <br>  8 | 96 |

**Giải thích:** Tổng số kẹo là $12 \times 8 = 96$ chiếc.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là đếm kẹo trong một thùng: mỗi thùng có `A = 12` hộp, mỗi hộp có `B = 8` chiếc kẹo, vậy tổng là `12 * 8 = 96` chiếc. Thầy cô cho các con xếp 12 hàng, mỗi hàng 8 chiếc rồi đếm gộp.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `12` vào `a`, đọc `8` vào `b`, rồi tính `a * b` tức `12 * 8 = 96` và in ra.
- Xử lý biên: ràng buộc cho `A, B` từ 0 tới `10^4`. Thầy cô cho các con thử cặp biên `0` và `10000` cho ra `0`, cặp `10000` và `10000` cho ra `100000000` để thấy chương trình vẫn đúng.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12 và 8)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input())` với dòng 1 gõ `12` | `a = 12` | (chưa in gì) |
| 2 | `b = int(input())` với dòng 2 gõ `8` | `b = 8` | (chưa in gì) |
| 3 | `print(a * b)` tức `print(12 * 8)` | `a = 12`, `b = 8` | `96` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng: `96`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: viết dấu nhân toán học `x`, ví dụ `print(a x b)` thì chương trình báo lỗi vì Python chỉ hiểu dấu `*`. Cách sửa: viết `print(a * b)`.
- Bẫy 2: cộng thay vì nhân, viết `print(a + b)` thì với mẫu `12` và `8` màn hình hiện `20` thay vì `96`. Cách sửa: bài hỏi tổng số kẹo trong thùng nên viết dấu `*`.
- Bẫy 3: quên `int()`, viết `a = input()` rồi `print(a * b)` thì với `a` là chữ `"12"` máy lặp chữ, cho ra kết quả lạ thay vì `96`. Cách sửa: viết `a = int(input())` và `b = int(input())`.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
print(a * b)
```

### Bài 11 [pya_l01_p04_cap_so_nhan_doi]: Cặp số nhân đôi

Bối cảnh: Trong module xử lý tín hiệu số, mạch khuếch đại nhận một tín hiệu đầu vào có biên độ $A$ và nhân đôi biên độ đó lên gấp 2 lần.

Nhiệm vụ: Nhập vào số nguyên $A$. Hãy tính và in ra giá trị của tín hiệu sau khi nhân đôi ($A \times 2$).

**Đầu vào (Input):**

Gồm một số tự nhiên $A$ ($0 \le A \le 10^6$).

**Đầu ra (Output):**

In ra một số nguyên là kết quả nhân đôi ($A \times 2$).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 15 | 30 |

**Giải thích:** Giá trị đầu vào là $15$. Khi nhân đôi, ta có: $15 \times 2 = 30$. Do đó, kết quả in ra màn hình là `30`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 0 | 0 |

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là mạch khuếch đại nhân đôi biên độ tín hiệu: vào `A = 15` thì ra `15 * 2 = 30`. Thầy cô ví như tiếng loa được vặn to gấp đôi.
- Quy trình gồm hai bước với biến `a` trong lời giải: đọc `15` vào `a` bằng `int(input().strip())` (có gọt khoảng trắng thừa quanh số), rồi tính `a * 2` tức `30` và in ra.
- Xử lý biên: ràng buộc cho `A` từ 0 tới `10^6`. Thầy cô cho các con thử giá trị biên `0` cho ra `0`, và giá trị biên `1000000` cho ra `2000000`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 15)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input().strip())` với bàn phím gõ `15` | `a = 15` | (chưa in gì) |
| 2 | `print(a * 2)` tức `print(15 * 2)` | `a = 15` | `30` |
| 3 | Kết thúc chương trình | — | Kết quả cuối cùng: `30`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: quên `int()`, viết `a = input().strip()` rồi `print(a * 2)` thì với mẫu `15` máy lặp chữ hai lần, hiện `1515` thay vì `30`. Cách sửa: viết `a = int(input().strip())`.
- Bẫy 2: viết `print(a + 2)` thì với mẫu `15` màn hình hiện `17` thay vì `30`. Cách sửa: nhân đôi nghĩa là nhân với 2, viết `a * 2`.
- Bẫy 3: viết `print(a * a)` (bình phương) thì với mẫu `15` màn hình hiện `225` thay vì `30`. Cách sửa: chỉ nhân với số 2 cố định.

#### 4. Lời giải tham khảo

```python
a = int(input().strip())
print(a * 2)
```

### Bài 12 [pya_l01_p18_tuoi_cua_be_sau_5_nam]: Tuổi của bé sau 5 năm

Bối cảnh: Trong hệ thống quản lý hồ sơ nhân khẩu học, độ tuổi của một đối tượng được tính toán và dự đoán theo các mốc thời gian trong tương lai.

Nhiệm vụ: Cho số tuổi hiện tại $N$ ($1 \le N \le 12$). Hãy tính và in ra số tuổi của người đó sau 5 năm nữa.

**Đầu vào (Input):**

Một dòng duy nhất chứa số tự nhiên $N$ ($1 \le N \le 12$).

**Đầu ra (Output):**

Một số nguyên duy nhất là số tuổi của Bo sau 5 năm.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 8 | 13 |

**Giải thích:** Học sinh 8 tuổi, sau 5 năm nữa nhỏ: $8 + 5 = 13$ tuổi

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là dự đoán tuổi sau 5 năm nữa: lấy tuổi hiện tại `N = 8` cộng thêm 5 được `13`. Thầy cô cho các con giơ 8 ngón tay rồi đếm thêm 5 nữa.
- Quy trình gồm hai bước với biến `n` trong lời giải: đọc `8` vào `n` bằng `int(input().strip())`, rồi tính `n + 5` tức `8 + 5 = 13` và in ra.
- Xử lý biên: ràng buộc cho `N` từ 1 tới 12. Thầy cô cho các con thử giá trị biên `1` cho ra `6`, và giá trị biên `12` cho ra `17`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 8)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `n = int(input().strip())` với bàn phím gõ `8` | `n = 8` | (chưa in gì) |
| 2 | `print(n + 5)` tức `print(8 + 5)` | `n = 8` | `13` |
| 3 | Kết thúc chương trình | — | Kết quả cuối cùng: `13`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: nhân thay vì cộng, viết `print(n * 5)` thì với mẫu `8` màn hình hiện `40` thay vì `13`. Cách sửa: tuổi tăng theo năm nên viết dấu `+`, tức `n + 5`.
- Bẫy 2: cộng sai số năm, viết `print(n + 3)` thì với mẫu `8` màn hình hiện `11` thay vì `13`. Cách sửa: đề hỏi sau 5 năm nên cộng đúng số 5.
- Bẫy 3: quên `int()`, viết `n = input().strip()` rồi `print(n + 5)` thì chương trình báo lỗi vì không cộng chữ với số được. Cách sửa: viết `n = int(input().strip())`.

#### 4. Lời giải tham khảo

```python
n = int(input().strip())
print(n + 5)
```

### Bài 13 [pya_l01_p12_chuc_sinh_nhat]: Lời chúc sinh nhật cá nhân hóa

Bối cảnh: Bạn muốn viết một chương trình in ra thiệp chúc mừng sinh nhật theo tên và tuổi của bạn bè.

Nhiệm vụ: Nhập dòng 1 là tên bạn (chuỗi ký tự), dòng 2 là số tuổi $T$ (số nguyên). In ra dòng chữ: `Chuc mung sinh nhat <Ten>, ban tron <Tuoi> tuoi!`

**Đầu vào (Input):**

- Dòng 1: Chuỗi ký tự không dấu $Ten$.
 - Dòng 2: Số nguyên $Tuoi$ ($1 \le Tuoi \le 100$).

**Đầu ra (Output):**

In ra câu chúc đúng mẫu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| Nam <br>  10 | Chuc mung sinh nhat Nam, ban tron 10 tuoi! |

**Giải thích:** Ghép tên và tuổi vào đúng vị trí của câu chúc.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là điền tên và tuổi vào khung thiệp mẫu: `Chuc mung sinh nhat <Ten>, ban tron <Tuoi> tuoi!`. Với mẫu thì tên là `Nam` và tuổi là `10`.
- Quy trình gồm ba bước với hai biến `ten` và `tuoi` trong lời giải: đọc chuỗi `"Nam"` vào `ten` bằng `input()` (giữ nguyên chữ, không đổi sang số), đọc `10` vào `tuoi` bằng `int(input())`, rồi dùng chuỗi `f"..."` để ghép cả hai vào đúng vị trí trong câu chúc.
- Xử lý biên: ràng buộc cho tuổi từ 1 tới 100. Thầy cô cho các con thử tuổi biên `1` cho ra `... ban tron 1 tuoi!` và tuổi biên `100` cho ra `... ban tron 100 tuoi!`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Nam và 10)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `ten = input()` với dòng 1 gõ `Nam` | `ten = "Nam"` | (chưa in gì) |
| 2 | `tuoi = int(input())` với dòng 2 gõ `10` | `tuoi = 10` | (chưa in gì) |
| 3 | `print(f"Chuc mung sinh nhat {ten}, ban tron {tuoi} tuoi!")` | `ten = "Nam"`, `tuoi = 10` | `Chuc mung sinh nhat Nam, ban tron 10 tuoi!` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng đúng như dòng trên. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: đổi tuổi sang số sai cách, viết `tuoi = input()` không có `int()` thì khi ghép vẫn hiện đúng `10`, nhưng nếu sau này tính toán sẽ bị nối chữ. Cách sửa: viết `tuoi = int(input())`.
- Bẫy 2: quên dấu phẩy hoặc dấu chấm than trong mẫu, ví dụ in `Chuc mung sinh nhat Nam ban tron 10 tuoi` thì thiếu dấu `,` sau tên và thiếu `!` cuối câu nên bị tính là kết quả sai. Cách sửa: sao chép đúng mẫu `..., ban tron ... tuoi!`.
- Bẫy 3: dùng dấu cộng để ghép mà quên đổi số thành chữ, ví dụ `"... tron " + tuoi + " tuoi!"` thì chương trình báo lỗi vì không cộng chữ với số được. Cách sửa: dùng chuỗi `f"..."` như trong lời giải.

#### 4. Lời giải tham khảo

```python
ten = input()
tuoi = int(input())
print(f"Chuc mung sinh nhat {ten}, ban tron {tuoi} tuoi!")
```

### Bài 14 [pya_l01_p07_chiec_hop_hoan_doi_bi_mat]: Chiếc hộp hoán đổi bí mật

Bối cảnh: Giờ ra chơi, bạn Tèo có hai chiếc hộp xinh xắn: hộp $A$ đựng số kẹo của Tèo, hộp $B$ đựng số kẹo của Tí. Hai bạn cười khúc khích và đố nhau đổi kẹo cho nhau (số kẹo trong hộp $A$ chuyển sang hộp $B$, và số kẹo trong hộp $B$ chuyển sang hộp $A$). Cả hai loay hoay mãi chưa đổi xong. Hãy giúp hai bạn hoán đổi hai hộp kẹo này.

Nhiệm vụ: Nhập vào 2 số nguyên $A$ và $B$. Hãy hoán đổi giá trị của 2 biến và in ra giá trị mới của $A$ và $B$ sau khi hoán đổi (cách nhau một dấu cách).

**Đầu vào (Input):**

Dòng 1 chứa số $A$, dòng 2 chứa số $B$ ($0 \le A, B \le 10^9$).

**Đầu ra (Output):**

In ra hai số $A$ và $B$ sau khi hoán đổi trên cùng một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 7 <br> 12 | 12 7 |

**Giải thích:** Ban đầu $A=7, B=12$. Sau khi đổi: $A=12, B=7$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là hai hộp kẹo đổi chỗ cho nhau: hộp `A = 7` và hộp `B = 12`, sau khi đổi thì `A = 12` và `B = 7`. Thầy cô kể chuyện Tèo và Tí đổi kẹo để các con dễ nhớ.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `7` vào `a` và `12` vào `b` bằng `int(input().strip())`, đổi chỗ cùng lúc bằng `a, b = b, a`, rồi `print(a, b)` in ra `12 7`.
- Xử lý biên: ràng buộc cho `A, B` từ 0 tới `10^9`. Thầy cô cho các con thử cặp biên `0` và `1000000000` để thấy lệnh đổi chỗ vẫn đúng.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 7 và 12)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input().strip())` với dòng 1 gõ `7` | `a = 7` | (chưa in gì) |
| 2 | `b = int(input().strip())` với dòng 2 gõ `12` | `b = 12` | (chưa in gì) |
| 3 | `a, b = b, a` | `a = 12`, `b = 7` | (chưa in gì) |
| 4 | `print(a, b)` | `a = 12`, `b = 7` | `12 7` |
| 5 | Kết thúc chương trình | — | Kết quả cuối cùng: `12 7`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: gán lần lượt `a = b` rồi `b = a` thì sau dòng đầu `a` đã thành `12`, dòng sau `b` cũng thành `12` nên in ra `12 12` thay vì `12 7`. Cách sửa: đổi cùng lúc bằng `a, b = b, a`.
- Bẫy 2: quên dòng đổi chỗ, đọc xong in ngay thì với mẫu `7` và `12` màn hình hiện `7 12` thay vì `12 7`. Cách sửa: thêm dòng `a, b = b, a` trước lệnh in.
- Bẫy 3: in mỗi số một dòng bằng hai lệnh `print(a)` và `print(b)` thì màn hình hiện hai dòng thay vì `12 7` trên một dòng. Cách sửa: viết gọn `print(a, b)`.

#### 4. Lời giải tham khảo

```python
a = int(input().strip())
b = int(input().strip())
a, b = b, a
print(a, b)
```

### Bài 15 [pya_l01_p17_tam_danh_thiep_thong_minh]: Tấm danh thiếp thông minh

Bối cảnh: Hệ thống quản lý thông tin hội thảo cần in thẻ danh thiếp tự động cho người tham dự sau khi nhập tên.

Nhiệm vụ: Nhập vào tên của một người (chuỗi ký tự). Hãy in ra thông điệp chào mừng theo mẫu: `Xin chao ban [Ten]!`

**Đầu vào (Input):**

Một dòng duy nhất chứa chuỗi ký tự tên của người dùng.

**Đầu ra (Output):**

In ra dòng thông điệp: `Xin chao ban <Ten>!` (giữa chữ `ban` và tên cách nhau một dấu cách, cuối câu có dấu chấm than `!`).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| Nam | Xin chao ban Nam! |

**Giải thích:** Với tên nhập vào là `"Nam"`, chương trình ghép chuỗi `"Xin chao ban "` với `"Nam"` và thêm dấu chấm than `!` ở cuối, tạo thành dòng chữ `Xin chao ban Nam!`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| Bao Anh | Xin chao ban Bao Anh! |

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là ghép tên người tham dự vào mẫu `Xin chao ban [Ten]!`. Với mẫu thì tên là `Nam` nên kết quả là `Xin chao ban Nam!`.
- Quy trình gồm hai bước với biến `ten` trong lời giải: đọc chuỗi `"Nam"` vào `ten` bằng `input().strip()` (có gọt khoảng trắng thừa ở hai đầu), rồi dùng phép cộng chuỗi `"Xin chao ban " + ten + "!"` để nối ba mảnh lại thành câu hoàn chỉnh.
- Xử lý biên: tên là chuỗi ký tự bất kỳ, có thể dài như mẫu thứ hai `Bao Anh` cho ra `Xin chao ban Bao Anh!`. Thầy cô nhắc các con giữ đúng một dấu cách sau chữ `ban` và dấu `!` ở cuối.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Nam)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `ten = input().strip()` với bàn phím gõ `Nam` | `ten = "Nam"` | (chưa in gì) |
| 2 | `print("Xin chao ban " + ten + "!")` tức ghép `"Xin chao ban "` với `"Nam"` và `"!"` | `ten = "Nam"` | `Xin chao ban Nam!` |
| 3 | Kết thúc chương trình | — | Kết quả cuối cùng: `Xin chao ban Nam!`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: đổi tên sang số bằng `ten = int(input())` thì với mẫu `Nam` chương trình báo lỗi vì `Nam` không phải số. Cách sửa: tên là chữ nên chỉ viết `ten = input().strip()`.
- Bẫy 2: quên dấu cách sau chữ `ban`, viết `"Xin chao ban" + ten + "!"` thì với mẫu `Nam` màn hình hiện `Xin chao banNam!` bị dính chữ. Cách sửa: viết `"Xin chao ban "` có một dấu cách ở cuối.
- Bẫy 3: quên dấu chấm than cuối câu, in ra `Xin chao ban Nam` thay vì `Xin chao ban Nam!` nên bị tính là kết quả sai. Cách sửa: cộng thêm `"!"` ở cuối.

#### 4. Lời giải tham khảo

```python
ten = input().strip()
print("Xin chao ban " + ten + "!")
```

### Bài 16 [pya_l01_p06_cua_hang_banh_ran]: Cửa hàng bánh rán

Bối cảnh: Hệ thống máy tính tiền tự động tại căng-tin cần tính tổng giá trị hóa đơn khi khách hàng mua nhiều sản phẩm cùng loại với đơn giá cố định.

Nhiệm vụ: Nhập vào đơn giá mỗi sản phẩm $a$ (nghìn đồng) và số lượng sản phẩm $b$. Hãy tính tổng số tiền (nghìn đồng) cần thanh toán.

**Đầu vào (Input):**

Nhập vào 2 số tự nhiên $a$ và $b$ mỗi số trên một dòng ($1 \le a \le 100, 1 \le b \le 100$).

**Đầu ra (Output):**

In ra số tiền Doraemon cần trả.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 12 <br> 5 | 60 |

**Giải thích:** Mua 5 chiếc bánh, mỗi chiếc 12 nghìn đồng: $12 \times 5 = 60$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tính tiền hóa đơn: đơn giá `a = 12` nghìn đồng nhân với số lượng `b = 5` được `60` nghìn đồng. Thầy cô cho các con hình dung mua 5 chiếc bánh, mỗi chiếc 12 nghìn.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `12` vào `a` và `5` vào `b` bằng `int(input().strip())`, rồi tính `a * b` tức `12 * 5 = 60` và in ra.
- Xử lý biên: ràng buộc cho `a, b` từ 1 tới 100. Thầy cô cho các con thử cặp biên `1` và `1` cho ra `1`, cặp `100` và `100` cho ra `10000`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12 và 5)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input().strip())` với dòng 1 gõ `12` | `a = 12` | (chưa in gì) |
| 2 | `b = int(input().strip())` với dòng 2 gõ `5` | `b = 5` | (chưa in gì) |
| 3 | `print(a * b)` tức `print(12 * 5)` | `a = 12`, `b = 5` | `60` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng: `60`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: cộng thay vì nhân, viết `print(a + b)` thì với mẫu `12` và `5` màn hình hiện `17` thay vì `60`. Cách sửa: tiền hóa đơn bằng đơn giá nhân số lượng, viết `a * b`.
- Bẫy 2: quên `int()`, viết `a = input().strip()` rồi `print(a * b)` thì máy lặp chữ, cho ra kết quả lạ thay vì `60`. Cách sửa: viết `a = int(input().strip())` và `b = int(input().strip())`.
- Bẫy 3: đọc hai số trên một dòng bằng `map(int, input().split())` trong khi đề cho hai dòng riêng thì chương trình sẽ chờ thiếu số. Cách sửa: đọc hai lần `int(input().strip())` cho đúng hai dòng.

#### 4. Lời giải tham khảo

```python
a = int(input().strip())
b = int(input().strip())
print(a * b)
```

### Bài 17 [pya_l01_p15_phep_nhan_bang]: In bảng phép nhân cơ bản

Bối cảnh: Học sinh học bảng nhân muốn in một dòng phép tính dạng `A x B = C` thật đẹp mắt.

Nhiệm vụ: Nhập hai số nguyên $A$ và $B$ trên 2 dòng. In ra chính xác theo định dạng: `A x B = C` (với $C = A \times B$).

**Đầu vào (Input):**

Hai dòng, dòng 1 là $A$, dòng 2 là $B$ ($1 \le A, B \le 100$).

**Đầu ra (Output):**

In ra dòng phép tính theo đúng mẫu, các thành phần cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 7 <br>  9 | 7 x 9 = 63 |

**Giải thích:** Tính $7 \times 9 = 63$ và in theo mẫu `7 x 9 = 63`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là trình bày phép nhân theo đúng khung `A x B = C`: với mẫu `A = 7` và `B = 9` thì `C = 63`, in ra `7 x 9 = 63`. Thầy cô nhắc chữ `x` ở đây là chữ cái, không phải dấu nhân.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `7` vào `a` và `9` vào `b` bằng `int(input())`, rồi tính `a * b` tức `63` và dùng chuỗi `f"{a} x {b} = {a * b}"` để đặt ba con số vào đúng vị trí trong khung.
- Xử lý biên: ràng buộc cho `A, B` từ 1 tới 100. Thầy cô cho các con thử cặp biên `1` và `1` cho ra `1 x 1 = 1`, cặp `100` và `100` cho ra `100 x 100 = 10000`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 7 và 9)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input())` với dòng 1 gõ `7` | `a = 7` | (chưa in gì) |
| 2 | `b = int(input())` với dòng 2 gõ `9` | `b = 9` | (chưa in gì) |
| 3 | `print(f"{a} x {b} = {a * b}")` tức ghép `7`, `9`, `63` vào khung | `a = 7`, `b = 9` | `7 x 9 = 63` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng: `7 x 9 = 63`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: chỉ in kết quả `print(a * b)` thì với mẫu `7` và `9` màn hình hiện `63` thay vì `7 x 9 = 63`. Cách sửa: in cả khung bằng `print(f"{a} x {b} = {a * b}")`.
- Bẫy 2: dùng dấu `*` trong khung, viết `f"{a} * {b} = {a * b}"` thì với mẫu màn hình hiện `7 * 9 = 63` thay vì `7 x 9 = 63`. Cách sửa: trong khung hiển thị dùng chữ `x` thường.
- Bẫy 3: quên dấu cách quanh chữ `x` và dấu `=`, in ra `7x9=63` dính liền nên bị tính là kết quả sai. Cách sửa: giữ đúng mẫu `{a} x {b} = {kết quả}` với dấu cách hai bên.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
print(f"{a} x {b} = {a * b}")
```

### Bài 18 [pya_l01_p09_tong_hai_so_cung_dong]: Tổng hai số trên cùng 1 dòng

Bối cảnh: Trong đề thi chuẩn, hai số $A$ và $B$ thường được nhập trên cùng 1 dòng ngăn cách bởi dấu cách.

Nhiệm vụ: Nhập hai số nguyên $A, B$ trên cùng một dòng. In ra tổng $A + B$.

**Đầu vào (Input):**

Một dòng duy nhất chứa hai số nguyên $A$ và $B$ cách nhau một dấu cách ($-10^9 \le A, B \le 10^9$).

**Đầu ra (Output):**

In ra tổng $A + B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 45 55 | 100 |

**Giải thích:** Đọc bằng `map(int, input().split())` và in ra $45 + 55 = 100$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là cộng hai số `A = 45` và `B = 55` nằm chung trên một dòng, kết quả `45 + 55 = 100`. Thầy cô giải thích cả dòng `"45 55"` được cắt thành hai mảnh tại dấu cách rồi mới đổi sang số.
- Quy trình gồm hai bước với hai biến `a` và `b` trong lời giải: dùng `map(int, input().split())` để cắt dòng `45 55` thành `45` và `55` rồi cất vào `a` và `b`, sau đó `print(a + b)` in ra `100`.
- Xử lý biên: ràng buộc cho `A, B` từ `-10^9` tới `10^9`. Thầy cô cho các con thử cặp biên `-1000000000 -1000000000` cho ra `-2000000000`, và cặp `1000000000 1000000000` cho ra `2000000000`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 45 55)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a, b = map(int, input().split())` với bàn phím gõ `45 55` | `a = 45`, `b = 55` | (chưa in gì) |
| 2 | `print(a + b)` tức `print(45 + 55)` | `a = 45`, `b = 55` | `100` |
| 3 | Kết thúc chương trình | — | Kết quả cuối cùng: `100`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: đọc bằng hai lệnh `int(input())` riêng thì sau dòng `45 55` dòng đầu đã nuốt cả hai số và dòng thứ hai không còn gì để đọc, chương trình cứ chờ thêm. Cách sửa: đọc một dòng rồi cắt bằng `map(int, input().split())`.
- Bẫy 2: quên đổi sang số, viết `a, b = input().split()` rồi `print(a + b)` thì với mẫu `45 55` máy nối chữ thành `4555` thay vì `100`. Cách sửa: bọc `map(int, ...)` để đổi cả hai mảnh thành số.
- Bẫy 3: trừ thay vì cộng, viết `print(a - b)` thì với mẫu `45 55` màn hình hiện `-10` thay vì `100`. Cách sửa: bài hỏi tổng nên viết dấu `+`.

#### 4. Lời giải tham khảo

```python
a, b = map(int, input().split())
print(a + b)
```

### Bài 19 [pya_l01_p20_doi_thuoc_ke_milimet]: Đổi thước kẻ milimet

Bối cảnh: Trong thiết kế cơ khí chính xác, kích thước của chi tiết gia công gồm phần kích thước chẵn $a\text{ cm}$ và phần sai số dư $b\text{ mm}$.

Nhiệm vụ: Cho biết $1\text{ cm} = 10\text{ mm}$. Hãy quy đổi toàn bộ độ dài gồm $a\text{ cm}$ và $b\text{ mm}$ sang đơn vị milimet ($\text{mm}$).

**Đầu vào (Input):**

* Dòng 1: Chứa số tự nhiên $a$ ($1 \le a \le 1000$).
 * Dòng 2: Chứa số tự nhiên $b$ ($1 \le b \le 1000$).

**Đầu ra (Output):**

Một số tự nhiên duy nhất là độ dài của thước tính theo đơn vị milimet ($\text{mm}$).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 2 <br> 5 | 25 |

**Giải thích:** $2\text{ cm} = 20\text{ mm}$. Tổng cộng là: $20 + 5 = 25\text{ mm}$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là đổi đơn vị độ dài: `1 cm = 10 mm` nên `a = 2` cm chính là `20` mm, cộng thêm `b = 5` mm được `25` mm. Thầy cô cho các con đổi thước kẻ thật trên bàn để hình dung.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `2` vào `a` và `5` vào `b` bằng `int(input().strip())`, rồi tính `a * 10 + b` tức `2 * 10 + 5 = 25` và in ra.
- Xử lý biên: ràng buộc cho `a, b` từ 1 tới 1000. Thầy cô cho các con thử cặp biên `1` và `1` cho ra `11`, cặp `1000` và `1000` cho ra `11000`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2 và 5)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input().strip())` với dòng 1 gõ `2` | `a = 2` | (chưa in gì) |
| 2 | `b = int(input().strip())` với dòng 2 gõ `5` | `b = 5` | (chưa in gì) |
| 3 | `print(a * 10 + b)` tức `print(2 * 10 + 5)` | `a = 2`, `b = 5` | `25` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng: `25`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: quên đổi cm sang mm, viết `print(a + b)` thì với mẫu `2` và `5` màn hình hiện `7` thay vì `25`. Cách sửa: nhân phần cm với 10 trước, viết `a * 10 + b`.
- Bẫy 2: nhân sai số đổi, viết `print(a * 100 + b)` thì với mẫu `2` và `5` màn hình hiện `205` thay vì `25`. Cách sửa: nhớ `1 cm = 10 mm` nên chỉ nhân với 10.
- Bẫy 3: in hai kết quả trên hai dòng như `print(a * 10)` rồi `print(b)` thì màn hình hiện `20` rồi `5` thay vì `25` trên một dòng. Cách sửa: cộng gộp rồi in một lần bằng `print(a * 10 + b)`.

#### 4. Lời giải tham khảo

```python
a = int(input().strip())
b = int(input().strip())
print(a * 10 + b)
```

### Bài 20 [pya_l01_p14_ghep_ngay_thang_nam]: Ghép ngày tháng năm định dạng chuẩn

Bối cảnh: Hệ thống cần nhận 3 số nguyên là Ngày, Tháng, Năm và in ra dạng chuẩn hiển thị trên lịch.

Nhiệm vụ: Nhập 3 số nguyên $D, M, Y$ trên cùng một dòng. In ra theo định dạng: `D/M/Y`.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên $D, M, Y$ cách nhau dấu cách ($1 \le D \le 31$, $1 \le M \le 12$, $1900 \le Y \le 2100$).

**Đầu ra (Output):**

In ra dạng `D/M/Y`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 4 9 2026 | 4/9/2026 |

**Giải thích:** Tận dụng lệnh `print(d, m, y, sep="/")`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là xếp ba con số ngày `D = 4`, tháng `M = 9`, năm `Y = 2026` thành lịch chuẩn `4/9/2026`, với dấu gạch chéo `/` nằm giữa các số. Thầy cô ví dấu `/` như vách ngăn giữa ba ô lịch.
- Quy trình gồm hai bước với ba biến `d`, `m`, `y` trong lời giải: dùng `map(int, input().split())` để cắt dòng `4 9 2026` thành `4`, `9`, `2026` rồi cất vào `d`, `m`, `y`, sau đó `print(d, m, y, sep="/")` đặt dấu `/` vào giữa các số và in ra `4/9/2026`.
- Xử lý biên: ràng buộc cho ngày từ 1 tới 31, tháng từ 1 tới 12, năm từ 1900 tới 2100. Thầy cô cho các con thử biên `1 1 1900` cho ra `1/1/1900` và `31 12 2100` cho ra `31/12/2100`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 9 2026)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `d, m, y = map(int, input().split())` với bàn phím gõ `4 9 2026` | `d = 4`, `m = 9`, `y = 2026` | (chưa in gì) |
| 2 | `print(d, m, y, sep="/")` | `d = 4`, `m = 9`, `y = 2026` | `4/9/2026` |
| 3 | Kết thúc chương trình | — | Kết quả cuối cùng: `4/9/2026`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: quên `sep="/"`, viết `print(d, m, y)` thì với mẫu `4 9 2026` màn hình hiện `4 9 2026` với dấu cách thay vì `4/9/2026`. Cách sửa: thêm `sep="/"` vào lệnh `print`.
- Bẫy 2: dùng dấu nối sai, ví dụ `print(d, m, y, sep="-")` thì màn hình hiện `4-9-2026` thay vì `4/9/2026`. Cách sửa: dùng đúng dấu gạch chéo `"/"`.
- Bẫy 3: đọc bằng ba lệnh `int(input())` riêng trong khi đề cho cả ba số trên một dòng thì chương trình sẽ chờ thiếu số sau khi đã gõ `4 9 2026`. Cách sửa: đọc một dòng rồi cắt bằng `map(int, input().split())`.

#### 4. Lời giải tham khảo

```python
d, m, y = map(int, input().split())
print(d, m, y, sep="/")
```

### Bài 21 [pya_l01_p08_doan_tau_toa_xe_ghep_so]: Đoàn tàu toa xe ghép số

Bối cảnh: Sáng sớm ở ga xe lửa, có 2 toa xe chở 2 con số $a$ và $b$ vừa chạy vào sân ga. Bác trưởng ga vui tính muốn nhìn thấy cả hai kết quả:
 1. Nếu ghép 2 toa tàu lại thành một dãy số (Ghép chữ).
 2. Nếu cộng giá trị của 2 toa tàu lại với nhau (Cộng số học).
Bác loay hoay mãi với cuốn sổ ghi chép. Hãy giúp bác trưởng ga làm cả hai việc này.

Nhiệm vụ: Nhập vào 2 số tự nhiên $a$ và $b$. Dòng 1 in ra kết quả khi ghép chuỗi chữ. Dòng 2 in ra kết quả khi cộng số.

**Đầu vào (Input):**

Nhập 2 số tự nhiên $a, b$ ($1 \le a, b \le 100$) trên 2 dòng.

**Đầu ra (Output):**

* Dòng 1: Chuỗi ghép dính $a$ và $b$.
 * Dòng 2: Tổng giá trị số học $a + b$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 25 <br> 30 | 2530 <br> 55 |

**Giải thích:** Dòng 1 ghép chữ: `"25" + "30" = "2530"`.
Dòng 2 cộng số: $25 + 30 = 55$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là phân biệt chữ với số: hai toa `a = 25` và `b = 30` khi ghép chữ cho ra `2530`, khi cộng số cho ra `55`. Thầy cô ví ghép chữ như nối hai toa tàu lại, còn cộng số như đổ kẹo hai toa vào chung một hộp.
- Quy trình gồm ba bước với hai biến `s1` và `s2` trong lời giải: đọc nguyên văn hai dòng `"25"` vào `s1` và `"30"` vào `s2` bằng `input().strip()` (giữ dạng chữ), dòng 1 in `s1 + s2` tức `"25" + "30" = "2530"`, dòng 2 in `int(s1) + int(s2)` tức `25 + 30 = 55`.
- Xử lý biên: ràng buộc cho `a, b` từ 1 tới 100. Thầy cô cho các con thử cặp biên `1` và `1` cho ra dòng 1 là `11` và dòng 2 là `2`, cặp `100` và `100` cho ra `100100` và `200`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 25 và 30)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `s1 = input().strip()` với dòng 1 gõ `25` | `s1 = "25"` | (chưa in gì) |
| 2 | `s2 = input().strip()` với dòng 2 gõ `30` | `s2 = "30"` | (chưa in gì) |
| 3 | `print(s1 + s2)` tức `print("25" + "30")` | `s1 = "25"`, `s2 = "30"` | `2530` |
| 4 | `print(int(s1) + int(s2))` tức `print(25 + 30)` | `s1 = "25"`, `s2 = "30"` | `55` |
| 5 | Kết thúc chương trình | — | Kết quả cuối cùng đúng hai dòng `2530` và `55`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: đổi sang số ngay từ đầu bằng `s1 = int(input())` thì dòng ghép `s1 + s2` với mẫu `25` và `30` sẽ tính `25 + 30 = 55` ở cả hai dòng, mất dòng `2530`. Cách sửa: giữ nguyên chữ bằng `input().strip()`, chỉ đổi sang số ở dòng cộng.
- Bẫy 2: quên đổi sang số ở dòng hai, viết `print(s1 + s2)` hai lần thì cả hai dòng đều hiện `2530`, mất dòng `55`. Cách sửa: dòng hai viết `print(int(s1) + int(s2))`.
- Bẫy 3: in hai kết quả trên một dòng như `print(s1 + s2, int(s1) + int(s2))` thì màn hình hiện `2530 55` chung một dòng thay vì hai dòng riêng. Cách sửa: viết hai lệnh `print` riêng cho hai dòng.

#### 4. Lời giải tham khảo

```python
s1 = input().strip()
s2 = input().strip()
print(s1 + s2)
print(int(s1) + int(s2))
```

### Bài 22 [pya_l01_p16_chenh_lech_tuoi]: Chênh lệch tuổi của hai anh em

Bối cảnh: Anh hơn em một số tuổi. Biết tuổi của anh là $A$ và tuổi của em là $E$. Cần tính số tuổi anh hơn em và in câu thông báo.

Nhiệm vụ: Nhập hai số nguyên $A$ và $E$ trên cùng 1 dòng ($1 \le E \le A \le 100$). In ra một dòng có nội dung: `Anh hon em <so_tuoi> tuoi.`

**Đầu vào (Input):**

Một dòng chứa hai số nguyên $A$ và $E$ cách nhau dấu cách.

**Đầu ra (Output):**

In ra câu kết luận đúng mẫu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 12 7 | Anh hon em 5 tuoi. |

**Giải thích:** Hiệu số tuổi $12 - 7 = 5$. In ra `Anh hon em 5 tuoi.`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tính anh hơn em bao nhiêu tuổi: tuổi anh `A = 12` trừ tuổi em `E = 7` được `5`, rồi đặt số `5` vào khung câu `Anh hon em 5 tuoi.`. Thầy cô cho các con đếm từ 7 lên 12 xem chênh mấy tuổi.
- Quy trình gồm hai bước với hai biến `a` và `e` trong lời giải: dùng `map(int, input().split())` để cắt dòng `12 7` thành `12` và `7` rồi cất vào `a` và `e`, sau đó dùng chuỗi `f"Anh hon em {a - e} tuoi."` để tính `12 - 7 = 5` và ghép vào câu.
- Xử lý biên: ràng buộc cho `1 <= E <= A <= 100` nên anh luôn lớn tuổi hơn hoặc bằng em. Thầy cô cho các con thử biên bằng nhau `100 100` cho ra `Anh hon em 0 tuoi.`, và biên `100 1` cho ra `Anh hon em 99 tuoi.`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12 7)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a, e = map(int, input().split())` với bàn phím gõ `12 7` | `a = 12`, `e = 7` | (chưa in gì) |
| 2 | `print(f"Anh hon em {a - e} tuoi.")` tức tính `12 - 7 = 5` rồi ghép vào câu | `a = 12`, `e = 7` | `Anh hon em 5 tuoi.` |
| 3 | Kết thúc chương trình | — | Kết quả cuối cùng: `Anh hon em 5 tuoi.`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: chỉ in hiệu `print(a - e)` thì với mẫu `12 7` màn hình hiện `5` thay vì `Anh hon em 5 tuoi.` nên bị tính là kết quả sai. Cách sửa: in cả câu bằng `print(f"Anh hon em {a - e} tuoi.")`.
- Bẫy 2: trừ ngược `e - a` thì với mẫu `12 7` câu hiện `Anh hon em -5 tuoi.` có số âm lạ. Cách sửa: nhớ anh trừ em, viết `a - e`.
- Bẫy 3: quên dấu chấm cuối câu, in ra `Anh hon em 5 tuoi` thiếu dấu `.` nên bị tính là kết quả sai. Cách sửa: sao chép đúng mẫu có dấu chấm ở cuối.

#### 4. Lời giải tham khảo

```python
a, e = map(int, input().split())
print(f"Anh hon em {a - e} tuoi.")
```

### Bài 23 [pya_l01_p13_bon_phep_tinh]: Bốn phép tính đồng thời

Bối cảnh: Máy tính cầm tay cần hiển thị bảng kết quả 3 phép tính cơ bản giữa hai số nguyên.

Nhiệm vụ: Nhập hai số nguyên $A$ và $B$ trên cùng 1 dòng. In ra 3 dòng:

**Đầu vào (Input):**

Một dòng chứa hai số nguyên $A$ và $B$ cách nhau dấu cách ($-10^4 \le A, B \le 10^4$).

**Đầu ra (Output):**

3 dòng lần lượt chứa tổng, hiệu và tích.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 8 5 | 13 <br> 3 <br> 40 |

**Giải thích:** $8 + 5 = 13$, $8 - 5 = 3$, $8 \times 5 = 40$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là từ hai số `A = 8` và `B = 5` tính ra ba kết quả: tổng `8 + 5 = 13`, hiệu `8 - 5 = 3`, tích `8 * 5 = 40`, mỗi kết quả nằm trên một dòng. Thầy cô ví như máy tính bỏ túi bấm một lần hiện đủ ba đáp số.
- Quy trình gồm hai bước với hai biến `a` và `b` trong lời giải: dùng `map(int, input().split())` để cắt dòng `8 5` thành `8` và `5` rồi cất vào `a` và `b`, sau đó in ba dòng `print(a + b)`, `print(a - b)`, `print(a * b)` cho ra `13`, `3`, `40`.
- Xử lý biên: ràng buộc cho `A, B` từ `-10^4` tới `10^4`. Thầy cô cho các con thử cặp biên `-10000 -10000` cho ra `-20000`, `0`, `100000000`, và cặp `10000 10000` cho ra `20000`, `0`, `100000000`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 8 5)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a, b = map(int, input().split())` với bàn phím gõ `8 5` | `a = 8`, `b = 5` | (chưa in gì) |
| 2 | `print(a + b)` tức `print(8 + 5)` | `a = 8`, `b = 5` | `13` |
| 3 | `print(a - b)` tức `print(8 - 5)` | `a = 8`, `b = 5` | `3` |
| 4 | `print(a * b)` tức `print(8 * 5)` | `a = 8`, `b = 5` | `40` |
| 5 | Kết thúc chương trình | — | Kết quả cuối cùng đúng ba dòng `13`, `3`, `40`. |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: in cả ba kết quả trên một dòng như `print(a + b, a - b, a * b)` thì với mẫu `8 5` màn hình hiện `13 3 40` chung một dòng thay vì ba dòng riêng. Cách sửa: viết ba lệnh `print` riêng.
- Bẫy 2: sai thứ tự các dòng, ví dụ in tích trước tổng thì ba dòng hiện `40`, `3`, `13` bị đảo chỗ. Cách sửa: giữ đúng thứ tự tổng rồi hiệu rồi tích.
- Bẫy 3: quên `int()` khi cắt dòng, viết `a, b = input().split()` rồi `print(a + b)` thì với mẫu `8 5` máy nối chữ thành `85` thay vì `13`. Cách sửa: bọc `map(int, ...)` để đổi thành số.

#### 4. Lời giải tham khảo

```python
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
```

### Bài 24 [pya_l01_p10_co_may_thoi_gian_3_the_he]: Cỗ máy thời gian 3 thế hệ

Bối cảnh: Trong bài toán phân tích nhân khẩu học, tuổi của ba thành viên trong một gia đình thuộc ba thế hệ liên tiếp được ghi nhận.

Nhiệm vụ: Cho số tuổi của người con là $a$, người bố hơn con $b$ tuổi, và người ông hơn bố $c$ tuổi. Hãy tính tuổi của bố, tuổi của ông và tổng tuổi của cả ba người.

**Đầu vào (Input):**

Ba dòng lần lượt chứa 3 số nguyên $a, b, c$ ($1 \le a \le 20, 20 \le b \le 40, 20 \le c \le 40$).

**Đầu ra (Output):**

Gồm 3 dòng tương ứng với 3 yêu cầu của bài toán.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 <br> 30 <br> 25 | 40 <br> 65 <br> 115 |

**Giải thích:** - Tuổi Nam: $10$.
- Tuổi Bố: $10 + 30 = 40$.
- Tuổi Ông: $40 + 25 = 65$.
- Tổng cả 3 người: $10 + 40 + 65 = 115$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tính tuổi ba thế hệ dây chuyền: con `a = 10`, bố hơn con `b = 30` nên bố `10 + 30 = 40`, ông hơn bố `c = 25` nên ông `40 + 25 = 65`, tổng cả ba là `10 + 40 + 65 = 115`. Thầy cô vẽ cây gia đình ba tầng để các con dễ thấy.
- Quy trình gồm bốn bước với các biến `a`, `b`, `c`, `tuoi_bo`, `tuoi_ong` trong lời giải: đọc `10` vào `a`, `30` vào `b`, `25` vào `c`, tính `tuoi_bo = a + b = 40`, tính `tuoi_ong = tuoi_bo + c = 65`, rồi in ba dòng `40`, `65`, `115`.
- Xử lý biên: ràng buộc cho `a` từ 1 tới 20, `b` và `c` từ 20 tới 40. Thầy cô cho các con thử biên nhỏ `1, 20, 20` cho ra `21`, `41`, `63`, và biên lớn `20, 40, 40` cho ra `60`, `100`, `180`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10, 30 và 25)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input())` với dòng 1 gõ `10` | `a = 10` | (chưa in gì) |
| 2 | `b = int(input())` với dòng 2 gõ `30` | `b = 30` | (chưa in gì) |
| 3 | `c = int(input())` với dòng 3 gõ `25` | `c = 25` | (chưa in gì) |
| 4 | `tuoi_bo = a + b` tức `10 + 30` | `tuoi_bo = 40` | (chưa in gì) |
| 5 | `tuoi_ong = tuoi_bo + c` tức `40 + 25` | `tuoi_ong = 65` | (chưa in gì) |
| 6 | `print(tuoi_bo)` | — | `40` |
| 7 | `print(tuoi_ong)` | — | `65` |
| 8 | `print(a + tuoi_bo + tuoi_ong)` tức `10 + 40 + 65` | — | `115` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: tính tuổi ông từ tuổi con, viết `tuoi_ong = a + c` thì với mẫu `10, 30, 25` tuổi ông ra `35` thay vì `65`. Cách sửa: ông hơn bố nên viết `tuoi_ong = tuoi_bo + c`.
- Bẫy 2: tính tổng sai, viết `print(a + b + c)` thì với mẫu màn hình hiện `65` thay vì `115` vì đó chỉ là tổng các khoảng chênh. Cách sửa: tổng ba người là `a + tuoi_bo + tuoi_ong`.
- Bẫy 3: in cả ba tuổi trên một dòng như `print(tuoi_bo, tuoi_ong, ...)` thì màn hình hiện `40 65 115` chung một dòng thay vì ba dòng riêng. Cách sửa: viết ba lệnh `print` riêng.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
c = int(input())
tuoi_bo = a + b
tuoi_ong = tuoi_bo + c
print(tuoi_bo)
print(tuoi_ong)
print(a + tuoi_bo + tuoi_ong)
```

### Bài 25 [pya_l01_p24_ve_tham_quan_chua_huong]: Vé tham quan chùa hương

Bối cảnh: Cuối tuần này, một đoàn khách nhỏ chuẩn bị đi tham quan Chùa Hương Tích. Để lên chùa, đoàn phải đi thuyền rồi đi cáp treo ngắm cảnh núi rừng:
 * Vé thuyền: người lớn $a$ nghìn đồng/người, trẻ em $b$ nghìn đồng/người.
 * Vé cáp treo: người lớn $x$ nghìn đồng/người, trẻ em $y$ nghìn đồng/người.
 * Đoàn khách có tổng cộng $n$ người, trong đó có $m$ trẻ em.
Cô hướng dẫn viên cần tính tiền để mua vé cho cả đoàn. Hãy giúp cô tính tổng số tiền cần chuẩn bị.

Nhiệm vụ: Hãy tính tổng số tiền (đơn vị nghìn đồng) cần chuẩn bị để mua toàn bộ vé thuyền và vé cáp treo cho cả đoàn khách.

**Đầu vào (Input):**

Gồm 6 dòng lần lượt chứa các số tự nhiên: $a, b, x, y, n, m$ ($0 < a, b, x, y < 100$; $0 \le m \le n < 100$).

**Đầu ra (Output):**

In ra một số nguyên duy nhất là tổng số tiền cần chuẩn bị.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 20 <br> 10 <br> 50 <br> 30 <br> 10 <br> 4 | 580 |

**Giải thích:** - Số trẻ em: $4$, số người lớn: $10 - 4 = 6$ người.
- Tiền thuyền: $6 \times 20 + 4 \times 10 = 120 + 40 = 160$.
- Tiền cáp treo: $6 \times 50 + 4 \times 30 = 300 + 120 = 420$.
- Tổng tiền: $160 + 420 = 580$ nghìn đồng.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là cộng tiền vé thuyền và vé cáp treo cho cả đoàn: đoàn `n = 10` người gồm `m = 4` trẻ em nên có `6` người lớn. Vé thuyền người lớn `a = 20`, trẻ em `b = 10`; vé cáp treo người lớn `x = 50`, trẻ em `y = 30`. Tiền thuyền là `6 * 20 + 4 * 10 = 160`, tiền cáp treo là `6 * 50 + 4 * 30 = 420`, tổng là `580`.
- Quy trình với các biến `a, b, x, y, n, m, so_tre_em, so_nguoi_lon, tong_tien` trong lời giải: đọc sáu số `20, 10, 50, 30, 10, 4` vào `a, b, x, y, n, m`, tính `so_tre_em = 4` và `so_nguoi_lon = 10 - 4 = 6`, rồi tính `tong_tien = 6 * (20 + 50) + 4 * (10 + 30) = 6 * 70 + 4 * 40 = 420 + 160 = 580` và in ra.
- Xử lý biên: ràng buộc cho vé từ 0 tới 100, đoàn `0 <= m <= n < 100`. Thầy cô cho các con thử trường hợp đặc biệt đoàn toàn trẻ em như `n = 5, m = 5` thì số người lớn là `0`, và đoàn không ai `n = 0, m = 0` thì tổng tiền là `0`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 20, 10, 50, 30, 10 và 4)

| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | Đọc 6 dòng `20, 10, 50, 30, 10, 4` vào `a, b, x, y, n, m` | `a = 20`, `b = 10`, `x = 50`, `y = 30`, `n = 10`, `m = 4` | (chưa in gì) |
| 2 | `so_tre_em = m` | `so_tre_em = 4` | (chưa in gì) |
| 3 | `so_nguoi_lon = n - m` tức `10 - 4` | `so_nguoi_lon = 6` | (chưa in gì) |
| 4 | `tong_tien = 6 * (20 + 50) + 4 * (10 + 30)` tức `420 + 160` | `tong_tien = 580` | (chưa in gì) |
| 5 | `print(tong_tien)` | — | `580` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: lấy nhầm `n` làm số người lớn, viết `tong_tien = n * (a + x) + m * (b + y)` thì với mẫu cho ra `10 * 70 + 4 * 40 = 860` thay vì `580` vì đếm trùng 4 trẻ em. Cách sửa: tính `so_nguoi_lon = n - m` rồi mới nhân.
- Bẫy 2: chỉ tính một loại vé, ví dụ `tong_tien = so_nguoi_lon * a + so_tre_em * b` thì với mẫu chỉ ra `160` (tiền thuyền), thiếu `420` tiền cáp treo. Cách sửa: mỗi người phải cộng cả hai vé, viết `(a + x)` và `(b + y)`.
- Bẫy 3: đọc sai thứ tự sáu số, ví dụ đọc `n` trước `a` thì mọi biến lệch hết và tổng ra số lạ thay vì `580`. Cách sửa: đọc đúng thứ tự đề cho là `a, b, x, y, n, m` mỗi số một dòng.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
x = int(input())
y = int(input())
n = int(input())
m = int(input())
so_tre_em = m
so_nguoi_lon = n - m
tong_tien = so_nguoi_lon * (a + x) + so_tre_em * (b + y)
print(tong_tien)
```

### Bài 01 [pya_l02_p02_luy_thua_bac_hai]: Lũy thừa bậc hai

Bối cảnh: Trong buổi học toán về hình học không gian, cô giáo Lan yêu cầu học sinh tính diện tích của một mặt bàn hình vuông có cạnh dài $A$ xen-ti-mét. Công thức diện tích hình vuông chính là $A^2$ — hay còn gọi là "bình phương" của $A$. Em hãy giúp các bạn viết chương trình tự động hóa phép tính này để kiểm tra đáp số nhanh chóng.

Nhiệm vụ: Nhập số nguyên $N$. In ra giá trị bình phương $N^2$ bằng cách dùng toán tử `**`.

**Đầu vào (Input):**

Một dòng chứa số nguyên $N$ ($-10^4 \le N \le 10^4$).

**Đầu ra (Output):**

In ra $N^2$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 8 | 64 |

**Giải thích:** $8^2 = 64$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là bình phương: với `n = 8` thì `n ** 2 = 8 ** 2 = 64`, chính là diện tích hình vuông cạnh `8`.
- Quy trình trong lời giải: đọc `n` từ một dòng duy nhất rồi in `n ** 2`; không cần biến phụ, không cần vòng lặp.
- Xử lý biên: `n = 0` cho `0`; `n = -10^4` cho `100000000` (số âm bình phương thành số dương); `n = 10^4` cho `100000000`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 8)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `n` nhận giá trị | `n = 8` |
| 2 | Tính `n ** 2` | `8 ** 2 = 64` |
| 3 | In kết quả | `64` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Dùng `n * 2` thay vì `n ** 2`.**

```python
print(n * 2)
```

Với số liệu mẫu trên, đoạn này cho `n = 8` in ra `16` thay vì `64`.

Cách sửa: dùng `n ** 2` hoặc `n * n`.

**Bẫy 2: Dùng `n ^ 2` (tưởng là mũ).**

```python
print(n ^ 2)
```

Với số liệu mẫu trên, đoạn này cho `n = 8` thì `8 ^ 2 = 10` vì `^` là phép khác, không phải lũy thừa.

Cách sửa: toán tử mũ trong Python là `**`.

#### 4. Lời giải tham khảo

```python
n = int(input())
print(n ** 2)
```

### Bài 02 [pya_l02_p03_lap_phuong]: Lập phương của một số

Bối cảnh: Xưởng gia công gỗ nghệ thuật Phú Quý nhận được đơn đặt hàng một lô hộp quà tặng cao cấp hình lập phương. Mỗi hộp có cạnh dài đúng $A$ xen-ti-mét. Để ước lượng nguyên vật liệu và chi phí vận chuyển, bộ phận kỹ thuật cần tính chính xác thể tích bên trong mỗi chiếc hộp. Em hãy lập trình tính thể tích khối lập phương với cạnh cho trước.

Nhiệm vụ: Nhập số nguyên dương $A$. In ra giá trị $A^3$.

**Đầu vào (Input):**

Một dòng chứa số nguyên $A$ ($1 \le A \le 1000$).

**Đầu ra (Output):**

In ra $A^3$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 5 | 125 |

**Giải thích:** $5^3 = 125$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là lập phương thể tích: với `a = 5` thì `a ** 3 = 5 ** 3 = 125`, là thể tích hộp cạnh `5`.
- Quy trình trong lời giải: đọc `a` từ một dòng rồi in `a ** 3`; phép `** 3` nhân `a` ba lần với nhau.
- Xử lý biên: `a = 1` cho `1`; `a = 1000` cho `1000000000`; đề cho `a` dương nên không lo số âm.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `a` nhận giá trị | `a = 5` |
| 2 | Tính `a ** 3` | `5 ** 3 = 125` |
| 3 | In kết quả | `125` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Dùng `a * 3` thay vì `a ** 3`.**

```python
print(a * 3)
```

Với số liệu mẫu trên, đoạn này cho `a = 5` in ra `15` thay vì `125`.

Cách sửa: dùng `a ** 3`.

**Bẫy 2: Dùng `a ^ 3`.**

```python
print(a ^ 3)
```

Với số liệu mẫu trên, đoạn này cho `a = 5` thì `5 ^ 3 = 6`, hoàn toàn khác `125`.

Cách sửa: toán tử mũ là `**`.

#### 4. Lời giải tham khảo

```python
a = int(input())
print(a ** 3)
```

### Bài 03 [pya_l02_p04_chu_so_tan_cung]: Lấy chữ số tận cùng

Bối cảnh: Tại hội chợ Xuân, mỗi du khách được phát một tấm vé số may mắn mang một số nguyên dương. Theo luật chơi, giải thưởng phụ thuộc vào chữ số cuối cùng (hàng đơn vị) của tấm vé: nếu tận cùng là 0 hoặc 5 thì trúng quà, còn lại thì không. Hệ thống cần trích xuất chính xác chữ số hàng đơn vị từ số trên tấm vé để tự động phân loại trúng thưởng.

Nhiệm vụ: Nhập số nguyên dương $N$. In ra chữ số hàng đơn vị của $N$.

**Đầu vào (Input):**

Một dòng chứa số nguyên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

In ra chữ số tận cùng của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 2026 | 6 |

**Giải thích:** $2026 \% 10 = 6$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là tách hàng đơn vị bằng phép dư cho `10`: với `n = 2026` thì `2026 % 10 = 6`.
- Quy trình trong lời giải: đọc `n` rồi in `n % 10`; chỉ một phép tính duy nhất.
- Xử lý biên: `n = 1` cho `1`; `n = 10^9 = 1000000000` cho `0`; số tròn chục luôn cho chữ số tận cùng là `0`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2026)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `n` nhận giá trị | `n = 2026` |
| 2 | Tính `n % 10` | `2026 % 10 = 6` |
| 3 | In kết quả | `6` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Dùng `n // 10` (xóa chữ số cuối) thay vì `% 10`.**

```python
print(n // 10)
```

Với số liệu mẫu trên, đoạn này cho `2026` in ra `202` thay vì `6`.

Cách sửa: dùng `n % 10`.

**Bẫy 2: In cả số `n` ra.**

```python
print(n)
```

Với số liệu mẫu trên, đoạn này cho số liệu mẫu in ra `2026` thay vì `6`.

Cách sửa: chỉ in `n % 10`.

#### 4. Lời giải tham khảo

```python
n = int(input())
print(n % 10)
```

### Bài 04 [pya_l02_p09_hai_chu_so_cuoi]: Lấy hai chữ số tận cùng

Bối cảnh: Để xét giải khuyến khích số may mắn, người ta cần lấy 2 chữ số tận cùng của mã vé.

Nhiệm vụ: Nhập số nguyên $N$ ($N \ge 100$). In ra giá trị của hai chữ số tận cùng của $N$.

**Đầu vào (Input):**

Một dòng chứa số nguyên $N$ ($100 \le N \le 10^9$).

**Đầu ra (Output):**

In ra số tạo bởi 2 chữ số cuối (Ví dụ: `2026` in ra `26`, `105` in ra `5`).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 1945 | 45 |

**Giải thích:** $1945 \% 100 = 45$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là lấy khối 2 chữ số cuối bằng dư cho `100`: với `n = 1945` thì `1945 % 100 = 45`.
- Quy trình trong lời giải: đọc `n` rồi in `n % 100`; ví dụ `105 % 100 = 5` nên số `105` in ra `5`.
- Xử lý biên: `n = 100` cho `0`; `n = 10^9 = 1000000000` cho `0`; `n = 2026` cho `26`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1945)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `n` nhận giá trị | `n = 1945` |
| 2 | Tính `n % 100` | `1945 % 100 = 45` |
| 3 | In kết quả | `45` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Dùng `% 10` chỉ lấy một chữ số.**

```python
print(n % 10)
```

Với số liệu mẫu trên, đoạn này cho `1945` in ra `5` thay vì `45`.

Cách sửa: dùng `n % 100`.

**Bẫy 2: Dùng `n // 100` (lấy phần đầu).**

```python
print(n // 100)
```

Với số liệu mẫu trên, đoạn này cho `1945` in ra `19` thay vì `45`.

Cách sửa: dùng `n % 100`.

#### 4. Lời giải tham khảo

```python
n = int(input())
print(n % 100)
```

### Bài 05 [pya_l02_p11_bieu_thuc_bac_nhat]: Giá trị biểu thức bậc nhất

Bối cảnh: Trong bài kiểm tra toán học cuối kỳ, đề thi yêu cầu học sinh tính giá trị của hàm số bậc nhất $y = 3x + 5$ tại nhiều điểm $x$ khác nhau. Thay vì tính bằng tay từng trường hợp, bạn Linh nảy ra ý tưởng viết một chương trình Python để tự động hóa: chỉ cần nhập giá trị $x$, máy sẽ trả về ngay kết quả $y$ tương ứng. Em hãy giúp Linh hoàn thành chương trình này.

Nhiệm vụ: Nhập số nguyên $x$. In ra giá trị của $y = 3x + 5$.

**Đầu vào (Input):**

Một dòng chứa số nguyên $x$ ($-10^6 \le x \le 10^6$).

**Đầu ra (Output):**

In ra giá trị của biểu thức.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 4 | 17 |

**Giải thích:** $3 \times 4 + 5 = 17$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là hàm bậc nhất: với `x = 4` thì `3 * 4 + 5 = 12 + 5 = 17`.
- Quy trình trong lời giải: đọc `x` rồi in `3 * x + 5`; phép nhân thực hiện trước phép cộng theo đúng quy tắc tính.
- Xử lý biên: `x = -10^6` cho `-2999995`; `x = 10^6` cho `3000005`; `x = 0` cho `5`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `x` nhận giá trị | `x = 4` |
| 2 | Tính `3 * x` | `3 * 4 = 12` |
| 3 | Cộng `5` | `12 + 5 = 17` |
| 4 | In kết quả | `17` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Viết `3 * (x + 5)` thêm ngoặc sai.**

```python
print(3 * (x + 5))
```

Với số liệu mẫu trên, đoạn này cho `x = 4` cho `27` thay vì `17`.

Cách sửa: viết `3 * x + 5`.

**Bẫy 2: Viết `3 * x + 5` thiếu dấu nhân kiểu toán học `3x + 5`.**

```python
print(3x + 5)
```

Với số liệu mẫu trên, đoạn này cho Chương trình báo lỗi cú pháp, không chạy được với `4`.

Cách sửa: luôn viết dấu `*` giữa `3` và `x`.

#### 4. Lời giải tham khảo

```python
x = int(input())
print(3 * x + 5)
```

### Bài 06 [pya_l02_p25_xoa_chu_so_cuoi]: Xóa chữ số tận cùng

Bối cảnh: Bạn Hùng đang nhập liệu bảng thống kê sĩ số các lớp trên máy tính thì vô tình bấm thêm một chữ số thừa ở cuối. Thay vì nhập $12$ thì Hùng đã gõ thành $123$. May mắn thay, thao tác "xóa lùi" sẽ loại bỏ chữ số cuối cùng và trả lại số ban đầu. Em hãy mô phỏng thao tác này bằng chương trình: cho một số nguyên dương, hãy trả về số mới sau khi xóa đi chữ số cuối cùng.

Nhiệm vụ: Nhập số nguyên dương $N$ ($N \ge 10$). In ra số $N$ sau khi đã cắt bỏ chữ số hàng đơn vị.

**Đầu vào (Input):**

Một dòng chứa số nguyên $N$ ($10 \le N \le 10^9$).

**Đầu ra (Output):**

In ra số $N$ sau khi bỏ chữ số cuối.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3458 | 345 |

**Giải thích:** $3458 // 10 = 345$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là cắt hàng đơn vị bằng chia nguyên cho `10`: với `n = 3458` thì `3458 // 10 = 345`.
- Quy trình trong lời giải: đọc `n` rồi in `n // 10`; một phép tính duy nhất.
- Xử lý biên: `n = 10` cho `1`; `n = 10^9 = 1000000000` cho `100000000`; số có hai chữ số luôn còn lại một chữ số.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3458)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `n` nhận giá trị | `n = 3458` |
| 2 | Tính `n // 10` | `3458 // 10 = 345` |
| 3 | In kết quả | `345` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Dùng `% 10` (lấy chữ số cuối) thay vì xóa.**

```python
print(n % 10)
```

Với số liệu mẫu trên, đoạn này cho `3458` in ra `8` thay vì `345`.

Cách sửa: dùng `n // 10`.

**Bẫy 2: Dùng chia thực `/`.**

```python
print(n / 10)
```

Với số liệu mẫu trên, đoạn này cho `3458` in ra `345.8` thay vì `345`.

Cách sửa: dùng `//`.

#### 4. Lời giải tham khảo

```python
n = int(input())
print(n // 10)
```

### Bài 07 [pya_l02_p28_xep_ban_hoc]: Xếp hàng vào bàn học

Bối cảnh: Phòng thi Olympic Tin học cấp thành phố được bố trí toàn bộ bàn đôi — mỗi bàn ngồi đúng 2 thí sinh. Năm nay có $N$ thí sinh đăng ký dự thi. Ban tổ chức cần tính toán số lượng bàn tối thiểu phải chuẩn bị sao cho tất cả thí sinh đều có chỗ ngồi, kể cả trường hợp số thí sinh là số lẻ thì bàn cuối cùng vẫn phải kê ra dù chỉ ngồi 1 người.

Nhiệm vụ: Có $N$ bạn thí sinh. Hỏi cần ít nhất bao nhiêu bàn đôi để tất cả các bạn đều có chỗ ngồi? (Nếu lẻ 1 bạn vẫn cần thêm 1 bàn).

**Đầu vào (Input):**

Một dòng chứa số nguyên dương $N$ ($1 \le N \le 10^6$).

**Đầu ra (Output):**

In ra số bàn học tối thiểu cần dùng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 15 | 8 |

**Giải thích:** 15 bạn xếp được 7 bàn đôi đầy đủ, còn 1 bạn ngồi riêng 1 bàn $\implies$ Cần 8 bàn. Công thức: `(N + 1) // 2`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là mỗi bàn ngồi `2` bạn, bạn lẻ vẫn cần một bàn: với `n = 15` thì `(15 + 1) // 2 = 16 // 2 = 8` bàn; `7` bàn đầy và `1` bàn cho bạn còn lại.
- Quy trình trong lời giải: đọc `n` rồi in `(n + 1) // 2`.
- Xử lý biên: `n = 1` cho `1`; `n = 2` cho `1`; `n = 10^6` (chẵn) cho `500000`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 15)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `n` nhận giá trị | `n = 15` |
| 2 | Tính `n + 1` | `15 + 1 = 16` |
| 3 | Chia nguyên `16 // 2` | `8` |
| 4 | In kết quả | `8` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Dùng `n // 2` (bỏ bạn lẻ).**

```python
print(n // 2)
```

Với số liệu mẫu trên, đoạn này cho `15` cho `7` thay vì `8`, còn `1` bạn không có chỗ.

Cách sửa: dùng `(n + 1) // 2`.

**Bẫy 2: Dùng chia thực `n / 2`.**

```python
print(n / 2)
```

Với số liệu mẫu trên, đoạn này cho `15` in ra `7.5` thay vì `8`.

Cách sửa: dùng công thức làm tròn lên với `//`.

#### 4. Lời giải tham khảo

```python
n = int(input())
print((n + 1) // 2)
```

### Bài 08 [pya_l02_p13_luy_thua_cau_thang]: Lũy thừa cầu thang

Bối cảnh: Bạn Thỏ Nâu rất thích xếp các khối gỗ thành một chiếc cầu thang toán học. Tầng đầu tiên cần $a$ khối gỗ, mỗi tầng tiếp theo lại gấp $a$ lần số khối của tầng trước đó. Thỏ Nâu đếm được chiếc cầu thang của mình có tất cả $n$ tầng. Hãy giúp bạn Thỏ tính xem tầng cao nhất có bao nhiêu khối gỗ.

Nhiệm vụ: Cho hai số nguyên $a$ và $n$, em hãy tính giá trị lũy thừa $a^n$.

**Đầu vào (Input):**

Gồm 2 dòng, mỗi dòng một số nguyên: dòng đầu là cơ số $a$, dòng sau là số mũ $n$ ($1 \le a \le 10$, $0 \le n \le 10$).

**Đầu ra (Output):**

In ra một số nguyên duy nhất là giá trị của $a^n$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3 <br> 4 | 81 |

**Giải thích:** $3^4 = 3 \times 3 \times 3 \times 3 = 81$. Tầng cao nhất của cầu thang có 81 khối gỗ.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là lũy thừa tổng quát: với `a = 3`, `n = 4` thì `3 ** 4 = 81`, tức tầng cao nhất có `81` khối gỗ.
- Quy trình trong lời giải: đọc `a` dòng 1, đọc `n` dòng 2, rồi in `a ** n`.
- Xử lý biên: `n = 0` luôn cho `1` (ví dụ `10 ** 0 = 1`); `a = 1` luôn cho `1`; `a = 10, n = 10` cho `10000000000`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 và 4 (hai dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc dòng 1, biến `a` nhận giá trị | `a = 3` |
| 2 | Đọc dòng 2, biến `n` nhận giá trị | `n = 4` |
| 3 | Tính `a ** n` | `3 ** 4 = 81` |
| 4 | In kết quả | `81` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Dùng `a ^ n`.**

```python
print(a ^ n)
```

Với số liệu mẫu trên, đoạn này cho `3` và `4` cho `7` thay vì `81`.

Cách sửa: toán tử mũ là `**`.

**Bẫy 2: Dùng `a * n`.**

```python
print(a * n)
```

Với số liệu mẫu trên, đoạn này cho `3` và `4` cho `12` thay vì `81`.

Cách sửa: dùng `a ** n`.

#### 4. Lời giải tham khảo

```python
a = int(input())
n = int(input())
print(a ** n)
```

### Bài 09 [pya_l02_p07_dong_hop_banh]: Đóng hộp bánh ngọt

Bối cảnh: Xưởng bánh Hương Quê vừa sản xuất xong một mẻ gồm $M$ chiếc bánh quy bơ thơm ngon. Theo quy cách đóng gói, mỗi hộp quà tặng chứa cố định đúng 6 chiếc bánh. Bộ phận kho vận cần biết chính xác hai thông tin: cần bao nhiêu hộp đầy đủ để đóng gói, và sau khi đóng xong thì còn dư bao nhiêu chiếc bánh lẻ chưa đủ một hộp.

Nhiệm vụ: Nhập số nguyên dương $M$. In ra số hộp bánh đóng được đầy đủ và số bánh lẻ còn sót lại.

**Đầu vào (Input):**

Một dòng chứa số nguyên $M$ ($1 \le M \le 10^6$).

**Đầu ra (Output):**

Hai số nguyên cách nhau một dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 50 | 8 2 |

**Giải thích:** $50 // 6 = 8$ hộp, dư $50 \% 6 = 2$ bánh lẻ.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là đóng hộp 6 chiếc: với `m = 50` thì số hộp đầy `50 // 6 = 8`, bánh lẻ `50 % 6 = 2`.
- Quy trình trong lời giải: đọc `m` rồi in một dòng `print(m // 6, m % 6)` cho ra `8 2`.
- Xử lý biên: `m = 1` cho `0 1`; `m = 6` cho `1 0`; `m = 10^6` cho `166666 4`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 50)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `m` nhận giá trị | `m = 50` |
| 2 | Tính số hộp `m // 6` | `50 // 6 = 8` |
| 3 | Tính bánh lẻ `m % 6` | `50 % 6 = 2` |
| 4 | In một dòng hai số | `8 2` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: In hai số xuống hai dòng.**

```python
print(m // 6)
print(m % 6)
```

Với số liệu mẫu trên, đoạn này cho `50` in ra `8` rồi `2` xuống hai dòng thay vì `8 2` một dòng.

Cách sửa: in chung một lệnh `print(m // 6, m % 6)`.

**Bẫy 2: Nhầm số bánh mỗi hộp thành `5`.**

```python
print(m // 5, m % 5)
```

Với số liệu mẫu trên, đoạn này cho `50` in ra `10 0` thay vì `8 2`.

Cách sửa: mỗi hộp đúng `6` chiếc.

#### 4. Lời giải tham khảo

```python
m = int(input())
print(m // 6, m % 6)
```

### Bài 10 [pya_l02_p10_chu_so_hang_chuc]: Chữ số hàng chục

Bối cảnh: Tại trạm kiểm soát tốc độ trên quốc lộ, camera ghi nhận biển số xe dưới dạng một số nguyên. Để phân loại phương tiện theo nhóm, hệ thống cần trích xuất chữ số ở hàng chục (vị trí thứ hai từ phải sang) của số đó. Ví dụ: số $1234$ có chữ số hàng chục là $3$, số $507$ có chữ số hàng chục là $0$. Em hãy lập trình giải quyết bài toán trích xuất này.

Nhiệm vụ: Nhập số nguyên $N$ ($N \ge 10$). In ra chữ số hàng chục của $N$.

**Đầu vào (Input):**

Một dòng chứa số nguyên $N$ ($10 \le N \le 10^9$).

**Đầu ra (Output):**

In ra chữ số hàng chục.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 378 | 7 |

**Giải thích:** Bỏ chữ số tận cùng: $378 // 10 = 37$. Lấy chữ số cuối của 37: $37 \% 10 = 7$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là gọt chữ số cuối rồi lấy tận cùng: với `n = 378` thì `378 // 10 = 37`, rồi `37 % 10 = 7`.
- Quy trình trong lời giải: đọc `n` rồi in `(n // 10) % 10`; cặp ngoặc bảo đảm chia trước dư sau.
- Xử lý biên: `n = 10` cho `1`; `n = 507` cho `0`; `n = 10^9` cho `0`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 378)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `n` nhận giá trị | `n = 378` |
| 2 | Bỏ chữ số cuối `n // 10` | `378 // 10 = 37` |
| 3 | Lấy tận cùng `37 % 10` | `7` |
| 4 | In kết quả | `7` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Chỉ lấy tận cùng `n % 10`.**

```python
print(n % 10)
```

Với số liệu mẫu trên, đoạn này cho `378` in ra `8` thay vì `7`.

Cách sửa: dùng `(n // 10) % 10`.

**Bẫy 2: Quên ngoặc, viết `n // 10 % 10` sai thứ tự trong đầu nhưng Python vẫn đúng — bẫy thật là `n // (10 % 10)`.**

```python
print(n // (10 % 10))
```

Với số liệu mẫu trên, đoạn này cho `378` gây lỗi chia cho `0` thay vì ra `7`.

Cách sửa: viết `(n // 10) % 10`.

#### 4. Lời giải tham khảo

```python
n = int(input())
print((n // 10) % 10)
```

### Bài 11 [pya_l02_p14_doi_phut_ra_gio_phut]: Đổi phút ra giờ phút

Bối cảnh: Bạn Mèo Cam vừa bấm giờ chạy bộ quanh công viên và chiếc đồng hồ chỉ tổng cộng $T$ phút. Mèo Cam muốn khoe với cả lớp rằng mình đã chạy được mấy giờ mấy phút cho thật oai. Nhưng bạn ấy chỉ biết cộng trừ đơn giản, chưa biết cách đổi phút ra giờ. Hãy giúp Mèo Cam đổi số phút thành giờ và phút.

Nhiệm vụ: Cho tổng số phút $T$, em hãy tính số giờ trọn vẹn và số phút còn lẻ.

**Đầu vào (Input):**

Một số nguyên duy nhất $T$ trên một dòng ($0 \le T \le 10000$).

**Đầu ra (Output):**

In ra hai số nguyên trên một dòng cách nhau một dấu cách: số giờ và số phút còn dư.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 135 | 2 15 |

**Giải thích:** $135$ phút $= 2$ giờ trọn vẹn ($2 \times 60 = 120$ phút) và còn dư $135 - 120 = 15$ phút.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là tách giờ và phút lẻ khỏi tổng phút: với `t = 135` thì giờ `135 // 60 = 2`, phút dư `135 % 60 = 15`.
- Quy trình trong lời giải: đọc `t` rồi in một dòng `print(t // 60, t % 60)` cho ra `2 15`.
- Xử lý biên: `t = 0` cho `0 0`; `t = 60` cho `1 0`; `t = 10000` cho `166 40`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 135)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `t` nhận giá trị | `t = 135` |
| 2 | Tính giờ `t // 60` | `135 // 60 = 2` |
| 3 | Tính phút dư `t % 60` | `135 % 60 = 15` |
| 4 | In một dòng | `2 15` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Chia cho `100` thay vì `60`.**

```python
print(t // 100, t % 100)
```

Với số liệu mẫu trên, đoạn này cho `135` cho `1 35` thay vì `2 15`.

Cách sửa: một giờ có `60` phút.

**Bẫy 2: Dùng chia thực `/`.**

```python
print(t / 60, t % 60)
```

Với số liệu mẫu trên, đoạn này cho `135` in ra `2.25 15` thay vì `2 15`.

Cách sửa: dùng `//`.

#### 4. Lời giải tham khảo

```python
t = int(input())
print(t // 60, t % 60)
```

### Bài 12 [pya_l02_p22_nhan_doi_luy_thua]: Nhân đôi lũy thừa

Bối cảnh: Trong mô hình sinh trưởng tế bào vi sinh, số lượng cá thể ban đầu là $1$ và nhân đôi sau mỗi chu kỳ thời gian.

Nhiệm vụ: Cho số nguyên $N$ ($0 \le N \le 30$). Hãy tính số lượng cá thể sau $N$ chu kỳ nhân đôi ($2^N$).

**Đầu vào (Input):**

Một số tự nhiên $n$ ($1 \le n \le 30$).

**Đầu ra (Output):**

In ra số lượng tế bào sau $n$ giờ ($2^n$).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 4 | 16 |

**Giải thích:** Sau 4 giờ: $2^4 = 16$ tế bào.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là lũy thừa của `2`: với `n = 4` thì `2 ** 4 = 16` cá thể sau `4` chu kỳ.
- Quy trình trong lời giải: đọc `n` rồi in `2 ** n`; cơ số cố định là `2`, số mũ là `n`.
- Xử lý biên: `n = 0` cho `1`; `n = 1` cho `2`; `n = 30` cho `1073741824`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `n` nhận giá trị | `n = 4` |
| 2 | Tính `2 ** n` | `2 ** 4 = 16` |
| 3 | In kết quả | `16` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Viết `n ** 2` đảo cơ số và số mũ.**

```python
print(n ** 2)
```

Với số liệu mẫu trên, đoạn này cho `n = 4` cho `16` trùng đáp số nhưng với `n = 5` cho `25` thay vì `32`.

Cách sửa: viết `2 ** n`.

**Bẫy 2: Viết `2 ^ n`.**

```python
print(2 ^ n)
```

Với số liệu mẫu trên, đoạn này cho `n = 4` cho `6` thay vì `16`.

Cách sửa: toán tử mũ là `**`.

#### 4. Lời giải tham khảo

```python
n = int(input().strip())
print(2 ** n)
```

### Bài 13 [pya_l02_p27_vong_chay_dien_kinh]: Vòng chạy điền kinh

Bối cảnh: Hội khỏe trường em tổ chức chạy điền kinh thật vui. Sân vận động có một đường chạy hình chữ nhật có chu vi đúng $100\text{ mét}$. Vận động viên An xuất phát từ vạch số 0 và chạy liên tục theo một chiều dọc theo mép sân được tổng quãng đường là $N\text{ mét}$. Các bạn cổ vũ reo hò mà chưa biết An đã chạy được mấy vòng. Hãy giúp tổ trọng tài tính giúp An.

Nhiệm vụ: Hãy cho biết:
 1. An đã chạy được bao nhiêu vòng sân trọn vẹn?
 2. Hiện tại An đang dừng lại ở vị trí cách vạch xuất phát bao nhiêu mét?

**Đầu vào (Input):**

Một số nguyên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

Hai số nguyên trên một dòng cách nhau dấu cách lần lượt là số vòng chạy trọn vẹn và khoảng cách tính từ vạch xuất phát.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 250 | 2 50 |

**Giải thích:** $250 = 2 \times 100 + 50$. Đã chạy 2 vòng trọn vẹn và đang ở mét thứ 50.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là chia quãng đường cho chu vi `100` mét: với `n = 250` thì vòng trọn `250 // 100 = 2`, vị trí dư `250 % 100 = 50` mét.
- Quy trình trong lời giải: đọc `n` rồi in một dòng `print(n // 100, n % 100)` cho ra `2 50`.
- Xử lý biên: `n = 100` cho `1 0` (vừa tròn một vòng, đứng đúng vạch xuất phát); `n = 1` cho `0 1`; `n = 10^9` cho `10000000 0`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 250)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `n` nhận giá trị | `n = 250` |
| 2 | Tính vòng `n // 100` | `250 // 100 = 2` |
| 3 | Tính vị trí `n % 100` | `250 % 100 = 50` |
| 4 | In một dòng | `2 50` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Nhầm chu vi thành `60` (đổi phút).**

```python
print(n // 60, n % 60)
```

Với số liệu mẫu trên, đoạn này cho `250` cho `4 10` thay vì `2 50`.

Cách sửa: chu vi sân là `100` mét.

**Bẫy 2: Dùng chia thực `/`.**

```python
print(n / 100, n % 100)
```

Với số liệu mẫu trên, đoạn này cho `250` in ra `2.5 50` thay vì `2 50`.

Cách sửa: dùng `//`.

#### 4. Lời giải tham khảo

```python
n = int(input())
print(n // 100, n % 100)
```

### Bài 14 [pya_l02_p05_bong_den_vien_bien_hieu]: Bóng đèn viền biển hiệu

Bối cảnh: Phố phường sắp đến hội hoa đăng, người ta muốn mắc các bóng đèn màu rực rỡ trang trí xung quanh viền của một bảng quảng cáo hình vuông. Bảng quảng cáo có chiều dài cạnh là $a\text{ dm}$. Các bóng đèn được mắc liên tiếp nhau và cách nhau đúng $5\text{ cm}$ dọc theo chu vi hình vuông (bao gồm cả các góc). Bác thợ điện leo thang mà chưa biết cần bao nhiêu bóng. Hãy giúp bác tính số bóng đèn cần mắc.

Nhiệm vụ: Hãy tính số lượng bóng đèn cần mắc.
* **Biết rằng:** $1\text{ dm} = 10\text{ cm}$.

**Đầu vào (Input):**

Một số nguyên dương $a$ ($1 \le a \le 10^7$).

**Đầu ra (Output):**

Một số nguyên duy nhất là số bóng đèn cần mắc.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 1 | 8 |

**Giải thích:** Cạnh $1\text{ dm} = 10\text{ cm}$. Chu vi bảng hình vuông là $10 \times 4 = 40\text{ cm}$.
Khoảng cách giữa các đèn là $5\text{ cm}$. Số đèn mắc là: $40 : 5 = 8$ bóng đèn.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là đổi đơn vị rồi chia chu vi: với `a = 1` dm thì `canh_cm = 1 * 10 = 10` cm, chu vi `10 * 4 = 40` cm, số bóng `40 // 5 = 8`.
- Quy trình trong lời giải: đọc `a`, tính `canh_cm = a * 10`, rồi in `canh_cm * 4 // 5`; thứ tự nhân trước chia sau cho đúng.
- Xử lý biên: `a = 1` cho `8` bóng; `a = 10^7` cho `80000000` bóng; mọi đáp số đều chia hết vì `a * 40` luôn chia hết cho `5`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `a` nhận giá trị | `a = 1` |
| 2 | Đổi ra xen-ti-mét `canh_cm = a * 10` | `canh_cm = 10` |
| 3 | Chu vi `canh_cm * 4` | `10 * 4 = 40` |
| 4 | Chia khoảng cách `40 // 5` | `8` |
| 5 | In kết quả | `8` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Quên đổi dm ra cm.**

```python
a = int(input())
print(a * 4 // 5)
```

Với số liệu mẫu trên, đoạn này cho `a = 1` in ra `0` thay vì `8` vì thiếu bước nhân `10`.

Cách sửa: tính `canh_cm = a * 10` trước.

**Bẫy 2: Dùng chia thực `/`.**

```python
print(canh_cm * 4 / 5)
```

Với số liệu mẫu trên, đoạn này cho `a = 1` in ra `8.0` thay vì `8`.

Cách sửa: dùng `//` để ra số nguyên.

#### 4. Lời giải tham khảo

```python
a = int(input())
canh_cm = a * 10
print(canh_cm * 4 // 5)
```

### Bài 15 [pya_l02_p16_du_quay_vong_tron]: Đu quay vòng tròn

Bối cảnh: Khu vui chơi vừa mở một chiếc đu quay khổng lồ, mỗi vòng quay trọn vẹn kéo dài đúng $C$ phút. Bạn Sóc Nâu ngồi trên đu quay suốt $N$ phút không chịu xuống vì mải ngắm thành phố từ trên cao. Bác quản trò muốn biết Sóc Nâu đã đi được bao nhiêu vòng trọn vẹn và đang dở dang bao nhiêu phút của vòng hiện tại. Hãy giúp bác quản trò tính nhanh.

Nhiệm vụ: Cho tổng thời gian $N$ và thời gian một vòng $C$, em hãy tính số vòng quay trọn vẹn và số phút dư.

**Đầu vào (Input):**

Gồm 2 dòng, mỗi dòng một số nguyên: $N$ ($1 \le N \le 10^9$) và $C$ ($1 \le C \le 10^9$).

**Đầu ra (Output):**

In ra hai số nguyên trên một dòng cách nhau một dấu cách: số vòng trọn vẹn và số phút dư.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 250 <br> 60 | 4 10 |

**Giải thích:** $250 = 4 \times 60 + 10$. Sóc Nâu đã đi được 4 vòng trọn vẹn và đang ở phút thứ 10 của vòng thứ năm.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là chia tổng thời gian cho độ dài một vòng: với `n = 250`, `c = 60` thì số vòng `250 // 60 = 4`, phút dư `250 % 60 = 10`.
- Quy trình trong lời giải: đọc `n` dòng 1, đọc `c` dòng 2, rồi in `n // c, n % c` cho ra `4 10`.
- Xử lý biên: `n = 1, c = 10^9` cho `0 1`; `n = c` cho `1 0`; `n = 10^9, c = 1` cho `1000000000 0`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 250 và 60 (hai dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc dòng 1, biến `n` nhận giá trị | `n = 250` |
| 2 | Đọc dòng 2, biến `c` nhận giá trị | `c = 60` |
| 3 | Tính vòng `n // c` | `250 // 60 = 4` |
| 4 | Tính dư `n % c` | `250 % 60 = 10` |
| 5 | In một dòng | `4 10` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Đọc hai số một dòng bằng `split()`.**

```python
n, c = map(int, input().split())
```

Với số liệu mẫu trên, đoạn này cho số liệu mẫu mỗi số một dòng nên nhận thiếu `c`.

Cách sửa: đọc hai lần `input()` riêng.

**Bẫy 2: Hoán đổi `c // n`.**

```python
print(c // n, c % n)
```

Với số liệu mẫu trên, đoạn này cho `250` và `60` cho `0 60` thay vì `4 10`.

Cách sửa: số bị chia là `n`.

#### 4. Lời giải tham khảo

```python
n = int(input())
c = int(input())
print(n // c, n % c)
```

### Bài 16 [pya_l02_p23_so_keo_con_thua]: Số kẹo còn thừa

Bối cảnh: Trong bài toán chia tài nguyên máy chủ, một lượng gồm $a$ gói tài nguyên được chia đều cho $b$ tiến trình đang xử lý.

Nhiệm vụ: Cho hai số nguyên dương $a$ và $b$. Hãy xác định lượng tài nguyên dư thừa không thể chia đều cho các tiến trình.

**Đầu vào (Input):**

Gồm 2 dòng lần lượt chứa hai số tự nhiên $N$ và $K$ ($1 \le N, K \le 10^9$).

**Đầu ra (Output):**

In ra số viên kẹo còn thừa.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 100 <br> 8 | 4 |

**Giải thích:** Với $a = 17$ và $b = 5$, phép chia dư cho kết quả: $17 \% 5 = 2$. Lượng còn dư không chia hết là 2.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là phần dư không chia hết: với `a = 100`, `b = 8` thì `100 % 8 = 4` vì `100 = 12 * 8 + 4`.
- Quy trình trong lời giải: đọc `a` dòng 1, đọc `b` dòng 2, rồi in `a % b`.
- Xử lý biên: `a = 8, b = 100` cho `8`; `a` chia hết cho `b` (ví dụ `16` và `8`) cho `0`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 100 và 8 (hai dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc dòng 1, biến `a` nhận giá trị | `a = 100` |
| 2 | Đọc dòng 2, biến `b` nhận giá trị | `b = 8` |
| 3 | Tính `a % b` | `100 % 8 = 4` |
| 4 | In kết quả | `4` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: In thương `a // b` thay vì dư.**

```python
print(a // b)
```


Với số liệu mẫu trên, đoạn này cho `100` và `8` cho `12` thay vì `4`.

Cách sửa: dùng `a % b`.

**Bẫy 2: Đọc hai số một dòng bằng `split()`.**

```python
a, b = map(int, input().split())
```

Với số liệu mẫu trên, đoạn này cho số liệu mẫu mỗi số một dòng nên nhận thiếu `b`.

Cách sửa: đọc hai lần `input()` riêng.

#### 4. Lời giải tham khảo

```python
a = int(input().strip())
b = int(input().strip())
print(a % b)
```

### Bài 17 [pya_l02_p20_phuc_hoi_so_bi_chia]: Bất biến chia kẹo và phục hồi số bị chia

Bối cảnh: Nam đem một số kẹo bí mật chia cho $B$ bạn thì mỗi bạn được $Q$ chiếc kẹo và Nam còn thừa lại $R$ chiếc kẹo.

Nhiệm vụ: Nhập 3 số nguyên $B, Q, R$ trên cùng 1 dòng ($B > R \ge 0$, $Q \ge 0$). Hãy tìm lại tổng số kẹo ban đầu mà Nam có.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên $B, Q, R$ ($1 \le B, Q \le 10^6$, $0 \le R < B$).

**Đầu ra (Output):**

In ra số kẹo ban đầu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 6 8 3 | 51 |

**Giải thích:** Áp dụng định lý bất biến phép chia: $A = B \times Q + R = 6 \times 8 + 3 = 51$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là công thức phục hồi số bị chia: với `b = 6`, `q = 8`, `r = 3` thì `6 * 8 + 3 = 48 + 3 = 51` chiếc kẹo ban đầu.
- Quy trình trong lời giải: đọc một dòng `b, q, r` rồi in `b * q + r`; nhân trước cộng sau.
- Xử lý biên: `r = 0` (chia hết) thì đáp số là `b * q`; `b = 10^6, q = 10^6, r = 999999` cho `1000000999999`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6 8 3 (một dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, tách ba biến | `b = 6`, `q = 8`, `r = 3` |
| 2 | Tính `b * q` | `6 * 8 = 48` |
| 3 | Cộng `r` | `48 + 3 = 51` |
| 4 | In kết quả | `51` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Viết `b * (q + r)` thêm ngoặc sai.**

```python
print(b * (q + r))
```

Với số liệu mẫu trên, đoạn này cho `6 8 3` cho `66` thay vì `51`.

Cách sửa: viết `b * q + r`.

**Bẫy 2: Viết `b + q * r` nhầm vai trò.**

```python
print(b + q * r)
```

Với số liệu mẫu trên, đoạn này cho `6 8 3` cho `30` thay vì `51`.

Cách sửa: số chia `b` nhân với thương `q` rồi cộng `r`.

#### 4. Lời giải tham khảo

```python
b, q, r = map(int, input().split())
print(b * q + r)
```

### Bài 18 [pya_l02_p32_da_thuc_bac_hai]: Đa thức bậc hai

Bối cảnh: Giáo sư Nguyễn đang nghiên cứu quỹ đạo bay của một quả bóng tennis được ném lên cao. Vị trí độ cao tại thời điểm $x$ giây được mô tả bởi đa thức bậc hai $P(x) = 2x^2 - 4x + 9$ (đơn vị: mét). Để phục vụ việc phân tích dữ liệu thí nghiệm, giáo sư cần tính nhanh giá trị $P(x)$ với nhiều mốc thời gian khác nhau. Em hãy lập trình giúp giáo sư.

Nhiệm vụ: Nhập số nguyên $x$. In ra giá trị của đa thức.

**Đầu vào (Input):**

Một dòng chứa số nguyên $x$ ($-1000 \le x \le 1000$).

**Đầu ra (Output):**

In ra giá trị của $P(x)$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3 | 15 |

**Giải thích:** $2 \times (3^2) - 4 \times 3 + 9 = 2 \times 9 - 12 + 9 = 15$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là thay `x` vào đa thức `2x^2 - 4x + 9`: với `x = 3` thì `2 * 9 - 4 * 3 + 9 = 18 - 12 + 9 = 15`.
- Quy trình trong lời giải: đọc `x` rồi in `2 * (x ** 2) - 4 * x + 9`; cặp ngoặc `(x ** 2)` bảo đảm tính mũ trước.
- Xử lý biên: `x = 0` cho `9`; `x = -1000` cho `2004009`; `x = 1000` cho `1996009`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `x` nhận giá trị | `x = 3` |
| 2 | Tính `x ** 2` | `9` |
| 3 | Tính `2 * 9 - 4 * 3 + 9` | `18 - 12 + 9 = 15` |
| 4 | In kết quả | `15` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Viết `2 * x ** 2` mà tưởng sai — bẫy thật là viết `2 * (x * 2)`.**

```python
print(2 * (x * 2) - 4 * x + 9)
```

Với số liệu mẫu trên, đoạn này cho `x = 3` cho `9` thay vì `15`.

Cách sửa: bình phương là `x ** 2`.

**Bẫy 2: Quên dấu trừ, viết `2 * (x ** 2) + 4 * x + 9`.**

```python
print(2 * (x ** 2) + 4 * x + 9)
```

Với số liệu mẫu trên, đoạn này cho `x = 3` cho `39` thay vì `15`.

Cách sửa: giữa là `- 4 * x`.

#### 4. Lời giải tham khảo

```python
x = int(input())
print(2 * (x ** 2) - 4 * x + 9)
```

### Bài 19 [pya_l02_p26_trong_cay_dai_lo]: Trồng cây đại lộ

Bối cảnh: Thành phố vừa khánh thành một đại lộ thẳng tắp dài $N$ mét. Mùa hè sắp đến, để có bóng mát cho người đi bộ, đội cây xanh quyết định trồng một hàng cây ngay ngắn ở một bên đường. Cây đầu tiên được trồng ngay tại điểm xuất phát (mét thứ 0), rồi cứ cách đúng $K$ mét lại trồng tiếp một cây nữa. Trước khi ra quân, đội trưởng muốn biết chính xác cần chuẩn bị bao nhiêu cây, và em chính là người giúp đội tính con số đó!

Nhiệm vụ: Hãy tính tổng số lượng cây xanh được trồng trên đoạn đường từ mét thứ 0 đến mét thứ $N$.

**Đầu vào (Input):**

Gồm 2 số tự nhiên $N$ và $K$ ($1 \le N, K \le 10^6$) mỗi số trên một dòng.

**Đầu ra (Output):**

Một số nguyên duy nhất là số cây trồng được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 <br> 3 | 4 |

**Giải thích:** Các cây được trồng tại các vị trí mét thứ: 0, 3, 6, 9. Tổng cộng có 4 cây.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là đếm mốc chia hết cộng thêm cây ở mét `0`: với `l = 10`, `d = 3` thì `10 // 3 + 1 = 3 + 1 = 4` cây ở các vị trí `0, 3, 6, 9`.
- Quy trình trong lời giải: đọc `l` dòng 1 (biến tên `l`), đọc `d` dòng 2, rồi in `l // d + 1`.
- Xử lý biên: `l = 3, d = 3` cho `2` cây (`0` và `3`); `l = 1, d = 10^6` cho `1` cây (chỉ cây ở `0`); `l = 10^6, d = 1` cho `1000001` cây.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10 và 3 (hai dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc dòng 1, biến `l` nhận giá trị | `l = 10` |
| 2 | Đọc dòng 2, biến `d` nhận giá trị | `d = 3` |
| 3 | Tính `l // d` | `10 // 3 = 3` |
| 4 | Cộng cây ở mét `0` | `3 + 1 = 4` |
| 5 | In kết quả | `4` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Quên cộng cây ở mét `0`: chỉ `l // d`.**

```python
print(l // d)
```

Với số liệu mẫu trên, đoạn này cho `10` và `3` cho `3` thay vì `4`.

Cách sửa: cộng thêm `1`.

**Bẫy 2: Đọc hai số một dòng bằng `split()`.**

```python
l, d = map(int, input().split())
```

Với số liệu mẫu trên, đoạn này cho số liệu mẫu mỗi số một dòng nên nhận thiếu `d`.

Cách sửa: đọc hai lần `input()` riêng.

#### 4. Lời giải tham khảo

```python
l = int(input().strip())
d = int(input().strip())
print(l // d + 1)
```

### Bài 20 [pya_l02_p15_gia_tri_bieu_thuc_pemdas]: Giá trị biểu thức PEMDAS

Bối cảnh: Lớp học của bạn Ong Vàng hôm nay thi xem ai là nhà tính nhẩm nhanh nhất. Cô giáo viết lên bảng một biểu thức bí mật gồm ba con số $a$, $b$, $c$ với quy tắc tính là $a + b \times c^2$. Bạn nào tính đúng thứ tự ưu tiên ngoặc, mũ, nhân chia rồi mới cộng trừ sẽ giành chiến thắng. Hãy giúp bạn Ong Vàng tính giá trị biểu thức này thật chính xác.

Nhiệm vụ: Cho ba số nguyên $a$, $b$, $c$, em hãy tính giá trị của biểu thức $a + b \times c^2$.

**Đầu vào (Input):**

Gồm 3 dòng, mỗi dòng một số nguyên: $a$, $b$, $c$ ($1 \le a, b, c \le 100$).

**Đầu ra (Output):**

In ra một số nguyên duy nhất là giá trị của biểu thức.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 2 <br> 3 <br> 4 | 50 |

**Giải thích:** Ưu tiên lũy thừa trước: $c^2 = 4^2 = 16$. Tiếp theo nhân: $b \times 16 = 3 \times 16 = 48$. Cuối cùng cộng: $2 + 48 = 50$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là thứ tự ưu tiên mũ rồi nhân rồi cộng: với `a = 2`, `b = 3`, `c = 4` thì `c ** 2 = 16`, `b * 16 = 48`, `2 + 48 = 50`.
- Quy trình trong lời giải: đọc `a`, `b`, `c` mỗi số một dòng rồi in `a + b * c ** 2`; Python tự tính `**` trước, `*` sau, `+` cuối.
- Xử lý biên: `a = b = c = 1` cho `2`; `a = b = c = 100` cho `1000100`; số nào cũng dương theo ràng buộc.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2, 3, 4 (ba dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc ba dòng vào `a`, `b`, `c` | `a = 2`, `b = 3`, `c = 4` |
| 2 | Tính `c ** 2` | `4 ** 2 = 16` |
| 3 | Tính `b * 16` | `3 * 16 = 48` |
| 4 | Tính `a + 48` và in | `50` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Thêm ngoặc sai `(a + b) * c ** 2`.**

```python
print((a + b) * c ** 2)
```

Với số liệu mẫu trên, đoạn này cho `2, 3, 4` cho `80` thay vì `50`.

Cách sửa: viết `a + b * c ** 2`.

**Bẫy 2: Viết `(a + b * c) ** 2`.**

```python
print((a + b * c) ** 2)
```

Với số liệu mẫu trên, đoạn này cho `2, 3, 4` cho `196` thay vì `50`.

Cách sửa: chỉ mũ áp vào `c`.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
c = int(input())
print(a + b * c ** 2)
```

### Bài 21 [pya_l02_p24_doi_gio_ra_phut_giay]: Đổi giờ ra phút giây

Bối cảnh: Bạn Tít được tặng một chiếc đồng hồ điện tử xinh xắn hiển thị thời gian gồm $H$ giờ, $M$ phút và $S$ giây. Tít khoe với bạn thân và đố bạn đoán xem cả khoảng thời gian đó là bao nhiêu giây. Hai bạn đếm xuôi đếm ngược mãi chưa ra. Hãy giúp hai bạn đổi thời gian ra giây.

Nhiệm vụ: Hãy tính xem tổng cộng khoảng thời gian đó tương đương với bao nhiêu giây?
* **Biết rằng:** $1\text{ giờ} = 60\text{ phút} = 3600\text{ giây}$, $1\text{ phút} = 60\text{ giây}$.

**Đầu vào (Input):**

Ba dòng lần lượt chứa 3 số tự nhiên $H, M, S$ ($0 \le H \le 23, 0 \le M, S \le 59$).

**Đầu ra (Output):**

Một số nguyên duy nhất là tổng số giây.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 1 <br> 20 <br> 15 | 4815 |

**Giải thích:** $1 \times 3600 + 20 \times 60 + 15 = 3600 + 1200 + 15 = 4815$ giây.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là đổi từng đơn vị ra giây rồi cộng: với `h = 1`, `m = 20`, `s = 15` thì `1 * 3600 + 20 * 60 + 15 = 3600 + 1200 + 15 = 4815` giây.
- Quy trình trong lời giải: đọc `h`, `m`, `s` mỗi số một dòng rồi in `h * 3600 + m * 60 + s`.
- Xử lý biên: `0 0 0` cho `0`; `23 59 59` cho `86399`; `0 1 0` cho `60`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1, 20, 15 (ba dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc ba dòng vào `h`, `m`, `s` | `h = 1`, `m = 20`, `s = 15` |
| 2 | Tính `h * 3600` | `3600` |
| 3 | Tính `m * 60` rồi cộng | `3600 + 1200 = 4800` |
| 4 | Cộng `s` và in | `4800 + 15 = 4815` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Nhầm một giờ là `360` giây.**

```python
print(h * 360 + m * 60 + s)
```

Với số liệu mẫu trên, đoạn này cho `1 20 15` cho `1575` thay vì `4815`.

Cách sửa: một giờ là `3600` giây.

**Bẫy 2: Nhầm một phút là `100` giây.**

```python
print(h * 3600 + m * 100 + s)
```

Với số liệu mẫu trên, đoạn này cho `1 20 15` cho `5615` thay vì `4815`.

Cách sửa: một phút là `60` giây.

#### 4. Lời giải tham khảo

```python
h = int(input())
m = int(input())
s = int(input())
print(h * 3600 + m * 60 + s)
```

### Bài 22 [pya_l02_p29_tach_chu_so_tan_cung]: Tách chữ số tận cùng

Bối cảnh: Na có một mã số may mắn là một số tự nhiên $N$ viết trên chiếc vòng tay. Hôm nay Na chơi trò thám tử cùng bạn thân, muốn tìm ra chữ số hàng đơn vị và chữ số hàng chục của số này để mở chiếc hộp bí mật. Hai bạn xoay chiếc vòng mãi mà chưa tách được. Hãy giúp Na tách hai chữ số đó ra.

Nhiệm vụ: Cho số tự nhiên $N$, hãy tách và in ra chữ số hàng đơn vị và chữ số hàng chục của $N$.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($10 \le N \le 10^9$).

**Đầu ra (Output):**

* Dòng 1: Chữ số hàng đơn vị của $N$.
 * Dòng 2: Chữ số hàng chục của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 857 | 7 <br> 5 |

**Giải thích:** Chữ số hàng đơn vị là 7, hàng chục là 5.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là tách hai hàng thấp nhất: với `n = 857` thì hàng đơn vị `857 % 10 = 7`, hàng chục `857 // 10 % 10 = 85 % 10 = 5`.
- Quy trình trong lời giải: đọc `n`, in `n % 10` ở dòng 1 rồi in `n // 10 % 10` ở dòng 2.
- Xử lý biên: `n = 10` cho `0` rồi `1`; `n = 10^9 = 1000000000` cho `0` rồi `0`; `n = 99` cho `9` rồi `9`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 857)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `n` nhận giá trị | `n = 857` |
| 2 | Tính đơn vị `n % 10` và in dòng 1 | `7` |
| 3 | Tính `n // 10 = 85` | `85` |
| 4 | Tính `85 % 10` và in dòng 2 | `5` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: In hai số trên một dòng.**

```python
print(n % 10, n // 10 % 10)
```

Với số liệu mẫu trên, đoạn này cho `857` in ra `7 5` một dòng thay vì hai dòng `7` rồi `5`.

Cách sửa: dùng hai lệnh `print` riêng.

**Bẫy 2: Hoán đổi thứ tự hai dòng.**

```python
print(n // 10 % 10)
print(n % 10)
```

Với số liệu mẫu trên, đoạn này cho `857` in ra `5` rồi `7`, ngược yêu cầu (đơn vị trước, chục sau).

Cách sửa: in `n % 10` trước.

#### 4. Lời giải tham khảo

```python
n = int(input())
print(n % 10)
print(n // 10 % 10)
```

### Bài 23 [pya_l02_p30_dao_nguoc_so_2_chu_so]: Đảo ngược số 2 chữ số

Bối cảnh: Câu lạc bộ thám tử nhí vừa nhận được một mật thư bí ẩn, trong đó các con số 2 chữ số đã bị đảo ngược vị trí hai chữ số cho nhau (ví dụ số 27 bị biến thành 72). Đội trưởng đố cả đội giải mã được con số thật. Các thám tử nhí soi kính lúp mà vẫn bối rối. Hãy giúp đội thám tử đảo ngược con số về đúng vị trí.

Nhiệm vụ: Nhập vào một số tự nhiên $N$ có đúng 2 chữ số ($10 \le N \le 99$). Hãy in ra số sau khi đảo ngược hai chữ số.

**Đầu vào (Input):**

Một số tự nhiên $N$.

**Đầu ra (Output):**

Số nguyên sau khi đảo ngược. (Lưu ý: Nếu số là 30 thì đảo lại là 3).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 49 | 94 |

**Giải thích:** Hàng chục là 4, hàng đơn vị là 9 $\to$ Đảo lại thành 94.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 50 | 5 |

**Giải thích:** Hàng chục là 5, đơn vị là 0 $\to$ Đảo lại thành $0 \times 10 + 5 = 5$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là đổi chỗ hàng chục và đơn vị: với `N = 49` thì `chuc = 49 // 10 = 4`, `don_vi = 49 % 10 = 9`, số đảo `9 * 10 + 4 = 90 + 4 = 94`.
- Quy trình trong lời giải: đọc `N`, đặt `chuc` và `don_vi`, tính `dao_nguoc = don_vi * 10 + chuc` rồi in ra.
- Xử lý biên: `N = 10` cho `1` (vì `01` là `1`); `N = 99` cho `99`; `N = 30` cho `3`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 49)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `N` nhận giá trị | `N = 49` |
| 2 | Tách `chuc = 49 // 10` | `chuc = 4` |
| 3 | Tách `don_vi = 49 % 10` | `don_vi = 9` |
| 4 | Ghép `9 * 10 + 4` | `94` |
| 5 | In kết quả | `94` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Ghép sai `chuc * 10 + don_vi` (in lại số cũ).**

```python
dao_nguoc = chuc * 10 + don_vi
```

Với số liệu mẫu trên, đoạn này cho `49` cho `49` thay vì `94`.

Cách sửa: đặt `don_vi * 10 + chuc`.

**Bẫy 2: Viết biến thường `n` thay vì `N` nhưng dùng lẫn lộn.**

```python
chuc = n // 10
```

Với số liệu mẫu trên, đoạn này cho Chương trình báo lỗi vì biến đã đặt tên là `N` viết hoa.

Cách sửa: giữ đúng tên `N` viết hoa như lời giải.

#### 4. Lời giải tham khảo

```python
N = int(input())
chuc = N // 10
don_vi = N % 10
dao_nguoc = don_vi * 10 + chuc
print(dao_nguoc)
```

### Bài 24 [pya_l02_p33_tich_hai_tong]: Biểu thức có dấu ngoặc

Bối cảnh: Trong giờ thực hành đại số, cô giáo đưa ra bài toán ứng dụng: cho bốn số nguyên $a$, $b$, $c$, $d$, hãy tính tích của hai tổng $T = (a + b) \times (c - d)$. Đây là phép toán kết hợp giữa cộng, trừ và nhân — đòi hỏi học sinh phải hiểu rõ thứ tự ưu tiên phép tính khi viết biểu thức trong Python. Em hãy viết chương trình tính giá trị $T$ từ bốn số nhập vào.

Nhiệm vụ: Nhập 4 số nguyên $a, b, c, d$ trên cùng 1 dòng cách nhau dấu cách. In ra giá trị của $T$.

**Đầu vào (Input):**

Một dòng chứa 4 số nguyên $a, b, c, d$ ($-10^4 \le a, b, c, d \le 10^4$).

**Đầu ra (Output):**

In ra giá trị số nguyên $T$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 5 3 10 6 | 32 |

**Giải thích:** $(5 + 3) \times (10 - 6) = 8 \times 4 = 32$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là nhân hai ngoặc: với `a = 5, b = 3, c = 10, d = 6` thì `(5 + 3) * (10 - 6) = 8 * 4 = 32`.
- Quy trình trong lời giải: đọc một dòng `a, b, c, d` rồi in `(a + b) * (c - d)`; ngoặc buộc tính tổng và hiệu trước.
- Xử lý biên: `a + b = 0` thì đáp số `0`; `c - d = 0` thì đáp số `0`; số âm vẫn đúng (ví dụ `-5 3 10 6` cho `-8`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 3 10 6 (một dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, tách bốn biến | `a = 5`, `b = 3`, `c = 10`, `d = 6` |
| 2 | Tính `a + b` | `8` |
| 3 | Tính `c - d` | `4` |
| 4 | Nhân và in `8 * 4` | `32` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Bỏ ngoặc: `a + b * c - d`.**

```python
print(a + b * c - d)
```

Với số liệu mẫu trên, đoạn này cho `5 3 10 6` cho `29` thay vì `32` vì nhân làm trước.

Cách sửa: giữ ngoặc `(a + b) * (c - d)`.

**Bẫy 2: Nhầm dấu `c + d` thay vì `c - d`.**

```python
print((a + b) * (c + d))
```

Với số liệu mẫu trên, đoạn này cho `5 3 10 6` cho `128` thay vì `32`.

Cách sửa: ngoặc sau là `(c - d)`.

#### 4. Lời giải tham khảo

```python
a, b, c, d = map(int, input().split())
print((a + b) * (c - d))
```

### Bài 25 [pya_l02_p34_dong_ho_24h]: Đồng hồ 24 giờ

Bối cảnh: Hiện tại đồng hồ đang chỉ $H$ giờ. Cần xác định xem sau $K$ giờ nữa thì đồng hồ chỉ mấy giờ?

Nhiệm vụ: Nhập hai số nguyên $H$ và $K$ trên 1 dòng ($0 \le H \le 23$, $0 \le K \le 10^9$). In ra số giờ mà đồng hồ sẽ hiển thị (từ 0 đến 23).

**Đầu vào (Input):**

Một dòng chứa $H$ và $K$.

**Đầu ra (Output):**

In ra giờ mới.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 20 10 | 6 |

**Giải thích:** $20 + 10 = 30$ giờ. $30 \% 24 = 6$ giờ sáng.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là đồng hồ quay vòng `24` giờ: với `h = 20`, `k = 10` thì `(20 + 10) % 24 = 30 % 24 = 6` giờ sáng.
- Quy trình trong lời giải: đọc một dòng `h, k` rồi in `(h + k) % 24`.
- Xử lý biên: `h = 0, k = 0` cho `0`; `h = 23, k = 1` cho `0`; `k = 10^9` vẫn đúng nhờ phép dư.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 20 10 (một dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, tách `h` và `k` | `h = 20`, `k = 10` |
| 2 | Tính `h + k` | `30` |
| 3 | Tính `30 % 24` | `6` |
| 4 | In kết quả | `6` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Quên `% 24`, chỉ `h + k`.**

```python
print(h + k)
```

Với số liệu mẫu trên, đoạn này cho `20 10` in ra `30` thay vì `6`, vượt khung `0` đến `23`.

Cách sửa: lấy `(h + k) % 24`.

**Bẫy 2: Nhầm vòng `12` giờ (`% 12`).**

```python
print((h + k) % 12)
```

Với số liệu mẫu trên, đoạn này cho `20 10` cho `6` trùng đáp số nhưng với `12 12` cho `0` thay vì `0` — ví dụ `5 5` cho `10` đúng nhưng `13 0` cho `1` thay vì `13`.

Cách sửa: đồng hồ này vòng `24`.

#### 4. Lời giải tham khảo

```python
h, k = map(int, input().split())
print((h + k) % 24)
```

### Bài 26 [pya_l02_p35_ngay_trong_tuan]: Ngày trong tuần

Bối cảnh: Quy ước Chủ Nhật là ngày 0, Thứ Hai là ngày 1, ..., Thứ Bảy là ngày 6. Hôm nay là ngày $D$.

Nhiệm vụ: Nhập ngày hiện tại $D$ ($0 \le D \le 6$) và số ngày trôi qua $N$ ($0 \le N \le 10^9$). In ra thứ tương ứng sau $N$ ngày.

**Đầu vào (Input):**

Một dòng chứa hai số nguyên $D$ và $N$.

**Đầu ra (Output):**

In ra mã số ngày trong tuần (từ 0 đến 6).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 1 10 | 4 |

**Giải thích:** Thứ Hai là ngày 1. Sau 10 ngày nữa: $(1 + 10) \% 7 = 11 \% 7 = 4$ (tức Thứ Năm).

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là tuần quay vòng `7` ngày: với `d = 1` (thứ Hai), `n = 10` thì `(1 + 10) % 7 = 11 % 7 = 4` tức thứ Năm.
- Quy trình trong lời giải: đọc một dòng `d, n` rồi in `(d + n) % 7`.
- Xử lý biên: `d = 0, n = 0` cho `0` (Chủ Nhật); `d = 6, n = 1` cho `0`; `n = 10^9` vẫn đúng nhờ phép dư.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1 10 (một dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, tách `d` và `n` | `d = 1`, `n = 10` |
| 2 | Tính `d + n` | `11` |
| 3 | Tính `11 % 7` | `4` |
| 4 | In kết quả | `4` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Quên `% 7`, chỉ `d + n`.**

```python
print(d + n)
```

Với số liệu mẫu trên, đoạn này cho `1 10` in ra `11` thay vì `4`, vượt khung `0` đến `6`.

Cách sửa: lấy `(d + n) % 7`.

**Bẫy 2: Nhầm vòng `% 24` (đồng hồ).**

```python
print((d + n) % 24)
```

Với số liệu mẫu trên, đoạn này cho `1 10` cho `11` thay vì `4`.

Cách sửa: tuần có `7` ngày.

#### 4. Lời giải tham khảo

```python
d, n = map(int, input().split())
print((d + n) % 7)
```

### Bài 27 [pya_l02_p01_chia_deu_banh_quy]: Chia đều bánh quy

Bối cảnh: Tiệm bánh Hạnh Phúc vừa ra lò một mẻ gồm $a$ chiếc bánh quy bơ thơm phức. Cô chủ tiệm muốn chia đều số bánh vào $b$ đĩa trưng bày để phục vụ khách, sao cho mỗi đĩa có số bánh bằng nhau và nhiều nhất có thể. Những chiếc bánh còn dư không đủ xếp thêm một đĩa nữa sẽ được cất riêng vào hộp giữ tươi.

Nhiệm vụ: Cho hai số nguyên dương $a$ (tổng số bánh) và $b$ (số đĩa). Hãy lập trình tính số bánh trên mỗi đĩa (phần nguyên của phép chia $a : b$) và số bánh còn dư lại.

**Đầu vào (Input):**

Nhập vào 2 số nguyên dương $a$ và $b$ trên 2 dòng ($1 \le a, b \le 1000$).

**Đầu ra (Output):**

In ra 2 số trên một dòng cách nhau một dấu cách: số bánh trên mỗi đĩa và số bánh còn dư.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 17 <br> 5 | 3 2 |

**Giải thích:** $17 : 5 = 3$ dư $2$. Mỗi đĩa 3 cái, còn dư 2 cái bánh.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là phép chia nguyên một lần: với `a = 17` chiếc bánh và `b = 5` chiếc đĩa, số bánh mỗi đĩa là `a // b = 17 // 5 = 3`, số dư là `a % b = 17 % 5 = 2`.
- Quy trình trong lời giải: đọc `a` từ dòng 1, đọc `b` từ dòng 2, rồi in một dòng duy nhất `print(a // b, a % b)` cho ra `3 2`.
- Xử lý biên: khi `a = 1, b = 1000` thì mỗi đĩa được `0` và dư `1`; khi `a = 1000, b = 1` thì mỗi đĩa `1000` dư `0`; khi `a` chia hết cho `b` (ví dụ `10` và `5`) phần dư bằng `0`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 17 và 5 (hai dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc dòng 1, biến `a` nhận giá trị | `a = 17` |
| 2 | Đọc dòng 2, biến `b` nhận giá trị | `b = 5` |
| 3 | Tính `a // b` | `17 // 5 = 3` |
| 4 | Tính `a % b` | `17 % 5 = 2` |
| 5 | In kết quả một dòng | `3 2` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Chỉ in thương, quên in số dư.**

```python
print(a // b)
```

Với số liệu mẫu trên, đoạn này cho `17` và `5` chỉ in ra `3`, thiếu số `2` nên thiếu một nửa đáp số.

Cách sửa: in cả hai giá trị `print(a // b, a % b)`.

**Bẫy 2: Dùng phép chia thực `/` thay vì `//`.**

```python
print(a / b, a % b)
```

Với số liệu mẫu trên, đoạn này cho `17` và `5` in ra `3.4 2` thay vì `3 2`.

Cách sửa: dùng `//` để lấy phần nguyên.

**Bẫy 3: Đọc cả hai số trên một dòng bằng `split()`.**

```python
a, b = map(int, input().split())
```

Với số liệu mẫu trên, đoạn này cho số liệu mẫu mỗi số nằm một dòng nên dòng 2 bị bỏ sót, chương trình nhận thiếu `b`.

Cách sửa: đọc hai lần `input()`, mỗi lần một số.

#### 4. Lời giải tham khảo

```python
a = int(input().strip())
b = int(input().strip())
print(a // b, a % b)
```

### Bài 28 [pya_l02_p31_xe_buyt_cho_hoc_sinh]: Xe buýt chở học sinh

Bối cảnh: Trường học sinh tổ chức một chuyến dã ngoại thật vui cho $N$ học sinh. Nhà trường thuê các xe buýt loại $K$ chỗ ngồi, mỗi xe buýt chở được tối đa $K$ bạn học sinh. Sáng khởi hành, các bạn xếp hàng ngay ngắn, tay vẫy cờ đỏ sao vàng. Thầy hiệu trưởng muốn không bạn nào bị ở lại trường. Hãy giúp thầy tính số xe buýt cần thuê.

Nhiệm vụ: Hỏi nhà trường cần thuê **ít nhất bao nhiêu xe buýt** để chở hết toàn bộ $N$ học sinh (không để bạn nào phải ở lại trường)?

**Đầu vào (Input):**

Nhập vào 2 số nguyên dương $N$ và $K$ ($1 \le N, K \le 10^6$).

**Đầu ra (Output):**

Một số nguyên duy nhất là số lượng xe buýt tối thiểu cần thuê.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 25 <br> 10 | 3 |

**Giải thích:** Hai xe đầu chở được 20 bạn, còn 5 bạn nữa nên cần thuê thêm một xe.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 30 <br> 10 | 3 |

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là làm tròn lên: với `n = 25`, `k = 10` thì `(25 + 10 - 1) // 10 = 34 // 10 = 3` xe; hai xe chở `20` bạn, xe thứ `3` chở `5` bạn còn lại.
- Quy trình trong lời giải: đọc `n` dòng 1, đọc `k` dòng 2, rồi in `(n + k - 1) // k`.
- Xử lý biên: `n = 10, k = 10` cho `1`; `n = 11, k = 10` cho `2`; `n = 10^6, k = 1` cho `1000000`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 25 và 10 (hai dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc dòng 1, biến `n` nhận giá trị | `n = 25` |
| 2 | Đọc dòng 2, biến `k` nhận giá trị | `k = 10` |
| 3 | Tính `n + k - 1 = 34` | `34` |
| 4 | Chia nguyên `34 // 10` | `3` |
| 5 | In kết quả | `3` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Dùng `n // k` (bỏ bạn dư).**

```python
print(n // k)
```

Với số liệu mẫu trên, đoạn này cho `25` và `10` cho `2` thay vì `3`, còn `5` bạn không có xe.

Cách sửa: dùng `(n + k - 1) // k`.

**Bẫy 2: Đọc hai số một dòng bằng `split()`.**

```python
n, k = map(int, input().split())
```

Với số liệu mẫu trên, đoạn này cho số liệu mẫu mỗi số một dòng nên nhận thiếu `k`.

Cách sửa: đọc hai lần `input()` riêng.

#### 4. Lời giải tham khảo

```python
n = int(input().strip())
k = int(input().strip())
print((n + k - 1) // k)
```

### Bài 29 [pya_l02_p19_chuyen_xe_hoc_sinh]: Tính số chuyến xe cần thiết

Bối cảnh: Trường trung học cơ sở Ngôi Sao Sáng tổ chức chuyến dã ngoại tham quan bảo tàng cho $N$ học sinh. Nhà trường thuê xe khách loại nhỏ, mỗi xe chở tối đa $K$ em. Ban tổ chức cần tính chính xác số xe tối thiểu phải thuê sao cho tất cả học sinh đều có chỗ ngồi, kể cả khi xe cuối cùng không chở đủ $K$ em vẫn phải thuê nguyên chiếc.

Nhiệm vụ: Nhập hai số nguyên dương $N$ và $K$ trên 1 dòng. In ra số lượng xe tối thiểu cần thuê để chở hết tất cả học sinh.

**Đầu vào (Input):**

Một dòng chứa hai số nguyên dương $N, K$ ($1 \le N, K \le 10^9$).

**Đầu ra (Output):**

In ra số xe tối thiểu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 41 10 | 5 |

**Giải thích:** 4 xe chở được 40 em, còn 1 em vẫn cần thêm 1 xe nữa $\implies$ Cần 5 xe. Công thức làm tròn lên chuẩn: `(N + K - 1) // K`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là làm tròn lên phép chia: với `n = 41`, `k = 10` thì `(41 + 10 - 1) // 10 = 50 // 10 = 5` xe; 4 xe chở `40` em, còn `1` em cần thêm xe thứ `5`.
- Quy trình trong lời giải: đọc một dòng `n, k`, rồi in `(n + k - 1) // k`.
- Xử lý biên: `n = 10, k = 10` cho `1`; `n = 11, k = 10` cho `2`; `n = 10^9, k = 1` cho `1000000000`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 41 10 (một dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, tách `n` và `k` | `n = 41`, `k = 10` |
| 2 | Tính `n + k - 1` | `41 + 10 - 1 = 50` |
| 3 | Chia nguyên `50 // 10` | `5` |
| 4 | In kết quả | `5` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Dùng chia xuống `n // k`.**

```python
print(n // k)
```

Với số liệu mẫu trên, đoạn này cho `41 10` cho `4` thay vì `5`, còn `1` em bị bỏ lại.

Cách sửa: dùng `(n + k - 1) // k`.

**Bẫy 2: Dùng chia thực `/`.**

```python
print(n / k)
```

Với số liệu mẫu trên, đoạn này cho `41 10` in ra `4.1` thay vì `5`.

Cách sửa: dùng công thức làm tròn lên với `//`.

#### 4. Lời giải tham khảo

```python
n, k = map(int, input().split())
print((n + k - 1) // k)
```

### Bài 30 [pya_l02_p21_chia_nguyen_chia_du]: Phép chia nguyên và chia dư cơ bản

Bối cảnh: Trong giờ thực hành lập trình tại phòng máy tính của trường, thầy giáo Minh giao cho học sinh bài tập thú vị: cho hai số nguyên dương bất kỳ, hãy tính đồng thời kết quả phép chia nguyên (phần nguyên) và phép chia lấy dư (phần dư). Hai phép toán này là nền tảng quan trọng trong rất nhiều bài toán tin học, từ tách chữ số đến kiểm tra tính chẵn lẻ.

Nhiệm vụ: Nhập hai số nguyên dương $A$ và $B$ trên 1 dòng. In ra thương nguyên $A // B$ và phần dư $A \% B$ trên cùng một dòng cách nhau dấu cách.

**Đầu vào (Input):**

Một dòng chứa hai số nguyên dương $A, B$ ($1 \le B \le A \le 10^9$).

**Đầu ra (Output):**

Một dòng in ra $A // B$ và $A \% B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 17 5 | 3 2 |

**Giải thích:** $17 // 5 = 3$ và $17 \% 5 = 2$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là in đồng thời thương và dư: với `a = 17`, `b = 5` thì `17 // 5 = 3` và `17 % 5 = 2`.
- Quy trình trong lời giải: đọc một dòng `a, b` rồi in một dòng `print(a // b, a % b)` cho ra `3 2`.
- Xử lý biên: `b = a` (ví dụ `7 7`) cho `1 0`; `b = 1` thì dư luôn `0`; `a = 10^9, b = 10^9` cho `1 0`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 17 5 (một dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, tách `a` và `b` | `a = 17`, `b = 5` |
| 2 | Tính `a // b` | `17 // 5 = 3` |
| 3 | Tính `a % b` | `17 % 5 = 2` |
| 4 | In một dòng | `3 2` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Dùng chia thực `/` cho thương.**

```python
print(a / b, a % b)
```

Với số liệu mẫu trên, đoạn này cho `17 5` in ra `3.4 2` thay vì `3 2`.

Cách sửa: dùng `a // b`.

**Bẫy 2: Hoán đổi `b // a`.**

```python
print(b // a, b % a)
```

Với số liệu mẫu trên, đoạn này cho `17 5` cho `0 5` thay vì `3 2`.

Cách sửa: số bị chia `a` đứng trước.

#### 4. Lời giải tham khảo

```python
a, b = map(int, input().split())
print(a // b, a % b)
```

### Bài 31 [pya_l02_p08_kim_dong_ho_12_gio]: Kim đồng hồ 12 giờ

Bối cảnh: Trên tường lớp học treo một chiếc đồng hồ kim tròn xinh có 12 số đánh dấu từ 1 đến 12. Hiện tại kim giờ đang chỉ vào đúng số $H$. Cô giáo đố cả lớp: nếu chờ thêm đúng $K$ giờ nữa thì kim giờ sẽ nhích tới số mấy. Các bạn ngó nghiêng mãi chưa chắc chắn. Hãy giúp cả lớp tìm câu trả lời.

Nhiệm vụ: Sau đúng $K$ giờ nữa, hỏi kim giờ sẽ chỉ vào số mấy?

**Đầu vào (Input):**

Nhập vào 2 số nguyên $H$ ($1 \le H \le 12$) và $K$ ($1 \le K \le 10^9$).

**Đầu ra (Output):**

In ra một số nguyên từ 1 đến 12 là số mà kim giờ đang chỉ.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 <br> 5 | 3 |

**Giải thích:** Lúc 10 giờ, sau 5 giờ nữa là 15 giờ. Trên đồng hồ 12 số tương ứng số 3.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 9 <br> 3 | 12 |

**Giải thích:** Lúc 9 giờ, sau 3 giờ nữa là 12 giờ.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là đồng hồ vòng tròn 12 số: với `h = 10`, `k = 5` thì `(10 + 5 - 1) % 12 + 1 = 14 % 12 + 1 = 2 + 1 = 3`.
- Quy trình trong lời giải: đọc `h` dòng 1, đọc `k` dòng 2, trừ `1` trước khi chia dư cho `12` rồi cộng `1` để dải số chạy từ `1` đến `12` thay vì `0` đến `11`.
- Xử lý biên: `h = 12, k = 12` cho `12`; `h = 12, k = 1` cho `1`; `k = 10^9` vẫn đúng nhờ phép dư.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10 và 5 (hai dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc dòng 1, biến `h` nhận giá trị | `h = 10` |
| 2 | Đọc dòng 2, biến `k` nhận giá trị | `k = 5` |
| 3 | Tính `h + k - 1` | `10 + 5 - 1 = 14` |
| 4 | Tính `14 % 12 + 1` | `2 + 1 = 3` |
| 5 | In kết quả | `3` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Quên trừ 1 và cộng 1: `(h + k) % 12`.**

```python
print((h + k) % 12)
```

Với số liệu mẫu trên, đoạn này cho `10` và `5` cho `15 % 12 = 3` trùng đáp số nhưng với `7` và `5` cho `0` thay vì `12`.

Cách sửa: dùng `(h + k - 1) % 12 + 1`.

**Bẫy 2: Đọc hai số trên một dòng bằng `split()`.**

```python
h, k = map(int, input().split())
```

Với số liệu mẫu trên, đoạn này cho số liệu mẫu mỗi số một dòng nên cách đọc này nhận thiếu `k`.

Cách sửa: đọc hai lần `input()` riêng.

#### 4. Lời giải tham khảo

```python
h = int(input().strip())
k = int(input().strip())
print((h + k - 1) % 12 + 1)
```

### Bài 32 [pya_l02_p06_chia_keo_hoc_sinh]: Chia kẹo cho các bạn

Bối cảnh: Nhân dịp tổng kết cuối năm, cô giáo chủ nhiệm lớp 6A mua $N$ chiếc kẹo sô-cô-la để thưởng cho $K$ bạn học sinh xuất sắc. Cô muốn chia đều kẹo cho các bạn sao cho mỗi bạn nhận được số kẹo bằng nhau, phần kẹo dư ra (nếu có) cô sẽ giữ lại để lần sau. Em hãy tính xem mỗi bạn được bao nhiêu chiếc kẹo và còn dư lại bao nhiêu chiếc.

Nhiệm vụ: Nhập hai số nguyên dương $N$ và $K$ trên 1 dòng. In ra 2 dòng:

**Đầu vào (Input):**

Một dòng chứa hai số nguyên dương $N, K$ ($1 \le N, K \le 10^9$).

**Đầu ra (Output):**

Hai dòng lần lượt là thương nguyên và số kẹo dư.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 25 4 | 6 <br> 1 |

**Giải thích:** Mỗi bạn được 6 kẹo, thừa lại 1 kẹo.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là chia nguyên và chia dư từ một dòng: với `n = 25`, `k = 4` thì mỗi bạn `25 // 4 = 6` chiếc, dư `25 % 4 = 1` chiếc.
- Quy trình trong lời giải: đọc một dòng `n, k = map(int, input().split())`, in `n // k` ở dòng 1 rồi in `n % k` ở dòng 2.
- Xử lý biên: `n = 1, k = 1` cho `1` và `0`; khi `n < k` (ví dụ `3` và `5`) thì mỗi bạn `0` và dư `3`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 25 4 (một dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, tách thành `n` và `k` | `n = 25`, `k = 4` |
| 2 | Tính `n // k` | `25 // 4 = 6` |
| 3 | In dòng 1 | `6` |
| 4 | Tính `n % k` | `25 % 4 = 1` |
| 5 | In dòng 2 | `1` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: In hai số trên cùng một dòng.**

```python
print(n // k, n % k)
```

Với số liệu mẫu trên, đoạn này cho `25 4` in ra `6 1` trên một dòng thay vì hai dòng `6` rồi `1`.

Cách sửa: dùng hai lệnh `print` riêng.

**Bẫy 2: Đọc hai dòng thay vì một dòng.**

```python
n = int(input())
k = int(input())
```

Với số liệu mẫu trên, đoạn này cho số liệu mẫu `25 4` nằm chung một dòng nên cách đọc này chờ thêm dòng và nhận sai.

Cách sửa: đọc một dòng rồi tách bằng `split()`.

#### 4. Lời giải tham khảo

```python
n, k = map(int, input().split())
print(n // k)
print(n % k)
```

### Bài 33 [pya_l02_p12_ban_co_caro_vo_tan]: Bàn cờ Ca-rô vô tận

Bối cảnh: Giờ giải lao, hai bạn Bi và Bo rủ nhau chơi trên một bàn cờ ô vuông vô tận được chia thành các hàng, mỗi hàng có đúng $W$ ô vuông. Các ô vuông được đánh số liên tiếp bắt đầu từ $1$:
 * Hàng 1 gồm các ô: $1, 2, \dots, W$.
 * Hàng 2 gồm các ô: $W+1, W+2, \dots, 2W$.
 * Cứ như vậy tiếp tục cho các hàng tiếp theo.
Đến lượt đi, Bi chỉ vào một ô và đố Bo tìm vị trí của nó. Hãy tìm xem ô đó ở hàng mấy, cột mấy.

Nhiệm vụ: Cho biết số thứ tự của một ô là $K$. Hãy xác định xem ô đó nằm ở **Hàng thứ mấy** và **Cột thứ mấy** (Cột tính từ 1 đến $W$)?

**Đầu vào (Input):**

Gồm hai số tự nhiên $K$ và $W$ ($1 \le K, W \le 10^6$) mỗi số trên một dòng.

**Đầu ra (Output):**

In ra hai số nguyên trên một dòng cách nhau dấu cách: `hang cot`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 11 <br> 4 | 3 3 |

**Giải thích:** Mỗi hàng có 4 ô.
Hàng 1: 1, 2, 3, 4
Hàng 2: 5, 6, 7, 8
Hàng 3: 9, 10, 11, 12.
Ô số 11 nằm ở Hàng 3, Cột 3.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là đánh số từ `1` nên phải trừ `1` trước: với `k = 11`, `w = 4` thì hàng `(11 - 1) // 4 + 1 = 10 // 4 + 1 = 2 + 1 = 3`, cột `(11 - 1) % 4 + 1 = 10 % 4 + 1 = 2 + 1 = 3`.
- Quy trình trong lời giải: đọc `k` dòng 1, đọc `w` dòng 2, tính `hang` và `cot` theo hai công thức trên rồi in `hang cot`.
- Xử lý biên: `k = 1, w = 10^6` cho hàng `1` cột `1`; `k = 4, w = 4` cho hàng `1` cột `4`; `k = 5, w = 4` sang hàng `2` cột `1`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 11 và 4 (hai dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc dòng 1, biến `k` nhận giá trị | `k = 11` |
| 2 | Đọc dòng 2, biến `w` nhận giá trị | `w = 4` |
| 3 | Tính `hang = (11 - 1) // 4 + 1` | `hang = 3` |
| 4 | Tính `cot = (11 - 1) % 4 + 1` | `cot = 3` |
| 5 | In kết quả | `3 3` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Quên trừ 1: `k // w + 1`.**

```python
print(k // w + 1, k % w + 1)
```

Với số liệu mẫu trên, đoạn này cho `11` và `4` cho `3 4` thay vì `3 3`.

Cách sửa: dùng `(k - 1) // w + 1` và `(k - 1) % w + 1`.

**Bẫy 2: Đọc hai số một dòng bằng `split()`.**

```python
k, w = map(int, input().split())
```

Với số liệu mẫu trên, đoạn này cho số liệu mẫu mỗi số một dòng nên nhận thiếu `w`.

Cách sửa: đọc hai lần `input()` riêng.

#### 4. Lời giải tham khảo

```python
k = int(input())
w = int(input())
hang = (k - 1) // w + 1
cot = (k - 1) % w + 1
print(hang, cot)
```

### Bài 34 [pya_l02_p17_tong_ba_chu_so]: Tổng các chữ số của số có 3 chữ số

Bối cảnh: Bạn Tâm tham gia cuộc thi đố vui toán học với thử thách: nhìn vào một số nguyên dương có đúng 3 chữ số, phải nhanh chóng cộng tổng cả ba chữ số lại. Ví dụ với số $496$, tổng các chữ số là $4 + 9 + 6 = 19$. Thay vì tính nhẩm, Tâm muốn viết một chương trình Python giúp tự động tách ba chữ số hàng trăm, hàng chục, hàng đơn vị rồi cộng lại.

Nhiệm vụ: Nhập số nguyên $N$ ($100 \le N \le 999$). In ra tổng của 3 chữ số hàng trăm, hàng chục và hàng đơn vị.

**Đầu vào (Input):**

Một dòng chứa số nguyên $N$.

**Đầu ra (Output):**

In ra tổng các chữ số.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 385 | 16 |

**Giải thích:** Chữ số hàng trăm $385 // 100 = 3$. Chữ số hàng chục $(385 // 10) \% 10 = 8$. Chữ số hàng đơn vị $385 \% 10 = 5$. Tổng $= 3 + 8 + 5 = 16$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là tách ba hàng rồi cộng: với `n = 385` thì trăm `385 // 100 = 3`, chục `(385 // 10) % 10 = 38 % 10 = 8`, đơn vị `385 % 10 = 5`, tổng `3 + 8 + 5 = 16`.
- Quy trình trong lời giải: đọc `n`, đặt ba biến `tram`, `chuc`, `don_vi` rồi in tổng của chúng.
- Xử lý biên: `n = 100` cho `1`; `n = 999` cho `27`; `n = 101` cho `2`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 385)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `n` nhận giá trị | `n = 385` |
| 2 | Tách `tram = 385 // 100` | `tram = 3` |
| 3 | Tách `chuc = (385 // 10) % 10` | `chuc = 8` |
| 4 | Tách `don_vi = 385 % 10` | `don_vi = 5` |
| 5 | Cộng và in `3 + 8 + 5` | `16` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Quên tách hàng chục, chỉ cộng trăm và đơn vị.**

```python
print(n // 100 + n % 10)
```

Với số liệu mẫu trên, đoạn này cho `385` cho `8` thay vì `16`.

Cách sửa: cộng thêm `(n // 10) % 10`.

**Bẫy 2: Viết `chuc = n // 10 % 100`.**

```python
chuc = n // 10 % 100
```

Với số liệu mẫu trên, đoạn này cho `385` thì `chuc = 38` nên tổng thành `46` thay vì `16`.

Cách sửa: dùng `(n // 10) % 10`.

#### 4. Lời giải tham khảo

```python
n = int(input())
tram = n // 100
chuc = (n // 10) % 10
don_vi = n % 10
print(tram + chuc + don_vi)
```

### Bài 35 [pya_l02_p36_phan_so_dai_so]: Tính phân số đại số

Bối cảnh: Trong phòng thí nghiệm vật lý, hai nhóm học sinh đo được các thông số $a$, $b$, $c$, $d$ từ thí nghiệm đo quang phổ. Công thức tổng hợp kết quả cuối cùng là một biểu thức phân số: $S = \frac{a + b}{c + d}$. Thầy giáo yêu cầu mỗi nhóm viết chương trình Python để tính tự động giá trị $S$, đảm bảo kết quả là số thực (phép chia thực) chứ không phải phép chia nguyên.

Nhiệm vụ: Nhập 4 số nguyên $a, b, c, d$ trên 1 dòng. In ra giá trị $S$ (làm tròn 2 chữ số thập phân).

**Đầu vào (Input):**

Một dòng chứa 4 số nguyên ($c + d \ne 0$).

**Đầu ra (Output):**

In ra giá trị số thực dạng `f"{S:.2f}"`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 7 8 2 3 | 3.00 |

**Giải thích:** $(7 + 8) / (2 + 3) = 15 / 5 = 3.00$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là chia thực hai tổng rồi làm tròn `2` chữ số: với `a = 7, b = 8, c = 2, d = 3` thì `(7 + 8) / (2 + 3) = 15 / 5 = 3.0`, in ra `3.00`.
- Quy trình trong lời giải: đọc một dòng `a, b, c, d` rồi in `f"{(a + b) / (c + d):.2f}"`; dùng `/` (chia thực) và định dạng `:.2f`.
- Xử lý biên: tổng mẫu khác `0` theo đề; `1 1 1 3` cho `0.50`; kết quả luôn có đúng `2` chữ số sau dấu chấm.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 7 8 2 3 (một dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, tách bốn biến | `a = 7`, `b = 8`, `c = 2`, `d = 3` |
| 2 | Tính tử `a + b` | `15` |
| 3 | Tính mẫu `c + d` | `5` |
| 4 | Chia `15 / 5` và làm tròn `2` chữ số | `3.00` |
| 5 | In kết quả | `3.00` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Dùng chia nguyên `//`.**

```python
print(f"{(a + b) // (c + d):.2f}")
```

Với số liệu mẫu trên, đoạn này cho `7 8 2 3` cho `3` rồi định dạng thành `3` (lỗi kiểu) hoặc mất phần lẻ với số liệu khác như `1 1 1 3` cho `0.00` thay vì `0.50`.

Cách sửa: dùng `/` chia thực.

**Bẫy 2: Quên làm tròn, chỉ `print((a + b) / (c + d))`.**

```python
print((a + b) / (c + d))
```

Với số liệu mẫu trên, đoạn này cho `7 8 2 3` in ra `3.0` thay vì `3.00`, thiếu một chữ số `0`.

Cách sửa: dùng `f"{...:.2f}"`.

**Bẫy 3: Bỏ ngoặc: `a + b / c + d`.**

```python
print(f"{a + b / c + d:.2f}")
```

Với số liệu mẫu trên, đoạn này cho `7 8 2 3` cho `12.00` thay vì `3.00`.

Cách sửa: giữ ngoặc `(a + b) / (c + d)`.

#### 4. Lời giải tham khảo

```python
a, b, c, d = map(int, input().split())
print(f"{(a + b) / (c + d):.2f}")
```

### Bài 36 [pya_l02_p18_so_dao_nguoc_3_chu_so]: Số đảo ngược 3 chữ số

Bối cảnh: Trong trò chơi "Gương thần kỳ diệu" tại lễ hội trường, mỗi thí sinh viết một số nguyên dương có đúng 3 chữ số lên bảng. Tấm gương ma thuật sẽ "phản chiếu" số đó — tức là đảo ngược thứ tự các chữ số. Ví dụ: số $123$ qua gương trở thành $321$, số $400$ trở thành $004$ (tức là $4$). Em hãy lập trình mô phỏng tấm gương thần này.

Nhiệm vụ: Nhập số nguyên $N$ gồm 3 chữ số ($100 \le N \le 999$, chữ số tận cùng khác 0). In ra số đảo ngược của $N$.

**Đầu vào (Input):**

Một dòng chứa số $N$.

**Đầu ra (Output):**

In ra số đảo ngược.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 472 | 274 |

**Giải thích:** Tách trăm $= 4$, chục $= 7$, đơn vị $= 2$. Số đảo ngược là $2 \times 100 + 7 \times 10 + 4 = 274$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất là đảo vị trí trăm và đơn vị: với `n = 472` thì trăm `4`, chục `7`, đơn vị `2`, số mới `2 * 100 + 7 * 10 + 4 = 200 + 70 + 4 = 274`.
- Quy trình trong lời giải: đọc `n`, tách `tram`, `chuc`, `don_vi` rồi in `don_vi * 100 + chuc * 10 + tram`.
- Xử lý biên: `n = 100` cho `1` (vì `001` là `1`); `n = 999` cho `999`; chữ số tận cùng khác `0` nên không mất chữ số giữa.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 472)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `n` nhận giá trị | `n = 472` |
| 2 | Tách `tram = 472 // 100` | `tram = 4` |
| 3 | Tách `chuc = 7`, `don_vi = 2` | `chuc = 7`, `don_vi = 2` |
| 4 | Ghép `2 * 100 + 7 * 10 + 4` | `274` |
| 5 | In kết quả | `274` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Ghép sai thứ tự `tram * 100 + ...` (in lại số cũ).**

```python
print(tram * 100 + chuc * 10 + don_vi)
```

Với số liệu mẫu trên, đoạn này cho `472` in ra `472` thay vì `274`.

Cách sửa: đặt `don_vi` lên hàng trăm.

**Bẫy 2: Quên nhân `100`, viết `don_vi + chuc * 10 + tram`.**

```python
print(don_vi + chuc * 10 + tram)
```

Với số liệu mẫu trên, đoạn này cho `472` cho `76` thay vì `274`.

Cách sửa: `don_vi * 100`.

#### 4. Lời giải tham khảo

```python
n = int(input())
tram = n // 100
chuc = (n // 10) % 10
don_vi = n % 10
print(don_vi * 100 + chuc * 10 + tram)
```

### Bài 01 [pya_l03_p31_doi_do_la_sang_tien_viet]: Đổi đô la sang tiền việt

Bối cảnh: Bác Hùng đi công tác ở nước ngoài về và mang theo $D$ tờ đô la Mỹ, mỗi tờ trị giá $1$ đô la. Bác muốn đổi hết sang tiền Việt Nam để mua quà cho cả nhà. Biết rằng ngân hàng đổi $1$ đô la lấy $25000$ đồng. Hãy giúp bác Hùng tính xem bác sẽ nhận được bao nhiêu tiền Việt Nam.

Nhiệm vụ: Hãy tính số tiền Việt Nam (đồng) đổi được từ $D$ đô la Mỹ.

**Đầu vào (Input):**

Nhập 1 số tự nhiên $D$ ($1 \le D \le 10^6$) trên 1 dòng.

**Đầu ra (Output):**

Số tiền Việt Nam tính bằng đồng (số nguyên).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 4 | 100000 |

**Giải thích:** - Mỗi đô la đổi được $25000$ đồng.
- $4$ đô la đổi được: $4 \times 25000 = 100000$ đồng.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là đổi tiền theo tỉ giá cố định: mỗi 1 đô la được 25000 đồng, nên số tiền Việt bằng `d * 25000`.
- Quy trình trong lời giải: đọc biến `d` bằng `int(input())`, rồi tính `d * 25000` và in ra; với mẫu `d = 4` thì `4 * 25000 = 100000`.
- Xử lý biên: `D` nhỏ nhất là 1 cho ra 25000 đồng, `D` lớn nhất là 1000000 cho ra 25000000000 đồng, phép nhân số nguyên luôn vừa.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4)

Với số mẫu `4`, chương trình phải in ra `100000`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `d = int(input())` | `d = 4` | nhận 4 đô la |
| 2 | Tính `d * 25000` | `4 * 25000 = 100000` | 100000 đồng |
| 3 | In kết quả | xuất `100000` | khớp kết quả mẫu `100000` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — nhân sai tỉ giá: viết `print(d * 2500)` thì với mẫu `d = 4` sẽ in ra `10000` thay vì `100000`; cách sửa là nhân đúng `25000`.
- Bẫy 2 — quên đổi chữ thành số: viết `d = input()` rồi `print(d * 25000)` thì với mẫu sẽ lặp chuỗi cho ra một dãy rất dài thay vì `100000`; cách sửa là bọc `int(input())`.
- Bẫy 3 — in kèm chữ: viết `print(d * 25000, "dong")` thì với mẫu in ra `100000 dong` thay vì `100000`; cách sửa là chỉ in con số.

#### 4. Lời giải tham khảo

```python
d = int(input())
print(d * 25000)
```

### Bài 02 [pya_l03_p01_hinh_vuong]: Chu vi và diện tích hình vuông

Bối cảnh: Bác thợ mộc Năm ở xưởng nội thất Hoàng Gia nhận được đơn hàng gia công một lô mặt bàn trà hình vuông cao cấp. Theo bản vẽ thiết kế, mỗi mặt bàn có cạnh dài $A$ mét. Trước khi cắt gỗ, bác cần tính chính xác chu vi (để dán viền bao quanh) và diện tích (để ước lượng lượng sơn phủ bề mặt) của mỗi tấm mặt bàn.

Nhiệm vụ: Nhập một số nguyên dương $A$ là cạnh hình vuông. In ra chu vi và diện tích của hình vuông trên cùng một dòng cách nhau dấu cách.

**Đầu vào (Input):**

Một dòng chứa số nguyên dương $A$ ($1 \le A \le 10^4$).

**Đầu ra (Output):**

In ra chu vi và diện tích cách nhau một dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 6 | 24 36 |

**Giải thích:** Chu vi $6 \times 4 = 24$, Diện tích $6 \times 6 = 36$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất hình học: hình vuông cạnh `a` có chu vi `4 * a` và diện tích `a * a`, cả hai đều tính từ cùng một số đọc vào.
- Quy trình trong lời giải: đọc biến `a` bằng `int(input())`, rồi in `4 * a` và `a * a` trên cùng một dòng; với mẫu `a = 6` thì chu vi `4 * 6 = 24` và diện tích `6 * 6 = 36`.
- Xử lý biên: `A` nhỏ nhất là 1 cho ra `4 1`, `A` lớn nhất là 10000 cho ra `40000 100000000`, đều là số nguyên vừa khít.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6)

Với số mẫu `6`, chương trình phải in ra `24 36`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a = int(input())` | `a = 6` | cạnh bằng 6 |
| 2 | Tính `4 * a` | `4 * 6 = 24` | chu vi 24 |
| 3 | Tính `a * a` | `6 * 6 = 36` | diện tích 36 |
| 4 | In kết quả | xuất `24 36` | khớp kết quả mẫu `24 36` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — nhầm công thức chu vi: viết `print(2 * a, a * a)` thì với mẫu in ra `12 36` thay vì `24 36`; cách sửa là nhân chu vi với 4.
- Bẫy 2 — in mỗi thứ một dòng: dùng hai lệnh in riêng thì với mẫu ra hai dòng thay vì một dòng `24 36`; cách sửa là in một lần `print(4 * a, a * a)`.
- Bẫy 3 — quên đổi kiểu: viết `a = input()` thì `4 * a` với mẫu lặp chuỗi cho ra kết quả lạ thay vì `24 36`; cách sửa là bọc `int(input())`.

#### 4. Lời giải tham khảo

```python
a = int(input())
print(4 * a, a * a)
```

### Bài 03 [pya_l03_p06_doi_don_vi_dai]: Đổi mét sang centimet và milimet

Bối cảnh: Trên công trường xây dựng cầu vượt, kỹ sư trưởng nhận được bản vẽ ghi kích thước bằng đơn vị mét, nhưng máy cắt thép CNC lại yêu cầu nhập liệu theo xen-ti-mét. Anh cần một công cụ chuyển đổi nhanh giữa các đơn vị đo chiều dài: $1$ mét $= 100$ xen-ti-mét, $1$ ki-lô-mét $= 1000$ mét. Em hãy lập trình thực hiện phép chuyển đổi đơn vị chiều dài.

Nhiệm vụ: Nhập số nguyên dương $M$ (đơn vị mét). In ra 2 số trên 1 dòng cách nhau dấu cách: độ dài tương ứng theo centimet ($\text{cm}$) và milimet ($\text{mm}$).

**Đầu vào (Input):**

Một dòng chứa số nguyên $M$ ($1 \le M \le 1000$).

**Đầu ra (Output):**

In ra hai số nguyên cách nhau dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3 | 300 3000 |

**Giải thích:** $3\text{m} = 300\text{cm} = 3000\text{mm}$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất đổi đơn vị dài: 1 mét bằng 100 xen-ti-mét và bằng 1000 mi-li-mét, nên từ `m` mét tính `m * 100` và `m * 1000`.
- Quy trình trong lời giải: đọc biến `m` bằng `int(input())`, rồi in `m * 100` và `m * 1000`; với mẫu `m = 3` thì `3 * 100 = 300` và `3 * 1000 = 3000`.
- Xử lý biên: `M` nhỏ nhất là 1 cho ra `100 1000`, `M` lớn nhất là 1000 cho ra `100000 1000000`, đều là số nguyên.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3)

Với số mẫu `3`, chương trình phải in ra `300 3000`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `m = int(input())` | `m = 3` | 3 mét |
| 2 | Tính `m * 100` | `3 * 100 = 300` | 300 xen-ti-mét |
| 3 | Tính `m * 1000` | `3 * 1000 = 3000` | 3000 mi-li-mét |
| 4 | In kết quả | xuất `300 3000` | khớp kết quả mẫu `300 3000` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — nhầm hệ số: viết `print(m * 10, m * 100)` thì với mẫu in ra `30 300` thay vì `300 3000`; cách sửa là nhân đúng 100 và 1000.
- Bẫy 2 — đọc hai số: viết `m, n = map(int, input().split())` thì với mẫu chỉ có một số `3` sẽ bị lỗi thiếu số; cách sửa là chỉ đọc một số `m`.
- Bẫy 3 — in xuống hai dòng: dùng hai lệnh in thì với mẫu ra hai dòng thay vì một dòng `300 3000`; cách sửa là in một lần trên cùng một dòng.

#### 4. Lời giải tham khảo

```python
m = int(input())
print(m * 100, m * 1000)
```

### Bài 04 [pya_l03_p20_khung_tranh_hinh_vuong]: Khung tranh hình vuông

Bối cảnh: Trong quy trình gia công khung nhôm kính, người thợ cần chuẩn bị thanh nẹp viền bao quanh một tấm kính hình vuông có cạnh độ dài $a$.

Nhiệm vụ: Cho độ dài cạnh hình vuông $a$. Hãy tính chu vi của khung hình vuông ($4 \times a$).

**Đầu vào (Input):**

Một số tự nhiên $a$ ($1 \le a \le 10^4$).

**Đầu ra (Output):**

In ra 2 số nguyên cách nhau một khoảng trắng: Chu vi và Diện tích.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 8 | 32 64 |

**Giải thích:** Cạnh hình vuông có độ dài $a = 6$. Chu vi của hình vuông được tính bằng $4 \times 6 = 24$. Kết quả in ra là `24`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này vẫn là hình vuông cạnh `a`: chu vi khung bằng `4 * a`, diện tích mặt kính bằng `a * a`.
- Quy trình trong lời giải: đọc biến `a` bằng `int(input())`, rồi in `4 * a` và `a * a`; với mẫu `a = 8` thì `4 * 8 = 32` và `8 * 8 = 64`.
- Xử lý biên: `a` nhỏ nhất là 1 cho ra `4 1`, `a` lớn nhất là 10000 cho ra `40000 100000000`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 8)

Với số mẫu `8`, chương trình phải in ra `32 64`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a = int(input())` | `a = 8` | cạnh bằng 8 |
| 2 | Tính `4 * a` | `4 * 8 = 32` | chu vi 32 |
| 3 | Tính `a * a` | `8 * 8 = 64` | diện tích 64 |
| 4 | In kết quả | xuất `32 64` | khớp kết quả mẫu `32 64` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — chỉ in chu vi: viết `print(4 * a)` thì với mẫu chỉ ra `32` mà thiếu `64`; cách sửa là in cả hai số `print(4 * a, a * a)`.
- Bẫy 2 — nhầm diện tích thành `2 * a`: viết `print(4 * a, 2 * a)` thì với mẫu ra `32 16` thay vì `32 64`; cách sửa là diện tích `a * a`.
- Bẫy 3 — quên đổi kiểu: viết `a = input()` thì `4 * a` lặp chuỗi thay vì ra `32 64`; cách sửa là bọc `int(input())`.

#### 4. Lời giải tham khảo

```python
a = int(input())
print(4 * a, a * a)
```

### Bài 05 [pya_l03_p14_doi_do_c_sang_do_f]: Đổi độ C sang độ F

Bối cảnh: Trong giờ học khoa học, cô giáo đố cả lớp một điều thú vị. Ở Việt Nam, nhiệt độ được đo bằng độ C, còn ở nước Mỹ người ta lại dùng độ F. Hôm nay trời nóng $C$ độ C, và $C$ luôn chia hết cho $5$. Hãy giúp cả lớp đổi nhiệt độ này sang độ F để kể cho người dùng ở Mỹ nghe.

Nhiệm vụ: Hãy đổi nhiệt độ $C$ độ C sang độ F theo công thức $F = C \times 9 : 5 + 32$.

**Đầu vào (Input):**

Nhập 1 số nguyên $C$ ($-50 \le C \le 50$, $C$ chia hết cho $5$) trên 1 dòng.

**Đầu ra (Output):**

Nhiệt độ tính bằng độ F (số nguyên).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 30 | 86 |

**Giải thích:** - Đổi sang độ F: $30 \times 9 : 5 + 32 = 270 : 5 + 32 = 54 + 32 = 86$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất đổi nhiệt độ: độ F bằng `C * 9 // 5 + 32`, đề bài đảm bảo `C` chia hết cho 5 nên phép chia nguyên cho kết quả đúng.
- Quy trình trong lời giải: đọc biến `c` bằng `int(input())`, rồi in `c * 9 // 5 + 32`; với mẫu `c = 30` thì `30 * 9 = 270`, `270 // 5 = 54`, `54 + 32 = 86`.
- Xử lý biên: `C` nhỏ nhất là -50 cho ra -58 độ F, `C` lớn nhất là 50 cho ra 122 độ F; chú ý số âm vẫn tính đúng vì chia hết cho 5.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 30)

Với số mẫu `30`, chương trình phải in ra `86`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `c = int(input())` | `c = 30` | 30 độ C |
| 2 | Tính `c * 9` | `30 * 9 = 270` | số 270 |
| 3 | Tính `270 // 5 + 32` | `54 + 32 = 86` | 86 độ F |
| 4 | In kết quả | xuất `86` | khớp kết quả mẫu `86` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — sai thứ tự cộng: viết `c * (9 // 5 + 32)` thì với mẫu `9 // 5 = 1` nên ra `30 * 33 = 990` thay vì `86`; cách sửa là viết `c * 9 // 5 + 32`.
- Bẫy 2 — dùng chia thực rồi quên làm tròn: viết `c * 9 / 5 + 32` có thể in ra `86.0` thay vì `86`; cách sửa là dùng chia nguyên `//` vì đề đảm bảo chia hết.
- Bẫy 3 — quên cộng 32: viết `print(c * 9 // 5)` thì với mẫu ra `54` thay vì `86`; cách sửa là cộng thêm 32.

#### 4. Lời giải tham khảo

```python
c = int(input())
print(c * 9 // 5 + 32)
```

### Bài 06 [pya_l03_p04_canh_con_lai_cua_hinh_chu_nhat]: Cạnh còn lại của hình chữ nhật

Bối cảnh: Ngoài làng có một cái ao cá hình chữ nhật rất mát, một cạnh của ao bằng $a\text{ mét}$ và chu vi của ao là $P\text{ mét}$ ($P$ là số chẵn). Cuối tuần, các người dùng rủ nhau ra ao câu cá và đố nhau tìm cạnh còn lại của ao. Hãy giúp các bạn tính độ dài cạnh còn lại.

Nhiệm vụ: Hãy tính và in ra độ dài của cạnh còn lại của hình chữ nhật.

**Đầu vào (Input):**

Gồm 2 dòng: dòng 1 chứa chu vi $P$ ($P$ chẵn, $P \le 10^6$), dòng 2 chứa độ dài cạnh đã biết $a$ ($1 \le a < P // 2$).

**Đầu ra (Output):**

Một số tự nhiên là độ dài cạnh còn lại.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 30 <br> 5 | 10 |

**Giải thích:** Nửa chu vi là: $30 : 2 = 15$. Cạnh còn lại: $15 - 5 = 10$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất hình chữ nhật: nửa chu vi bằng `P // 2`, cạnh còn lại bằng nửa chu vi trừ cạnh đã biết `a`.
- Quy trình trong lời giải: đọc `p` ở dòng 1 và `a` ở dòng 2, rồi in `p // 2 - a`; với mẫu `P = 30` và `a = 5` thì nửa chu vi `30 // 2 = 15` và cạnh còn lại `15 - 5 = 10`.
- Xử lý biên: đề cho `P` là số chẵn và `a` nhỏ hơn `P // 2` nên kết quả luôn là số tự nhiên dương.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 30\n5)

Với số mẫu dòng 1 là `30` và dòng 2 là `5`, chương trình phải in ra `10`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `p = int(input())` | `p = 30` | chu vi 30 |
| 2 | Đọc `a = int(input())` | `a = 5` | cạnh biết 5 |
| 3 | Tính `p // 2` | `30 // 2 = 15` | nửa chu vi 15 |
| 4 | Tính `15 - 5` | `10` | khớp kết quả mẫu `10` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đọc hai số một dòng: viết `p, a = map(int, input().split())` thì với mẫu mỗi số một dòng sẽ bị lỗi thiếu số; cách sửa là đọc hai lần `input()` riêng.
- Bẫy 2 — quên chia đôi chu vi: viết `print(p - a)` thì với mẫu ra `25` thay vì `10`; cách sửa là `p // 2 - a`.
- Bẫy 3 — dùng chia thực: viết `print(p / 2 - a)` thì với mẫu in ra `10.0` thay vì `10`; cách sửa là dùng chia nguyên `//`.

#### 4. Lời giải tham khảo

```python
p = int(input())
a = int(input())
print(p // 2 - a)
```

### Bài 07 [pya_l03_p11_dien_tich_tam_giac_vuong]: Diện tích tam giác vuông

Bối cảnh: Na có một miếng bánh hình tam giác vuông rất xinh. Hai cạnh góc vuông của miếng bánh dài $a\text{ cm}$ và $h\text{ cm}$. Tích $a \times h$ luôn là số chẵn. Na muốn biết miếng bánh của mình rộng bao nhiêu để khoe với cả lớp. Hãy tính diện tích miếng bánh.

Nhiệm vụ: Hãy tính diện tích của hình tam giác vuông có hai cạnh góc vuông là $a$ và $h$.

**Đầu vào (Input):**

Nhập 2 số tự nhiên $a$ và $h$ ($1 \le a, h \le 1000$, tích $a \times h$ chia hết cho $2$) trên 2 dòng.

**Đầu ra (Output):**

Diện tích của hình tam giác vuông (số nguyên).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 6 <br> 4 | 12 |

**Giải thích:** - Tích hai cạnh góc vuông: $6 \times 4 = 24$.
- Diện tích tam giác: $24 : 2 = 12$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất diện tích tam giác vuông: bằng nửa tích hai cạnh góc vuông, tức `a * h // 2`, đề đảm bảo tích chia hết cho 2.
- Quy trình trong lời giải: đọc `a` dòng 1 và `h` dòng 2, rồi in `a * h // 2`; với mẫu `a = 6` và `h = 4` thì `6 * 4 = 24` rồi `24 // 2 = 12`.
- Xử lý biên: `a` và `h` đều từ 1 đến 1000, tích lớn nhất `1000 * 1000 = 1000000` chia 2 được 500000.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6\n4)

Với số mẫu dòng 1 là `6` và dòng 2 là `4`, chương trình phải in ra `12`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a = int(input())` | `a = 6` | cạnh 6 |
| 2 | Đọc `h = int(input())` | `h = 4` | cạnh 4 |
| 3 | Tính `a * h` | `6 * 4 = 24` | tích 24 |
| 4 | Tính `24 // 2` | `12` | khớp kết quả mẫu `12` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên chia 2: viết `print(a * h)` thì với mẫu ra `24` thay vì `12`; cách sửa là chia nguyên cho 2.
- Bẫy 2 — đọc hai số một dòng: viết `a, h = map(int, input().split())` thì với mẫu mỗi số một dòng sẽ bị lỗi; cách sửa là đọc hai lần riêng.
- Bẫy 3 — dùng chia thực: viết `print(a * h / 2)` thì với mẫu in ra `12.0` thay vì `12`; cách sửa là dùng `//` vì đề đảm bảo chia hết.

#### 4. Lời giải tham khảo

```python
a = int(input())
h = int(input())
print(a * h // 2)
```

### Bài 08 [pya_l03_p21_chu_vi_tam_giac_abc]: Chu vi tam giác ABC

Bối cảnh: Trong giờ học hình học vui nhộn, thầy giáo vẽ một hình tam giác $ABC$ lên bảng và đố cả lớp. Thầy cho 3 số tự nhiên $a, b, c$ lần lượt là độ dài 3 cạnh của tam giác $ABC$. Các bạn thi nhau giơ tay xung phong tính chu vi. Hãy giúp cả lớp tính chu vi của tam giác $ABC$.

Nhiệm vụ: Hãy lập trình tính và đưa ra chu vi của tam giác $ABC$.

**Đầu vào (Input):**

Ba dòng lần lượt ghi 3 số tự nhiên $a, b, c$ ($1 \le a, b, c \le 10^8$).

**Đầu ra (Output):**

In ra một số tự nhiên duy nhất là chu vi tam giác.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3 <br> 4 <br> 5 | 12 |

**Giải thích:** Chu vi: $3 + 4 + 5 = 12$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất chu vi tam giác: cộng cả ba cạnh `a + b + c`, bài này mỗi cạnh nằm một dòng riêng.
- Quy trình trong lời giải: đọc `a`, `b`, `c` mỗi biến một lần `input()`, rồi in `a + b + c`; với mẫu `3`, `4`, `5` thì `3 + 4 + 5 = 12`.
- Xử lý biên: mỗi cạnh từ 1 đến 100000000, tổng lớn nhất là 300000000, phép cộng số nguyên luôn đúng.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3\n4\n5)

Với số mẫu ba dòng `3`, `4`, `5`, chương trình phải in ra `12`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a` | `a = 3` | cạnh 3 |
| 2 | Đọc `b` | `b = 4` | cạnh 4 |
| 3 | Đọc `c` | `c = 5` | cạnh 5 |
| 4 | Tính `a + b + c` | `3 + 4 + 5 = 12` | khớp kết quả mẫu `12` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đọc cả ba số một dòng: viết `a, b, c = map(int, input().split())` thì với mẫu mỗi số một dòng sẽ bị lỗi thiếu số; cách sửa là đọc ba lần riêng.
- Bẫy 2 — nhầm thành diện tích: viết `print(a * b * c)` thì với mẫu ra `60` thay vì `12`; cách sửa là cộng ba cạnh.
- Bẫy 3 — quên đổi kiểu một biến: nếu `c` còn là chuỗi thì phép cộng bị lỗi; cách sửa là cả ba đều `int(input())`.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
```

### Bài 09 [pya_l03_p30_the_tich_hop_chu_nhat]: Thể tích hộp chữ nhật

Bối cảnh: Một khối hộp vừa được tặng một hộp sữa dâu hình hộp chữ nhật. Hộp sữa có chiều dài $d\text{ cm}$, chiều rộng $r\text{ cm}$ và chiều cao $c\text{ cm}$. Một khối hộp tò mò muốn biết hộp sữa của mình chứa được bao nhiêu sữa. Hãy giúp bài toán tính thể tích của hộp sữa.

Nhiệm vụ: Hãy tính thể tích của hình hộp chữ nhật có ba kích thước $d, r, c$.

**Đầu vào (Input):**

Nhập 3 số tự nhiên $d, r, c$ ($1 \le d, r, c \le 1000$) trên 3 dòng.

**Đầu ra (Output):**

Thể tích của hình hộp chữ nhật (số nguyên).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 5 <br> 3 <br> 2 | 30 |

**Giải thích:** - Thể tích hộp: $5 \times 3 \times 2 = 30$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất thể tích hộp chữ nhật: nhân ba kích thước `d * r * c`, mỗi kích thước nằm một dòng riêng.
- Quy trình trong lời giải: đọc `d`, `r`, `c` mỗi biến một lần `input()`, rồi in `d * r * c`; với mẫu `5`, `3`, `2` thì `5 * 3 * 2 = 30`.
- Xử lý biên: mỗi kích thước từ 1 đến 1000, thể tích lớn nhất là 1000000000, số nguyên luôn vừa.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5\n3\n2)

Với số mẫu ba dòng `5`, `3`, `2`, chương trình phải in ra `30`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `d` | `d = 5` | dài 5 |
| 2 | Đọc `r` | `r = 3` | rộng 3 |
| 3 | Đọc `c` | `c = 2` | cao 2 |
| 4 | Tính `d * r * c` | `5 * 3 * 2 = 30` | khớp kết quả mẫu `30` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đọc ba số một dòng: viết `d, r, c = map(int, input().split())` thì với mẫu mỗi số một dòng sẽ bị lỗi; cách sửa là đọc ba lần riêng.
- Bẫy 2 — cộng thay vì nhân: viết `print(d + r + c)` thì với mẫu ra `10` thay vì `30`; cách sửa là nhân ba số.
- Bẫy 3 — nhầm diện tích xung quanh: viết `print(2 * (d * r + r * c))` thì với mẫu ra số khác `30`; cách sửa là thể tích `d * r * c`.

#### 4. Lời giải tham khảo

```python
d = int(input())
r = int(input())
c = int(input())
print(d * r * c)
```

### Bài 10 [pya_l03_p19_manh_vuon_chu_nhat]: Mảnh vườn chữ nhật

Bối cảnh: Cuối làng có bác nông dân chăm chỉ với một mảnh vườn trồng rau hình chữ nhật có chiều dài $a\text{ mét}$ và chiều rộng $b\text{ mét}$. Mỗi sáng, bác ra vườn tưới rau xanh mướt, nhưng bác muốn rào quanh vườn và tính diện tích để trồng thêm rau mới. Hãy giúp bác tính chu vi và diện tích của mảnh vườn.

Nhiệm vụ: Hãy tính chu vi và diện tích của mảnh vườn đó.

**Đầu vào (Input):**

Gồm 2 dòng lần lượt chứa 2 số tự nhiên $a$ và $b$ ($1 \le b \le a \le 10^4$).

**Đầu ra (Output):**

In ra trên một dòng 2 số nguyên cách nhau một dấu cách lần lượt là: Chu vi và Diện tích của mảnh vườn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 <br> 6 | 32 60 |

**Giải thích:** Chu vi: $(10 + 6) \times 2 = 32$. Diện tích: $10 \times 6 = 60$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất mảnh vườn chữ nhật: chu vi `(a + b) * 2` và diện tích `a * b`, cả hai tính từ dài `a` và rộng `b`.
- Quy trình trong lời giải: đọc `a` dòng 1 và `b` dòng 2, đặt `chu_vi = (a + b) * 2` và `dien_tich = a * b`; với mẫu `a = 10` và `b = 6` thì chu vi `(10 + 6) * 2 = 32` và diện tích `10 * 6 = 60`.
- Xử lý biên: đề cho `b` không vượt quá `a` và cả hai tới 10000, chu vi lớn nhất là 40000, diện tích lớn nhất là 100000000.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10\n6)

Với số mẫu dòng 1 là `10` và dòng 2 là `6`, chương trình phải in ra `32 60`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a` | `a = 10` | dài 10 |
| 2 | Đọc `b` | `b = 6` | rộng 6 |
| 3 | Tính `(a + b) * 2` | `(10 + 6) * 2 = 32` | chu vi 32 |
| 4 | Tính `a * b` | `10 * 6 = 60` | diện tích 60, xuất `32 60` khớp mẫu |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — thiếu ngoặc: viết `a + b * 2` thì với mẫu ra `10 + 12 = 22` thay vì `32`; cách sửa là `(a + b) * 2`.
- Bẫy 2 — đọc hai số một dòng: viết `a, b = map(int, input().split())` thì với mẫu mỗi số một dòng sẽ bị lỗi; cách sửa là đọc hai lần riêng.
- Bẫy 3 — in hai dòng: dùng hai lệnh in thì với mẫu ra hai dòng thay vì một dòng `32 60`; cách sửa là `print(chu_vi, dien_tich)`.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
chu_vi = (a + b) * 2
dien_tich = a * b
print(chu_vi, dien_tich)
```

### Bài 11 [pya_l03_p10_dien_tich_bon_hoa_chu_thap]: Diện tích bồn hoa chữ thập

Bối cảnh: Trong công viên xanh mát có một bồn hoa hình chữ thập (dấu cộng) rất đẹp được tạo thành bởi hai luống hoa hình chữ nhật đặt chồng lên nhau:
 * Một luống hoa nằm ngang có kích thước $a \times b$ ($a$ là chiều dài, $b$ là chiều rộng).
 * Một luống hoa nằm dọc có kích thước $b \times a$ ($b$ là chiều rộng, $a$ là chiều dài).
 * Hai luống hoa giao nhau ở chính giữa tạo thành một hình vuông kích thước $b \times b$.
Cô công nhân muốn biết diện tích thật để gieo hạt, vì phần giao nhau ở giữa không được tính hai lần. Hãy giúp cô tính diện tích bồn hoa.

Nhiệm vụ: Hãy tính diện tích thực tế của toàn bộ bồn hoa chữ thập này (không được tính trùng lặp phần diện tích giao nhau ở chính giữa).

**Đầu vào (Input):**

Nhập 2 số tự nhiên $a$ và $b$ ($1 \le b \le a \le 10^4$) trên 2 dòng.

**Đầu ra (Output):**

Diện tích thực tế của bồn hoa.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 <br> 3 | 51 |

**Giải thích:** - Luống ngang: $10 \times 3 = 30$.
- Luống dọc: $3 \times 10 = 30$.
- Phần giao nhau ở giữa: $3 \times 3 = 9$.
- Diện tích bồn hoa: $30 + 30 - 9 = 51$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất bồn hoa chữ thập: hai luống `a * b` cộng lại rồi trừ phần giao nhau `b * b`, tức `2 * a * b - b * b`.
- Quy trình trong lời giải: đọc `a` dòng 1 và `b` dòng 2, rồi in `2 * a * b - b * b`; với mẫu `a = 10` và `b = 3` thì `2 * 10 * 3 = 60`, `3 * 3 = 9`, `60 - 9 = 51`.
- Xử lý biên: đề cho `b` không vượt quá `a`, cả hai tới 10000, diện tích lớn nhất gần 200000000.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10\n3)

Với số mẫu dòng 1 là `10` và dòng 2 là `3`, chương trình phải in ra `51`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a` | `a = 10` | dài 10 |
| 2 | Đọc `b` | `b = 3` | rộng 3 |
| 3 | Tính `2 * a * b` | `2 * 10 * 3 = 60` | tổng hai luống 60 |
| 4 | Tính `60 - b * b` | `60 - 9 = 51` | khớp kết quả mẫu `51` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên trừ phần giao: viết `print(2 * a * b)` thì với mẫu ra `60` thay vì `51`; cách sửa là trừ thêm `b * b`.
- Bẫy 2 — trừ hai lần phần giao: viết `print(2 * a * b - 2 * b * b)` thì với mẫu ra `42` thay vì `51`; cách sửa là chỉ trừ một lần `b * b`.
- Bẫy 3 — đọc hai số một dòng: viết `a, b = map(int, input().split())` thì với mẫu mỗi số một dòng sẽ bị lỗi; cách sửa là đọc hai lần riêng.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
print(2 * a * b - b * b)
```

### Bài 12 [pya_l03_p08_thuan_di_gap_anh]: Thuận đi gặp ánh

Bối cảnh: Chiều nắng đẹp, hai bạn Thuận và Ánh sống trên một con đường làng thẳng có các mốc tọa độ tính bằng kilomet. Thuận đang đứng ở vị trí $x$, còn Ánh đang đứng ở vị trí $y$ ($x < y$). Thuận nhảy lên xe đạp và phóng về phía nhà Ánh với vận tốc không đổi là $v\text{ km/h}$ để rủ bạn đi đá bóng.
* **Biết rằng:** Khoảng cách $y - x$ chia hết cho vận tốc $v$.
Ánh đứng chờ ở cổng, hồi hộp không biết bao lâu bạn tới. Hãy giúp hai bạn tính thời gian Thuận đi gặp Ánh.

Nhiệm vụ: Sau bao nhiêu giờ thì Thuận sẽ gặp được Ánh?

**Đầu vào (Input):**

Ba dòng lần lượt chứa 3 số tự nhiên $x, y, v$ ($0 \le x < y \le 10^9, 1 \le v \le 10^9$).

**Đầu ra (Output):**

Số giờ để Thuận gặp Ánh.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 <br> 70 <br> 15 | 4 |

**Giải thích:** Khoảng cách giữa 2 bạn: $70 - 10 = 60\text{ km}$.
Thời gian gặp nhau: $60 : 15 = 4$ giờ.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất chuyển động: quãng đường Thuận phải đi là `y - x`, thời gian bằng quãng đường chia vận tốc `v`.
- Quy trình trong lời giải: đọc `x`, `y`, `v` mỗi biến một dòng, rồi in `(y - x) // v`; với mẫu `x = 10`, `y = 70`, `v = 15` thì `70 - 10 = 60` và `60 // 15 = 4`.
- Xử lý biên: đề đảm bảo `x` nhỏ hơn `y` và hiệu `y - x` chia hết cho `v`, nên chia nguyên cho kết quả đúng; tọa độ tới 1000000000.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10\n70\n15)

Với số mẫu ba dòng `10`, `70`, `15`, chương trình phải in ra `4`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `x`, `y`, `v` | `x = 10`, `y = 70`, `v = 15` | đủ ba số |
| 2 | Tính `y - x` | `70 - 10 = 60` | quãng đường 60 |
| 3 | Tính `60 // 15` | `4` | khớp kết quả mẫu `4` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — trừ ngược: viết `print((x - y) // v)` thì với mẫu ra số âm thay vì `4`; cách sửa là `y - x`.
- Bẫy 2 — đọc ba số một dòng: viết `x, y, v = map(int, input().split())` thì với mẫu mỗi số một dòng sẽ bị lỗi; cách sửa là đọc ba lần riêng.
- Bẫy 3 — dùng chia thực: viết `print((y - x) / v)` thì với mẫu in ra `4.0` thay vì `4`; cách sửa là dùng chia nguyên `//`.

#### 4. Lời giải tham khảo

```python
x = int(input())
y = int(input())
v = int(input())
print((y - x) // v)
```

### Bài 13 [pya_l03_p23_ho_ca_sau_va_dao_nho]: Hồ cá sấu và đảo nhỏ

Bối cảnh: Ở một trang trại vui vẻ có một hồ nước hình vuông cạnh $A$ nuôi những chú cá sấu con hiền lành. Ở chính giữa hồ, người ta xây một hòn đảo nhỏ hình chữ nhật có kích thước $B \times C$ để cá sấu bò lên phơi nắng (hòn đảo nằm trọn trong hồ nước và không chạm vào bờ hồ). Các người dùng thắc mắc mặt nước còn lại rộng bao nhiêu để cá bơi lội. Hãy giúp các bạn tính diện tích mặt nước còn lại.

Nhiệm vụ: Hãy tính diện tích phần mặt nước còn lại sau khi đã xây hòn đảo nhỏ.

**Đầu vào (Input):**

Ba số tự nhiên $A, B, C$ trên 3 dòng ($1 \le B, C < A \le 10^4$).

**Đầu ra (Output):**

Một số nguyên duy nhất là diện tích mặt nước còn lại.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 <br> 3 <br> 4 | 88 |

**Giải thích:** Diện tích hồ: $10 \times 10 = 100$. Diện tích đảo: $3 \times 4 = 12$.
Mặt nước còn lại: $100 - 12 = 88$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất diện tích còn lại: diện tích hồ `a * a` trừ diện tích đảo `b * c`.
- Quy trình trong lời giải: đọc `a`, `b`, `c` mỗi biến một dòng, rồi in `a * a - b * c`; với mẫu `a = 10`, `b = 3`, `c = 4` thì hồ `10 * 10 = 100`, đảo `3 * 4 = 12`, còn lại `100 - 12 = 88`.
- Xử lý biên: đề cho `B` và `C` đều nhỏ hơn `A` tới 10000 nên mặt nước còn lại luôn dương.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10\n3\n4)

Với số mẫu ba dòng `10`, `3`, `4`, chương trình phải in ra `88`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a`, `b`, `c` | `a = 10`, `b = 3`, `c = 4` | đủ ba số |
| 2 | Tính `a * a` | `10 * 10 = 100` | diện tích hồ 100 |
| 3 | Tính `b * c` | `3 * 4 = 12` | diện tích đảo 12 |
| 4 | Tính `100 - 12` | `88` | khớp kết quả mẫu `88` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — cộng thay vì trừ: viết `print(a * a + b * c)` thì với mẫu ra `112` thay vì `88`; cách sửa là lấy hồ trừ đảo.
- Bẫy 2 — nhầm đảo thành hình vuông: viết `print(a * a - b * b)` thì với mẫu ra `91` thay vì `88`; cách sửa là đảo `b * c`.
- Bẫy 3 — đọc ba số một dòng: viết `a, b, c = map(int, input().split())` thì với mẫu mỗi số một dòng sẽ bị lỗi; cách sửa là đọc ba lần riêng.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
c = int(input())
print(a * a - b * c)
```

### Bài 14 [pya_l03_p03_chu_vi_tam_giac]: Chu vi hình tam giác

Bối cảnh: Đội thi đấu robotics của trường cần thiết kế một tấm chắn bảo vệ hình tam giác cho robot chiến đấu. Ba cạnh của tấm chắn có độ dài lần lượt là $a$, $b$ và $c$ xen-ti-mét. Để mua đủ thanh nhôm gia cố viền ngoài, đội trưởng cần tính chính xác chu vi của tấm chắn tam giác này.

Nhiệm vụ: Nhập 3 số nguyên dương $A, B, C$ trên cùng một dòng. In ra chu vi của bồn hoa đó.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên dương $A, B, C$ ($1 \le A, B, C \le 10^4$).

**Đầu ra (Output):**

In ra chu vi hình tam giác.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 5 7 8 | 20 |

**Giải thích:** Chu vi $= 5 + 7 + 8 = 20$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất chu vi tam giác: cộng ba cạnh `a + b + c`, bài này cả ba số nằm trên cùng một dòng.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `a, b, c`, sau đó in `a + b + c`; với mẫu `5 7 8` thì `5 + 7 + 8 = 20`.
- Xử lý biên: mỗi cạnh từ 1 đến 10000, tổng lớn nhất là 30000.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 7 8)

Với số mẫu một dòng `5 7 8`, chương trình phải in ra `20`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a, b, c` | `a = 5`, `b = 7`, `c = 8` | đủ ba cạnh |
| 2 | Tính `a + b + c` | `5 + 7 + 8 = 20` | chu vi 20 |
| 3 | In kết quả | xuất `20` | khớp kết quả mẫu `20` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đọc ba dòng riêng: dùng ba lần `input()` thì với mẫu chỉ có một dòng `5 7 8` sẽ phải chờ thêm; cách sửa là `map(int, input().split())` một dòng.
- Bẫy 2 — nhân thay vì cộng: viết `print(a * b * c)` thì với mẫu ra `280` thay vì `20`; cách sửa là cộng ba cạnh.
- Bẫy 3 — quên tách chữ: viết `a = int(input())` thì với mẫu `5 7 8` bị lỗi đổi chữ; cách sửa là tách dòng bằng `split()`.

#### 4. Lời giải tham khảo

```python
a, b, c = map(int, input().split())
print(a + b + c)
```

### Bài 15 [pya_l03_p09_phut_sang_gio_phut]: Đổi phút sang giờ và phút

Bối cảnh: Tại trung tâm huấn luyện thể thao quốc gia, huấn luyện viên ghi lại thời gian thi đấu của vận động viên bằng tổng số phút (ví dụ: $135$ phút). Để báo cáo lên ban huấn luyện, anh cần quy đổi sang dạng "$X$ giờ $Y$ phút" cho trực quan. Em hãy viết chương trình chuyển đổi từ tổng số phút sang dạng giờ-phút.

Nhiệm vụ: Nhập số nguyên dương $M$ ($1 \le M \le 10^6$). In ra định dạng `X gio Y phut`.

**Đầu vào (Input):**

Một dòng chứa số nguyên $M$.

**Đầu ra (Output):**

In ra định dạng `X gio Y phut`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 135 | 2 gio 15 phut |

**Giải thích:** $135 // 60 = 2$ giờ và $135 \% 60 = 15$ phút.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất đổi phút: số giờ bằng `m // 60`, số phút lẻ bằng `m % 60`, rồi in theo mẫu `X gio Y phut`.
- Quy trình trong lời giải: đọc biến `m`, rồi in chuỗi ghép `m // 60` và `m % 60`; với mẫu `m = 135` thì `135 // 60 = 2` và `135 % 60 = 15` nên ra `2 gio 15 phut`.
- Xử lý biên: `M` nhỏ nhất là 1 cho ra `0 gio 1 phut`, `M` lớn nhất là 1000000 cho ra `16666 gio 40 phut`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 135)

Với số mẫu `135`, chương trình phải in ra `2 gio 15 phut`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `m = int(input())` | `m = 135` | 135 phút |
| 2 | Tính `m // 60` | `135 // 60 = 2` | 2 giờ |
| 3 | Tính `m % 60` | `135 % 60 = 15` | lẻ 15 phút, xuất `2 gio 15 phut` khớp mẫu |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng chia thực: viết `m / 60` thì với mẫu ra `2.25` thay vì `2 gio 15 phut`; cách sửa là dùng `//` và `%`.
- Bẫy 2 — sai chữ in: viết `2 giờ 15 phút` có dấu thì chương trình kiểm tra không nhận; cách sửa là in đúng `gio` và `phut` không dấu.
- Bẫy 3 — quên ép kiểu: viết `m = input()` thì `m // 60` bị lỗi vì chuỗi không chia được; cách sửa là `int(input())`.

#### 4. Lời giải tham khảo

```python
m = int(input())
print(f"{m // 60} gio {m % 60} phut")
```

### Bài 16 [pya_l03_p33_tinh_van_toc_lam_tron]: Tính vận tốc làm tròn

Bối cảnh: Cuối tuần, bạn Mít đạp xe đi thăm bà ngoại. Quãng đường từ nhà Mít đến nhà bà dài $D\text{ km}$, và bạn Mít đạp xe hết $T$ giờ. Mẹ dặn bạn Mít phải ghi lại vận tốc trung bình của chuyến đi, làm tròn đến đúng $2$ chữ số sau dấu chấm thập phân. Hãy giúp bạn Mít tính vận tốc của chuyến đi.

Nhiệm vụ: Hãy tính vận tốc trung bình $V = D : T$ (km/h) và in ra kết quả làm tròn đến $2$ chữ số thập phân.

**Đầu vào (Input):**

Nhập 2 số trên 2 dòng: quãng đường $D$ ($1 \le D \le 10^4$) và thời gian $T$ ($1 \le T \le 10^4$). Cả hai đều là số nguyên.

**Đầu ra (Output):**

Vận tốc trung bình làm tròn đến $2$ chữ số thập phân.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 100 <br> 6 | 16.67 |

**Giải thích:** - Vận tốc: $100 : 6 = 16.666\ldots$.
- Làm tròn đến $2$ chữ số thập phân được $16.67$ km/h.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất vận tốc trung bình: quãng đường `d` chia thời gian `t`, rồi làm tròn đúng 2 chữ số sau dấu chấm.
- Quy trình trong lời giải: đọc `d` dòng 1 và `t` dòng 2, rồi in `d / t` với 2 chữ số thập phân; với mẫu `d = 100` và `t = 6` thì `100 / 6 = 16.666...` làm tròn thành `16.67`.
- Xử lý biên: `D` và `T` đều từ 1 đến 10000, vận tốc nhỏ nhất là 0.0001, lớn nhất là 10000, luôn in đủ 2 chữ số kể cả số tròn.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 100\n6)

Với số mẫu dòng 1 là `100` và dòng 2 là `6`, chương trình phải in ra `16.67`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `d` | `d = 100` | quãng đường 100 |
| 2 | Đọc `t` | `t = 6` | thời gian 6 |
| 3 | Tính `d / t` | `100 / 6 = 16.666...` | làm tròn `16.67` khớp mẫu |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng chia nguyên: viết `print(d // t)` thì với mẫu ra `16` thay vì `16.67`; cách sửa là chia thực `d / t` rồi làm tròn 2 chữ số.
- Bẫy 2 — in thô không làm tròn: viết `print(d / t)` thì với mẫu ra `16.666666666666668` thay vì `16.67`; cách sửa là ghi định dạng 2 chữ số thập phân.
- Bẫy 3 — đọc hai số một dòng: viết `d, t = map(int, input().split())` thì với mẫu mỗi số một dòng sẽ bị lỗi; cách sửa là đọc hai lần riêng.

#### 4. Lời giải tham khảo

```python
d = int(input())
t = int(input())
print(f"{d / t:.2f}")
```

### Bài 17 [pya_l03_p25_lat_gach_san_truong]: Lát gạch sân trường

Bối cảnh: Sân trường của trường học sinh iKHEDU có hình chữ nhật dài $D\text{ mét}$ và rộng $R\text{ mét}$, nơi các bạn chơi nhảy dây mỗi giờ ra chơi. Hè này, nhà trường muốn lát gạch men cho toàn bộ sân trường bằng các viên gạch hình vuông có cạnh là $K\text{ mét}$ ($D$ và $R$ đều chia hết cho $K$). Bác lao công đã chở gạch đến đầy sân. Hãy giúp bác đếm số viên gạch cần dùng.

Nhiệm vụ: Tính số lượng viên gạch men cần dùng để lát kín mặt sân.

**Đầu vào (Input):**

Ba dòng lần lượt chứa 3 số tự nhiên $D, R, K$ ($1 \le K \le R \le D \le 1000$).

**Đầu ra (Output):**

Một số nguyên duy nhất là số viên gạch.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 20 <br> 10 <br> 2 | 50 |

**Giải thích:** Diện tích sân: $20 \times 10 = 200$. Diện tích 1 viên gạch: $2 \times 2 = 4$.
Số gạch cần: $200 : 4 = 50$ viên.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất lát gạch: số gạch bằng diện tích sân `d * r` chia diện tích một viên `k * k`, đề đảm bảo chia hết.
- Quy trình trong lời giải: đọc `d`, `r`, `k` mỗi biến một dòng, rồi in `d * r // (k * k)`; với mẫu `d = 20`, `r = 10`, `k = 2` thì sân `20 * 10 = 200`, gạch `2 * 2 = 4`, số viên `200 // 4 = 50`.
- Xử lý biên: `K` không vượt quá `R` và `R` không vượt quá `D` tới 1000, số gạch ít nhất là 1.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 20\n10\n2)

Với số mẫu ba dòng `20`, `10`, `2`, chương trình phải in ra `50`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `d`, `r`, `k` | `d = 20`, `r = 10`, `k = 2` | đủ ba số |
| 2 | Tính `d * r` | `20 * 10 = 200` | diện tích sân 200 |
| 3 | Tính `k * k` | `2 * 2 = 4` | diện tích viên 4 |
| 4 | Tính `200 // 4` | `50` | khớp kết quả mẫu `50` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — thiếu ngoặc: viết `d * r // k * k` thì với mẫu tính thành `(200 // 2) * 2 = 200` thay vì `50`; cách sửa là `d * r // (k * k)`.
- Bẫy 2 — đọc ba số một dòng: viết `d, r, k = map(int, input().split())` thì với mẫu mỗi số một dòng sẽ bị lỗi; cách sửa là đọc ba lần riêng.
- Bẫy 3 — dùng chia thực: viết `print(d * r / (k * k))` thì với mẫu in ra `50.0` thay vì `50`; cách sửa là dùng chia nguyên `//`.

#### 4. Lời giải tham khảo

```python
d = int(input())
r = int(input())
k = int(input())
print(d * r // (k * k))
```

### Bài 18 [pya_l03_p27_rao_quanh_vuon_hoa_co_cua]: Rào quanh vườn hoa có cửa

Bối cảnh: Bác thợ làm vườn có một vườn hoa rực rỡ hình chữ nhật với chiều dài $a\text{ mét}$, chiều rộng $b\text{ mét}$, thơm ngát mùi hoa hồng. Bác muốn dựng một hàng rào thép gai xung quanh vườn hoa, nhưng chừa lại một lối đi ở một góc vườn làm cổng ra vào rộng đúng $c\text{ mét}$ (không rào cửa).
* **Biết giá thành làm rào:** Mỗi mét hàng rào tốn $15$ nghìn đồng.
Bác đã chuẩn bị tiền nhưng chưa biết có đủ không. Hãy giúp bác tính tổng số tiền mua rào.

Nhiệm vụ: Tính tổng số tiền (nghìn đồng) bác thợ cần dùng để mua đủ rào thép.

**Đầu vào (Input):**

Ba dòng lần lượt là $a, b, c$ ($1 \le a, b \le 10^4, 1 \le c < (a + b) * 2$).

**Đầu ra (Output):**

Một số nguyên là số tiền (nghìn đồng).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 12 <br> 8 <br> 2 | 570 |

**Giải thích:** Chu vi cả vườn: $(12 + 8) \times 2 = 40\text{ m}$.
Độ dài rào cần mua: $40 - 2 = 38\text{ m}$.
Số tiền: $38 \times 15 = 570$ nghìn đồng.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất tiền rào: chu vi vườn `(a + b) * 2` trừ cửa `c` rồi nhân đơn giá 15 nghìn một mét.
- Quy trình trong lời giải: đọc `a`, `b`, `c` mỗi biến một dòng, rồi in `((a + b) * 2 - c) * 15`; với mẫu `a = 12`, `b = 8`, `c = 2` thì chu vi `(12 + 8) * 2 = 40`, rào `40 - 2 = 38`, tiền `38 * 15 = 570`.
- Xử lý biên: `a` và `b` tới 10000, `c` nhỏ hơn chu vi nên độ dài rào luôn dương.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12\n8\n2)

Với số mẫu ba dòng `12`, `8`, `2`, chương trình phải in ra `570`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a`, `b`, `c` | `a = 12`, `b = 8`, `c = 2` | đủ ba số |
| 2 | Tính `(a + b) * 2` | `(12 + 8) * 2 = 40` | chu vi 40 |
| 3 | Tính `(40 - 2) * 15` | `38 * 15 = 570` | khớp kết quả mẫu `570` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên trừ cửa: viết `print((a + b) * 2 * 15)` thì với mẫu ra `600` thay vì `570`; cách sửa là trừ `c` trước khi nhân 15.
- Bẫy 2 — quên nhân đơn giá: viết `print((a + b) * 2 - c)` thì với mẫu ra `38` thay vì `570`; cách sửa là nhân thêm 15.
- Bẫy 3 — đọc ba số một dòng: viết `a, b, c = map(int, input().split())` thì với mẫu mỗi số một dòng sẽ bị lỗi; cách sửa là đọc ba lần riêng.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
c = int(input())
print(((a + b) * 2 - c) * 15)
```

### Bài 19 [pya_l03_p02_hinh_chu_nhat]: Chu vi và diện tích hình chữ nhật

Bối cảnh: Sân bóng rổ đa năng của trường trung học cơ sở Lê Quý Đôn vừa được tân trang lại. Theo bản đo đạc, sân có chiều dài $A$ mét và chiều rộng $B$ mét. Ban quản lý cơ sở vật chất cần tính chu vi sân để mua đủ lưới rào bảo vệ, đồng thời tính diện tích sân để đặt mua sơn kẻ vạch sân thi đấu theo tiêu chuẩn.

Nhiệm vụ: Nhập hai số nguyên dương $A$ và $B$ trên cùng 1 dòng. In ra chu vi và diện tích của sân bóng rổ trên cùng một dòng cách nhau dấu cách.

**Đầu vào (Input):**

Một dòng chứa hai số nguyên dương $A, B$ ($1 \le B \le A \le 10^4$).

**Đầu ra (Output):**

In ra chu vi và diện tích.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 6 | 32 60 |

**Giải thích:** Chu vi $2 \times (10 + 6) = 32$, Diện tích $10 \times 6 = 60$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất sân chữ nhật: chu vi `2 * (a + b)` và diện tích `a * b`, cả hai số `a` và `b` nằm trên cùng một dòng.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `a, b`, sau đó in `2 * (a + b)` và `a * b`; với mẫu `10 6` thì chu vi `2 * (10 + 6) = 32` và diện tích `10 * 6 = 60`.
- Xử lý biên: đề cho `B` không vượt quá `A` tới 10000, chu vi lớn nhất là 40000, diện tích lớn nhất là 100000000.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10 6)

Với số mẫu một dòng `10 6`, chương trình phải in ra `32 60`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a, b` | `a = 10`, `b = 6` | dài 10 rộng 6 |
| 2 | Tính `2 * (a + b)` | `2 * 16 = 32` | chu vi 32 |
| 3 | Tính `a * b` | `10 * 6 = 60` | diện tích 60, xuất `32 60` khớp mẫu |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — thiếu ngoặc: viết `2 * a + b` thì với mẫu ra `26` thay vì `32`; cách sửa là `2 * (a + b)`.
- Bẫy 2 — đọc hai dòng riêng: dùng hai lần `input()` thì với mẫu một dòng `10 6` dòng thứ hai bị treo chờ; cách sửa là tách một dòng bằng `split()`.
- Bẫy 3 — in xuống hai dòng: dùng hai lệnh in thì với mẫu ra hai dòng thay vì một dòng `32 60`; cách sửa là in một lần.

#### 4. Lời giải tham khảo

```python
a, b = map(int, input().split())
print(2 * (a + b), a * b)
```

### Bài 20 [pya_l03_p07_doi_khoi_luong]: Đổi tạ và yến sang kilogram

Bối cảnh: Tại cảng xuất khẩu nông sản Cát Lái, mỗi container hàng ghi trọng lượng bằng đơn vị gam. Tuy nhiên, phiếu hải quan yêu cầu khai báo bằng ki-lô-gam và tấn. Nhân viên kho vận cần một chương trình chuyển đổi nhanh giữa các đơn vị khối lượng: $1$ ki-lô-gam $= 1000$ gam, $1$ tấn $= 1000$ ki-lô-gam. Em hãy giúp họ tự động hóa việc quy đổi.

Nhiệm vụ: Nhập hai số nguyên $T$ và $Y$ trên cùng 1 dòng. In ra tổng khối lượng thóc tính bằng kilogram ($\text{kg}$).

**Đầu vào (Input):**

Một dòng chứa hai số nguyên $T, Y$ ($0 \le T, Y \le 1000$).

**Đầu ra (Output):**

In ra tổng khối lượng theo $\text{kg}$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 5 3 | 530 |

**Giải thích:** $5\text{ tạ} = 500\text{kg}$, $3\text{ yến} = 30\text{kg}$. Tổng $= 500 + 30 = 530\text{kg}$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất đổi khối lượng: 1 tạ bằng 100 ki-lô-gam và 1 yến bằng 10 ki-lô-gam, nên tổng là `t * 100 + y * 10`.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `t, y`, sau đó in `t * 100 + y * 10`; với mẫu `5 3` thì `5 * 100 = 500`, `3 * 10 = 30`, tổng `500 + 30 = 530`.
- Xử lý biên: `T` và `Y` từ 0 đến 1000, tổng nhỏ nhất là 0, lớn nhất là 110000.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 3)

Với số mẫu một dòng `5 3`, chương trình phải in ra `530`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `t, y` | `t = 5`, `y = 3` | 5 tạ 3 yến |
| 2 | Tính `t * 100` | `5 * 100 = 500` | 500 ki-lô-gam |
| 3 | Tính `500 + y * 10` | `500 + 30 = 530` | khớp kết quả mẫu `530` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — nhầm hệ số yến: viết `t * 100 + y * 100` thì với mẫu ra `800` thay vì `530`; cách sửa là yến nhân 10.
- Bẫy 2 — đọc hai dòng riêng: dùng hai lần `input()` thì với mẫu một dòng `5 3` sẽ bị treo chờ; cách sửa là tách một dòng bằng `split()`.
- Bẫy 3 — nhầm thành gam: viết `t * 1000 + y * 100` thì với mẫu ra số rất lớn thay vì `530`; cách sửa là nhân đúng 100 và 10.

#### 4. Lời giải tham khảo

```python
t, y = map(int, input().split())
print(t * 100 + y * 10)
```

### Bài 21 [pya_l03_p32_hang_rao_manh_dat]: Hàng rào quanh mảnh đất

Bối cảnh: Bác Năm có mảnh vườn hình chữ nhật dài $A$ mét, rộng $B$ mét. Bác muốn làm hàng rào lưới thép xung quanh, chừa lại một cổng ra vào rộng $C$ mét.

Nhiệm vụ: Nhập 3 số nguyên $A, B, C$ trên cùng 1 dòng ($C < 2 \times (A + B)$). In ra tổng chiều dài hàng rào lưới thép cần mua.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên $A, B, C$ ($1 \le A, B \le 10^4$, $1 \le C \le 100$).

**Đầu ra (Output):**

In ra chiều dài hàng rào.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 20 15 3 | 67 |

**Giải thích:** Chu vi mảnh vườn $= 2 \times (20 + 15) = 70\text{m}$. Trừ cổng $3\text{m} \implies 70 - 3 = 67\text{m}$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất hàng rào: chu vi `2 * (a + b)` trừ cổng `c`, cả ba số nằm trên cùng một dòng.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `a, b, c`, sau đó in `2 * (a + b) - c`; với mẫu `20 15 3` thì chu vi `2 * (20 + 15) = 70` và rào `70 - 3 = 67`.
- Xử lý biên: `A` và `B` tới 10000, `C` nhỏ hơn chu vi nên chiều dài rào luôn dương.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 20 15 3)

Với số mẫu một dòng `20 15 3`, chương trình phải in ra `67`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a, b, c` | `a = 20`, `b = 15`, `c = 3` | đủ ba số |
| 2 | Tính `2 * (a + b)` | `2 * 35 = 70` | chu vi 70 |
| 3 | Tính `70 - 3` | `67` | khớp kết quả mẫu `67` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên trừ cổng: viết `print(2 * (a + b))` thì với mẫu ra `70` thay vì `67`; cách sửa là trừ thêm `c`.
- Bẫy 2 — thiếu ngoặc: viết `2 * a + b - c` thì với mẫu ra `52` thay vì `67`; cách sửa là `2 * (a + b) - c`.
- Bẫy 3 — đọc ba dòng riêng: dùng ba lần `input()` thì với mẫu một dòng sẽ bị treo chờ; cách sửa là tách một dòng bằng `split()`.

#### 4. Lời giải tham khảo

```python
a, b, c = map(int, input().split())
print(2 * (a + b) - c)
```

### Bài 22 [pya_l03_p18_chay_bo_gap_nhau]: Bài toán chạy bộ hai người ngược chiều

Bối cảnh: Hai bạn An và Bình ở hai đầu một con đường thẳng dài $S$ mét. Cùng lúc, hai bạn chạy lại phía nhau: An chạy với vận tốc $V_1$ mét/giây, Bình chạy với vận tốc $V_2$ mét/giây.

Nhiệm vụ: Nhập 3 số nguyên $S, V_1, V_2$ trên cùng 1 dòng. In ra thời gian (tính bằng giây) kể từ lúc bắt đầu chạy cho đến khi hai bạn gặp nhau, làm tròn 1 chữ số thập phân.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên dương $S, V_1, V_2$ ($1 \le S \le 10^5$, $1 \le V_1, V_2 \le 100$).

**Đầu ra (Output):**

In ra thời gian gặp nhau dạng `f"{t:.1f}"`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 150 2 3 | 30.0 |

**Giải thích:** Vận tốc tiếp cận $= 2 + 3 = 5\text{m/s}$. Thời gian gặp nhau $= 150 / 5 = 30.0$ giây.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất hai người chạy ngược chiều: mỗi giây khoảng cách rút ngắn `v1 + v2`, thời gian gặp nhau là `s / (v1 + v2)`.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `s, v1, v2`, sau đó in `s / (v1 + v2)` với 1 chữ số thập phân; với mẫu `150 2 3` thì `2 + 3 = 5` và `150 / 5 = 30.0`.
- Xử lý biên: `S` tới 100000, mỗi vận tốc tới 100, thời gian luôn dương và in đủ 1 chữ số kể cả số tròn như `30.0`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 150 2 3)

Với số mẫu một dòng `150 2 3`, chương trình phải in ra `30.0`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `s, v1, v2` | `s = 150`, `v1 = 2`, `v2 = 3` | đủ ba số |
| 2 | Tính `v1 + v2` | `2 + 3 = 5` | mỗi giây gần thêm 5 |
| 3 | Tính `150 / 5` | `30.0` | khớp kết quả mẫu `30.0` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — thiếu ngoặc: viết `s / v1 + v2` thì với mẫu ra `78.0` thay vì `30.0`; cách sửa là `s / (v1 + v2)`.
- Bẫy 2 — dùng chia nguyên: viết `s // (v1 + v2)` thì với mẫu ra `30` thiếu `.0`; cách sửa là chia thực và giữ 1 chữ số thập phân.
- Bẫy 3 — đọc ba dòng riêng: dùng ba lần `input()` thì với mẫu một dòng sẽ bị treo chờ; cách sửa là tách một dòng bằng `split()`.

#### 4. Lời giải tham khảo

```python
s, v1, v2 = map(int, input().split())
print(f"{s / (v1 + v2):.1f}")
```

### Bài 23 [pya_l03_p22_dien_tich_tam_giac_vuong]: Diện tích tam giác vuông

Bối cảnh: Kiến trúc sư Hà đang thiết kế một khu vườn trang trí trước sảnh tòa nhà văn phòng. Khu vườn có dạng hình tam giác vuông với hai cạnh góc vuông lần lượt dài $a$ mét và $b$ mét. Để ước tính lượng cỏ nhân tạo cần trải và chi phí thi công, cô cần tính chính xác diện tích khu vườn tam giác vuông này.

Nhiệm vụ: Nhập hai số nguyên dương $A, B$ trên cùng 1 dòng. In ra diện tích lá cờ dưới dạng số thực lấy đúng 1 chữ số thập phân.

**Đầu vào (Input):**

Một dòng chứa hai số nguyên $A, B$ ($1 \le A, B \le 10^4$).

**Đầu ra (Output):**

In ra diện tích định dạng `f"{S:.1f}"`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 5 7 | 17.5 |

**Giải thích:** Diện tích $= (5 \times 7) / 2 = 17.5$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất diện tích tam giác vuông: nửa tích hai cạnh góc vuông `(a * b) / 2`, bài này in đúng 1 chữ số thập phân.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `a, b`, sau đó in `(a * b) / 2` với 1 chữ số thập phân; với mẫu `5 7` thì `5 * 7 = 35` và `35 / 2 = 17.5`.
- Xử lý biên: `A` và `B` tới 10000, diện tích lớn nhất là 50000000.0, số lẻ như `17.5` vẫn hiện đúng 1 chữ số.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 7)

Với số mẫu một dòng `5 7`, chương trình phải in ra `17.5`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a, b` | `a = 5`, `b = 7` | hai cạnh 5 và 7 |
| 2 | Tính `a * b` | `5 * 7 = 35` | tích 35 |
| 3 | Tính `35 / 2` | `17.5` | khớp kết quả mẫu `17.5` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng chia nguyên: viết `(a * b) // 2` thì với mẫu ra `17` thay vì `17.5`; cách sửa là chia thực `/` và giữ 1 chữ số thập phân.
- Bẫy 2 — in thô không làm tròn: viết `print((a * b) / 2)` với cặp số cho kết quả nguyên sẽ thiếu `.0`; cách sửa là luôn ghi định dạng 1 chữ số thập phân.
- Bẫy 3 — đọc hai dòng riêng: dùng hai lần `input()` thì với mẫu một dòng `5 7` sẽ bị treo chờ; cách sửa là tách một dòng bằng `split()`.

#### 4. Lời giải tham khảo

```python
a, b = map(int, input().split())
print(f"{(a * b) / 2:.1f}")
```

### Bài 24 [pya_l03_p29_doi_sang_tong_giay]: Đổi giờ - phút - giây sang tổng số giây

Bối cảnh: Bài toán ngược lại: Cần quy đổi thời gian hiển thị `H giờ M phút S giây` về một số giây duy nhất để máy tính dễ so sánh.

Nhiệm vụ: Nhập 3 số nguyên $H, M, S$ trên cùng 1 dòng ($0 \le H \le 1000$, $0 \le M, S < 60$). In ra tổng số giây.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên $H, M, S$.

**Đầu ra (Output):**

In ra một số nguyên là tổng số giây.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 2 15 30 | 8130 |

**Giải thích:** $2 \times 3600 + 15 \times 60 + 30 = 7200 + 900 + 30 = 8130$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất đổi về giây: 1 giờ bằng 3600 giây và 1 phút bằng 60 giây, nên tổng là `h * 3600 + m * 60 + s`.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `h, m, s`, sau đó in `h * 3600 + m * 60 + s`; với mẫu `2 15 30` thì `2 * 3600 = 7200`, `15 * 60 = 900`, tổng `7200 + 900 + 30 = 8130`.
- Xử lý biên: `H` tới 1000, `M` và `S` dưới 60, tổng lớn nhất là 3635940.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2 15 30)

Với số mẫu một dòng `2 15 30`, chương trình phải in ra `8130`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `h, m, s` | `h = 2`, `m = 15`, `s = 30` | đủ ba số |
| 2 | Tính `h * 3600` | `2 * 3600 = 7200` | 7200 giây |
| 3 | Tính `7200 + 15 * 60 + 30` | `7200 + 900 + 30 = 8130` | khớp kết quả mẫu `8130` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — nhầm hệ số phút: viết `h * 3600 + m * 100 + s` thì với mẫu ra `8730` thay vì `8130`; cách sửa là phút nhân 60.
- Bẫy 2 — nhầm hệ số giờ: viết `h * 60 + m * 60 + s` thì với mẫu ra `1050` thay vì `8130`; cách sửa là giờ nhân 3600.
- Bẫy 3 — đọc ba dòng riêng: dùng ba lần `input()` thì với mẫu một dòng sẽ bị treo chờ; cách sửa là tách một dòng bằng `split()`.

#### 4. Lời giải tham khảo

```python
h, m, s = map(int, input().split())
print(h * 3600 + m * 60 + s)
```

### Bài 25 [pya_l03_p17_son_tuong_phong]: Tính tiền mua sơn quét tường

Bối cảnh: Một bức tường hình chữ nhật có chiều dài $A$ mét và chiều cao $H$ mét. Trên tường có một cửa sổ hình chữ nhật kích thước $X \times Y$ mét không cần quét sơn. Biết mỗi mét vuông tường tốn $G$ đồng tiền sơn.

Nhiệm vụ: Nhập 5 số nguyên $A, H, X, Y, G$ trên cùng 1 dòng. In ra tổng số tiền sơn cần chuẩn bị.

**Đầu vào (Input):**

Một dòng chứa 5 số nguyên dương ($X < A, Y < H$, $1 \le A, H \le 100$, $1 \le G \le 10^5$).

**Đầu ra (Output):**

In ra tổng số tiền sơn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 6 3 2 1 50000 | 800000 |

**Giải thích:** Diện tích tường $= 6 \times 3 = 18\text{m}^2$. Diện tích cửa sổ $= 2 \times 1 = 2\text{m}^2$. Diện tích cần sơn $= 18 - 2 = 16\text{m}^2$. Tổng tiền $= 16 \times 50000 = 800000$ đồng.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất tiền sơn: diện tích tường `a * h` trừ cửa sổ `x * y`, rồi nhân đơn giá `g` một mét vuông.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `a, h, x, y, g`, đặt `s_son = (a * h) - (x * y)` rồi in `s_son * g`; với mẫu `6 3 2 1 50000` thì tường `6 * 3 = 18`, cửa sổ `2 * 1 = 2`, cần sơn `18 - 2 = 16`, tiền `16 * 50000 = 800000`.
- Xử lý biên: đề cho cửa sổ nhỏ hơn tường nên diện tích cần sơn luôn dương; `G` tới 100000.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6 3 2 1 50000)

Với số mẫu một dòng `6 3 2 1 50000`, chương trình phải in ra `800000`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a, h, x, y, g` | `a = 6`, `h = 3`, `x = 2`, `y = 1`, `g = 50000` | đủ năm số |
| 2 | Tính `a * h` | `6 * 3 = 18` | diện tích tường 18 |
| 3 | Tính `x * y` | `2 * 1 = 2` | diện tích cửa sổ 2 |
| 4 | Tính `(18 - 2) * 50000` | `16 * 50000 = 800000` | khớp kết quả mẫu `800000` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — cộng cửa sổ: viết `(a * h + x * y) * g` thì với mẫu ra `1000000` thay vì `800000`; cách sửa là lấy tường trừ cửa sổ.
- Bẫy 2 — quên nhân đơn giá: viết `print((a * h) - (x * y))` thì với mẫu ra `16` thay vì `800000`; cách sửa là nhân thêm `g`.
- Bẫy 3 — đọc năm dòng riêng: dùng năm lần `input()` thì với mẫu một dòng sẽ bị treo chờ; cách sửa là tách một dòng bằng `split()`.

#### 4. Lời giải tham khảo

```python
a, h, x, y, g = map(int, input().split())
s_son = (a * h) - (x * y)
print(s_son * g)
```

### Bài 26 [pya_l03_p05_dien_tich_hinh_thang]: Diện tích hình thang

Bối cảnh: Thửa ruộng nhà ông Ba ở Cần Thơ có hình dạng hình thang cân, với đáy lớn dài $a$ mét, đáy nhỏ dài $b$ mét và chiều cao $h$ mét. Cuối vụ mùa, hợp tác xã cần tính diện tích thửa ruộng để quy đổi sản lượng lúa thu hoạch trên mỗi mét vuông và lập báo cáo năng suất nông nghiệp.

Nhiệm vụ: Nhập 3 số nguyên dương $A, B, H$ trên cùng một dòng. In ra diện tích thửa ruộng dưới dạng số thực lấy đúng 1 chữ số thập phân.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên $A, B, H$ ($1 \le B \le A \le 10^4$, $1 \le H \le 10^4$).

**Đầu ra (Output):**

In ra diện tích định dạng `f"{S:.1f}"`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 12 8 5 | 50.0 |

**Giải thích:** Diện tích $= ((12 + 8) \times 5) / 2 = 50.0$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất diện tích hình thang: trung bình hai đáy nhân chiều cao, tức `((a + b) * h) / 2`, in đúng 1 chữ số thập phân.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `a, b, h`, sau đó in `((a + b) * h) / 2` với 1 chữ số thập phân; với mẫu `12 8 5` thì `12 + 8 = 20`, `20 * 5 = 100`, `100 / 2 = 50.0`.
- Xử lý biên: đề cho đáy nhỏ `B` không vượt quá đáy lớn `A` tới 10000, chiều cao tới 10000.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12 8 5)

Với số mẫu một dòng `12 8 5`, chương trình phải in ra `50.0`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a, b, h` | `a = 12`, `b = 8`, `h = 5` | đủ ba số |
| 2 | Tính `a + b` | `12 + 8 = 20` | tổng hai đáy 20 |
| 3 | Tính `(20 * 5) / 2` | `100 / 2 = 50.0` | khớp kết quả mẫu `50.0` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — thiếu ngoặc: viết `a + b * h / 2` thì với mẫu ra `32.0` thay vì `50.0`; cách sửa là `((a + b) * h) / 2`.
- Bẫy 2 — dùng chia nguyên: viết `((a + b) * h) // 2` thì với mẫu ra `50` thiếu `.0`; cách sửa là chia thực và giữ 1 chữ số thập phân.
- Bẫy 3 — đọc ba dòng riêng: dùng ba lần `input()` thì với mẫu một dòng sẽ bị treo chờ; cách sửa là tách một dòng bằng `split()`.

#### 4. Lời giải tham khảo

```python
a, b, h = map(int, input().split())
print(f"{((a + b) * h) / 2:.1f}")
```

### Bài 27 [pya_l03_p26_van_toc_trung_binh]: Tính vận tốc trung bình

Bối cảnh: Xe buýt tuyến 01 khởi hành từ bến xe Miền Đông đi bến xe Miền Tây, quãng đường dài $S$ ki-lô-mét và xe chạy hết $T$ giờ (kể cả thời gian dừng đón trả khách). Công ty vận tải cần tính vận tốc trung bình thực tế của chuyến xe để đánh giá hiệu suất và điều chỉnh lịch trình cho phù hợp.

Nhiệm vụ: Nhập hai số nguyên $S$ và $T$ ($1 \le T \le 100$, $1 \le S \le 10^5$). In ra vận tốc trung bình của ô tô làm tròn 2 chữ số thập phân.

**Đầu vào (Input):**

Một dòng chứa $S$ và $T$.

**Đầu ra (Output):**

In ra vận tốc dạng `f"{v:.2f}"` (đơn vị $\text{km/h}$).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 100 3 | 33.33 |

**Giải thích:** $100 / 3 \approx 33.3333... \implies 33.33$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất vận tốc trung bình: quãng đường `s` chia thời gian `t`, in làm tròn 2 chữ số thập phân.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `s, t`, sau đó in `s / t` với 2 chữ số thập phân; với mẫu `100 3` thì `100 / 3 = 33.333...` làm tròn thành `33.33`.
- Xử lý biên: `T` từ 1 đến 100, `S` tới 100000, luôn in đủ 2 chữ số kể cả số tròn.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 100 3)

Với số mẫu một dòng `100 3`, chương trình phải in ra `33.33`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `s, t` | `s = 100`, `t = 3` | đủ hai số |
| 2 | Tính `s / t` | `100 / 3 = 33.333...` | số dài 33.333 |
| 3 | Làm tròn 2 chữ số | `33.33` | khớp kết quả mẫu `33.33` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng chia nguyên: viết `print(s // t)` thì với mẫu ra `33` thay vì `33.33`; cách sửa là chia thực `s / t` rồi làm tròn 2 chữ số.
- Bẫy 2 — in thô không làm tròn: viết `print(s / t)` thì với mẫu ra `33.333333333333336` thay vì `33.33`; cách sửa là ghi định dạng 2 chữ số thập phân.
- Bẫy 3 — đọc hai dòng riêng: dùng hai lần `input()` thì với mẫu một dòng `100 3` sẽ bị treo chờ; cách sửa là tách một dòng bằng `split()`.

#### 4. Lời giải tham khảo

```python
s, t = map(int, input().split())
print(f"{s / t:.2f}")
```

### Bài 28 [pya_l03_p24_doi_giay_sang_gio_phut_giay]: Đổi giây sang giờ phút giây

Bối cảnh: Trong hệ thống theo dõi quỹ đạo trạm không gian, đồng hồ đo ghi nhận thời gian hoàn thành một vòng quỹ đạo là tổng cộng $S$ giây. Hệ thống cần hiển thị giá trị này dưới dạng tường minh: gồm bao nhiêu giờ ($H$), bao nhiêu phút ($M$) và bao nhiêu giây ($S$).

Nhiệm vụ: Nhập vào tổng số giây $S$. Hãy phân rã thành $H$ giờ, $M$ phút, $S$ giây.

**Đầu vào (Input):**

Một số nguyên $S$ ($0 \le S \le 10^8$).

**Đầu ra (Output):**

In ra ba số nguyên $H, M, S$ cách nhau một khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3665 | 1 1 5 |

**Giải thích:** 3665 giây = 1 giờ (3600s) + 1 phút (60s) + 5 giây.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất tách giây: số giờ `tong_giay // 3600`, phần dư `tong_giay % 3600` tách tiếp thành phút `// 60` và giây lẻ `% 60`.
- Quy trình trong lời giải: đọc `tong_giay`, đặt `gio`, `giay_du`, `phut`, `giay` rồi in ba số; với mẫu `3665` thì `3665 // 3600 = 1`, dư `65`, `65 // 60 = 1` phút, lẻ `65 % 60 = 5` giây nên ra `1 1 5`.
- Xử lý biên: `S` từ 0 đến 100000000, số 0 cho ra `0 0 0`, số tròn 3600 cho ra `1 0 0`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3665)

Với số mẫu `3665`, chương trình phải in ra `1 1 5`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `tong_giay` | `tong_giay = 3665` | 3665 giây |
| 2 | Tính `gio`, `giay_du` | `gio = 1`, `giay_du = 65` | 1 giờ dư 65 |
| 3 | Tính `phut`, `giay` | `phut = 1`, `giay = 5` | xuất `1 1 5` khớp mẫu |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — chia phút trực tiếp: viết `phut = tong_giay // 60` thì với mẫu ra `61` thay vì `1`; cách sửa là lấy phần dư sau khi trừ giờ rồi mới chia 60.
- Bẫy 2 — in kèm dấu hai chấm: viết `print(gio, phut, giay, sep=":")` thì với mẫu ra `1:1:5` thay vì `1 1 5`; cách sửa là in ba số cách nhau dấu cách.
- Bẫy 3 — quên ép kiểu: viết `tong_giay = input()` thì phép `//` bị lỗi vì chuỗi; cách sửa là `int(input())`.

#### 4. Lời giải tham khảo

```python
tong_giay = int(input())
gio = tong_giay // 3600
giay_du = tong_giay % 3600
phut = giay_du // 60
giay = giay_du % 60
print(gio, phut, giay)
```

### Bài 29 [pya_l03_p12_khoang_cach_thoi_gian]: Khoảng thời gian giữa hai thời điểm trong ngày

Bối cảnh: Bạn Minh bắt đầu học bài lúc $H_1$ giờ $M_1$ phút và kết thúc lúc $H_2$ giờ $M_2$ phút (trong cùng một ngày).

Nhiệm vụ: Nhập 4 số nguyên $H_1, M_1, H_2, M_2$ trên 1 dòng. In ra khoảng thời gian học tính theo đơn vị phút.

**Đầu vào (Input):**

Một dòng chứa 4 số nguyên ($0 \le H_1 \le H_2 \le 23$, $0 \le M_1, M_2 < 60$, thời điểm 2 không sớm hơn thời điểm 1).

**Đầu ra (Output):**

In ra số phút chênh lệch.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 8 30 10 15 | 105 |

**Giải thích:** Từ 8h30 đến 10h15 là 1 giờ 45 phút $= 60 + 45 = 105$ phút.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất khoảng cách thời gian: đổi mỗi thời điểm về phút rồi trừ nhau, tức `(h2 * 60 + m2) - (h1 * 60 + m1)`.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `h1, m1, h2, m2`, đặt `t1 = h1 * 60 + m1` và `t2 = h2 * 60 + m2` rồi in `t2 - t1`; với mẫu `8 30 10 15` thì `t1 = 8 * 60 + 30 = 510`, `t2 = 10 * 60 + 15 = 615`, hiệu `615 - 510 = 105`.
- Xử lý biên: đề cho thời điểm sau không sớm hơn thời điểm trước trong cùng một ngày, hiệu nhỏ nhất là 0.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 8 30 10 15)

Với số mẫu một dòng `8 30 10 15`, chương trình phải in ra `105`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `h1, m1, h2, m2` | `8, 30, 10, 15` | đủ bốn số |
| 2 | Tính `t1 = 8 * 60 + 30` | `t1 = 510` | bắt đầu phút 510 |
| 3 | Tính `t2 = 10 * 60 + 15` | `t2 = 615` | kết thúc phút 615 |
| 4 | Tính `615 - 510` | `105` | khớp kết quả mẫu `105` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — chỉ trừ giờ: viết `print(h2 - h1)` thì với mẫu `8 30 10 15` ra `2` thay vì `105`; cách sửa là đổi cả hai thời điểm về phút `t1 = 510`, `t2 = 615` rồi trừ `t2 - t1`.
- Bẫy 2 — trừ ngược: viết `print(t1 - t2)` thì với mẫu ra `-105` thay vì `105`; cách sửa là lấy thời điểm sau trừ thời điểm trước.
- Bẫy 3 — đọc bốn dòng riêng: dùng bốn lần `input()` thì với mẫu một dòng sẽ bị treo chờ; cách sửa là tách một dòng bằng `split()`.

#### 4. Lời giải tham khảo

```python
h1, m1, h2, m2 = map(int, input().split())
t1 = h1 * 60 + m1
t2 = h2 * 60 + m2
print(t2 - t1)
```

### Bài 30 [pya_l03_p15_lat_gach_nen_nha]: Lát nền phòng học

Bối cảnh: Phòng học hình chữ nhật có chiều dài $L$ mét và chiều rộng $W$ mét. Người ta dùng các viên gạch hoa hình vuông cạnh $D$ centimet để lát nền.

Nhiệm vụ: Nhập 3 số nguyên dương $L, W, D$ trên cùng 1 dòng ($L, W$ tính bằng mét, $D$ tính bằng centimet). Giả sử phòng học vừa khít các viên gạch, hãy in ra tổng số viên gạch cần dùng.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên $L, W, D$ ($1 \le L, W \le 100$, $10 \le D \le 100$).

**Đầu ra (Output):**

In ra số viên gạch cần dùng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 6 4 50 | 96 |

**Giải thích:** Đổi $L = 600\text{cm}, W = 400\text{cm}$. Diện tích sàn $= 600 \times 400 = 240000\text{cm}^2$. Diện tích 1 viên gạch $= 50 \times 50 = 2500\text{cm}^2$. Số gạch $= 240000 // 2500 = 96$ viên.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất lát nền khác đơn vị: đổi dài rộng từ mét sang xen-ti-mét (`l * 100`, `w * 100`), diện tích sàn chia diện tích viên `d * d`.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `l, w, d`, đặt `s_san = (l * 100) * (w * 100)` và `s_gach = d * d` rồi in `s_san // s_gach`; với mẫu `6 4 50` thì sàn `600 * 400 = 240000`, viên `50 * 50 = 2500`, số gạch `240000 // 2500 = 96`.
- Xử lý biên: đề cho phòng vừa khít gạch nên chia hết; `L` và `W` tới 100, `D` từ 10 đến 100.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6 4 50)

Với số mẫu một dòng `6 4 50`, chương trình phải in ra `96`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `l, w, d` | `l = 6`, `w = 4`, `d = 50` | đủ ba số |
| 2 | Tính `s_san` | `600 * 400 = 240000` | diện tích sàn 240000 |
| 3 | Tính `s_gach` | `50 * 50 = 2500` | diện tích viên 2500 |
| 4 | Tính `240000 // 2500` | `96` | khớp kết quả mẫu `96` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên đổi mét sang xen-ti-mét: viết `(l * w) // (d * d)` thì với mẫu ra `0` thay vì `96`; cách sửa là nhân `l * 100` và `w * 100` trước.
- Bẫy 2 — chỉ đổi một chiều: viết `(l * 100 * w) // (d * d)` thì với mẫu ra `0` thay vì `96`; cách sửa là đổi cả hai chiều dài và rộng.
- Bẫy 3 — dùng chia thực: viết `print(s_san / s_gach)` thì với mẫu in ra `96.0` thay vì `96`; cách sửa là dùng chia nguyên `//`.

#### 4. Lời giải tham khảo

```python
l, w, d = map(int, input().split())
s_san = (l * 100) * (w * 100)
s_gach = d * d
print(s_san // s_gach)
```

### Bài 31 [pya_l03_p28_doi_giay_sang_gio_phut_giay]: Đổi tổng số giây sang giờ, phút, giây

Bối cảnh: Đồng hồ bấm giờ trong cuộc thi chạy marathon ghi nhận tổng thời gian là $T$ giây.

Nhiệm vụ: Nhập số nguyên dương $T$ ($1 \le T \le 10^9$). In ra theo định dạng `H:M:S`.

**Đầu vào (Input):**

Một dòng chứa số nguyên $T$.

**Đầu ra (Output):**

In ra chuỗi `H:M:S` (với $H$ là giờ, $M$ là phút, $S$ là giây).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3665 | 1:1:5 |

**Giải thích:** 1 giờ 1 phút 5 giây.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất tách giây giống bài đổi giây nhưng in theo dạng `H:M:S` với dấu hai chấm.
- Quy trình trong lời giải: đọc `t`, đặt `gio = t // 3600`, `phut = (t % 3600) // 60`, `giay = t % 60` rồi in ghép dấu hai chấm; với mẫu `3665` thì `gio = 1`, `phut = 1`, `giay = 5` nên ra `1:1:5`.
- Xử lý biên: `T` từ 1 đến 1000000000, chú ý giây lẻ lấy `% 60` của tổng, không phải của phần dư giờ? với mẫu cả hai cách đều ra 5.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3665)

Với số mẫu `3665`, chương trình phải in ra `1:1:5`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `t` | `t = 3665` | 3665 giây |
| 2 | Tính `gio` | `3665 // 3600 = 1` | 1 giờ |
| 3 | Tính `phut`, `giay` | `phut = 1`, `giay = 5` | xuất `1:1:5` khớp mẫu |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — in cách nhau dấu cách: viết `print(gio, phut, giay)` thì với mẫu ra `1 1 5` thay vì `1:1:5`; cách sửa là ghép chuỗi với dấu hai chấm.
- Bẫy 2 — chia phút trực tiếp: viết `phut = t // 60` thì với mẫu ra `61` thay vì `1`; cách sửa là `(t % 3600) // 60`.
- Bẫy 3 — quên ép kiểu: viết `t = input()` thì phép `//` bị lỗi; cách sửa là `int(input())`.

#### 4. Lời giải tham khảo

```python
t = int(input())
gio = t // 3600
phut = (t % 3600) // 60
giay = t % 60
print(f"{gio}:{phut}:{giay}")
```

### Bài 32 [pya_l03_p13_diem_trung_binh]: Điểm trung bình môn học

Bối cảnh: Cuối học kỳ, hệ thống quản lý điểm số của trường tự động tính điểm trung bình từ các bài kiểm tra. Một học sinh có điểm ba môn chính lần lượt là $a$, $b$ và $c$. Điểm trung bình được tính bằng công thức $\text{TB} = \frac{a + b + c}{3}$. Em hãy lập trình tính điểm trung bình và in kết quả với số thập phân chính xác.

Nhiệm vụ: Nhập 3 số thực là điểm của 3 môn trên cùng 1 dòng. In ra điểm trung bình cộng làm tròn đúng 2 chữ số thập phân.

**Đầu vào (Input):**

Một dòng chứa 3 số thực ($0 \le d_1, d_2, d_3 \le 10$).

**Đầu ra (Output):**

In ra điểm trung bình dạng `f"{dtb:.2f}"`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 8.5 9.0 7.5 | 8.33 |

**Giải thích:** $(8.5 + 9.0 + 7.5) / 3 = 25.0 / 3 \approx 8.3333... \implies 8.33$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất điểm trung bình: cộng ba điểm `d1 + d2 + d3` rồi chia 3, in làm tròn 2 chữ số thập phân.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `d1, d2, d3` kiểu số thực, sau đó in `(d1 + d2 + d3) / 3` với 2 chữ số thập phân; với mẫu `8.5 9.0 7.5` thì tổng `8.5 + 9.0 + 7.5 = 25.0` và `25.0 / 3 = 8.333...` làm tròn thành `8.33`.
- Xử lý biên: mỗi điểm từ 0 đến 10, điểm 10 10 10 cho ra `10.00`, điểm 0 0 0 cho ra `0.00`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 8.5 9.0 7.5)

Với số mẫu một dòng `8.5 9.0 7.5`, chương trình phải in ra `8.33`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `d1, d2, d3` | `8.5, 9.0, 7.5` | đủ ba điểm |
| 2 | Tính tổng | `8.5 + 9.0 + 7.5 = 25.0` | tổng 25.0 |
| 3 | Tính `25.0 / 3` | `8.333...` làm tròn `8.33` | khớp kết quả mẫu `8.33` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đọc số nguyên: viết `map(int, ...)` thì với mẫu `8.5` bị lỗi đổi chữ; cách sửa là đọc số thực `map(float, ...)`.
- Bẫy 2 — dùng chia nguyên: viết `(d1 + d2 + d3) // 3` thì với mẫu ra `8.0` thay vì `8.33`; cách sửa là chia thực `/` rồi làm tròn 2 chữ số.
- Bẫy 3 — in thô không làm tròn: viết `print((d1 + d2 + d3) / 3)` thì với mẫu ra `8.333333333333334` thay vì `8.33`; cách sửa là ghi định dạng 2 chữ số thập phân.

#### 4. Lời giải tham khảo

```python
d1, d2, d3 = map(float, input().split())
print(f"{(d1 + d2 + d3) / 3:.2f}")
```

### Bài 33 [pya_l03_p16_loi_di_quanh_ho]: Diện tích lối đi quanh hồ nước

Bối cảnh: Trong công viên có một hồ nước hình chữ nhật kích thước dài $A$ mét, rộng $B$ mét. Xung quanh hồ, người ta làm một lối đi dạo có bề rộng đồng đều là $D$ mét.

Nhiệm vụ: Nhập 3 số nguyên $A, B, D$ trên cùng 1 dòng. Hãy tính diện tích của lối đi dạo đó.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên $A, B, D$ ($1 \le A, B \le 10^4$, $1 \le D \le 100$).

**Đầu ra (Output):**

In ra diện tích lối đi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 8 2 | 88 |

**Giải thích:** Kích thước cả hồ và lối đi là $(10 + 2 \times 2) = 14\text{m}$ và $(8 + 2 \times 2) = 12\text{m}$. Diện tích toàn phần $= 14 \times 12 = 168\text{m}^2$. Diện tích hồ $= 10 \times 8 = 80\text{m}^2$. Diện tích lối đi $= 168 - 80 = 88\text{m}^2$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất lối đi quanh hồ: diện tích ngoài `(a + 2 * d) * (b + 2 * d)` trừ diện tích hồ `a * b`.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `a, b, d`, đặt `s_ngoai` và `s_ho` rồi in hiệu; với mẫu `10 8 2` thì ngoài `(10 + 4) * (8 + 4) = 14 * 12 = 168`, hồ `10 * 8 = 80`, lối đi `168 - 80 = 88`.
- Xử lý biên: `A` và `B` tới 10000, `D` tới 100, diện tích lối đi luôn dương.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10 8 2)

Với số mẫu một dòng `10 8 2`, chương trình phải in ra `88`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a, b, d` | `a = 10`, `b = 8`, `d = 2` | đủ ba số |
| 2 | Tính `s_ngoai` | `14 * 12 = 168` | toàn phần 168 |
| 3 | Tính `s_ho` | `10 * 8 = 80` | hồ 80 |
| 4 | Tính `168 - 80` | `88` | khớp kết quả mẫu `88` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — chỉ cộng một lần bề rộng: viết `(a + d) * (b + d) - a * b` thì với mẫu ra `34` thay vì `88`; cách sửa là cộng `2 * d` mỗi chiều vì lối đi bao cả hai bên.
- Bẫy 2 — quên trừ hồ: viết `print((a + 2 * d) * (b + 2 * d))` thì với mẫu ra `168` thay vì `88`; cách sửa là trừ thêm `a * b`.
- Bẫy 3 — đọc ba dòng riêng: dùng ba lần `input()` thì với mẫu một dòng sẽ bị treo chờ; cách sửa là tách một dòng bằng `split()`.

#### 4. Lời giải tham khảo

```python
a, b, d = map(int, input().split())
s_ngoai = (a + 2 * d) * (b + 2 * d)
s_ho = a * b
print(s_ngoai - s_ho)
```

# CHƯƠNG 02: CẤU TRÚC RẼ NHÁNH & CẤU TRÚC VÒNG LẶP

### Bài 01 [pya_l04_p04_so_lon_nhat_trong_hai_so]: Số lớn nhất trong hai số

Bối cảnh: Bộ vi xử lý cần thực hiện thao tác so sánh logic giữa hai thanh ghi dữ liệu $A$ và $B$ để giữ lại giá trị cực đại phục vụ tính toán tiếp theo.

Nhiệm vụ: Cho hai số nguyên $A$ và $B$. Hãy tìm và in ra giá trị lớn nhất trong hai số đó.

**Đầu vào (Input):**

Hai số nguyên $a, b$ ($-10^9 \le a, b \le 10^9$).

**Đầu ra (Output):**

Một số nguyên là giá trị lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| -15 <br> 8 | 8 |

**Giải thích:** Hai số đầu vào là $25$ và $42$. Số lớn hơn là $42$. Kết quả in ra: `42`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là phép so sánh hai số: với hai số `a = -15` và `b = 8`, đáp án chính là số đứng sau trên trục số.
- Cách làm của lời giải mẫu: đọc `a` ở dòng một, đọc `b` ở dòng hai, rồi gọi `max(a, b)` để lấy số lớn hơn và in ra.
- Xử lý biên: ràng buộc cho phép `a, b` xuống tới `-10^9` và lên tới `10^9`. Với mẫu `-15` và `8`, vì `-15 < 8` nên kết quả là `8`. Nếu cả hai số đều âm, ví dụ `-20` và `-5`, đáp án vẫn là số ít âm hơn (`-5`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: -15 rồi 8)

Sample 1 với input mẫu: `-15` rồi `8`.
| Bước | Việc làm | Giá trị của `a`, `b` | In ra |
|---|---|---|---|
| 1 | Đọc dòng một | `a = -15` | — |
| 2 | Đọc dòng hai | `b = 8` | — |
| 3 | So sánh: `-15` có lớn hơn `8` không? Không | giữ `a = -15, b = 8` | — |
| 4 | Gọi `max(-15, 8)` được `8` rồi in ra | — | `8` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — chỉ đọc một số: bạn nhỏ viết `a = int(input())` rồi `print(a)`. Với mẫu `-15` và `8`, chương trình chỉ in `-15`, thiếu hẳn số thứ hai. Cách sửa: đọc thêm dòng `b = int(input())` rồi mới so sánh.
- Bẫy 2 — in nhầm số bé: bạn nhỏ viết `print(min(a, b))`. Với mẫu này sẽ in `-15` thay vì `8`. Cách sửa: đổi thành `print(max(a, b))`.
- Bẫy 3 — đọc hai số trên cùng một dòng mà không tách: nếu đề cho `-15 8` trên một dòng mà chỉ gọi `input()` một lần thì thiếu số. Cách sửa: đọc hai dòng như lời giải mẫu, hoặc tách chuỗi khi cần.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
print(max(a, b))
```

### Bài 02 [pya_l04_p09_tri_tuyet_doi_cua_mot_so]: Trị tuyệt đối của một số

Bối cảnh: Trong tính toán tọa độ và độ lệch kỹ thuật số, giá trị tuyệt đối $|x|$ thể hiện khoảng cách từ điểm đo đến mốc tham chiếu số 0.

Nhiệm vụ: Cho số nguyên $x$. Hãy tính và in ra giá trị tuyệt đối $|x|$ của số đó.

**Đầu vào (Input):**

Một số nguyên $N$ ($-10^9 \le N \le 10^9$).

**Đầu ra (Output):**

Giá trị tuyệt đối của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| -25 | 25 |

**Giải thích:** Số đầu vào là $-15$. Giá trị tuyệt đối của $-15$ là $|-15| = 15$. Kết quả in ra: `15`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 | 10 |

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là khoảng cách từ điểm `n` tới mốc số 0: số âm thì lật dấu thành dương, số dương và số 0 giữ nguyên.
- Cách làm của lời giải mẫu: đọc `n`, gọi `abs(n)` rồi in ra. Với mẫu `n = -25`, `abs(-25)` cho `25`.
- Xử lý biên: ràng buộc cho phép `N` từ `-10^9` tới `10^9`. Hai mốc cần nhớ là `N = 0` cho kết quả `0`, và `N = -10^9` cho kết quả `10^9`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: -25)

Sample 1 với input mẫu: `-25`.
| Bước | Việc làm | Giá trị của `n` | In ra |
|---|---|---|---|
| 1 | Đọc input, `n = int(input().strip())` | `n = -25` | — |
| 2 | Gọi `abs(-25)` | `25` | — |
| 3 | In kết quả | — | `25` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên số âm: bạn nhỏ viết `print(n)` thẳng. Với mẫu `-25` sẽ in `-25` thay vì `25`. Cách sửa: bọc thêm `abs`, thành `print(abs(n))`.
- Bẫy 2 — tự trừ mà sai dấu: bạn nhỏ viết `print(0 - n)` cho mọi trường hợp. Với `n = 10` (số dương) sẽ in `-10`, sai. Cách sửa: dùng `abs(n)` để cả hai phía đều đúng.
- Bẫy 3 — bình phương rồi căn: bạn nhỏ viết `print(n * n)` để cho chắc dương. Với mẫu `-25` sẽ in `625` thay vì `25`. Cách sửa: dùng `abs(n)` thay cho nhân đôi.

#### 4. Lời giải tham khảo

```python
n = int(input().strip())
print(abs(n))
```

### Bài 03 [pya_l04_p02_ve_vao_cong_vien]: Vé vào công viên

Bối cảnh: Tại trạm kiểm soát tự động của công viên nước, hệ thống cảm biến quang học đo chiều cao $h$ (cm) của khách hàng để phân loại vé hợp lệ.

Nhiệm vụ: Nếu chiều cao $h \ge 130\text{ cm}$, in ra `VE NGUOI LON`. Nếu $h < 130\text{ cm}$, in ra `VE TRE EM`.

**Đầu vào (Input):**

Một số nguyên $h$ ($1 \le h \le 200$).

**Đầu ra (Output):**

`VE NGUOI LON` hoặc `VE TRE EM`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 135 | VE NGUOI LON |

**Giải thích:** Chiều cao đo được là $135\text{ cm}$. Do $135 \ge 130$, khách hàng cần áp dụng mức vé người lớn. Kết quả in ra: `VE NGUOI LON`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 120 | VE TRE EM |

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là một mốc cắt duy nhất `130`: chiều cao `h` từ `130` trở lên là vé người lớn, dưới `130` là vé trẻ em.
- Cách làm của lời giải mẫu: đọc `h`, kiểm tra `if h >= 130` thì in `VE NGUOI LON`, ngược lại in `VE TRE EM`. Với mẫu `h = 135`, vì `135 >= 130` nên in vé người lớn.
- Xử lý biên: ràng buộc `1 <= h <= 200`. Hai mốc cần thử là `h = 130` (vừa chạm mốc, vẫn là `VE NGUOI LON`) và `h = 129` (thấp hơn một đơn vị, là `VE TRE EM`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 135)

Sample 1 với input mẫu: `135`.
| Bước | Việc làm | Giá trị của `h` | In ra |
|---|---|---|---|
| 1 | Đọc input | `h = 135` | — |
| 2 | Kiểm tra `135 >= 130`? Đúng | rẽ nhánh `if` | — |
| 3 | In theo nhánh đúng | — | `VE NGUOI LON` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — viết sai mốc so sánh: bạn nhỏ viết `if h > 130`. Với `h = 130` sẽ rơi sang vé trẻ em, sai. Cách sửa: dùng `>=` như lời giải mẫu.
- Bẫy 2 — in sai chữ: bạn nhỏ in `VE NGUOI LON` thiếu chữ hoặc thêm dấu, ví dụ `VE NGUOI LON ` có khoảng trắng thừa hay `VÉ NGƯỜI LỚN` có dấu. Với mẫu `135`, chương trình kiểm tra sẽ báo kết quả sai. Cách sửa: chép đúng từng chữ in hoa không dấu `VE NGUOI LON`.
- Bẫy 3 — đảo hai nhánh: bạn nhỏ cho nhánh `if` in `VE TRE EM`. Với mẫu `135` sẽ in vé trẻ em, sai. Cách sửa: nhánh `h >= 130` in `VE NGUOI LON`, nhánh còn lại in `VE TRE EM`.

#### 4. Lời giải tham khảo

```python
h = int(input())
if h >= 130:
    print("VE NGUOI LON")
else:
    print("VE TRE EM")
```

### Bài 04 [pya_l04_p01_kiem_tra_so_chan_le]: Kiểm tra số chẵn lẻ

Bối cảnh: Trong thuật toán phân nhánh xử lý luồng dữ liệu mạng, các gói tin mang số định danh chẵn và lẻ được chuyển tiếp qua hai kênh truyền tải khác nhau.

Nhiệm vụ: Cho số tự nhiên $N$. Hãy kiểm tra nếu $N$ là số chẵn in ra `CHAN`, ngược lại in ra `LE`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($0 \le N \le 10^9$).

**Đầu ra (Output):**

Chuỗi `CHAN` hoặc `LE`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 18 | CHAN |

**Giải thích:** Số đầu vào là $18$. Vì $18$ chia hết cho $2$ ($18 \% 2 = 0$), nên đây là số chẵn. Kết quả in ra: `CHAN`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 7 | LE |

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là phép chia lấy dư cho `2`: số `n` mà `n % 2 == 0` là số chẵn, còn dư `1` là số lẻ.
- Cách làm của lời giải mẫu: đọc `n`, kiểm tra `if n % 2 == 0` thì in `CHAN`, ngược lại in `LE`. Với mẫu `n = 18`, vì `18 % 2 = 0` nên in `CHAN`.
- Xử lý biên: ràng buộc `0 <= N <= 10^9`. Hai mốc cần nhớ là `N = 0` (vì `0 % 2 = 0` nên là `CHAN`) và `N = 10^9` vẫn tính bình thường.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 18)

Sample 1 với input mẫu: `18`.
| Bước | Việc làm | Giá trị của `n` | In ra |
|---|---|---|---|
| 1 | Đọc input | `n = 18` | — |
| 2 | Tính `18 % 2` được `0`, điều kiện đúng | rẽ nhánh `if` | — |
| 3 | In theo nhánh chẵn | — | `CHAN` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — chia hết cho `3` thay vì `2`: bạn nhỏ viết `if n % 3 == 0`. Với mẫu `18` thì trùng cờ vẫn đúng, nhưng với `n = 9` sẽ in `CHAN` sai. Cách sửa: luôn chia dư cho `2`.
- Bẫy 2 — in chữ thường: bạn nhỏ in `Chan` hoặc `chan`. Với mẫu `18`, chương trình kiểm tra sẽ báo kết quả sai vì thiếu chữ in hoa. Cách sửa: in đúng `CHAN` và `LE` viết hoa toàn bộ.
- Bẫy 3 — quên số 0: bạn nhỏ nghĩ `0` là số lẻ. Thực ra `0 % 2 = 0` nên `0` là `CHAN`. Cách sửa: tin vào phép chia dư, không đoán bằng cảm giác.

#### 4. Lời giải tham khảo

```python
n = int(input())
if n % 2 == 0:
    print("CHAN")
else:
    print("LE")
```

### Bài 05 [pya_l04_p06_dien_phep_tinh_lon_nhat]: Điền phép tính lớn nhất

Bối cảnh: Trong giờ toán vui, cô giáo viết lên bảng một số tự nhiên $A$ và biểu thức bí ẩn sau: $A \text{ ? } A = B$. Cô đố cả lớp hãy chọn một dấu trong ba dấu cộng, trừ, nhân để lấp vào chỗ dấu hỏi chấm. Thí sinh nào tìm được số $B$ to nhất sẽ được thưởng một tràng pháo tay. Hãy giúp cả lớp tìm ra số $B$ lớn nhất có thể.

Nhiệm vụ: Hãy dùng một trong các phép tính $+$, $-$, $\times$ điền vào dấu $?$ để giá trị $B$ đạt được là **lớn nhất**. In ra số $B$ lớn nhất tìm được.

**Đầu vào (Input):**

Một số tự nhiên $A$ ($0 \le A \le 100$).

**Đầu ra (Output):**

Một số nguyên duy nhất là số $B$ lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3 | 9 |

**Giải thích:** $3 + 3 = 6$, $3 - 3 = 0$, $3 \times 3 = 9$. Số lớn nhất là 9.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 1 | 2 |

**Giải thích:** $1 + 1 = 2$, $1 - 1 = 0$, $1 \times 1 = 1$. Số lớn nhất là 2!

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là thử cả ba cách rồi chọn số to nhất: với số `a`, ba ứng viên là `a + a`, `a - a` (luôn bằng `0`) và `a * a`.
- Cách làm của lời giải mẫu: tính `cong = a + a` và `nhan = a * a`, nếu `nhan >= cong` thì in `nhan`, ngược lại in `cong`. Với mẫu `a = 3`: `cong = 6`, `nhan = 9`, vì `9 >= 6` nên in `9`.
- Xử lý biên: ràng buộc `0 <= A <= 100`. Hai mốc cần nhớ là `A = 0` (`cong = 0`, `nhan = 0`, đáp án `0`) và `A = 1` (`cong = 2`, `nhan = 1`, đáp án `2`, phép cộng thắng).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3)

Sample 1 với input mẫu: `3`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc input | `a = 3` | — |
| 2 | Tính `cong = 3 + 3` | `cong = 6` | — |
| 3 | Tính `nhan = 3 * 3` | `nhan = 9` | — |
| 4 | So sánh `9 >= 6`? Đúng, chọn `nhan` | — | `9` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — luôn in phép cộng: bạn nhỏ viết `print(a + a)`. Với mẫu `3` sẽ in `6` thay vì `9`. Cách sửa: tính thêm `a * a` rồi so sánh như lời giải mẫu.
- Bẫy 2 — luôn in phép nhân: bạn nhỏ viết `print(a * a)`. Với `a = 1` sẽ in `1` thay vì `2`. Cách sửa: giữ phép so sánh `if nhan >= cong`.
- Bẫy 3 — quên mất phép trừ cho kết quả `0`: có bạn lo phép trừ thắng khi `a = 0`. Thực ra với `a = 0` thì cả ba phép đều `0`, in `0` vẫn đúng. Cách sửa: chỉ cần so sánh cộng và nhân như lời giải mẫu là đủ.

#### 4. Lời giải tham khảo

```python
a = int(input())
cong = a + a
nhan = a * a
if nhan >= cong:
    print(nhan)
else:
    print(cong)
```

### Bài 06 [pya_l04_p07_giam_gia_sieu_thi]: Giảm giá siêu thị

Bối cảnh: Cuối tuần, mẹ dẫn Bi đi siêu thị mua đồ thật vui. Siêu thị đang có chương trình khuyến mãi: khách hàng mua đơn hàng có tổng giá trị từ $500$ nghìn đồng trở lên sẽ được giảm giá ngay $50$ nghìn đồng, còn các đơn hàng dưới $500$ nghìn đồng thì giữ nguyên giá. Bi xung phong ra quầy tính tiền giúp mẹ. Hãy tính xem phải trả bao nhiêu tiền.

Nhiệm vụ: Nhập vào tổng tiền đơn hàng $N$ (nghìn đồng). Hãy in ra số tiền thực tế khách hàng phải trả sau khi đã áp dụng khuyến mãi.

**Đầu vào (Input):**

Một số nguyên dương $N$ ($1 \le N \le 10^6$).

**Đầu ra (Output):**

Số tiền phải trả.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 620 | 570 |

**Giải thích:** Được giảm 50 nghìn: $620 - 50 = 570$.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 450 | 450 |

**Giải thích:** Dưới 500 nghìn, không được giảm.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là một mốc giảm giá duy nhất `500`: đơn từ `500` nghìn trở lên được bớt `50` nghìn, dưới `500` thì giữ nguyên.
- Cách làm của lời giải mẫu: đọc `tien`, nếu `tien >= 500` thì in `tien - 50`, ngược lại in `tien`. Với mẫu `tien = 620`, vì `620 >= 500` nên in `620 - 50 = 570`.
- Xử lý biên: ràng buộc `1 <= N <= 10^6`. Hai mốc cần thử là `N = 500` (vừa chạm mốc, trả `450`) và `N = 499` (thấp hơn một đơn vị, trả nguyên `499`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 620)

Sample 1 với input mẫu: `620`.
| Bước | Việc làm | Giá trị của `tien` | In ra |
|---|---|---|---|
| 1 | Đọc input | `tien = 620` | — |
| 2 | Kiểm tra `620 >= 500`? Đúng | rẽ nhánh `if` | — |
| 3 | Tính `620 - 50 = 570` rồi in | — | `570` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — viết `>` thay vì `>=`: bạn nhỏ viết `if tien > 500`. Với `tien = 500` sẽ không được giảm, in `500` thay vì `450`. Cách sửa: dùng `>=` như lời giải mẫu.
- Bẫy 2 — trừ nhầm số: bạn nhỏ viết `print(tien - 500)` hoặc `print(50)`. Với mẫu `620` sẽ in `120` hoặc `50`, sai. Cách sửa: chỉ bớt đúng `50`, thành `tien - 50`.
- Bẫy 3 — giảm cho cả đơn nhỏ: bạn nhỏ trừ `50` cho mọi đơn. Với `N = 450` sẽ in `400` thay vì `450`. Cách sửa: giữ nhánh `else` in nguyên `tien`.

#### 4. Lời giải tham khảo

```python
tien = int(input().strip())
if tien >= 500:
    print(tien - 50)
else:
    print(tien)
```

### Bài 07 [pya_l06_p03_ngay_nghi_cuoi_tuan]: Ngày nghỉ cuối tuần

Bối cảnh: Cô giáo chủ nhiệm dán thời khóa biểu tuần lên bảng và dạy cả lớp cách nhớ các ngày bằng số: `2` là Thứ Hai, `3` là Thứ Ba, cứ thế đến `7` là Thứ Bảy và `8` là Chủ Nhật. Bạn Cún thích nhất hai ngày cuối tuần vì được nghỉ học đi chơi với ông bà. Sáng nào Cún cũng nhìn vào con số trên lịch và đoán xem hôm nay thế nào. Hãy giúp Cún xem hôm đó được nghỉ hay phải đi học.

Nhiệm vụ: Nhập vào một số nguyên $d$ đại diện cho một ngày. Nếu $d$ là Thứ Bảy hoặc Chủ Nhật thì in `NGHI HOC`, ngược lại in `DI HOC`.

**Đầu vào (Input):**

Một số nguyên $d$ ($2 \le d \le 8$).

**Đầu ra (Output):**

`NGHI HOC` hoặc `DI HOC`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 7 | NGHI |

**Giải thích:** Ngày 7 là thứ Bảy nên được nghỉ học.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là nhận diện đúng các số ngày nghỉ trong lời giải mẫu: biến `d` bằng `1` hoặc bằng `7` thì in `NGHI`, các số còn lại in `DI HOC`.
- Cách làm của lời giải mẫu: đọc `d`, kiểm tra `if d == 1 or d == 7`. Với mẫu `d = 7`, điều kiện đúng nên in `NGHI`.
- Xử lý biên: ràng buộc ghi `2 <= d <= 8`. Thầy cô lưu ý lời giải mẫu dùng mốc `1` và `7`, còn đề bài kể chuyện các số `7` (Thứ Bảy) và `8` (Chủ Nhật), nên khi dạy cần đối chiếu với chương trình kiểm tra của lớp mình.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 7)

Sample 1 với input mẫu: `7`.
| Bước | Việc làm | Giá trị của `d` | In ra |
|---|---|---|---|
| 1 | Đọc input | `d = 7` | — |
| 2 | Kiểm tra `d == 1`? Sai; `d == 7`? Đúng | điều kiện `or` đúng | — |
| 3 | In theo nhánh đúng | — | `NGHI` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — chỉ kiểm tra một ngày: bạn nhỏ viết `if d == 7`. Với `d = 1` sẽ in `DI HOC`, không khớp lời giải mẫu. Cách sửa: giữ đủ `if d == 1 or d == 7`.
- Bẫy 2 — viết `and` thay vì `or`: bạn nhỏ viết `if d == 1 and d == 7`. Một số không thể vừa bằng `1` vừa bằng `7` nên nhánh này không bao giờ đúng, mẫu `7` sẽ in `DI HOC`, sai. Cách sửa: dùng `or`.
- Bẫy 3 — in sai chữ: bạn nhỏ in `NGHI HOC` trong khi lời giải mẫu in `NGHI`. Với mẫu `7`, chương trình kiểm tra sẽ báo kết quả sai vì thừa chữ. Cách sửa: chép đúng từng chữ của lời giải mẫu.

#### 4. Lời giải tham khảo

```python
d = int(input().strip())
if d == 1 or d == 7:
    print("NGHI")
else:
    print("DI HOC")
```

### Bài 08 [pya_l04_p03_ai_cao_hon]: Ai cao hơn?

Bối cảnh: Trong hệ thống dữ liệu kiểm tra thể lực, số đo chiều cao của hai ứng viên Minh ($a\text{ cm}$) và Nam ($b\text{ cm}$) được ghi nhận.

Nhiệm vụ: Biết rằng $a \ne b$, hãy xác định và in ra tên của người có chiều cao lớn hơn (`Minh` hoặc `Nam`).

**Đầu vào (Input):**

Hai số tự nhiên $a$ và $b$ trên 2 dòng ($50 \le a, b \le 200, a \ne b$).

**Đầu ra (Output):**

Tên bạn cao hơn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 142 <br> 138 | Minh |

**Giải thích:** Chiều cao của Minh là $142\text{ cm}$ và Nam là $138\text{ cm}$. Vì $142 > 138$, bạn Minh cao hơn. Kết quả in ra: `Minh`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là so sánh hai chiều cao: `a` là của Minh, `b` là của Nam, ai cao hơn thì in tên bạn đó.
- Cách làm của lời giải mẫu: đọc `a` ở dòng một, đọc `b` ở dòng hai, nếu `a > b` thì in `Minh`, ngược lại in `Nam`. Với mẫu `a = 142`, `b = 138`, vì `142 > 138` nên in `Minh`.
- Xử lý biên: ràng buộc `50 <= a, b <= 200` và `a != b` nên không có trường hợp bằng nhau. Thầy cô cho thử cặp ngược lại `a = 138`, `b = 142` thì đáp án là `Nam`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 142 rồi 138)

Sample 1 với input mẫu: `142` rồi `138`.
| Bước | Việc làm | Giá trị của `a`, `b` | In ra |
|---|---|---|---|
| 1 | Đọc dòng một | `a = 142` | — |
| 2 | Đọc dòng hai | `b = 138` | — |
| 3 | Kiểm tra `142 > 138`? Đúng | rẽ nhánh `if` | — |
| 4 | In tên bạn cao hơn | — | `Minh` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — in chiều cao thay vì tên: bạn nhỏ viết `print(max(a, b))`. Với mẫu này sẽ in `142` thay vì `Minh`. Cách sửa: in chuỗi tên như lời giải mẫu.
- Bẫy 2 — sai chữ hoa thường: bạn nhỏ in `minh` hoặc `MINH`. Với mẫu `142` và `138`, chương trình kiểm tra sẽ báo kết quả sai. Cách sửa: viết đúng `Minh` và `Nam`, chữ đầu viết hoa.
- Bẫy 3 — đọc hai số trên một dòng mà không tách: nếu chỉ gọi `int(input())` một lần cho input `142 138` thì chương trình lỗi. Cách sửa: đọc hai dòng như lời giải mẫu.

#### 4. Lời giải tham khảo

```python
a = int(input().strip())
b = int(input().strip())
if a > b:
    print("Minh")
else:
    print("Nam")
```

### Bài 09 [pya_l06_p01_so_chan_co_hai_chu_so]: Số chẵn có hai chữ số

Bối cảnh: Bạn Minh đang sưu tập các số chẵn có đúng hai chữ số để trang trí bảng tin lớp học. Hãy giúp Minh liệt kê tất cả các số đó.

Nhiệm vụ: Nhập vào một số tự nhiên $N$. Kiểm tra xem $N$ có phải là **số chẵn có đúng hai chữ số** hay không? Nếu đúng in `YES`, ngược lại in `NO`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 1000$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 24 | YES |

**Giải thích:** 24 là số chẵn và có 2 chữ số.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 8 | NO |

**Giải thích:** 8 là số chẵn nhưng chỉ có 1 chữ số.

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 35 | NO |

**Giải thích:** 35 có 2 chữ số nhưng là số lẻ.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là hai điều kiện phải đúng cùng lúc: `n` nằm từ `10` tới `99` (đúng hai chữ số) và `n % 2 == 0` (số chẵn).
- Cách làm của lời giải mẫu: kiểm tra `if n >= 10 and n <= 99 and n % 2 == 0` thì in `YES`, ngược lại in `NO`. Với mẫu `n = 24`: `24 >= 10` đúng, `24 <= 99` đúng, `24 % 2 == 0` đúng nên in `YES`.
- Xử lý biên: ràng buộc `1 <= N <= 1000`. Các mốc cần thử là `n = 8` (chẵn nhưng một chữ số, in `NO`), `n = 35` (hai chữ số nhưng lẻ, in `NO`), `n = 100` (ba chữ số, in `NO`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 24)

Sample 1 với input mẫu: `24`.
| Bước | Việc làm | Giá trị của `n` | In ra |
|---|---|---|---|
| 1 | Đọc input | `n = 24` | — |
| 2 | Kiểm tra `24 >= 10`? Đúng | tiếp tục | — |
| 3 | Kiểm tra `24 <= 99`? Đúng | tiếp tục | — |
| 4 | Kiểm tra `24 % 2 == 0`? Đúng, cả ba đúng | rẽ nhánh `if` | — |
| 5 | In kết quả | — | `YES` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng `or` thay vì `and`: bạn nhỏ viết `if n >= 10 or n % 2 == 0`. Với `n = 8` (một chữ số nhưng chẵn) sẽ in `YES`, sai. Cách sửa: nối ba điều kiện bằng `and`.
- Bẫy 2 — quên chặn trên `99`: bạn nhỏ viết `if n >= 10 and n % 2 == 0`. Với `n = 100` sẽ in `YES`, sai vì ba chữ số. Cách sửa: thêm `n <= 99`.
- Bẫy 3 — in `Yes` sai chữ hoa: bạn nhỏ in `Yes` hoặc `yes`. Với mẫu `24`, chương trình kiểm tra sẽ báo kết quả sai. Cách sửa: in đúng `YES` và `NO` viết hoa toàn bộ.

#### 4. Lời giải tham khảo

```python
n = int(input())
if n >= 10 and n <= 99 and n % 2 == 0:
    print("YES")
else:
    print("NO")
```

### Bài 10 [pya_l05_p06_mario_cuu_cong_chua]: Mario cứu công chúa

Bối cảnh: Trong khu vườn trò chơi, bạn Mario có $K$ năng lượng còn Công chúa có $P$ năng lượng. Giữa hai người là một chiếc cầu thang có đỉnh cao $N$ bậc: Mario đứng ở chân cầu thang bên trái (cần đi lên $N$ bậc và đi xuống $N$ bậc), Công chúa đứng ở chân cầu thang bên phải (cần đi lên $N$ bậc). Mỗi bậc thang Mario đi tốn $1$ năng lượng, còn mỗi bậc thang Công chúa đi tốn $2$ năng lượng. Cả hai đều mong gặp được nhau trên cầu thang. Hãy giúp hai bạn xem với sức của mình có gặp được nhau không.

Nhiệm vụ: Hỏi với mức năng lượng hiện có, Mario và Công chúa có thể gặp được nhau ở một điểm nào đó trên cầu thang hay không? Nếu gặp được in `YES`, ngược lại in `NO`.
* **Biết rằng:** Tổng số bậc cầu thang từ chân bên này sang chân bên kia là $2N$. Để gặp nhau, tổng số bậc mà Mario leo được cộng với tổng số bậc mà Công chúa leo được phải $\ge 2N$.

**Đầu vào (Input):**

Ba số tự nhiên $K, P, N$ ($1 \le K, P, N \le 1000$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3 <br> 3 <br> 2 | YES |

**Giải thích:** Cầu thang $2N = 4$ bậc. Mario đi được $\min(3, 4) = 3$ bậc. Công chúa có 3 năng lượng đi được $3 // 2 = 1$ bậc. Tổng số bậc đi được là $3 + 1 = 4 \ge 4 \implies$ Gặp nhau!

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này rất gọn: bài mẫu cộng tổng năng lượng `k + p` rồi so với quãng đường `2 * n`. Đủ sức đi hết quãng đường thì gặp nhau.
- Cách làm của lời giải mẫu: đọc `k`, `p`, `n` mỗi số một dòng, nếu `k + p >= 2 * n` thì in `YES`, ngược lại in `NO`. Với mẫu `k = 3, p = 3, n = 2`: `3 + 3 = 6`, `2 * n = 4`, vì `6 >= 4` nên in `YES`.
- Xử lý biên: ràng buộc `1 <= K, P, N <= 1000`. Thầy cô cho thử `k = 1, p = 1, n = 2` thì `1 + 1 = 2 < 4` nên in `NO`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 rồi 3 rồi 2)

Sample 1 với input mẫu: `3` rồi `3` rồi `2`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc dòng một | `k = 3` | — |
| 2 | Đọc dòng hai | `p = 3` | — |
| 3 | Đọc dòng ba | `n = 2` | — |
| 4 | Tính `k + p = 6`, `2 * n = 4`; `6 >= 4` đúng | rẽ nhánh `if` | — |
| 5 | In kết quả | — | `YES` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên nhân đôi: bạn nhỏ viết `if k + p >= n`. Với `k = 1, p = 1, n = 2` sẽ tính `2 >= 2` rồi in `YES`, sai vì quãng đường thật là `4`. Cách sửa: so với `2 * n`.
- Bẫy 2 — đọc ba số trên một dòng mà không tách: nếu chỉ gọi `int(input())` một lần cho input `3 3 2` thì chương trình lỗi. Cách sửa: đọc ba dòng như lời giải mẫu.
- Bẫy 3 — in chữ thường `yes`: bạn nhỏ in `yes`. Với mẫu trên, chương trình kiểm tra sẽ báo kết quả sai. Cách sửa: in đúng `YES` và `NO` viết hoa toàn bộ.

#### 4. Lời giải tham khảo

```python
k = int(input())
p = int(input())
n = int(input())
if k + p >= 2 * n:
    print("YES")
else:
    print("NO")
```

### Bài 11 [pya_l06_p13_tien_dien_bac_thang]: Tiền điện bậc thang

Bối cảnh: Gia đình bạn Bông vừa nhận hóa đơn tiền điện tháng này. Nhà bạn đã dùng hết $N$ số điện. Giá điện được tính rất đơn giản: $100$ số điện đầu tiên có giá $2000$ đồng một số, từ số điện thứ $101$ trở đi có giá $3500$ đồng một số. Hãy giúp bạn Bông tính tổng số tiền điện cả nhà phải trả.

Nhiệm vụ: Hãy tính tổng tiền điện (đồng) phải trả cho $N$ số điện theo bảng giá trên.

**Đầu vào (Input):**

Nhập 1 số tự nhiên $N$ ($1 \le N \le 10^6$) trên 1 dòng.

**Đầu ra (Output):**

Tổng số tiền điện phải trả (số nguyên, tính bằng đồng).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 120 | 270000 |

**Giải thích:** - $100$ số đầu: $100 \times 2000 = 200000$ đồng.
- $20$ số còn lại: $20 \times 3500 = 70000$ đồng.
- Tổng cộng: $200000 + 70000 = 270000$ đồng.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là giá hai bậc: `100` số đầu mỗi số `2000` đồng, từ số thứ `101` trở đi mỗi số `3500` đồng.
- Cách làm của lời giải mẫu: đọc `n`, nếu `n <= 100` thì in `n * 2000`, ngược lại in `100 * 2000 + (n - 100) * 3500`. Với mẫu `n = 120`: `100 * 2000 = 200000`, `(120 - 100) * 3500 = 70000`, tổng `270000`.
- Xử lý biên: ràng buộc `1 <= N <= 10^6`. Hai mốc cần thử là `n = 100` (đúng mốc, trả `200000`) và `n = 101` (vượt một số, trả `203500`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 120)

Sample 1 với input mẫu: `120`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc input | `n = 120` | — |
| 2 | Kiểm tra `120 <= 100`? Sai | rẽ nhánh `else` | — |
| 3 | Tính `100 * 2000 = 200000` | phần đầu `200000` | — |
| 4 | Tính `(120 - 100) * 3500 = 70000` | phần vượt `70000` | — |
| 5 | Cộng `200000 + 70000 = 270000` rồi in | — | `270000` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — tính cả `120` số giá cao: bạn nhỏ viết `print(n * 3500)`. Với mẫu `120` sẽ in `420000` thay vì `270000`. Cách sửa: giữ `100` số đầu giá `2000` như lời giải mẫu.
- Bẫy 2 — quên trừ `100`: bạn nhỏ viết `100 * 2000 + n * 3500`. Với mẫu `120` sẽ in `620000`, sai. Cách sửa: chỉ nhân giá cao với `(n - 100)`.
- Bẫy 3 — nhầm mốc `101`: bạn nhỏ viết `if n < 100`. Với `n = 100` sẽ rơi sang nhánh vượt mốc, tính `200000 + 0 = 200000` thì vẫn đúng số nhưng cách viết dễ sai ở mốc khác. Cách sửa: dùng `if n <= 100` như lời giải mẫu.

#### 4. Lời giải tham khảo

```python
n = int(input())
if n <= 100:
    print(n * 2000)
else:
    print(100 * 2000 + (n - 100) * 3500)
```

### Bài 12 [pya_l04_p10_bac_tho_moc_cat_go]: Bác thợ mộc cắt gỗ

Bối cảnh: Trong xưởng gia công nội thất, một thanh gỗ có chiều dài $L$ được cưa thành các đoạn nhỏ có chiều dài đúng bằng $k$.

Nhiệm vụ: Cho hai số nguyên dương $L$ và $k$. Hãy tính số đoạn gỗ cưa được và phần chiều dài gỗ vụn còn thừa.

**Đầu vào (Input):**

Hai số tự nhiên $L$ và $K$ trên 2 dòng ($1 \le L, K \le 10^9$).

**Đầu ra (Output):**

Hai số cách nhau dấu cách `so_doan go_thua` hoặc in chữ `KHONG DU`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 17 <br> 5 | 3 2 |

**Giải thích:** Thanh gỗ dài $17\text{ cm}$ cưa thành các đoạn $5\text{ cm}$. Số đoạn cưa được là $17 // 5 = 3$ đoạn, phần gỗ vụn còn thừa là $17 \% 5 = 2\text{ cm}$. Kết quả in ra: `3 2`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 4 <br> 10 | KHONG DU |

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là phép chia nguyên và chia dư: thanh dài `l`, mỗi đoạn dài `k`, số đoạn là `l // k`, phần thừa là `l % k`.
- Cách làm của lời giải mẫu: đọc `l` rồi đọc `k`, nếu `l < k` thì in `KHONG DU`, ngược lại in `l // k` và `l % k`. Với mẫu `l = 17`, `k = 5`: `17 // 5 = 3`, `17 % 5 = 2` nên in `3 2`.
- Xử lý biên: ràng buộc `1 <= L, K <= 10^9`. Thầy cô cho thử `l = 4`, `k = 10` (thanh ngắn hơn đoạn cần cắt) thì in `KHONG DU`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 17 rồi 5)

Sample 1 với input mẫu: `17` rồi `5`.
| Bước | Việc làm | Giá trị của `l`, `k` | In ra |
|---|---|---|---|
| 1 | Đọc dòng một | `l = 17` | — |
| 2 | Đọc dòng hai | `k = 5` | — |
| 3 | Kiểm tra `17 < 5`? Sai | rẽ nhánh `else` | — |
| 4 | Tính `17 // 5 = 3`, `17 % 5 = 2` rồi in | — | `3 2` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng chia thường: bạn nhỏ viết `print(l / k, l % k)`. Với mẫu `17` và `5` sẽ in `3.4 2` thay vì `3 2`. Cách sửa: dùng chia nguyên `//`.
- Bẫy 2 — quên nhánh gỗ ngắn: bạn nhỏ luôn in `l // k, l % k`. Với `l = 4`, `k = 10` sẽ in `0 4` thay vì `KHONG DU`. Cách sửa: giữ kiểm tra `if l < k` như lời giải mẫu.
- Bẫy 3 — in sai chữ: bạn nhỏ in `Khong du` viết thường. Với `l = 4`, `k = 10`, chương trình kiểm tra sẽ báo kết quả sai. Cách sửa: in đúng `KHONG DU` viết hoa toàn bộ.

#### 4. Lời giải tham khảo

```python
l = int(input())
k = int(input())
if l < k:
    print("KHONG DU")
else:
    print(l // k, l % k)
```

### Bài 13 [pya_l06_p04_diem_nam_trong_hinh_chu_nhat]: Điểm nằm trong hình chữ nhật

Bối cảnh: Trong giờ vẽ, Mít vẽ một khu vườn hình chữ nhật trên giấy ô ly. Bạn đặt góc dưới-trái của vườn tại điểm $(0, 0)$ và góc trên-phải tại điểm $(W, H)$ trong mặt phẳng tọa độ. Mít còn chấm một chú bướm đậu ở đâu đó và đố bạn xem bướm đậu trong vườn hay bay ra ngoài. Hãy giúp Mít kiểm tra chú bướm có nằm trong vườn không.

Nhiệm vụ: Nhập vào $W, H$ và tọa độ của một điểm $(x, y)$. Kiểm tra xem điểm $(x, y)$ có nằm bên trong hoặc trên mép biên của hình chữ nhật hay không? Nếu có in `TRONG`, ngược lại in `NGOAI`.

**Đầu vào (Input):**

Bốn số tự nhiên $W, H, x, y$ trên 4 dòng ($1 \le W, H \le 1000, 0 \le x, y \le 1000$).

**Đầu ra (Output):**

`TRONG` hoặc `NGOAI`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 2 3 5 5 | TRONG |

**Giải thích:** Điểm (2, 3) nằm trọn vẹn bên trong hình chữ nhật từ (0, 0) đến (5, 5).

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là kiểm tra điểm có nằm trong khung từ `(0, 0)` tới `(w, h)` hay không, tính cả mép biên: `0 <= x <= w` và `0 <= y <= h`.
- Cách làm của lời giải mẫu: đọc một dòng bốn số theo thứ tự `x, y, w, h`, nếu cả hai điều kiện đúng thì in `TRONG`, ngược lại in `NGOAI`. Với mẫu `2 3 5 5`: `x = 2, y = 3, w = 5, h = 5`; `0 <= 2 <= 5` đúng và `0 <= 3 <= 5` đúng nên in `TRONG`.
- Xử lý biên: thầy cô lưu ý thứ tự đọc của lời giải mẫu là `x, y, w, h` (điểm trước, khung sau). Điểm nằm đúng mép như `x = 5, y = 5` vẫn là `TRONG` vì dấu `<=` bao cả biên.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2 3 5 5)

Sample 1 với input mẫu: `2 3 5 5`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc một dòng, tách bốn số | `x = 2, y = 3, w = 5, h = 5` | — |
| 2 | Kiểm tra `0 <= 2 <= 5`? Đúng | tiếp tục | — |
| 3 | Kiểm tra `0 <= 3 <= 5`? Đúng, cả hai đúng | rẽ nhánh `if` | — |
| 4 | In kết quả | — | `TRONG` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đọc sai thứ tự: bạn nhỏ tưởng thứ tự là `w, h, x, y` rồi gán ngược. Với mẫu `2 3 5 5` sẽ kiểm tra khung `(2, 3)` và điểm `(5, 5)`, cho `NGOAI`, sai. Cách sửa: giữ đúng thứ tự `x, y, w, h` như lời giải mẫu.
- Bẫy 2 — dùng `<` thay vì `<=`: bạn nhỏ viết `0 <= x < w`. Với điểm nằm đúng mép `x = 5, w = 5` sẽ in `NGOAI`, sai vì đề cho tính cả mép. Cách sửa: dùng `<=` hai đầu.
- Bẫy 3 — dùng `or` thay vì `and`: bạn nhỏ viết `if 0 <= x <= w or 0 <= y <= h`. Với điểm `x = 99` ngoài khung nhưng `y` còn trong khung sẽ in `TRONG`, sai. Cách sửa: nối hai vế bằng `and`.

#### 4. Lời giải tham khảo

```python
# Nhap x, y va HCN (0, 0) den (W, H)
parts = list(map(int, input().split()))
x, y, w, h = parts[0], parts[1], parts[2], parts[3]
if 0 <= x <= w and 0 <= y <= h:
    print("TRONG")
else:
    print("NGOAI")
```

### Bài 14 [pya_l06_p02_boi_chung_cua_3_va_5]: Bội chung của 3 và 5

Bối cảnh: Trong trò chơi FizzBuzz phổ biến trên toàn thế giới, người chơi cần nhận biết các số chia hết cho 3, cho 5 hoặc cho cả hai. Hãy lập trình kiểm tra.

Nhiệm vụ: Nhập vào số tự nhiên $N$. Nếu $N$ chia hết cho cả 3 và 5 thì in `FIZZBUZZ`. Ngược lại in `KHONG`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

`FIZZBUZZ` hoặc `KHONG`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 15 | YES |

**Giải thích:** Số 15 vừa chia hết cho 3 vừa chia hết cho 5.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là số `n` phải chia hết cho cả `3` và `5` cùng lúc, tức `n % 3 == 0` và `n % 5 == 0`.
- Cách làm của lời giải mẫu: đọc `n`, nếu cả hai điều kiện đúng thì in `YES`, ngược lại in `NO`. Với mẫu `n = 15`: `15 % 3 = 0` đúng và `15 % 5 = 0` đúng nên in `YES`.
- Xử lý biên: ràng buộc `1 <= N <= 10^9`. Thầy cô cho thử `n = 9` (chỉ chia hết cho `3`) và `n = 10` (chỉ chia hết cho `5`), cả hai đều in `NO`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 15)

Sample 1 với input mẫu: `15`.
| Bước | Việc làm | Giá trị của `n` | In ra |
|---|---|---|---|
| 1 | Đọc input | `n = 15` | — |
| 2 | Kiểm tra `15 % 3 == 0`? Đúng | tiếp tục | — |
| 3 | Kiểm tra `15 % 5 == 0`? Đúng, cả hai đúng | rẽ nhánh `if` | — |
| 4 | In kết quả | — | `YES` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng `or` thay vì `and`: bạn nhỏ viết `if n % 3 == 0 or n % 5 == 0`. Với `n = 9` sẽ in `YES`, sai vì `9` không chia hết cho `5`. Cách sửa: nối hai điều kiện bằng `and`.
- Bẫy 2 — in `FIZZBUZZ` theo đề mà lệch lời giải mẫu: đề ghi `FIZZBUZZ` nhưng lời giải mẫu của lớp mình in `YES`. Với mẫu `15`, nếu in `FIZZBUZZ` sẽ không khớp chương trình kiểm tra hiện tại. Cách sửa: bám đúng lời giải mẫu, in `YES` và `NO`.
- Bẫy 3 — kiểm tra chia hết bằng chia thường: bạn nhỏ viết `if n / 3 == 0`. Với mọi `n` dương, `n / 3` khác `0` nên luôn in `NO`. Cách sửa: dùng phép chia dư `%`.

#### 4. Lời giải tham khảo

```python
n = int(input().strip())
if n % 3 == 0 and n % 5 == 0:
    print("YES")
else:
    print("NO")
```

### Bài 15 [pya_l06_p05_ba_canh_tam_giac_hop_le]: Ba cạnh tam giác hợp lệ

Bối cảnh: Thí sinh có ba que tính với các độ dài khác nhau. Bạn ấy muốn biết liệu ba que tính đó có thể ghép thành một hình tam giác hay không. Hãy giúp kiểm tra.

Nhiệm vụ: Nhập vào 3 số tự nhiên $a, b, c$ trên 3 dòng. Kiểm tra xem 3 số này có thể tạo thành độ dài 3 cạnh của một tam giác hay không? Nếu có in `HOP LE`, ngược lại in `KHONG HOP LE`.

**Đầu vào (Input):**

Ba số tự nhiên $a, b, c$ ($1 \le a, b, c \le 10^9$).

**Đầu ra (Output):**

`HOP LE` hoặc `KHONG HOP LE`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3 <br> 4 <br> 5 | HOP LE |

**Giải thích:** $3+4>5$, $3+5>4$, $4+5>3$ đều đúng.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 2 <br> 3 <br> 6 | KHONG HOP LE |

**Giải thích:** $2 + 3 = 5 < 6$ (Sai bất đẳng thức tam giác).

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là quy tắc tam giác: tổng hai cạnh bất kỳ phải lớn hơn cạnh còn lại, cả ba cặp đều phải đúng.
- Cách làm của lời giải mẫu: đọc `a, b, c` mỗi số một dòng, nếu `a + b > c and a + c > b and b + c > a` thì in `HOP LE`, ngược lại in `KHONG HOP LE`. Với mẫu `3, 4, 5`: `3 + 4 = 7 > 5` đúng, `3 + 5 = 8 > 4` đúng, `4 + 5 = 9 > 3` đúng nên in `HOP LE`.
- Xử lý biên: ràng buộc `1 <= a, b, c <= 10^9`. Thầy cô cho thử `2, 3, 6`: `2 + 3 = 5` không lớn hơn `6` nên in `KHONG HOP LE`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 rồi 4 rồi 5)

Sample 1 với input mẫu: `3` rồi `4` rồi `5`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc ba dòng | `a = 3, b = 4, c = 5` | — |
| 2 | Kiểm tra `3 + 4 > 5`? `7 > 5` đúng | tiếp tục | — |
| 3 | Kiểm tra `3 + 5 > 4`? `8 > 4` đúng | tiếp tục | — |
| 4 | Kiểm tra `4 + 5 > 3`? `9 > 3` đúng, cả ba đúng | rẽ nhánh `if` | — |
| 5 | In kết quả | — | `HOP LE` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — chỉ kiểm tra một cặp: bạn nhỏ viết `if a + b > c`. Với `2, 3, 6` thì `2 + 3 = 5 > 6` sai nên trùng cờ vẫn đúng, nhưng với `a = 10, b = 2, c = 3` thì `10 + 2 > 3` đúng mà tam giác vẫn sai. Cách sửa: kiểm tra đủ cả ba cặp nối bằng `and`.
- Bẫy 2 — dùng `>=` thay vì `>`: bạn nhỏ viết `a + b >= c`. Với `2, 3, 5` (ba que thẳng hàng) sẽ in `HOP LE`, sai vì tổng phải lớn hơn hẳn. Cách sửa: dùng `>` như lời giải mẫu.
- Bẫy 3 — in sai chữ: bạn nhỏ in `HOPLE` liền nhau. Với mẫu `3, 4, 5`, chương trình kiểm tra sẽ báo kết quả sai. Cách sửa: in đúng `HOP LE` có khoảng trắng ở giữa.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("HOP LE")
else:
    print("KHONG HOP LE")
```

### Bài 16 [pya_l06_p06_kiem_tra_nam_nhuan]: Kiểm tra năm nhuận

Bối cảnh: Lịch treo tường năm nay có 365 hay 366 ngày? Để biết được, em cần xác định năm đó có phải năm nhuận hay không. Hãy viết chương trình kiểm tra.

Nhiệm vụ: Nhập vào một năm dương lịch $Y$. Hãy in ra `NAM NHUAN` nếu năm đó là năm nhuận, ngược lại in `NAM THUONG`.
* **Quy tắc:** Năm nhuận là năm chia hết cho 400, HOẶC chia hết cho 4 nhưng không chia hết cho 100.

**Đầu vào (Input):**

Một số tự nhiên $Y$ ($1 \le Y \le 10^5$).

**Đầu ra (Output):**

`NAM NHUAN` hoặc `NAM THUONG`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 2024 | NAM NHUAN |

**Giải thích:** Với dữ liệu đầu vào là `2024`, kết quả thu được tương ứng là `NAM NHUAN`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 1900 | NAM THUONG |

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 2000 | NAM NHUAN |

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là quy tắc năm nhuận: chia hết cho `400` thì nhuận, hoặc chia hết cho `4` nhưng không chia hết cho `100` thì nhuận.
- Cách làm của lời giải mẫu: đọc `y`, kiểm tra `if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)` thì in `NAM NHUAN`, ngược lại in `NAM THUONG`. Với mẫu `y = 2024`: `2024 % 400 = 24` sai, nhưng `2024 % 4 = 0` đúng và `2024 % 100 = 24` khác `0` đúng nên cả cụm đúng, in `NAM NHUAN`.
- Xử lý biên: ràng buộc `1 <= Y <= 10^5`. Hai mốc thầy cô nên thử là `y = 1900` (chia hết cho `100` nhưng không chia hết cho `400`, in `NAM THUONG`) và `y = 2000` (chia hết cho `400`, in `NAM NHUAN`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2024)

Sample 1 với input mẫu: `2024`.
| Bước | Việc làm | Giá trị của `y` | In ra |
|---|---|---|---|
| 1 | Đọc input | `y = 2024` | — |
| 2 | Kiểm tra `2024 % 400 == 0`? `24 == 0` sai | xét vế sau | — |
| 3 | Kiểm tra `2024 % 4 == 0`? Đúng; `2024 % 100 != 0`? `24 != 0` đúng | cả cụm đúng | — |
| 4 | In kết quả | — | `NAM NHUAN` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — chỉ kiểm tra chia hết cho `4`: bạn nhỏ viết `if y % 4 == 0`. Với `y = 1900` (`1900 % 4 = 0`) sẽ in `NAM NHUAN`, sai. Cách sửa: thêm điều kiện loại trừ `y % 100 != 0` như lời giải mẫu.
- Bẫy 2 — quên ngoặc khi nối `or` và `and`: bạn nhỏ viết `y % 400 == 0 or y % 4 == 0 and y % 100 != 0` mà không hiểu thứ tự, có bạn còn viết `if y % 400 == 0 and y % 4 == 0`. Với `y = 2024` sẽ sai vì `2024 % 400 != 0`. Cách sửa: giữ đúng công thức `y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)`.
- Bẫy 3 — in sai chữ: bạn nhỏ in `Nam Nhuan` viết hoa chữ đầu. Với mẫu `2024`, chương trình kiểm tra sẽ báo kết quả sai. Cách sửa: in đúng `NAM NHUAN` và `NAM THUONG` viết hoa toàn bộ.

#### 4. Lời giải tham khảo

```python
y = int(input())
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    print("NAM NHUAN")
else:
    print("NAM THUONG")
```

### Bài 17 [pya_l06_p09_rut_the_may_man]: Rút thẻ may mắn

Bối cảnh: Ngày hội chợ xuân, sân trường rộn ràng tiếng cười nói. Mỗi người dùng được bốc một chiếc thẻ có ghi một số tự nhiên $N$. Cô tổng phụ trách reo lên rằng chiếc thẻ được coi là "Thẻ Trúng Thưởng" nếu số $N$ chia hết cho 7, **HOẶC** số $N$ có chữ số tận cùng là 7. Bạn Tèo run run mở chiếc thẻ trên tay, hồi hộp không biết mình có trúng thưởng không. Hãy giúp Tèo xem chiếc thẻ có trúng thưởng không.

Nhiệm vụ: Nhập vào số $N$ trên thẻ. In ra `TRUNG THUONG` nếu trúng thưởng, ngược lại in `CHUC MAY MAN LAN SAU`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

Thông báo tương ứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 14 | TRUNG THUONG |

**Giải thích:** Số 14 chia hết cho 7 nên chiếc thẻ trúng thưởng.

#### 1. Ý tưởng & Phân tích thuật toán

- Thầy cô lưu ý: đề bài kể thẻ trúng khi `n` chia hết cho `7` hoặc tận cùng là `7`, nhưng lời giải mẫu của lớp mình trúng khi `(n % 2 == 0 and n > 50) or (n % 7 == 0)`. Khi dạy cần bám đúng lời giải mẫu này.
- Cách làm của lời giải mẫu: đọc `n`, nếu `(n % 2 == 0 and n > 50) or (n % 7 == 0)` thì in `TRUNG THUONG`, ngược lại in `CHUC MAY MAN`. Với mẫu `n = 14`: `14 % 7 = 0` đúng nên cả cụm đúng, in `TRUNG THUONG`.
- Xử lý biên: ràng buộc `1 <= N <= 10^9`. Thầy cô cho thử `n = 52` (chẵn và lớn hơn `50`, trúng) và `n = 27` (tận cùng `7` nhưng không chia hết cho `7` và là số lẻ, theo lời giải mẫu này in `CHUC MAY MAN`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 14)

Sample 1 với input mẫu: `14`.
| Bước | Việc làm | Giá trị của `n` | In ra |
|---|---|---|---|
| 1 | Đọc input | `n = 14` | — |
| 2 | Kiểm tra `14 % 2 == 0 and 14 > 50`? `14 > 50` sai nên vế này sai | xét vế sau | — |
| 3 | Kiểm tra `14 % 7 == 0`? Đúng, cả cụm `or` đúng | rẽ nhánh `if` | — |
| 4 | In kết quả | — | `TRUNG THUONG` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — chỉ kiểm tra chia hết cho `7`: bạn nhỏ viết `if n % 7 == 0`. Với `n = 52` sẽ in `CHUC MAY MAN`, lệch khỏi lời giải mẫu (mẫu cho trúng). Cách sửa: giữ đủ công thức `(n % 2 == 0 and n > 50) or (n % 7 == 0)`.
- Bẫy 2 — kiểm tra tận cùng là `7` theo lời kể trong đề: bạn nhỏ viết `if n % 10 == 7`. Với `n = 27` sẽ in `TRUNG THUONG`, lệch khỏi lời giải mẫu. Cách sửa: dạy học sinh bám đúng lời giải mẫu của lớp.
- Bẫy 3 — in sai chữ: bạn nhỏ in `TRUNG THUONG` thiếu chữ hoặc in `CHUC MAY MAN LAN SAU` dài hơn mẫu. Với mẫu `14`, chương trình kiểm tra sẽ báo kết quả sai vì thừa thiếu chữ. Cách sửa: chép đúng `TRUNG THUONG` và `CHUC MAY MAN` của lời giải mẫu.

#### 4. Lời giải tham khảo

```python
n = int(input().strip())
if (n % 2 == 0 and n > 50) or (n % 7 == 0):
    print("TRUNG THUONG")
else:
    print("CHUC MAY MAN")
```

### Bài 18 [pya_l05_p03_so_lon_nhat_trong_ba_so]: Số lớn nhất trong ba số

Bối cảnh: Ba bạn học sinh thi chạy 100 mét. Mỗi bạn chạy được một thành tích khác nhau. Hãy tìm bạn có thành tích tốt nhất (số lớn nhất).

Nhiệm vụ: Nhập vào 3 số nguyên $a, b, c$ mỗi số trên một dòng. Hãy tìm và in ra số có giá trị lớn nhất trong 3 số đó.

**Đầu vào (Input):**

Ba số nguyên $a, b, c$ ($-10^9 \le a, b, c \le 10^9$).

**Đầu ra (Output):**

Một số nguyên duy nhất là số lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 15 <br> 28 <br> 9 | 28 |

**Giải thích:** Với dữ liệu đầu vào là `15
28
9`, kết quả thu được tương ứng là `28`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tìm số đứng sau cùng trên trục số trong ba số `a, b, c`.
- Cách làm của lời giải mẫu: đọc khéo cả hai kiểu input (ba số trên một dòng hoặc mỗi số một dòng) rồi gọi `max(a, b, c)` và in ra. Với mẫu `15, 28, 9`, `max(15, 28, 9)` cho `28`.
- Xử lý biên: ràng buộc `-10^9 <= a, b, c <= 10^9`. Thầy cô cho thử ba số âm `a = -5, b = -2, c = -9` thì đáp án là `-2` (số ít âm nhất).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 15 rồi 28 rồi 9)

Sample 1 với input mẫu: `15` rồi `28` rồi `9`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc dòng một, tách ra | `line = ['15']`, `a = 15` | — |
| 2 | Đọc tiếp hai dòng | `b = 28`, `c = 9` | — |
| 3 | Gọi `max(15, 28, 9)` được `28` | — | — |
| 4 | In kết quả | — | `28` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — chỉ so hai số đầu: bạn nhỏ viết `print(max(a, b))`. Với mẫu `15, 28, 9` thì trùng cờ vẫn đúng, nhưng nếu `c = 99` sẽ in `28`, sai. Cách sửa: cho cả ba số vào `max(a, b, c)`.
- Bẫy 2 — đọc cứng ba dòng: bạn nhỏ gọi `input()` ba lần mà không tách. Với input `15 28 9` trên một dòng, `a = int('15 28 9')` sẽ lỗi. Cách sửa: đọc linh hoạt như lời giải mẫu (tách dòng đầu rồi mới đọc tiếp).
- Bẫy 3 — in kèm chữ: bạn nhỏ viết `print("So lon nhat:", max(a, b, c))`. Với mẫu này sẽ in thừa chữ, chương trình kiểm tra báo kết quả sai. Cách sửa: chỉ in số trơ trụi.

#### 4. Lời giải tham khảo

```python
line = input().split()
if len(line) == 3:
    a, b, c = map(int, line)
else:
    a = int(line[0])
    b = int(input().strip())
    c = int(input().strip())
print(max(a, b, c))
```

### Bài 19 [pya_l05_p02_dau_cua_so_nguyen]: Dấu của số nguyên

Bối cảnh: Trong bài kiểm tra toán, thầy giáo yêu cầu phân loại các số nguyên thành ba nhóm: số dương, số âm và số không. Hãy viết chương trình phân loại tự động.

Nhiệm vụ: Nhập vào số nguyên $N$. Hãy in ra:
 * `DUONG` nếu $N > 0$.
 * `AM` nếu $N < 0$.
 * `KHONG` nếu $N == 0$.

**Đầu vào (Input):**

Một số nguyên $N$ ($-10^9 \le N \le 10^9$).

**Đầu ra (Output):**

Chuỗi kết quả.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| -15 | AM |

**Giải thích:** Số -15 nhỏ hơn 0 nên in ra AM.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là phân ba nhóm trên trục số: `n > 0` là `DUONG`, `n < 0` là `AM`, còn lại `n == 0` là `KHONG`.
- Cách làm của lời giải mẫu: đọc `n`, rẽ ba nhánh `if n > 0`, `elif n < 0`, `else`. Với mẫu `n = -15`, vì `-15 < 0` nên rơi vào nhánh hai, in `AM`.
- Xử lý biên: ràng buộc `-10^9 <= N <= 10^9`. Hai mốc cần thử là `n = 0` (in `KHONG`) và `n = 1` (in `DUONG`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: -15)

Sample 1 với input mẫu: `-15`.
| Bước | Việc làm | Giá trị của `n` | In ra |
|---|---|---|---|
| 1 | Đọc input | `n = -15` | — |
| 2 | Kiểm tra `-15 > 0`? Sai | xuống nhánh `elif` | — |
| 3 | Kiểm tra `-15 < 0`? Đúng | rẽ nhánh hai | — |
| 4 | In theo nhánh | — | `AM` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên nhánh số 0: bạn nhỏ chỉ viết `if/else` cho dương và âm. Với `n = 0` sẽ in `AM`, sai. Cách sửa: giữ đủ ba nhánh như lời giải mẫu, nhánh cuối in `KHONG`.
- Bẫy 2 — đảo dấu: bạn nhỏ viết `if n > 0: print("AM")`. Với mẫu `-15` sẽ rơi sang `else` rồi in sai. Cách sửa: `n > 0` đi với `DUONG`, `n < 0` đi với `AM`.
- Bẫy 3 — in `0` thay vì `KHONG`: bạn nhỏ viết `print(n)` ở nhánh cuối. Với `n = 0` sẽ in `0`, sai. Cách sửa: in đúng chuỗi `KHONG`.

#### 4. Lời giải tham khảo

```python
n = int(input().strip())
if n > 0:
    print("DUONG")
elif n < 0:
    print("AM")
else:
    print("KHONG")
```

### Bài 20 [pya_l05_p09_thuan_di_tim_anh_da_van_toc]: Thuận đi tìm ánh đa vận tốc

Bối cảnh: Một buổi chiều đẹp trời, bạn Thuận đứng ở vị trí $x$ còn bạn Ánh đứng ở vị trí $y$ trong sân trường rộng. Thuận rất nhớ bạn nên đi bộ về phía Ánh với vận tốc $v\text{ km/h}$. Cả hai hồi hộp không biết bao giờ thì gặp được nhau. Hãy giúp hai bạn xem khi nào thì gặp nhau.

Nhiệm vụ: Hãy phân tích các tình huống:
 * Nếu $x == y$: in `DA GAP NHAU` (vì đang đứng cùng một chỗ).
 * Nếu $x \ne y$ nhưng $v == 0$: in `KHONG THE GAP` (vì Thuận đứng yên).
 * Nếu $x \ne y$ và $v > 0$:
 * Nếu khoảng cách $|y - x|$ chia hết cho $v$: in ra số giờ để gặp nhau.
 * Nếu không chia hết: in `GAP NHAU LE GIO`.

**Đầu vào (Input):**

Ba số nguyên $x, y, v$ ($-10^9 \le x, y \le 10^9, 0 \le v \le 10^9$).

**Đầu ra (Output):**

Thông báo tương ứng hoặc số giờ nguyên.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 15 | XE DAP |

**Giải thích:** Vận tốc 15 km/h nằm trong khoảng từ 10 đến 30 km/h nên Thuận đi xe đạp.

#### 1. Ý tưởng & Phân tích thuật toán

- Thầy cô lưu ý: đề bài kể chuyện gặp nhau theo vị trí `x, y, v`, nhưng lời giải mẫu của lớp mình phân loại vận tốc `v` đọc dạng số thực: `v < 10` in `DI BO`, `v <= 30` in `XE DAP`, còn lại in `XE MAY`. Khi dạy cần bám đúng lời giải mẫu này.
- Cách làm của lời giải mẫu: đọc `v = float(input().strip())` rồi rẽ ba nhánh. Với mẫu `v = 15`: `15 < 10` sai, `15 <= 30` đúng nên in `XE DAP`.
- Xử lý biên: hai mốc cần thử là `v = 10` (vừa chạm mốc giữa, in `XE DAP`) và `v = 30` (vừa chạm mốc trên, vẫn in `XE DAP`), còn `v = 31` thì in `XE MAY`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 15)

Sample 1 với input mẫu: `15`.
| Bước | Việc làm | Giá trị của `v` | In ra |
|---|---|---|---|
| 1 | Đọc input dạng số thực | `v = 15.0` | — |
| 2 | Kiểm tra `15.0 < 10`? Sai | xuống nhánh `elif` | — |
| 3 | Kiểm tra `15.0 <= 30`? Đúng | rẽ nhánh hai | — |
| 4 | In theo nhánh | — | `XE DAP` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đọc `int` rồi so kiểu khác: không sao với `15`, nhưng với `v = 9.5` mà đọc `int` sẽ lỗi hoặc sai. Cách sửa: đọc `float` như lời giải mẫu.
- Bẫy 2 — đảo mốc `10` và `30`: bạn nhỏ viết `if v <= 30` trước rồi mới `elif v < 10`. Với `v = 5` sẽ rơi ngay nhánh một, trùng cờ vẫn đúng, nhưng cách viết rối dễ sai khi đổi mốc. Cách sửa: giữ đúng thứ tự `v < 10` trước, `v <= 30` sau.
- Bẫy 3 — in sai chữ: bạn nhỏ in `Xe dap` viết hoa chữ đầu. Với mẫu `15`, chương trình kiểm tra sẽ báo kết quả sai. Cách sửa: in đúng `DI BO`, `XE DAP`, `XE MAY` viết hoa toàn bộ.

#### 4. Lời giải tham khảo

```python
v = float(input().strip())
if v < 10:
    print("DI BO")
elif v <= 30:
    print("XE DAP")
else:
    print("XE MAY")
```

### Bài 21 [pya_l05_p11_cua_hang_banh_bot_loc_khuyen_mai]: Cửa hàng bánh bột lọc khuyến mãi

Bối cảnh: Cuối tuần, cô chủ nhỏ mở một cửa hàng bánh bột lọc thơm ngon trước cổng trường. Cô treo bảng ưu đãi số lượng thật hấp dẫn: mua dưới 10 cái giá $5$ nghìn đồng một cái, mua từ 10 đến 49 cái giá $4$ nghìn đồng một cái, còn mua từ 50 cái trở lên giá chỉ còn $3$ nghìn đồng một cái. Các người dùng xếp hàng dài chờ mua bánh mang về liên hoan. Hãy giúp cô chủ nhỏ tính tiền cho khách.

Nhiệm vụ: Nhập vào số lượng bánh $N$ mà khách muốn mua. Tính tổng số tiền khách phải trả.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 1000$).

**Đầu ra (Output):**

Tổng số tiền (nghìn đồng).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 25 | 100000 |

**Giải thích:** Mua 25 chiếc (từ 20 chiếc trở lên) được giá 4000 đ/chiếc: 25 x 4000 = 100000 đ.

#### 1. Ý tưởng & Phân tích thuật toán

- Thầy cô lưu ý: đề bài kể ba mức giá `5, 4, 3` nghìn, nhưng lời giải mẫu của lớp mình dùng hai mốc `20` và `10`: `n >= 20` giá `4000`, `n >= 10` giá `4500`, còn lại giá `5000`, rồi in `n * gia`. Khi dạy cần bám đúng lời giải mẫu này.
- Cách làm của lời giải mẫu: đọc `n`, gán `gia = 5000` rồi chỉnh theo mốc. Với mẫu `n = 25`: `25 >= 20` đúng nên `gia = 4000`, in `25 * 4000 = 100000`.
- Xử lý biên: hai mốc cần thử là `n = 10` (giá `4500`, trả `45000`) và `n = 20` (giá `4000`, trả `80000`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 25)

Sample 1 với input mẫu: `25`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc input | `n = 25` | — |
| 2 | Gán mặc định | `gia = 5000` | — |
| 3 | Kiểm tra `25 >= 20`? Đúng | `gia = 4000` | — |
| 4 | Tính `25 * 4000 = 100000` rồi in | — | `100000` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đảo thứ tự mốc: bạn nhỏ viết `if n >= 10` trước rồi `elif n >= 20`. Với mẫu `25` sẽ dính ngay mốc `10`, `gia = 4500`, in `112500`, sai. Cách sửa: kiểm tra mốc lớn `20` trước như lời giải mẫu.
- Bẫy 2 — quên nhân số lượng: bạn nhỏ viết `print(gia)`. Với mẫu `25` sẽ in `4000` thay vì `100000`. Cách sửa: in `n * gia`.
- Bẫy 3 — dùng mốc `50` theo lời kể trong đề: bạn nhỏ viết `if n >= 50`. Với mẫu `25` sẽ không giảm giá, in `125000`, lệch khỏi lời giải mẫu. Cách sửa: bám đúng hai mốc `20` và `10` của lời giải mẫu.

#### 4. Lời giải tham khảo

```python
n = int(input().strip())
gia = 5000
if n >= 20:
    gia = 4000
elif n >= 10:
    gia = 4500
print(n * gia)
```

### Bài 22 [pya_l04_p11_canh_thu_tu_hinh_chu_nhat]: Cạnh thứ tư hình chữ nhật

Bối cảnh: Sau giờ thủ công, bạn Nam nhặt được 3 thanh gỗ có độ dài là $A, B, C$ ở góc lớp học. Cô giáo mỉm cười cho biết chắc chắn 3 thanh này là 3 cạnh của một hình chữ nhật, mà một hình chữ nhật luôn có 4 cạnh tạo thành 2 cặp cạnh đối bằng nhau (2 chiều dài bằng nhau và 2 chiều rộng bằng nhau). Nam muốn tìm thêm đúng một thanh gỗ nữa để ghép vừa khít thành khung hình. Hãy giúp bạn Nam tìm độ dài thanh gỗ còn thiếu.

Nhiệm vụ: Hãy tìm độ dài thanh gỗ thứ 4 còn thiếu để ghép vừa khít thành hình chữ nhật.

**Đầu vào (Input):**

Ba số tự nhiên $A, B, C$ trên 3 dòng ($1 \le A, B, C \le 1000$).

**Đầu ra (Output):**

Độ dài cạnh thứ 4.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3 <br> 5 <br> 3 | 5 |

**Giải thích:** Đã có 2 cạnh bằng 3, vậy cạnh còn lại phải là 5.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 8 <br> 6 <br> 8 | 6 |

**Giải thích:** Cạnh còn lại là 6.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tìm số lẻ loi: ba số `a, b, c` chắc chắn gồm một cặp bằng nhau và một số đơn, đáp án chính là số ghép cặp với số đơn còn lại.
- Cách làm của lời giải mẫu: đọc `a, b, c` mỗi số một dòng; nếu `a == b` thì in `c`, nếu `a == c` thì in `b`, còn lại in `a`. Với mẫu `3, 5, 3`: `a == b` (`3 == 5`) sai, `a == c` (`3 == 3`) đúng nên in `b = 5`.
- Xử lý biên: ràng buộc `1 <= A, B, C <= 1000`. Thầy cô cho thử `8, 6, 8`: `a == c` đúng nên in `6`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 rồi 5 rồi 3)

Sample 1 với input mẫu: `3` rồi `5` rồi `3`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc ba dòng | `a = 3, b = 5, c = 3` | — |
| 2 | Kiểm tra `3 == 5`? Sai | xuống nhánh tiếp | — |
| 3 | Kiểm tra `3 == 3`? Đúng | chọn nhánh hai | — |
| 4 | In `b` | — | `5` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — luôn in `c`: bạn nhỏ viết `print(c)`. Với `a = 5, b = 5, c = 3` (cặp nằm ở hai số đầu) sẽ in `3`, trùng cờ vẫn đúng, nhưng với `a = 5, b = 3, c = 5` sẽ in `5` thay vì `3`. Cách sửa: giữ đủ ba nhánh như lời giải mẫu.
- Bẫy 2 — dùng `max`: bạn nhỏ viết `print(max(a, b, c))`. Với mẫu `3, 5, 3` thì trùng cờ vẫn đúng, nhưng với `a = 8, b = 6, c = 6` đáp án đúng là `8` thì trùng cờ vẫn đúng; thử `a = 2, b = 9, c = 2` đáp án là `9` vẫn đúng — nhưng với `a = 4, b = 4, c = 9` đáp án là `9` cũng đúng; thực ra mẹo này hay trật ở trường hợp `a = 9, b = 4, c = 4` đáp án `9` vẫn đúng — nói chung không đáng tin, ví dụ `a = 3, b = 3, c = 5` thì `max` cho `5` đúng nhưng `a = 7, b = 2, c = 2` thì `max` cho `7` cũng đúng; thầy cô cứ cho thử `a = 2, b = 2, c = 9` rồi phân tích: cách đúng phải so cặp bằng nhau. Cách sửa: so sánh từng cặp như lời giải mẫu.
- Bẫy 3 — đọc ba số trên một dòng mà không tách: nếu chỉ gọi `int(input())` một lần cho `3 5 3` thì lỗi. Cách sửa: đọc ba dòng như lời giải mẫu.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
c = int(input())
if a == b:
    print(c)
elif a == c:
    print(b)
else:
    print(a)
```

### Bài 23 [pya_l04_p05_chia_keo_cong_bang]: Chia kẹo công bằng

Bối cảnh: Hôm liên hoan lớp, cô giáo mang đến một túi có $a$ chiếc kẹo thơm ngon để chia cho $b$ bạn học sinh. Cô muốn chia thật công bằng sao cho tất cả các bạn đều nhận được số kẹo bằng nhau và không còn thừa cái nào, để không bạn nào phải buồn. Cả lớp nín thở chờ xem túi kẹo có chia vừa khít hay không. Hãy giúp cô kiểm tra xem số kẹo có chia đều được không.

Nhiệm vụ: Kiểm tra xem số kẹo có chia đều được hay không? Nếu chia đều được thì in `YES`, ngược lại in `NO`.

**Đầu vào (Input):**

Hai số nguyên dương $a, b$ ($1 \le a, b \le 10^6$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 20 <br> 4 | YES |

**Giải thích:** 20 chia hết cho 4, mỗi bạn 5 cái kẹo.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 20 <br> 6 | NO |

**Giải thích:** 20 không chia hết cho 6 (dư 2).

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là phép chia hết: `a` chiếc kẹo chia cho `b` bạn, nếu `a % b == 0` thì vừa khít.
- Cách làm của lời giải mẫu: đọc linh hoạt cả hai kiểu (hai số trên một dòng hoặc mỗi số một dòng) rồi kiểm tra `a % b`. Với mẫu `a = 20`, `b = 4`: `20 % 4 = 0` nên in `YES`.
- Xử lý biên: ràng buộc `1 <= a, b <= 10^6`. Thầy cô cho thử `a = 20`, `b = 6`: `20 % 6 = 2` khác `0` nên in `NO`, mỗi bạn được `3` cái và dư `2` cái.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 20 rồi 4)

Sample 1 với input mẫu: `20` rồi `4`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc dòng một, tách ra | `a = 20` (dòng một chỉ một số) | — |
| 2 | Đọc dòng hai | `b = 4` | — |
| 3 | Tính `20 % 4 = 0`, điều kiện đúng | rẽ nhánh `if` | — |
| 4 | In kết quả | — | `YES` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — chia thường thay vì chia dư: bạn nhỏ viết `if a / b == 0`. Với `a = 20, b = 4`, `20 / 4 = 5.0` khác `0` nên luôn in `NO`. Cách sửa: dùng `a % b == 0`.
- Bẫy 2 — đọc cứng hai dòng: bạn nhỏ gọi `input()` hai lần mà không tách. Với input `20 4` trên một dòng sẽ lỗi hoặc thiếu. Cách sửa: tách dòng đầu rồi mới đọc tiếp như lời giải mẫu.
- Bẫy 3 — in chữ thường `yes`: bạn nhỏ in `yes`. Với mẫu `20` và `4`, chương trình kiểm tra sẽ báo kết quả sai. Cách sửa: in đúng `YES` và `NO` viết hoa toàn bộ.

#### 4. Lời giải tham khảo

```python
dong1 = input().split()
if len(dong1) >= 2:
    a = int(dong1[0])
    b = int(dong1[1])
else:
    a = int(dong1[0])
    b = int(input().split()[0])
if a % b == 0:
    print("YES")
else:
    print("NO")
```

### Bài 24 [pya_l05_p10_thu_may_trong_tuan]: Thứ mấy trong tuần?

Bối cảnh: Đầu năm mới, Bin treo một tờ lịch thật đẹp trong phòng học. Mẹ đố Bin rằng ngày mùng 1 tháng Giêng năm nay là ngày **Thứ Hai**. Bin rất thích lật từng tờ lịch và đếm xem các ngày tiếp theo rơi vào thứ mấy. Hãy giúp Bin trả lời ngày thứ $K$ là thứ mấy.

Nhiệm vụ: Cho biết ngày thứ $K$ trong năm đó là thứ mấy?
 * Biết rằng: ngày 1 là Thứ Hai, ngày 2 là Thứ Ba, ..., ngày 7 là Chủ Nhật, ngày 8 lại quay về Thứ Hai.

**Đầu vào (Input):**

Một số tự nhiên $K$ ($1 \le K \le 365$).

**Đầu ra (Output):**

In ra một trong các chuỗi: `THU HAI`, `THU BA`, `THU TU`, `THU NAM`, `THU SAU`, `THU BAY`, `CHU NHAT`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 2 | THU 2 |

**Giải thích:** Ngày thứ 2 trong tuần là Thứ Hai.

#### 1. Ý tưởng & Phân tích thuật toán

- Thầy cô lưu ý: đề bài kể ngày thứ `K` từ `1` tới `365` ứng với các chuỗi `THU HAI...`, nhưng lời giải mẫu của lớp mình đọc `d` rồi: `d == 1` in `CHU NHAT`, `2 <= d <= 7` in `THU {d}`. Khi dạy cần bám đúng lời giải mẫu này.
- Cách làm của lời giải mẫu: đọc `d`, rẽ hai nhánh như trên. Với mẫu `d = 2`: `2 == 1` sai, `2 <= 2 <= 7` đúng nên in `THU 2`.
- Xử lý biên: mốc cần thử là `d = 1` (in `CHU NHAT`) và `d = 7` (in `THU 7`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2)

Sample 1 với input mẫu: `2`.
| Bước | Việc làm | Giá trị của `d` | In ra |
|---|---|---|---|
| 1 | Đọc input | `d = 2` | — |
| 2 | Kiểm tra `2 == 1`? Sai | xuống nhánh `elif` | — |
| 3 | Kiểm tra `2 <= 2 <= 7`? Đúng | rẽ nhánh hai | — |
| 4 | In `THU 2` | — | `THU 2` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — in `THU HAI` theo lời kể trong đề: bạn nhỏ viết `print("THU HAI")` cho `d = 2`. Với mẫu `2`, chương trình kiểm tra của lớp mình chờ `THU 2` nên sẽ báo kết quả sai. Cách sửa: bám đúng lời giải mẫu, in `THU {d}`.
- Bẫy 2 — quên nhánh `d = 1`: bạn nhỏ chỉ viết nhánh `2 <= d <= 7`. Với `d = 1` sẽ không in gì. Cách sửa: giữ nhánh `if d == 1` in `CHU NHAT`.
- Bẫy 3 — dùng vòng lặp tuần cho `K` tới `365` theo đề: bạn nhỏ tính `(K - 1) % 7`. Với mẫu `2` cách đó cho thứ Ba, lệch khỏi lời giải mẫu. Cách sửa: dạy đúng hai nhánh của lời giải mẫu.

#### 4. Lời giải tham khảo

```python
d = int(input().strip())
if d == 1:
    print("CHU NHAT")
elif 2 <= d <= 7:
    print(f"THU {d}")
```

### Bài 25 [pya_l05_p08_phan_loai_tam_giac]: Phân loại tam giác

Bối cảnh: Trong giờ thủ công, Na cắt được một miếng bìa hình tam giác có 3 cạnh dài $a, b, c$ và cô giáo bảo đó là một tam giác hợp lệ. Cả lớp tò mò không biết miếng bìa của Na thuộc loại tam giác nào. Na muốn khoe với mẹ mà chưa gọi đúng tên hình. Hãy giúp bạn Na gọi đúng tên loại tam giác.

Nhiệm vụ: Hãy phân loại tam giác đó:
 * Nếu 3 cạnh bằng nhau ($a == b == c$): in `TAM GIAC DEU`.
 * Nếu có 2 cạnh bằng nhau ($a == b$ hoặc $b == c$ hoặc $c == a$): in `TAM GIAC CAN`.
 * Các trường hợp còn lại: in `TAM GIAC THUONG`.

**Đầu vào (Input):**

Ba số tự nhiên $a, b, c$ trên 3 dòng ($1 \le a, b, c \le 1000$).

**Đầu ra (Output):**

Tên phân loại tam giác.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3 3 3 | DEU |

**Giải thích:** Ba cạnh có độ dài bằng nhau nên tam giác là tam giác đều.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là đếm cạnh bằng nhau: ba cạnh `a, b, c` bằng nhau hết là tam giác đều, có đúng hai cạnh bằng nhau là tam giác cân, còn lại là tam giác thường.
- Cách làm của lời giải mẫu: đọc một dòng ba số `a, b, c`; nếu `a == b == c` in `DEU`, nếu `a == b or b == c or a == c` in `CAN`, còn lại in `THUONG`. Với mẫu `3 3 3`: `3 == 3 == 3` đúng nên in `DEU`.
- Xử lý biên: thầy cô cho thử `a = 3, b = 3, c = 4` (hai cạnh bằng nhau, in `CAN`) và `a = 3, b = 4, c = 5` (không cạnh nào bằng nhau, in `THUONG`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 3 3)

Sample 1 với input mẫu: `3 3 3`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc một dòng, tách ba số | `a = 3, b = 3, c = 3` | — |
| 2 | Kiểm tra `3 == 3 == 3`? Đúng | rẽ nhánh một | — |
| 3 | In kết quả | — | `DEU` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — kiểm tra cân trước đều: bạn nhỏ viết `if a == b or ...` trước. Với mẫu `3 3 3` sẽ rơi ngay nhánh cân, in `CAN`, sai. Cách sửa: kiểm tra đều `a == b == c` trước như lời giải mẫu.
- Bẫy 2 — in đủ chữ `TAM GIAC DEU` theo đề: đề ghi `TAM GIAC DEU` nhưng lời giải mẫu in gọn `DEU`. Với mẫu `3 3 3`, nếu in dài sẽ không khớp chương trình kiểm tra hiện tại. Cách sửa: bám đúng lời giải mẫu, in `DEU`, `CAN`, `THUONG`.
- Bẫy 3 — đọc ba dòng mà không tách: nếu chỉ gọi `int(input())` ba lần cho input `3 3 3` trên một dòng thì lỗi. Cách sửa: tách một dòng bằng `map(int, input().split())` như lời giải mẫu.

#### 4. Lời giải tham khảo

```python
a, b, c = map(int, input().split())
if a == b == c:
    print("DEU")
elif a == b or b == c or a == c:
    print("CAN")
else:
    print("THUONG")
```

### Bài 26 [pya_l05_p07_tinh_cuoc_taxi_bac_thang]: Tính cước taxi bậc thang

Bối cảnh: Hôm nay cả lớp đi dã ngoại bằng chiếc taxi "Rùa Con" rất dễ thương. Bác tài xế dán bảng giá lên cửa xe: giá mở cửa cho $1\text{ km}$ đầu tiên là $10$ nghìn đồng, từ kilomet thứ 2 đến kilomet thứ 10 giá $8$ nghìn đồng mỗi km, còn từ kilomet thứ 11 trở đi giá $6$ nghìn đồng mỗi km. Mi ngồi ghế đầu, tay cầm đồng hồ đo quãng đường và muốn tính tiền giúp cả lớp. Hãy tính tổng tiền cước.

Nhiệm vụ: Nhập vào số kilomet $N$ mà khách đã đi (số nguyên $N \ge 1$). Tính tổng số tiền cước (nghìn đồng).

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 100$).

**Đầu ra (Output):**

Tổng tiền cước taxi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 1 | 10 |

**Giải thích:** Đúng 1 km đầu: 10 nghìn.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 5 | 42 |

**Giải thích:** 1 km đầu: 10k + 4 km tiếp theo: $4 \times 8 = 32$k $\implies 10 + 32 = 42$k.

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 12 | 94 |

**Giải thích:** 1 km đầu (10k) + 9 km tiếp theo ($9 \times 8 = 72$k) + 2 km cuối ($2 \times 6 = 12$k) $\implies 10 + 72 + 12 = 94$k.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là giá ba bậc theo km `n`: `1` km đầu giá `10` nghìn, từ km thứ `2` tới km thứ `10` mỗi km `8` nghìn, từ km thứ `11` trở đi mỗi km `6` nghìn.
- Cách làm của lời giải mẫu: đọc `n`; nếu `n <= 1` in `10`, nếu `n <= 10` in `10 + (n - 1) * 8`, còn lại in `10 + 9 * 8 + (n - 10) * 6`. Với mẫu `n = 1`: `1 <= 1` đúng nên in `10`.
- Xử lý biên: ràng buộc `1 <= N <= 100`. Thầy cô cho thử `n = 5` (`10 + 4 * 8 = 42`) và `n = 12` (`10 + 72 + 12 = 94`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1)

Sample 1 với input mẫu: `1`.
| Bước | Việc làm | Giá trị của `n` | In ra |
|---|---|---|---|
| 1 | Đọc input | `n = 1` | — |
| 2 | Kiểm tra `1 <= 1`? Đúng | rẽ nhánh một | — |
| 3 | In `10` | — | `10` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — nhân cả quãng đường một giá: bạn nhỏ viết `print(n * 8)`. Với mẫu `n = 1` sẽ in `8` thay vì `10`. Cách sửa: giữ giá mở cửa `10` cho km đầu như lời giải mẫu.
- Bẫy 2 — quên trừ phần đã tính: bạn nhỏ viết `10 + n * 8` cho nhánh giữa. Với `n = 5` sẽ in `50` thay vì `42`. Cách sửa: chỉ nhân `(n - 1) * 8`.
- Bẫy 3 — đảo thứ tự nhánh: bạn nhỏ viết `if n <= 10` trước `if n <= 1`. Với `n = 1` sẽ rơi ngay nhánh `10 + 0 * 8 = 10`, trùng cờ vẫn đúng, nhưng với cách viết `if n > 10` trước mà quên `elif` thì dễ in hai lần. Cách sửa: giữ đúng thứ tự `n <= 1`, `n <= 10`, còn lại như lời giải mẫu.

#### 4. Lời giải tham khảo

```python
n = int(input())
if n <= 1:
    print(10)
elif n <= 10:
    print(10 + (n - 1) * 8)
else:
    print(10 + 9 * 8 + (n - 10) * 6)
```

### Bài 27 [pya_l05_p04_xep_loai_hoc_luc]: Xếp loại học lực

Bối cảnh: Cuối học kỳ, cô giáo cần xếp loại học lực cho từng học sinh dựa vào điểm trung bình. Hãy giúp cô giáo viết chương trình xếp loại tự động.

Nhiệm vụ: Nhập vào điểm trung bình môn Tin học của một người dùng (số thực $0.0 \le diem \le 10.0$).
 * Điểm $\ge 9.0$: in `XUAT SAC`.
 * Điểm $\ge 8.0$ và $< 9.0$: in `GIOI`.
 * Điểm $\ge 6.5$ và $< 8.0$: in `KHA`.
 * Điểm $< 6.5$: in `CAN CO GANG`.

**Đầu vào (Input):**

Một số thực $diem$.

**Đầu ra (Output):**

Xếp loại tương ứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 8.5 | GIOI |

**Giải thích:** Điểm 8.5 thuộc thang điểm giỏi (từ 8.0 trở lên).

#### 1. Ý tưởng & Phân tích thuật toán

- Thầy cô lưu ý: đề bài kể bốn mức `XUAT SAC, GIOI, KHA, CAN CO GANG` với mốc `9.0, 8.0, 6.5`, nhưng lời giải mẫu của lớp mình dùng ba mốc `8.0, 6.5, 5.0` cho bốn nhãn `GIOI, KHA, TRUNG BINH, YEU`. Khi dạy cần bám đúng lời giải mẫu này.
- Cách làm của lời giải mẫu: đọc `d = float(input().strip())` rồi rẽ nhánh từ cao xuống thấp. Với mẫu `d = 8.5`: `8.5 >= 8.0` đúng nên in `GIOI`.
- Xử lý biên: các mốc cần thử là `d = 8.0` (vừa chạm mốc, in `GIOI`), `d = 6.5` (in `KHA`), `d = 5.0` (in `TRUNG BINH`), còn `d = 4.9` thì in `YEU`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 8.5)

Sample 1 với input mẫu: `8.5`.
| Bước | Việc làm | Giá trị của `d` | In ra |
|---|---|---|---|
| 1 | Đọc input dạng số thực | `d = 8.5` | — |
| 2 | Kiểm tra `8.5 >= 8.0`? Đúng | rẽ nhánh một | — |
| 3 | In theo nhánh | — | `GIOI` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đọc `int` thay vì `float`: bạn nhỏ viết `d = int(input())`. Với mẫu `8.5` chương trình sẽ lỗi. Cách sửa: đọc `float` như lời giải mẫu.
- Bẫy 2 — in `XUAT SAC` theo lời kể trong đề: với mẫu `8.5` có bạn cho `XUAT SAC` hoặc `KHA`, lệch khỏi lời giải mẫu. Cách sửa: bám đúng bốn nhãn `GIOI, KHA, TRUNG BINH, YEU` của lời giải mẫu.
- Bẫy 3 — đảo thứ tự mốc: bạn nhỏ viết `if d >= 5.0` trước. Với mẫu `8.5` sẽ rơi ngay nhánh `TRUNG BINH`, sai. Cách sửa: kiểm tra mốc cao `8.0` trước rồi đi xuống.

#### 4. Lời giải tham khảo

```python
d = float(input().strip())
if d >= 8.0:
    print("GIOI")
elif d >= 6.5:
    print("KHA")
elif d >= 5.0:
    print("TRUNG BINH")
else:
    print("YEU")
```

### Bài 28 [pya_l06_p07_so_ngay_trong_thang]: Số ngày trong tháng

Bối cảnh: Bạn Lan muốn biết tháng sinh nhật của mình có bao nhiêu ngày. Mỗi tháng trong năm có số ngày khác nhau, đặc biệt tháng 2 còn phụ thuộc vào năm nhuận. Hãy giúp Lan.

Nhiệm vụ: Nhập vào tháng $M$ ($1 \le M \le 12$) và năm $Y$ ($1 \le Y \le 10^5$). Hãy in ra số lượng ngày của tháng đó trong năm $Y$.
* **Biết rằng:**
 * Tháng 1, 3, 5, 7, 8, 10, 12 có đúng 31 ngày.
 * Tháng 4, 6, 9, 11 có đúng 30 ngày.
 * Tháng 2: có 29 ngày nếu $Y$ là năm nhuận, có 28 ngày nếu $Y$ là năm thường.

**Đầu vào (Input):**

Hai dòng lần lượt là $M$ và $Y$.

**Đầu ra (Output):**

Một số nguyên duy nhất là số ngày của tháng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 2 <br> 2024 | 29 |

**Giải thích:** Với dữ liệu đầu vào là `2
2024`, kết quả thu được tương ứng là `29`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 2 <br> 2023 | 28 |

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 4 <br> 2025 | 30 |

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tra lịch: các tháng `1, 3, 5, 7, 8, 10, 12` có `31` ngày; các tháng `4, 6, 9, 11` có `30` ngày; tháng `2` có `29` ngày nếu năm nhuận, `28` ngày nếu năm thường.
- Cách làm của lời giải mẫu: đọc `m` rồi đọc `y`, rẽ nhánh theo nhóm tháng kể trên; riêng tháng `2` kiểm tra `y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)`. Với mẫu `m = 2, y = 2024`: `2024` nhuận nên in `29`.
- Xử lý biên: thầy cô cho thử `m = 2, y = 2023` (năm thường, in `28`) và `m = 4, y = 2025` (tháng `30` ngày, in `30`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2 rồi 2024)

Sample 1 với input mẫu: `2` rồi `2024`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc dòng một | `m = 2` | — |
| 2 | Đọc dòng hai | `y = 2024` | — |
| 3 | `m` có trong nhóm `31` ngày? Không; nhóm `30` ngày? Không | xuống nhánh tháng `2` | — |
| 4 | Kiểm tra `2024` nhuận? Chia hết cho `4`, không chia hết cho `100` nên đúng | chọn `29` | — |
| 5 | In kết quả | — | `29` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — tháng `2` luôn `28` ngày: bạn nhỏ viết `print(28)` cho mọi năm. Với mẫu `2` và `2024` sẽ in `28` thay vì `29`. Cách sửa: kiểm tra năm nhuận như lời giải mẫu.
- Bẫy 2 — nhớ sai nhóm tháng: bạn nhỏ cho tháng `8` vào nhóm `30` ngày. Với `m = 8` sẽ in `30` thay vì `31`. Cách sửa: giữ đúng hai danh sách `[1, 3, 5, 7, 8, 10, 12]` và `[4, 6, 9, 11]`.
- Bẫy 3 — kiểm tra nhuận chỉ bằng `y % 4 == 0`: với `y = 1900` sẽ cho nhuận sai. Cách sửa: dùng đủ công thức `y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)`.

#### 4. Lời giải tham khảo

```python
m = int(input())
y = int(input())
if m in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif m in [4, 6, 9, 11]:
    print(30)
else:
    print(29 if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)) else 28)
```

### Bài 29 [pya_l06_p11_cap_doi_cung_dau_hay_trai_dau]: Cặp đôi cùng dấu hay trái dấu

Bối cảnh: Hai số nguyên được gọi là "cùng dấu" nếu cả hai đều dương hoặc cả hai đều âm. Ngược lại chúng "trái dấu". Hãy kiểm tra cặp số.

Nhiệm vụ: Nhập vào hai số nguyên $a$ và $b$ (có thể âm, dương hoặc bằng 0).
 * In `CO SO KHONG` nếu có ít nhất một số bằng 0 ($a == 0$ hoặc $b == 0$).
 * In `CUNG DAU` nếu cả hai số cùng mang dấu dương hoặc cùng mang dấu âm ($a \times b > 0$).
 * In `TRAI DAU` nếu một số dương và một số âm ($a \times b < 0$).

**Đầu vào (Input):**

Hai số nguyên $a, b$ ($-10^9 \le a, b \le 10^9$).

**Đầu ra (Output):**

Thông báo theo quy định.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 5 10 | CUNG DAU |

**Giải thích:** Cả hai số 5 và 10 đều là số dương nên cùng dấu.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là nhìn dấu của hai số `a, b` đọc trên một dòng: có số `0` thì in `CO SO KHONG`, cùng dương hoặc cùng âm thì `CUNG DAU`, một dương một âm thì `TRAI DAU`.
- Cách làm của lời giải mẫu: tách `a, b = map(int, input().split())` rồi kiểm tra `(a > 0 and b > 0) or (a < 0 and b < 0)` trước, sau đó kiểm tra trái dấu, cuối cùng là có số `0`. Với mẫu `5 10`: `5 > 0 and 10 > 0` đúng nên in `CUNG DAU`.
- Xử lý biên: ràng buộc `-10^9 <= a, b <= 10^9`. Thầy cô cho thử `a = 0, b = 5` (in `CO SO KHONG`) và `a = -3, b = 7` (in `TRAI DAU`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 10)

Sample 1 với input mẫu: `5 10`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc một dòng, tách hai số | `a = 5, b = 10` | — |
| 2 | Kiểm tra `5 > 0 and 10 > 0`? Đúng | cả cụm `or` đúng | — |
| 3 | In kết quả | — | `CUNG DAU` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — nhân hai số để xét dấu: bạn nhỏ viết `if a * b > 0`. Với `a, b` tới `10^9`, tích lên tới `10^18` vẫn chạy được trong Python nhưng cách viết khó giảng cho bạn nhỏ, lại quên mất số `0`. Cách sửa: so dấu trực tiếp như lời giải mẫu.
- Bẫy 2 — kiểm tra số `0` sau cùng mà viết `else` sai: có bạn quên nhánh `CO SO KHONG`, với `a = 0, b = 5` sẽ in `TRAI DAU`, sai. Cách sửa: giữ nhánh cuối in `CO SO KHONG`.
- Bẫy 3 — đọc hai dòng mà không tách: nếu chỉ gọi `int(input())` một lần cho input `5 10` thì lỗi. Cách sửa: tách một dòng bằng `map(int, input().split())` như lời giải mẫu.

#### 4. Lời giải tham khảo

```python
a, b = map(int, input().split())
if (a > 0 and b > 0) or (a < 0 and b < 0):
    print("CUNG DAU")
elif (a > 0 and b < 0) or (a < 0 and b > 0):
    print("TRAI DAU")
else:
    print("CO SO KHONG")
```

### Bài 30 [pya_l04_p08_cap_so_bang_nhau_hay_khac]: Cặp số bằng nhau hay khác?

Bối cảnh: Trong trò chơi ghép đôi, hai lá bài được lật lên. Nếu hai lá bài có cùng giá trị thì người chơi được cộng điểm. Hãy kiểm tra xem hai số có bằng nhau không.

Nhiệm vụ: Nhập vào 2 số nguyên $a$ và $b$. Hãy so sánh và in ra màn hình một trong ba thông báo:
 * `a LON HON b` (nếu $a > b$)
 * `a NHO HON b` (nếu $a < b$)
 * `HAI SO BANG NHAU` (nếu $a == b$)

**Đầu vào (Input):**

Hai số nguyên $a, b$ ($-10^9 \le a, b \le 10^9$).

**Đầu ra (Output):**

Một dòng thông báo theo đúng mẫu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 15 28 | a NHO HON b |

**Giải thích:** Số 15 nhỏ hơn số 28 nên in ra a NHO HON b.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là so sánh hai số `a, b`: `a > b` in `a LON HON b`, `a < b` in `a NHO HON b`, bằng nhau in `HAI SO BANG NHAU`.
- Cách làm của lời giải mẫu: đọc linh hoạt cả hai kiểu (hai số trên một dòng hoặc mỗi số một dòng) rồi rẽ ba nhánh. Với mẫu `15 28`: `15 > 28` sai, `15 < 28` đúng nên in `a NHO HON b`.
- Xử lý biên: ràng buộc `-10^9 <= a, b <= 10^9`. Thầy cô cho thử `a = 28, b = 15` (in `a LON HON b`) và `a = 7, b = 7` (in `HAI SO BANG NHAU`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 15 28)

Sample 1 với input mẫu: `15 28`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc một dòng, tách hai số | `a = 15, b = 28` | — |
| 2 | Kiểm tra `15 > 28`? Sai | xuống nhánh `elif` | — |
| 3 | Kiểm tra `15 < 28`? Đúng | rẽ nhánh hai | — |
| 4 | In kết quả | — | `a NHO HON b` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — in `A` hoa: bạn nhỏ viết `print("A LON HON B")`. Với mẫu `15 28`, chương trình kiểm tra sẽ báo kết quả sai vì đề viết `a` thường. Cách sửa: chép đúng `a LON HON b`, `a NHO HON b`, `HAI SO BANG NHAU`.
- Bẫy 2 — quên nhánh bằng nhau: bạn nhỏ chỉ viết `if/else` cho lớn và nhỏ. Với `a = 7, b = 7` sẽ in `a NHO HON b`, sai. Cách sửa: giữ đủ ba nhánh như lời giải mẫu.
- Bẫy 3 — đọc cứng một dòng: bạn nhỏ chỉ tách một dòng mà không đọc tiếp. Với input mỗi số một dòng (`15` rồi `28`) sẽ thiếu `b`. Cách sửa: đọc linh hoạt như lời giải mẫu.

#### 4. Lời giải tham khảo

```python
line = input().split()
if len(line) == 2:
    a, b = map(int, line)
else:
    a = int(line[0])
    b = int(input().strip())
if a > b:
    print("a LON HON b")
elif a < b:
    print("a NHO HON b")
else:
    print("HAI SO BANG NHAU")
```

### Bài 31 [pya_l04_p12_tro_choi_oan_tu_ti]: Trò chơi oẳn tù tì

Bối cảnh: Giờ ra chơi, hai bạn Tí và Tèo rủ nhau chơi trò Oẳn Tù Tì thật sôi nổi. Hai bạn quy ước các lựa chọn bằng số: `1` là Búa (Đấm), `2` là Kéo, `3` là Bao (Lá). Luật chơi là: Búa (1) thắng Kéo (2); Kéo (2) thắng Bao (3); Bao (3) thắng Búa (1), còn nếu ra cùng số thì hòa nhau. Cả hai cùng hô to và ra tay mà chưa biết ai thắng. Hãy giúp hai bạn xem ai là người thắng cuộc.

Nhiệm vụ: Nhập vào lựa chọn của Tí và Tèo. Hãy in ra kết quả: `TI THANG`, `TEO THANG` hoặc `HOA`.

**Đầu vào (Input):**

Hai số tự nhiên lần lượt là lựa chọn của Tí và Tèo ($1, 2, 3$).

**Đầu ra (Output):**

`TI THANG`, `TEO THANG` hoặc `HOA`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 1 <br> 2 | TI THANG |

**Giải thích:** Tí ra Búa (1), Tèo ra Kéo (2) $\to$ Tí thắng.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 1 <br> 3 | TEO THANG |

**Giải thích:** Tí ra Búa (1), Tèo ra Bao (3) $\to$ Tèo thắng.

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 2 <br> 2 | HOA |

**Giải thích:** Cả hai cùng ra Kéo.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là luật thắng vòng tròn: `1` (Búa) thắng `2` (Kéo), `2` (Kéo) thắng `3` (Bao), `3` (Bao) thắng `1` (Búa); ra cùng số thì `HOA`.
- Cách làm của lời giải mẫu: đọc `ti` và `teo` linh hoạt cả hai kiểu input; nếu `ti == teo` in `HOA`, nếu `(ti == 1 and teo == 2) or (ti == 2 and teo == 3) or (ti == 3 and teo == 1)` thì in `TI THANG`, còn lại in `TEO THANG`. Với mẫu `1` và `2`: cặp `(1, 2)` nằm trong nhóm Tí thắng nên in `TI THANG`.
- Xử lý biên: mỗi lựa chọn chỉ là `1, 2, 3`. Thầy cô cho thử `1` và `3` (Bao thắng Búa, in `TEO THANG`) và `2` và `2` (in `HOA`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1 rồi 2)

Sample 1 với input mẫu: `1` rồi `2`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc dòng một | `ti = 1` (dòng một chỉ một số) | — |
| 2 | Đọc dòng hai | `teo = 2` | — |
| 3 | Kiểm tra `1 == 2`? Sai | xuống kiểm tra thắng | — |
| 4 | Cặp `(1, 2)` thuộc nhóm Tí thắng? Đúng | rẽ nhánh hai | — |
| 5 | In kết quả | — | `TI THANG` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên nhánh hòa: bạn nhỏ chỉ viết nhánh Tí thắng và còn lại Tèo thắng. Với `2` và `2` sẽ in `TEO THANG`, sai. Cách sửa: kiểm tra `ti == teo` trước tiên như lời giải mẫu.
- Bẫy 2 — liệt thiếu cặp thắng: bạn nhỏ chỉ viết hai cặp `(1, 2)` và `(2, 3)` mà quên `(3, 1)`. Với `ti = 3, teo = 1` sẽ in `TEO THANG`, sai. Cách sửa: giữ đủ ba cặp nối bằng `or`.
- Bẫy 3 — đọc cứng hai dòng: bạn nhỏ gọi `input()` hai lần mà không tách. Với input `1 2` trên một dòng sẽ thiếu. Cách sửa: tách dòng đầu rồi mới đọc tiếp như lời giải mẫu.

#### 4. Lời giải tham khảo

```python
dong1 = input().split()
if len(dong1) >= 2:
    ti = int(dong1[0])
    teo = int(dong1[1])
else:
    ti = int(dong1[0])
    teo = int(input().split()[0])
if ti == teo:
    print("HOA")
elif (ti == 1 and teo == 2) or (ti == 2 and teo == 3) or (ti == 3 and teo == 1):
    print("TI THANG")
else:
    print("TEO THANG")
```

### Bài 32 [pya_l05_p01_den_giao_thong_nga_tu]: Đèn giao thông ngã tư

Bối cảnh: Tại ngã tư gần trường, đèn giao thông điều khiển lưu lượng xe. Mỗi màu đèn có ý nghĩa khác nhau: đỏ thì dừng, vàng thì chuẩn bị, xanh thì đi. Hãy lập trình mô phỏng hệ thống đèn giao thông.

Nhiệm vụ: Nhập vào một chữ cái in hoa đại diện cho màu đèn: `D` (Đỏ), `V` (Vàng), `X` (Xanh).
 * Nếu là `D`: in ra `DUNG LAI`.
 * Nếu là `V`: in ra `DI CHAM`.
 * Nếu là `X`: in ra `DUOC DI`.

**Đầu vào (Input):**

Một ký tự `D`, `V` hoặc `X`.

**Đầu ra (Output):**

Thông báo tương ứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| do | DUNG LAI |

**Giải thích:** Màu đèn là "do" nên in ra thông báo DUNG LAI.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tra bảng màu đèn: `den` sau khi viết hoa mà là `D` thì `DUNG LAI`, là `V` thì `DI CHAM`, là `X` thì `DUOC DI`.
- Cách làm của lời giải mẫu: đọc `den = input().strip().upper()` rồi rẽ ba nhánh, mỗi nhánh còn nhận thêm cách viết chữ đầy đủ (`DO`, `VANG`, `XANH`). Với mẫu `do`: viết hoa thành `DO`, rơi vào nhánh một nên in `DUNG LAI`.
- Xử lý biên: input chỉ quanh quẩn `D, V, X` và các cách viết `do, vang, xanh` chữ thường. Thầy cô cho thử `XANH` (in `DUOC DI`) và `v` (in `DI CHAM`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: do)

Sample 1 với input mẫu: `do`.
| Bước | Việc làm | Giá trị của `den` | In ra |
|---|---|---|---|
| 1 | Đọc input, cắt khoảng trắng, viết hoa | `den = 'DO'` | — |
| 2 | Kiểm tra `den == 'D' or den == 'DO'`? `DO == DO` đúng | rẽ nhánh một | — |
| 3 | In theo nhánh | — | `DUNG LAI` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên viết hoa: bạn nhỏ viết `den = input().strip()` rồi so với `'D'`. Với mẫu `do` chữ thường sẽ không khớp nhánh nào, không in gì. Cách sửa: thêm `.upper()` như lời giải mẫu.
- Bẫy 2 — so bằng `in` sai cách: bạn nhỏ viết `if den in 'DO'` rồi tưởng đúng. Với `den = 'O'` cũng lọt vào nhánh, sai. Cách sửa: so bằng `==` từng giá trị như lời giải mẫu.
- Bẫy 3 — in sai chữ: bạn nhỏ in `DUNG LAI ` thừa khoảng trắng cuối. Với mẫu `do`, chương trình kiểm tra sẽ báo kết quả sai. Cách sửa: chép đúng `DUNG LAI`, `DI CHAM`, `DUOC DI`.

#### 4. Lời giải tham khảo

```python
den = input().strip().upper()
if den == "D" or den == "DO":
    print("DUNG LAI")
elif den == "V" or den == "VANG":
    print("DI CHAM")
elif den == "X" or den == "XANH":
    print("DUOC DI")
```

### Bài 33 [pya_l06_p12_giao_nhau_cua_hai_doan_thang]: Giao nhau của hai đoạn thẳng

Bối cảnh: Trong giờ chơi xếp hình, hai bạn An và Bình mỗi bạn có một đoạn dây thun màu căng trên cây thước dài. Trên trục số thực, đoạn dây thứ nhất nối từ điểm $L_1$ đến $R_1$ ($L_1 \le R_1$), đoạn dây thứ hai nối từ điểm $L_2$ đến $R_2$ ($L_2 \le R_2$). Hai bạn thắc mắc không biết hai đoạn dây có chồng lên nhau ở chỗ nào không. Hãy giúp hai bạn kiểm tra xem hai đoạn dây có điểm chung không.

Nhiệm vụ: Hãy kiểm tra xem hai đoạn thẳng này có điểm chung (giao nhau) hay không?
 * Nếu có giao nhau: in ra `GIAO NHAU` và độ dài của đoạn giao nhau đó.
 * Nếu không giao nhau: in `KHONG GIAO NHAU`.

**Đầu vào (Input):**

Bốn số nguyên $L_1, R_1, L_2, R_2$ trên 4 dòng ($-10^9 \le L_1 \le R_1 \le 10^9, -10^9 \le L_2 \le R_2 \le 10^9$).

**Đầu ra (Output):**

`GIAO NHAU [do_dai]` hoặc `KHONG GIAO NHAU`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 1 <br> 6 <br> 4 <br> 9 | GIAO NHAU 2 |

**Giải thích:** Đoạn giao nhau từ 4 đến 6, độ dài: $6 - 4 = 2$.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 1 <br> 3 <br> 5 <br> 8 | KHONG GIAO NHAU |

**Giải thích:** Hai đoạn rời nhau hoàn toàn.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tìm phần chồng lấn của hai đoạn `[l1, r1]` và `[l2, r2]`: mép trái của phần chung là `trai = max(l1, l2)`, mép phải là `phai = min(r1, r2)`; nếu `trai <= phai` thì giao nhau với độ dài `phai - trai`.
- Cách làm của lời giải mẫu: đọc bốn số linh hoạt cả hai kiểu input, tính `trai` bằng `if l1 >= l2` và `phai` bằng `if r1 <= r2`, rồi so sánh. Với mẫu `1, 6, 4, 9`: `trai = max(1, 4) = 4`, `phai = min(6, 9) = 6`; `4 <= 6` đúng nên in `GIAO NHAU 2`.
- Xử lý biên: ràng buộc cho phép tới `10^9` và âm tới `-10^9`. Thầy cô cho thử `1, 3, 5, 8`: `trai = 5`, `phai = 3`, `5 <= 3` sai nên in `KHONG GIAO NHAU`. Hai đoạn chạm nhau tại một điểm, ví dụ `1, 4, 4, 9`, vẫn là giao nhau với độ dài `0`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1 rồi 6 rồi 4 rồi 9)

Sample 1 với input mẫu: `1` rồi `6` rồi `4` rồi `9`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc bốn số | `l1 = 1, r1 = 6, l2 = 4, r2 = 9` | — |
| 2 | Tính mép trái: `1 >= 4`? Sai nên `trai = 4` | `trai = 4` | — |
| 3 | Tính mép phải: `6 <= 9`? Đúng nên `phai = 6` | `phai = 6` | — |
| 4 | Kiểm tra `4 <= 6`? Đúng | giao nhau | — |
| 5 | Tính `6 - 4 = 2` rồi in | — | `GIAO NHAU 2` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — lấy `min` cho mép trái: bạn nhỏ viết `trai = min(l1, l2)`. Với mẫu `1, 6, 4, 9` sẽ được `trai = 1`, `phai = 6`, in `GIAO NHAU 5`, sai. Cách sửa: mép trái lấy số lớn hơn (`max`), mép phải lấy số nhỏ hơn (`min`).
- Bẫy 2 — dùng `<` thay vì `<=`: bạn nhỏ viết `if trai < phai`. Với hai đoạn chạm nhau tại một điểm như `1, 4, 4, 9` sẽ in `KHONG GIAO NHAU`, sai vì đề tính cả điểm chung. Cách sửa: dùng `trai <= phai`.
- Bẫy 3 — đọc cứng bốn dòng: bạn nhỏ gọi `input()` bốn lần mà không tách. Với input `1 6 4 9` trên một dòng sẽ thiếu. Cách sửa: tách dòng đầu rồi mới đọc tiếp như lời giải mẫu.

#### 4. Lời giải tham khảo

```python
dong1 = input().split()
if len(dong1) >= 4:
    l1 = int(dong1[0])
    r1 = int(dong1[1])
    l2 = int(dong1[2])
    r2 = int(dong1[3])
else:
    l1 = int(dong1[0])
    r1 = int(input().split()[0])
    l2 = int(input().split()[0])
    r2 = int(input().split()[0])
if l1 >= l2:
    trai = l1
else:
    trai = l2
if r1 <= r2:
    phai = r1
else:
    phai = r2
if trai <= phai:
    print("GIAO NHAU", phai - trai)
else:
    print("KHONG GIAO NHAU")
```

### Bài 34 [pya_l05_p05_ve_gui_xe_ben_bai]: Vé gửi xe bến bãi

Bối cảnh: Sáng chủ nhật, cả nhà Bo đến khu vui chơi gửi xe ở bãi giữ xe thông minh. Bác bảo vệ vui tính chỉ bảng giá vé theo loại phương tiện: loại `1` (Xe đạp) giá $2$ nghìn đồng, loại `2` (Xe máy) giá $5$ nghìn đồng, loại `3` (Xe ô tô) giá $30$ nghìn đồng, còn các loại khác thì máy báo `LOI PHUONG TIEN`. Bo xung phong đọc mã loại xe giúp bác. Hãy tính đúng giá vé.

Nhiệm vụ: Nhập vào mã loại xe và in ra giá vé tương ứng; nếu mã không thuộc `1`, `2`, `3` thì in `LOI PHUONG TIEN`.

**Đầu vào (Input):**

Một số nguyên mã loại xe.

**Đầu ra (Output):**

Số tiền gửi xe hoặc chữ `LOI PHUONG TIEN`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| xe may | 5000 |

**Giải thích:** Phương tiện gửi là xe máy có mức phí 5000 đồng.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tra bảng giá theo mã đã viết thường: `pt` là `1` hoặc `xe dap` thì `2000`, là `2` hoặc `xe may` thì `5000`, là `3` hoặc `o to` thì `30000`, còn lại in `LOI PHUONG TIEN`.
- Cách làm của lời giải mẫu: đọc `pt = input().strip().lower()` rồi rẽ bốn nhánh. Với mẫu `xe may`: viết thường vẫn là `xe may`, rơi vào nhánh hai nên in `5000`.
- Xử lý biên: thầy cô cho thử `XE DAP` viết hoa (nhờ `.lower()` nên vẫn nhận, in `2000`) và mã lạ `5` (in `LOI PHUONG TIEN`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: xe may)

Sample 1 với input mẫu: `xe may`.
| Bước | Việc làm | Giá trị của `pt` | In ra |
|---|---|---|---|
| 1 | Đọc input, cắt khoảng trắng, viết thường | `pt = 'xe may'` | — |
| 2 | Kiểm tra nhánh một (`1` / `xe dap`)? Sai | xuống nhánh hai | — |
| 3 | Kiểm tra `pt == '2' or pt == 'xe may'`? Đúng | rẽ nhánh hai | — |
| 4 | In `5000` | — | `5000` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên viết thường: bạn nhỏ viết `pt = input().strip()` rồi so với `'xe may'`. Với mẫu `XE MAY` viết hoa sẽ không khớp, in `LOI PHUONG TIEN`, sai. Cách sửa: thêm `.lower()` như lời giải mẫu.
- Bẫy 2 — đọc `int` cho mã số: bạn nhỏ viết `pt = int(input())`. Với mẫu `xe may` chương trình sẽ lỗi. Cách sửa: đọc chuỗi như lời giải mẫu để nhận cả số và chữ.
- Bẫy 3 — quên nhánh mã lạ: bạn nhỏ chỉ viết ba nhánh xe mà không có `else`. Với mã `5` sẽ không in gì. Cách sửa: giữ nhánh cuối in `LOI PHUONG TIEN`.

#### 4. Lời giải tham khảo

```python
pt = input().strip().lower()
if pt == "1" or pt == "xe dap":
    print(2000)
elif pt == "2" or pt == "xe may":
    print(5000)
elif pt == "3" or pt == "o to":
    print(30000)
else:
    print("LOI PHUONG TIEN")
```

### Bài 35 [pya_l05_p12_bon_mua_trong_nam]: Bốn mùa trong năm

Bối cảnh: Trong giờ khoa học, cô giáo treo bức tranh bốn mùa thật đẹp lên bảng. Cô giảng rằng một năm có 12 tháng được chia thành 4 mùa: **Mùa Xuân** gồm tháng 1, 2, 3; **Mùa Hạ (Hè)** gồm tháng 4, 5, 6; **Mùa Thu** gồm tháng 7, 8, 9; còn **Mùa Đông** gồm tháng 10, 11, 12. Su thích nhất mùa hè vì được đi biển cùng gia đình. Hãy xác định một tháng bất kỳ thuộc mùa nào.

Nhiệm vụ: Nhập vào một số nguyên $M$.
 * Nếu $1 \le M \le 12$, hãy in ra tên mùa tương ứng (`XUAN`, `HA`, `THU`, `DONG`).
 * Nếu $M$ không nằm từ 1 đến 12, in ra `THANG KHONG HOP LE`.

**Đầu vào (Input):**

Một số nguyên $M$ ($-100 \le M \le 100$).

**Đầu ra (Output):**

Tên mùa hoặc thông báo lỗi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 4 | HA |

**Giải thích:** Tháng 4 thuộc mùa hạ (mùa hè).

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tra tháng `t` vào bốn nhóm: `1, 2, 3` là `XUAN`; `4, 5, 6` là `HA`; `7, 8, 9` là `THU`; `10, 11, 12` là `DONG`.
- Cách làm của lời giải mẫu: đọc `t`, kiểm tra `if t in [1, 2, 3]` rồi tới các `elif` theo nhóm. Với mẫu `t = 4`: nhóm xuân sai, nhóm `4, 5, 6` đúng nên in `HA`.
- Xử lý biên: ràng buộc `-100 <= M <= 100`. Thầy cô lưu ý lời giải mẫu không có nhánh cho tháng ngoài `1..12`, nên với `M = 0` hay `M = 13` chương trình không in gì; khi dạy cần đối chiếu với chương trình kiểm tra của lớp mình.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4)

Sample 1 với input mẫu: `4`.
| Bước | Việc làm | Giá trị của `t` | In ra |
|---|---|---|---|
| 1 | Đọc input | `t = 4` | — |
| 2 | Kiểm tra `4` trong `[1, 2, 3]`? Sai | xuống nhánh `elif` | — |
| 3 | Kiểm tra `4` trong `[4, 5, 6]`? Đúng | rẽ nhánh hai | — |
| 4 | In kết quả | — | `HA` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — viết điều kiện dài dòng sai: bạn nhỏ viết `if t == 4 or 5 or 6`. Với `t = 1` cụm này vẫn đúng nên in `HA`, sai. Cách sửa: dùng `t in [4, 5, 6]` như lời giải mẫu.
- Bẫy 2 — xếp tháng `6` vào mùa thu: bạn nhỏ viết nhóm thu là `[6, 7, 8]`. Với `t = 6` sẽ in `THU` thay vì `HA`. Cách sửa: giữ đúng bốn nhóm của lời giải mẫu.
- Bẫy 3 — in `HE` thay vì `HA`: đề kể mùa Hạ (Hè) nên có bạn in `HE`. Với mẫu `4`, chương trình kiểm tra chờ `HA` nên sẽ báo kết quả sai. Cách sửa: in đúng `HA`.

#### 4. Lời giải tham khảo

```python
t = int(input().strip())
if t in [1, 2, 3]:
    print("XUAN")
elif t in [4, 5, 6]:
    print("HA")
elif t in [7, 8, 9]:
    print("THU")
elif t in [10, 11, 12]:
    print("DONG")
```

### Bài 36 [pya_l06_p08_tam_giac_vuong_hay_khong]: Tam giác vuông hay không?

Bối cảnh: Trong giờ toán hình, cô giáo kể về định lý Pytago nổi tiếng: tam giác có 3 cạnh $a, b, c$ là tam giác vuông nếu bình phương một cạnh bằng tổng bình phương hai cạnh còn lại ($a^2 + b^2 = c^2$ hoặc $a^2 + c^2 = b^2$ hoặc $b^2 + c^2 = a^2$). Bạn Tôm rất thích xếp que tính thành hình tam giác và đoán xem hình nào có góc vuông. Tôm loay hoay mãi chưa chắc chắn. Hãy giúp Tôm kiểm tra xem ba que tính có tạo thành tam giác vuông không.

Nhiệm vụ: Cho 3 số dương $a, b, c$. Nếu chúng tạo thành một tam giác vuông thì in `VUONG`, ngược lại in `KHONG VUONG`.

**Đầu vào (Input):**

Ba số nguyên $a, b, c$ ($1 \le a, b, c \le 10^4$).

**Đầu ra (Output):**

`VUONG` hoặc `KHONG VUONG`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3 <br> 4 <br> 5 | VUONG |

**Giải thích:** $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là kiểm tra đẳng thức bình phương ba cạnh: `a * a + b * b == c * c` hoặc `a * a + c * c == b * b` hoặc `b * b + c * c == a * a`, đúng một vế là vuông.
- Cách làm của lời giải mẫu: đọc `a, b, c` linh hoạt cả hai kiểu input rồi kiểm tra cả ba vế nối bằng `or`. Với mẫu `3, 4, 5`: `3*3 + 4*4 = 25`, `5*5 = 25`, vế một đúng nên in `VUONG`.
- Xử lý biên: ràng buộc `1 <= a, b, c <= 10^4`, bình phương lên tới `10^8` vẫn vừa số nguyên. Thầy cô cho thử `a = 3, b = 4, c = 6` (`9 + 16 = 25` khác `36`, cả ba vế sai, in `KHONG VUONG`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 rồi 4 rồi 5)

Sample 1 với input mẫu: `3` rồi `4` rồi `5`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc các số | `a = 3, b = 4, c = 5` | — |
| 2 | Tính `3*3 + 4*4 = 25`, `5*5 = 25`; `25 == 25` đúng | cả cụm `or` đúng | — |
| 3 | In kết quả | — | `VUONG` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — chỉ kiểm tra một vế: bạn nhỏ viết `if a * a + b * b == c * c`. Với `a = 5, b = 3, c = 4` (cạnh huyền nằm ở `a`) sẽ in `KHONG VUONG`, sai. Cách sửa: giữ đủ ba vế nối bằng `or`.
- Bẫy 2 — dùng căn bậc hai: bạn nhỏ tính `c == (a*a + b*b) ** 0.5` rồi so số thực. Với số lớn dễ lệch dấu chấm động. Cách sửa: so bình phương nguyên như lời giải mẫu.
- Bẫy 3 — quên số mũ: bạn nhỏ viết `a + b == c`. Với mẫu `3, 4, 5` thì `7 == 5` sai nên in `KHONG VUONG`, sai. Cách sửa: nhân mỗi cạnh với chính nó trước khi cộng.

#### 4. Lời giải tham khảo

```python
dong1 = input().split()
if len(dong1) >= 3:
    a = int(dong1[0])
    b = int(dong1[1])
    c = int(dong1[2])
else:
    a = int(dong1[0])
    b = int(input().split()[0])
    c = int(input().split()[0])
if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
    print("VUONG")
else:
    print("KHONG VUONG")
```

### Bài 37 [pya_l06_p10_ngay_ke_tiep_trong_nam]: Ngày kế tiếp trong năm

Bối cảnh: Bạn Bông có một cuốn lịch để bàn rất xinh và ngày nào cũng tự tay xé một tờ. Hôm nay tờ lịch ghi một ngày hợp lệ gồm 3 số: ngày $D$, tháng $M$, năm $Y$. Bông tò mò muốn biết lật sang tờ tiếp theo sẽ là ngày tháng năm nào. Mẹ dặn rằng phải nhớ cả tháng dài tháng ngắn và năm nhuận nữa. Hãy giúp Bông tìm ra ngày kế tiếp ngay sau đó.

Nhiệm vụ: Hãy tính và in ra ngày, tháng, năm của **ngày kế tiếp ngay sau đó**.

**Đầu vào (Input):**

Ba số tự nhiên $D, M, Y$ trên 3 dòng.

**Đầu ra (Output):**

Ba số nguyên cách nhau một dấu cách `D_tiep M_tiep Y_tiep`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 31 <br> 12 <br> 2024 | 1 1 2025 |

**Giải thích:** Ngày cuối năm chuyển sang ngày đầu năm mới!

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 28 <br> 2 <br> 2024 | 29 2 2024 |

**Giải thích:** Năm 2024 là năm nhuận nên tháng 2 có ngày 29.

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 28 <br> 2 <br> 2023 | 1 3 2023 |

**Giải thích:** Năm 2023 thường nên sau 28/2 là sang 1/3.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là lật sang ngày mai: biết tháng `m` có bao nhiêu ngày (`ngay_trong_thang`) rồi xét ba cửa: còn trong tháng thì `d + 1`, hết tháng nhưng còn trong năm thì sang `1` tháng sau, hết năm thì sang `1 1` năm sau.
- Cách làm của lời giải mẫu: đọc `d, m, y` mỗi số một dòng; tính `nhuan` cho năm `y`; tra `ngay_trong_thang` (`31` cho các tháng `1, 3, 5, 7, 8, 10, 12`; `30` cho `4, 6, 9, 11`; tháng `2` là `29` nếu nhuận, `28` nếu thường); rồi rẽ ba nhánh in. Với mẫu `31, 12, 2024`: tháng `12` có `31` ngày, `d` đã chạm mốc và `m` chạm `12` nên in `1 1 2025`.
- Xử lý biên: thầy cô cho thử `28, 2, 2024` (nhuận, tháng `2` có `29` ngày, `28 < 29` nên in `29 2 2024`) và `28, 2, 2023` (thường, tháng `2` có `28` ngày, hết tháng nên in `1 3 2023`).

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 31 rồi 12 rồi 2024)

Sample 1 với input mẫu: `31` rồi `12` rồi `2024`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc ba dòng | `d = 31, m = 12, y = 2024` | — |
| 2 | Kiểm tra `2024` nhuận? Đúng | `nhuan = True` | — |
| 3 | Tháng `12` thuộc nhóm `31` ngày | `ngay_trong_thang = 31` | — |
| 4 | `31 < 31`? Sai; `12 < 12`? Sai | xuống nhánh cuối | — |
| 5 | In ngày đầu năm mới | — | `1 1 2025` |

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — tháng `2` luôn `28` ngày: bạn nhỏ viết `ngay_trong_thang = 28` cho mọi năm. Với `28, 2, 2024` sẽ in `1 3 2024` thay vì `29 2 2024`. Cách sửa: kiểm tra `nhuan` như lời giải mẫu.
- Bẫy 2 — quên cửa hết năm: bạn nhỏ chỉ viết `if d < ngay_trong_thang ... else print(1, m + 1, y)`. Với mẫu `31, 12, 2024` sẽ in `1 13 2024`, sai. Cách sửa: giữ nhánh `elif m < 12` rồi mới `else` sang năm mới.
- Bẫy 3 — nhớ sai nhóm tháng: bạn nhỏ cho tháng `8` vào nhóm `30` ngày. Với `31, 8, 2024` sẽ tính sai mốc. Cách sửa: giữ đúng nhóm `31` ngày là `1, 3, 5, 7, 8, 10, 12`.

#### 4. Lời giải tham khảo

```python
d = int(input().split()[0])
m = int(input().split()[0])
y = int(input().split()[0])
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    nhuan = True
else:
    nhuan = False
if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    ngay_trong_thang = 31
elif m == 4 or m == 6 or m == 9 or m == 11:
    ngay_trong_thang = 30
elif nhuan:
    ngay_trong_thang = 29
else:
    ngay_trong_thang = 28
if d < ngay_trong_thang:
    print(d + 1, m, y)
elif m < 12:
    print(1, m + 1, y)
else:
    print(1, 1, y + 1)
```

### Bài 01 [pya_l07_p14_tong_day_sieu_lon_khong_lap]: Tổng dãy siêu lớn không lặp

Bối cảnh: Trong hội thi lập trình của trường, ban giám khảo đố cả lớp một số $N$ cực lớn lên tới $10^9$ ($1$ tỷ) bạn nào cũng tròn mắt ngạc nhiên. Cô giáo dặn rằng nếu em dùng vòng lặp `for i in range(1, N + 1):` thì chương trình sẽ bị chạy quá thời gian quy định (Time Limit Exceeded - TLE) vì máy tính phải lặp 1 tỷ lần mất hơn 10 giây! Cả lớp đang loay hoay chưa biết làm sao cho nhanh. Hãy giúp cả lớp tìm cách tính thật nhanh.

Nhiệm vụ: Hãy tính tổng $S = 1 + 2 + \dots + N$ với thời gian chạy tức thì ($< 0.001$ giây) bằng công thức toán học.

**Đầu vào (Input):**

Một số nguyên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

Giá trị tổng $S$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 1000000000 | 500000000500000000 |

**Giải thích:** Với dữ liệu đầu vào là `1000000000`, kết quả thu được tương ứng là `500000000500000000`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: tổng 1 + 2 + ... + N bằng công thức ghép cặp của Gauss: `S = N * (N + 1) // 2`. Với N tới 1 000 000 000 mà dùng vòng lặp `for` thì phải lặp 1 tỉ lần, chạy quá thời gian quy định, nên bắt buộc dùng công thức tính thẳng.
- Quy trình trong lời giải: đọc `n = int(input())`, rồi tính `n * (n + 1) // 2` và in ra. Dấu `//` là chia lấy phần nguyên, giữ kết quả luôn là số nguyên.
- Xử lý biên: với N nhỏ nhất là 1 thì `1 * 2 // 2 = 1`; với N lớn nhất 1 000 000 000 thì `1000000000 * 1000000001 // 2 = 500000000500000000`, Python tính số nguyên lớn chính xác.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1000000000)

| Lượt | Giá trị của `n` | Biểu thức tính | Kết quả in ra |
|---|---|---|---|
| 1 | 1000000000 | 1000000000 * 1000000001 // 2 | 500000000500000000 |

Chương trình chỉ tính một phép nhân, một phép cộng và một phép chia nguyên rồi in ra `500000000500000000`, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng vòng lặp cộng dồn:
```python
n = int(input())
s = 0
for i in range(1, n + 1):
    s = s + i
print(s)
```
Với mẫu `1000000000` chương trình lặp 1 tỉ lần nên chạy quá thời gian quy định, không ra kết quả kịp. Cách sửa: thay cả vòng lặp bằng `print(n * (n + 1) // 2)`.
- Bẫy 2 — dùng chia `/` thay vì `//`:
```python
n = int(input())
print(n * (n + 1) / 2)
```
Với mẫu `1000000000` sẽ in ra `5e+17` (dạng số thực, mất chính xác). Cách sửa: dùng `//` để chia lấy phần nguyên.

#### 4. Lời giải tham khảo

```python
n = int(input())
print(n * (n + 1) // 2)
```

### Bài 02 [pya_l07_p01_dem_sao_len_troi]: Đếm sao lên trời

Bối cảnh: Đêm hè, người dùng ngước nhìn bầu trời đầy sao và bắt đầu đếm: 1, 2, 3... Hãy giúp in dãy số đếm sao từ 1 đến $N$.

Nhiệm vụ: Nhập vào một số tự nhiên $N$. Hãy in các số từ $1$ đến $N$ trên cùng một dòng, mỗi số cách nhau một khoảng trắng.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 100$).

**Đầu ra (Output):**

Dãy số từ 1 đến $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 5 | 1 2 3 4 5 |

**Giải thích:** Với dữ liệu đầu vào là `5`, kết quả thu được tương ứng là `1 2 3 4 5`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: in dãy số đếm 1, 2, 3, ..., N trên cùng một dòng, mỗi số cách nhau một dấu cách. Đây là bài làm quen với `range(1, n + 1)` sinh đúng N số.
- Quy trình trong lời giải: đọc `n`, rồi `" ".join(str(i) for i in range(1, n + 1))` biến từng số `i` thành chữ rồi nối lại bằng dấu cách, cuối cùng `print` một lần.
- Xử lý biên: với N nhỏ nhất là 1 thì chỉ in `1`; với N lớn nhất là 100 thì in đủ 100 số từ `1` tới `100`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5)

| Bước | Giá trị của `n` | `i` sinh ra từ `range(1, n + 1)` | Chuỗi sau `join` |
|---|---|---|---|
| 1 | 5 | 1, 2, 3, 4, 5 | `1 2 3 4 5` |

Chương trình in ra một dòng duy nhất `1 2 3 4 5`, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng `range(n)`:
```python
n = int(input().strip())
print(" ".join(str(i) for i in range(n)))
```
Với mẫu `5` sẽ in ra `0 1 2 3 4`, cho kết quả sai vì dãy bắt đầu từ 0 và thiếu số 5. Cách sửa: dùng `range(1, n + 1)`.
- Bẫy 2 — mỗi số một dòng:
```python
n = int(input().strip())
for i in range(1, n + 1):
    print(i)
```
Với mẫu `5` sẽ in 5 dòng thay vì một dòng `1 2 3 4 5`. Cách sửa: gom thành một chuỗi bằng `" ".join(...)` rồi in một lần.

#### 4. Lời giải tham khảo

```python
n = int(input().strip())
print(" ".join(str(i) for i in range(1, n + 1)))
```

### Bài 03 [pya_l07_p02_dem_nguoc_phong_ten_lua]: Đếm ngược phóng tên lửa

Bối cảnh: Trạm phóng tên lửa bắt đầu đếm ngược: 10, 9, 8... 1, PHONG! Hãy lập trình mô phỏng đếm ngược phóng tên lửa.

Nhiệm vụ: Trước khi phóng tàu vũ trụ, đồng hồ đếm ngược từ $N$ về 1, cuối cùng in ra chữ `PHONG!`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 20$).

**Đầu ra (Output):**

Mỗi số trên một dòng, dòng cuối in `PHONG!`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3 | 3 <br> 2 <br> 1 <br> PHONG! |

**Giải thích:** Với dữ liệu đầu vào là `3`, kết quả thu được tương ứng là `3
2
1
PHONG!`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: đếm ngược từ N về 1, mỗi số một dòng, rồi dòng cuối in chữ `PHONG!`. Dùng `range(n, 0, -1)` để bước nhảy là trừ 1 và dừng trước 0.
- Quy trình trong lời giải: đọc `n`, vòng lặp cho `i` chạy 3, 2, 1 và `print(i)` từng dòng, sau vòng lặp in thêm `print("PHONG!")`.
- Xử lý biên: với N nhỏ nhất là 1 thì chỉ in `1` rồi `PHONG!`; với N lớn nhất là 20 thì in đủ 20 dòng số cộng dòng `PHONG!`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3)

| Lượt lặp | Giá trị của `i` | Dòng in ra |
|---|---|---|
| 1 | 3 | 3 |
| 2 | 2 | 2 |
| 3 | 1 | 1 |
| sau lặp | — | PHONG! |

Kết quả cuối cùng là 4 dòng `3 / 2 / 1 / PHONG!`, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng `range(n, 1, -1)`:
```python
n = int(input())
for i in range(n, 1, -1):
    print(i)
print("PHONG!")
```
Với mẫu `3` chỉ in `3 / 2 / PHONG!`, thiếu mất số `1`. Cách sửa: điểm dừng là `0`, tức `range(n, 0, -1)`.
- Bẫy 2 — quên dòng `PHONG!` hoặc viết sai chữ hoa:
```python
n = int(input())
for i in range(n, 0, -1):
    print(i)
```
Với mẫu `3` chỉ in `3 / 2 / 1`, thiếu dòng cuối nên chương trình kiểm tra báo kết quả sai. Cách sửa: thêm `print("PHONG!")` sau vòng lặp.

#### 4. Lời giải tham khảo

```python
n = int(input())
for i in range(n, 0, -1):
    print(i)
print("PHONG!")
```

### Bài 04 [pya_l07_p03_tong_cac_so_tu_nhien]: Tổng các số tự nhiên

Bối cảnh: Nhà toán học Gauss khi còn đã tìm ra cách tính nhanh tổng các số từ 1 đến 100. Hãy viết chương trình tính tổng $1 + 2 + \dots + N$.

Nhiệm vụ: Nhập số nguyên dương $N$. Hãy tính tổng $S = 1 + 2 + 3 + \dots + N$.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^5$).

**Đầu ra (Output):**

Một số nguyên duy nhất là tổng $S$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 4 | 10 |

**Giải thích:** $1 + 2 + 3 + 4 = 10$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: tổng 1 + 2 + ... + N. Với N tới 100 000, lời giải dùng công thức `n * (n + 1) // 2` tính thẳng một phép, giống mẹo ghép cặp của Gauss.
- Quy trình trong lời giải: đọc `n`, tính `n * (n + 1) // 2` rồi `print`. Dấu `//` giữ kết quả là số nguyên.
- Xử lý biên: với N nhỏ nhất là 1 thì `1 * 2 // 2 = 1`; với N lớn nhất là 100 000 thì `100000 * 100001 // 2 = 5000050000`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4)

| Lượt | Giá trị của `n` | Biểu thức tính | Kết quả in ra |
|---|---|---|---|
| 1 | 4 | 4 * 5 // 2 | 10 |

Kết quả `10` chính là `1 + 2 + 3 + 4`, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng chia `/`:
```python
n = int(input().strip())
print(n * (n + 1) / 2)
```
Với mẫu `4` sẽ in ra `10.0` thay vì `10`, cho kết quả sai định dạng. Cách sửa: dùng `//`.
- Bẫy 2 — cộng dồn nhưng quên khởi tạo:
```python
n = int(input().strip())
for i in range(1, n + 1):
    s = s + i
print(s)
```
Chương trình báo lỗi vì biến `s` chưa được gán `0` trước vòng lặp. Cách sửa: thêm `s = 0` trước vòng lặp, hoặc dùng thẳng công thức như lời giải.

#### 4. Lời giải tham khảo

```python
n = int(input().strip())
print(n * (n + 1) // 2)
```

### Bài 05 [pya_l07_p13_tam_giac_vuong_dau_sao]: Tam giác vuông dấu sao

Bối cảnh: Thí sinh muốn vẽ một tam giác vuông bằng dấu sao, mỗi hàng tăng thêm một ngôi sao. Hãy giúp bạn ấy.

Nhiệm vụ: Nhập vào chiều cao $N$ của tam giác vuông. Hãy in ra tam giác vuông cân gồm các dấu sao theo mẫu:
 * Dòng 1 có 1 dấu `*`
 * Dòng 2 có 2 dấu `*`
 * ...
 * Dòng $N$ có $N$ dấu `*`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 50$).

**Đầu ra (Output):**

Tam giác vuông dấu `*`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 4 | * <br> ** <br> *** <br> **** |

**Giải thích:** Với dữ liệu đầu vào là `4`, kết quả thu được tương ứng là `*
**
***
****`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: dòng thứ `i` có đúng `i` dấu sao. Nhân chuỗi `'*' * i` được một hàng có độ dài tăng dần từ 1 tới N.
- Quy trình trong lời giải: đọc `n`, vòng lặp cho `i` chạy từ 1 tới `n`, mỗi lượt `print('*' * i)` in một hàng.
- Xử lý biên: với N nhỏ nhất là 1 thì chỉ in một dòng `*`; với N lớn nhất là 50 thì hàng cuối có đúng 50 dấu sao.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4)

| Lượt lặp | Giá trị của `i` | `'*' * i` | Dòng in ra |
|---|---|---|---|
| 1 | 1 | `*` | * |
| 2 | 2 | `**` | ** |
| 3 | 3 | `***` | *** |
| 4 | 4 | `****` | **** |

Bốn dòng ghép lại thành tam giác mẫu, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng `range(n)`:
```python
n = int(input())
for i in range(n):
    print('*' * i)
```
Với mẫu `4` dòng đầu là chuỗi rỗng và chỉ in tới 3 sao, cho kết quả sai. Cách sửa: dùng `range(1, n + 1)`.
- Bẫy 2 — in sao cách nhau dấu cách:
```python
n = int(input())
for i in range(1, n + 1):
    print('* ' * i)
```
Với mẫu `4` dòng đầu thành `* ` có dấu cách thừa, chương trình kiểm tra báo kết quả sai. Cách sửa: nhân đúng `'*' * i` không thêm dấu cách.

#### 4. Lời giải tham khảo

```python
n = int(input())
for i in range(1, n + 1):
    print('*' * i)
```

### Bài 06 [pya_l07_p12_hang_cot_dau_sao]: Hàng cột dấu sao

Bối cảnh: Trong giờ tin học, thầy giáo yêu cầu vẽ một hình chữ nhật bằng dấu sao `*`. Hãy viết chương trình vẽ hình.

Nhiệm vụ: Nhập vào số hàng $R$ và số cột $C$. Hãy in ra một hình chữ nhật đặc gồm các dấu sao `*` có kích thước $R$ hàng và $C$ cột.

**Đầu vào (Input):**

Hai số tự nhiên $R$ và $C$ ($1 \le R, C \le 50$).

**Đầu ra (Output):**

Hình chữ nhật dấu `*`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3 <br> 5 | ***** <br> ***** <br> ***** |

**Giải thích:** Với dữ liệu đầu vào là `3
5`, kết quả thu được tương ứng là `*****
*****
*****`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: hình chữ nhật đặc kích thước R hàng, C cột. Mỗi hàng là chuỗi `'*' * c` dài đúng C ký tự, lặp lại R lần.
- Quy trình trong lời giải: đọc `r` rồi đọc `c`, vòng lặp `for i in range(r)` in `print('*' * c)` mỗi lượt một hàng.
- Xử lý biên: với R = 1, C = 1 thì chỉ in một dấu `*`; với R = 50, C = 50 thì in 50 hàng, mỗi hàng 50 dấu sao.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 / 5)

| Lượt lặp | `i` trong `range(3)` | `'*' * 5` | Dòng in ra |
|---|---|---|---|
| 1 | 0 | `*****` | ***** |
| 2 | 1 | `*****` | ***** |
| 3 | 2 | `*****` | ***** |

Ba hàng giống nhau ghép thành hình chữ nhật 3x5, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đọc cả hai số trên một dòng:
```python
r, c = map(int, input().split())
for i in range(r):
    print('*' * c)
```
Với mẫu nhập `3` rồi xuống dòng `5`, lệnh tách một dòng sẽ thiếu số và lỗi. Cách sửa: đọc riêng `r = int(input())` rồi `c = int(input())` như lời giải.
- Bẫy 2 — nhầm số hàng với số cột:
```python
r = int(input())
c = int(input())
for i in range(c):
    print('*' * r)
```
Với mẫu `3 / 5` sẽ in 5 hàng mỗi hàng 3 sao, cho kết quả sai kích thước. Cách sửa: lặp `range(r)` và nhân `'*' * c`.

#### 4. Lời giải tham khảo

```python
r = int(input())
c = int(input())
for i in range(r):
    print('*' * c)
```

### Bài 07 [pya_l07_p07_tinh_giai_thua_n]: Tính giai thừa $N!$

Bối cảnh: Cuối tuần, bạn Tý mở một gian hàng kẹo nhỏ trước cổng trường. Tý xếp kẹo thành từng hàng vui nhộn: hàng có số tự nhiên $N$ thì Tý nhân tất cả các số tự nhiên từ 1 đến $N$ với nhau. Cách nhân dồn này được gọi là giai thừa, ký hiệu là $N!$, và được tính bằng công thức:
 $$N! = 1 \times 2 \times 3 \times \dots \times N$$
Hôm nay khách đông quá, Tý tính không kịp. Hãy giúp Tý tính nhanh giá trị $N!$.

Nhiệm vụ: Nhập số tự nhiên $N$ ($1 \le N \le 20$). Hãy tính và in ra giá trị $N!$.

**Đầu vào (Input):**

Một số tự nhiên $N$.

**Đầu ra (Output):**

Giá trị $N!$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 5 | 120 |

**Giải thích:** $1 \times 2 \times 3 \times 4 \times 5 = 120$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: giai thừa `N! = 1 x 2 x ... x N`. Khác với cộng dồn, ở đây biến `gt` khởi đầu bằng 1 và mỗi bước nhân thêm `i`.
- Quy trình trong lời giải: đọc `n`, đặt `gt = 1`, vòng lặp cho `i` chạy 1 tới `n`, mỗi lượt `gt = gt * i`, cuối cùng in `gt`.
- Xử lý biên: với N nhỏ nhất là 1 thì `gt = 1`; với N lớn nhất là 20 thì `20! = 2432902008176640000`, Python vẫn tính chính xác.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5)

| Lượt lặp | Giá trị của `i` | Phép tính `gt = gt * i` | Giá trị mới của `gt` |
|---|---|---|---|
| đầu | — | `gt = 1` | 1 |
| 1 | 1 | 1 * 1 | 1 |
| 2 | 2 | 1 * 2 | 2 |
| 3 | 3 | 2 * 3 | 6 |
| 4 | 4 | 6 * 4 | 24 |
| 5 | 5 | 24 * 5 | 120 |

In ra `120`, khớp với kết quả mẫu (`1 x 2 x 3 x 4 x 5 = 120`).

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — khởi tạo `gt = 0`:
```python
n = int(input())
gt = 0
for i in range(1, n + 1):
    gt = gt * i
print(gt)
```
Với mẫu `5` sẽ in ra `0` vì nhân với 0 luôn bằng 0. Cách sửa: khởi tạo `gt = 1`.
- Bẫy 2 — dùng cộng thay vì nhân:
```python
n = int(input())
gt = 1
for i in range(1, n + 1):
    gt = gt + i
print(gt)
```
Với mẫu `5` sẽ in ra `16` thay vì `120`. Cách sửa: dùng `gt = gt * i`.

#### 4. Lời giải tham khảo

```python
n = int(input())
gt = 1
for i in range(1, n + 1):
    gt = gt * i
print(gt)
```

### Bài 08 [pya_l07_p10_tong_binh_phuong]: Tổng bình phương

Bối cảnh: Nhà toán học muốn tính tổng bình phương của các số từ 1 đến $N$: $1^2 + 2^2 + 3^2 + \dots + N^2$. Hãy viết chương trình tính.

Nhiệm vụ: Nhập vào số nguyên dương $N$. Hãy tính tổng:
 $$S = 1^2 + 2^2 + 3^2 + \dots + N^2$$

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 1000$).

**Đầu ra (Output):**

Một số nguyên duy nhất là tổng $S$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3 | 14 |

**Giải thích:** $1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: tổng `S = 1^2 + 2^2 + ... + N^2`. Mỗi bước cộng thêm bình phương `i * i` của số hiện tại vào biến `s`.
- Quy trình trong lời giải: đọc `n`, đặt `s = 0`, vòng lặp cho `i` chạy 1 tới `n`, mỗi lượt `s = s + i * i`, cuối cùng in `s`.
- Xử lý biên: với N nhỏ nhất là 1 thì `s = 1`; với N lớn nhất là 1000 thì tổng là `1000 * 1001 * 2001 // 6 = 333833500`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3)

| Lượt lặp | Giá trị của `i` | Cộng thêm `i * i` | Giá trị mới của `s` |
|---|---|---|---|
| đầu | — | `s = 0` | 0 |
| 1 | 1 | 1 | 1 |
| 2 | 2 | 4 | 5 |
| 3 | 3 | 9 | 14 |

In ra `14` (vì `1 + 4 + 9 = 14`), khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — cộng `i` thay vì `i * i`:
```python
n = int(input())
s = 0
for i in range(1, n + 1):
    s = s + i
print(s)
```
Với mẫu `3` sẽ in ra `6` thay vì `14`. Cách sửa: cộng `s = s + i * i`.
- Bẫy 2 — dùng `i ** 2` nhưng đặt trong `print` mỗi lượt:
```python
n = int(input())
s = 0
for i in range(1, n + 1):
    s = s + i * i
    print(s)
```
Với mẫu `3` sẽ in 3 dòng `1 / 5 / 14` thay vì chỉ một dòng `14`. Cách sửa: để `print(s)` ngoài vòng lặp, không thụt đầu dòng.

#### 4. Lời giải tham khảo

```python
n = int(input())
s = 0
for i in range(1, n + 1):
    s = s + i * i
print(s)
```

### Bài 09 [pya_l07_p04_bang_cuu_chuong]: Bảng cửu chương

Bối cảnh: Trong giờ Toán, cô giáo yêu cầu học sinh in bảng cửu chương của một số $K$ bất kỳ. Hãy viết chương trình in bảng nhân tự động.

Nhiệm vụ: Nhập vào một số nguyên $K$ ($1 \le K \le 9$). Hãy in ra bảng cửu chương nhân của số $K$ từ 1 đến 10 theo đúng mẫu.

**Đầu vào (Input):**

Một số nguyên $K$.

**Đầu ra (Output):**

Gồm 10 dòng, mỗi dòng có định dạng: `K x i = [ket_qua]`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 5 | 5 x 1 = 5 <br> 5 x 2 = 10 <br> 5 x 3 = 15 <br> 5 x 4 = 20 <br> 5 x 5 = 25 <br> 5 x 6 = 30 <br> 5 x 7 = 35 <br> 5 x 8 = 40 <br> 5 x 9 = 45 <br> 5 x 10 = 50 |

**Giải thích:** Với dữ liệu đầu vào là `5`, kết quả thu được tương ứng là `5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: in 10 dòng bảng nhân của số K, dòng thứ `i` có dạng `K x i = K*i`. Vòng lặp cho `i` chạy từ 1 tới 10.
- Quy trình trong lời giải: đọc `n`, vòng lặp `for i in range(1, 11)`, mỗi lượt `print(f"{n} x {i} = {n * i}")` tự tính tích `n * i`.
- Xử lý biên: với K nhỏ nhất là 1 thì dòng cuối là `1 x 10 = 10`; với K lớn nhất là 9 thì dòng cuối là `9 x 10 = 90`.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5)

| Lượt lặp | Giá trị của `i` | Tích `5 * i` | Dòng in ra |
|---|---|---|---|
| 1 | 1 | 5 | 5 x 1 = 5 |
| 2 | 2 | 10 | 5 x 2 = 10 |
| 3 | 3 | 15 | 5 x 3 = 15 |
| 4 | 4 | 20 | 5 x 4 = 20 |
| 5 | 5 | 25 | 5 x 5 = 25 |
| 6 | 6 | 30 | 5 x 6 = 30 |
| 7 | 7 | 35 | 5 x 7 = 35 |
| 8 | 8 | 40 | 5 x 8 = 40 |
| 9 | 9 | 45 | 5 x 9 = 45 |
| 10 | 10 | 50 | 5 x 10 = 50 |

Đủ 10 dòng như kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng `range(1, 10)`:
```python
n = int(input().strip())
for i in range(1, 10):
    print(f"{n} x {i} = {n * i}")
```
Với mẫu `5` chỉ in 9 dòng, thiếu dòng `5 x 10 = 50`. Cách sửa: dùng `range(1, 11)`.
- Bẫy 2 — sai định dạng khoảng trắng:
```python
n = int(input().strip())
for i in range(1, 11):
    print(f"{n}x{i}={n * i}")
```
Với mẫu `5` dòng đầu thành `5x1=5` thay vì `5 x 1 = 5`, chương trình kiểm tra báo kết quả sai. Cách sửa: giữ đúng mẫu `f"{n} x {i} = {n * i}"`.

#### 4. Lời giải tham khảo

```python
n = int(input().strip())
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

### Bài 10 [pya_l07_p05_tong_so_chan_trong_doan]: Tổng số chẵn trong đoạn

Bối cảnh: Thí sinh muốn tính tổng tất cả các số chẵn nằm trong đoạn từ $A$ đến $B$. Hãy giúp bạn ấy viết chương trình tính nhanh.

Nhiệm vụ: Cho hai số nguyên dương $A$ và $B$ ($A \le B$). Hãy tính tổng tất cả các số chẵn nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$ nếu chúng là số chẵn).

**Đầu vào (Input):**

Hai số tự nhiên $A$ và $B$ trên 2 dòng ($1 \le A \le B \le 10^4$).

**Đầu ra (Output):**

Tổng các số chẵn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 3 <br> 8 | 18 |

**Giải thích:** Các số chẵn là: 4, 6, 8. Tổng: $4 + 6 + 8 = 18$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: trong đoạn từ A tới B chỉ cộng những số chia hết cho 2 (`i % 2 == 0`). Các số lẻ bị bỏ qua.
- Quy trình trong lời giải: đọc `a` rồi đọc `b`, đặt `s = 0`, vòng lặp cho `i` chạy từ `a` tới `b` (kể cả `b` nhờ `range(a, b + 1)`), nếu `i % 2 == 0` thì `s += i`, cuối cùng in `s`.
- Xử lý biên: đoạn nhỏ nhất A = B = 1 thì không có số chẵn nào nên tổng là 0; đoạn tới 10 000 thì vòng lặp duyệt tối đa 10 000 số.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 / 8)

| Lượt lặp | Giá trị của `i` | `i % 2 == 0`? | Giá trị mới của `s` |
|---|---|---|---|
| đầu | — | — | 0 |
| 1 | 3 | không | 0 |
| 2 | 4 | có, cộng 4 | 4 |
| 3 | 5 | không | 4 |
| 4 | 6 | có, cộng 6 | 10 |
| 5 | 7 | không | 10 |
| 6 | 8 | có, cộng 8 | 18 |

In ra `18` (vì `4 + 6 + 8 = 18`), khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên cộng 1 ở điểm dừng:
```python
a = int(input())
b = int(input())
s = 0
for i in range(a, b):
    if i % 2 == 0:
        s += i
print(s)
```
Với mẫu `3 / 8` chỉ xét tới 7 nên in ra `10` thay vì `18`. Cách sửa: dùng `range(a, b + 1)`.
- Bẫy 2 — kiểm tra số lẻ thay vì số chẵn:
```python
a = int(input())
b = int(input())
s = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        s += i
print(s)
```
Với mẫu `3 / 8` sẽ cộng 3 + 5 + 7 = `15` thay vì `18`. Cách sửa: điều kiện đúng là `i % 2 == 0`.

#### 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
s = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        s += i
print(s)
```

### Bài 11 [pya_l07_p11_doc_sach_moi_ngay]: Đọc sách mỗi ngày

Bối cảnh: Nghỉ hè, bạn Hoa mượn ở thư viện một cuốn truyện thật dày có tổng cộng $N$ trang để rèn thói quen đọc sách mỗi ngày. Ngày thứ nhất Hoa đọc được 1 trang thật ngon lành.
 * Ngày thứ hai Hoa đọc được 2 trang.
 * Ngày thứ ba Hoa đọc được 3 trang.
 * Cứ như vậy, ngày thứ $k$ Hoa đọc được $k$ trang.
Hoa háo hức muốn biết mình đọc hết truyện sau mấy ngày. Hãy đếm số ngày.

Nhiệm vụ: Hỏi sau đúng bao nhiêu ngày thì Hoa sẽ đọc hết (hoặc vượt quá) $N$ trang của cuốn sách?

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^4$).

**Đầu ra (Output):**

Số ngày ít nhất để Hoa đọc xong cuốn sách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 | 4 |

**Giải thích:** Ngày 1: 1 trang; ngày 2: 2 trang (tổng 3); ngày 3: 3 trang (tổng 6); ngày 4: 4 trang (tổng 10 $\ge 10$). Sau 4 ngày đọc xong.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 11 | 5 |

**Giải thích:** Sau 4 ngày mới đọc 10 trang, phải sang ngày thứ 5 mới đọc hết.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: ngày thứ `ngay` đọc được đúng `ngay` trang, tổng sau k ngày là `1 + 2 + ... + k`. Tìm k nhỏ nhất sao cho tổng đạt hoặc vượt N.
- Quy trình trong lời giải: đọc `n`, biến `tong` cộng dồn từng `ngay` trong `range(1, n + 2)`; ngay khi `tong >= n` thì in `ngay` và `break` dừng lại.
- Xử lý biên: với N nhỏ nhất là 1 thì ngày 1 đã đủ (tổng 1) nên in `1`; với N lớn nhất là 10 000 thì vòng lặp `range(1, n + 2)` luôn đủ dài để tìm ra đáp án.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10)

| Ngày (`ngay`) | Số trang ngày đó | Tổng `tong` | `tong >= 10`? |
|---|---|---|---|
| đầu | — | 0 | — |
| 1 | 1 | 1 | chưa |
| 2 | 2 | 3 | chưa |
| 3 | 3 | 6 | chưa |
| 4 | 4 | 10 | đủ, in 4 và dừng |

In ra `4`, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên `break` sau khi in:
```python
n = int(input())
tong = 0
for ngay in range(1, n + 2):
    tong = tong + ngay
    if tong >= n:
        print(ngay)
```
Với mẫu `10` sẽ in thêm các ngày 5, 6, ... vì vòng lặp không dừng. Cách sửa: thêm `break` ngay sau `print(ngay)`.
- Bẫy 2 — so sánh bằng thay vì lớn hơn hoặc bằng:
```python
n = int(input())
tong = 0
for ngay in range(1, n + 2):
    tong = tong + ngay
    if tong == n:
        print(ngay)
        break
```
Với những N không phải tổng của dãy liên tiếp (ví dụ N = 11: tổng nhảy từ 10 lên 15) thì không bao giờ bằng nên chẳng in gì. Cách sửa: điều kiện đúng là `tong >= n`.

#### 4. Lời giải tham khảo

```python
n = int(input())
tong = 0
for ngay in range(1, n + 2):
    tong = tong + ngay
    if tong >= n:
        print(ngay)
        break
```

### Bài 12 [pya_l07_p08_day_so_cach_deu]: Dãy số cách đều

Bối cảnh: Lớp bạn Na chơi trò nhảy ô số rất vui trên sân trường. Cả lớp thống nhất chọn số bắt đầu là số $a$, rồi mỗi bước nhảy phải dài đúng $d$ đơn vị, nghĩa là số tiếp theo hơn số đứng trước nó đúng $d$ đơn vị. Các bạn xếp thành một hàng dài và đọc to từng số mình nhảy tới. Na đếm mãi mà quên mất, hãy Na viết tiếp dãy số này.

Nhiệm vụ: Nhập vào số bắt đầu $a$, khoảng cách $d$ và số lượng phần tử cần in $n$. Hãy in ra $n$ số đầu tiên của dãy trên một dòng, cách nhau dấu cách.

**Đầu vào (Input):**

Ba số tự nhiên $a, d, n$ ($1 \le a, d, n \le 100$).

**Đầu ra (Output):**

Dãy số gồm $n$ phần tử.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 2 <br> 3 <br> 5 | 2 5 8 11 14 |

**Giải thích:** Với dữ liệu đầu vào là `2
3
5`, kết quả thu được tương ứng là `2 5 8 11 14`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: dãy cộng với số hạng đầu `a`, công sai `d`. Số hạng thứ `i` (đếm từ 0) là `a + i * d`.
- Quy trình trong lời giải: đọc `a`, `d`, `n`; vòng lặp cho `i` chạy `range(n)`, mỗi lượt in `a + i * d`; nếu chưa phải số cuối (`i < n - 1`) thì in thêm một dấu cách, cuối cùng xuống dòng.
- Xử lý biên: với n nhỏ nhất là 1 thì chỉ in mỗi `a`; mỗi giá trị a, d, n đều không vượt quá 100.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2 / 3 / 5)

| Lượt lặp | Giá trị của `i` | Tính `2 + i * 3` | Phần in ra |
|---|---|---|---|
| 1 | 0 | 2 | `2 ` |
| 2 | 1 | 5 | `5 ` |
| 3 | 2 | 8 | `8 ` |
| 4 | 3 | 11 | `11 ` |
| 5 | 4 | 14 | `14` + xuống dòng |

Một dòng duy nhất `2 5 8 11 14`, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — công thức thiếu `a`:
```python
a = int(input())
d = int(input())
n = int(input())
for i in range(n):
    print(a + d, end='')
```
Với mẫu `2 / 3 / 5` sẽ in toàn số `5` lặp lại. Cách sửa: công thức đúng là `a + i * d`.
- Bẫy 2 — mỗi số một dòng:
```python
a = int(input())
d = int(input())
n = int(input())
for i in range(n):
    print(a + i * d)
```
Với mẫu `2 / 3 / 5` sẽ in 5 dòng thay vì một dòng `2 5 8 11 14`. Cách sửa: in với `end=''` và chèn dấu cách giữa các số như lời giải.

#### 4. Lời giải tham khảo

```python
a = int(input())
d = int(input())
n = int(input())
for i in range(n):
    print(a + i * d, end='')
    if i < n - 1:
        print(' ', end='')
print()
```

### Bài 13 [pya_l07_p06_dem_boi_so_cua_k]: Đếm bội số của K

Bối cảnh: Cô giáo hỏi: "Trong đoạn từ $A$ đến $B$, có bao nhiêu số chia hết cho $K$?". Hãy viết chương trình đếm nhanh.

Nhiệm vụ: Nhập vào 3 số tự nhiên $A, B, K$ ($A \le B$). Hãy đếm xem có bao nhiêu số trong đoạn $[A, B]$ chia hết cho $K$.

**Đầu vào (Input):**

Ba số $A, B, K$ trên 3 dòng ($1 \le A \le B \le 10^5, 1 \le K \le 100$).

**Đầu ra (Output):**

Số lượng số chia hết cho $K$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 1 <br> 10 <br> 3 | 3 |

**Giải thích:** Gồm các số: 3, 6, 9. Tổng cộng 3 số.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: đếm các số trong đoạn [A, B] chia hết cho K, tức `i % k == 0`. Khác bài tính tổng, ở đây biến `count` tăng 1 mỗi khi gặp bội số.
- Quy trình trong lời giải: đọc 3 số vào danh sách `data` rồi tách `a, b, k`; đặt `count = 0`; vòng lặp cho `i` chạy từ `a` tới `b` (kể cả `b`), gặp bội của `k` thì `count = count + 1`; cuối cùng in `count`.
- Xử lý biên: nếu K lớn hơn cả đoạn (ví dụ A = 1, B = 10, K = 100) thì kết quả là 0; B tới 100 000 nên vòng lặp duyệt trực tiếp vẫn kịp.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1 / 10 / 3)

| Lượt lặp | Giá trị của `i` | `i % 3 == 0`? | Giá trị mới của `count` |
|---|---|---|---|
| đầu | — | — | 0 |
| 1 | 1 | không | 0 |
| 2 | 2 | không | 0 |
| 3 | 3 | có | 1 |
| 4 | 4 | không | 1 |
| 5 | 5 | không | 1 |
| 6 | 6 | có | 2 |
| 7 | 7 | không | 2 |
| 8 | 8 | không | 2 |
| 9 | 9 | có | 3 |
| 10 | 10 | không | 3 |

In ra `3` (các số 3, 6, 9), khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đọc sai thứ tự:
```python
a = int(input())
k = int(input())
b = int(input())
```
Với mẫu `1 / 10 / 3` sẽ hiểu K = 10, B = 3 nên đoạn rỗng và in ra `0`. Cách sửa: giữ đúng thứ tự `a, b, k` như lời giải.
- Bẫy 2 — cộng `i` thay vì tăng `count`:
```python
count = 0
for i in range(a, b + 1):
    if i % k == 0:
        count = count + i
print(count)
```
Với mẫu `1 / 10 / 3` sẽ in ra `18` (tổng) thay vì `3` (số lượng). Cách sửa: tăng `count = count + 1`.

#### 4. Lời giải tham khảo

```python
data = []
for _ in range(3):
    data.append(int(input()))
a, b, k = data
count = 0
for i in range(a, b + 1):
    if i % k == 0:
        count = count + 1
print(count)
```

### Bài 14 [pya_l07_p09_tim_uoc_so_cua_n]: Tìm ước số của N

Bối cảnh: Thí sinh đang học về ước số trong giờ Toán. Hãy viết chương trình liệt kê tất cả các ước số của một số $N$ cho trước.

Nhiệm vụ: Nhập vào số tự nhiên $N$. Hãy in ra tất cả các ước số dương của $N$ theo thứ tự tăng dần trên một dòng.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^4$).

**Đầu ra (Output):**

Các ước số của $N$ cách nhau một dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 12 | 1 2 3 4 6 12 |

**Giải thích:** Với dữ liệu đầu vào là `12`, kết quả thu được tương ứng là `1 2 3 4 6 12`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: ước của N là những số `i` mà `N % i == 0`. Duyệt `i` từ 1 tới N theo thứ tự tăng dần nên kết quả đã đúng thứ tự, không cần sắp xếp.
- Quy trình trong lời giải: đọc `n`, cờ `first` đánh dấu số đầu tiên để in dấu cách cho đẹp; gặp ước thì nếu không phải số đầu in `' '` trước rồi in `i`; cuối cùng xuống dòng.
- Xử lý biên: với N nhỏ nhất là 1 thì chỉ in `1`; với N lớn nhất là 10 000 thì duyệt 10 000 lượt, vẫn nhẹ.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12)

| Giá trị của `i` | `12 % i == 0`? | `first` | Phần in ra |
|---|---|---|---|
| 1 | có (12 % 1 = 0) | True thành False | `1` |
| 2 | có | False | ` 2` |
| 3 | có | False | ` 3` |
| 4 | có | False | ` 4` |
| 5 | không | — | — |
| 6 | có | False | ` 6` |
| 7-11 | không | — | — |
| 12 | có | False | ` 12` |

Một dòng `1 2 3 4 6 12`, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — kiểm tra ngược `i % n == 0`:
```python
n = int(input())
for i in range(1, n + 1):
    if i % n == 0:
        print(i, end=' ')
```
Với mẫu `12` chỉ in ra `12` vì chỉ có 12 chia hết cho 12. Cách sửa: điều kiện đúng là `n % i == 0`.
- Bẫy 2 — dấu cách thừa ở cuối:
```python
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')
```
Với mẫu `12` sẽ in `1 2 3 4 6 12 ` dư một dấu cách cuối, chương trình kiểm tra có thể báo kết quả sai. Cách sửa: dùng cờ `first` như lời giải để chỉ chèn cách ở giữa.

#### 4. Lời giải tham khảo

```python
n = int(input())
first = True
for i in range(1, n + 1):
    if n % i == 0:
        if not first:
            print(' ', end='')
        print(i, end='')
        first = False
print()
```

### Bài 01 [pya_l08_p08_tim_luy_thua_cua_2_lon_hon_n]: Tìm lũy thừa của 2 lớn hơn N

Bối cảnh: Tìm lũy thừa nhỏ nhất của 2 mà lớn hơn hoặc bằng số $N$ cho trước. Đây là bài toán cơ bản trong khoa học máy tính liên quan đến cấp phát bộ nhớ.

Nhiệm vụ: Nhập vào số tự nhiên $N$. Hãy tìm số có dạng lũy thừa của 2 ($1, 2, 4, 8, 16, 32, \dots$) **nhỏ nhất mà lớn hơn $N$**.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

Số lũy thừa của 2 tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 | 16 |

**Giải thích:** Lũy thừa của 2 gồm 1, 2, 4, 8, 16... Số nhỏ nhất $> 10$ là 16.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 16 | 32 |

**Giải thích:** Số phải lớn hơn 16 nên là 32.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: dãy lũy thừa của 2 là 1, 2, 4, 8, 16, ... Mỗi bước nhân đôi `lt = lt * 2` cho tới khi vượt qua N.
- Quy trình trong lời giải: đọc `n`, đặt `lt = 1`; chừng nào `lt <= n` thì nhân đôi `lt`; khi thoát vòng lặp thì `lt` là số cần tìm, đem in ra.
- Xử lý biên: với N nhỏ nhất là 1 thì `lt` đi 1 thành 2 nên in `2`; với N tới 1 000 000 000 thì nhân đôi khoảng 30 lần là xong.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10)

| Lần kiểm tra | Giá trị của `lt` | `lt <= 10`? | Hành động |
|---|---|---|---|
| đầu | 1 | đúng | lt thành 2 |
| 2 | 2 | đúng | lt thành 4 |
| 3 | 4 | đúng | lt thành 8 |
| 4 | 8 | đúng | lt thành 16 |
| 5 | 16 | sai | dừng, in 16 |

In ra `16` là lũy thừa của 2 nhỏ nhất mà lớn hơn 10, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — điều kiện dừng sai thành `lt < n`:
```python
n = int(input())
lt = 1
while lt < n:
    lt = lt * 2
print(lt)
```
Nếu N bản thân là lũy thừa của 2 (ví dụ N = 8) sẽ in ra `8` thay vì `16`. Cách sửa: điều kiện đúng là `while lt <= n`.
- Bẫy 2 — quên nhân đôi bên trong vòng lặp:
```python
n = int(input())
lt = 1
while lt <= n:
    lt = lt + 1
print(lt)
```
Với mẫu `10` sẽ in ra `11` thay vì `16`. Cách sửa: mỗi bước phải nhân đôi `lt = lt * 2`.

#### 4. Lời giải tham khảo

```python
n = int(input())
lt = 1
while lt <= n:
    lt = lt * 2
print(lt)
```

### Bài 02 [pya_l08_p06_gap_doi_to_giay_len_mat_trang]: Gấp đôi tờ giấy lên mặt trăng

Bối cảnh: Trong giờ thủ công, bạn Mít lấy ra một tờ giấy siêu mỏng ban đầu có độ dày là $1\text{ mm}$ để làm thí nghiệm vui. Mít gấp đôi tờ giấy lại, và lạ chưa: cứ mỗi lần gấp đôi tờ giấy lại, độ dày của nó lại tăng gấp đôi ($2\text{ mm}, 4\text{ mm}, 8\text{ mm}, \dots$). Mít mơ ước chồng giấy của mình sẽ cao chạm tới mặt trăng. Hãy giúp Mít đếm số lần gấp.

Nhiệm vụ: Hỏi cần phải gấp đôi tờ giấy ít nhất bao nhiêu lần để độ dày của nó đạt hoặc vượt quá độ cao $H\text{ mm}$?

**Đầu vào (Input):**

Một số tự nhiên $H$ ($1 \le H \le 10^9$).

**Đầu ra (Output):**

Số lần gấp đôi tối thiểu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 | 4 |

**Giải thích:** Lần 1: 2mm, lần 2: 4mm, lần 3: 8mm, lần 4: 16mm ($\ge 10$). Cần 4 lần.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: độ dày tờ giấy nhân đôi sau mỗi lần gấp: 1, 2, 4, 8, 16, ... Đếm xem gấp mấy lần thì đạt hoặc vượt chiều cao H.
- Quy trình trong lời giải: đọc `h`, đặt `day = 1` và `count = 0`; chừng nào `day < h` thì `day = day * 2` và `count = count + 1`; cuối cùng in `count`.
- Xử lý biên: với H nhỏ nhất là 1 thì không cần gấp lần nào nên in `0`; với H tới 1 000 000 000 thì gấp khoảng 30 lần là đủ.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10)

| Lần kiểm tra | `day` | `day < 10`? | `count` sau bước |
|---|---|---|---|
| đầu | 1 | đúng | 0 |
| 1 | 2 | đúng | 1 |
| 2 | 4 | đúng | 2 |
| 3 | 8 | đúng | 3 |
| 4 | 16 | sai (16 >= 10) | 4, dừng |

In ra `4` (2mm, 4mm, 8mm, 16mm), khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — tăng `count` trước khi gấp:
```python
h = int(input())
day = 1
count = 0
while day < h:
    count = count + 1
    day = day * 2
print(count)
```
Trông giống nhau nhưng với cách này thứ tự vẫn đúng; bẫy thật sự là khởi đầu `day = 0`:
```python
h = int(input())
day = 0
count = 0
while day < h:
    day = day * 2
    count = count + 1
print(count)
```
Với mẫu `10` thì `0 * 2` mãi bằng 0 nên vòng lặp không bao giờ dừng. Cách sửa: khởi đầu `day = 1`.
- Bẫy 2 — điều kiện `day <= h`:
```python
h = int(input())
day = 1
count = 0
while day <= h:
    day = day * 2
    count = count + 1
print(count)
```
Khi H đúng bằng lũy thừa của 2 (ví dụ H = 8) sẽ đếm thừa một lần. Cách sửa: điều kiện đúng là `while day < h`.

#### 4. Lời giải tham khảo

```python
h = int(input())
day = 1
count = 0
while day < h:
    day = day * 2
    count = count + 1
print(count)
```

### Bài 03 [pya_l08_p07_ong_heo_mua_xe_may]: Ống heo mua xe máy

Bối cảnh: Bác Nam có một chú heo đất thật xinh đặt ở góc nhà. Bác muốn tiết kiệm tiền để mua một chiếc xe máy có giá $P$ nghìn đồng cho cả gia đình đi chơi.
 * Ngày thứ nhất bác bỏ vào ống heo 1 nghìn đồng.
 * Ngày thứ hai bác bỏ vào 2 nghìn đồng.
 * Ngày thứ $k$ bác bỏ vào đúng $k$ nghìn đồng.
Mỗi tối bác đều lắc heo nghe kêu leng keng rất vui. Hãy giúp bác Nam đếm xem sau mấy ngày thì đủ tiền.

Nhiệm vụ: Hỏi sau bao nhiêu ngày thì tổng số tiền trong ống heo của bác Nam đạt hoặc vượt quá $P$ nghìn đồng?

**Đầu vào (Input):**

Một số tự nhiên $P$ ($1 \le P \le 10^7$).

**Đầu ra (Output):**

Số ngày ít nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 15 | 5 |

**Giải thích:** Ngày 1: 1k, ngày 2: 2k (tổng 3k), ngày 3: 3k (tổng 6k), ngày 4: 4k (tổng 10k), ngày 5: 5k (tổng 15k $\ge 15$). Sau 5 ngày.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: ngày thứ `ngay` bỏ vào đúng `ngay` nghìn đồng, tổng sau k ngày là `1 + 2 + ... + k`. Tìm k nhỏ nhất để tổng đạt hoặc vượt P.
- Quy trình trong lời giải: đọc `p`, đặt `tong = 0` và `ngay = 0`; chừng nào `tong < p` thì tăng `ngay` thêm 1 rồi cộng `tong = tong + ngay`; cuối cùng in `ngay`.
- Xử lý biên: với P nhỏ nhất là 1 thì ngày 1 đã đủ nên in `1`; với P tới 10 000 000 thì số ngày khoảng 4472 ngày.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 15)

| Ngày (`ngay`) | Bỏ vào ngày đó | Tổng `tong` | `tong < 15`? |
|---|---|---|---|
| đầu | — | 0 | đúng |
| 1 | 1 | 1 | đúng |
| 2 | 2 | 3 | đúng |
| 3 | 3 | 6 | đúng |
| 4 | 4 | 10 | đúng |
| 5 | 5 | 15 | sai, dừng |

In ra `5`, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — cộng trước khi tăng ngày:
```python
p = int(input())
tong = 0
ngay = 0
while tong < p:
    tong = tong + ngay
    ngay = ngay + 1
print(ngay)
```
Với mẫu `15` thì ngày đầu cộng 0 nên kết quả lệch thành `6`. Cách sửa: tăng `ngay` trước rồi mới cộng `tong = tong + ngay`.
- Bẫy 2 — mỗi ngày bỏ cố định 1 nghìn:
```python
p = int(input())
tong = 0
ngay = 0
while tong < p:
    ngay = ngay + 1
    tong = tong + 1
print(ngay)
```
Với mẫu `15` sẽ in ra `15` thay vì `5`. Cách sửa: ngày thứ `ngay` phải cộng đúng `ngay` nghìn.

#### 4. Lời giải tham khảo

```python
p = int(input())
tong = 0
ngay = 0
while tong < p:
    ngay = ngay + 1
    tong = tong + ngay
print(ngay)
```

### Bài 04 [pya_l08_p10_dem_so_luong_chu_so_cua_n]: Đếm số lượng chữ số của N

Bối cảnh: Cho một số nguyên dương $N$. Hãy đếm xem số đó có bao nhiêu chữ số. Ví dụ: $12345$ có $5$ chữ số.

Nhiệm vụ: Nhập vào một số nguyên dương $N$. Dùng vòng lặp `while` và phép chia nguyên `// 10`, hãy đếm xem số $N$ có bao nhiêu chữ số.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^{18}$).

**Đầu ra (Output):**

Số lượng chữ số của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 2026 | 4 |

**Giải thích:** Với dữ liệu đầu vào là `2026`, kết quả thu được tương ứng là `4`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: mỗi lần chia nguyên cho 10 (`N // 10`) là rụng đi một chữ số cuối. Đếm xem rụng mấy lần thì N còn 0.
- Quy trình trong lời giải: đọc `N`, đặt `dem = 0`; chừng nào `N > 0` thì `N = N // 10` và `dem = dem + 1`; cuối cùng in `dem`.
- Xử lý biên: với N nhỏ nhất là 1 thì chia một lần là hết nên in `1`; với N tới 10^18 (tối đa 19 chữ số nếu tính cả giới hạn) thì vòng lặp chạy đúng bằng số chữ số.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2026)

| Lần kiểm tra | Giá trị của `N` | `N > 0`? | `dem` sau bước |
|---|---|---|---|
| đầu | 2026 | đúng | 0 |
| 1 | 202 | đúng | 1 |
| 2 | 20 | đúng | 2 |
| 3 | 2 | đúng | 3 |
| 4 | 0 | sai, dừng | 4 |

In ra `4` vì 2026 có 4 chữ số, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng chia `/` thay vì `//`:
```python
N = int(input())
dem = 0
while N > 0:
      N = N / 10
      dem = dem + 1
print(dem)
```
Với mẫu `2026` thì N thành số thực 202.6, 20.26, ... không bao giờ bằng 0 đúng cách và có thể lặp rất lâu. Cách sửa: dùng `N = N // 10`.
- Bẫy 2 — điều kiện `N >= 0`:
```python
N = int(input())
dem = 0
while N >= 0:
      N = N // 10
      dem = dem + 1
print(dem)
```
Với mẫu `2026` thì khi N đã về 0 vòng lặp vẫn chạy tiếp (0 // 10 vẫn là 0) nên không bao giờ dừng. Cách sửa: điều kiện đúng là `while N > 0`.

#### 4. Lời giải tham khảo

```python
N = int(input())
dem = 0
while N > 0:
      N = N // 10
      dem = dem + 1
print(dem)
```

### Bài 05 [pya_l08_p01_dem_xuoi_bang_while]: Đếm xuôi bằng while

Bối cảnh: Bạn robot đang tập đếm số từ 1 đến $N$ bằng vòng lặp `while`. Hãy giúp robot hoàn thành nhiệm vụ.

Nhiệm vụ: Nhập vào số tự nhiên $N$. Dùng vòng lặp `while`, hãy in ra các số từ $1$ đến $N$ trên một dòng.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 100$).

**Đầu ra (Output):**

Dãy số từ 1 đến $N$.
 ```python
 N = int(input())
 i = 1
 while i <= N:
 print(i, end=" ")
 i = i + 1
 ```

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 5 | 1 2 3 4 5 |

**Giải thích:** In các số từ 1 đến 5 trên một dòng cách nhau khoảng trắng.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: giống bài đếm sao nhưng bắt buộc dùng vòng lặp `while` với lính canh `i <= n`. Biến `i` bắt đầu từ 1 và tự tăng 1 sau mỗi lượt.
- Quy trình trong lời giải: đọc `n`, đặt `i = 1` và danh sách rỗng `res`; chừng nào `i <= n` thì thêm `str(i)` vào `res` rồi `i += 1`; cuối cùng nối `res` bằng dấu cách và in ra.
- Xử lý biên: với N nhỏ nhất là 1 thì chỉ in `1`; với N lớn nhất là 100 thì in đủ 100 số.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5)

| Lần kiểm tra | Giá trị của `i` | `i <= 5`? | `res` sau bước |
|---|---|---|---|
| đầu | 1 | đúng | [1] |
| 2 | 2 | đúng | [1, 2] |
| 3 | 3 | đúng | [1, 2, 3] |
| 4 | 4 | đúng | [1, 2, 3, 4] |
| 5 | 5 | đúng | [1, 2, 3, 4, 5] |
| 6 | 6 | sai, dừng | — |

In ra một dòng `1 2 3 4 5`, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên tăng `i`:
```python
n = int(input().strip())
i = 1
res = []
while i <= n:
    res.append(str(i))
print(" ".join(res))
```
Với mẫu `5` vòng lặp chạy mãi không dừng vì `i` luôn bằng 1. Cách sửa: thêm `i += 1` trong vòng lặp.
- Bẫy 2 — khởi đầu `i = 0`:
```python
n = int(input().strip())
i = 0
res = []
while i <= n:
    res.append(str(i))
    i += 1
print(" ".join(res))
```
Với mẫu `5` sẽ in ra `0 1 2 3 4 5` thừa số 0. Cách sửa: khởi đầu `i = 1`.

#### 4. Lời giải tham khảo

```python
n = int(input().strip())
i = 1
res = []
while i <= n:
    res.append(str(i))
    i += 1
print(" ".join(res))
```

### Bài 06 [pya_l08_p03_nhap_so_den_khi_gap_so_0]: Nhập số đến khi gặp số 0

Bối cảnh: Trò chơi nhập số: Người chơi nhập liên tục các số, chương trình đếm tổng số lượng số đã nhập cho đến khi gặp số 0 thì dừng lại.

Nhiệm vụ: Viết chương trình nhập liên tiếp các số nguyên từ bàn phím. Việc nhập kết thúc khi người dùng nhập số 0. Hãy đếm xem người dùng đã nhập **bao nhiêu số** (không tính số 0 cuối cùng).

**Đầu vào (Input):**

Một dãy các số nguyên, kết thúc bằng số 0.

**Đầu ra (Output):**

Một số nguyên duy nhất là số lượng các số đã nhập trước số 0.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 5 <br> 12 <br> 8 <br> 0 | 3 |

**Giải thích:** Có 3 số: 5, 12, 8 đã được nhập trước khi gặp 0.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: không biết trước có bao nhiêu số, cứ đọc tới khi gặp số 0 thì dừng. Số 0 chỉ là lính gác báo dừng, không được đếm.
- Quy trình trong lời giải: đặt `count = 0`; `while True` đọc từng `x`; nếu `x == 0` thì `break`; ngược lại `count = count + 1`; cuối cùng in `count`.
- Xử lý biên: nếu nhập ngay số 0 đầu tiên thì kết quả là 0; dãy mẫu có 3 số trước số 0 nên kết quả là 3.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 / 12 / 8 / 0)

| Lần đọc | Giá trị của `x` | `x == 0`? | `count` sau bước |
|---|---|---|---|
| đầu | — | — | 0 |
| 1 | 5 | không | 1 |
| 2 | 12 | không | 2 |
| 3 | 8 | không | 3 |
| 4 | 0 | có, dừng | 3 |

In ra `3` vì có 3 số 5, 12, 8 trước số 0, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đếm luôn số 0:
```python
count = 0
while True:
    x = int(input())
    count = count + 1
    if x == 0:
        break
print(count)
```
Với mẫu `5 / 12 / 8 / 0` sẽ in ra `4` thay vì `3`. Cách sửa: kiểm tra `if x == 0: break` trước rồi mới tăng `count`.
- Bẫy 2 — dừng khi gặp số âm:
```python
count = 0
while True:
    x = int(input())
    if x <= 0:
        break
    count = count + 1
print(count)
```
Với dãy có số âm hợp lệ thì chương trình dừng sớm và đếm thiếu. Cách sửa: chỉ dừng khi `x == 0`.

#### 4. Lời giải tham khảo

```python
count = 0
while True:
    x = int(input())
    if x == 0:
        break
    count = count + 1
print(count)
```

### Bài 07 [pya_l08_p04_tong_day_so_ket_thuc_bang_0]: Tổng dãy số kết thúc bằng 0

Bối cảnh: Thí sinh nhập liên tiếp các số nguyên. Khi nhập số 0, chương trình dừng lại và in ra tổng tất cả các số đã nhập trước đó.

Nhiệm vụ: Nhập liên tục các số nguyên từ bàn phím cho đến khi gặp số 0. Hãy tính và in ra **tổng của tất cả các số** đã nhập.

**Đầu vào (Input):**

Một dãy số nguyên kết thúc bằng 0.

**Đầu ra (Output):**

Tổng các số.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 <br> 20 <br> 5 <br> 0 | 35 |

**Giải thích:** $10 + 20 + 5 = 35$.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: giống bài đếm tới số 0 nhưng thay vì đếm số lượng, ở đây cộng dồn giá trị vào biến `tong`. Số 0 cũng không được cộng.
- Quy trình trong lời giải: đặt `tong = 0`; `while True` đọc từng `x`; nếu `x == 0` thì `break`; ngược lại `tong = tong + x`; cuối cùng in `tong`.
- Xử lý biên: nếu nhập ngay số 0 thì tổng là 0; dãy mẫu 10, 20, 5 cho tổng 35.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10 / 20 / 5 / 0)

| Lần đọc | Giá trị của `x` | `x == 0`? | `tong` sau bước |
|---|---|---|---|
| đầu | — | — | 0 |
| 1 | 10 | không | 10 |
| 2 | 20 | không | 30 |
| 3 | 5 | không | 35 |
| 4 | 0 | có, dừng | 35 |

In ra `35` (vì `10 + 20 + 5 = 35`), khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — cộng luôn số 0 rồi mới kiểm tra (vẫn đúng trị nhưng lỗi tư duy), bẫy thật là tăng nhầm biến:
```python
tong = 0
while True:
    x = int(input())
    if x == 0:
        break
    tong = tong + 1
print(tong)
```
Với mẫu `10 / 20 / 5 / 0` sẽ in ra `3` (đếm số lượng) thay vì `35` (tổng). Cách sửa: cộng đúng `tong = tong + x`.
- Bẫy 2 — in tổng trong vòng lặp:
```python
tong = 0
while True:
    x = int(input())
    if x == 0:
        break
    tong = tong + x
    print(tong)
```
Với mẫu sẽ in 3 dòng `10 / 30 / 35` thay vì một dòng `35`. Cách sửa: để `print(tong)` ngoài vòng lặp.

#### 4. Lời giải tham khảo

```python
tong = 0
while True:
    x = int(input())
    if x == 0:
        break
    tong = tong + x
print(tong)
```

### Bài 08 [pya_l08_p11_tro_choi_doan_so_nhi_phan]: Trò chơi đoán số nhị phân

Bối cảnh: Giờ ra chơi, bạn An nghĩ ra một số bí mật từ 1 đến $N$ rồi đố cả lớp cùng đoán. Bạn Bình xung phong với chiến thuật rất hay tên là "Chặt đôi khoảng tìm kiếm" (Tìm kiếm nhị phân) để đoán số: mỗi câu hỏi Bình chia đôi khoảng đang xét ($N = N // 2$). Cả lớp nín thở theo dõi từng lượt đoán của Bình. Hãy giúp Bình tính trước xem mình cần đoán mấy lượt.

Nhiệm vụ: Hỏi trong trường hợp xấu nhất, Bình phải đoán **nhiều nhất bao nhiêu lần** thì chắc chắn tìm ra số của An (lặp cho đến khi khoảng chỉ còn 1 số: $N == 1$)?

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

Số bước đoán tối đa.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 8 | 4 |

**Giải thích:** Các bước: $8 \to 4 \to 2 \to 1$ (cần 4 bước).

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: mỗi lượt đoán thì khoảng tìm kiếm còn một nửa (`n = n // 2`). Đếm xem chặt đôi mấy lần thì khoảng còn đúng 1 số.
- Quy trình trong lời giải: đọc `n`, đặt `count = 0`; `while True` thì tăng `count` thêm 1, nếu `n == 1` thì dừng, ngược lại chặt đôi `n = n // 2`; cuối cùng in `count`.
- Xử lý biên: với N nhỏ nhất là 1 thì chỉ cần 1 lượt nên in `1`; với N tới 1 000 000 000 thì chặt đôi khoảng 30 lần.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 8)

| Lượt lặp | `n` đầu lượt | `count` sau khi tăng | Hành động |
|---|---|---|---|
| 1 | 8 | 1 | chưa bằng 1, n thành 4 |
| 2 | 4 | 2 | chưa bằng 1, n thành 2 |
| 3 | 2 | 3 | chưa bằng 1, n thành 1 |
| 4 | 1 | 4 | bằng 1, dừng |

In ra `4` (đường đi `8 -> 4 -> 2 -> 1`), khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — tăng `count` sau khi kiểm tra:
```python
n = int(input())
count = 0
while True:
    if n == 1:
        break
    n = n // 2
    count = count + 1
print(count)
```
Với mẫu `8` sẽ in ra `3` thay vì `4` vì lượt cuối không được đếm. Cách sửa: tăng `count` ngay đầu vòng lặp như lời giải.
- Bẫy 2 — dùng chia `/`:
```python
n = int(input())
count = 0
while True:
    count = count + 1
    if n == 1:
        break
    n = n / 2
print(count)
```
Với mẫu `8` thì n thành 4.0, 2.0, 1.0 rồi so sánh vẫn đúng, nhưng với N lớn số thực mất chính xác. Cách sửa: dùng `n = n // 2`.

#### 4. Lời giải tham khảo

```python
n = int(input())
count = 0
while True:
    count = count + 1
    if n == 1:
        break
    n = n // 2
print(count)
```

### Bài 09 [pya_l08_p02_rut_tham_den_khi_trung]: Rút thăm đến khi trúng

Bối cảnh: Giờ ra chơi, Bo tổ chức trò bốc thăm trúng thưởng cho cả lớp thật rộn ràng. Bo bỏ vào hộp thật nhiều lá phiếu có ghi số, rồi bốc lên từng lá một. Cả lớp reo hò vì ai cũng mong chờ, và Bo sẽ dừng lại ngay khi bốc trúng lá phiếu ghi số **7**. Trò chơi vui quá nên ai cũng muốn biết kết quả. Hãy giúp Bo công bố kết quả bốc thăm.

Nhiệm vụ: Nhập liên tục các số nguyên từ bàn phím cho đến khi gặp số 7 thì dừng lại. Hãy in ra dòng chữ: `DA TRUNG THUONG!`

**Đầu vào (Input):**

Một dãy các số nguyên, mỗi số trên một dòng, số cuối cùng chắc chắn là số 7.

**Đầu ra (Output):**

In `DA TRUNG THUONG!` sau khi vòng lặp dừng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 10 <br> 25 <br> 7 | DA TRUNG THUONG! |

**Giải thích:** Sau khi nhập hai số 10 và 25, số thứ ba nhập vào là 7 nên vòng lặp dừng và in ra thông báo `DA TRUNG THUONG!`.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: đọc liên tục không biết trước số lượng, dừng ngay khi bốc trúng lá phiếu số 7. Vòng lặp `while True` đọc từng `x` và `break` khi gặp 7.
- Quy trình trong lời giải: `while True` đọc `x`; nếu `x == 7` (lời giải còn chấp nhận thêm 77 cho chắc) thì `break`; sau vòng lặp in đúng một dòng `DA TRUNG THUONG!`.
- Xử lý biên: nếu lá đầu tiên đã là 7 thì in ngay; dãy mẫu 10, 25, 7 thì dừng ở lá thứ ba.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10 / 25 / 7)

| Lần đọc | Giá trị của `x` | `x == 7`? | Hành động |
|---|---|---|---|
| 1 | 10 | không | đọc tiếp |
| 2 | 25 | không | đọc tiếp |
| 3 | 7 | có | dừng vòng lặp |

Sau vòng lặp in ra `DA TRUNG THUONG!`, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — in thông báo trong vòng lặp:
```python
while True:
    x = int(input().strip())
    if x == 7:
        print("DA TRUNG THUONG!")
print("DA TRUNG THUONG!")
```
Với mẫu `10 / 25 / 7` vòng lặp không dừng nên chương trình treo luôn. Cách sửa: dùng `break` khi gặp 7 và chỉ in một lần sau vòng lặp.
- Bẫy 2 — sai chữ in (thường hoặc có dấu):
```python
while True:
    x = int(input().strip())
    if x == 7:
        break
print("Da trung thuong!")
```
Với mẫu `10 / 25 / 7` sẽ in `Da trung thuong!` khác chữ mẫu nên chương trình kiểm tra báo kết quả sai. Cách sửa: in đúng chữ in hoa `DA TRUNG THUONG!`.

#### 4. Lời giải tham khảo

```python
while True:
    try:
        x = int(input().strip())
        if x == 7 or x == 77:
            break
    except:
        break
print("DA TRUNG THUONG!")
```

### Bài 10 [pya_l08_p12_day_so_collatz_3n_1]: Dãy số Collatz (3n + 1)

Bối cảnh: Bạn Tí vừa đọc được một câu đố toán học kỳ bí tên là giả thuyết Collatz trong quyển truyện tranh khoa học ở thư viện. Trò biến hình số bắt đầu từ số tự nhiên $N > 0$ như sau:
 * Nếu $N$ là số chẵn: chia đôi $N = N // 2$.
 * Nếu $N$ là số lẻ: nhân ba cộng một $N = 3 \times N + 1$.
 * Lặp lại quy trình trên cho đến khi số $N$ biến thành số $1$ thì dừng lại!
Tí khoe với cả lớp mà chưa bạn nào đếm đúng số bước. Hãy giúp Tí đếm số bước biến hình.

Nhiệm vụ: Nhập vào số tự nhiên $N$. Hãy in ra số bước biến đổi để $N$ trở thành 1.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^5$).

**Đầu ra (Output):**

Số bước biến đổi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 6 | 8 |

**Giải thích:** Dãy biến đổi: $6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$ (qua 8 bước biến đổi).

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: luật biến hình Collatz: số chẵn thì chia đôi (`n = n // 2`), số lẻ thì nhân ba cộng một (`n = 3 * n + 1`). Biến `count` đếm mỗi lần biến hình cho tới khi n thành 1.
- Quy trình trong lời giải: đọc `n`, đặt `count = 0`; chừng nào `n != 1` thì xét chẵn lẻ để biến đổi rồi tăng `count`; cuối cùng in `count`.
- Xử lý biên: với N nhỏ nhất là 1 thì không biến hình lần nào nên in `0`; với N tới 100 000 vòng lặp vẫn kết thúc và cho kết quả đúng.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6)

| Bước | `n` đầu bước | Chẵn hay lẻ? | `n` sau bước | `count` |
|---|---|---|---|---|
| đầu | 6 | — | — | 0 |
| 1 | 6 | chẵn, 6 // 2 | 3 | 1 |
| 2 | 3 | lẻ, 3*3+1 | 10 | 2 |
| 3 | 10 | chẵn | 5 | 3 |
| 4 | 5 | lẻ | 16 | 4 |
| 5 | 16 | chẵn | 8 | 5 |
| 6 | 8 | chẵn | 4 | 6 |
| 7 | 4 | chẵn | 2 | 7 |
| 8 | 2 | chẵn | 1 | 8, dừng |

In ra `8`, khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên tăng `count` ở nhánh lẻ:
```python
n = int(input())
count = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
        count = count + 1
    else:
        n = 3 * n + 1
print(count)
```
Với mẫu `6` sẽ in ra `5` thay vì `8` vì 3 bước lẻ không được đếm. Cách sửa: đặt `count = count + 1` chung cho cả hai nhánh.
- Bẫy 2 — dùng `/` khi chia đôi:
```python
n = int(input())
count = 0
while n != 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    count = count + 1
print(count)
```
Với mẫu `6` thì n thành số thực 3.0, 10.0... dễ sai ở phép chia hết tiếp theo. Cách sửa: dùng `n = n // 2`.

#### 4. Lời giải tham khảo

```python
n = int(input())
count = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    count = count + 1
print(count)
```

### Bài 11 [pya_l08_p05_dem_so_chan_den_khi_gap_0]: Đếm số chẵn đến khi gặp 0

Bối cảnh: Trong trò chơi đếm số, người dùng nhập các số liên tục. Chương trình đếm xem có bao nhiêu số chẵn đã được nhập, cho đến khi gặp số 0 thì dừng.

Nhiệm vụ: Nhập liên tiếp các số nguyên từ bàn phím cho đến khi nhập số 0. Hãy đếm xem có bao nhiêu số chẵn trong các số đã nhập (không tính số 0).

**Đầu vào (Input):**

Dãy số nguyên kết thúc bằng 0.

**Đầu ra (Output):**

Số lượng số chẵn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 4 <br> 7 <br> 8 <br> 12 <br> 0 | 3 |

**Giải thích:** Có 3 số chẵn là 4, 8, 12.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: vừa đọc tới số 0 thì dừng (như bài đếm số lượng), vừa chỉ đếm những số chia hết cho 2 (`x % 2 == 0`). Số 0 dừng vòng lặp không được đếm.
- Quy trình trong lời giải: đặt `count = 0`; `while True` đọc `x`; nếu `x == 0` thì `break`; nếu `x % 2 == 0` thì tăng `count`; cuối cùng in `count`.
- Xử lý biên: nếu nhập ngay số 0 thì kết quả là 0; dãy mẫu 4, 7, 8, 12 cho 3 số chẵn.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 / 7 / 8 / 12 / 0)

| Lần đọc | Giá trị của `x` | Kiểm tra | `count` sau bước |
|---|---|---|---|
| đầu | — | — | 0 |
| 1 | 4 | chẵn, đếm | 1 |
| 2 | 7 | lẻ, bỏ qua | 1 |
| 3 | 8 | chẵn, đếm | 2 |
| 4 | 12 | chẵn, đếm | 3 |
| 5 | 0 | dừng | 3 |

In ra `3` (các số 4, 8, 12), khớp với kết quả mẫu.

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — kiểm tra chẵn trước khi kiểm tra 0:
```python
count = 0
while True:
    x = int(input())
    if x % 2 == 0:
        count = count + 1
    if x == 0:
        break
print(count)
```
Với mẫu `4 / 7 / 8 / 12 / 0` sẽ đếm luôn số 0 (0 chia hết cho 2) nên in ra `4` thay vì `3`. Cách sửa: kiểm tra `if x == 0: break` trước.
- Bẫy 2 — đếm số lẻ:
```python
count = 0
while True:
    x = int(input())
    if x == 0:
        break
    if x % 2 == 1:
        count = count + 1
print(count)
```
Với mẫu sẽ in ra `1` (chỉ có số 7) thay vì `3`. Cách sửa: điều kiện đúng là `x % 2 == 0`.

#### 4. Lời giải tham khảo

```python
count = 0
while True:
    x = int(input())
    if x == 0:
        break
    if x % 2 == 0:
        count = count + 1
print(count)
```

### Bài 12 [pya_l08_p09_chu_oc_sen_leo_cot_co]: Chú ốc sên leo cột cờ

Bối cảnh: Sáng nay, chú ốc sên chăm chỉ thức dậy dưới chân một cột cờ cao $H$ mét trong sân trường và quyết tâm leo lên đỉnh để ngắm mây trời.
 * Ban ngày, chú ốc sên bò lên được $A$ mét.
 * Ban đêm, khi ngủ chú bị tụt xuống $B$ mét ($B < A$).
 * Khi chú chạm tới hoặc vượt qua đỉnh cột cờ vào ban ngày, chú sẽ dừng lại và cắm cờ (không bị tụt nữa).
Các bạn kiến đứng dưới cổ vũ ầm ĩ. Hãy giúp chú ốc sên tính xem mình leo mất mấy ngày.

Nhiệm vụ: Hỏi chú ốc sên mất bao nhiêu ngày để leo lên tới đỉnh cột cờ?

**Đầu vào (Input):**

Ba số tự nhiên $H, A, B$ trên 3 dòng ($1 \le B < A \le H \le 10^6$).

**Đầu ra (Output):**

Số ngày để ốc sên chạm đỉnh.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
| :--- | :--- |
| 5 <br> 3 <br> 1 | 2 |

**Giải thích:** Ngày 1: leo lên 3m, đêm tụt 1m còn 2m.
Ngày 2: từ 2m leo thêm 3m lên 5m (chạm đỉnh ngay trong ngày!). Vậy mất 2 ngày.

#### 1. Ý tưởng & Phân tích thuật toán

- Bản chất: mỗi ngày leo lên A mét, nếu chưa chạm đỉnh thì đêm tụt B mét. Ngày chạm hoặc vượt đỉnh thì dừng ngay, không tụt nữa.
- Quy trình trong lời giải: đọc `h`, `a`, `b`; đặt `cao = 0` và `ngay = 0`; mỗi vòng tăng `ngay`, cộng `cao = cao + a`, kiểm tra `cao >= h` thì dừng, chưa đủ thì trừ `cao = cao - b`.
- Xử lý biên: nếu A đã lớn hơn hoặc bằng H (ví dụ H = 5, A = 5) thì ngày 1 đã xong; đề đảm bảo B < A nên mỗi ngày tiến thêm `A - B` mét, vòng lặp chắc chắn dừng.

#### 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 / 3 / 1)

| Ngày (`ngay`) | `cao` sau khi leo (+3) | Chạm đỉnh (`>= 5`)? | `cao` sau đêm (-1) |
|---|---|---|---|
| đầu | 0 | — | — |
| 1 | 3 | chưa | 2 |
| 2 | 5 | đủ, dừng | — |

In ra `2`, khớp với kết quả mẫu (ngày 1 còn 2m, ngày 2 chạm 5m).

#### 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — trừ B trước khi kiểm tra đỉnh:
```python
h = int(input())
a = int(input())
b = int(input())
cao = 0
ngay = 0
while True:
    ngay = ngay + 1
    cao = cao + a - b
    if cao >= h:
        break
print(ngay)
```
Với mẫu `5 / 3 / 1` thì ngày 2 tính thành 4 nên phải sang ngày 3, in ra `3` thay vì `2`. Cách sửa: cộng A rồi kiểm tra đỉnh trước, chỉ trừ B khi chưa chạm đỉnh.
- Bẫy 2 — công thức một dòng bỏ qua đêm cuối:
```python
h = int(input())
a = int(input())
b = int(input())
print((h + (a - b) - 1) // (a - b))
```
Với mẫu `5 / 3 / 1` cho `(5 + 1) // 2 = 3` thay vì `2` vì đêm cuối không bị tụt. Cách sửa: mô phỏng từng ngày bằng vòng lặp như lời giải.

#### 4. Lời giải tham khảo

```python
h = int(input())
a = int(input())
b = int(input())
cao = 0
ngay = 0
while True:
    ngay = ngay + 1
    cao = cao + a
    if cao >= h:
        break
    cao = cao - b
print(ngay)
```

# Mục lục

