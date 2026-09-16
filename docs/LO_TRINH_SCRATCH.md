# HO SO DAC TA LO TRINH SU PHAM (SPEC REV 4.0)
# KHOA HOC: SCRATCH — TU DUY KHOI LENH, DO HOA & THUAT TOAN

> **Doi tuong:** Tieu hoc 8–11 tuoi. **Quy mo:** 6 CHUONG — 16 BAI (giao vien chu dong xep buoi day).
> Mo hinh 2 track: Bai 01–02 = Native Scratch Foundation (Pen, khong map Python); Bai 03–16 = Algorithmic Transfer (ten Chuong/Bai GIU NGUYEN Python; ma Scratch `sca_l01`–`sca_l14`; trace nguon qua cot Nguon, muc 1 + 6).

## 1. Bang map MA THAT Python → Scratch (dev bat buoc theo)

| Bai Scratch | Bai Python (ten goc) | Nguon Python (trace) | Ma Scratch (ID chot) |
|---|---|---|---|
| Bai 01–02 (Pen) — Native Foundation | Phu luc Pen (muc 5) | — | `sca_pen_pXX_ten` |
| Bai 03 | B01 Lệnh xuất nhập, biến số và kiểu dữ liệu | `pya_l01_*` (25 bai) | `sca_l01_p01..p25` |
| Bai 04 | B02 Toán tử và biểu thức | `pya_l02_*` (36 bai) | `sca_l02_p01..p36` |
| Bai 05 | B03 Phép chia nguyên, chia dư và lũy thừa | `pya_l03_*` (33 bai) | `sca_l03_p01..p33` |
| Bai 06 | B04 Cấu trúc rẽ nhánh — Concept: Re nhanh; Nguon: B04/l04 + mo rong l05/l06 (37 bai) | cot Nguon giu ma that | `sca_l04_p01..p37` (danh lai, trace qua cot Nguon) |
| Bai 07 | B05 Vòng lặp for và hàm range | `pya_l07_*` (14 bai) | `sca_l05_p01..p14`  |
| Bai 08 | B06 Vòng lặp while và biến cờ | `pya_l08_*` (12 bai) | `sca_l06_p01..p12`  |
| Bai 09 | B07 Quy luật dãy số và tam giác số | `pya_l09_*` (14 bai) | `sca_l07_p01..p14`  |
| Bai 10 | B08 Kỹ thuật tách chữ số và xử lý số nguyên qua vòng lặp while | `pya_l10_*` (14 bai) | `sca_l08_p01..p14`  |
| Bai 11 | B09 Ước số, Bội số và Số nguyên tố | `pya_l11_*` (14 bai) | `sca_l09_p01..p14`  |
| Bai 12 | B10 Đếm số theo quy luật và số đặc biệt | `pya_l12_*` (12 bai) | `sca_l10_p01..p12`  |
| Bai 13 | B11 Danh sách và thao tác cơ bản | `pya_l16_*` (26 bai) | `sca_l11_p01..p26`  |
| Bai 14 | B12 Thống kê danh sách và sắp xếp | `pya_l17_*` (14 bai) | `sca_l12_p01..p14`  |
| Bai 15 | B13 Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự | `pya_l13_*` (12 bai) | `sca_l13_p01..p12` |
| Bai 16 | B14 Duyệt chuỗi, biến đổi ký tự và tách từ | `pya_l14_*` + `pya_l15_*` tron (24 bai) | `sca_l14_p01..p24` (danh lai, trace qua cot Nguon) |

## 2. Bang chuyen doi Python → Scratch (1 bang duy nhat)

| Python | Scratch | Bay loi / Quy tac day |
|---|---|---|
| `input()` | `ask + set [bien] to (answer)` | luu NGAY sau moi ask (ghi de) |
| `print(x)` 1 dong | 1 `say` (nhieu bien → `join` long + cach) | CAM 2 `say` thay 1 dong (de nhau) |
| `print` nhieu dong | nhieu luot `say` (+`wait` ngan) | vd 3 dong tong/hieu/tich |
| `a, b = b, a` | qua `tam`: tam=a; a=b; b=tam | — |
| `//`, `%` | `floor(A/B)`, `A mod B` | — |
| `round(x,2)` / `f"{x:.2f}"` | `(round(x*100))/100`; bai ep `3.00` → SIMPLIFY, chap nhan `3` | vd phan so dai so, van toc |
| `for i in range(1,n+1)` | `repeat n` + dem tay (`i=1`, cuoi vong `change i by 1`) | khoi tao tong=0/tich=1 |
| `while` | `repeat until` (lap khi SAI, dung khi DUNG — nguoc while) | bay treo vo tan |
| `list[0]` | `item 1 of [list]` — INDEX TU 1 | cot tu |
| `len` | `length of [list]` / `length of ()` | — |
| `s[i]` | `letter (i) of ()` | — |
| `split()` | duyet gap cach → nap List | khong primitive san |

## 3. Khung bai hoc + tiet hoc

- Moi bai: Micro-theory 1 trang A4 (Khai niem vi von → Khoi tieu diem: ten Viet/nhom mau/dang Mu-Lap-Tron-Luc giac → 1–2 Quy tac vang/Bay loi → Dry-run) + Quiz toi thieu 10 cau (4 lua chon + dap an + giai thich + gan LO) + Bai tap 2 truc (P0–P3 × Observe/Arrange/Complete/Create).
- Timebox 90': 10' Khoi dong → 15' Kham pha → 20' Scaffolding → 30' Create (2–3 bai) → 10' Quiz → 5' Chot bay loi.
- Pacing: tren lop 1–2 bai dan + 4–6 Create; ve nha 15–20 bai P0–P3 tren LMS.
- Trinh bay: bang + cong thuc; callout Luu y/Meo nho/Quy tac vang; KHONG emoji; hinh co tieu de + so thu tu. Wording `Scratch-compatible`.

## 4. Quy tac Pen DAN XOAN (spiral — sua loi day ask som)

- Bai 01/02 Chuong 01 chi ve voi THONG SO CO DINH (dien so truc tiep vao o tron). Bai 2 VD1/VD2 file Pen (nhap canh/so hinh) de den Bai 03 nhu ban nang cap "nhap tu ban phim de ve" — dung chinh cac bai Pen cu de day ask-bien.
- Bai 05 (L03): 33 bai hinh hoc/do luong la SO HOC THUAN (nhap kich thuoc → tinh → say), KHONG nham voi bai ve Pen.

## 5. SYLLABUS CHI TIET (6 chuong, 16 bai)

### CHUONG 01: BUT VE (2 bai)

**Bai 01 — Ve hinh voi Pen va Repeat.**
- Khoi dong "Meo lam quen lop" → Kham pha: toa do tam (0,0), co xanh, Pen (xoa tat ca, mau, co but, dat/nhac but); tien/lui + 4 huong (0/90/180/-90) → Hoat dong: doan thang sac-day + dau cong do tam + cau thang 4 bac → Bay loi: quen xoa dau → hinh cu de len; nhac but truoc khi doi cho.
- Khoi dong "ve tay 8 khoi vs 1 repeat" → Kham pha: tron 360, goc ngoai = 360/so canh (`360° / so canh` — minh hoa goc quay bang hinh ve, khong giai thich dai); repeat + xoay phai → Hoat dong: Cau 1 (360/3,4,5,6) + 5.1 vuong dong tam (nhac-doi-dat) + 5.2 cot bac thang → My Blocks co ban (xuat hien theo nhu cau): "viet lai cum lenh nhieu lan → gom thanh khoi rieng de tai dung" (chi o muc gom cum lenh, CHUA day tham so).
- Kho Pen: `sca_pen_pXX` theo Cau file Ve hinh.

**Bai 02 — Hinh tron, cung tron va hoa van.**
- Khoi dong "duong cong = 360 doan thang ngan" → Kham pha: buoc = (2×R×3.14)/360 (R co dinh — cong thuc chi la CONG CU tinh gia tri can di, KHONG day y nghia toan chu vi) → Hoat dong: tron tam/mep + 10.1 chum dong tam + 10.4 sau tron + Cau 15 cau vong 7 mau (cung 180, R tang).
- canh hoa (2 cung 90 doi xung) → hoa 8 canh (Cau 16) → My Blocks nang cao: khoi `ve_hinh(...)` CO tham so, doi kich thuoc → tai dung → hoa van (Cau 6 la co → chum 8; Cau 7 nhanh → tuyet 6; Cau 9 canh → chong chong 9; Cau 12 Olympic) → Bay loi: loop 360 lag → Run-without-refresh.
- Tien trinh tu duy: hinh vuong → nhieu hinh → My Block → doi kich thuoc → hoa van.

### Phu luc Pen — Ngan hang bai tap tu chi tiet (dev build truc tiep, khong can file ngoai)

Moi bai duoi day ghi day du yeu cau + thong so + ky thuat. Bai nao ghi "theo hinh mau" thi hinh nam trong GOI ANH dinh kem (chu du an gui kem file nay); dev khong phai tim file goc.

**Bai 01 (ma `sca_pen_p00..p05`, `sca_pen_vd03`):**
- `p00_setup`: Co xanh → xoa tat ca → chon mau but → co net ve → dat but; toi x:0 y:0; huong 90; tien/lui buoc. Hoat dong: doan thang sac-day; dau cong do giua san khau; cau thang 4 bac.
- `p01` (Cau 1): Ve tam giac deu, hinh vuong, ngu giac deu, luc giac deu canh 100 bang `repeat n [tien 100, xoay 360/n]` (360/3, 360/4, 360/5, 360/6).
- `p02..p04` (Cau 2–4): Nhan phim 1/2/3/4 → ve 4 hinh tuong ung theo hinh mau goi anh.
- `p05` (Cau 5): 5.1 ve 3 hinh vuong dong tam (xong 1 hinh → nhac but, doi toa do, dat but, ve hinh lon hon); 5.2 ve 4 cot chu nhat bac thang cao dan.
- `vd03`: Manh ghep Ngu giac co do dai canh thay doi (tham so) — day khi hoc sinh lap lai cum lenh (My Blocks theo nhu cau).

