# CẨM NANG CÚ PHÁP KHỐI LỆNH SCRATCHBLOCKS (DSL SPECIFICATION)

> Tài liệu này chuẩn hóa **100% cú pháp khối lệnh dạng văn bản (Scratchblocks DSL text format)** dùng trong các file `solution.dsl`, bài học `LessonXX_Production_Content.md` và đề bài của khóa học **Scratch Bảng A**.
> Cú pháp tương thích hoàn toàn với trình biên dịch `scratchblocks v3.7.1` (chuẩn Scratch 3.0).

---

## 1. Quy Ước Hình Dáng Khối Lệnh (Block Shapes)

| Hình dáng khối | Tên kỹ thuật | Cú pháp DSL | Màu sắc Scratch 3.0 |
|---|---|---|---|
| **Khối Mũ (Hat)** | Sự kiện khởi đầu | `when green flag clicked`, `when [space v] key pressed` | Vàng Events |
| **Khối Ngăn (Stack)** | Lệnh hành động | `move (10) steps`, `set [a v] to (10)` | Xanh dương Motion / Cam Variables |
| **Khối Chữ C (C-block)** | Khối lặp & điều kiện | `repeat (10) ... end`, `if <...> then ... end` | Cam Control |
| **Khối Ô Tròn (Reporter)** | Giá trị / Biểu thức | `((a) + (b))`, `(answer)`, `(length of [list v])` | Tròn, màu theo nhóm |
| **Khối Lục Giác (Boolean)** | Điều kiện logic True/False | `<(a) > (b)>`, `<[list v] contains (x)?>` | Lục giác, Xanh lá / Xanh lơ |
| **Khối Bút Vẽ (Pen)** | Vẽ đồ họa | `pen down`, `pen up`, `set pen color to [#ff0000]` | Xanh ngọc Pen |
| **Khối Tự Tạo (My Blocks)** | Khối hàm người dùng | `define ve_hinh (canh)`, `ve_hinh (100)` | Đỏ hồng My Blocks |

---

## 2. Bảng Tra Cứu Cú Pháp Khối Lệnh Tiêu Điểm

### 2.1. Nhóm Bút vẽ Pen (Extension)
```scratchblocks
erase all
pen down
pen up
set pen color to [#0000ff]
change pen color by (10)
set pen size to (2)
change pen size by (1)
```

### 2.2. Nhóm Chuyển động (Motion)
```scratchblocks
go to x: (0) y: (0)
point in direction (90)
move (100) steps
turn right (90) degrees
turn left (60) degrees
```

### 2.3. Nhóm Cảm biến & Xuất nhập (Sensing & IPO)
```scratchblocks
ask [Nhap so thu nhat:] and wait
(answer)
```

### 2.4. Nhóm Hiển thị (Looks)
```scratchblocks
say (join [Tong la: ] (tong))
say [Xin chao cac ban!] for (2) seconds
```

### 2.5. Nhóm Biến số & Danh sách (Variables & List)
```scratchblocks
set [x v] to [10]
change [x v] by (1)

add [qua tao] to [danh_sach v]
delete (1) of [danh_sach v]
delete all of [danh_sach v]
insert [cam] at (1) of [danh_sach v]
replace item (1) of [danh_sach v] with [xoai]
(item (1) of [danh_sach v])
(length of [danh_sach v])
<[danh_sach v] contains [cam] ?>
```

### 2.6. Nhóm Toán tử (Operators)
```scratchblocks
((a) + (b))
((a) - (b))
((a) * (b))
((a) / (b))
((a) mod (b))
(round (a))
(letter (1) of [Xin chao])
(length of [Xin chao])
(join [Hello ] [World])

<(a) > (b)>
<(a) < (b)>
<(a) = (b)>
<<condition1> and <condition2>>
<<condition1> or <condition2>>
<not <condition>>
```

### 2.7. Nhóm Điều khiển (Control)
```scratchblocks
repeat (4)
    move (100) steps
    turn right (90) degrees
end

if <(diem) >= (8)> then
    say [Gioi]
else
    say [Can co gang]
end

repeat until <(n) = (0)>
    set [tong v] to ((tong) + ((n) mod (10)))
    set [n v] to ([floor v] of ((n) / (10)))
end

stop [all v]
```

### 2.8. Khối Tự Tạo My Blocks (Custom Blocks)
```scratchblocks
define ve_da_giac (so_canh) (chieu_dai)
repeat (so_canh)
    move (chieu_dai) steps
    turn right ((360) / (so_canh)) degrees
end
```

---

## 3. Quy Tắc Vàng Khi Viết DSL

1. **Khối chữ C bắt buộc có `end`**: Mọi khối lặp (`repeat`, `repeat until`) và rẽ nhánh (`if`, `if...else`) bắt buộc phải đóng bằng từ khóa `end` thẳng hàng để bảo đảm tính phân cấp cây cú pháp.
2. **Dấu ngoặc tròn `()` cho giá trị, ngoặc nhọn `<>` cho điều kiện**:
   - Đúng: `<(a) > (b)>`, `((a) + (b))`
   - Sai: `((a) > (b))` (sai loại khối điều kiện lục giác)
3. **Menu thả xuống dùng ký hiệu `v`**:
   - Đúng: `set [bien v] to (10)`, `point in direction (90)`
   - Đúng: `[floor v] of (x)`
4. **Không viết chữ có dấu trong tên biến DSL**: Để tránh lỗi font khi render tự động, tên biến trong DSL dùng tiếng Việt không dấu cách nhau bằng gạch dưới: `[tong]`, `[bien_dem]`, `[so_canh]`, `[danh_sach]`.