**Bai 02 (ma `sca_pen_p10..p18`, `sca_pen_vd04..vd07`):**
- `p10` (Cau 10): Nhan phim 1–4 → 4 hinh tron theo hinh mau (tron tu tam + tron tu mep; chum dong tam; 6 tron quanh 1 tam).
- `p13` (Cau 13): Nhan phim 1–3 → 3 hinh theo hinh mau (gom tron R=50 do, net 2; 6 tron R tang 50→100+; 40 tron doi mau).
- `p14` (Cau 14): Nhan phim 1–4 → cung 45/90/180/360 do theo hinh mau.
- `p15` (Cau 15): Cau vong 7 mau (do, cam, vang, xanh la, lam nhat, lam dam, tim) bang cung tron 180 do, net day, ban kinh tang dan tu ngoai vao trong.
- `p16` (Cau 16): Manh ghep Canh hoa = lap 2 lan [cung 90 do + xoay 90]; ve bong hoa so canh nhap tu ban phim o ban day du (ban Bai 02 dung 8 canh co dinh, mau tu chon).
- `p17` (Cau 17): Manh ghep Canh cung (cung 180 do, ban kinh tuy chon) + Hinh 17.1 theo hinh mau.
- `p18` (Cau 18): Nhan phim 1–4 → 4 hinh theo hinh mau.
- `vd04..vd05`: Manh ghep "Duong tron 1/2" voi ban kinh cho truoc; ve tron R tu chon + doi mau.
- `vd06..vd07`: Manh ghep cung tron; ve quat (cung + ban kinh, mau tuy chon).
- `p06f/p07f/p11f/p12f` (ban co dinh Cau 6/7/11/12): Cau 6 la co → chum 8 la (so co dinh); Cau 7 nhanh cay → bong tuyet 6 nhanh (so co dinh); Cau 11 nhanh → 2 hinh moi hinh 10 nhanh (so co dinh); Cau 12 logo Olympic (tron xanh duong/den/do tren; vang/xanh la duoi; net 10; toa do co dinh theo hinh mau).
- `p08` (Cau 8): Manh ghep nhanh theo hinh mau goi anh.
- `p09f` (ban co dinh Cau 9): Canh chong chong goi y `tien 100, xoay 60, tien 100, xoay 150, tien 173, xoay 150` → chong chong 9 canh co dinh; hoa tuyet 8 canh co dinh.

**Spiral tai Bai 03 (ma `sca_pen_p06..p11-ask`, `sca_pen_vd01..vd02`):**
- `vd01`: Luc giac deu canh nhap tu ban phim (`ask` → `repeat 6 [tien (answer), xoay 60]`).
- `vd02`: Chum hinh vuong so luong + do dai + mau tu chon (2 loop long; ngoai xoay 360/so-luong).
- `p06/p07/p09/p11-ask`: Dung de Cau 6/7/9/11 goc (so la co/nhanh/canh nhap tu ban phim).
- `p30` (Cau 30): Nhan phim 1 → Hinh 30.1 (nhap 10 canh); phim 2 → Hinh 30.2 (nhap 4 canh).

**Ngan hang nang cao (ma `sca_pen_p19..p59`, rai sau bien/loop):**
- `vd10`: Hinh to mau (net 2–3). `p19`: hinh theo mau, mau tuy y. `p20`: xoan oc (canh nho nhat 10, lap 35 lan, moi lan tang 5; bien the giam tu 250) → Bai 07. `p21`: ket hop tam giac/tron/chu nhat/ngoi sao/vuong theo hinh mau. `p22`: chia tron R=120 thanh 3 (hoac 5) phan mau khac nhau. `p23`: hoa thoi (canh nhu Hinh 23.1, so canh nhap). `p24`: theo hinh mau.
- `p25/p27/p28`: phim 1–4 → 4 hinh theo hinh mau. `p26`: hinh tu "Canh" + so luong nhap. `p29`: hoa thoi (4 canh 80, goc 360/n hoac 180-360/n, n hinh). `p31`: tron khuyet (net 2). `p32`: kim tu thap. `p33..p35/p37/p39/p43`: theo hinh mau (gom bien bao cam R ngoai 110/trong 90; violet R50; tam giac soc nho nhat 30; long den ong sao).
- `p36`: luoi vuong n×n (n nhap, o 30, toa do ban dau theo hinh mau). `p38/p40`: so hang + kich thuoc o nhap. `p44`: tam giac nhieu tang (so tang nhap). `p47`: luoi cot×dong nhap (o vuong, diem neo theo hinh mau) → Bai 09 (nested). `p48`: canh chong chong. `p50`: ngoi sao canh tam giac (nhap canh tam giac nho). `p51`: co do sao vang (dai 3a, rong 2a, tam–dinh sao theo hinh mau, a nhap) → du an.
- `p54`: n tron (n chan, 0<n≤360) R/mau tu chon. `p55..p57/p59`: hinh theo mau voi R tron (nho/lon) nhap. `p58`: hinh voi canh luc giac ngoai nhap.

### CHUONG 02: TÍNH TOÁN CƠ BẢN (Bai 03–05)

**Bai 03 — Lệnh xuất nhập, biến số và kiểu dữ liệu (Nguon L01; ma `sca_l01_*`).****
- Khoi dong "Lam sao Meo biet ten em?" → Kham pha IPO (ban phim → bo nho → san khau); ask/answer + say + join (chu y dau cach) → Hoat dong: "Danh thiep thong minh" (nhap ten → chao) + "Thiep sinh nhat" (ghep ten + tuoi) + Pen spiral: luc giac canh nhap (VD1).
- Kham pha hop dan nhan; gan = tinh phai nap trai; BAY ghi de answer (cat ngay sau moi ask); hoan doi qua `tam`; dry-run a/b/tong → Hoat dong: "May cong 2 so" + "Hop keo hoan doi" + Pen spiral: chum vuong xoay theo so nhap (VD2).
- Kho: muc 6 (25 bai: P0 chao robot/cau doi; P1 doc-in/nhan doi/tong-hieu-tich/cap doi/tuoi/sep/end; P2 hoan doi/chuc/cua hang/doi thuoc/ghep ngay/bang nhan/doan tau/chenh tuoi; P3 bon phep tinh/co may 3 the he/Chua Huong).

**Bai 04 — Toán tử và biểu thức (Nguon L02; ma `sca_l02_*`).****
- Khoi dong viet tay vs may tinh → Kham pha long trong = ngoac (PEMDAS); (a+b)/c; (a+b)(c-d); mod mo dau (chan/le) → Hoat dong: may tinh chu nhat + y=3x+5 → Bay loi: keo nham vi tri long.
- luy thua bac 2/3 (A×A); ve doan khach (thuyen + cap treo); so sanh = > < mo dau; tach tan cung `mod 10` → Hoat dong: can-tin (tien banh + thua) + co may 3 the he.
- Kho: muc 6 (36 bai: P0 luy thua/lap phuong; P1 bac nhat/cau thang/nhan doi luy thua/tan cung/2CS/xoa cuoi/chuc/chia deu/chia keo; P2 PEMDAS/tich 2 tong/dong hop/chia nguyen-du/dong ho 24h/xe buyt/chuyen xe/kim 12h/caro/tong 3CS/dao 3CS; P3 da thuc/phan so .2f-SIMPLIFY/phuc hoi so bi chia).

**Bai 05 — Phép chia nguyên, chia dư và lũy thừa (Nguon L03; ma `sca_l03_*`).****
- Khoi dong "17 keo chia 5 ban" → Kham pha thuong/du; `floor(A/B)`; chan/le; boc `mod 10` + cat `floor(/10)` → Hoat dong: doi do la + vuon chu nhat + khung tranh.
- 24h `mod 24` + lich 7; giay ↔ H:M:S; tran `floor((N+K-1)/K)` → Hoat dong: marathon H:M:S + chuyen xe da ngoai + lat nen.
- Kho: muc 6 (33 bai).

### CHUONG 03: CẤU TRÚC RẼ NHÁNH & CẤU TRÚC VÒNG LẶP (Bai 06–08)

**Bai 06 — Cấu trúc rẽ nhánh (Nguon L04 + mo rong; ma `sca_l04_*`).****
- Khoi dong "mua → o, khong → di bo" → Kham pha if don/doi; long thay elif (hoc luc/taxi); BAY nhieu if doc lap → Hoat dong: ve cong vien + taxi Rua Con.
- and/or/not; tam giac 3 and; nhuan (400 hoac (4 va khong 100)); linh canh max-3 → Hoat dong: 3 que tam giac + nam nhuan + oan tu ti.
- Kho: muc 6 (37 bai, giu cum ma `l04/l05/l06` goc).

**Bai 07 — Vòng lặp for và hàm range (Nguon L05; ma `sca_l05_*`).****
- Kham pha repeat + dem tay; tong=0/tich=1/dem; duyet A..B → Hoat dong: dem nguoc ten lua + tong tu nhien.
- cuu chuong; dem uoc; tam giac sao (long mo dau) → Hoat dong: bang cuu chuong + tam giac dau sao.
- Kho: muc 6 (14 bai `sca_l05_*` nguon `pya_l07_*`).

**Bai 08 — Vòng lặp while và biến cờ (Nguon L06; ma `sca_l06_*`).****
- Khoi dong "khi nao dung choi?" → Kham pha until (lap-khi-SAI); treo vo tan → Hoat dong: gap giay mat trang + ong heo xe may.
- Flag 0/1; dung kich ban; linh canh 0 → Hoat dong: rut tham + doan so nhi phan.
- Kho: muc 6 (12 bai `sca_l06_*` nguon `pya_l08_*`).

### CHUONG 04: BÀI TOÁN SỐ HỌC & TÁCH CHỮ SỐ (Bai 09–12)

**Bai 09 — Quy luật dãy số và tam giác số (Nguon L07; ma `sca_l07_*`).****
- CSC `u1+(n-1)d`; CSN/dan dau; cuon chieu `tam=a;a=b;b=tam+b` → Hoat dong: Fibonacci + Tribonacci.
- ngoai=hang/trong=cot; ban co 0/1; Floyd + Pen: dinh nghia [Canh hoa] → xoay 360/so-canh → Hoat dong: ban co + Floyd.
- Kho: muc 6 (14 bai `sca_l07_*` nguon `pya_l09_*`).

**Bai 10 — Kỹ thuật tách chữ số và xử lý số nguyên qua vòng lặp while (Nguon L08; ma `sca_l08_*`).****
- khung `until N=0`: boc `mod 10`, cat `floor(/10)` → tong/tich khac 0; dem chan-le; max-min → Hoat dong: may dem chu so.
- `dao=dao*10+d`; BAY quen `goc=N`; Armstrong 153; digital root → Hoat dong: guong Palindrome + hop Armstrong.
- Kho: muc 6 (14 bai `sca_l08_*` nguon `pya_l10_*`).

**Bai 11 — Ước số, Bội số và Số nguyên tố (Nguon L09; ma `sca_l09_*`).****
- tai sao duyet N lag → dinh ly `i*i>n`; cap (i,N/i); chinh phuong (uoc le) → Hoat dong: may dem uoc.
- co prime; Euclid (tru/chia du) UCLN/BCNN; thua so nguyen to → Hoat dong: tham tu prime + phan tich thua so.
- Kho: muc 6 (14 bai `sca_l09_*` nguon `pya_l11_*`).

**Bai 12 — Đếm số theo quy luật và số đặc biệt (Nguon L10; ma `sca_l10_*`).****
- tru tien to `(B//K)-((A-1)//K)`; bao ham-loai tru (2 hoac 3) → Hoat dong: may dem sieu toc O(1).
- hoan hao 6=1+2+3; phong phu/thieu/song than thiet → Hoat dong: kiem tra hoan hao + doi ban than thiet.
- Kho: muc 6 (12 bai `sca_l10_*` nguon `pya_l12_*`).

### CHUONG 05: DANH SÁCH (LIST) & THỐNG KÊ (Bai 13–14)

**Bai 13 — Danh sách và thao tác cơ bản (Nguon L11; ma `sca_l11_*`).****
- tu ngan keo hien san khau; INDEX TU 1 (khac Python 0); add/delete/insert/replace/item/length/contains → Hoat dong: bang diem thi dua + xep the so.
- duyet `i=1..length`; tong/dem/tach chan-le → Hoat dong: thong ke diem + tach dong chan-le.
- Kho: muc 6 (26 bai `sca_l11_*` nguon `pya_l16_*`).

**Bai 14 — Thống kê danh sách và sắp xếp (Nguon L12; ma `sca_l12_*`).****
- linh canh max=item 1 (+vi tri); lon nhi; trung binh; unique → Hoat dong: bang vang thu khoa.
- cap ke sai → doi qua `tam`; bong bong noi dan truc quan → Hoat dong: hang doc tang dan.
- median/mode; greedy tra sua (EXTENSION); olympic bo max-min → Hoat dong: xep hang tra sua.
- Kho: muc 6 (14 bai `sca_l12_*` nguon `pya_l17_*`).

### CHUONG 06: XỬ LÝ CHUỖI KÝ TỰ (Bai 15–16)

**Bai 15 — Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự (Nguon L13; ma `sca_l13_*`).****
- vi tri tu 1; `letter/length`; loop cat chuoi con; email sau @ → Hoat dong: may do cau + rut trich domain.
- ghep nguoc phai→trai; RADAR/LEVEL; cat doi (chan); xoa K → Hoat dong: may soi Palindrome + dao chu.
- Kho: muc 6 (12 bai `sca_l13_*` nguon `pya_l13_*`; left-rotation + palindrome dai nhat = CHALLENGE).

**Bai 16 — Duyệt chuỗi, biến đổi ký tự và tách từ (Nguon L14; ma `sca_l14_*`).****
- duyet dem hoa/thuong/so + AEIOU → Hoat dong: may phan tich mat khau + dem nguyen am.
- tach tu (`tu=""` tich luy den gap cach → List); chuan hoa thua → Hoat dong: dem tu + tu dai nhat.
- Run-Length (AAAABBC→A4B2C1); Caesar dich K + giai ma → Hoat dong: nen van ban + mat thu Caesar.
- Kho: muc 6 (24 bai `sca_l14_*`, nguon giu cum `l14/l15`; EXTENSION: Run-Length/Caesar/anagram/ascii; EXCLUDE co ly do).

**Tong ket:** du an game/do hoa tuong tac — game nham nhanh (diem/xep hang/list ky luc) hoac tranh hoa van tu dong theo tham so nhap.

## 6. KHO BAI TAP CHI TIET — 287 BAI (ID chot + trace nguon)

> Quy tac ID chot (production): Ma Scratch chay theo lesson Scratch (`sca_l01`–`sca_l14` = L01–L14 Python, danh STT lai `p01..` theo Bai goc); cot Nguon giu ma Python that de trace 1-1. VIDU: `sca_l05_p04` ← nguon `pya_l07_p04`. Bai 08 giu cum nguon `l04/l05/l06` goc. Cot Tang = de xuat P0–P3, QA chot khi duyet.

### Bai 03 — Kho bai tap (25 bai, ma `sca_l01_*`)

| # | Ma Scratch | Nguon Python | Ten bai | Tang |
|---|---|---|---|---|
| 1 | `sca_l01_p01_loi_chao_robot` | `pya_l01_p01_loi_chao_robot` | Lời chào robot | P0 |
| 2 | `sca_l01_p02_cau_doi_tet` | `pya_l01_p02_cau_doi_tet` | Câu đối ngày tết | P0 |
| 3 | `sca_l01_p03_doc_in_so_nguyen` | `pya_l01_p05_doc_in_so_nguyen` | Đọc và in số nguyên | P1 |
| 4 | `sca_l01_p04_in_so_sep` | `pya_l01_p03_in_so_sep` | In số trên một hàng với sep | P1 |
| 5 | `sca_l01_p05_nhan_doi_gia_tri` | `pya_l01_p25_nhan_doi_gia_tri` | Nhân đôi giá trị | P1 |
| 6 | `sca_l01_p06_in_end_cung_dong` | `pya_l01_p19_in_end_cung_dong` | In không xuống dòng với end | P1 |
| 7 | `sca_l01_p07_hoan_doi_hai_bien` | `pya_l01_p11_hoan_doi_hai_bien` | Hoán đổi vị trí hai biến | P2 |
| 8 | `sca_l01_p08_tong_hai_so_2_dong` | `pya_l01_p21_tong_hai_so_2_dong` | Tổng hai số nguyên 2 dòng | P1 |
| 9 | `sca_l01_p09_hieu_hai_so` | `pya_l01_p22_hieu_hai_so` | Hiệu hai số nguyên | P1 |
| 10 | `sca_l01_p10_tich_hai_so` | `pya_l01_p23_tich_hai_so` | Tích hai số nguyên | P1 |
| 11 | `sca_l01_p11_cap_so_nhan_doi` | `pya_l01_p04_cap_so_nhan_doi` | Cặp số nhân đôi | P1 |
| 12 | `sca_l01_p12_tuoi_cua_be_sau_5_nam` | `pya_l01_p18_tuoi_cua_be_sau_5_nam` | Tuổi của bé sau 5 năm | P1 |
| 13 | `sca_l01_p13_chuc_sinh_nhat` | `pya_l01_p12_chuc_sinh_nhat` | Lời chúc sinh nhật cá nhân hóa | P2 |
| 14 | `sca_l01_p14_chiec_hop_hoan_doi_bi_mat` | `pya_l01_p07_chiec_hop_hoan_doi_bi_mat` | Chiếc hộp hoán đổi bí mật | P2 |
| 15 | `sca_l01_p15_tam_danh_thiep_thong_minh` | `pya_l01_p17_tam_danh_thiep_thong_minh` | Tấm danh thiếp thông minh | P2 |
| 16 | `sca_l01_p16_cua_hang_banh_ran` | `pya_l01_p06_cua_hang_banh_ran` | Cửa hàng bánh rán | P2 |
| 17 | `sca_l01_p17_phep_nhan_bang` | `pya_l01_p15_phep_nhan_bang` | In bảng phép nhân cơ bản | P2 |
| 18 | `sca_l01_p18_tong_hai_so_cung_dong` | `pya_l01_p09_tong_hai_so_cung_dong` | Tổng hai số trên cùng 1 dòng | P1 |
| 19 | `sca_l01_p19_doi_thuoc_ke_milimet` | `pya_l01_p20_doi_thuoc_ke_milimet` | Đổi thước kẻ milimet | P2 |
| 20 | `sca_l01_p20_ghep_ngay_thang_nam` | `pya_l01_p14_ghep_ngay_thang_nam` | Ghép ngày tháng năm định dạng chuẩn | P2 |
| 21 | `sca_l01_p21_doan_tau_toa_xe_ghep_so` | `pya_l01_p08_doan_tau_toa_xe_ghep_so` | Đoàn tàu toa xe ghép số | P2 |
| 22 | `sca_l01_p22_chenh_lech_tuoi` | `pya_l01_p16_chenh_lech_tuoi` | Chênh lệch tuổi của hai anh em | P2 |
| 23 | `sca_l01_p23_bon_phep_tinh` | `pya_l01_p13_bon_phep_tinh` | Bốn phép tính đồng thời | P3 |
| 24 | `sca_l01_p24_co_may_thoi_gian_3_the_he` | `pya_l01_p10_co_may_thoi_gian_3_the_he` | Cỗ máy thời gian 3 thế hệ | P3 |
| 25 | `sca_l01_p25_ve_tham_quan_chua_huong` | `pya_l01_p24_ve_tham_quan_chua_huong` | Vé tham quan chùa hương | P3 |

### Bai 04 — Kho bai tap (36 bai, ma `sca_l02_*`)

| # | Ma Scratch | Nguon Python | Ten bai | Tang |
|---|---|---|---|---|
| 1 | `sca_l02_p01_luy_thua_bac_hai` | `pya_l02_p02_luy_thua_bac_hai` | Lũy thừa bậc hai | P0 |
| 2 | `sca_l02_p02_lap_phuong` | `pya_l02_p03_lap_phuong` | Lập phương của một số | P0 |
| 3 | `sca_l02_p03_chu_so_tan_cung` | `pya_l02_p04_chu_so_tan_cung` | Lấy chữ số tận cùng | P1 |
| 4 | `sca_l02_p04_hai_chu_so_cuoi` | `pya_l02_p09_hai_chu_so_cuoi` | Lấy hai chữ số tận cùng | P1 |
| 5 | `sca_l02_p05_bieu_thuc_bac_nhat` | `pya_l02_p11_bieu_thuc_bac_nhat` | Giá trị biểu thức bậc nhất | P1 |
| 6 | `sca_l02_p06_xoa_chu_so_cuoi` | `pya_l02_p25_xoa_chu_so_cuoi` | Xóa chữ số tận cùng | P1 |
| 7 | `sca_l02_p07_xep_ban_hoc` | `pya_l02_p28_xep_ban_hoc` | Xếp hàng vào bàn học | P2 |
| 8 | `sca_l02_p08_luy_thua_cau_thang` | `pya_l02_p13_luy_thua_cau_thang` | Lũy thừa cầu thang | P1 |
| 9 | `sca_l02_p09_dong_hop_banh` | `pya_l02_p07_dong_hop_banh` | Đóng hộp bánh ngọt | P2 |
| 10 | `sca_l02_p10_chu_so_hang_chuc` | `pya_l02_p10_chu_so_hang_chuc` | Chữ số hàng chục | P1 |
| 11 | `sca_l02_p11_doi_phut_ra_gio_phut` | `pya_l02_p14_doi_phut_ra_gio_phut` | Đổi phút ra giờ phút | P2 |
| 12 | `sca_l02_p12_nhan_doi_luy_thua` | `pya_l02_p22_nhan_doi_luy_thua` | Nhân đôi lũy thừa | P1 |
| 13 | `sca_l02_p13_vong_chay_dien_kinh` | `pya_l02_p27_vong_chay_dien_kinh` | Vòng chạy điền kinh | P2 |
| 14 | `sca_l02_p14_bong_den_vien_bien_hieu` | `pya_l02_p05_bong_den_vien_bien_hieu` | Bóng đèn viền biển hiệu | P2 |
| 15 | `sca_l02_p15_du_quay_vong_tron` | `pya_l02_p16_du_quay_vong_tron` | Đu quay vòng tròn | P2 |
| 16 | `sca_l02_p16_so_keo_con_thua` | `pya_l02_p23_so_keo_con_thua` | Số kẹo còn thừa | P2 |
| 17 | `sca_l02_p17_phuc_hoi_so_bi_chia` | `pya_l02_p20_phuc_hoi_so_bi_chia` | Bất biến chia kẹo và phục hồi số bị chia | P3 |
| 18 | `sca_l02_p18_da_thuc_bac_hai` | `pya_l02_p32_da_thuc_bac_hai` | Đa thức bậc hai | P3 |
| 19 | `sca_l02_p19_trong_cay_dai_lo` | `pya_l02_p26_trong_cay_dai_lo` | Trồng cây đại lộ | P2 |
| 20 | `sca_l02_p20_gia_tri_bieu_thuc_pemdas` | `pya_l02_p15_gia_tri_bieu_thuc_pemdas` | Giá trị biểu thức PEMDAS | P2 |
| 21 | `sca_l02_p21_doi_gio_ra_phut_giay` | `pya_l02_p24_doi_gio_ra_phut_giay` | Đổi giờ ra phút giây | P2 |
| 22 | `sca_l02_p22_tach_chu_so_tan_cung` | `pya_l02_p29_tach_chu_so_tan_cung` | Tách chữ số tận cùng | P1 |
| 23 | `sca_l02_p23_dao_nguoc_so_2_chu_so` | `pya_l02_p30_dao_nguoc_so_2_chu_so` | Đảo ngược số 2 chữ số | P3 |
| 24 | `sca_l02_p24_tich_hai_tong` | `pya_l02_p33_tich_hai_tong` | Biểu thức có dấu ngoặc | P2 |
| 25 | `sca_l02_p25_dong_ho_24h` | `pya_l02_p34_dong_ho_24h` | Đồng hồ 24 giờ | P3 |
| 26 | `sca_l02_p26_ngay_trong_tuan` | `pya_l02_p35_ngay_trong_tuan` | Ngày trong tuần | P2 |
| 27 | `sca_l02_p27_chia_deu_banh_quy` | `pya_l02_p01_chia_deu_banh_quy` | Chia đều bánh quy | P1 |
| 28 | `sca_l02_p28_xe_buyt_cho_hoc_sinh` | `pya_l02_p31_xe_buyt_cho_hoc_sinh` | Xe buýt chở học sinh | P3 |
| 29 | `sca_l02_p29_chuyen_xe_hoc_sinh` | `pya_l02_p19_chuyen_xe_hoc_sinh` | Tính số chuyến xe cần thiết | P3 |
| 30 | `sca_l02_p30_chia_nguyen_chia_du` | `pya_l02_p21_chia_nguyen_chia_du` | Phép chia nguyên và chia dư cơ bản | P2 |
| 31 | `sca_l02_p31_kim_dong_ho_12_gio` | `pya_l02_p08_kim_dong_ho_12_gio` | Kim đồng hồ 12 giờ | P2 |
| 32 | `sca_l02_p32_chia_keo_hoc_sinh` | `pya_l02_p06_chia_keo_hoc_sinh` | Chia kẹo cho các bạn | P1 |
| 33 | `sca_l02_p33_ban_co_caro_vo_tan` | `pya_l02_p12_ban_co_caro_vo_tan` | Bàn cờ Ca-rô vô tận | P3 |
| 34 | `sca_l02_p34_tong_ba_chu_so` | `pya_l02_p17_tong_ba_chu_so` | Tổng các chữ số của số có 3 chữ số | P2 |
| 35 | `sca_l02_p35_phan_so_dai_so` | `pya_l02_p36_phan_so_dai_so` | Tính phân số đại số | P3 |
| 36 | `sca_l02_p36_so_dao_nguoc_3_chu_so` | `pya_l02_p18_so_dao_nguoc_3_chu_so` | Số đảo ngược 3 chữ số | P2 |

### Bai 05 — Kho bai tap (33 bai, ma `sca_l03_*`)

| # | Ma Scratch | Nguon Python | Ten bai | Tang |
|---|---|---|---|---|
| 1 | `sca_l03_p01_doi_do_la_sang_tien_viet` | `pya_l03_p31_doi_do_la_sang_tien_viet` | Đổi đô la sang tiền việt | P0 |
| 2 | `sca_l03_p02_hinh_vuong` | `pya_l03_p01_hinh_vuong` | Chu vi và diện tích hình vuông | P1 |
| 3 | `sca_l03_p03_doi_don_vi_dai` | `pya_l03_p06_doi_don_vi_dai` | Đổi mét sang centimet và milimet | P0 |
| 4 | `sca_l03_p04_khung_tranh_hinh_vuong` | `pya_l03_p20_khung_tranh_hinh_vuong` | Khung tranh hình vuông | P1 |
| 5 | `sca_l03_p05_doi_do_c_sang_do_f` | `pya_l03_p14_doi_do_c_sang_do_f` | Đổi độ C sang độ F | P1 |
| 6 | `sca_l03_p06_canh_con_lai_cua_hinh_chu_nhat` | `pya_l03_p04_canh_con_lai_cua_hinh_chu_nhat` | Cạnh còn lại của hình chữ nhật | P2 |
| 7 | `sca_l03_p07_dien_tich_tam_giac_vuong` | `pya_l03_p11_dien_tich_tam_giac_vuong` | Diện tích tam giác vuông | P1 |
| 8 | `sca_l03_p08_chu_vi_tam_giac_abc` | `pya_l03_p21_chu_vi_tam_giac_abc` | Chu vi tam giác ABC | P1 |
| 9 | `sca_l03_p09_the_tich_hop_chu_nhat` | `pya_l03_p30_the_tich_hop_chu_nhat` | Thể tích hộp chữ nhật | P1 |
| 10 | `sca_l03_p10_manh_vuon_chu_nhat` | `pya_l03_p19_manh_vuon_chu_nhat` | Mảnh vườn chữ nhật | P1 |
| 11 | `sca_l03_p11_dien_tich_bon_hoa_chu_thap` | `pya_l03_p10_dien_tich_bon_hoa_chu_thap` | Diện tích bồn hoa chữ thập | P2 |
| 12 | `sca_l03_p12_thuan_di_gap_anh` | `pya_l03_p08_thuan_di_gap_anh` | Thuận đi gặp ánh | P2 |
| 13 | `sca_l03_p13_ho_ca_sau_va_dao_nho` | `pya_l03_p23_ho_ca_sau_va_dao_nho` | Hồ cá sấu và đảo nhỏ | P2 |
| 14 | `sca_l03_p14_chu_vi_tam_giac` | `pya_l03_p03_chu_vi_tam_giac` | Chu vi hình tam giác | P1 |
| 15 | `sca_l03_p15_phut_sang_gio_phut` | `pya_l03_p09_phut_sang_gio_phut` | Đổi phút sang giờ và phút | P2 |
| 16 | `sca_l03_p16_tinh_van_toc_lam_tron` | `pya_l03_p33_tinh_van_toc_lam_tron` | Tính vận tốc làm tròn | P3 |
| 17 | `sca_l03_p17_lat_gach_san_truong` | `pya_l03_p25_lat_gach_san_truong` | Lát gạch sân trường | P2 |
| 18 | `sca_l03_p18_rao_quanh_vuon_hoa_co_cua` | `pya_l03_p27_rao_quanh_vuon_hoa_co_cua` | Rào quanh vườn hoa có cửa | P3 |
| 19 | `sca_l03_p19_hinh_chu_nhat` | `pya_l03_p02_hinh_chu_nhat` | Chu vi và diện tích hình chữ nhật | P1 |
| 20 | `sca_l03_p20_doi_khoi_luong` | `pya_l03_p07_doi_khoi_luong` | Đổi tạ và yến sang kilogram | P1 |
| 21 | `sca_l03_p21_hang_rao_manh_dat` | `pya_l03_p32_hang_rao_manh_dat` | Hàng rào quanh mảnh đất | P2 |
| 22 | `sca_l03_p22_chay_bo_gap_nhau` | `pya_l03_p18_chay_bo_gap_nhau` | Bài toán chạy bộ hai người ngược chiều | P2 |
| 23 | `sca_l03_p23_dien_tich_tam_giac_vuong` | `pya_l03_p22_dien_tich_tam_giac_vuong` | Diện tích tam giác vuông | P1 |
| 24 | `sca_l03_p24_doi_sang_tong_giay` | `pya_l03_p29_doi_sang_tong_giay` | Đổi giờ - phút - giây sang tổng số giây | P2 |
| 25 | `sca_l03_p25_son_tuong_phong` | `pya_l03_p17_son_tuong_phong` | Tính tiền mua sơn quét tường | P2 |
| 26 | `sca_l03_p26_dien_tich_hinh_thang` | `pya_l03_p05_dien_tich_hinh_thang` | Diện tích hình thang | P2 |
| 27 | `sca_l03_p27_van_toc_trung_binh` | `pya_l03_p26_van_toc_trung_binh` | Tính vận tốc trung bình | P2 |
| 28 | `sca_l03_p28_doi_giay_sang_gio_phut_giay` | `pya_l03_p24_doi_giay_sang_gio_phut_giay` | Đổi giây sang giờ phút giây | P3 |
| 29 | `sca_l03_p29_khoang_cach_thoi_gian` | `pya_l03_p12_khoang_cach_thoi_gian` | Khoảng thời gian giữa hai thời điểm trong ngày | P3 |
| 30 | `sca_l03_p30_lat_gach_nen_nha` | `pya_l03_p15_lat_gach_nen_nha` | Lát nền phòng học | P3 |
| 31 | `sca_l03_p31_doi_giay_sang_gio_phut_giay` | `pya_l03_p28_doi_giay_sang_gio_phut_giay` | Đổi tổng số giây sang giờ, phút, giây | P3 |
| 32 | `sca_l03_p32_diem_trung_binh` | `pya_l03_p13_diem_trung_binh` | Điểm trung bình môn học | P2 |
| 33 | `sca_l03_p33_loi_di_quanh_ho` | `pya_l03_p16_loi_di_quanh_ho` | Diện tích lối đi quanh hồ nước | P3 |

### Bai 06 — Kho bai tap (37 bai, ma `sca_l04_*`)

| # | Ma Scratch | Nguon Python | Ten bai | Tang |
|---|---|---|---|---|
| 1 | `sca_l04_p01_so_lon_nhat_trong_hai_so` | `pya_l04_p04_so_lon_nhat_trong_hai_so` | Số lớn nhất trong hai số | P0 |
| 2 | `sca_l04_p02_tri_tuyet_doi_cua_mot_so` | `pya_l04_p09_tri_tuyet_doi_cua_mot_so` | Trị tuyệt đối của một số | P0 |
| 3 | `sca_l04_p03_ve_vao_cong_vien` | `pya_l04_p02_ve_vao_cong_vien` | Vé vào công viên | P1 |
| 4 | `sca_l04_p04_kiem_tra_so_chan_le` | `pya_l04_p01_kiem_tra_so_chan_le` | Kiểm tra số chẵn lẻ | P0 |
| 5 | `sca_l04_p05_dien_phep_tinh_lon_nhat` | `pya_l04_p06_dien_phep_tinh_lon_nhat` | Điền phép tính lớn nhất | P1 |
| 6 | `sca_l04_p06_giam_gia_sieu_thi` | `pya_l04_p07_giam_gia_sieu_thi` | Giảm giá siêu thị | P1 |
| 7 | `sca_l04_p07_ngay_nghi_cuoi_tuan` | `pya_l06_p03_ngay_nghi_cuoi_tuan` | Ngày nghỉ cuối tuần | P1 |
| 8 | `sca_l04_p08_ai_cao_hon` | `pya_l04_p03_ai_cao_hon` | Ai cao hơn? | P1 |
| 9 | `sca_l04_p09_so_chan_co_hai_chu_so` | `pya_l06_p01_so_chan_co_hai_chu_so` | Số chẵn có hai chữ số | P2 |
| 10 | `sca_l04_p10_mario_cuu_cong_chua` | `pya_l05_p06_mario_cuu_cong_chua` | Mario cứu công chúa | P2 |
| 11 | `sca_l04_p11_tien_dien_bac_thang` | `pya_l06_p13_tien_dien_bac_thang` | Tiền điện bậc thang | P3 |
| 12 | `sca_l04_p12_bac_tho_moc_cat_go` | `pya_l04_p10_bac_tho_moc_cat_go` | Bác thợ mộc cắt gỗ | P1 |
| 13 | `sca_l04_p13_diem_nam_trong_hinh_chu_nhat` | `pya_l06_p04_diem_nam_trong_hinh_chu_nhat` | Điểm nằm trong hình chữ nhật | P2 |
| 14 | `sca_l04_p14_boi_chung_cua_3_va_5` | `pya_l06_p02_boi_chung_cua_3_va_5` | Bội chung của 3 và 5 | P2 |
| 15 | `sca_l04_p15_ba_canh_tam_giac_hop_le` | `pya_l06_p05_ba_canh_tam_giac_hop_le` | Ba cạnh tam giác hợp lệ | P2 |
| 16 | `sca_l04_p16_kiem_tra_nam_nhuan` | `pya_l06_p06_kiem_tra_nam_nhuan` | Kiểm tra năm nhuận | P2 |
| 17 | `sca_l04_p17_rut_the_may_man` | `pya_l06_p09_rut_the_may_man` | Rút thẻ may mắn | P2 |
| 18 | `sca_l04_p18_so_lon_nhat_trong_ba_so` | `pya_l05_p03_so_lon_nhat_trong_ba_so` | Số lớn nhất trong ba số | P2 |
| 19 | `sca_l04_p19_dau_cua_so_nguyen` | `pya_l05_p02_dau_cua_so_nguyen` | Dấu của số nguyên | P2 |
| 20 | `sca_l04_p20_thuan_di_tim_anh_da_van_toc` | `pya_l05_p09_thuan_di_tim_anh_da_van_toc` | Thuận đi tìm ánh đa vận tốc | P3 |
| 21 | `sca_l04_p21_cua_hang_banh_bot_loc_khuyen_mai` | `pya_l05_p11_cua_hang_banh_bot_loc_khuyen_mai` | Cửa hàng bánh bột lọc khuyến mãi | P2 |
| 22 | `sca_l04_p22_canh_thu_tu_hinh_chu_nhat` | `pya_l04_p11_canh_thu_tu_hinh_chu_nhat` | Cạnh thứ tư hình chữ nhật | P2 |
| 23 | `sca_l04_p23_chia_keo_cong_bang` | `pya_l04_p05_chia_keo_cong_bang` | Chia kẹo công bằng | P1 |
| 24 | `sca_l04_p24_thu_may_trong_tuan` | `pya_l05_p10_thu_may_trong_tuan` | Thứ mấy trong tuần? | P2 |
| 25 | `sca_l04_p25_phan_loai_tam_giac` | `pya_l05_p08_phan_loai_tam_giac` | Phân loại tam giác | P2 |
| 26 | `sca_l04_p26_tinh_cuoc_taxi_bac_thang` | `pya_l05_p07_tinh_cuoc_taxi_bac_thang` | Tính cước taxi bậc thang | P3 |
| 27 | `sca_l04_p27_xep_loai_hoc_luc` | `pya_l05_p04_xep_loai_hoc_luc` | Xếp loại học lực | P2 |
| 28 | `sca_l04_p28_so_ngay_trong_thang` | `pya_l06_p07_so_ngay_trong_thang` | Số ngày trong tháng | P3 |
| 29 | `sca_l04_p29_cap_doi_cung_dau_hay_trai_dau` | `pya_l06_p11_cap_doi_cung_dau_hay_trai_dau` | Cặp đôi cùng dấu hay trái dấu | P2 |
| 30 | `sca_l04_p30_cap_so_bang_nhau_hay_khac` | `pya_l04_p08_cap_so_bang_nhau_hay_khac` | Cặp số bằng nhau hay khác? | P1 |
| 31 | `sca_l04_p31_tro_choi_oan_tu_ti` | `pya_l04_p12_tro_choi_oan_tu_ti` | Trò chơi oẳn tù tì | P3 |
| 32 | `sca_l04_p32_den_giao_thong_nga_tu` | `pya_l05_p01_den_giao_thong_nga_tu` | Đèn giao thông ngã tư | P1 |
| 33 | `sca_l04_p33_giao_nhau_cua_hai_doan_thang` | `pya_l06_p12_giao_nhau_cua_hai_doan_thang` | Giao nhau của hai đoạn thẳng | P3 |
| 34 | `sca_l04_p34_ve_gui_xe_ben_bai` | `pya_l05_p05_ve_gui_xe_ben_bai` | Vé gửi xe bến bãi | P2 |
| 35 | `sca_l04_p35_bon_mua_trong_nam` | `pya_l05_p12_bon_mua_trong_nam` | Bốn mùa trong năm | P1 |
| 36 | `sca_l04_p36_tam_giac_vuong_hay_khong` | `pya_l06_p08_tam_giac_vuong_hay_khong` | Tam giác vuông hay không? | P2 |
| 37 | `sca_l04_p37_ngay_ke_tiep_trong_nam` | `pya_l06_p10_ngay_ke_tiep_trong_nam` | Ngày kế tiếp trong năm | P3 |

### Bai 07 — Kho bai tap (14 bai, ma `sca_l05_*`)

| # | Ma Scratch | Nguon Python | Ten bai | Tang |
|---|---|---|---|---|
| 1 | `sca_l05_p01_tong_day_sieu_lon_khong_lap` | `pya_l07_p14_tong_day_sieu_lon_khong_lap` | Tổng dãy siêu lớn không lặp | P3 |
| 2 | `sca_l05_p02_dem_sao_len_troi` | `pya_l07_p01_dem_sao_len_troi` | Đếm sao lên trời | P0 |
| 3 | `sca_l05_p03_dem_nguoc_phong_ten_lua` | `pya_l07_p02_dem_nguoc_phong_ten_lua` | Đếm ngược phóng tên lửa | P0 |
| 4 | `sca_l05_p04_tong_cac_so_tu_nhien` | `pya_l07_p03_tong_cac_so_tu_nhien` | Tổng các số tự nhiên | P1 |
| 5 | `sca_l05_p05_tam_giac_vuong_dau_sao` | `pya_l07_p13_tam_giac_vuong_dau_sao` | Tam giác vuông dấu sao | P2 |
| 6 | `sca_l05_p06_hang_cot_dau_sao` | `pya_l07_p12_hang_cot_dau_sao` | Hàng cột dấu sao | P2 |
| 7 | `sca_l05_p07_tinh_giai_thua_n` | `pya_l07_p07_tinh_giai_thua_n` | Tính giai thừa | P1 |
| 8 | `sca_l05_p08_tong_binh_phuong` | `pya_l07_p10_tong_binh_phuong` | Tổng bình phương | P3 |
| 9 | `sca_l05_p09_bang_cuu_chuong` | `pya_l07_p04_bang_cuu_chuong` | Bảng cửu chương | P1 |
| 10 | `sca_l05_p10_tong_so_chan_trong_doan` | `pya_l07_p05_tong_so_chan_trong_doan` | Tổng số chẵn trong đoạn | P2 |
| 11 | `sca_l05_p11_doc_sach_moi_ngay` | `pya_l07_p11_doc_sach_moi_ngay` | Đọc sách mỗi ngày | P2 |
| 12 | `sca_l05_p12_day_so_cach_deu` | `pya_l07_p08_day_so_cach_deu` | Dãy số cách đều | P2 |
| 13 | `sca_l05_p13_dem_boi_so_cua_k` | `pya_l07_p06_dem_boi_so_cua_k` | Đếm bội số của K | P2 |
| 14 | `sca_l05_p14_tim_uoc_so_cua_n` | `pya_l07_p09_tim_uoc_so_cua_n` | Tìm ước số của N | P3 |

### Bai 08 — Kho bai tap (12 bai, ma `sca_l06_*`)

| # | Ma Scratch | Nguon Python | Ten bai | Tang |
|---|---|---|---|---|
| 1 | `sca_l06_p01_tim_luy_thua_cua_2_lon_hon_n` | `pya_l08_p08_tim_luy_thua_cua_2_lon_hon_n` | Tìm lũy thừa của 2 lớn hơn N | P0 |
| 2 | `sca_l06_p02_gap_doi_to_giay_len_mat_trang` | `pya_l08_p06_gap_doi_to_giay_len_mat_trang` | Gấp đôi tờ giấy lên mặt trăng | P1 |
| 3 | `sca_l06_p03_ong_heo_mua_xe_may` | `pya_l08_p07_ong_heo_mua_xe_may` | Ống heo mua xe máy | P1 |
| 4 | `sca_l06_p04_dem_so_luong_chu_so_cua_n` | `pya_l08_p10_dem_so_luong_chu_so_cua_n` | Đếm số lượng chữ số của N | P1 |
| 5 | `sca_l06_p05_dem_xuoi_bang_while` | `pya_l08_p01_dem_xuoi_bang_while` | Đếm xuôi bằng while | P0 |
| 6 | `sca_l06_p06_nhap_so_den_khi_gap_so_0` | `pya_l08_p03_nhap_so_den_khi_gap_so_0` | Nhập số đến khi gặp số 0 | P2 |
| 7 | `sca_l06_p07_tong_day_so_ket_thuc_bang_0` | `pya_l08_p04_tong_day_so_ket_thuc_bang_0` | Tổng dãy số kết thúc bằng 0 | P2 |
| 8 | `sca_l06_p08_tro_choi_doan_so_nhi_phan` | `pya_l08_p11_tro_choi_doan_so_nhi_phan` | Trò chơi đoán số nhị phân | P3 |
| 9 | `sca_l06_p09_rut_tham_den_khi_trung` | `pya_l08_p02_rut_tham_den_khi_trung` | Rút thăm đến khi trúng | P2 |
| 10 | `sca_l06_p10_day_so_collatz_3n_1` | `pya_l08_p12_day_so_collatz_3n_1` | Dãy số Collatz (3n + 1) | P3 |
| 11 | `sca_l06_p11_dem_so_chan_den_khi_gap_0` | `pya_l08_p05_dem_so_chan_den_khi_gap_0` | Đếm số chẵn đến khi gặp 0 | P2 |
| 12 | `sca_l06_p12_chu_oc_sen_leo_cot_co` | `pya_l08_p09_chu_oc_sen_leo_cot_co` | Chú ốc sên leo cột cờ | P3 |

### Bai 09 — Kho bai tap (14 bai, ma `sca_l07_*`)

| # | Ma Scratch | Nguon Python | Ten bai | Tang |
|---|---|---|---|---|
| 1 | `sca_l07_p01_trao_doi_hai_chiec_coc` | `pya_l09_p01_trao_doi_hai_chiec_coc` | Tráo đổi hai chiếc cốc | P3 |
| 2 | `sca_l07_p02_so_hang_day_cap_so_cong` | `pya_l09_p03_so_hang_day_cap_so_cong` | Số hạng dãy cấp số cộng | P0 |
| 3 | `sca_l07_p03_so_fibonacci_thu_n` | `pya_l09_p04_so_fibonacci_thu_n` | Số Fibonacci thứ N | P1 |
| 4 | `sca_l07_p04_tong_tich_hai_so_lien_nhau` | `pya_l09_p06_tong_tich_hai_so_lien_nhau` | Tổng tích hai số liền nhau | P1 |
| 5 | `sca_l07_p05_tam_giac_so_don_gian` | `pya_l09_p08_tam_giac_so_don_gian` | Tam giác số đơn giản | P2 |
| 6 | `sca_l07_p06_ma_tran_so_ban_co_dan_xen` | `pya_l09_p12_ma_tran_so_ban_co_dan_xen` | Ma trận số bàn cờ đan xen | P2 |
| 7 | `sca_l07_p07_day_so_nhan_doi` | `pya_l09_p02_day_so_nhan_doi` | Dãy số nhân đôi | P0 |
| 8 | `sca_l07_p08_day_so_dan_dau` | `pya_l09_p05_day_so_dan_dau` | Dãy số đan dấu | P0 |
| 9 | `sca_l07_p09_tam_giac_sao_can` | `pya_l09_p09_tam_giac_sao_can` | Tam giác sao cân | P2 |
| 10 | `sca_l07_p10_day_so_tam_giac_triangular_numbers` | `pya_l09_p10_day_so_tam_giac_triangular_numbers` | Dãy số tam giác (triangular numbers) | P2 |
| 11 | `sca_l07_p11_tim_vi_tri_trong_day_tu_nhien_dai` | `pya_l09_p14_tim_vi_tri_trong_day_tu_nhien_dai` | Tìm vị trí trong dãy tự nhiên dài | P3 |
| 12 | `sca_l07_p12_tam_giac_floyd` | `pya_l09_p13_tam_giac_floyd` | Tam giác Floyd | P3 |
| 13 | `sca_l07_p13_day_so_boi_ba_boi_nam` | `pya_l09_p07_day_so_boi_ba_boi_nam` | Dãy số bội ba bội năm | P2 |
| 14 | `sca_l07_p14_day_so_tribonacci` | `pya_l09_p11_day_so_tribonacci` | Dãy số Tribonacci | P1 |

### Bai 10 — Kho bai tap (14 bai, ma `sca_l08_*`)

| # | Ma Scratch | Nguon Python | Ten bai | Tang |
|---|---|---|---|---|
| 1 | `sca_l08_p01_lay_chu_so_don_vi_chuc` | `pya_l10_p01_lay_chu_so_don_vi_chuc` | Lấy chữ số đơn vị & chục | P0 |
| 2 | `sca_l08_p02_tong_chu_so_cua_so_3_chu_so` | `pya_l10_p02_tong_chu_so_cua_so_3_chu_so` | Tổng chữ số của số 3 chữ số | P0 |
| 3 | `sca_l08_p03_tong_cac_chu_so_cua_n` | `pya_l10_p03_tong_cac_chu_so_cua_n` | Tổng các chữ số của N | P1 |
| 4 | `sca_l08_p04_so_dao_nguoc` | `pya_l10_p08_so_dao_nguoc` | Số đảo ngược | P2 |
| 5 | `sca_l08_p05_tich_cac_chu_so_khac_khong` | `pya_l10_p05_tich_cac_chu_so_khac_khong` | Tích các chữ số khác không | P2 |
| 6 | `sca_l08_p06_dem_so_luong_chu_so` | `pya_l10_p04_dem_so_luong_chu_so` | Đếm số lượng chữ số | P1 |
| 7 | `sca_l08_p07_kiem_tra_so_doi_xung_palindrome` | `pya_l10_p09_kiem_tra_so_doi_xung_palindrome` | Kiểm tra số đối xứng (palindrome) | P2 |
| 8 | `sca_l08_p08_can_bac_so_hoc_digital_root` | `pya_l10_p13_can_bac_so_hoc_digital_root` | Căn bậc số học (digital root) | P3 |
| 9 | `sca_l08_p09_chu_so_lon_nhat_nho_nhat` | `pya_l10_p07_chu_so_lon_nhat_nho_nhat` | Chữ số lớn nhất & nhỏ nhất | P2 |
| 10 | `sca_l08_p10_so_may_man_chua_so_7` | `pya_l10_p11_so_may_man_chua_so_7` | Số may mắn chứa số 7 | P3 |
| 11 | `sca_l08_p11_dem_chu_so_chan_va_le` | `pya_l10_p06_dem_chu_so_chan_va_le` | Đếm chữ số chẵn và lẻ | P1 |
| 12 | `sca_l08_p12_so_tang_giam_dep` | `pya_l10_p14_so_tang_giam_dep` | Số tăng giảm đẹp | P2 |
| 13 | `sca_l08_p13_so_toan_chan_hoac_toan_le` | `pya_l10_p10_so_toan_chan_hoac_toan_le` | Số toàn chẵn hoặc toàn lẻ | P3 |
| 14 | `sca_l08_p14_dem_so_luong_so_doi_xung_trong_doan` | `pya_l10_p12_dem_so_luong_so_doi_xung_trong_doan` | Đếm số lượng số đối xứng trong đoạn | P3 |

### Bai 11 — Kho bai tap (14 bai, ma `sca_l09_*`)

| # | Ma Scratch | Nguon Python | Ten bai | Tang |
|---|---|---|---|---|
| 1 | `sca_l09_p01_uoc_chung_lon_nhat_bcnn` | `pya_l11_p06_uoc_chung_lon_nhat_bcnn` | Ước chung lớn nhất & BCNN | P3 |
| 2 | `sca_l09_p02_dem_so_luong_uoc_so` | `pya_l11_p02_dem_so_luong_uoc_so` | Đếm số lượng ước số | P0 |
| 3 | `sca_l09_p03_tinh_tong_cac_uoc_so` | `pya_l11_p03_tinh_tong_cac_uoc_so` | Tính tổng các ước số | P1 |
| 4 | `sca_l09_p04_hai_so_nguyen_to_cung_nhau` | `pya_l11_p10_hai_so_nguyen_to_cung_nhau` | Hai số nguyên tố cùng nhau | P2 |
| 5 | `sca_l09_p05_liet_ke_tat_ca_uoc_so` | `pya_l11_p01_liet_ke_tat_ca_uoc_so` | Liệt kê tất cả ước số | P1 |
| 6 | `sca_l09_p06_dem_uoc_chan_cua_n` | `pya_l11_p07_dem_uoc_chan_cua_n` | Đếm ước chẵn của N | P2 |
| 7 | `sca_l09_p07_tim_uoc_so_lon_thu_hai` | `pya_l11_p08_tim_uoc_so_lon_thu_hai` | Tìm ước số lớn thứ hai | P2 |
| 8 | `sca_l09_p08_kiem_tra_so_chinh_phuong` | `pya_l11_p05_kiem_tra_so_chinh_phuong` | Kiểm tra số chính phương | P0 |
| 9 | `sca_l09_p09_phan_tich_ra_thua_so_nguyen_to` | `pya_l11_p13_phan_tich_ra_thua_so_nguyen_to` | Phân tích ra thừa số nguyên tố | P2 |
| 10 | `sca_l09_p10_kiem_tra_so_nguyen_to` | `pya_l11_p04_kiem_tra_so_nguyen_to` | Kiểm tra số nguyên tố | P1 |
| 11 | `sca_l09_p11_dem_so_nguyen_to_trong_doan` | `pya_l11_p09_dem_so_nguyen_to_trong_doan` | Đếm số nguyên tố trong đoạn | P2 |
| 12 | `sca_l09_p12_tim_so_co_dung_3_uoc_so` | `pya_l11_p14_tim_so_co_dung_3_uoc_so` | Tìm số có đúng 3 ước số | P3 |
| 13 | `sca_l09_p13_so_sieu_nguyen_to_super_prime` | `pya_l11_p12_so_sieu_nguyen_to_super_prime` | Số siêu nguyên tố (super prime) | P3 |
| 14 | `sca_l09_p14_cap_so_nguyen_to_sinh_doi` | `pya_l11_p11_cap_so_nguyen_to_sinh_doi` | Cặp số nguyên tố sinh đôi | P3 |

### Bai 12 — Kho bai tap (12 bai, ma `sca_l10_*`)

| # | Ma Scratch | Nguon Python | Ten bai | Tang |
|---|---|---|---|---|
| 1 | `sca_l10_p01_dem_so_chia_het_cho_k` | `pya_l12_p01_dem_so_chia_het_cho_k` | Đếm số chia hết cho K | P0 |
| 2 | `sca_l10_p02_dem_so_chia_het_cho_2_hoac_3` | `pya_l12_p07_dem_so_chia_het_cho_2_hoac_3` | Đếm số chia hết cho 2 hoặc 3 | P1 |
| 3 | `sca_l10_p03_dem_so_le_trong_doan` | `pya_l12_p02_dem_so_le_trong_doan` | Đếm số lẻ trong đoạn | P0 |
| 4 | `sca_l10_p04_dem_boi_cua_3_nhung_khong_chia_het_cho_5` | `pya_l12_p06_dem_boi_cua_3_nhung_khong_chia_het_cho_5` | Đếm bội của 3 nhưng không chia hết cho 5 | P1 |
| 5 | `sca_l10_p05_so_armstrong_ba_chu_so` | `pya_l12_p04_so_armstrong_ba_chu_so` | Số Armstrong ba chữ số | P2 |
| 6 | `sca_l10_p06_so_tu_man_narcissistic_number_k_chu_so` | `pya_l12_p12_so_tu_man_narcissistic_number_k_chu_so` | Số tự mãn (Narcissistic number K chữ số) | P2 |
| 7 | `sca_l10_p07_dem_so_khong_chua_chu_so_0` | `pya_l12_p10_dem_so_khong_chua_chu_so_0` | Đếm số không chứa chữ số 0 | P1 |
| 8 | `sca_l10_p08_kiem_tra_so_hoan_hao` | `pya_l12_p03_kiem_tra_so_hoan_hao` | Kiểm tra số hoàn hảo | P3 |
| 9 | `sca_l10_p09_dem_so_chinh_phuong_trong_doan` | `pya_l12_p11_dem_so_chinh_phuong_trong_doan` | Đếm số chính phương trong đoạn | P2 |
| 10 | `sca_l10_p10_tim_tat_ca_so_hoan_hao_nho_hon_n` | `pya_l12_p05_tim_tat_ca_so_hoan_hao_nho_hon_n` | Tìm tất cả số hoàn hảo nhỏ hơn N | P3 |
| 11 | `sca_l10_p11_so_phong_phu_abundant_number` | `pya_l12_p09_so_phong_phu_abundant_number` | Số phong phú (abundant number) | P3 |
| 12 | `sca_l10_p12_cap_so_than_thiet` | `pya_l12_p08_cap_so_than_thiet` | Cặp số thân thiết | P3 |

### Bai 13 — Kho bai tap (26 bai, ma `sca_l11_*`)

| # | Ma Scratch | Nguon Python | Ten bai | Tang |
|---|---|---|---|---|
| 1 | `sca_l11_p01_thuong_doc_sach` | `pya_l16_p23_thuong_doc_sach` | Thưởng đọc sách | P1 |
| 2 | `sca_l11_p02_so_ghe_doi_xung` | `pya_l16_p21_so_ghe_doi_xung` | Số ghế đối xứng | P2 |
| 3 | `sca_l11_p03_tim_vi_tri_dau_tien_cua_x` | `pya_l16_p08_tim_vi_tri_dau_tien_cua_x` | Tìm vị trí đầu tiên của X | P2 |
| 4 | `sca_l11_p04_nhap_day_so_in_phan_tu_dau_cuoi` | `pya_l16_p01_nhap_day_so_in_phan_tu_dau_cuoi` | Nhập dãy số & in phần tử đầu - cuối | P1 |
| 5 | `sca_l11_p05_tinh_tong_cac_phan_tu_trong_day` | `pya_l16_p03_tinh_tong_cac_phan_tu_trong_day` | Tính tổng các phần tử trong dãy | P1 |
| 6 | `sca_l11_p06_tim_so_lon_nhat_nho_nhat` | `pya_l16_p05_tim_so_lon_nhat_nho_nhat` | Tìm số lớn nhất & nhỏ nhất | P1 |
| 7 | `sca_l11_p07_in_day_so_theo_thu_tu_dao_nguoc` | `pya_l16_p06_in_day_so_theo_thu_tu_dao_nguoc` | In dãy số theo thứ tự đảo ngược | P2 |
| 8 | `sca_l11_p08_dem_so_lan_xuat_hien_cua_x` | `pya_l16_p07_dem_so_lan_xuat_hien_cua_x` | Đếm số lần xuất hiện của X | P2 |
| 9 | `sca_l11_p09_thay_the_tat_ca_so_am_bang_so_0` | `pya_l16_p11_thay_the_tat_ca_so_am_bang_so_0` | Thay thế tất cả số âm bằng số 0 | P2 |
| 10 | `sca_l11_p10_heo_dat_tiet_kiem` | `pya_l16_p15_heo_dat_tiet_kiem` | Heo đất tiết kiệm | P2 |
| 11 | `sca_l11_p11_dem_so_luong_so_chan_trong_mang` | `pya_l16_p04_dem_so_luong_so_chan_trong_mang` | Đếm số lượng số chẵn trong mảng | P2 |
| 12 | `sca_l11_p12_them_diem_vao_danh_sach` | `pya_l16_p02_them_diem_vao_danh_sach` | Thêm điểm vào danh sách | P2 |
| 13 | `sca_l11_p13_chen_so_vao_vi_tri_k` | `pya_l16_p12_chen_so_vao_vi_tri_k` | Chèn số vào vị trí K | P2 |
| 14 | `sca_l11_p14_mat_khau_bi_an` | `pya_l16_p18_mat_khau_bi_an` | Mật khẩu bị ẩn | P2 |
| 15 | `sca_l11_p15_xep_hang_chieu_cao` | `pya_l16_p22_xep_hang_chieu_cao` | Xếp hàng chiều cao | P2 |
| 16 | `sca_l11_p16_xoa_phan_tu_dau_tien_bang_x` | `pya_l16_p10_xoa_phan_tu_dau_tien_bang_x` | Xóa phần tử đầu tiên bằng X | P2 |
| 17 | `sca_l11_p17_xoay_vong_danh_sach_sang_phai` | `pya_l16_p13_xoay_vong_danh_sach_sang_phai` | Xoay vòng danh sách sang phải | P3 |
| 18 | `sca_l11_p18_tach_mang_chan_va_mang_le` | `pya_l16_p09_tach_mang_chan_va_mang_le` | Tách mảng chẵn và mảng lẻ | P2 |
| 19 | `sca_l11_p19_dem_tu_dai` | `pya_l16_p24_dem_tu_dai` | Đếm từ dài | P2 |
| 20 | `sca_l11_p20_bang_diem_lop_hoc` | `pya_l16_p17_bang_diem_lop_hoc` | Bảng điểm lớp học | P2 |
| 21 | `sca_l11_p21_cap_so_co_tong_bang_s` | `pya_l16_p14_cap_so_co_tong_bang_s` | Cặp số có tổng bằng S | P3 |
| 22 | `sca_l11_p22_ve_so_may_man` | `pya_l16_p16_ve_so_may_man` | Vé số may mắn | P2 |
| 23 | `sca_l11_p23_chuyen_tau_vuot_deo` | `pya_l16_p26_chuyen_tau_vuot_deo` | Chuyến tàu vượt đèo | P2 |
| 24 | `sca_l11_p24_tong_chu_so_lon_nhat` | `pya_l16_p20_tong_chu_so_lon_nhat` | Tổng chữ số lớn nhất | P2 |
| 25 | `sca_l11_p25_dem_keo_chan_le` | `pya_l16_p19_dem_keo_chan_le` | Đếm kẹo chẵn lẻ | P1 |
| 26 | `sca_l11_p26_dem_sao_nguyen_to` | `pya_l16_p25_dem_sao_nguyen_to` | Đếm sao nguyên tố | P3 |

### Bai 14 — Kho bai tap (14 bai, ma `sca_l12_*`)

| # | Ma Scratch | Nguon Python | Ten bai | Tang |
|---|---|---|---|---|
| 1 | `sca_l12_p01_diem_so_cao_nhat_thap_nhat` | `pya_l17_p01_diem_so_cao_nhat_thap_nhat` | Điểm số cao nhất & thấp nhất | P1 |
| 2 | `sca_l12_p02_loc_bo_cac_so_trung_lap` | `pya_l17_p07_loc_bo_cac_so_trung_lap` | Lọc bỏ các số trùng lặp | P1 |
| 3 | `sca_l12_p03_sap_xep_ten_theo_thu_tu_bang_chu_cai` | `pya_l17_p09_sap_xep_ten_theo_thu_tu_bang_chu_cai` | Sắp xếp tên theo thứ tự bảng chữ cái | P3 |
| 4 | `sca_l12_p04_ghep_hai_day_da_sap_xep` | `pya_l17_p13_ghep_hai_day_da_sap_xep` | Ghép hai dãy đã sắp xếp | P3 |
| 5 | `sca_l12_p05_dem_so_luong_hoc_sinh_tren_diem_trung_binh` | `pya_l17_p06_dem_so_luong_hoc_sinh_tren_diem_trung_binh` | Đếm số lượng học sinh trên điểm trung bình | P1 |
| 6 | `sca_l12_p06_sap_xep_tang_dan_don_gian` | `pya_l17_p02_sap_xep_tang_dan_don_gian` | Sắp xếp tăng dần đơn giản | P2 |
| 7 | `sca_l12_p07_sap_xep_giam_dan_bang_xep_hang` | `pya_l17_p04_sap_xep_giam_dan_bang_xep_hang` | Sắp xếp giảm dần bảng xếp hạng | P2 |
| 8 | `sca_l12_p08_trung_vi_cua_day_so_median` | `pya_l17_p11_trung_vi_cua_day_so_median` | Trung vị của dãy số (Median) | P2 |
| 9 | `sca_l12_p09_tim_so_lon_thu_nhi_trong_mang` | `pya_l17_p05_tim_so_lon_thu_nhi_trong_mang` | Tìm số lớn thứ nhì trong mảng | P2 |
| 10 | `sca_l12_p10_diem_trung_binh_mon_hoc` | `pya_l17_p03_diem_trung_binh_mon_hoc` | Điểm trung bình môn học | P2 |
| 11 | `sca_l12_p11_chenh_lech_nho_nhat_giua_hai_so` | `pya_l17_p10_chenh_lech_nho_nhat_giua_hai_so` | Chênh lệch nhỏ nhất giữa hai số | P2 |
| 12 | `sca_l12_p12_so_xuat_hien_nhieu_lan_nhat_mode` | `pya_l17_p12_so_xuat_hien_nhieu_lan_nhat_mode` | Số xuất hiện nhiều lần nhất (Mode) | P3 |
| 13 | `sca_l12_p13_diem_olympic_bo_max_bo_min` | `pya_l17_p08_diem_olympic_bo_max_bo_min` | Điểm olympic bỏ max bỏ min | P3 |
| 14 | `sca_l12_p14_xep_hang_mua_tra_sua_greedy` | `pya_l17_p14_xep_hang_mua_tra_sua_greedy` | Xếp hàng mua trà sữa (Greedy) | P3 |

### Bai 15 — Kho bai tap (12 bai, ma `sca_l13_*`)

| # | Ma Scratch | Nguon Python | Ten bai | Tang |
|---|---|---|---|---|
| 1 | `sca_l13_p01_do_dai_cua_chuoi` | `pya_l13_p02_do_dai_cua_chuoi` | Độ dài của chuỗi | P0 |
| 2 | `sca_l13_p02_cat_ba_ky_tu_dau_tien` | `pya_l13_p03_cat_ba_ky_tu_dau_tien` | Cắt ba ký tự đầu tiên | P1 |
| 3 | `sca_l13_p03_dao_nguoc_ten_rieng` | `pya_l13_p04_dao_nguoc_ten_rieng` | Đảo ngược tên riêng | P1 |
| 4 | `sca_l13_p04_ky_tu_o_vi_tri_chan` | `pya_l13_p08_ky_tu_o_vi_tri_chan` | Ký tự Ở vị trí chẵn | P1 |
| 5 | `sca_l13_p05_rut_trich_ten_mien_email` | `pya_l13_p07_rut_trich_ten_mien_email` | Rút trích tên miền email | P2 |
| 6 | `sca_l13_p06_ky_tu_dau_ky_tu_cuoi` | `pya_l13_p01_ky_tu_dau_ky_tu_cuoi` | Ký tự đầu & ký tự cuối | P0 |
| 7 | `sca_l13_p07_dich_chuyen_vong_quanh_left_rotation` | `pya_l13_p11_dich_chuyen_vong_quanh_left_rotation` | Dịch chuyển vòng quanh (left rotation) | P3 |
| 8 | `sca_l13_p08_cat_doi_chuoi_ky_tu` | `pya_l13_p06_cat_doi_chuoi_ky_tu` | Cắt đôi chuỗi ký tự | P2 |
| 9 | `sca_l13_p09_hoan_doi_nua_dau_nua_sau` | `pya_l13_p09_hoan_doi_nua_dau_nua_sau` | Hoán đổi nửa đầu nửa sau | P2 |
| 10 | `sca_l13_p10_xoa_ky_tu_o_vi_tri_k` | `pya_l13_p10_xoa_ky_tu_o_vi_tri_k` | Xóa ký tự ở vị trí K | P2 |
| 11 | `sca_l13_p11_kiem_tra_tu_doi_xung_palindrome` | `pya_l13_p05_kiem_tra_tu_doi_xung_palindrome` | Kiểm tra từ đối xứng (palindrome) | P3 |
| 12 | `sca_l13_p12_chuoi_con_doi_xung_dai_nhat` | `pya_l13_p12_chuoi_con_doi_xung_dai_nhat` | Chuỗi con đối xứng dài nhất | P3 |

### Bai 16 — Kho bai tap (24 bai, ma `sca_l14_*`)

| # | Ma Scratch | Nguon Python | Ten bai | Tang |
|---|---|---|---|---|
| 1 | `sca_l14_p01_chuyen_toan_bo_thanh_chu_hoa` | `pya_l14_p02_chuyen_toan_bo_thanh_chu_hoa` | Chuyển toàn bộ thành chữ hoa | P0 |
| 2 | `sca_l14_p02_thay_the_ky_tu_bi_mat` | `pya_l14_p08_thay_the_ky_tu_bi_mat` | Thay thế ký tự bí mật | P2 |
| 3 | `sca_l14_p03_xoa_bo_toan_bo_dau_cach` | `pya_l14_p09_xoa_bo_toan_bo_dau_cach` | Xóa bỏ toàn bộ dấu cách | P0 |
| 4 | `sca_l14_p04_ma_ascii_cua_ky_tu` | `pya_l15_p03_ma_ascii_cua_ky_tu` | Mã ASCII của ký tự | P1 |
| 5 | `sca_l14_p05_dem_so_tu_trong_cau` | `pya_l15_p01_dem_so_tu_trong_cau` | Đếm số từ trong câu | P1 |
| 6 | `sca_l14_p06_tim_tu_dai_nhat_trong_cau` | `pya_l15_p05_tim_tu_dai_nhat_trong_cau` | Tìm từ dài nhất trong câu | P1 |
| 7 | `sca_l14_p07_ky_tu_ke_tiep_trong_bang_chu_cai` | `pya_l15_p04_ky_tu_ke_tiep_trong_bang_chu_cai` | Ký tự kế tiếp trong bảng chữ cái | P1 |
| 8 | `sca_l14_p08_tu_dau_tien_tu_cuoi_cung` | `pya_l15_p02_tu_dau_tien_tu_cuoi_cung` | Từ đầu tiên & từ cuối cùng | P1 |
| 9 | `sca_l14_p09_chuan_hoa_khoang_trang` | `pya_l15_p06_chuan_hoa_khoang_trang` | Chuẩn hóa khoảng trắng | P2 |
| 10 | `sca_l14_p10_in_tung_chu_cai_xuong_dong` | `pya_l14_p01_in_tung_chu_cai_xuong_dong` | In từng chữ cái xuống dòng | P2 |
| 11 | `sca_l14_p11_viet_hoa_chu_cai_dau_moi_tu_title_case` | `pya_l15_p07_viet_hoa_chu_cai_dau_moi_tu_title_case` | Viết hoa chữ cái đầu mỗi từ (title case) | P1 |
| 12 | `sca_l14_p12_dao_nguoc_tung_tu_trong_cau` | `pya_l15_p08_dao_nguoc_tung_tu_trong_cau` | Đảo ngược từng từ trong câu | P2 |
| 13 | `sca_l14_p13_mat_ma_thay_the_hoan_vi_anagram` | `pya_l15_p12_mat_ma_thay_the_hoan_vi_anagram` | Mật mã thay thế hoán vị (anagram) | P3 |
| 14 | `sca_l14_p14_tu_xuat_hien_nhieu_nhat_trong_doan` | `pya_l15_p11_tu_xuat_hien_nhieu_nhat_trong_doan` | Từ xuất hiện nhiều nhất trong đoạn | P3 |
| 15 | `sca_l14_p15_dem_so_luong_nguyen_am` | `pya_l14_p10_dem_so_luong_nguyen_am` | Đếm số lượng nguyên âm | P1 |
| 16 | `sca_l14_p16_dem_ky_tu_a_ca_hoa_lan_thuong` | `pya_l14_p03_dem_ky_tu_a_ca_hoa_lan_thuong` | Đếm ký tự ‘A’ (cả hoa lẫn thường) | P1 |
| 17 | `sca_l14_p17_tinh_tong_cac_chu_so_trong_chuoi` | `pya_l14_p06_tinh_tong_cac_chu_so_trong_chuoi` | Tính tổng các chữ số trong chuỗi | P2 |
| 18 | `sca_l14_p18_tach_rieng_chu_so_ra_khoi_van_ban` | `pya_l14_p05_tach_rieng_chu_so_ra_khoi_van_ban` | Tách riêng chữ số ra khỏi văn bản | P2 |
| 19 | `sca_l14_p19_nen_chuoi_ky_tu_runlength_encoding` | `pya_l14_p11_nen_chuoi_ky_tu_runlength_encoding` | Nén chuỗi ký tự (Run-Length encoding) | P3 |
| 20 | `sca_l14_p20_dem_chu_cai_in_hoa_in_thuong` | `pya_l14_p04_dem_chu_cai_in_hoa_in_thuong` | Đếm chữ cái in hoa & in thường | P2 |
| 21 | `sca_l14_p21_mat_ma_caesar_dich_chuyen_k` | `pya_l15_p09_mat_ma_caesar_dich_chuyen_k` | Mật mã Caesar dịch chuyển K | P3 |
| 22 | `sca_l14_p22_giai_ma_mat_thu_caesar` | `pya_l15_p10_giai_ma_mat_thu_caesar` | Giải mã mật thư Caesar | P3 |
| 23 | `sca_l14_p23_doi_chu_hoa_thanh_thuong_nguoc_lai` | `pya_l14_p07_doi_chu_hoa_thanh_thuong_nguoc_lai` | Đổi chữ hoa thành thường & ngược lại | P2 |
| 24 | `sca_l14_p24_trich_xuat_so_lon_nhat_trong_van_ban` | `pya_l14_p12_trich_xuat_so_lon_nhat_trong_van_ban` | Trích xuất số lớn nhất trong văn bản | P2 |

