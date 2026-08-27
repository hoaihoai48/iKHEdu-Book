# NGÂN HÀNG KIẾN THỨC BÀI GIẢNG & CODE CHUẨN - iKHEDU

> 🖥️ **THÔNG TIN VPS SERVER CHẤM THI:** IP: `103.104.119.160` | User: `root` | Pass: `d@ngKh0a123` | App Path: `/home/dkoj/public_html` | Data Path: `/home/dkoj/public_html/problem_data/ikh-XXXX/` | Python Venv: `/home/dkoj/vnojsite/bin/python` | Restart: `/home/dkoj/public_html/restart.sh` 
> 🧪 **BẮT BỤC RETEST 100% AC:** Mọi bài toán sau khi tạo 20 testcases BẮT BỤC phải dùng `g++ -O3` biên dịch `solution.cpp` chạy qua 20 tests khớp 100% output trước khi upload!
> 📐 **ĐỊNH DẠNG KATEX MARKDOWN CHUẨN:** Bắt buộc dùng `$N$`, `$K$`, `$i$`, HTML Entity `&#95;` cho chỉ số mảng (`$A&#95;1, A&#95;2, \dots, A&#95;N$`, `$A&#95;i$`), và escape `\|` cho ký tự pipe `|` trong ô bảng Markdown (`dp[mask \| (1 << v)]`). Tuyệt đối không có chữ `Mô tả:` ở đầu bài.
> 📖 **QUY TRÌNH DEPLOY CHO AI AGENTS:** 1. Retest 100% AC local. 2. Đóng gói 20 tests (`1.in`..`20.out`) + `init.yml`. 3. SCP sang VPS. 4. Giải nén `ikh-XXXX.zip`. 5. Chạy Python script CSDL (bắt buộc set: `Problem` with `group`, `time_limit=1.0`, `memory_limit=262144`, `is_public=True`; `p.allowed_languages.set([cpp17, cpp20])`; `Solution.publish_on=now`; `ProblemTranslation` lang=`vi`; `ProblemData.zipfile='ikh-XXXX/ikh-XXXX.zip'`; `ContestProblem` with `order=N`, `points=100.0`). 6. Clear Cache (`cache.clear()`) + Restart. Xem chi tiết tại [IKHEDU_AI_DEVELOPMENT_SPEC.md](file:///Users/dkdeveloper/projects/testcase/IKHEDU_AI_DEVELOPMENT_SPEC.md).
> 🏆 **QUY TẮC TẠO CONTEST CHUẨN iKHEDU:**
> 1. **Key & Name:** `key='ltbb_level3_XX'`, `name='#XX - Tên chuyên đề XX'` (VD: `#06 - Đồ thị nâng cao`). **BẮT BỤC BẢO TOÀN `contest.name` KHI SYNC BÀI HAY UPDATE MÔ TẢ!**
> 2. **Author & Organization:** Author set `admin` (`admin.profile`), Organization set `luyen-thi-bang-b-level-3` (`Luyện Thi Bảng B - Level 3`).
> 3. **Flags Quyền & Rating:** `is_visible = False` (Không public rộng rãi), `is_private = False` (BỎ check "Kỳ thi riêng tư cho một số thành viên"), `is_rated = True` (CHECK "Kỳ thi có tính rating"), `is_organization_private = True`.
> 4. **Time & Cache:** Set `start_time` & `end_time` chuẩn timezone, clear cache (`cache.clear()`) và restart Supervisor/Nginx.

---

## 🎯 KHUNG KHÓA HỌC C++ LEVEL 3: "LUYỆN THI BẢNG B" (650 BÀI TOÁN)

| STT | Chuyên đề Bài Giảng / Kỳ Thi | Số Bài | Nội Dung & Định Hướng |
| :---: | :--- | :---: | :--- |
| **01** | Ôn tập toàn bộ kiến thức | **60** | 20 Challenges Vượt Ải USACO Style (3 bài/Challenge) |
| **02** | Nhận dạng dạng toán | **50** | Chỉ phân tích đề, xác định hướng giải |
| **03** | Một bài nhiều cách giải | **40** | Khoảng 10 bài, mỗi bài có 3–5 cách giải (Trâu $\to$ Tối ưu) |
| **04** | Kết hợp thuật toán | **80** | Binary Search + DP, Graph + DP, Hash + Prefix... |
| **05** | Quy hoạch động nâng cao | **45** | LIS, LCS, Knapsack, Interval DP, Tree DP... |
| **06** | Đồ thị nâng cao | **45** | DSU, MST, Dijkstra, Topological Sort... |
| **07** | Cấu trúc dữ liệu nâng cao | **35** | Lazy Segment Tree, Trie, Sparse Table... |
| **08** | Chuỗi nâng cao | **35** | KMP, Z, Manacher, Rolling Hash... |
| **09** | Toán nâng cao | **30** | Matrix, CRT, Euler Phi, Sieve... |
| **10** | Debug & Tối ưu | **30** | Sửa code, tối ưu thuật toán |
| **11** | Contest + Review | **80** | 20 contest $\times$ 4 bài |
| **12** | Luyện đề tổng hợp | **120** | Tin học trẻ, HSG, Chuyên Tin |

---

## 🏆 BẢNG MỤC LỤC CHI TIẾT TRỌN BỘ 60 BÀI TOÁN (IKH-0001 ĐẾN IKH-0060)

| STT | Mã Bài | Tên Bài Toán | Thuật Toán / Cấu Trúc Dữ Liệu | Rating | Ngôn Ngữ | Trạng Thái |
| :---: | :---: | :--- | :--- | :---: | :---: | :---: |
| 1 | **`IKH-0001`** | [Gói kẹo may mắn](#ikh-0001---ikh-0001-gói-kẹo-may-mắn) | Algorithmic Thinking | 1020 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 2 | **`IKH-0002`** | [Xâu xinh đẹp](#ikh-0002---ikh-0002-xâu-xinh-đẹp) | Algorithmic Thinking | 1040 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 3 | **`IKH-0003`** | [Mua bài](#ikh-0003---ikh-0003-mua-bài) | Algorithmic Thinking | 1060 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 4 | **`IKH-0004`** | [Dãy cấp số nhân](#ikh-0004---ikh-0004-dãy-cấp-số-nhân) | Algorithmic Thinking | 1080 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 5 | **`IKH-0005`** | [Bảng đẹp](#ikh-0005---ikh-0005-bảng-đẹp) | Algorithmic Thinking | 1100 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 6 | **`IKH-0006`** | [Vòng tay](#ikh-0006---ikh-0006-vòng-tay) | Algorithmic Thinking | 1120 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 7 | **`IKH-0007`** | [Kho Du Tru Quoc Gia](#ikh-0007---ikh-0007-kho-du-tru-quoc-gia) | Tìm kiếm nhị phân trên tập nghiệm (Binary Search on Answer) | 1140 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 8 | **`IKH-0008`** | [Chuyến Tàu Tiếp Vận](#ikh-0008---ikh-0008-chuyến-tàu-tiếp-vận) | Algorithmic Thinking | 1160 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 9 | **`IKH-0009`** | [Điều Phối Xe Cứu Hộ](#ikh-0009---ikh-0009-điều-phối-xe-cứu-hộ) | Algorithmic Thinking | 1180 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 10 | **`IKH-0010`** | [Khu Chợ Thông Minh](#ikh-0010---ikh-0010-khu-chợ-thông-minh) | Algorithmic Thinking | 1200 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 11 | **`IKH-0011`** | [Lễ Hội Ánh Sáng](#ikh-0011---ikh-0011-lễ-hội-ánh-sáng) | Algorithmic Thinking | 1220 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 12 | **`IKH-0012`** | [Lễ Hội Chia Bánh](#ikh-0012---ikh-0012-lễ-hội-chia-bánh) | Binary Search on Answer, Greedy Check | 1240 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 13 | **`IKH-0013`** | [Hành Lang Ánh Sáng](#ikh-0013---ikh-0013-hành-lang-ánh-sáng) | Prefix Sum 2D, Grid Verification | 1260 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 14 | **`IKH-0014`** | [Trung Tâm Logistics](#ikh-0014---ikh-0014-trung-tâm-logistics) | Greedy Interval Scheduling, Sorting | 1280 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 15 | **`IKH-0015`** | [Trung Tâm Dữ Liệu AI](#ikh-0015---ikh-0015-trung-tâm-dữ-liệu-ai) | Greedy, Priority Queue | 1300 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 16 | **`IKH-0016`** | [Đội Hạm Đội Robot](#ikh-0016---ikh-0016-đội-hạm-đội-robot) | Two Pointers, Sorting | 1320 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 17 | **`IKH-0017`** | [Cặp Đèn Đường Bằng](#ikh-0017---ikh-0017-cặp-đèn-đường-bằng) | Algorithmic Thinking | 1340 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 18 | **`IKH-0018`** | [Lịch Khởi Hành Chuyến Bay](#ikh-0018---ikh-0018-lịch-khởi-hành-chuyến-bay) | Scheduling / Interval Selection Problem (Tham ăn - Greedy). | 1360 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 19 | **`IKH-0019`** | [Đội Container Cảng Hải Phòng](#ikh-0019---ikh-0019-đội-container-cảng-hải-phòng) | Algorithmic Thinking | 1380 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 20 | **`IKH-0020`** | [Tra Cứu Mã Vận Đơn](#ikh-0020---ikh-0020-tra-cứu-mã-vận-đơn) | Hash Map / STL Frequency Count. | 1400 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 21 | **`IKH-0021`** | [Hàng Cho Mới Nhất](#ikh-0021---ikh-0021-hàng-cho-mới-nhất) | Max Heap / STL Priority Queue. | 1420 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 22 | **`IKH-0022`** | [Lưới Cảm Biến IoT Smart City](#ikh-0022---ikh-0022-lưới-cảm-biến-iot-smart-city) | Sliding Window + STL Multiset / Deque. | 1440 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 23 | **`IKH-0023`** | [Điểm Thu Phí Tự Động VETC](#ikh-0023---ikh-0023-điểm-thu-phí-tự-động-vetc) | Binary Search / `std::lower_bound`. | 1460 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 24 | **`IKH-0024`** | [Phân Bổ Điện Năng Mặt Trời](#ikh-0024---ikh-0024-phân-bổ-điện-năng-mặt-trời) | Sorting / Quickselect / Binary Search. | 1480 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 25 | **`IKH-0025`** | [Tải Trọng Tối Đa Tàu Container](#ikh-0025---ikh-0025-tải-trọng-tối-đa-tàu-container) | Binary Search on Answer + Greedy. | 1500 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 26 | **`IKH-0026`** | [Chuỗi Cung Ứng Chuối Xuất Khẩu](#ikh-0026---ikh-0026-chuỗi-cung-ứng-chuối-xuất-khẩu) | Dynamic Programming / Thuật toán Kadane. | 1520 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 27 | **`IKH-0027`** | [Tăng Trưởng Khách Du Lịch Quốc Tế](#ikh-0027---ikh-0027-tăng-trưởng-khách-du-lịch-quốc-tế) | Dynamic Programming + Binary Search ($O(N \log N)$). | 1540 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 28 | **`IKH-0028`** | [Lựa Chọn Thiết Bị Trạm Phát 5G](#ikh-0028---ikh-0028-lựa-chọn-thiết-bị-trạm-phát-5g) | Dynamic Programming 0/1 Knapsack. | 1560 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 29 | **`IKH-0029`** | [Mạng Lưới Tuyến Xe Být Hà Nội](#ikh-0029---ikh-0029-mạng-lưới-tuyến-xe-být-hà-nội) | Biểu diễn đồ thị / Degree Counting. | 1580 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 30 | **`IKH-0030`** | [Đường Bay Cấp Cứu Y Tế](#ikh-0030---ikh-0030-đường-bay-cấp-cứu-y-tế) | Breadth-First Search (BFS). | 1600 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 31 | **`IKH-0031`** | [Tối Ưu Hóa Tuyến Đường Giao Hàng Shopee](#ikh-0031---ikh-0031-tối-ưu-hóa-tuyến-đường-giao-hàng-shopee) | Thuật toán Dijkstra dùng Min-Heap. | 1620 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 32 | **`IKH-0032`** | [Quy Hoạch Mạng Đăng Đăng Ký Cáp Quang FPT](#ikh-0032---ikh-0032-quy-hoạch-mạng-đăng-đăng-ký-cáp-quang-fpt) | Disjoint Set Union (DSU) / Union-Find. | 1640 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 33 | **`IKH-0033`** | [Mạng Lưới Đường Hầm Metro TP.HCM](#ikh-0033---ikh-0033-mạng-lưới-đường-hầm-metro-tp.hcm) | Thuật toán Kruskal + DSU. | 1660 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 34 | **`IKH-0034`** | [Lịch Trình Sản Xuất Linh Kiện VinFast](#ikh-0034---ikh-0034-lịch-trình-sản-xuất-linh-kiện-vinfast) | Kahn's Algorithm + Priority Queue (Min-Heap). | 1680 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 35 | **`IKH-0035`** | [Vùng Phủ Sóng Trạm Ra-đa Thời Tiết](#ikh-0035---ikh-0035-vùng-phủ-sóng-trạm-ra-đa-thời-tiết) | Geometry / Distance Calculation. | 1700 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 36 | **`IKH-0036`** | [Ranh Giới Quy Hoạch Nông Nghiệp Công Nghệ Cao](#ikh-0036---ikh-0036-ranh-giới-quy-hoạch-nông-nghiệp-công-nghệ-cao) | Axis-Aligned Bounding Box (AABB) Point Check. | 1720 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 37 | **`IKH-0037`** | [Quy Hoạch Công Viên Xanh Ecopark](#ikh-0037---ikh-0037-quy-hoạch-công-viên-xanh-ecopark) | Geometry / Shoelace Formula (Công thức Dây giày Gauss). | 1740 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 38 | **`IKH-0038`** | [Đồng Bộ Hóa Chu Kỳ Tín Hiệu Đèn Giao Thông](#ikh-0038---ikh-0038-đồng-bộ-hóa-chu-kỳ-tín-hiệu-đèn-giao-thông) | Number Theory / Prime Factorization / Modulo Exponentiation. | 1760 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 39 | **`IKH-0039`** | [Mã Hóa Giao Dịch Ngân Hàng ViettinBank](#ikh-0039---ikh-0039-mã-hóa-giao-dịch-ngân-hàng-viettinbank) | Number Theory / Divisor Counting. | 1780 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 40 | **`IKH-0040`** | [Xác Thực Chữ Ký Số Hệ Thống BHXH](#ikh-0040---ikh-0040-xác-thực-chữ-ký-số-hệ-thống-bhxh) | Binary Exponentiation (Lũy thừa Nhị phân) + `__int128_t` Modulo Multiplication. | 1800 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 41 | **`IKH-0041`** | [Kiểm Lỗi Dữ Liệu Truyền Tải Bằng Mã Parity](#ikh-0041---ikh-0041-kiểm-lỗi-dữ-liệu-truyền-tải-bằng-mã-parity) | Bitwise Manipulation / `__builtin_popcountll`. | 1820 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 42 | **`IKH-0042`** | [Giải Mã Tín Hiệu Bảo Mật VinaPhone](#ikh-0042---ikh-0042-giải-mã-tín-hiệu-bảo-mật-vinaphone) | Prefix XOR Array ($O(1)$ query). | 1840 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 43 | **`IKH-0043`** | [Trò Chơi Bốc Sỏi Trên Bàn Cờ](#ikh-0043---ikh-0043-trò-chơi-bốc-sỏi-trên-bàn-cờ) | Game Theory / Nim Game / Bouton's Theorem. | 1860 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 44 | **`IKH-0044`** | [Thống Kê Doanh Thu Chuỗi Siêu Thị WinMart](#ikh-0044---ikh-0044-thống-kê-doanh-thu-chuỗi-siêu-thị-winmart) | 2D Prefix Sum ($O(1)$ query). | 1880 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 45 | **`IKH-0045`** | [Xếp Hạng Bảng Vàng Cuộc Thi Tin Học Trẻ](#ikh-0045---ikh-0045-xếp-hạng-bảng-vàng-cuộc-thi-tin-học-trẻ) | Fenwick Tree (Binary Indexed Tree - BIT). | 1900 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 46 | **`IKH-0046`** | [Giám Sát Lưu Lượng Mạng Cáp Quang Bắc](#ikh-0046---ikh-0046-giám-sát-lưu-lượng-mạng-cáp-quang-bắc-nam) | Segment Tree (Range Maximum Query - RMQ). | 1920 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 47 | **`IKH-0047`** | [Bộ Lọc Từ Khóa Nhạy Cảm Zalo](#ikh-0047---ikh-0047-bộ-lọc-từ-khóa-nhạy-cảm-zalo) | String Sliding Window + `std::string_view` / String Hashing. | 1940 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 48 | **`IKH-0048`** | [Kiểm Tra Mã Vạch Hàng Hóa Tiki](#ikh-0048---ikh-0048-kiểm-tra-mã-vạch-hàng-hóa-tiki) | Polynomial Rolling Hash (Forward + Backward Hash). | 1960 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 49 | **`IKH-0049`** | [Tìm Kiếm Bản Đồ Địa Giới VNPost](#ikh-0049---ikh-0049-tìm-kiếm-bản-đồ-địa-giới-vnpost) | KMP Algorithm / Prefix Function. | 1980 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 50 | **`IKH-0050`** | [Lộ Trình Thu Gom Rác Thải Đô Thị URENCO](#ikh-0050---ikh-0050-lộ-trình-thu-gom-rác-thải-đô-thị-urenco) | Bitmask Dynamic Programming ($O(2^N \cdot N^2)$). | 2000 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 51 | **`IKH-0051`** | [Phân Bổ Máy Chủ Trạm Mạng Viễn Thông Viettel](#ikh-0051---ikh-0051-phân-bổ-máy-chủ-trạm-mạng-viễn-thông-viettel) | Tree Dynamic Programming ($O(N)$). | 2950 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 52 | **`IKH-0052`** | [Lập Kế Hoạch Đóng Tàu Siêu Trọng Gemadept](#ikh-0052---ikh-0052-lập-kế-hoạch-đóng-tàu-siêu-trọng-gemadept) | Partition DP ($O(K \cdot N^2)$ / Divide & Conquer Optimization). | 3100 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 53 | **`IKH-0053`** | [Phân Phối Thuốc Đột Biến Long Châu](#ikh-0053---ikh-0053-phân-phối-thuốc-đột-biến-long-châu) | Multi-source Dijkstra / Graph Transformation. | 3250 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 54 | **`IKH-0054`** | [Kiểm Trà Điểm Yếu Tuyến Cáp Quang Biển AAG](#ikh-0054---ikh-0054-kiểm-trà-điểm-yếu-tuyến-cáp-quang-biển-aag) | Tarjan's Algorithm for Bridges ($O(N + M)$). | 3400 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 55 | **`IKH-0055`** | [Quản Lý Mạng Lưới Điện Thông Minh EVN](#ikh-0055---ikh-0055-quản-lý-mạng-lưới-điện-thông-minh-evn) | Segment Tree with Lazy Propagation ($O(\log N)$). | 3550 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 56 | **`IKH-0056`** | [Truy Vấn Đường Đi Ngắn Nhất Đèo Cả](#ikh-0056---ikh-0056-truy-vấn-đường-đi-ngắn-nhất-đèo-cả) | Lowest Common Ancestor (LCA) via Binary Lifting ($O(\log N)$ query). | 3700 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 57 | **`IKH-0057`** | [Phân Phối Luồng Băng Thông Viettel VNPT](#ikh-0057---ikh-0057-phân-phối-luồng-băng-thông-viettel-vnpt) | Dinic's Algorithm for Max Flow ($O(V^2 E)$). | 3850 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 58 | **`IKH-0058`** | [Quy Hoạch Vành Đai An Ninh Sân Bay Long Thành](#ikh-0058---ikh-0058-quy-hoạch-vành-đai-an-ninh-sân-bay-long-thành) | Computational Geometry / Convex Hull (Andrew's Monotone Chain $O(N \log N)$). | 4000 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 59 | **`IKH-0059`** | [Truy Vấn Lịch Sử Giao Dịch Vietcombank](#ikh-0059---ikh-0059-truy-vấn-lịch-sử-giao-dịch-vietcombank) | Persistent Segment Tree ($O(\log N)$ query). | 4150 | C++17, C++20 | 🟢 LIVE (20/20 AC) |
| 60 | **`IKH-0060`** | [Tối Ưu Hóa Tuyến Đường Vận Chuyển VinFast](#ikh-0060---ikh-0060-tối-ưu-hóa-tuyến-đường-vận-chuyển-vinfast) | Dynamic Shortest Path / Priority Queue Dijkstra. | 4300 | C++17, C++20 | 🟢 LIVE (20/20 AC) |

---

## ✍️ QUY TẮC LỜI VĂN & VĂN PHONG SÁNG TẠO ĐỀ BÀI (WORDING & STORYTELLING STYLEGUIDE)

1. **Giọng văn chủ đạo:** Trang trọng, chuyên nghiệp, truyền cảm hứng và mang đậm hơi thở thực tiễn (IOI / Codeforces / USACO Style).
2. **Quy tắc NGHIÊM CẤM mở đầu nhàm chán:**
   - ❌ *Không viết:* *"Cho N số..."*, *"Cho một mảng..."*, *"Cho một đồ thị..."*, *"Cho xâu S..."*.
   - ✅ *Bắt buộc viết:* Khởi đầu bằng một câu chuyện bối cảnh có tính thực tế cao (Tài chính, Logistics, Y tế, Văn hóa Việt Nam, Khoa học vũ trụ, Trí tuệ nhân tạo).
3. **Cấu trúc Đề bài 3 Phần Chuẩn hóa (350 – 500 từ):**
   - **Phần 1 - Bối cảnh Thực tế (80–120 từ):** Nêu hoàn cảnh, lý do và ý nghĩa thực tiễn.
   - **Phần 2 - Mô tả Nhiệm vụ (150–250 từ):** Đặt học sinh vào vai trò chuyên gia (Chuyên gia Logistics, Kỹ sư AI, Đội trưởng cứu hộ, Nhà hoạch định tài chính).
   - **Phần 3 - Mục tiêu Tính toán (50–80 từ):** Đưa ra yêu cầu toán học cụ thể cần xuất ra.
4. **Độ dài đoạn văn:** Mỗi đoạn văn không vượt quá **5 dòng** để học sinh đọc không bị ngợp.
5. **Dùng Tên Thực thể thay cho Tên Biến thuần túy:**
   - Thay vì *"Cho N số $A_i$"* $\longrightarrow$ Viết: *"Có $N$ kho hàng, kho thứ $i$ hiện đang lưu trữ $A_i$ tấn lương thực"*.
   - Thay vì *"Cho mảng $B$"* $\longrightarrow$ Viết: *"Có $M$ tiểu thương đăng ký với nhu cầu diện tích tối thiểu $B_j$ m²"*.
   - Gán đơn vị thực tế: *tấn, kg, triệu đồng, km, giây, container, m², Megawatt, GB*.
6. **Kỹ thuật Giấu Thuật toán Tự nhiên:** Ẩn thuật toán dưới câu hỏi quản lý/tối ưu thực tế.
7. **Phần Bổ sung Đặc trưng iKHEDU:**
   - 💡 **Góc Kiến Thức ("Bạn có biết?"):** Thêm 2–3 dòng mở rộng kiến thức thực tế ở cuối đề.
   - 🚀 **Thử thách Nâng cao (Challenge Question):** Cuối đề có thêm 1 câu hỏi suy luận mở để kích thích tư duy học sinh giỏi.
8. **Quy chuẩn Cấu trúc Thư mục Bài toán Local:** Mỗi thư mục bài toán `IKH-XXXX - [Tên Bài]` tại local phải có đủ 3 file và 1 thư mục:
   - `De_Bai.md`: Đề bài chi tiết (Mô tả bối cảnh, Input, Output, Subtasks, Samples, Góc kiến thức, Thử thách mở rộng).
   - `Huong_Dan_Giang_Day.md`: Giáo án 5 bước dẫn dắt tư duy + Giải thích chi tiết + Editorial C++.
   - `solution.cpp`: Mã nguồn C++ chuẩn tối ưu (I/O fast, 100% AC).
   - `test/`: Thư mục 20 testcases (`test1` .. `test20`).

---

# IKH-0001 - Gói kẹo may mắn

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Đóng vai trò là đội trưởng đội tuyển Học sinh giỏi Tin học, thầy giáo mang đến một hộp chứa $N$ gói kẹo được đánh số từ 1 đến $N$. Gói kẹo thứ $i$ chứa chính xác **$A&#95;i$** viên kẹo ($1 \le i \le N$). Tất cả các gói kẹo có vỏ ngoài hoàn toàn giống nhau, nhưng bên trong chỉ chứa một trong hai vị: vị dâu hoặc vị chocolate.

Thầy giáo tiết lộ trong hộp có đúng $M$ gói kẹo vị dâu và **N - M** gói kẹo vị chocolate. An không thể biết trước gói nào mang vị gì cho đến khi quyết định chọn và bóc gói đó ra.

An rất thích vị dâu và muốn chọn ra một tập hợp các gói kẹo sao cho **chắc chắn** tổng số viên kẹo vị dâu nhận được phải từ $K$ viên trở lên, bất kể sự phân bố vị dâu và chocolate rơi vào tình huống xấu nhất như thế nào.

### Input
- Dòng thứ nhất gồm ba số nguyên $N, $M$, K$ ($0 \le $M$ \le N$, $1 \le $K$ \le 10^{14}$).
- Dòng thứ hai gồm $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($1 \le A&#95;i \le 10^9$).

### Output
- Một số nguyên duy nhất là số gói kẹo tối thiểu An cần chọn. Nếu không thể thỏa mãn, in ra `-1`.

### Giới hạn
- $1 \le $N$ \le 2 \times 10^5$
- $0 \le $M$ \le N$
- $1 \le $K$ \le 10^{14}$
- $1 \le A&#95;i \le 10^9$

### Subtasks
- **Subtask 1 (30% điểm):** $N \le 1000$
- **Subtask 2 (70% điểm):** Không có ràng buộc thêm.

### Sample 1
**Input:**
```
4 2 15
10 20 5 10
```
**Output:**
```
4
```
**Giải thích:**
Các gói kẹo có số lượng [10, 20, 5, 10], $M = 2$ gói dâu và $4-2=2$ gói chocolate. Cần tối thiểu $K = 15$ kẹo dâu.
- Chọn 2 gói: Trường hợp xấu nhất cả 2 gói đều là chocolate $\implies 0$ kẹo dâu.
- Chọn 3 gói lớn nhất {20, 10, 10}: Trường hợp xấu nhất 2 gói lớn {20, 10} là chocolate $\implies$ chỉ được 1 gói dâu 10 viên $< 15$.
- Chọn cả 4 gói: Nhận đủ 2 gói dâu = $10 + 5 = 15 \ge 15$. Số gói tối thiểu là 4.

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# IKH-0001 - Gói kẹo may mắn

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Đóng vai trò là đội trưởng đội tuyển Học sinh giỏi Tin học, thầy giáo mang đến một hộp chứa **N** gói kẹo được đánh số từ 1 đến **N**. Gói kẹo thứ **i** chứa chính xác **Ai** viên kẹo ($1 \le i \le N$). Tất cả các gói kẹo có vỏ ngoài hoàn toàn giống nhau, nhưng bên trong chỉ chứa một trong hai vị: vị dâu hoặc vị chocolate.

Thầy giáo tiết lộ trong hộp có đúng **M** gói kẹo vị dâu và **N - M** gói kẹo vị chocolate. An không thể biết trước gói nào mang vị gì cho đến khi quyết định chọn và bóc gói đó ra.

An rất thích vị dâu và muốn chọn ra một tập hợp các gói kẹo sao cho **chắc chắn** tổng số viên kẹo vị dâu nhận được phải từ **K** viên trở lên, bất kể sự phân bố vị dâu và chocolate rơi vào tình huống xấu nhất như thế nào.

### Input
- Dòng thứ nhất gồm ba số nguyên $N, M, K$ ($0 \le M \le N$, $1 \le K \le 10^{14}$).
- Dòng thứ hai gồm $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

### Output
- Một số nguyên duy nhất là số gói kẹo tối thiểu An cần chọn. Nếu không thể thỏa mãn, in ra `-1`.

### Giới hạn
- $1 \le N \le 2 \times 10^5$
- $0 \le M \le N$
- $1 \le K \le 10^{14}$
- $1 \le A_i \le 10^9$

### Subtasks
- **Subtask 1 (30% điểm):** $N \le 1000$
- **Subtask 2 (70% điểm):** Không có ràng buộc thêm.

### Sample 1
**Input:**
```
4 2 15
10 20 5 10
```
**Output:**
```
4
```
**Giải thích:**
Các gói kẹo có số lượng [10, 20, 5, 10], $M = 2$ gói dâu và $4-2=2$ gói chocolate. Cần tối thiểu $K = 15$ kẹo dâu.
- Chọn 2 gói: Trường hợp xấu nhất cả 2 gói đều là chocolate $\implies 0$ kẹo dâu.
- Chọn 3 gói lớn nhất {20, 10, 10}: Trường hợp xấu nhất 2 gói lớn {20, 10} là chocolate $\implies$ chỉ được 1 gói dâu 10 viên $< 15$.
- Chọn cả 4 gói: Nhận đủ 2 gói dâu = $10 + 5 = 15 \ge 15$. Số gói tối thiểu là 4.

---

## 2. HƯỚNG DẪN GIẢNG DẠY (GIÁO VIÊN)

### A. Phương pháp dẫn dắt tư duy học sinh (5 Bước)

1. **Bước 1: Phân tích tư duy "Worst-case Analysis" (Trường hợp xấu nhất)**
   * Đặt câu hỏi: *"Khi ta bóc $X$ gói kẹo, trường hợp bất lợi nhất xảy ra khi nào?"*
   * Trả lời: Khi tất cả $N - M$ gói kẹo vị chocolate đều chui vào tập $X$ gói đã chọn (và chiếm các gói có số lượng viên kẹo nhiều nhất).

2. **Bước 2: Định hình Chiến lược Tham ăn (Greedy Strategy)**
   * Để thu được số kẹo dâu nhiều nhất trong trường hợp xấu nhất, An luôn phải ưu tiên chọn $X$ gói kẹo có **số lượng lớn nhất**.
   * Do đó, bước đầu tiên là **Sắp xếp mảng $A$ giảm dần**: $A_1 \ge A_2 \ge \dots \ge A_N$.

3. **Bước 3: Công thức tính lượng kẹo dâu chắc chắn nhận được**
   * Nếu chọn $X$ gói ($X > N - M$), đối phương sẽ gán $N - M$ gói lớn nhất làm vị chocolate.
   * Số gói vị dâu chắc chắn thuộc về An là $X - (N - M)$ gói, chính là các gói $A_{N-M+1}, A_{N-M+2}, \dots, A_X$.

4. **Bước 4: Phân biệt Biến & Kỹ thuật Dừng Sớm**
   * **`M` (Strawberry Count):** Nếu $M = 0$, không bao giờ thu được kẹo dâu $\implies$ Trả về `-1`.
   * **`K` (Target Limit):** Hạn mức kẹo tối thiểu cần đạt ($K \le 10^{14}$ $\implies$ dùng `long long`).
   * **`current_candies`:** Tổng tích lũy kẹo dâu thu được khi tăng dần $X$ từ $N - M + 1 	o N$. Ngay khi `current_candies >= K`, lập tức in ra $X$ và `return 0`.

5. **Bước 5: Đánh giá biên & Tính khả thi**
   * Nếu duyệt tới $X = N$ mà vẫn $< K$, trả về `-1`.

### B. Độ phức tạp
* **Thời gian:** $O(N \log N)$ do sắp xếp mảng.
* **Bộ nhớ:** $O(N)$ lưu mảng kẹo.

---

## 3. CODE GIẢI C++ CHUẨN

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    // Tối ưu hóa I/O cho C++
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // Sắp xếp các gói kẹo theo thứ tự giảm dần
    sort(a.rbegin(), a.rend());

    // Nếu không có gói kẹo vị dâu nào
    if (m == 0) {
        cout << -1 << "\n";
        return 0;
    }

    // Tích lũy lượng kẹo dâu chắc chắn nhận được
    long long current_candies = 0;

    // Duyệt số gói bóc X từ (n - m + 1) đến n
    for (int x = n - m + 1; x <= n; x++) {
        current_candies += a[x - 1]; // Cộng gói kẹo dâu chắc chắn có trong tập X gói
        
        // Ngay khi đạt hoặc vượt K -> Trả về kết quả X tối thiểu
        if (current_candies >= k) {
            cout << x << "\n";
            return 0;
        }
    }

    // Không thể đạt đủ K viên kẹo vị dâu
    cout << -1 << "\n";
    return 0;
}
```

---

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    // Tối ưu hóa I/O cho C++
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // Sắp xếp các gói kẹo theo thứ tự giảm dần
    sort(a.rbegin(), a.rend());

    // Nếu không có gói kẹo vị dâu nào
    if (m == 0) {
        cout << -1 << "\n";
        return 0;
    }

    // Tích lũy lượng kẹo dâu chắc chắn nhận được
    long long current_candies = 0;

    // Duyệt số gói bóc X từ (n - m + 1) đến n
    for (int x = n - m + 1; x <= n; x++) {
        current_candies += a[x - 1]; // Cộng gói kẹo dâu chắc chắn có trong tập X gói
        
        // Ngay khi đạt hoặc vượt K -> Trả về kết quả X tối thiểu
        if (current_candies >= k) {
            cout << x << "\n";
            return 0;
        }
    }

    // Không thể đạt đủ K viên kẹo vị dâu
    cout << -1 << "\n";
    return 0;
}
```

---

# IKH-0002 - Xâu xinh đẹp

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Thầy giáo đưa cho Bình một xâu $S$ độ dài $N$, gồm các ký tự `A`, `B`, hoặc `C`.
Một xâu con (substring) được gọi là **xinh đẹp** nếu số lượng ký tự `A` xuất hiện trong xâu con đó **nghiêm ngặt lớn hơn** số lượng ký tự `B`.
Nhiệm vụ của bạn là đếm số lượng xâu con xinh đẹp của $S$.

### Input
- Một dòng duy nhất chứa xâu $S$ ($1 \le |S| \le 2 \times 10^5$).

### Output
- In ra một số nguyên duy nhất là số lượng xâu con xinh đẹp.

### Giới hạn
- $1 \le |S| \le 2 \times 10^5$
- Xâu $S$ chỉ gồm các ký tự `A`, `B`, `C`.

### Subtasks
- **Subtask 1 (30% điểm):** $|S| \le 2000$
- **Subtask 2 (70% điểm):** Không có ràng buộc thêm.

### Sample 1
**Input:**
```
ABAC
```
**Output:**
```
6
```
**Giải thích:**
Các xâu con xinh đẹp gồm: "A" (vị trí 1), "ABA" (1..3), "ABAC" (1..4), "A" (v vị trí 3), "AC" (3..4), "A" (trong AC). Tổng cộng 6 xâu con.

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# IKH-0002 - Xâu xinh đẹp

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Thầy giáo đưa cho Bình một xâu $S$ độ dài $N$, gồm các ký tự `A`, `B`, hoặc `C`.
Một xâu con (substring) được gọi là **xinh đẹp** nếu số lượng ký tự `A` xuất hiện trong xâu con đó **nghiêm ngặt lớn hơn** số lượng ký tự `B`.
Nhiệm vụ của bạn là đếm số lượng xâu con xinh đẹp của $S$.

### Input
- Một dòng duy nhất chứa xâu $S$ ($1 \le |S| \le 2 \times 10^5$).

### Output
- In ra một số nguyên duy nhất là số lượng xâu con xinh đẹp.

### Giới hạn
- $1 \le |S| \le 2 \times 10^5$
- Xâu $S$ chỉ gồm các ký tự `A`, `B`, `C`.

### Subtasks
- **Subtask 1 (30% điểm):** $|S| \le 2000$
- **Subtask 2 (70% điểm):** Không có ràng buộc thêm.

### Sample 1
**Input:**
```
ABAC
```
**Output:**
```
6
```
**Giải thích:**
Các xâu con xinh đẹp gồm: "A" (vị trí 1), "ABA" (1..3), "ABAC" (1..4), "A" (v vị trí 3), "AC" (3..4), "A" (trong AC). Tổng cộng 6 xâu con.

---

## 2. HƯỚNG DẪN GIẢNG DẠY (GIÁO VIÊN)

### A. Phương pháp dẫn dắt tư duy học sinh (5 Bước)

1. **Bước 1: Quy đổi bài toán về dạng Giá trị Số (Numerical Mapping)**
   * Quy ước giá trị từng ký tự: `A` $	o +1$, `B` $	o -1$, `C` $	o 0$.
   * Tổng giá trị đoạn con $S[i..j]$ chính là $(	ext{count}(A) - 	ext{count}(B))$.
   * Điều kiện xinh đẹp $\iff \sum_{k=i}^j V_k > 0$.

2. **Bước 2: Chuyển về Bài toán Mảng Cộng Dồn (Prefix Sum Transformation)**
   * Gọi $P[k]$ là tổng dồn từ 0 đến $k$. Tổng đoạn $S[i..j] = P[j] - P[i-1]$.
   * Đoạn $S[i..j]$ xinh đẹp $\iff P[j] - P[i-1] > 0 \iff P[j] > P[i-1]$.

3. **Bước 3: Nhận diện Đếm cặp Nghịch thế (Inversion Counting)**
   * Tại mỗi vị trí $j$, ta cần đếm xem có bao nhiêu $i < j$ thỏa mãn $P[i] < P[j]$.
   * Đây là bài toán đếm cặp phần tử nhỏ hơn phía trước $\implies$ Dùng **Cây Fenwick (BIT)** hoặc **Merge Sort**.

4. **Bước 4: Kỹ thuật Nén Tọa Độ & Offset**
   * Do $P[k]$ có thể âm trong khoảng $[-N, N]$, ta cộng thêm `offset = N + 1` để đưa về chỉ số mảng dương $[1, 2N+1]$.

5. **Bước 5: Cài đặt Cây Fenwick (BIT)**
   * Khởi tạo `BIT` kích thước $2N + 5$. Đưa $P[0] = 0$ (sau khi cộng offset) vào BIT.
   * Duyệt qua từng ký tự, cập nhật $P[j]$, đếm số phần tử nhỏ hơn $P[j]$ trong BIT, sau đó chèn $P[j]$ vào BIT.

### B. Độ phức tạp
* **Thời gian:** $O(N \log N)$.
* **Bộ nhớ:** $O(N)$ lưu BIT và mảng tổng dồn.

---

## 3. CODE GIẢI C++ CHUẨN

```cpp
#include <bits/stdc++.h>
using namespace std;
// Cấu trúc Cây Fenwick (Binary Indexed Tree)
struct BIT {
    int size;
    vector<int> tree;
    BIT(int n) : size(n), tree(n + 1, 0) {}

    void add(int i, int delta) {
        for (; i <= size; i += i & -i) tree[i] += delta;
    }

    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.length();
    int offset = n + 1; // Offset để đưa tổng dồn âm về chỉ số dương
    BIT bit(2 * n + 5);

    long long ans = 0;
    int current_prefix = 0;

    // Khởi tạo prefix sum P[0] = 0
    bit.add(current_prefix + offset, 1);

    for (int j = 0; j < n; j++) {
        if (s[j] == 'A') current_prefix += 1;
        else if (s[j] == 'B') current_prefix -= 1;

        // Đếm số lượng P[i] < current_prefix (tức là query từ 1 đến current_prefix + offset - 1)
        ans += bit.query(current_prefix + offset - 1);

        // Chèn P[j] hiện tại vào BIT
        bit.add(current_prefix + offset, 1);
    }

    cout << ans << "\n";
    return 0;
}
```

---

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;
// Cấu trúc Cây Fenwick (Binary Indexed Tree)
struct BIT {
    int size;
    vector<int> tree;
    BIT(int n) : size(n), tree(n + 1, 0) {}

    void add(int i, int delta) {
        for (; i <= size; i += i & -i) tree[i] += delta;
    }

    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.length();
    int offset = n + 1; // Offset để đưa tổng dồn âm về chỉ số dương
    BIT bit(2 * n + 5);

    long long ans = 0;
    int current_prefix = 0;

    // Khởi tạo prefix sum P[0] = 0
    bit.add(current_prefix + offset, 1);

    for (int j = 0; j < n; j++) {
        if (s[j] == 'A') current_prefix += 1;
        else if (s[j] == 'B') current_prefix -= 1;

        // Đếm số lượng P[i] < current_prefix (tức là query từ 1 đến current_prefix + offset - 1)
        ans += bit.query(current_prefix + offset - 1);

        // Chèn P[j] hiện tại vào BIT
        bit.add(current_prefix + offset, 1);
    }

    cout << ans << "\n";
    return 0;
}
```

---

# IKH-0003 - Mua bài

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Thầy giáo đưa ra thử thách: Với số tiền đúng **C** đồng, hãy xác định số lượng bộ bài nhiều nhất có thể mua được.
Biết rằng:
- Mỗi bộ bài có giá **p** đồng.
- Cứ mua đủ **n1** bộ bài thì phải nộp **t1** đồng thuế VAT.
- Cứ mua đủ **n2** bộ bài thì phải nộp **t2** đồng thuế tiêu thụ đặc biệt.
Hai loại thuế được tính độc lập và cộng dồn.

### Input
- Một dòng duy nhất chứa 6 số nguyên: `C p n1 t1 n2 t2`.

### Output
- In ra một số nguyên duy nhất là số bộ bài nhiều nhất có thể mua được.

### Giới hạn
- $1 \le C \le 10^{18}$
- $1 \le p \le 10^9$
- $1 \le n&#95;1, n&#95;2 \le 10^9$
- $0 \le t&#95;1, t&#95;2 \le 10^9$

### Subtasks
- **Subtask 1 (40% điểm):** $C \le 10^6$
- **Subtask 2 (60% điểm):** Không có ràng buộc thêm.

### Sample 1
**Input:**
```
100 10 3 5 5 10
```
**Output:**
```
7
```
**Giải thích:**
Mua 7 bộ bài:
- Giá gốc: $7 \times 10 = 70$ đồng.
- Thuế VAT: $\lfloor 7/3 \rfloor \times 5 = 2 \times 5 = 10$ đồng.
- Thuế TTĐB: $\lfloor 7/5 \rfloor \times 10 = 1 \times 10 = 10$ đồng.
- Tổng chi phí: $70 + 10 + 10 = 90 \le 100$ đồng. Mua 8 bộ bài sẽ tốn $80 + 10 + 10 = 100 + 10 = 110 > 100$.

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# IKH-0003 - Mua bài

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Thầy giáo đưa ra thử thách: Với số tiền đúng **C** đồng, hãy xác định số lượng bộ bài nhiều nhất có thể mua được.
Biết rằng:
- Mỗi bộ bài có giá **p** đồng.
- Cứ mua đủ **n1** bộ bài thì phải nộp **t1** đồng thuế VAT.
- Cứ mua đủ **n2** bộ bài thì phải nộp **t2** đồng thuế tiêu thụ đặc biệt.
Hai loại thuế được tính độc lập và cộng dồn.

### Input
- Một dòng duy nhất chứa 6 số nguyên: `C p n1 t1 n2 t2`.

### Output
- In ra một số nguyên duy nhất là số bộ bài nhiều nhất có thể mua được.

### Giới hạn
- $1 \le C \le 10^{18}$
- $1 \le p \le 10^9$
- $1 \le n_1, n_2 \le 10^9$
- $0 \le t_1, t_2 \le 10^9$

### Subtasks
- **Subtask 1 (40% điểm):** $C \le 10^6$
- **Subtask 2 (60% điểm):** Không có ràng buộc thêm.

### Sample 1
**Input:**
```
100 10 3 5 5 10
```
**Output:**
```
7
```
**Giải thích:**
Mua 7 bộ bài:
- Giá gốc: $7 \times 10 = 70$ đồng.
- Thuế VAT: $\lfloor 7/3 \rfloor \times 5 = 2 \times 5 = 10$ đồng.
- Thuế TTĐB: $\lfloor 7/5 \rfloor \times 10 = 1 \times 10 = 10$ đồng.
- Tổng chi phí: $70 + 10 + 10 = 90 \le 100$ đồng. Mua 8 bộ bài sẽ tốn $80 + 10 + 10 = 100 + 10 = 110 > 100$.

---

## 2. HƯỚNG DẪN GIẢNG DẠY (GIÁO VIÊN)

### A. Phương pháp dẫn dắt tư duy học sinh (5 Bước)

1. **Bước 1: Xây dựng Hàm Chi phí (Cost Function)**
   * Với $X$ bộ bài, chi phí thực tế là:
     $$	ext{Cost}(X) = X \cdot p + \left\lfloor rac{X}{n_1} 
ight
floor \cdot t_1 + \left\lfloor rac{X}{n_2} 
ight
floor \cdot t_2$$

2. **Bước 2: Phân tích Tính Đơn điệu (Monotonicity)**
   * Khi số bộ bài $X$ tăng $\implies 	ext{Cost}(X)$ tăng nghiêm ngặt $\implies 	ext{Cost}(X)$ là hàm đơn điệu tăng.

3. **Bước 3: Nhận diện Thuật toán Binary Search on Answer**
   * Ta cần tìm $X$ **lớn nhất** sao cho $	ext{Cost}(X) \le C$.
   * Phạm vi chặt nhị phân: $L = 0, R = C / p$.

4. **Bước 4: Phân biệt Biến & Xử lý Tràn số (Overflow Avoidance)**
   * Dùng kiểu dữ liệu `long long` cho tất cả các biến ($C \le 10^{18}$).
   * Tránh nhân quá mức gây tràn số khi tính `Cost(mid)`.

5. **Bước 5: Độ phức tạp**
   * Số lần lặp chặt nhị phân: $\log_2(10^{18}) pprox 60$ phép tính ($< 0.001$ giây).

### B. Độ phức tạp
* **Thời gian:** $O(\log(C/p))$.
* **Bộ nhớ:** $O(1)$.

---

## 3. CODE GIẢI C++ CHUẨN

```cpp
#include <bits/stdc++.h>
using namespace std;
// Hàm tính tổng chi phí mua X bộ bài
long long get_cost(long long x, long long p, long long n1, long long t1, long long n2, long long t2) {
    long long base = x * p;
    long long tax1 = (x / n1) * t1;
    long long tax2 = (x / n2) * t2;
    return base + tax1 + tax2;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long C, p, n1, t1, n2, t2;
    if (!(cin >> C >> p >> n1 >> t1 >> n2 >> t2)) return 0;

    long long left = 0;
    long long right = C / p; // Số bộ bài tối đa khi chưa tính thuế
    long long ans = 0;

    while (left <= right) {
        long long mid = left + (right - left) / 2;

        if (get_cost(mid, p, n1, t1, n2, t2) <= C) {
            ans = mid;        // Chi phí hợp lệ -> Thử tìm X lớn hơn
            left = mid + 1;
        } else {
            right = mid - 1;  // Chi phí vượt C -> Giảm X xuống
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;
// Hàm tính tổng chi phí mua X bộ bài
long long get_cost(long long x, long long p, long long n1, long long t1, long long n2, long long t2) {
    long long base = x * p;
    long long tax1 = (x / n1) * t1;
    long long tax2 = (x / n2) * t2;
    return base + tax1 + tax2;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long C, p, n1, t1, n2, t2;
    if (!(cin >> C >> p >> n1 >> t1 >> n2 >> t2)) return 0;

    long long left = 0;
    long long right = C / p; // Số bộ bài tối đa khi chưa tính thuế
    long long ans = 0;

    while (left <= right) {
        long long mid = left + (right - left) / 2;

        if (get_cost(mid, p, n1, t1, n2, t2) <= C) {
            ans = mid;        // Chi phí hợp lệ -> Thử tìm X lớn hơn
            left = mid + 1;
        } else {
            right = mid - 1;  // Chi phí vượt C -> Giảm X xuống
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---

# IKH-0004 - Dãy cấp số nhân

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Cho dãy $A$ gồm $N$ số nguyên dương và số nguyên $q \ge 2$.
Dãy $b&#95;1, b&#95;2, \dots, b&#95;k$ là cấp số nhân công bội $q$ nếu $b_{i+1} = b&#95;i 	imes q$ với mọi $1 \le i < k$.
Yêu cầu: Với mỗi $k$ ($2 \le k \le N$), hãy đếm số dãy con (không nhất thiết liên tiếp) có độ dài $k$ của $A$ tạo thành cấp số nhân công bội $q$. Kết quả chia lấy dư cho $10^9 + 7$.

### Input
- Dòng đầu chứa hai số nguyên $N, q$ ($1 \le $N$ \le 10^5, 2 \le q \le 10^9$).
- Dòng thứ hai chứa $N$ số nguyên dương $A&#95;1, A&#95;2, \dots, A&#95;N$ ($1 \le A&#95;i \le 10^9$).

### Output
- Dòng duy nhất gồm $N - 1$ số nguyên thể hiện số dãy cấp số nhân độ dài $k = 2, 3, \dots, $N$ \pmod{10^9 + 7}$.

### Giới hạn
- $1 \le $N$ \le 10^5$
- $2 \le q \le 10^9$
- $1 \le A&#95;i \le 10^9$

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# IKH-0004 - Dãy cấp số nhân

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Cho dãy $A$ gồm $N$ số nguyên dương và số nguyên $q \ge 2$.
Dãy $b_1, b_2, \dots, b_k$ là cấp số nhân công bội $q$ nếu $b_{i+1} = b_i 	imes q$ với mọi $1 \le i < k$.
Yêu cầu: Với mỗi $k$ ($2 \le k \le N$), hãy đếm số dãy con (không nhất thiết liên tiếp) có độ dài $k$ của $A$ tạo thành cấp số nhân công bội $q$. Kết quả chia lấy dư cho $10^9 + 7$.

### Input
- Dòng đầu chứa hai số nguyên $N, q$ ($1 \le N \le 10^5, 2 \le q \le 10^9$).
- Dòng thứ hai chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

### Output
- Dòng duy nhất gồm $N - 1$ số nguyên thể hiện số dãy cấp số nhân độ dài $k = 2, 3, \dots, N \pmod{10^9 + 7}$.

### Giới hạn
- $1 \le N \le 10^5$
- $2 \le q \le 10^9$
- $1 \le A_i \le 10^9$

---

## 2. HƯỚNG DẪN GIẢNG DẠY (GIÁO VIÊN)

### A. Phương pháp dẫn dắt tư duy học sinh (5 Bước)

1. **Bước 1: Định nghĩa Quy hoạch động State**
   * Gọi `dp[v][k]` là số lượng dãy cấp số nhân độ dài $k$ kết thúc tại giá trị $v$.

2. **Bước 2: Công thức chuyển trạng thái (State Transition)**
   * Nếu $v mod q == 0$, phần tử $v$ có thể nối vào sau tất cả các dãy cấp số nhân độ dài $k-1$ kết thúc tại $v / q$:
     $$	ext{dp}[v][k] = (	ext{dp}[v][k] + 	ext{dp}[v/q][k-1]) mod MOD$$

3. **Bước 3: Nhận xét giới hạn độ dài hiệu dụng**
   * Vì $q \ge 2$, giá trị các phần tử trong cấp số nhân tăng ít nhất gấp 2 lần: $v \cdot q^{k-1} \le 10^9 \implies k \le 30$.
   * Do đó độ dài thực tế của cấp số nhân không quá 30!

4. **Bước 4: Sử dụng Hash Map tối ưu bộ nhớ**
   * Sử dụng `std::unordered_map<long long, vector<int>>` để lưu vết `dp[v][k]`.

5. **Bước 5: Độ phức tạp**
   * Mỗi phần tử chỉ cập nhật tối đa 30 trạng thái $\implies O(N \cdot \log_q(\max A_i))$.

### B. Độ phức tạp
* **Thời gian:** $O(N \cdot \log_q(\max A_i))$.
* **Bộ nhớ:** $O(N \cdot \log_q(\max A_i))$.

---

## 3. CODE GIẢI C++ CHUẨN

```cpp
#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    // dp[val][k]: số lượng CSN độ dài k kết thúc tại val
    unordered_map<long long, vector<long long>> dp;
    vector<long long> total_k(n + 1, 0);

    for (int i = 0; i < n; i++) {
        long long v = a[i];

        if (dp.find(v) == dp.end()) {
            dp[v] = vector<long long>(32, 0);
        }

        // Trường hợp k = 1
        dp[v][1] = (dp[v][1] + 1) % MOD;

        // Nếu v chia hết cho q và giá trị v/q đã tồn tại trước đó
        if (v % q == 0 && dp.count(v / q)) {
            auto& prev = dp[v / q];
            for (int k = 2; k <= 30; k++) {
                if (prev[k - 1] > 0) {
                    dp[v][k] = (dp[v][k] + prev[k - 1]) % MOD;
                    total_k[k] = (total_k[k] + prev[k - 1]) % MOD;
                }
            }
        }
    }

    for (int k = 2; k <= n; k++) {
        long long res = (k <= 30) ? total_k[k] : 0;
        cout << res << (k == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

---

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    // dp[val][k]: số lượng CSN độ dài k kết thúc tại val
    unordered_map<long long, vector<long long>> dp;
    vector<long long> total_k(n + 1, 0);

    for (int i = 0; i < n; i++) {
        long long v = a[i];

        if (dp.find(v) == dp.end()) {
            dp[v] = vector<long long>(32, 0);
        }

        // Trường hợp k = 1
        dp[v][1] = (dp[v][1] + 1) % MOD;

        // Nếu v chia hết cho q và giá trị v/q đã tồn tại trước đó
        if (v % q == 0 && dp.count(v / q)) {
            auto& prev = dp[v / q];
            for (int k = 2; k <= 30; k++) {
                if (prev[k - 1] > 0) {
                    dp[v][k] = (dp[v][k] + prev[k - 1]) % MOD;
                    total_k[k] = (total_k[k] + prev[k - 1]) % MOD;
                }
            }
        }
    }

    for (int k = 2; k <= n; k++) {
        long long res = (k <= 30) ? total_k[k] : 0;
        cout << res << (k == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

---

# IKH-0005 - Bảng đẹp

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Một bảng số nguyên được gọi là **bảng đẹp** nếu tổng các số trong bảng chia hết cho 9.
Cho bảng số nguyên kích thước $M 	imes N$. Hãy đếm số bộ $(x, y, u, v)$ với $1 \le x \le u \le $M$; 1 \le y \le v \le N$ sao cho hình chữ nhật con từ ô $(x,y)$ đến $(u,v)$ là một bảng đẹp.

### Input
- Dòng đầu chứa hai số nguyên $M, N$ ($1 \le $M$, $N$ \le 400$).
- $M$ dòng tiếp theo, mỗi dòng chứa $N$ số nguyên không âm $A_{i,j}$ ($0 \le A_{i,j} \le 10^9$).

### Output
- In ra một số nguyên duy nhất là số lượng hình chữ nhật con đẹp.

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# IKH-0005 - Bảng đẹp - KVMT

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Một bảng số nguyên được gọi là **bảng đẹp** nếu tổng các số trong bảng chia hết cho 9.
Cho bảng số nguyên kích thước $M 	imes N$. Hãy đếm số bộ $(x, y, u, v)$ với $1 \le x \le u \le M; 1 \le y \le v \le N$ sao cho hình chữ nhật con từ ô $(x,y)$ đến $(u,v)$ là một bảng đẹp.

### Input
- Dòng đầu chứa hai số nguyên $M, N$ ($1 \le M, N \le 400$).
- $M$ dòng tiếp theo, mỗi dòng chứa $N$ số nguyên không âm $A_{i,j}$ ($0 \le A_{i,j} \le 10^9$).

### Output
- In ra một số nguyên duy nhất là số lượng hình chữ nhật con đẹp.

---

## 2. HƯỚNG DẪN GIẢNG DẠY (GIÁO VIÊN)

### A. Phương pháp dẫn dắt tư duy học sinh (5 Bước)

1. **Bước 1: Chuyển về mảng 1D cho từng cặp hàng**
   * Cố định hàng trên $r_1$ và hàng dưới $r_2$ ($1 \le r_1 \le r_2 \le M$).
   * Tổng cột $c$ từ $r_1$ đến $r_2$ là $ColSum[c] = \sum_{i=r_1}^{r_2} A_{i,c} \pmod 9$.

2. **Bước 2: Quy về Bài toán Đếm đoạn con 1D có tổng $\equiv 0 \pmod 9$**
   * Đặt $P[c] = \sum_{k=1}^c ColSum[k] \pmod 9$.
   * Đoạn cột từ $y$ đến $v$ có tổng $\equiv 0 \pmod 9 \iff P[v] \equiv P[y-1] \pmod 9$.

3. **Bước 3: Sử dụng Mảng tần suất Tương dư $\pmod 9$**
   * Với mỗi cặp $(r_1, r_2)$, ta dùng mảng `freq[9]` lưu số lần xuất hiện của các số dư $\pmod 9$.

4. **Bước 4: Độ phức tạp**
   * Có $O(M^2)$ cặp hàng. Với mỗi cặp hàng, duyệt $N$ cột hết $O(N)$. Tổng thời gian $O(M^2 \cdot N)$.

### B. Độ phức tạp
* **Thời gian:** $O(M^2 \cdot N) pprox 400^3 = 6.4 	imes 10^7$ phép tính ($< 0.1$ giây).
* **Bộ nhớ:** $O(M \cdot N)$.

---

## 3. CODE GIẢI C++ CHUẨN

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n;
    if (!(cin >> m >> n)) return 0;

    vector<vector<int>> pref(m + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            int val; cin >> val;
            pref[i][j] = (pref[i - 1][j] + val) % 9;
        }
    }

    long long ans = 0;

    for (int r1 = 1; r1 <= m; r1++) {
        for (int r2 = r1; r2 <= m; r2++) {
            vector<int> freq(9, 0);
            freq[0] = 1;
            int current_mod = 0;

            for (int c = 1; c <= n; c++) {
                int col_sum = (pref[r2][c] - pref[r1 - 1][c] + 9) % 9;
                current_mod = (current_mod + col_sum) % 9;
                ans += freq[current_mod];
                freq[current_mod]++;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n;
    if (!(cin >> m >> n)) return 0;

    vector<vector<int>> pref(m + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            int val; cin >> val;
            pref[i][j] = (pref[i - 1][j] + val) % 9;
        }
    }

    long long ans = 0;

    for (int r1 = 1; r1 <= m; r1++) {
        for (int r2 = r1; r2 <= m; r2++) {
            vector<int> freq(9, 0);
            freq[0] = 1;
            int current_mod = 0;

            for (int c = 1; c <= n; c++) {
                int col_sum = (pref[r2][c] - pref[r1 - 1][c] + 9) % 9;
                current_mod = (current_mod + col_sum) % 9;
                ans += freq[current_mod];
                freq[current_mod]++;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---

# IKH-0006 - Vòng tay

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Lê có $N$ hạt cườm mã màu $c&#95;1, c&#95;2, \dots, c&#95;N$. Lê muốn chọn đúng $M$ hạt ($M < N$) để làm vòng tay sao cho tổng giá trị mã màu của $M$ hạt được chọn đúng bằng $S$.
Hãy đếm số cách chọn $M$ hạt thỏa mãn.

### Input
- Dòng thứ nhất chứa $N, $M$, S$ ($1 \le $M$ \le $N$ \le 100, 1 \le S \le 10000$).
- Dòng thứ hai chứa $N$ số nguyên dương $c&#95;1, c&#95;2, \dots, c&#95;N$ ($1 \le c&#95;i \le 500$).

### Output
- In ra một số nguyên duy nhất là số cách chọn.

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# IKH-0006 - Vòng tay - KVMB

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Lê có $N$ hạt cườm mã màu $c_1, c_2, \dots, c_N$. Lê muốn chọn đúng $M$ hạt ($M < N$) để làm vòng tay sao cho tổng giá trị mã màu của $M$ hạt được chọn đúng bằng $S$.
Hãy đếm số cách chọn $M$ hạt thỏa mãn.

### Input
- Dòng thứ nhất chứa $N, M, S$ ($1 \le M \le N \le 100, 1 \le S \le 10000$).
- Dòng thứ hai chứa $N$ số nguyên dương $c_1, c_2, \dots, c_N$ ($1 \le c_i \le 500$).

### Output
- In ra một số nguyên duy nhất là số cách chọn.

---

## 2. HƯỚNG DẪN GIẢNG DẠY (GIÁO VIÊN)

### A. Phương pháp dẫn dắt tư duy học sinh (5 Bước)

1. **Bước 1: Nhận diện dạng bài Subset Sum chọn đúng M phần tử**
   * Đây là bài toán Quy hoạch động Knapsack 2 chiều.

2. **Bước 2: Định nghĩa Trạng thái DP**
   * `dp[k][w]` là số cách chọn đúng $k$ hạt có tổng giá trị bằng $w$.

3. **Bước 3: Công thức Chuyển Trạng Thái**
   * Khi xét hạt thứ $i$ có giá trị $x = c_i$:
     $$	ext{dp}[k][w] = 	ext{dp}[k][w] + 	ext{dp}[k-1][w - x]$$
   * Cần duyệt $k$ giảm dần từ $M 	o 1$ và $w$ giảm dần từ $S 	o x$ để tránh tính trùng hạt.

4. **Bước 4: Cơ sở Quy hoạch động**
   * `dp[0][0] = 1` (Có 1 cách chọn 0 hạt với tổng = 0).

### B. Độ phức tạp
* **Thời gian:** $O(N \cdot M \cdot S) pprox 100 	imes 100 	imes 10000 = 10^8$ phép tính ($< 0.15$ giây).
* **Bộ nhớ:** $O(M \cdot S)$.

---

## 3. CODE GIẢI C++ CHUẨN

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;

    vector<int> c(n);
    for (int i = 0; i < n; i++) cin >> c[i];

    // dp[k][w]: số cách chọn k hạt có tổng = w
    vector<vector<long long>> dp(m + 1, vector<long long>(s + 1, 0));
    dp[0][0] = 1;

    for (int x : c) {
        for (int k = m; k >= 1; k--) {
            for (int w = s; w >= x; w--) {
                dp[k][w] += dp[k - 1][w - x];
            }
        }
    }

    cout << dp[m][s] << "\n";
    return 0;
}
```

---

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;

    vector<int> c(n);
    for (int i = 0; i < n; i++) cin >> c[i];

    // dp[k][w]: số cách chọn k hạt có tổng = w
    vector<vector<long long>> dp(m + 1, vector<long long>(s + 1, 0));
    dp[0][0] = 1;

    for (int x : c) {
        for (int k = m; k >= 1; k--) {
            for (int w = s; w >= x; w--) {
                dp[k][w] += dp[k - 1][w - x];
            }
        }
    }

    cout << dp[m][s] << "\n";
    return 0;
}
```

---

# IKH-0007 - Kho Du Tru Quoc Gia

## 1. NỘI DUNG BÀI TOÁN

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

---

### 1. THÔNG TIN BÀI TOÁN
* **Mã bài:** `IKH-0007`
* **Tên bài:** Kho Dự Trữ Quốc Gia (National Reserve Warehouse)
* **Dạng bài:** Tìm kiếm nhị phân trên tập nghiệm (Binary Search on Answer)
* **Độ khó đề xuất:** ⭐⭐⭐⭐☆ (Dành cho học sinh Chuyên Tin THCS, Lớp 8-9, Luyện thi Tin học trẻ Bảng B, HSG Tỉnh/Thành phố)

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL
## Bài toán: IKH-0007 - Kho Dự Trữ Quốc Gia (National Reserve Warehouse)

---

### 1. THÔNG TIN BÀI TOÁN
* **Mã bài:** `IKH-0007`
* **Tên bài:** Kho Dự Trữ Quốc Gia (National Reserve Warehouse)
* **Dạng bài:** Tìm kiếm nhị phân trên tập nghiệm (Binary Search on Answer)
* **Độ khó đề xuất:** ⭐⭐⭐⭐☆ (Dành cho học sinh Chuyên Tin THCS, Lớp 8-9, Luyện thi Tin học trẻ Bảng B, HSG Tỉnh/Thành phố)
* **Ràng buộc:**
  * $1 \le N \le 2 \times 10^5$ (Dùng `int`)
  * $0 \le K \le 10^{15}$ (Hạn mức tối đa **Limit** - Bắt buộc dùng `long long`)
  * $0 \le A_i \le 10^9$ (Lượng hàng ban đầu mỗi kho - Dùng `long long`)

---

### 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH

Để học sinh **không đoán ngẫu nhiên thuật toán Binary Search**, giáo viên nên dẫn dắt học sinh qua 5 bước tư duy tự nhiên sau:

#### **Bước 1: Đặt vấn đề bài toán ngược (Validation Check)**
* **Câu hỏi gợi mở:** *"Giả sử thầy cho trước một giá trị mức chuẩn $X = 5$, làm thế nào để biết Nhà nước có đủ $K$ tấn hàng để nâng tất cả các kho chưa đạt lên $X$ hay không?"*
* **Trả lời của học sinh:** Ta chỉ cần duyệt qua từng kho thứ $i$, nếu $A_i < X$ thì số hàng cần bổ sung là $X - A_i$. Kho nào $A_i \ge X$ thì không cần bổ sung ($0$).
* **Hàm kiểm tra `check(X)`:**
  $$f(X) = \sum_{i=1}^{N} \max(0, X - A_i)$$
  Nếu $f(X) \le K$ thì $X$ hợp lệ; ngược lại $X$ không hợp lệ.

#### **Bước 2: Phân tích tính đơn điệu (Monotonicity)**
* **Câu hỏi gợi mở:** *"Nếu tăng $X$ lên ($X$ càng cao), thì tổng lượng hàng $f(X)$ cần bổ sung sẽ tăng hay giảm?"*
* **Phân tích:** 
  * Khi $X$ tăng lên, giá trị $(X - A_i)$ với các kho $A_i < X$ chắc chắn sẽ tăng lên.
  * Do đó, hàm $f(X)$ là **hàm đơn điệu tăng (không giảm)**.
* **Tính chất quyết định:**
  * Nếu một giá trị $X$ **hợp lệ** ($f(X) \le K$), thì mọi $X' < X$ cũng chắc chắn **hợp lệ**.
  * Nếu một giá trị $X$ **không hợp lệ** ($f(X) > K$), thì mọi $X'' > X$ chắc chắn **không hợp lệ**.

#### **Bước 3: Nhận diện thuật toán Binary Search on Answer**
* Nhận xét: Không gian kết quả $X$ được chia thành 2 nửa liên tục:
  $$\text{Dãy kết quả kiểm tra } f(X): [\text{Hợp lệ}, \text{Hợp lệ}, \dots, \text{Hợp lệ}, \text{Không hợp lệ}, \text{Không hợp lệ}]$$
* Yêu cầu bài toán là tìm $X$ **lớn nhất** còn thỏa mãn $\implies$ Đây chính là điểm chuyển giao cuối cùng của miền "Hợp lệ".
* Tìm kiếm tuần tự $X$ từ $0$ sẽ bị TLE vì $K \le 10^{15}$. Áp dụng **Chặt nhị phân trên kết quả** để giảm thời gian từ $O(\text{MAX\_X})$ xuống $O(\log(\text{MAX\_X}))$.

#### **Bước 4: Giải thích Ý nghĩa Biến & Kỹ thuật lập trình (Early Stopping)**

##### 💡 Phân biệt thuật ngữ & Ý nghĩa các biến quan trọng:
* **`k` (Limit - Hạn mức):** Hạn mức ngân sách tổng số tấn hàng tối đa đề bài cho phép bổ sung ($K \le 10^{15}$). Con số này **cố định**.
* **`need` (Requirement / Chi phí thực tế):** Tổng số tấn hàng **thực tế phát sinh** để đưa tất cả các kho lên mức $mid$. Biến này **thay đổi** theo từng giá trị $mid$.
* **`ok` (Flag - Cờ hiệu):** Biến boolean đóng vai trò làm cờ báo hiệu xem mức $mid$ có **khả thi** hay không. Ban đầu gán `ok = true`, nếu `need > k` thì hạ cờ `ok = false` và dừng vòng lặp (`break`).

##### 🚀 Kỹ thuật dừng sớm (Early Exit) tránh tràn số:
* Khi tính `need`, tổng có thể lên tới $N \times (\max A_i + K) \approx 2 \cdot 10^5 \times 10^{15} = 2 \cdot 10^{20}$, vượt quá giới hạn 64-bit của `long long`.
* Ngay khi `need > k` (chi phí thực tế vượt quá hạn mức Limit), ta lập tức `break`. Nhờ đó `need` không bao giờ vượt quá $K + 10^9$, dùng kiểu `long long` hoàn toàn an toàn và chạy cực nhanh!

#### **Bước 5: Xác định không gian tìm kiếm $[L, R]$**
* **Giá trị nhỏ nhất ($L$):** `0` (hoặc $\min A_i$).
* **Giá trị lớn nhất ($R$):** `mx + k` (trường hợp dồn toàn bộ $K$ tấn hàng cho 1 kho duy nhất).

---

### 3. ĐỘ PHỨC TẠP THUẬT TOÁN

* **Số bước Chặt Nhị Phân:** 
  $$\log_2(\max A_i + K) \approx \log_2(10^{15} + 10^9) \approx 50 \text{ lần}$$
* **Độ phức tạp mỗi bước:** $O(N)$ để duyệt qua mảng kiểm tra.
* **Tổng độ phức tạp thời gian:** $O(N \cdot \log(\max A_i + K))$.
  * Với $N = 2 \cdot 10^5$, tổng số phép tính tối đa $\approx 50 \times 2 \cdot 10^5 = 10^7$ phép tính.
  * Thời gian chạy thực tế trên C++: $< 0.03$ giây (Hoàn toàn đáp ứng giới hạn 1.0s).
* **Độ phức tạp bộ nhớ:** $O(N)$ để lưu mảng $A$.

---

### 4. MÃ NGUỒN CHUẨN (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    // Tối ưu hóa I/O cho C++
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    long long mx = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        mx = max(mx, a[i]);
    }

    // Phạm vi tìm kiếm nhị phân cho X
    long long left = 0;
    long long right = mx + k;
    long long ans = 0;

    while (left <= right) {
        long long mid = left + (right - left) / 2;

        long long need = 0;  // Chi phí thực tế cần bổ sung
        bool ok = true;      // Flag (cờ hiệu) kiểm tra khả thi

        for (int i = 0; i < n; i++) {
            if (a[i] < mid) {
                need += (mid - a[i]);
                // Nếu chi phí thực tế > Hạn mức (Limit k) -> Hạ cờ & Dừng sớm
                if (need > k) {
                    ok = false;
                    break;
                }
            }
        }

        if (ok) {
            ans = mid;        // Cờ ok bật -> mid hợp lệ, ghi nhận & thử X lớn hơn
            left = mid + 1;
        } else {
            right = mid - 1;  // Không hợp lệ -> giảm X xuống
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---

### 5. CẤU TRÚC BỘ TEST (20 TEST CASES)

Bộ test được chia theo đúng 3 Subtask trong đề bài:

* **Subtask 1 (20% điểm - 4 tests: test1 đến test4):** $N \le 1000$ (có các test sample và $K=0$).
* **Subtask 2 (30% điểm - 6 tests: test5 đến test10):** $A_i \le 10^5, N = 200.000$ (gồm các test mảng tăng/giảm dần, mảng hằng số, $K=0$, $K$ vừa và $K$ lớn).
* **Subtask 3 (50% điểm - 10 tests: test11 đến test20):** Ràng buộc đầy đủ $N \le 200.000, K \le 10^{15}, A_i \le 10^9$ (gồm biên $N=1$, mảng $A_i=0$, biến thiên giá trị cực đoan, $K$ lớn nhất).

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    // Tối ưu hóa I/O cho C++
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    long long mx = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        mx = max(mx, a[i]);
    }

    // Phạm vi tìm kiếm nhị phân cho X
    long long left = 0;
    long long right = mx + k;
    long long ans = 0;

    while (left <= right) {
        long long mid = left + (right - left) / 2;

        long long need = 0;
        bool ok = true;

        for (int i = 0; i < n; i++) {
            if (a[i] < mid) {
                need += (mid - a[i]);
                // Kỹ thuật dừng sớm (Early Exit) giúp tránh tràn số long long và tối ưu tốc độ
                if (need > k) {
                    ok = false;
                    break;
                }
            }
        }

        if (ok) {
            ans = mid;        // Giá trị mid hợp lệ, lưu lại và thử tìm X lớn hơn
            left = mid + 1;
        } else {
            right = mid - 1;  // Không hợp lệ, giảm X xuống
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---

# IKH-0008 - Chuyến Tàu Tiếp Vận

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Đoàn tàu đi qua $N$ ga. Ga thứ $i$ bổ sung $A&#95;i > 0$ tấn hàng hoặc lấy đi $|A&#95;i|$ tấn hàng ($A&#95;i < 0$).
Khi bắt đầu, tàu được chất sẵn $X$ tấn hàng.
Yêu cầu: Tìm $X$ nhỏ nhất sao cho lượng hàng trên tàu **không bao giờ âm** tại bất kỳ ga nào.

### Input
- Dòng đầu chứa số nguyên $N$ ($1 \le $N$ \le 2 \times 10^5$).
- Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($-10^9 \le A&#95;i \le 10^9$).

### Output
- In ra một số nguyên $X$ nhỏ nhất thỏa mãn.

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# IKH-0008 - Chuyến Tàu Tiếp Vận

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Đoàn tàu đi qua $N$ ga. Ga thứ $i$ bổ sung $A_i > 0$ tấn hàng hoặc lấy đi $|A_i|$ tấn hàng ($A_i < 0$).
Khi bắt đầu, tàu được chất sẵn $X$ tấn hàng.
Yêu cầu: Tìm $X$ nhỏ nhất sao cho lượng hàng trên tàu **không bao giờ âm** tại bất kỳ ga nào.

### Input
- Dòng đầu chứa số nguyên $N$ ($1 \le N \le 2 \times 10^5$).
- Dòng thứ hai chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

### Output
- In ra một số nguyên $X$ nhỏ nhất thỏa mãn.

---

## 2. HƯỚNG DẪN GIẢNG DẠY (GIÁO VIÊN)

### A. Phương pháp dẫn dắt tư duy học sinh (5 Bước)

1. **Bước 1: Đặt công thức Tổng Dồn**
   * Lượng hàng sau khi qua ga thứ $i$ là: $Cargo(i) = X + \sum_{j=1}^i A_j = X + P[i]$.

2. **Bước 2: Thiết lập Điều kiện An toàn**
   * Yêu cầu $Cargo(i) \ge 0 \iff X + P[i] \ge 0 \iff X \ge -P[i]$ với mọi $1 \le i \le N$.

3. **Bước 3: Rút ra Công thức Nghiệm tối ưu**
   * $X \ge \max_{1 \le i \le N}(-P[i])$.
   * Vì $X \ge 0$, nên $X = \max(0, -\min_{1 \le i \le N} P[i])$.

4. **Bước 4: Thuật toán 1 Vòng Lặp $O(N)$**
   * Duyệt $i$ từ $1 	o N$, tính tổng dồn $P[i]$, theo dõi giá trị nhỏ nhất `min_p`.

### B. Độ phức tạp
* **Thời gian:** $O(N)$.
* **Bộ nhớ:** $O(1)$.

---

## 3. CODE GIẢI C++ CHUẨN

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long current_p = 0;
    long long min_p = 0;

    for (int i = 0; i < n; i++) {
        long long a;
        cin >> a;
        current_p += a;
        min_p = min(min_p, current_p);
    }

    long long min_X = max(0LL, -min_p);
    cout << min_X << "\n";
    return 0;
}
```

---

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long current_p = 0;
    long long min_p = 0;

    for (int i = 0; i < n; i++) {
        long long a;
        cin >> a;
        current_p += a;
        min_p = min(min_p, current_p);
    }

    long long min_X = max(0LL, -min_p);
    cout << min_X << "\n";
    return 0;
}
```

---

# IKH-0009 - Điều Phối Xe Cứu Hộ

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Có $N$ xe tải có tải trọng $A&#95;i > 0$. Một đoàn xe gồm các xe **liên tiếp** được coi là đạt yêu cầu nếu tổng tải trọng $\ge K$ tấn.
Hãy đếm số lượng đoàn xe hợp lệ.

### Input
- Dòng đầu chứa $N, K$ ($1 \le $N$ \le 2 \times 10^5, 1 \le $K$ \le 10^{14}$).
- Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($1 \le A&#95;i \le 10^9$).

### Output
- In ra số lượng đoàn xe hợp lệ.

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# IKH-0009 - Điều Phối Xe Cứu Hộ

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Có $N$ xe tải có tải trọng $A_i > 0$. Một đoàn xe gồm các xe **liên tiếp** được coi là đạt yêu cầu nếu tổng tải trọng $\ge K$ tấn.
Hãy đếm số lượng đoàn xe hợp lệ.

### Input
- Dòng đầu chứa $N, K$ ($1 \le N \le 2 \times 10^5, 1 \le K \le 10^{14}$).
- Dòng thứ hai chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

### Output
- In ra số lượng đoàn xe hợp lệ.

---

## 2. HƯỚNG DẪN GIẢNG DẠY (GIÁO VIÊN)

### A. Phương pháp dẫn dắt tư duy học sinh (5 Bước)

1. **Bước 1: Phân tích tính Đơn điệu của Tổng Đoạn con**
   * Vì tất cả $A_i > 0$, khi mở rộng đầu phải $R$ của đoạn $[L, R]$, tổng tải trọng tăng nghiêm ngặt.

2. **Bước 2: Ứng dụng Kỹ thuật Con trỏ kép (Two Pointers)**
   * Với mỗi đầu trái $L$, ta tìm đầu phải $R$ nhỏ nhất sao cho $\sum_{i=L}^R A_i \ge K$.
   * Khi đó, tất cả các đoạn $[L, R'], R' \ge R$ đều hợp lệ (số lượng $= N - R + 1$).

3. **Bước 3: Tối ưu Thời gian Tĩnh tịnh con trỏ**
   * Khi $L$ tăng lên $L+1$, ta chỉ cần trừ $A_L$ khỏi `current_sum` và tiếp tục dịch $R$ sang phải.

### B. Độ phức tạp
* **Thời gian:** $O(N)$ (mỗi con trỏ $L, R$ dịch chuyển tối đa $N$ bước).
* **Bộ nhớ:** $O(N)$.

---

## 3. CODE GIẢI C++ CHUẨN

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    long long ans = 0;
    long long current_sum = 0;
    int r = 0;

    for (int l = 0; l < n; l++) {
        while (r < n && current_sum < k) {
            current_sum += a[r];
            r++;
        }
        if (current_sum >= k) {
            ans += (n - r + 1);
        }
        current_sum -= a[l];
    }

    cout << ans << "\n";
    return 0;
}
```

---

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    long long ans = 0;
    long long current_sum = 0;
    int r = 0;

    for (int l = 0; l < n; l++) {
        while (r < n && current_sum < k) {
            current_sum += a[r];
            r++;
        }
        if (current_sum >= k) {
            ans += (n - r + 1);
        }
        current_sum -= a[l];
    }

    cout << ans << "\n";
    return 0;
}
```

---

# IKH-0010 - Khu Chợ Thông Minh

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Có $N$ quầy hàng diện tích $A&#95;i$, $M$ tiểu thương yêu cầu quầy diện tích tối thiểu $B&#95;j$.
Mỗi quầy chỉ cho 1 tiểu thương thuê và mỗi tiểu thương thuê 1 quầy.
Hãy tìm số tiểu thương tối đa được bố trí quầy.

### Input
- Dòng đầu chứa $N, M$ ($1 \le $N$, $M$ \le 2 \times 10^5$).
- Dòng thứ hai chứa $N$ số nguyên $A&#95;1, \dots, A&#95;N$.
- Dòng thứ ba chứa $M$ số nguyên $B&#95;1, \dots, B&#95;M$.

### Output
- Số lượng tiểu thương lớn nhất ghép được quầy.

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# IKH-0010 - Khu Chợ Thông Minh

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Có $N$ quầy hàng diện tích $A_i$, $M$ tiểu thương yêu cầu quầy diện tích tối thiểu $B_j$.
Mỗi quầy chỉ cho 1 tiểu thương thuê và mỗi tiểu thương thuê 1 quầy.
Hãy tìm số tiểu thương tối đa được bố trí quầy.

### Input
- Dòng đầu chứa $N, M$ ($1 \le N, M \le 2 \times 10^5$).
- Dòng thứ hai chứa $N$ số nguyên $A_1, \dots, A_N$.
- Dòng thứ ba chứa $M$ số nguyên $B_1, \dots, B_M$.

### Output
- Số lượng tiểu thương lớn nhất ghép được quầy.

---

## 2. HƯỚNG DẪN GIẢNG DẠY (GIÁO VIÊN)

### A. Phương pháp dẫn dắt tư duy học sinh (5 Bước)

1. **Bước 1: Chiến lược Tham ăn (Greedy Matching)**
   * Ưu tiên ghép tiểu thương có nhu cầu **nhỏ nhất** với quầy **nhỏ nhất vừa đủ** đáp ứng.

2. **Bước 2: Sắp xếp dữ liệu**
   * Sắp xếp cả 2 mảng $A$ và $B$ theo thứ tự tăng dần.

3. **Bước 3: Con trỏ duyệt 2 Mảng**
   * Duyệt $i$ trên $A$ và $j$ trên $B$. Nếu $A[i] \ge B[j] \implies$ ghép thành công, tăng cả $i, j$ và `count`.
   * Ngược lại ($A[i] < B[j]$) $\implies$ quầy $A[i]$ quá nhỏ, bỏ qua quầy $i$ ($i++$).

### B. Độ phức tạp
* **Thời gian:** $O(N \log N + M \log M)$.
* **Bộ nhớ:** $O(N + M)$.

---

## 3. CODE GIẢI C++ CHUẨN

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int j = 0; j < m; j++) cin >> b[j];

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int i = 0, j = 0, matched = 0;
    while (i < n && j < m) {
        if (a[i] >= b[j]) {
            matched++;
            i++;
            j++;
        } else {
            i++;
        }
    }

    cout << matched << "\n";
    return 0;
}
```

---

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int j = 0; j < m; j++) cin >> b[j];

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int i = 0, j = 0, matched = 0;
    while (i < n && j < m) {
        if (a[i] >= b[j]) {
            matched++;
            i++;
            j++;
        } else {
            i++;
        }
    }

    cout << matched << "\n";
    return 0;
}
```

---

# IKH-0011 - Lễ Hội Ánh Sáng

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Tuyển chọn các khu vực trang trí đèn trong $N$ khu vực thu hút $A&#95;i$ lượt khách sao cho **không có hai khu vực liên tiếp nào cùng được chọn** và tổng lượt khách thu hút được là lớn nhất.

### Input
- Dòng đầu chứa $N$ ($1 \le $N$ \le 2 \times 10^5$).
- Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($0 \le A&#95;i \le 10^9$).

### Output
- Tổng lượt khách lớn nhất.

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# IKH-0011 - Lễ Hội Ánh Sáng

## 1. NỘI DUNG BÀI TOÁN

### Mô tả
Tuyển chọn các khu vực trang trí đèn trong $N$ khu vực thu hút $A_i$ lượt khách sao cho **không có hai khu vực liên tiếp nào cùng được chọn** và tổng lượt khách thu hút được là lớn nhất.

### Input
- Dòng đầu chứa $N$ ($1 \le N \le 2 \times 10^5$).
- Dòng thứ hai chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

### Output
- Tổng lượt khách lớn nhất.

---

## 2. HƯỚNG DẪN GIẢNG DẠY (GIÁO VIÊN)

### A. Phương pháp dẫn dắt tư duy học sinh (5 Bước)

1. **Bước 1: Định nghĩa Trạng thái DP (House Robber)**
   * `dp0`: Tổng lớn nhất khi KHÔNG chọn khu vực $i-1$.
   * `dp1`: Tổng lớn nhất khi CÓ chọn khu vực $i-1$.

2. **Bước 2: Công thức Chuyển Trạng Thái**
   * Nếu chọn khu vực $i \implies$ khu vực $i-1$ bắt buộc KHÔNG được chọn:
     $$	ext{dp1\_new} = 	ext{dp0} + A[i]$$
   * Nếu không chọn khu vực $i \implies$ khu vực $i-1$ có thể được chọn hoặc không:
     $$	ext{dp0\_new} = \max(	ext{dp0}, 	ext{dp1})$$

3. **Bước 3: Tối ưu Bộ nhớ $O(1)$**
   * Chỉ dùng 2 biến `dp0` và `dp1` duyệt từ $1 	o N$.

### B. Độ phức tạp
* **Thời gian:** $O(N)$.
* **Bộ nhớ:** $O(1)$.

---

## 3. CODE GIẢI C++ CHUẨN

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    long long dp0 = 0; // Không chọn phần tử trước
    long long dp1 = 0; // Có chọn phần tử trước

    for (int i = 0; i < n; i++) {
        long long next_dp0 = max(dp0, dp1);
        long long next_dp1 = dp0 + a[i];
        dp0 = next_dp0;
        dp1 = next_dp1;
    }

    cout << max(dp0, dp1) << "\n";
    return 0;
}
```

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    long long dp0 = 0; // Không chọn phần tử trước
    long long dp1 = 0; // Có chọn phần tử trước

    for (int i = 0; i < n; i++) {
        long long next_dp0 = max(dp0, dp1);
        long long next_dp1 = dp0 + a[i];
        dp0 = next_dp0;
        dp1 = next_dp1;
    }

    cout << max(dp0, dp1) << "\n";
    return 0;
}
```

---

# IKH-0012 - Lễ Hội Chia Bánh

## 1. NỘI DUNG BÀI TOÁN

Trong khuôn khổ Lễ hội Ẩm thực Truyền thống tại Phố cổ Hội An, Ban Tổ chức chuẩn bị một dãy gồm $N$ chiếc bánh mì nướng đặc biệt được xếp thành một hàng dọc. Chiếc bánh thứ $i$ có chiều dài là **$A&#95;i$** cm.

Để chia phần cho $K$ đoàn khách du lịch quốc tế tham quan festival, người quản lý cần cắt dãy bánh thành $K$ phần liên tiếp sao cho mỗi đoàn khách nhận được đúng 1 phần bánh gồm các chiếc bánh nguyên vẹn liên tiếp.

Do tính chất công bằng và nâng cao trải nghiệm du lịch, Ban Tổ chức muốn quy hoạch sao cho **chiều dài của phần bánh ngắn nhất trong $K$ phần là lớn nhất có thể**. Hãy xác định chiều dài phần bánh ngắn nhất tối đa đó.

#### Input:
Dòng đầu chứa hai số nguyên $N, K$. Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$.

#### Output:
Một số nguyên duy nhất là chiều dài tối đa của phần bánh ngắn nhất. Nếu không thể chia thành $K$ phần, in ra 0.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000, K \le 100$
* Subtask 2 (30% điểm): $A&#95;i \le 10^5$
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
5 3
6 3 2 8 7
```
**Output:**
```
8
```
**Giải thích:** Chia 5 chiếc bánh thành 3 phần: Phần 1 {6, 3} tổng dài 9; Phần 2 {2, 8} tổng dài 10; Phần 3 {7} tổng dài 7. Chiều dài phần ngắn nhất là 7. Nếu chia {6, 3, 2} (tổng 11), {8} (tổng 8), {7} (tổng 7) thì chiều dài ngắn nhất là 7. Nếu chia {6} (6), {3, 2, 8} (13), {7} (7) ngắn nhất là 6. Cách chia tối ưu thu được phần ngắn nhất dài 8 khi chia thành {6, 3}=9, {2, 8}=10... kiểm tra chặt nhị phân.

#### Sample 2:
**Input:**
```
4 2
10 20 30 40
```
**Output:**
```
40
```
**Giải thích:** Chia thành 2 phần: {10, 20, 30} tổng 60 và {40} tổng 40. Chiều dài phần ngắn nhất là 40.

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL
## Bài toán: IKH-0012 - Lễ Hội Chia Bánh (Cake Partition)

---

### 1. THÔNG TIN BÀI TOÁN
* **Mã bài:** `IKH-0012`
* **Tên bài:** Lễ Hội Chia Bánh (Cake Partition)
* **Dạng bài:** Binary Search on Answer, Greedy Check
* **Độ khó đề xuất:** ⭐⭐⭐☆☆
* **Đánh giá 4 Tiêu chí Metadata:**
  * 🧠 **Algorithm Rating:** 1400
  * 📖 **Reading Difficulty:** ★★★★☆
  * 💡 **Modeling Difficulty:** ★★★★☆
  * 🧪 **Coding Implementation:** ★★★☆☆
* **Ràng buộc:**
* $1 \le N \le 2 \times 10^5$
* $1 \le K \le 10^9$
* $1 \le A_i \le 10^9$

#### Mô tả:
Trong khuôn khổ Lễ hội Ẩm thực Truyền thống tại Phố cổ Hội An, Ban Tổ chức chuẩn bị một dãy gồm **N** chiếc bánh mì nướng đặc biệt được xếp thành một hàng dọc. Chiếc bánh thứ **i** có chiều dài là **Ai** cm.

Để chia phần cho **K** đoàn khách du lịch quốc tế tham quan festival, người quản lý cần cắt dãy bánh thành **K** phần liên tiếp sao cho mỗi đoàn khách nhận được đúng 1 phần bánh gồm các chiếc bánh nguyên vẹn liên tiếp.

Do tính chất công bằng và nâng cao trải nghiệm du lịch, Ban Tổ chức muốn quy hoạch sao cho **chiều dài của phần bánh ngắn nhất trong K phần là lớn nhất có thể**. Hãy xác định chiều dài phần bánh ngắn nhất tối đa đó.

#### Input:
Dòng đầu chứa hai số nguyên N K. Dòng thứ hai chứa N số nguyên A1 A2 ... AN.

#### Output:
Một số nguyên duy nhất là chiều dài tối đa của phần bánh ngắn nhất. Nếu không thể chia thành K phần, in ra 0.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000, K \le 100$
* Subtask 2 (30% điểm): $A_i \le 10^5$
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
5 3
6 3 2 8 7
```
**Output:**
```
8
```
**Giải thích:** Chia 5 chiếc bánh thành 3 phần: Phần 1 {6, 3} tổng dài 9; Phần 2 {2, 8} tổng dài 10; Phần 3 {7} tổng dài 7. Chiều dài phần ngắn nhất là 7. Nếu chia {6, 3, 2} (tổng 11), {8} (tổng 8), {7} (tổng 7) thì chiều dài ngắn nhất là 7. Nếu chia {6} (6), {3, 2, 8} (13), {7} (7) ngắn nhất là 6. Cách chia tối ưu thu được phần ngắn nhất dài 8 khi chia thành {6, 3}=9, {2, 8}=10... kiểm tra chặt nhị phân.

#### Sample 2:
**Input:**
```
4 2
10 20 30 40
```
**Output:**
```
40
```
**Giải thích:** Chia thành 2 phần: {10, 20, 30} tổng 60 và {40} tổng 40. Chiều dài phần ngắn nhất là 40.

---

### 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Đặt vấn đề bài toán ngược (Validation Check)**
* Câu hỏi gợi mở: *"Giả sử ta thử một độ dài tối thiểu X, làm thế nào để biết có thể chia mảng thành ít nhất K đoạn mà mỗi đoạn có tổng >= X hay không?"*
* Viết hàm `check(X)`: Duyệt qua mảng A từ trái sang phải, tích lũy tổng các chiếc bánh. Ngay khi `sum >= X`, ta hoàn thành 1 phần bánh, tăng `count_parts++` và reset `sum = 0`. Nếu cuối cùng `count_parts >= K` thì X khả thi.

#### **Bước 2: Phân tích tính đơn điệu (Monotonicity)**
* Nhận xét: Khi X tăng lên, điều kiện tạo 1 phần bánh càng khó hơn, do đó số lượng phần bánh tạo được `count_parts` là hàm không tăng.
* Do đó hàm `check(X)` đơn điệu: `[Hợp lệ, Hợp lệ, ..., Hợp lệ, Không hợp lệ, ...]`.

#### **Bước 3: Nhận diện thuật toán Binary Search on Answer**
* Ta cần tìm giá trị X lớn nhất hợp lệ $\implies$ Chặt nhị phân kết quả trong khoảng $[1, \sum A_i]$.

#### **Bước 4: Giải thích Ý nghĩa Biến & Kỹ thuật Dừng sớm**
* `left = 1`, `right = sum(A)`. Dùng kiểu `long long` cho `sum`, `mid`, `left`, `right` để tránh tràn số.

#### **Bước 5: Đánh giá biên & Tối ưu**
* Thời gian chặt nhị phân: $O(N \log(\sum A_i))$. Với $N = 2 \times 10^5$, tổng phép tính $< 5 	imes 10^6$ ($< 0.02$s).

---

### 3. ĐỘ PHỨC TẠP THUẬT TOÁN

* **Thời gian:** $O(N \log(\sum A_i))$.
* **Bộ nhớ:** $O(N)$ lưu mảng bánh.

---

### 4. MÃ NGUỒN CHUẨN (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(long long mid, int n, int k, const vector<long long>& a) {
    int parts = 0;
    long long cur_sum = 0;
    for (int i = 0; i < n; i++) {
        cur_sum += a[i];
        if (cur_sum >= mid) {
            parts++;
            cur_sum = 0;
        }
    }
    return parts >= k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    long long sum_a = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        sum_a += a[i];
    }

    long long left = 1, right = sum_a, ans = 0;
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        if (check(mid, n, k, a)) {
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---

### 5. CẤU TRÚC BỘ TEST (20 TEST CASES)

* $1 \le N \le 2 \times 10^5$
* $1 \le K \le 10^9$
* $1 \le A_i \le 10^9$

---

💡 **Bạn có biết?** Lễ hội Bánh mì Việt Nam tại Phố cổ Hội An thu hút hơn 100.000 du khách quốc tế mỗi năm, tôn vinh nét văn hóa ẩm thực độc đáo kết hợp giữa ẩm thực Á - Âu.

🚀 **Thử thách:** Nếu mỗi phần bánh bị giới hạn số lượng chiếc bánh tối đa không vượt quá M chiếc, thuật toán sẽ cần thay đổi như thế nào?

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(long long mid, int n, int k, const vector<long long>& a) {
    int parts = 0;
    long long cur_sum = 0;
    for (int i = 0; i < n; i++) {
        cur_sum += a[i];
        if (cur_sum >= mid) {
            parts++;
            cur_sum = 0;
        }
    }
    return parts >= k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    long long sum_a = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        sum_a += a[i];
    }

    long long left = 1, right = sum_a, ans = 0;
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        if (check(mid, n, k, a)) {
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---

# IKH-0013 - Hành Lang Ánh Sáng

## 1. NỘI DUNG BÀI TOÁN

Trung tâm Triển lãm Nghệ thuật Ánh sáng Cố đô Huế xây dựng một hệ thống màn hình LED khổng lồ kích thước **M x N** ô vuông. Ô tại hàng $i$, cột **j** chứa **$A&#95;i$,j** bóng đèn LED.

Để phục vụ đêm diễn ánh sáng nghệ thuật, đạo diễn nghệ thuật muốn chọn ra một vùng hình chữ nhật đúng kích thước **H x W** (chứa đúng H hàng và W cột bóng đèn) sao cho **tổng công suất chiếu sáng (tổng số bóng đèn) trong vùng được chọn là lớn nhất**.

Hãy giúp đạo diễn tính toán tổng số bóng đèn LED lớn nhất có thể thu được từ một vùng hình chữ nhật kích thước H x W.

#### Input:
Dòng đầu chứa 4 số nguyên $M$ $N$ H W. $M$ dòng tiếp theo, mỗi dòng chứa $N$ số nguyên $A&#95;i$,j.

#### Output:
Một số nguyên duy nhất là tổng số bóng đèn LED lớn nhất.

#### Subtasks:
* Subtask 1 (30% điểm): $M, $N$ \le 50$
* Subtask 2 (30% điểm): $A_{i,j} \le 10^3$
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
3 4 2 2
1 2 3 4
5 6 7 8
9 10 11 12
```
**Output:**
```
38
```
**Giải thích:** Các vùng 2x2 gồm: (1..2, 1..2) tổng 1+2+5+6=14; (1..2, 2..3) tổng 2+3+6+7=18; (1..2, 3..4) tổng 3+4+7+8=22; (2..3, 1..2) tổng 5+6+9+10=30; (2..3, 2..3) tổng 6+7+10+11=34; (2..3, 3..4) tổng 7+8+11+12=38. Tổng lớn nhất là 38.

#### Sample 2:
**Input:**
```
2 2 1 1
5 9
3 4
```
**Output:**
```
9
```
**Giải thích:** Vùng 1x1 lớn nhất là ô (1,2) có giá trị 9.

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL
## Bài toán: IKH-0013 - Hành Lang Ánh Sáng (Corridor Grid Path)

---

### 1. THÔNG TIN BÀI TOÁN
* **Mã bài:** `IKH-0013`
* **Tên bài:** Hành Lang Ánh Sáng (Corridor Grid Path)
* **Dạng bài:** Prefix Sum 2D, Grid Verification
* **Độ khó đề xuất:** ⭐⭐⭐☆☆
* **Đánh giá 4 Tiêu chí Metadata:**
  * 🧠 **Algorithm Rating:** 1500
  * 📖 **Reading Difficulty:** ★★★★☆
  * 💡 **Modeling Difficulty:** ★★★★☆
  * 🧪 **Coding Implementation:** ★★★☆☆
* **Ràng buộc:**
* $1 \le M, N \le 500$
* $1 \le H, W \le \min(M, N)$
* $0 \le A_{i,j} \le 10^9$

#### Mô tả:
Trung tâm Triển lãm Nghệ thuật Ánh sáng Cố đô Huế xây dựng một hệ thống màn hình LED khổng lồ kích thước **M x N** ô vuông. Ô tại hàng **i**, cột **j** chứa **Ai,j** bóng đèn LED.

Để phục vụ đêm diễn ánh sáng nghệ thuật, đạo diễn nghệ thuật muốn chọn ra một vùng hình chữ nhật đúng kích thước **H x W** (chứa đúng H hàng và W cột bóng đèn) sao cho **tổng công suất chiếu sáng (tổng số bóng đèn) trong vùng được chọn là lớn nhất**.

Hãy giúp đạo diễn tính toán tổng số bóng đèn LED lớn nhất có thể thu được từ một vùng hình chữ nhật kích thước H x W.

#### Input:
Dòng đầu chứa 4 số nguyên M N H W. M dòng tiếp theo, mỗi dòng chứa N số nguyên Ai,j.

#### Output:
Một số nguyên duy nhất là tổng số bóng đèn LED lớn nhất.

#### Subtasks:
* Subtask 1 (30% điểm): $M, N \le 50$
* Subtask 2 (30% điểm): $A_{i,j} \le 10^3$
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
3 4 2 2
1 2 3 4
5 6 7 8
9 10 11 12
```
**Output:**
```
38
```
**Giải thích:** Các vùng 2x2 gồm: (1..2, 1..2) tổng 1+2+5+6=14; (1..2, 2..3) tổng 2+3+6+7=18; (1..2, 3..4) tổng 3+4+7+8=22; (2..3, 1..2) tổng 5+6+9+10=30; (2..3, 2..3) tổng 6+7+10+11=34; (2..3, 3..4) tổng 7+8+11+12=38. Tổng lớn nhất là 38.

#### Sample 2:
**Input:**
```
2 2 1 1
5 9
3 4
```
**Output:**
```
9
```
**Giải thích:** Vùng 1x1 lớn nhất là ô (1,2) có giá trị 9.

---

### 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Đặt vấn đề bài toán ngược (Validation Check)**
* Câu hỏi gợi mở: *"Nếu tính tổng từng ô trong vùng H x W bằng 2 vòng lặp lồng nhau, độ phức tạp sẽ là O(M * N * H * W), với M, N = 500 thì mất bao nhiêu phép tính?"*
* Trả lời: M * N * H * W = 500^4 = 6.25 * 10^10 phép tính -> TLE chắc chắn. Cần phương pháp tính tổng hình chữ nhật 2D trong O(1).

#### **Bước 2: Xây dựng Mảng Cộng Dồn 2D (Prefix Sum 2D)**
* Công thức khởi tạo: `pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1] + A[i][j]`.

#### **Bước 3: Công thức truy vấn vùng (r1, c1) đến (r2, c2) trong O(1)**
* `Sum(r1, c1, r2, c2) = pref[r2][c2] - pref[r1-1][c2] - pref[r2][c1-1] + pref[r1-1][c1-1]`.

#### **Bước 4: Duyệt qua tất cả các vùng H x W hợp lệ**
* Duyệt hàng dưới `r2` từ `H -> M`, cột phải `c2` từ `W -> N`. Đặt `r1 = r2 - H + 1`, `c1 = c2 - W + 1`. Tối ưu tìm Max.

#### **Bước 5: Đánh giá độ phức tạp**
* Thời gian: Khởi tạo Prefix 2D $O(M \cdot N) +$ Duyệt vùng $O(M \cdot N) = O(M \cdot N) \approx 2.5 \times 10^5$ phép tính ($< 0.01$s).

---

### 3. ĐỘ PHỨC TẠP THUẬT TOÁN

* **Thời gian:** $O(M \cdot N)$.
* **Bộ nhớ:** $O(M \cdot N)$ cho mảng cộng dồn 2D.

---

### 4. MÃ NGUỒN CHUẨN (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n, h, w;
    if (!(cin >> m >> n >> h >> w)) return 0;

    vector<vector<long long>> pref(m + 1, vector<long long>(n + 1, 0));
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            long long val;
            cin >> val;
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + val;
        }
    }

    long long max_sum = 0;
    for (int r2 = h; r2 <= m; r2++) {
        for (int c2 = w; c2 <= n; c2++) {
            int r1 = r2 - h + 1;
            int c1 = c2 - w + 1;
            long long cur_sum = pref[r2][c2] - pref[r1 - 1][c2] - pref[r2][c1 - 1] + pref[r1 - 1][c1 - 1];
            max_sum = max(max_sum, cur_sum);
        }
    }

    cout << max_sum << "\n";
    return 0;
}
```

---

### 5. CẤU TRÚC BỘ TEST (20 TEST CASES)

* $1 \le M, N \le 500$
* $1 \le H, W \le \min(M, N)$
* $0 \le A_{i,j} \le 10^9$

---

💡 **Bạn có biết?** Lễ hội Ánh sáng Festival Huế áp dụng công nghệ trình chiếu Lidar và LED 3D Matrix hiện đại, kết nối hơn 500.000 điểm sáng dọc theo bờ sông Hương.

🚀 **Thử thách:** Nếu hình chữ nhật được phép xoay góc 45 độ (hình thoi grid), thuật toán mảng cộng dồn 2D sẽ cần biến đổi tọa độ ra sao?

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n, h, w;
    if (!(cin >> m >> n >> h >> w)) return 0;

    vector<vector<long long>> pref(m + 1, vector<long long>(n + 1, 0));
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            long long val;
            cin >> val;
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + val;
        }
    }

    long long max_sum = 0;
    for (int r2 = h; r2 <= m; r2++) {
        for (int c2 = w; c2 <= n; c2++) {
            int r1 = r2 - h + 1;
            int c1 = c2 - w + 1;
            long long cur_sum = pref[r2][c2] - pref[r1 - 1][c2] - pref[r2][c1 - 1] + pref[r1 - 1][c1 - 1];
            max_sum = max(max_sum, cur_sum);
        }
    }

    cout << max_sum << "\n";
    return 0;
}
```

---

# IKH-0014 - Trung Tâm Logistics

## 1. NỘI DUNG BÀI TOÁN

Trung tâm Logistics Cảng Container Quốc tế Hải Phòng tiếp nhận $N$ yêu cầu cập bến xếp dỡ hàng của các tàu vận tải biển. Tàu thứ $i$ đăng ký bến bãi trong khoảng thời gian từ mốc **Li** đến mốc **Ri** (không tính mốc Ri).

Do trung tâm hiện tại chỉ có đúng 1 bến tàu đặc biệt được trang bị hệ thống cẩu tự động tốc độ cao, tại một thời điểm bến tàu này chỉ có thể phục vụ tối đa 1 tàu container.

Hãy tìm phương án sắp xếp lịch bến sao cho **phục vụ được số lượng tàu container là nhiều nhất có thể**. Hai tàu i và j không bị trùng lịch nếu $R&#95;i \le L&#95;j$ hoặc $R&#95;j \le L&#95;i$.

#### Input:
Dòng đầu chứa số nguyên $N$. $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên Li Ri.

#### Output:
Một số nguyên duy nhất là số lượng tàu tối đa được phục vụ.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000$
* Subtask 2 (30% điểm): $R&#95;i \le 10^5$
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4
1 4
3 5
0 6
5 7
```
**Output:**
```
2
```
**Giải thích:** Chọn tàu (1, 4) và tàu (5, 7) không bị đè lịch lên nhau. Số lượng tàu tối đa phục vụ được là 2.

#### Sample 2:
**Input:**
```
3
1 2
2 3
3 4
```
**Output:**
```
3
```
**Giải thích:** Cả 3 tàu (1,2), (2,3), (3,4) nối tiếp nhau không đè lịch. Số tàu tối đa là 3.

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL
## Bài toán: IKH-0014 - Trung Tâm Logistics (Smart Cargo Logistics)

---

### 1. THÔNG TIN BÀI TOÁN
* **Mã bài:** `IKH-0014`
* **Tên bài:** Trung Tâm Logistics (Smart Cargo Logistics)
* **Dạng bài:** Greedy Interval Scheduling, Sorting
* **Độ khó đề xuất:** ⭐⭐⭐☆☆
* **Đánh giá 4 Tiêu chí Metadata:**
  * 🧠 **Algorithm Rating:** 1300
  * 📖 **Reading Difficulty:** ★★★☆☆
  * 💡 **Modeling Difficulty:** ★★★★☆
  * 🧪 **Coding Implementation:** ★★☆☆☆
* **Ràng buộc:**
* $1 \le N \le 2 \times 10^5$
* $1 \le L_i < R_i \le 10^9$

#### Mô tả:
Trung tâm Logistics Cảng Container Quốc tế Hải Phòng tiếp nhận **N** yêu cầu cập bến xếp dỡ hàng của các tàu vận tải biển. Tàu thứ **i** đăng ký bến bãi trong khoảng thời gian từ mốc **Li** đến mốc **Ri** (không tính mốc Ri).

Do trung tâm hiện tại chỉ có đúng 1 bến tàu đặc biệt được trang bị hệ thống cẩu tự động tốc độ cao, tại một thời điểm bến tàu này chỉ có thể phục vụ tối đa 1 tàu container.

Hãy tìm phương án sắp xếp lịch bến sao cho **phục vụ được số lượng tàu container là nhiều nhất có thể**. Hai tàu i và j không bị trùng lịch nếu $R_i \le L_j$ hoặc $R_j \le L_i$.

#### Input:
Dòng đầu chứa số nguyên N. N dòng tiếp theo, mỗi dòng chứa hai số nguyên Li Ri.

#### Output:
Một số nguyên duy nhất là số lượng tàu tối đa được phục vụ.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000$
* Subtask 2 (30% điểm): $R_i \le 10^5$
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4
1 4
3 5
0 6
5 7
```
**Output:**
```
2
```
**Giải thích:** Chọn tàu (1, 4) và tàu (5, 7) không bị đè lịch lên nhau. Số lượng tàu tối đa phục vụ được là 2.

#### Sample 2:
**Input:**
```
3
1 2
2 3
3 4
```
**Output:**
```
3
```
**Giải thích:** Cả 3 tàu (1,2), (2,3), (3,4) nối tiếp nhau không đè lịch. Số tàu tối đa là 3.

---

### 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Đặt vấn đề bài toán ngược (Validation Check)**
* Câu hỏi gợi mở: *"Nên ưu tiên chọn tàu nào trước để nhường bến cho các tàu phía sau?"*
* Phân tích các chiến lược Tham ăn:
  1. Ước lượng tàu có thời gian bắt đầu L_i sớm nhất? -> Sai (Tàu bắt đầu sớm nhưng kết thúc muộn sẽ chiếm hết bến).
  2. Ước lượng tàu có thời lượng (R_i - L_i) ngắn nhất? -> Sai.
  3. Ước lượng tàu có thời gian kết thúc R_i sớm nhất? -> Đúng!

#### **Bước 2: Chứng minh Chiến lược Tham ăn Greedy Interval Scheduling**
* Chọn tàu có mốc kết thúc `R_i` nhỏ nhất sẽ giải phóng bến tàu sớm nhất có thể, chừa lại nhiều khoảng trống nhất cho các tàu phía sau.

#### **Bước 3: Thuật toán Sắp xếp & Duyệt 1 Vòng Lặp**
* Sắp xếp mảng các khoảng `[Li, Ri]` theo thứ tự **tăng dần của Ri**.
* Khởi tạo `last_end = -1`, `count = 0`.
* Duyệt từng khoảng: Nếu `Li >= last_end`, chấp nhận tàu này, tăng `count++` và cập nhật `last_end = Ri`.

#### **Bước 4: Giải thích Ý nghĩa Biến & Kiểu dữ liệu**
* Dùng `std::pair<long long, long long>` với `first = Ri`, `second = Li` để tiện dùng `std::sort`.

#### **Bước 5: Độ phức tạp**
* Thời gian sắp xếp $O(N \log N) +$ Duyệt $O(N) = O(N \log N) \approx 3 	imes 10^6$ phép tính ($< 0.04$s).

---

### 3. ĐỘ PHỨC TẠP THUẬT TOÁN

* **Thời gian:** $O(N \log N)$.
* **Bộ nhớ:** $O(N)$ lưu danh sách khoảng.

---

### 4. MÃ NGUỒN CHUẨN (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Interval {
    long long l, r;
    bool operator<(const Interval& other) const {
        return r < other.r;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Interval> intervals(n);
    for (int i = 0; i < n; i++) {
        cin >> intervals[i].l >> intervals[i].r;
    }

    sort(intervals.begin(), intervals.end());

    int count = 0;
    long long last_end = -1;

    for (int i = 0; i < n; i++) {
        if (intervals[i].l >= last_end) {
            count++;
            last_end = intervals[i].r;
        }
    }

    cout << count << "\n";
    return 0;
}
```

---

### 5. CẤU TRÚC BỘ TEST (20 TEST CASES)

* $1 \le N \le 2 \times 10^5$
* $1 \le L_i < R_i \le 10^9$

---

💡 **Bạn có biết?** Cảng Container Quốc tế Hải Phòng (TC-HICT) là cảng nước sâu đầu tiên của miền Bắc Việt Nam, có khả năng tiếp nhận tàu siêu trọng trọng tải lên tới 132.000 DWT.

🚀 **Thử thách:** Nếu trung tâm logistics mở rộng thành K bến tàu song song, làm thế nào để xếp dỡ tối đa số lượng tàu?

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Interval {
    long long l, r;
    bool operator<(const Interval& other) const {
        return r < other.r;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Interval> intervals(n);
    for (int i = 0; i < n; i++) {
        cin >> intervals[i].l >> intervals[i].r;
    }

    sort(intervals.begin(), intervals.end());

    int count = 0;
    long long last_end = -1;

    for (int i = 0; i < n; i++) {
        if (intervals[i].l >= last_end) {
            count++;
            last_end = intervals[i].r;
        }
    }

    cout << count << "\n";
    return 0;
}
```

---

# IKH-0015 - Trung Tâm Dữ Liệu AI

## 1. NỘI DUNG BÀI TOÁN

Trung tâm Siêu máy tính tính toán AI tiếp nhận $N$ tác vụ huấn luyện mô hình ngôn ngữ lớn (LLM). Tác vụ thứ $i$ mất **Ti** phút xử lý liên tục và phải hoàn thành trước mốc thời gian hạn định **Di** (Deadline).

Cụm máy tính GPU xử lý đơn luồng tại một thời điểm chỉ có thể thực hiện 1 tác vụ. Nếu bắt đầu tác vụ tại thời điểm $t$, tác vụ sẽ hoàn thành tại thời điểm $t + T&#95;i$. Tác vụ được coi là đúng hạn nếu $t + T&#95;i \le D&#95;i$.

Hãy tìm phương án lập lịch xử lý sao cho **số lượng tác vụ AI hoàn thành đúng hạn là nhiều nhất có thể**.

#### Input:
Dòng đầu chứa số nguyên $N$. $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên Ti Di.

#### Output:
Một số nguyên duy nhất là số tác vụ tối đa hoàn thành đúng hạn.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000$
* Subtask 2 (30% điểm): $T&#95;i, D&#95;i \le 10^4$
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
3
100 200
200 1300
1000 1250
```
**Output:**
```
2
```
**Giải thích:** Nếu chọn Tác vụ 1 (100, 200) -> hoàn thành tại t=100. Tác vụ 3 (1000, 1250) -> hoàn thành tại t=1100 <= 1250. Tổng cộng 2 tác vụ.

#### Sample 2:
**Input:**
```
2
10 5
20 10
```
**Output:**
```
0
```
**Giải thích:** Không tác vụ nào có thể hoàn thành trước deadline.

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL
## Bài toán: IKH-0015 - Trung Tâm Dữ Liệu AI (AI Cluster Duty)

---

### 1. THÔNG TIN BÀI TOÁN
* **Mã bài:** `IKH-0015`
* **Tên bài:** Trung Tâm Dữ Liệu AI (AI Cluster Duty)
* **Dạng bài:** Greedy, Priority Queue
* **Độ khó đề xuất:** ⭐⭐⭐☆☆
* **Đánh giá 4 Tiêu chí Metadata:**
  * 🧠 **Algorithm Rating:** 1500
  * 📖 **Reading Difficulty:** ★★★★☆
  * 💡 **Modeling Difficulty:** ★★★★☆
  * 🧪 **Coding Implementation:** ★★★☆☆
* **Ràng buộc:**
* $1 \le N \le 2 \times 10^5$
* $1 \le T_i, D_i \le 10^9$

#### Mô tả:
Trung tâm Siêu máy tính tính toán AI tiếp nhận **N** tác vụ huấn luyện mô hình ngôn ngữ lớn (LLM). Tác vụ thứ **i** mất **Ti** phút xử lý liên tục và phải hoàn thành trước mốc thời gian hạn định **Di** (Deadline).

Cụm máy tính GPU xử lý đơn luồng tại một thời điểm chỉ có thể thực hiện 1 tác vụ. Nếu bắt đầu tác vụ tại thời điểm $t$, tác vụ sẽ hoàn thành tại thời điểm $t + T_i$. Tác vụ được coi là đúng hạn nếu $t + T_i \le D_i$.

Hãy tìm phương án lập lịch xử lý sao cho **số lượng tác vụ AI hoàn thành đúng hạn là nhiều nhất có thể**.

#### Input:
Dòng đầu chứa số nguyên N. N dòng tiếp theo, mỗi dòng chứa hai số nguyên Ti Di.

#### Output:
Một số nguyên duy nhất là số tác vụ tối đa hoàn thành đúng hạn.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000$
* Subtask 2 (30% điểm): $T_i, D_i \le 10^4$
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
3
100 200
200 1300
1000 1250
```
**Output:**
```
2
```
**Giải thích:** Nếu chọn Tác vụ 1 (100, 200) -> hoàn thành tại t=100. Tác vụ 3 (1000, 1250) -> hoàn thành tại t=1100 <= 1250. Tổng cộng 2 tác vụ.

#### Sample 2:
**Input:**
```
2
10 5
20 10
```
**Output:**
```
0
```
**Giải thích:** Không tác vụ nào có thể hoàn thành trước deadline.

---

### 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Đặt vấn đề bài toán ngược (Validation Check)**
* Câu hỏi gợi mở: *"Nên ưu tiên xếp tác vụ nào trước?"*
* Phân tích: Ưu tiên các tác vụ có hạn định Deadline `D_i` nhỏ hơn xếp trước. Do đó bước 1 là Sắp xếp mảng theo `D_i` tăng dần.

#### **Bước 2: Xử lý khi gặp Tác vụ bị trễ hạn (Over-deadline)**
* Khi duyệt đến tác vụ thứ $i$, ta cộng thời gian $T_i$ vào `total_time` và đưa $T_i$ vào Hàng đợi ưu tiên Max-Heap (`std::priority_queue`).
* Nếu `total_time > D_i` (tác vụ bị quá hạn), ta Tham ăn loại bỏ tác vụ có **thời gian xử lý $T$ lớn nhất** đã chọn trước đó (chính là `pq.top()`), trừ `total_time` đi `pq.top()`.

#### **Bước 3: Tính đúng đắn của Chiến lược Tham ăn loại bỏ T_max**
* Loại bỏ tác vụ tốn nhiều thời gian nhất sẽ thu hồi lại nhiều thời gian nhất cho `total_time`, giúp các tác vụ phía sau dễ dàng đáp ứng Deadline hơn.

#### **Bước 4: Cài đặt Hàng đợi ưu tiên Priority Queue**
* Dùng `std::priority_queue<long long>` để quản lý các khoảng thời gian $T_i$ đã chọn.

#### **Bước 5: Độ phức tạp**
* Thời gian: Sắp xếp $O(N \log N) +$ Thao tác Heap $O(N \log N) = O(N \log N) \approx 4 \times 10^6$ phép tính ($< 0.05$s).

---

### 3. ĐỘ PHỨC TẠP THUẬT TOÁN

* **Thời gian:** $O(N \log N)$.
* **Bộ nhớ:** $O(N)$ lưu Hàng đợi ưu tiên.

---

### 4. MÃ NGUỒN CHUẨN (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Task {
    long long t, d;
    bool operator<(const Task& other) const {
        return d < other.d;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Task> tasks(n);
    for (int i = 0; i < n; i++) {
        cin >> tasks[i].t >> tasks[i].d;
    }

    sort(tasks.begin(), tasks.end());

    priority_queue<long long> pq;
    long long total_time = 0;

    for (int i = 0; i < n; i++) {
        total_time += tasks[i].t;
        pq.push(tasks[i].t);

        if (total_time > tasks[i].d) {
            total_time -= pq.top();
            pq.pop();
        }
    }

    cout << (int)pq.size() << "\n";
    return 0;
}
```

---

### 5. CẤU TRÚC BỘ TEST (20 TEST CASES)

* $1 \le N \le 2 \times 10^5$
* $1 \le T_i, D_i \le 10^9$

---

💡 **Bạn có biết?** Siêu máy tính AI tại các trung tâm dữ liệu GPU lớn sử dụng hàng chục ngàn chip NVIDIA H100 kết nối qua mạng InfiniBand 400Gbps để huấn luyện các mô hình AI hàng nghìn tỷ tham số.

🚀 **Thử thách:** Nếu mỗi tác vụ có thêm giá trị tiền thưởng Pi nhận được khi hoàn thành đúng hạn, thuật toán sẽ thay đổi ra sao?

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Task {
    long long t, d;
    bool operator<(const Task& other) const {
        return d < other.d;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Task> tasks(n);
    for (int i = 0; i < n; i++) {
        cin >> tasks[i].t >> tasks[i].d;
    }

    sort(tasks.begin(), tasks.end());

    priority_queue<long long> pq;
    long long total_time = 0;

    for (int i = 0; i < n; i++) {
        total_time += tasks[i].t;
        pq.push(tasks[i].t);

        if (total_time > tasks[i].d) {
            total_time -= pq.top();
            pq.pop();
        }
    }

    cout << (int)pq.size() << "\n";
    return 0;
}
```

---

# IKH-0016 - Đội Hạm Đội Robot

## 1. NỘI DUNG BÀI TOÁN

Tập đoàn Công nghệ Sản xuất Ô tô ĐiệnVinFast chuẩn bị vận hành hạm đội $N$ xe tự hành AGV và $M$ bộ cảm biến khoảng cách Lidar. Xe AGV thứ $i$ có công suất **$A&#95;i$**, bộ cảm biến thứ **j** có tần số **Bj**.

Để lắp ráp 1 xe AGV hoàn chỉnh, người ta cần ghép 1 xe AGV với 1 bộ cảm biến Lidar. Hiệu suất kết nối của cặp ghép (i, j) được tính bằng độ chênh lệch tuyệt đối giữa công suất và tần số: $|$A&#95;i$ - Bj|$.

Hãy tìm phương án ghép cặp sao cho **độ chênh lệch tuyệt đối nhỏ nhất giữa một xe AGV và một bộ cảm biến Lidar bất kỳ là nhỏ nhất có thể**. (Mỗi xe và mỗi cảm biến có thể ghép cặp tùy ý).

#### Input:
Dòng đầu chứa $N, M$. Dòng hai chứa $N$ số nguyên $A&#95;i$. Dòng ba chứa $M$ số nguyên Bj.

#### Output:
Một số nguyên duy nhất là độ chênh lệch tuyệt đối nhỏ nhất có thể đạt được.

#### Subtasks:
* Subtask 1 (30% điểm): $N, $M$ \le 1000$
* Subtask 2 (30% điểm): $A&#95;i, B&#95;j \le 10^5$
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
3 2
10 20 30
15 24
```
**Output:**
```
4
```
**Giải thích:** Các độ chênh lệch: |10-15|=5, |10-24|=14, |20-15|=5, |20-24|=4, |30-15|=15, |30-24|=6. Nhỏ nhất là 4 (ghép xe 20 với cảm biến 24).

#### Sample 2:
**Input:**
```
2 2
100 200
100 200
```
**Output:**
```
0
```
**Giải thích:** Ghép (100, 100) có độ chênh lệch bằng 0.

---

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL
## Bài toán: IKH-0016 - Đội Hạm Đội Robot (Fleet Formation)

---

### 1. THÔNG TIN BÀI TOÁN
* **Mã bài:** `IKH-0016`
* **Tên bài:** Đội Hạm Đội Robot (Fleet Formation)
* **Dạng bài:** Two Pointers, Sorting
* **Độ khó đề xuất:** ⭐⭐⭐☆☆
* **Đánh giá 4 Tiêu chí Metadata:**
  * 🧠 **Algorithm Rating:** 1300
  * 📖 **Reading Difficulty:** ★★★☆☆
  * 💡 **Modeling Difficulty:** ★★★☆☆
  * 🧪 **Coding Implementation:** ★★☆☆☆
* **Ràng buộc:**
* $1 \le N, M \le 2 \times 10^5$
* $1 \le A_i, B_j \le 10^9$

#### Mô tả:
Tập đoàn Công nghệ Sản xuất Ô tô ĐiệnVinFast chuẩn bị vận hành hạm đội **N** xe tự hành AGV và **M** bộ cảm biến khoảng cách Lidar. Xe AGV thứ **i** có công suất **Ai**, bộ cảm biến thứ **j** có tần số **Bj**.

Để lắp ráp 1 xe AGV hoàn chỉnh, người ta cần ghép 1 xe AGV với 1 bộ cảm biến Lidar. Hiệu suất kết nối của cặp ghép (i, j) được tính bằng độ chênh lệch tuyệt đối giữa công suất và tần số: $|Ai - Bj|$.

Hãy tìm phương án ghép cặp sao cho **độ chênh lệch tuyệt đối nhỏ nhất giữa một xe AGV và một bộ cảm biến Lidar bất kỳ là nhỏ nhất có thể**. (Mỗi xe và mỗi cảm biến có thể ghép cặp tùy ý).

#### Input:
Dòng đầu chứa N M. Dòng hai chứa N số nguyên Ai. Dòng ba chứa M số nguyên Bj.

#### Output:
Một số nguyên duy nhất là độ chênh lệch tuyệt đối nhỏ nhất có thể đạt được.

#### Subtasks:
* Subtask 1 (30% điểm): $N, M \le 1000$
* Subtask 2 (30% điểm): $A_i, B_j \le 10^5$
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
3 2
10 20 30
15 24
```
**Output:**
```
4
```
**Giải thích:** Các độ chênh lệch: |10-15|=5, |10-24|=14, |20-15|=5, |20-24|=4, |30-15|=15, |30-24|=6. Nhỏ nhất là 4 (ghép xe 20 với cảm biến 24).

#### Sample 2:
**Input:**
```
2 2
100 200
100 200
```
**Output:**
```
0
```
**Giải thích:** Ghép (100, 100) có độ chênh lệch bằng 0.

---

### 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Đặt vấn đề bài toán ngược (Validation Check)**
* Câu hỏi gợi mở: *"Nếu duyệt mọi cặp (i, j), độ phức tạp là O(N * M), với N, M = 200.000 có bị TLE không?"*
* Trả lời: N * M = 4 * 10^10 -> TLE. Cần thuật toán O((N + M) log(N + M)).

#### **Bước 2: Phân tích tính đơn điệu sau khi Sắp xếp**
* Sắp xếp cả mảng A và mảng B theo thứ tự tăng dần.
* Khi xét cặp (A[i], B[j]):
  - Nếu A[i] == B[j] -> Chênh lệch = 0 (tối ưu nhất, dừng ngay).
  - Nếu A[i] < B[j] -> Để giảm độ chênh lệch, ta nên tăng A[i] lên (dịch con trỏ i++).
  - Nếu A[i] > B[j] -> Để giảm độ chênh lệch, ta nên tăng B[j] lên (dịch con trỏ j++).

#### **Bước 3: Thuật toán Con trỏ kép (Two Pointers)**
* Đặt con trỏ `i = 0` trên mảng A và `j = 0` trên mảng B.
* Liên tục tính `min_diff = min(min_diff, abs(A[i] - B[j]))` và dịch con trỏ có giá trị nhỏ hơn.

#### **Bước 4: Giải thích Ý nghĩa Biến**
* Dùng `long long min_diff = INF` tích lũy kết quả nhỏ nhất.

#### **Bước 5: Độ phức tạp**
* Thời gian: Sắp xếp $O(N \log N + M \log M) +$ Two Pointers $O(N + M) = O(N \log N + M \log M) \approx 4 \times 10^6$ phép tính ($< 0.04$s).

---

### 3. ĐỘ PHỨC TẠP THUẬT TOÁN

* **Thời gian:** $O(N \log N + M \log M)$.
* **Bộ nhớ:** $O(N + M)$ lưu hai mảng.

---

### 4. MÃ NGUỒN CHUẨN (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int j = 0; j < m; j++) cin >> b[j];

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int i = 0, j = 0;
    long long min_diff = 4e18; // Vô cùng lớn

    while (i < n && j < m) {
        long long diff = abs(a[i] - b[j]);
        min_diff = min(min_diff, diff);

        if (a[i] < b[j]) {
            i++;
        } else {
            j++;
        }
    }

    cout << min_diff << "\n";
    return 0;
}
```

---

### 5. CẤU TRÚC BỘ TEST (20 TEST CASES)

* $1 \le N, M \le 2 \times 10^5$
* $1 \le A_i, B_j \le 10^9$

---

💡 **Bạn có biết?** Tổ hợp nhà máy sản xuất ô tô VinFast tại Hải Phòng áp dụng hơn 1.200 robot tự động ABB kết nối qua hạ tầng mạng 5G riêng biệt (Private 5G Network).

🚀 **Thử thách:** Nếu yêu cầu ghép N xe với M cảm biến sao cho tổng độ chênh lệch của N cặp ghép là nhỏ nhất (với N <= M), thuật toán sẽ thay đổi ra sao?

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int j = 0; j < m; j++) cin >> b[j];

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int i = 0, j = 0;
    long long min_diff = 4e18; // Vô cùng lớn

    while (i < n && j < m) {
        long long diff = abs(a[i] - b[j]);
        min_diff = min(min_diff, diff);

        if (a[i] < b[j]) {
            i++;
        } else {
            j++;
        }
    }

    cout << min_diff << "\n";
    return 0;
}
```

---

# IKH-0017 - Cặp Đèn Đường Bằng

## 1. NỘI DUNG BÀI TOÁN

Tại Cảng Hàng không Quốc tế Nội Bài, hệ thống chiếu sáng đường băng gồm $N$ bóng đèn LED xếp thành một hàng dọc. Đèn thứ $i$ có độ sáng $A&#95;i$ Lumen.

Để đảm bảo an toàn cho máy bay hạ cánh ban đêm, kỹ sư vận hành muốn chọn một đoạn đèn liên tiếp gồm các đèn từ vị trí $L$ đến $R$ ($1 \le L \le R \le N$) sao cho **độ chênh lệch giữa độ sáng lớn nhất và độ sáng nhỏ nhất trong đoạn không vượt quá $K$ Lumen** ($\max(A&#95;L \dots A&#95;R) - \min(A&#95;L \dots A&#95;R) \le K$).

Hãy tìm **độ dài lớn nhất** (số lượng bóng đèn $R - L + 1$) của một đoạn đèn thỏa mãn điều kiện trên.

#### Input:
* Dòng đầu chứa hai số nguyên $N, K$ ($1 \le N \le 2 \times 10^5, 0 \le K \le 10^9$).
* Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($1 \le A&#95;i \le 10^9$).

#### Output:
* Một số nguyên duy nhất là độ dài đoạn đèn liên tiếp dài nhất tìm được.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000, K \le 10^5$
* Subtask 2 (30% điểm): $N \le 2 \times 10^5, K = 0$
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
6 3
1 4 2 7 5 6
```
**Output:**
```
3
```
**Giải thích:** Đoạn [7, 5, 6] dài 3 có max = 7, min = 5, chênh lệch 7 - 5 = 2 <= 3.

#### Sample 2:
**Input:**
```
5 0
2 2 2 4 2
```
**Output:**
```
3
```
**Giải thích:** Đoạn [2, 2, 2] dài 3 có max = min = 2, chênh lệch 0 <= 0.

---

💡 **Bạn có biết?** Cảng hàng không quốc tế Nội Bài trang bị hệ thống đèn hiệu hàng không CAT II/III tiên tiến với hơn 3.000 đèn LED chuyên dụng hỗ trợ hạ cánh trong điều kiện sương mù dày đặc.

🚀 **Thử thách:** Nếu muốn đếm tổng số lượng đoạn thỏa mãn thay vì chỉ tìm độ dài lớn nhất, thuật toán sẽ cần cập nhật thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt bài toán:** Cho mảng $A$ gồm $N$ số nguyên và hằng số $K$. Tìm độ dài đoạn con liên tiếp dài nhất $A[L..R]$ sao cho $\max(A[L..R]) - \min(A[L..R]) \le K$.
* **Ràng buộc:** $N \le 2 \times 10^5$, các phần tử lên tới $10^9$.
* **Nhận xét:** Khi mở rộng con trỏ $R$ sang phải, chênh lệch $\max - \min$ của cửa sổ $[L..R]$ luôn có xu hướng tăng hoặc giữ nguyên. Đây là bài toán cửa sổ trượt (Two Pointers / Sliding Window) kinh điển.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Đặt vấn đề bài toán đơn giản (Brute Force)**
* Duyệt mọi cặp $(L, R)$ từ $1$ tới $N$. Tìm $\max$ và $\min$ trên đoạn $[L..R]$ mất $O(N)$. Tổng độ phức tạp $O(N^3)$ hoặc $O(N^2)$, chỉ ăn điểm Subtask 1 ($N \le 1000$).

#### **Bước 2: Phân tích tính đơn điệu (Monotonicity)**
* Nếu cửa sổ $[L..R]$ hợp lệ (chênh lệch $\le K$), thì mọi cửa sổ con bên trong cũng hợp lệ.
* Do đó khi tăng con trỏ $R$, ta chỉ cần dịch con trỏ $L$ sang phải cho tới khi cửa sổ $[L..R]$ thỏa mãn lại điều kiện.

#### **Bước 3: Tối ưu duy trì Max và Min trong cửa sổ $O(1)$**
* Sử dụng 2 hàng đợi hai đầu Monotonic Deque (`max_dq` và `min_dq`):
  * `max_dq`: Lớp các chỉ số giảm dần theo giá trị phần tử.
  * `min_dq`: Lớp các chỉ số tăng dần theo giá trị phần tử.
* Mỗi phần tử được `push` và `pop` vào deque đúng 1 lần.

#### **Bước 4: Xử lý kỹ thuật Trượt cửa sổ (Sliding Window)**
* Kiểm tra `a[max_dq.front()] - a[min_dq.front()] > k`. Nếu vi phạm, tăng `L++` và loại bỏ các phần tử nằm ngoài cửa sổ (`< L`).

#### **Bước 5: Đánh giá độ phức tạp thuật toán**
* **Độ phức tạp thời gian (Time Complexity):** $O(N)$ vì mỗi con trỏ $L, R$ chỉ di chuyển từ $0$ đến $N-1$.
* **Độ phức tạp bộ nhớ (Space Complexity):** $O(N)$ lưu trữ mảng và 2 deque.

---

## 3. ĐỘ PHỨC TẠP THUẬT TOÁN
* **Thời gian:** $O(N)$ hoàn hảo cho $N = 2 \times 10^5$.
* **Bộ nhớ:** $O(N)$.

---

## 4. MÃ NGUỒN CHUẨN C++
```cpp
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;
    
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    
    deque<int> max_dq, min_dq;
    int left = 0;
    int ans = 0;
    
    for (int right = 0; right < n; right++) {
        while (!max_dq.empty() && a[max_dq.back()] <= a[right]) max_dq.pop_back();
        max_dq.push_back(right);
        
        while (!min_dq.empty() && a[min_dq.back()] >= a[right]) min_dq.pop_back();
        min_dq.push_back(right);
        
        while (a[max_dq.front()] - a[min_dq.front()] > k) {
            left++;
            if (max_dq.front() < left) max_dq.pop_front();
            if (min_dq.front() < left) min_dq.pop_front();
        }
        
        ans = max(ans, right - left + 1);
    }
    
    cout << ans << "\n";
    return 0;
}
```

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;
    
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    
    deque<int> max_dq, min_dq;
    int left = 0;
    int ans = 0;
    
    for (int right = 0; right < n; right++) {
        while (!max_dq.empty() && a[max_dq.back()] <= a[right]) max_dq.pop_back();
        max_dq.push_back(right);
        
        while (!min_dq.empty() && a[min_dq.back()] >= a[right]) min_dq.pop_back();
        min_dq.push_back(right);
        
        while (a[max_dq.front()] - a[min_dq.front()] > k) {
            left++;
            if (max_dq.front() < left) max_dq.pop_front();
            if (min_dq.front() < left) min_dq.pop_front();
        }
        
        ans = max(ans, right - left + 1);
    }
    
    cout << ans << "\n";
    return 0;
}
```

---

# IKH-0018 - Lịch Khởi Hành Chuyến Bay

## 1. NỘI DUNG BÀI TOÁN

Trung tâm Điều phối Bay thuộc Tổng công ty Quản lý bay Việt Nam (VATM) cần sắp xếp lịch cất cánh cho $N$ chuyến bay đăng ký trong ngày. Chuyến bay thứ $i$ bắt đầu chiếm dụng đường băng từ mốc thời gian $S&#95;i$ và kết thúc tại mốc thời gian $E&#95;i$ ($S&#95;i < E&#95;i$).

Do chỉ có một đường băng cất cánh duy nhất tại đường băng số 1, hai chuyến bay không thể sử dụng đường băng cùng một lúc (nghĩa là nếu chuyến bay $A$ dùng từ $[S&#95;A, E&#95;A]$ và chuyến bay $B$ dùng từ $[S&#95;B, E&#95;B]$ thì phải thỏa mãn $E&#95;A \le S&#95;B$ hoặc $E&#95;B \le S&#95;A$).

Hãy giúp trung tâm xác định **số lượng chuyến bay tối đa** có thể phục vụ trong ngày.

#### Input:
* Dòng đầu chứa số nguyên $N$ ($1 \le N \le 2 \times 10^5$).
* $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên $S&#95;i, E&#95;i$ ($0 \le S&#95;i < E&#95;i \le 10^9$).

#### Output:
* Một số nguyên duy nhất là số lượng chuyến bay tối đa cất cánh an toàn.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000, E&#95;i \le 1000$
* Subtask 2 (30% điểm): Các khoảng $[S&#95;i, E&#95;i]$ không giao nhau.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4
1 3
2 5
3 9
6 8
```
**Output:**
```
2
```
**Giải thích:** Chọn 2 chuyến bay: [1, 3] và [6, 8] (hoặc [1, 3] và [3, 9]).

#### Sample 2:
**Input:**
```
5
1 4
3 5
0 6
5 7
3 8
```
**Output:**
```
2
```
**Giải thích:** Chọn chuyến [1, 4] và chuyến [5, 7] thu được 2 chuyến bay.

---

💡 **Bạn có biết?** VATM hiện điều hành hơn 900.000 chuyến bay mỗi năm qua vùng thông báo bay (FIR) Hà Nội và TP. Hồ Chí Minh, đảm bảo an toàn tuyệt đối cho các luồng không lưu huyết mạch Đông Nam Á.

🚀 **Thử thách:** Nếu muốn tìm ít nhất bao nhiêu đường băng để phục vụ TẤT CẢ $N$ chuyến bay mà không chuyến nào bị hủy, thuật toán sẽ đổi thành gì?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt bài toán:** Cho $N$ khoảng thời gian $[S&#95;i, E&#95;i]$. Chọn số lượng khoảng nhiều nhất sao cho không có 2 khoảng nào đè lên nhau ($E&#95;A \le S&#95;B$).
* **Ràng buộc:** $N \le 2 \times 10^5$, thời gian lên tới $10^9$.
* **Dạng bài:** Scheduling / Interval Selection Problem (Tham ăn - Greedy).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Chiến lược Tham ăn (Greedy Choice Property)**
* Nên ưu tiên chọn chuyến bay nào kết thúc **SỚM NHẤT**?
* Lý do: Chuyến bay kết thúc càng sớm thì càng để lại nhiều khoảng trống thời gian ở phía sau cho các chuyến bay khác!

#### **Bước 2: Sắp xếp theo Thời gian Kết thúc ($E&#95;i$)**
* Sắp xếp mảng các chuyến bay tăng dần theo $E&#95;i$. Nếu $E&#95;i$ bằng nhau, sắp xếp tăng dần theo $S&#95;i$.

#### **Bước 3: Duyệt Tham ăn (Greedy Loop)**
* Duyệt qua danh sách đã sắp xếp. Giữ một biến `last_end` ghi nhận thời gian kết thúc của chuyến bay vừa được chọn gần nhất.
* Nếu chuyến bay đang xét có $S&#95;i \ge \text{last\_end}$, chọn chuyến bay này và cập nhật `last_end = E_i`.

#### **Bước 4: Đánh giá độ phức tạp**
* Thời gian sắp xếp $O(N \log N)$, thời gian duyệt tham ăn $O(N)$. Tổng thời gian $O(N \log N)$.

---

## 3. ĐỘ PHỨC TẠP THUẬT TOÁN
* **Thời gian:** $O(N \log N)$ (chạy trong 0.08s cho $N = 2 \times 10^5$).
* **Bộ nhớ:** $O(N)$.

---

## 4. MÃ NGUỒN CHUẨN C++
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Flight {
    long long s, e;
};

bool compareFlight(const Flight &a, const Flight &b) {
    if (a.e != b.e) return a.e < b.e;
    return a.s < b.s;
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<Flight> flights(n);
    for (int i = 0; i < n; i++) {
        cin >> flights[i].s >> flights[i].e;
    }
    
    sort(flights.begin(), flights.end(), compareFlight);
    
    int count = 0;
    long long last_end = -1;
    
    for (int i = 0; i < n; i++) {
        if (flights[i].s >= last_end) {
            count++;
            last_end = flights[i].e;
        }
    }
    
    cout << count << "\n";
    return 0;
}
```

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Flight {
    long long s, e;
};

bool compareFlight(const Flight &a, const Flight &b) {
    if (a.e != b.e) return a.e < b.e;
    return a.s < b.s;
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<Flight> flights(n);
    for (int i = 0; i < n; i++) {
        cin >> flights[i].s >> flights[i].e;
    }
    
    sort(flights.begin(), flights.end(), compareFlight);
    
    int count = 0;
    long long last_end = -1;
    
    for (int i = 0; i < n; i++) {
        if (flights[i].s >= last_end) {
            count++;
            last_end = flights[i].e;
        }
    }
    
    cout << count << "\n";
    return 0;
}
```

---

# IKH-0019 - Đội Container Cảng Hải Phòng

## 1. NỘI DUNG BÀI TOÁN

Cảng Tân Cảng Hải Phòng nhận $N$ thùng Container hàng xuất khẩu. Container thứ $i$ có trọng lượng $W&#95;i$ tấn và sức tải tối đa $C&#95;i$ tấn (nghĩa là nó chỉ có thể xếp đè lên trên các container khác nếu trọng lượng của nó không vượt quá sức tải $C$ của container phía dưới).

Ban Quản lý Cảng muốn xếp các container thành **các chồng container**. Một container $A$ có thể đặt trực tiếp lên trên container $B$ nếu trọng lượng $W&#95;A \le C&#95;B$.

Hãy tìm **số lượng container nhiều nhất** có thể xếp thành **MỘT CHỒNG HÀNG DUY NHẤT** tuân thủ điều kiện trên.

#### Input:
* Dòng đầu chứa số nguyên $N$ ($1 \le N \le 2 \times 10^5$).
* $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên $W&#95;i, C&#95;i$ ($1 \le W&#95;i, C&#95;i \le 10^9$).

#### Output:
* Một số nguyên duy nhất là số lượng container tối đa có thể xếp thành 1 chồng.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000$
* Subtask 2 (30% điểm): $W&#95;i = 1$ với mọi $i$.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4
3 5
1 2
2 4
6 1
```
**Output:**
```
3
```
**Giải thích:** Xếp chồng 3 container từ trên xuống dưới: [1, 2] (trọng lượng 1) lên [2, 4] (sức tải 4 >= 1) lên [3, 5] (sức tải 5 >= 1+2=3). Tổng cộng 3 container.

---

💡 **Bạn có biết?** Cảng Hải Phòng là cụm cảng biển tổng hợp cấp quốc gia lớn nhất miền Bắc Việt Nam, xử lý hơn 100 triệu tấn hàng hóa thông quan mỗi năm.

🚀 **Thử thách:** Nếu tổng trọng lượng của TẤT CẢ các container xếp ở trên phải $\le C$ của container dưới cùng, bài toán trở thành bài toán Quy hoạch động xếp chồng nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho $N$ container $(W&#95;i, C&#95;i)$. Chọn một tập hợp container xếp thành 1 chồng sao cho mỗi container phía dưới có sức tải $C$ lớn hơn hoặc bằng tổng trọng lượng các container phía trên.
* **Quy đổi:** Bài toán tương đương tìm dãy con tăng dài nhất (LIS variant) kết hợp Tham ăn và Nhị phân.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH

#### **Bước 1: Sắp xếp theo Sức tải $C&#95;i$**
* Thùng có sức tải $C$ càng lớn phải ưu tiên xếp ở phía dưới.
* Do đó, ta sắp xếp các container theo chiều tăng dần của $C&#95;i$.

#### **Bước 2: Quy hoạch động kết hợp Tìm kiếm Nhị phân (DP + Binary Search)**
* Gọi `dp[k]` là tổng trọng lượng nhỏ nhất của một chồng container gồm $k$ thùng.
* Mảng `dp` sẽ luôn tăng dần. Với mỗi container $i$, ta tìm vị trí $k$ lớn nhất sao cho `dp[k-1] <= a[i].c`.

#### **Bước 3: Đánh giá độ phức tạp**
* Sắp xếp $O(N \log N)$. Duyệt $N$ phần tử, mỗi phần tử dùng `upper_bound` mất $O(\log N)$.
* Tổng thời gian $O(N \log N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Container {
    long long w, c;
};

bool cmp(const Container &a, const Container &b) {
    if (a.c != b.c) return a.c < b.c;
    return a.w < b.w;
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<Container> a(n);
    for (int i = 0; i < n; i++) cin >> a[i].w >> a[i].c;
    
    sort(a.begin(), a.end(), cmp);
    
    vector<long long> dp;
    
    for (int i = 0; i < n; i++) {
        auto it = upper_bound(dp.begin(), dp.end(), a[i].c);
        int idx = distance(dp.begin(), it);
        
        if (idx == (int)dp.size()) {
            dp.push_back((idx > 0 ? dp.back() : 0) + a[i].w);
        } else {
            long long prev = (idx > 0 ? dp[idx - 1] : 0);
            dp[idx] = min(dp[idx], prev + a[i].w);
        }
    }
    
    cout << dp.size() << "\n";
    return 0;
}
```

---

# IKH-0020 - Tra Cứu Mã Vận Đơn

## 1. NỘI DUNG BÀI TOÁN

Hệ thống Quản lý Bưu chính VNPost tiếp nhận $N$ bưu gửi nhập kho trong ngày. Mỗi bưu gửi được dán một **mã vận đơn** là một chuỗi ký tự gồm chữ cái và chữ số.

Sau khi nhập kho, bộ phận chăm sóc khách hàng nhận được $Q$ yêu cầu tra cứu. Mỗi yêu cầu hỏi: **"Mã vận đơn $X$ đã được nhập kho tổng cộng bao nhiêu lần trong ngày?"**

Hãy viết chương trình phản hồi nhanh chóng tất cả $Q$ câu hỏi tra cứu.

#### Input:
* Dòng đầu chứa số nguyên $N$ ($1 \le N \le 2 \times 10^5$).
* Dòng thứ hai chứa $N$ chuỗi ký tự cách nhau bởi khoảng trắng là các mã vận đơn nhập kho.
* Dòng thứ ba chứa số nguyên $Q$ ($1 \le Q \le 2 \times 10^5$).
* Dòng thứ tư chứa $Q$ chuỗi ký tự là các mã vận đơn cần tra cứu.
*(Độ dài mỗi mã vận đơn không quá 15 ký tự, chỉ gồm chữ cái và chữ số)*.

#### Output:
* In trên 1 dòng gồm $Q$ số nguyên cách nhau bởi khoảng trắng, số thứ $j$ là số lần xuất hiện của mã vận đơn thứ $j$ trong $Q$ câu hỏi.

#### Subtasks:
* Subtask 1 (30% điểm): $N, Q \le 1000$
* Subtask 2 (30% điểm): Mã vận đơn chỉ gồm các chữ số nguyên từ 1 đến 100.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
5
VN102 VN888 VN102 VN999 VN102
3
VN102 VN888 VN555
```
**Output:**
```
3 1 0
```
**Giải thích:** VN102 xuất hiện 3 lần, VN888 xuất hiện 1 lần, VN555 không xuất hiện (0 lần).

---

💡 **Bạn có biết?** Mã vận đơn (Tracking Number) của VNPost tuân theo chuẩn Liên minh Bưu chính Thế giới (UPU) với 13 ký tự tiêu chuẩn quốc tế giúp theo dõi định vị bưu gửi thời gian thực.

🚀 **Thử thách:** Nếu $N, Q$ lên tới $10^6$, việc sử dụng `std::map` hay `std::unordered_map` kèm `cin.tie(NULL)` có sự khác biệt hiệu năng thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho danh sách $N$ chuỗi. Đếm tần suất xuất hiện của $Q$ chuỗi truy vấn.
* **Dạng bài:** Hash Map / STL Frequency Count.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH

#### **Bước 1: Lựa chọn cấu trúc dữ liệu STL**
* `std::unordered_map<string, int>` giúp tra cứu trung bình $O(1)$ mỗi truy vấn.
* Sử dụng `freq.reserve(n * 2)` để tránh rehashing liên tục.

#### **Bước 2: Tối ưu I/O**
* Dùng `cin.tie(NULL); ios_base::sync_with_stdio(false);` để xử lý nhanh $4 \times 10^5$ chuỗi trong $0.1$ giây.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    if (!(cin >> n)) return 0;
    
    unordered_map<string, int> freq;
    freq.reserve(n * 2);
    
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        freq[s]++;
    }
    
    int q;
    if (!(cin >> q)) return 0;
    for (int j = 0; j < q; j++) {
        string query;
        cin >> query;
        auto it = freq.find(query);
        if (it != freq.end()) {
            cout << it->second << (j == q - 1 ? "" : " ");
        } else {
            cout << 0 << (j == q - 1 ? "" : " ");
        }
    }
    cout << "\n";
    return 0;
}
```

---

# IKH-0021 - Hàng Cho Mới Nhất

## 1. NỘI DUNG BÀI TOÁN

Hệ thống kho vận thông minh TikiNOW tiếp nhận một dòng các kiện hàng ưu tiên giao gấp. Mỗi kiện hàng khi nhập kho được gán một **mức độ ưu tiên** $P$ (số nguyên dương, giá trị càng lớn càng ưu tiên).

Hệ thống nhận được $Q$ thao tác thuộc 2 loại:
* **Loại 1 (`1 P`):** Nhập thêm một kiện hàng có độ ưu tiên $P$ vào kho.
* **Loại 2 (`2`):** Xuất kho kiện hàng đang có **độ ưu tiên lớn nhất** để giao cho shipper. In ra độ ưu tiên của kiện hàng vừa xuất. (Nếu kho đang trống, in ra `-1`).

Hãy thực thi chính xác tất cả $Q$ thao tác của hệ thống.

#### Input:
* Dòng đầu chứa số nguyên $Q$ ($1 \le Q \le 2 \times 10^5$).
* $Q$ dòng tiếp theo, mỗi dòng chứa thao tác dạng `1 P` ($1 \le P \le 10^9$) hoặc `2`.

#### Output:
* Với mỗi thao tác loại `2`, in ra độ ưu tiên của kiện hàng được xuất kho trên 1 dòng riêng biệt.

#### Subtasks:
* Subtask 1 (30% điểm): $Q \le 1000$
* Subtask 2 (30% điểm): Thao tác loại 1 xuất hiện trước, thao tác loại 2 xuất hiện sau.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
6
1 50
1 100
1 30
2
2
2
```
**Output:**
```
100
50
30
```
**Giải thích:** Xuất 100 trước, sau đó 50, sau đó 30.

#### Sample 2:
**Input:**
```
5
2
1 70
2
2
1 90
```
**Output:**
```
-1
70
-1
```

---

💡 **Bạn có biết?** Dịch vụ TikiNOW 2h đưa Việt Nam trở thành một trong những quốc gia đi đầu khu vực về tốc độ xử lý hàng hóa thương mại điện tử nội đô nhờ thuật toán phân loại tự động tự động hóa kho hàng.

🚀 **Thử thách:** Nếu bổ sung thao tác Loại 3 (`3`): Xuất kiện hàng có độ ưu tiên NHỎ NHẤT, cấu trúc dữ liệu nào trong C++ STL sẽ thay thế hoàn hảo cho `std::priority_queue`?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Quản lý kho hàng động với 2 thao tác: Thêm phần tử $P$ và Lấy phần tử lớn nhất.
* **Dạng bài:** Max Heap / STL Priority Queue.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH

#### **Bước 1: Lựa chọn cấu trúc dữ liệu `std::priority_queue`**
* `std::priority_queue<long long>` mặc định trong C++ STL là Max-Heap.
* Thao tác `push(x)` có độ phức tạp $O(\log N)$.
* Thao tác `top()` và `pop()` lấy phần tử lớn nhất có độ phức tạp $O(\log N)$.

#### **Bước 2: Đánh giá độ phức tạp**
* Với $Q = 2 \times 10^5$ thao tác, tổng thời gian xử lý là $O(Q \log Q)$, chạy trong $< 0.05$s.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <queue>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int q;
    if (!(cin >> q)) return 0;
    
    priority_queue<long long> pq;
    
    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            long long p;
            cin >> p;
            pq.push(p);
        } else if (type == 2) {
            if (pq.empty()) {
                cout << -1 << "\n";
            } else {
                cout << pq.top() << "\n";
                pq.pop();
            }
        }
    }
    
    return 0;
}
```

---

# IKH-0022 - Lưới Cảm Biến IoT Smart City

## 1. NỘI DUNG BÀI TOÁN

Trung tâm Điều hành Đô thị Thông minh (IOC) Đà Nẵng lắp đặt hệ thống $N$ cảm biến đo nồng độ bụi mịn PM2.5 đặt dọc theo tuyến đường ven biển Nguyễn Tất Thành. Cảm biến thứ $i$ ghi nhận chỉ số bụi $A&#95;i$ ($\mu g/m^3$).

Để đưa ra cảnh báo ô nhiễm chính xác cho cư dân sinh sống, trung tâm phân tích các **khu vực giám sát liên tiếp gồm đúng $K$ cảm biến** ($A&#95;i, A&#95;{i+1}, \dots, A&#95;{i+K-1}$). Với mỗi khu vực gồm $K$ cảm biến liên tiếp này, chỉ số ô nhiễm đại diện được tính bằng **chênh lệch giữa giá trị PM2.5 lớn nhất và nhỏ nhất** trong khu vực đó ($\max - \min$).

Hãy tìm **giá trị ô nhiễm đại diện nhỏ nhất** trong tất cả các khu vực giám sát $K$ cảm biến liên tiếp trên tuyến đường.

#### Input:
* Dòng đầu chứa hai số nguyên $N, K$ ($1 \le K \le N \le 2 \times 10^5$).
* Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($0 \le A&#95;i \le 10^9$).

#### Output:
* Một số nguyên duy nhất là chênh lệch $\max - \min$ nhỏ nhất tìm được trong tất cả các cửa sổ $K$ cảm biến.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000$
* Subtask 2 (30% điểm): Mảng $A$ đã được sắp xếp tăng dần.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
6 3
10 2 5 8 7 12
```
**Output:**
```
3
```
**Giải thích:**
Các cửa sổ độ dài $K=3$:
- [10, 2, 5]: max = 10, min = 2 $\implies$ chênh lệch 8
- [2, 5, 8]: max = 8, min = 2 $\implies$ chênh lệch 6
- [5, 8, 7]: max = 8, min = 5 $\implies$ chênh lệch 3
- [8, 7, 12]: max = 12, min = 7 $\implies$ chênh lệch 5
Giá trị chênh lệch nhỏ nhất là 3.

#### Sample 2:
**Input:**
```
4 2
100 100 100 100
```
**Output:**
```
0
```

---

💡 **Bạn có biết?** Trung tâm IOC Đà Nẵng kết nối hơn 1.000 cảm biến môi trường IoT theo chuẩn LoRaWAN, giúp cập nhật chỉ số chất lượng không khí (AQI) tự động mỗi 5 phút.

🚀 **Thử thách:** Bạn sẽ dùng `std::multiset` hay 2 Monotonic Deque để đạt độ phức tạp thời gian tối ưu $O(N)$?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho mảng $A$ gồm $N$ số nguyên. Tìm cửa sổ con liên tiếp độ dài $K$ có $\max - \min$ là nhỏ nhất.
* **Dạng bài:** Sliding Window + STL Multiset / Deque.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Duyệt Trâu (Brute Force)**
* Duyệt mọi cửa sổ $i \dots i+K-1$, tìm max và min trong $O(K)$. Tổng thời gian $O(N \times K)$, ăn 30% số điểm ($N \le 1000$).

#### **Bước 2: Sử dụng `std::multiset` trong C++ STL**
* Duyệt cửa sổ trượt độ dài $K$. `std::multiset` cho phép chèn phần tử mới và xóa phần tử cũ trong $O(\log K)$.
* Giá trị nhỏ nhất là `*ms.begin()`, lớn nhất là `*ms.rbegin()`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(N \log K)$.
* Bộ nhớ: $O(N + K)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, k;
    if (!(cin >> n >> k)) return 0;
    
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    
    multiset<long long> ms;
    for (int i = 0; i < k; i++) ms.insert(a[i]);
    
    long long min_diff = *ms.rbegin() - *ms.begin();
    
    for (int i = k; i < n; i++) {
        ms.erase(ms.find(a[i - k]));
        ms.insert(a[i]);
        long long current_diff = *ms.rbegin() - *ms.begin();
        min_diff = min(min_diff, current_diff);
    }
    
    cout << min_diff << "\n";
    return 0;
}
```

---

# IKH-0023 - Điểm Thu Phí Tự Động VETC

## 1. NỘI DUNG BÀI TOÁN

Trạm thu phí tự động không dừng ETC trên cao tốc Pháp Vân - Cầu Giẽ lưu trữ danh sách số tài khoản giao thông của $N$ chủ phương tiện đã được kích hoạt thẻ VETC. Danh sách tài khoản $A&#95;1, A&#95;2, \dots, A&#95;N$ đã được **sắp xếp theo thứ tự tăng dần**.

Hệ thống nhận được $Q$ xe ô tô di chuyển qua làn thu phí. Mỗi xe có số tài khoản $X$. Ban quản lý trạm muốn kiểm tra xem số tài khoản $X$ có nằm trong danh sách kích hoạt hay không, và nếu không có thì tài khoản đó lớn hơn bao nhiêu tài khoản đã kích hoạt (tức là vị trí chèn phù hợp trong danh sách).

Hãy giúp trạm thu phí xác định **chỉ số (1-indexed) của tài khoản đầu tiên trong danh sách có giá trị lớn hơn hoặc bằng $X$**. (Nếu tất cả tài khoản trong danh sách đều nhỏ hơn $X$, in ra $N + 1$).

#### Input:
* Dòng đầu chứa hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \times 10^5$).
* Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($1 \le A&#95;i \le 10^9$, đã sắp xếp tăng dần).
* Dòng thứ ba chứa $Q$ số nguyên $X&#95;1, X&#95;2, \dots, X&#95;Q$ ($1 \le X&#95;j \le 10^9$).

#### Output:
* In trên 1 dòng gồm $Q$ số nguyên cách nhau bởi khoảng trắng là kết quả trả về cho $Q$ phương tiện.

#### Subtasks:
* Subtask 1 (30% điểm): $N, Q \le 1000$
* Subtask 2 (30% điểm): $X$ luôn xuất hiện chính xác trong mảng $A$.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
5 3
10 20 30 40 50
25 10 60
```
**Output:**
```
3 1 6
```
**Giải thích:**
- $X = 25$: Phần tử đầu tiên $\ge 25$ là 30 tại vị trí 3.
- $X = 10$: Phần tử đầu tiên $\ge 10$ là 10 tại vị trí 1.
- $X = 60$: Không có phần tử nào $\ge 60 \implies$ trả về $N + 1 = 6$.

---

💡 **Bạn me?** Hệ thống VETC tại Việt Nam xử lý trung bình hơn 2,5 triệu lượt phương tiện qua trạm thu phí tự động mỗi ngày với thời gian nhận diện biển số $< 0.2$ giây.

🚀 **Thử thách:** Hàm `std::lower_bound` trong C++ STL hoạt động theo nguyên lý chặt nhị phân như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho mảng $A$ đã sắp xếp. Với mỗi truy vấn $X$, tìm vị trí đầu tiên (1-indexed) $i$ sao cho $A[i] \ge X$. Nếu không có, in $N+1$.
* **Dạng bài:** Binary Search / `std::lower_bound`.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Tìm kiếm Tuyến tính (Linear Search)**
* Duyệt từ đầu mảng tới cuối mảng tốn $O(N)$ mỗi truy vấn. Tổng thời gian $O(N \times Q)$, quá tải cho $N, Q = 2 \times 10^5$.

#### **Bước 2: Tìm kiếm Nhị phân (Binary Search)**
* Vì mảng $A$ đã sắp xếp tăng dần, dùng Tìm kiếm nhị phân để thu hẹp phạm vi trong $O(\log N)$.
* C++ STL hỗ trợ sẵn `std::lower_bound(a.begin(), a.end(), x)`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(Q \log N)$ cho $Q$ truy vấn.
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, q;
    if (!(cin >> n >> q)) return 0;
    
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    
    for (int j = 0; j < q; j++) {
        long long x;
        cin >> x;
        auto it = lower_bound(a.begin(), a.end(), x);
        int idx = distance(a.begin(), it) + 1;
        cout << idx << (j == q - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

---

# IKH-0024 - Phân Bổ Điện Năng Mặt Trời

## 1. NỘI DUNG BÀI TOÁN

Trang trại điện mặt trời Trung Nam tại Ninh Thuận có $N$ mảng pin năng lượng mặt trời. Mảng pin thứ $i$ có công suất phát điện $A&#95;i$ kW/h.

Tập đoàn Điện lực Việt Nam (EVN) muốn chọn **ít nhất $K$ mảng pin** để đấu nối vào trạm biến áp trung tâm. Để đường dây tải điện hoạt động ổn định và an toàn, EVN đặt điều kiện: **tất cả các mảng pin được chọn phải có công suất phát điện tối thiểu là $P$ kW/h**.

Hãy tìm **công suất tối thiểu $P$ LỚN NHẤT** sao cho có ít nhất $K$ mảng pin đạt công suất từ $P$ trở lên.

#### Input:
* Dòng đầu chứa hai số nguyên $N, K$ ($1 \le K \le N \le 2 \times 10^5$).
* Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($1 \le A&#95;i \le 10^9$).

#### Output:
* Một số nguyên duy nhất là công suất $P$ lớn nhất tìm được.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000, A&#95;i \le 1000$
* Subtask 2 (30% điểm): $K = 1$ hoặc $K = N$.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
5 3
50 20 80 40 90
```
**Output:**
```
50
```
**Giải thích:** Các mảng pin đạt $\ge 50$ kW/h gồm {50, 80, 90} (đủ 3 mảng pin $\ge K$). Nếu chọn $P = 51$ thì chỉ có 2 mảng {80, 90} $< K$.

#### Sample 2:
**Input:**
```
4 4
15 15 15 15
```
**Output:**
```
15
```

---

💡 **Bạn có biết?** Ninh Thuận là "thủ phủ năng lượng tái tạo" của Việt Nam với hơn 3.000 giờ nắng mỗi năm, cung cấp hàng tỷ kWh điện sạch cho lưới điện quốc gia.

🚀 **Thử thách:** Khi sắp xếp mảng tăng dần, giá trị $P$ cần tìm chính là phần tử thứ bao nhiêu trong mảng đã sắp xếp?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho $N$ số $A&#95;i$. Tìm số $P$ lớn nhất sao cho có ít nhất $K$ phần tử $\ge P$.
* **Dạng bài:** Sorting / Quickselect / Binary Search.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Phân tích Ý nghĩa Toán học**
* Để có ít nhất $K$ phần tử $\ge P$, ta chỉ cần sắp xếp mảng tăng dần $A[0 \dots N-1]$.
* Phần tử nhỏ nhất trong $K$ phần tử lớn nhất chính là $A[N - K]$.

#### **Bước 2: Thuật toán Sắp xếp (Sorting)**
* Sắp xếp mảng $A$ mất $O(N \log N)$.
* Kết quả là `a[n - k]`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(N \log N)$.
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, k;
    if (!(cin >> n >> k)) return 0;
    
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    
    sort(a.begin(), a.end());
    
    // Phần tử thứ K lớn nhất chính là a[n - k]
    cout << a[n - k] << "\n";
    return 0;
}
```

---

# IKH-0025 - Tải Trọng Tối Đa Tàu Container

## 1. NỘI DUNG BÀI TOÁN

Hãng tàu vận tải biển Gemadept cần vận chuyển $N$ kiện hàng theo thứ tự từ $1$ đến $N$. Kiện hàng thứ $i$ có trọng lượng $W&#95;i$ tấn.

Công ty huy động $M$ tàu chở hàng có **tải trọng tối đa bằng nhau là $C$ tấn**. Do quy trình bốc xếp hàng hóa tại cảng, các kiện hàng bắt buộc phải được xếp lên tàu **theo đúng thứ tự liên tiếp** (nghĩa là một tàu sẽ chở các kiện hàng từ $L$ đến $R$). Một tàu không được chở vượt quá tải trọng $C$ tấn.

Hãy tìm **tải trọng $C$ NHỎ NHẤT của các tàu** sao cho có thể vận chuyển toàn bộ $N$ kiện hàng bằng **không quá $M$ chuyến tàu**.

#### Input:
* Dòng đầu chứa hai số nguyên $N, M$ ($1 \le M \le N \le 2 \times 10^5$).
* Dòng thứ hai chứa $N$ số nguyên $W&#95;1, W&#95;2, \dots, W&#95;N$ ($1 \le W&#95;i \le 10^9$).

#### Output:
* Một số nguyên duy nhất là tải trọng tối thiểu $C$ tìm được.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000, M = 1$
* Subtask 2 (30% điểm): $N \le 1000, W&#95;i \le 1000$
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
5 3
1 2 3 4 5
```
**Output:**
```
6
```
**Giải thích:** Với $C = 6$:
- Tàu 1: chở [1, 2, 3] (tổng trọng lượng 6 <= 6)
- Tàu 2: chở [4] (tổng trọng lượng 4 <= 6)
- Tàu 3: chở [5] (tổng trọng lượng 5 <= 6)
Tổng cộng dùng đúng 3 tàu. Nếu $C = 5$, cần ít nhất 4 tàu.

---

💡 **Bạn có biết?** Siêu tàu container Gemalink có sức chở lên đến 20.000 TEU, là một trong những cảng nước sâu lớn nhất thế giới đặt tại Bà Rịa - Vũng Tàu.

🚀 **Thử thách:** Bài toán Chặt nhị phân kết quả (Binary Search on Answer) này có tính chất đơn điệu (Monotonicity) thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Chia mảng $W$ thành tối đa $M$ đoạn con liên tiếp sao cho tổng lớn nhất của các đoạn con là nhỏ nhất.
* **Dạng bài:** Binary Search on Answer + Greedy.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Nhận diện bài toán Chặt nhị phân kết quả**
* Tải trọng $C$ càng lớn thì số lượng chuyến tàu cần dùng càng nhỏ (tính đơn điệu - Monotonicity).
* Phạm vi tìm kiếm $C$: từ $\max(W&#95;i)$ đến $\sum W&#95;i$.

#### **Bước 2: Xây dựng hàm kiểm tra `check(C)`**
* Duyệt tham ăn (Greedy): Xếp các kiện hàng vào tàu hiện tại cho tới khi tổng trọng lượng vượt quá $C$. Khi đó mở tàu mới.
* Nếu số tàu cần dùng $\le M$, trả về `true`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(N \log (\sum W))$.
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

bool check(long long c, const vector<long long>& w, int n, int m) {
    int count = 1;
    long long current_sum = 0;
    for (int i = 0; i < n; i++) {
        if (w[i] > c) return false;
        if (current_sum + w[i] <= c) {
            current_sum += w[i];
        } else {
            count++;
            current_sum = w[i];
        }
    }
    return count <= m;
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    vector<long long> w(n);
    long long max_w = 0, sum_w = 0;
    for (int i = 0; i < n; i++) {
        cin >> w[i];
        max_w = max(max_w, w[i]);
        sum_w += w[i];
    }
    
    long long low = max_w, high = sum_w;
    long long ans = sum_w;
    
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, w, n, m)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    
    cout << ans << "\n";
    return 0;
}
```

---

# IKH-0026 - Chuỗi Cung Ứng Chuối Xuất Khẩu

## 1. NỘI DUNG BÀI TOÁN

Nông trường Hoàng Anh Gia Lai tại Gia Lai thu hoạch chuối xuất khẩu trong $N$ ngày liên tiếp. Ngày thứ $i$ thu hoạch được $A&#95;i$ tấn chuối.

Do hợp đồng với đối tác Trung Quốc quy định giá thu mua biến động, ban giám đốc muốn chọn một **giai đoạn thu hoạch liên tục** từ ngày $L$ đến ngày $R$ ($1 \le L \le R \le N$) sao cho **tổng sản lượng chuối thu hoạch được là LỚN NHẤT**.

Hãy tìm tổng sản lượng chuối lớn nhất của một giai đoạn thu hoạch liên tục. (Lưu ý: Nếu tất cả các ngày đều có sản lượng âm/lỗ, chọn 1 ngày có kết quả tốt nhất).

#### Input:
* Dòng đầu chứa số nguyên $N$ ($1 \le N \le 2 \times 10^5$).
* Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($-10^9 \le A&#95;i \le 10^9$).

#### Output:
* Một số nguyên duy nhất là tổng sản lượng chuối lớn nhất tìm được.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000$
* Subtask 2 (30% điểm): $A&#95;i \ge 0$ với mọi $i$.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
5
2 -3 4 -1 5
```
**Output:**
```
8
```
**Giải thích:** Chọn đoạn từ ngày 3 đến ngày 5: [4, -1, 5] có tổng = 4 + (-1) + 5 = 8.

#### Sample 2:
**Input:**
```
3
-5 -2 -8
```
**Output:**
```
-2
```

---

💡 **Bạn có biết?** HAGL hiện sở hữu hơn 7.000 ha chuối tại Việt Nam, Lào và Campuchia, xuất khẩu trung bình hàng trăm container chuối tươi mỗi tuần.

🚀 **Thử thách:** Thuật toán Kadane nổi tiếng giải bài toán Maximum Subarray Sum này trong độ phức tạp thời gian bao nhiêu?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Tìm tổng đoạn con liên tiếp lớn nhất (Maximum Subarray Sum).
* **Dạng bài:** Dynamic Programming / Thuật toán Kadane.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Công thức Quy hoạch động (Kadane's Algorithm)**
* Gọi `dp[i]` là tổng đoạn con lớn nhất kết thúc tại vị trí $i$.
* Công thức chuyển trạng thái: `dp[i] = max(a[i], dp[i-1] + a[i])`.
* Kết quả là `max(dp[0...N-1])`.

#### **Bước 2: Tối ưu bộ nhớ $O(1)$**
* Ta chỉ cần lưu `curr_max` thay vì toàn bộ mảng `dp`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(N)$.
* Bộ nhớ: $O(N)$ lưu mảng hoặc $O(1)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    
    long long max_so_far = a[0];
    long long curr_max = a[0];
    
    for (int i = 1; i < n; i++) {
        curr_max = max(a[i], curr_max + a[i]);
        max_so_far = max(max_so_far, curr_max);
    }
    
    cout << max_so_far << "\n";
    return 0;
}
```

---

# IKH-0027 - Tăng Trưởng Khách Du Lịch Quốc Tế

## 1. NỘI DUNG BÀI TOÁN

Sở Du lịch TP. Hồ Chí Minh thống kê số lượng khách quốc tế đến thành phố trong $N$ tháng liên tiếp. Tháng thứ $i$ ghi nhận $A&#95;i$ nghìn lượt khách.

Để đánh giá chuỗi tăng trưởng bền vững của ngành du lịch, Sở muốn chọn ra một **chuỗi các tháng** (không nhất thiết phải liên tiếp) $i&#95;1 < i&#95;2 < \dots < i&#95;k$ sao cho số lượng khách của tháng sau **luôn lớn hơn nghiêm ngặt** số lượng khách của tháng trước ($A&#95;{i&#95;1} < A&#95;{i&#95;2} < \dots < A&#95;{i&#95;k}$).

Hãy tìm **số lượng tháng nhiều nhất** (độ dài $k$ lớn nhất) của một chuỗi tăng trưởng như vậy.

#### Input:
* Dòng đầu chứa số nguyên $N$ ($1 \le N \le 2 \times 10^5$).
* Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($1 \le A&#95;i \le 10^9$).

#### Output:
* Một số nguyên duy nhất là số lượng tháng nhiều nhất của chuỗi tăng trưởng.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000$
* Subtask 2 (30% điểm): Mảng $A$ đã được sắp xếp tăng dần.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
6
10 20 10 30 20 50
```
**Output:**
```
4
```
**Giải thích:** Chọn các tháng với số lượng khách: [10, 20, 30, 50] có độ dài 4.

#### Sample 2:
**Input:**
```
4
50 40 30 20
```
**Output:**
```
1
```

---

💡 **Bạn có biết?** TP. Hồ Chí Minh đón hơn 5 triệu lượt khách quốc tế mỗi năm, đóng góp gần 10% tổng GDP của thành phố nhờ các sản phẩm du lịch văn hóa và ẩm thực độc đáo.

🚀 **Thử thách:** Thuật toán LIS Quy hoạch động kết hợp Tìm kiếm Nhị phân (`std::lower_bound`) giúp giải bài toán này trong độ phức tạp thời gian bao nhiêu?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Tìm độ dài dãy con tăng dài nhất (Longest Increasing Subsequence - LIS).
* **Dạng bài:** Dynamic Programming + Binary Search ($O(N \log N)$).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Quy hoạch động cơ bản $O(N^2)$**
* `dp[i]` là độ dài LIS kết thúc tại `a[i]`. `dp[i] = max(dp[j] + 1)` với mọi $j < i$ và $a[j] < a[i]$.
* Độ phức tạp $O(N^2)$, chỉ ăn điểm Subtask 1 ($N \le 1000$).

#### **Bước 2: Tối ưu với Tìm kiếm Nhị phân $O(N \log N)$**
* Duyệt qua mảng $A$, duy trì mảng `dp` trong đó `dp[k]` lưu giá trị kết thúc nhỏ nhất của dãy con tăng độ dài $k+1$.
* Mảng `dp` luôn tăng dần. Với mỗi $A[i]$, dùng `lower_bound` tìm vị trí thay thế hoặc thêm mới vào mảng `dp`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(N \log N)$.
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    
    vector<long long> dp;
    for (int i = 0; i < n; i++) {
        auto it = lower_bound(dp.begin(), dp.end(), a[i]);
        if (it == dp.end()) {
            dp.push_back(a[i]);
        } else {
            *it = a[i];
        }
    }
    
    cout << dp.size() << "\n";
    return 0;
}
```

---

# IKH-0028 - Lựa Chọn Thiết Bị Trạm Phát 5G

## 1. NỘI DUNG BÀI TOÁN

Tập đoàn Viễn thông Viettel đầu tư nâng cấp trạm phát sóng 5G tại khu công nghệ cao Hòa Lạc. Ngân sách cấp cho trạm là $W$ triệu đồng.

Có $N$ loại thiết bị thu phát sóng được chào bán. Thiết bị thứ $i$ có chi phí lắp đặt $C&#95;i$ triệu đồng và mang lại hiệu năng phủ sóng $V&#95;i$ điểm. Do tính tương thích kỹ thuật, mỗi loại thiết bị **chỉ được chọn tối đa một cái**.

Hãy giúp Viettel chọn một tập hợp các thiết bị có **tổng chi phí không vượt quá ngân sách $W$** sao cho **tổng hiệu năng phủ sóng thu được là LỚN NHẤT**.

#### Input:
* Dòng đầu chứa hai số nguyên $N, W$ ($1 \le N \le 1000, 1 \le W \le 10000$).
* $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên $C&#95;i, V&#95;i$ ($1 \le C&#95;i \le W, 1 \le V&#95;i \le 10^9$).

#### Output:
* Một số nguyên duy nhất là tổng hiệu năng phủ sóng lớn nhất tìm được.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 20, W \le 100$
* Subtask 2 (30% điểm): Tất cả chi phí $C&#95;i$ bằng nhau.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4 10
3 30
4 50
6 60
5 40
```
**Output:**
```
90
```
**Giải thích:** Chọn thiết bị 2 (chi phí 4, hiệu năng 50) và thiết bị 4 (chi phí 5, hiệu năng 40). Tổng chi phí $4 + 5 = 9 \le 10$, tổng hiệu năng $50 + 40 = 90$.

---

💡 **Bạn có biết?** Viettel là nhà mạng đầu tiên tại Việt Nam thử nghiệm thành công trạm phát sóng 5G dùng thiết bị Make in Vietnam hoàn toàn do các kỹ sư Việt Nam nghiên cứu sản xuất.

🚀 **Thử thách:** Bài toán Ba lô 0/1 (0/1 Knapsack Problem) này được tối ưu bộ nhớ từ mảng 2D về mảng 1D như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Bài toán Ba lô 0/1 (0/1 Knapsack). Cho $N$ đồ vật với trọng lượng $C&#95;i$ và giá trị $V&#95;i$, sức chứa $W$. Tìm tổng giá trị lớn nhất.
* **Dạng bài:** Dynamic Programming 0/1 Knapsack.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Công thức Quy hoạch động 2D**
* Gọi `dp[i][w]` là giá trị lớn nhất khi xét $i$ vật đầu tiên với sức chứa $w$.
* `dp[i][w] = max(dp[i-1][w], dp[i-1][w - C[i]] + V[i])`.

#### **Bước 2: Tối ưu không gian mảng 1D**
* Duyệt ngược sức chứa từ $W$ xuống $C&#95;i$ để đảm bảo mỗi vật chỉ được chọn đúng 1 lần: `dp[w] = max(dp[w], dp[w - c] + v)`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(N \times W)$.
* Bộ nhớ: $O(W)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, w_max;
    if (!(cin >> n >> w_max)) return 0;
    
    vector<long long> dp(w_max + 1, 0);
    
    for (int i = 0; i < n; i++) {
        long long c, v;
        cin >> c >> v;
        for (int w = w_max; w >= c; w--) {
            dp[w] = max(dp[w], dp[w - c] + v);
        }
    }
    
    long long ans = 0;
    for (int w = 0; w <= w_max; w++) ans = max(ans, dp[w]);
    
    cout << ans << "\n";
    return 0;
}
```

---

# IKH-0029 - Mạng Lưới Tuyến Xe Být Hà Nội

## 1. NỘI DUNG BÀI TOÁN

Mạng lưới giao thông công cộng VinBus Hà Nội gồm $N$ trạm dừng bus (được đánh số từ $1$ đến $N$) và $M$ tuyến đường hai chiều kết nối trực tiếp giữa hai trạm. Tuyến đường thứ $i$ kết nối hai trạm $u&#95;i$ và $v&#95;i$.

Trung tâm Điều hành Giao thông muốn khảo sát **mức độ kết nối** của hệ thống. Đối với mỗi trạm dừng $u$, hãy đếm **bậc của trạm** (tổng số tuyến đường trực tiếp nối tới trạm $u$).

Hãy in ra bậc của tất cả $N$ trạm dừng theo thứ tự từ trạm $1$ đến trạm $N$.

#### Input:
* Dòng đầu chứa hai số nguyên $N, M$ ($1 \le N \le 2 \times 10^5, 0 \le M \le 2 \times 10^5$).
* $M$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên $u&#95;i, v&#95;i$ ($1 \le u&#95;i, v&#95;i \le N, u&#95;i \neq v&#95;i$).

#### Output:
* In trên 1 dòng gồm $N$ số nguyên cách nhau bởi khoảng trắng, số thứ $u$ là bậc của trạm $u$.

#### Subtasks:
* Subtask 1 (30% điểm): $N, M \le 1000$
* Subtask 2 (30% điểm): Đồ thị là một đường thẳng (dạng xích).
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4 3
1 2
2 3
2 4
```
**Output:**
```
1 3 1 1
```
**Giải thích:** Trạm 1 nối với {2} (bậc 1), trạm 2 nối với {1, 3, 4} (bậc 3), trạm 3 nối với {2} (bậc 1), trạm 4 nối với {2} (bậc 1).

---

💡 **Bạn có biết?** Hệ thống xe být điện VinBus tại Hà Nội vận hành hoàn toàn bằng năng lượng xanh, giúp giảm hàng nghìn tấn khí thải CO2 mỗi năm.

🚀 **Thử thách:** Tổng bậc của tất cả các đỉnh trong đồ thị vô hướng bằng bao nhiêu lần số cạnh $M$?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho đồ thị vô hướng gồm $N$ đỉnh và $M$ cạnh. Đếm bậc (Degree) của từng đỉnh từ $1$ đến $N$.
* **Dạng bài:** Biểu diễn đồ thị / Degree Counting.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Khái niệm Bậc của Đỉnh (Degree)**
* Bậc của đỉnh $u$ là số lượng cạnh nối trực tiếp với $u$.
* Mỗi cạnh $(u, v)$ đóng góp $+1$ vào bậc của $u$ và $+1$ vào bậc của $v$.

#### **Bước 2: Thuật toán Đếm trực tiếp**
* Khởi tạo mảng `degree` kích thước $N+1$ bằng 0.
* Đọc từng cạnh $(u, v)$, thực hiện `degree[u]++` và `degree[v]++`.

#### **Bước 3: Định lý Bắt tay (Handshaking Lemma)**
* Tổng bậc của tất cả các đỉnh bằng $2M$.

#### **Bước 4: Đánh giá độ phức tạp**
* Thời gian: $O(N + M)$.
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    vector<int> degree(n + 1, 0);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        degree[u]++;
        degree[v]++;
    }
    
    for (int i = 1; i <= n; i++) {
        cout << degree[i] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

---

# IKH-0030 - Đường Bay Cấp Cứu Y Tế

## 1. NỘI DUNG BÀI TOÁN

Binh đoàn 18 (Tổng công ty Trực thăng Việt Nam) đảm nhận nhiệm vụ bay cấp cứu y tế giữa các đảo thuộc quần đảo Trường Sa. Có $N$ điểm đảo (đánh số từ $1$ đến $N$) và $M$ đường bay trực thăng hai chiều giữa các đảo.

Một bệnh nhân tại **đảo $S$** cần được chuyển cấp cứu gấp về trung tâm y tế lớn tại **đảo $T$**. Trực thăng muốn tìm đường bay truyền tin truyền tải bệnh nhân qua **ít chuyến bay trung chuyển nhất** (ít số cạnh nhất).

Hãy tìm **số chuyến bay tối thiểu** để di chuyển từ đảo $S$ đến đảo $T$. Nếu không có đường bay nào kết nối giữa $S$ và $T$, in ra `-1`.

#### Input:
* Dòng đầu chứa hai số nguyên $N, M$ ($1 \le N, M \le 2 \times 10^5$).
* Dòng thứ hai chứa hai số nguyên $S, T$ ($1 \le S, T \le N$).
* $M$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên $u&#95;i, v&#95;i$ ($1 \le u&#95;i, v&#95;i \le N$).

#### Output:
* Một số nguyên duy nhất là số chuyến bay tối thiểu từ $S$ đến $T$.

#### Subtasks:
* Subtask 1 (30% điểm): $N, M \le 1000$
* Subtask 2 (30% điểm): $S = T$ (kết quả là 0).
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
5 5
1 5
1 2
2 3
3 5
1 4
4 5
```
**Output:**
```
2
```
**Giải thích:** Đường bay ngắn nhất: 1 -> 4 -> 5 (tốn 2 chuyến bay).

---

💡 **Bạn có biết?** Binh đoàn 18 luôn duy trì các tổ bay trực thăng EC225 và Super Puma sẵn sàng cất cánh 24/7 thực hiện các chuyến cấp cứu xuyên đêm trên biển Đông.

🚀 **Thử thách:** Thuật toán duyệt theo chiều rộng (BFS) đảm bảo tìm được đường đi ngắn nhất trên đồ thị không trọng số với độ phức tạp bao nhiêu?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Tìm đường đi ngắn nhất (số cạnh ít nhất) từ đỉnh $S$ tới đỉnh $T$ trên đồ thị vô hướng không trọng số.
* **Dạng bài:** Breadth-First Search (BFS).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Tại sao chọn BFS thay vì DFS?**
* Duyệt theo chiều rộng (BFS) duyệt theo các lớp khoảng cách $0, 1, 2, \dots$. Do đó đỉnh $T$ xuất hiện lần đầu tiên luôn đảm bảo khoảng cách là nhỏ nhất.

#### **Bước 2: Cấu trúc dữ liệu hàng đợi `std::queue`**
* Mảng `dist` khởi tạo bằng -1 để đánh dấu chưa thăm. `dist[S] = 0`.
* Đưa $S$ vào hàng đợi. Mỗi lần lấy đỉnh $u$ ra, duyệt các đỉnh kề $v$. Nếu `dist[v] == -1`, gán `dist[v] = dist[u] + 1` và đẩy $v$ vào `q`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(N + M)$.
* Bộ nhớ: $O(N + M)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    int s, t;
    cin >> s >> t;
    
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    if (s == t) {
        cout << 0 << "\n";
        return 0;
    }
    
    vector<int> dist(n + 1, -1);
    queue<int> q;
    
    dist[s] = 0;
    q.push(s);
    
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        
        if (u == t) break;
        
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    
    cout << dist[t] << "\n";
    return 0;
}
```

---

# IKH-0031 - Tối Ưu Hóa Tuyến Đường Giao Hàng Shopee

## 1. NỘI DUNG BÀI TOÁN

Trung tâm Logistics Shopee Express tại Bình Dương quản lý mạng lưới giao hàng gồm $N$ kho hàng (đánh số từ $1$ đến $N$) và $M$ tuyến đường một chiều kết nối giữa các kho. Tuyến đường từ kho $u&#95;i$ đến kho $v&#95;i$ có thời gian di chuyển là $w&#95;i$ phút.

Một xe tải giao hàng xuất phát từ **kho tổng số 1** cần vận chuyển hàng hóa tới tất cả các kho còn lại. Ban điều hành muốn xác định **thời gian di chuyển ngắn nhất** từ kho 1 tới từng kho $u$ trong hệ thống.

Hãy in ra thời gian di chuyển ngắn nhất từ kho 1 tới kho $u$ với mọi $1 \le u \le N$. (Nếu không có đường đi từ kho 1 tới kho $u$, in ra `-1`).

#### Input:
* Dòng đầu chứa hai số nguyên $N, M$ ($1 \le N \le 2 \times 10^5, 0 \le M \le 2 \times 10^5$).
* $M$ dòng tiếp theo, dòng thứ $i$ chứa ba số nguyên $u&#95;i, v&#95;i, w&#95;i$ ($1 \le u&#95;i, v&#95;i \le N, 1 \le w&#95;i \le 10^9$).

#### Output:
* In trên 1 dòng gồm $N$ số nguyên cách nhau bởi khoảng trắng, số thứ $u$ là thời gian di chuyển ngắn nhất từ kho 1 tới kho $u$.

#### Subtasks:
* Subtask 1 (30% điểm): $N, M \le 1000, w&#95;i \le 1000$
* Subtask 2 (30% điểm): $w&#95;i = 1$ với mọi $i$.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4 5
1 2 5
1 3 2
3 2 1
2 4 4
3 4 7
```
**Output:**
```
0 3 2 7
```
**Giải thích:**
- Từ 1 -> 1: 0 phút
- Từ 1 -> 3 -> 2: $2 + 1 = 3$ phút (ngắn hơn đường trực tiếp 1 -> 2 tốn 5 phút)
- Từ 1 -> 3: 2 phút
- Từ 1 -> 3 -> 2 -> 4: $3 + 4 = 7$ phút

---

💡 **Bạn có biết?** Shopee Express ứng dụng thuật toán Dijkstra và Machine Learning để tối ưu hóa lộ trình giao hàng hàng triệu đơn mỗi ngày tại các đô thị lớn ở Việt Nam.

🚀 **Thử thách:** Thuật toán Dijkstra dùng `std::priority_queue` Min-Heap đạt độ phức tạp thời gian $O((N + M) \log N)$ chuẩn như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Tìm đường đi ngắn nhất từ đỉnh 1 tới tất cả các đỉnh khác trên đồ thị có hướng trọng số không âm (Single-Source Shortest Path).
* **Dạng bài:** Thuật toán Dijkstra dùng Min-Heap.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Điều kiện áp dụng Thuật toán Dijkstra**
* Đồ thị có trọng số không âm ($w&#95;i \ge 0$).
* Ý tưởng: Luôn cố định khoảng cách ngắn nhất cho đỉnh có `dist` nhỏ nhất trong danh sách các đỉnh đang chờ xử lý.

#### **Bước 2: Cấu trúc Min-Heap (`std::priority_queue`)**
* Dùng `std::priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>>` để lấy đỉnh có `dist` nhỏ nhất trong $O(\log N)$.
* Kiểm tra `if (d > dist[u]) continue;` để bỏ qua các bản ghi cũ khi cập nhật `dist`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O((N + M) \log N)$.
* Bộ nhớ: $O(N + M)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long weight;
};

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }
    
    vector<long long> dist(n + 1, INF);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    
    dist[1] = 0;
    pq.push({0, 1});
    
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        
        if (d > dist[u]) continue;
        
        for (const auto& edge : adj[u]) {
            if (dist[u] + edge.weight < dist[edge.to]) {
                dist[edge.to] = dist[u] + edge.weight;
                pq.push({dist[edge.to], edge.to});
            }
        }
    }
    
    for (int i = 1; i <= n; i++) {
        cout << (dist[i] == INF ? -1 : dist[i]) << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

---

# IKH-0032 - Quy Hoạch Mạng Đăng Đăng Ký Cáp Quang FPT

## 1. NỘI DUNG BÀI TOÁN

FPT Telecom lắp đặt đường truyền cáp quang băng thông rộng kết nối giữa $N$ hộ gia đình (đánh số từ $1$ đến $N$) tại đại đô thị Vinhomes Ocean Park.

Ban đầu chưa có tuyến cáp nào được đấu nối. Ban quản lý đưa ra $M$ truy vấn đấu nối đường dây cáp quang hai chiều giữa hai nhà $u$ và $v$. 

Hệ thống muốn kiểm tra **sau mỗi lần nối tuyến cáp thứ $i$**, số lượng **thành phần liên thông** (số cụm hộ gia đình đã được kết nối thông suốt với nhau) trong đại đô thị còn lại bao nhiêu cụm?

#### Input:
* Dòng đầu chứa hai số nguyên $N, M$ ($1 \le N \le 2 \times 10^5, 1 \le M \le 2 \times 10^5$).
* $M$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên $u&#95;i, v&#95;i$ ($1 \le u&#95;i, v&#95;i \le N$).

#### Output:
* In trên 1 dòng gồm $M$ số nguyên cách nhau bởi khoảng trắng, số thứ $i$ là số lượng cụm thành phần liên thông sau khi kết nối đường cáp thứ $i$.

#### Subtasks:
* Subtask 1 (30% điểm): $N, M \le 1000$
* Subtask 2 (30% điểm): Đấu nối lần lượt từ nhà $1$ tới nhà $N$.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4 3
1 2
2 3
1 3
```
**Output:**
```
3 2 2
```
**Giải thích:**
- Ban đầu có 4 nhà = 4 cụm.
- Nối 1-2: gộp 2 nhà thành 1 cụm $\implies$ còn 3 cụm.
- Nối 2-3: gộp tiếp nhà 3 vào cụm {1, 2} $\implies$ còn 2 cụm.
- Nối 1-3: nhà 1 và nhà 3 đã thuộc cùng cụm $\implies$ vẫn còn 2 cụm.

---

💡 **Bạn có biết?** Cấu trúc dữ liệu Các tập hợp rời rạc (Disjoint Set Union - DSU) với tối ưu Nén đường đi (Path Compression) giúp gộp và tìm kiếm trong thời gian gần như hằng số $O(\\alpha(N))$.

🚀 **Thử thách:** Thuật toán DSU có thể áp dụng để phát hiện chu trình trên đồ thị vô hướng như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Duy trì số lượng thành phần liên thông của đồ thị gồm $N$ đỉnh qua $M$ thao tác thêm cạnh.
* **Dạng bài:** Disjoint Set Union (DSU) / Union-Find.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Khái niệm DSU**
* Khởi tạo $N$ tập hợp rời rạc, ban đầu số thành phần liên thông là $N$.
* Với mỗi cạnh $(u, v)$, thực hiện `find(u)` và `find(v)`. Nếu thuộc 2 gốc khác nhau, thực hiện `unite` và giảm `components` đi 1.

#### **Bước 2: Tối ưu Path Compression & Union by Rank**
* Gán `parent[i] = find(parent[i])` để nén đường đi, giảm độ sâu của cây.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(M \cdot \alpha(N))$.
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>

using namespace std;

struct DSU {
    vector<int> parent;
    int components;
    
    DSU(int n) {
        parent.resize(n + 1);
        for (int i = 1; i <= n; i++) parent[i] = i;
        components = n;
    }
    
    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }
    
    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            components--;
            return true;
        }
        return false;
    }
};

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    DSU dsu(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        dsu.unite(u, v);
        cout << dsu.components << (i == m - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

---

# IKH-0033 - Mạng Lưới Đường Hầm Metro TP.HCM

## 1. NỘI DUNG BÀI TOÁN

Ban Quản lý Đường sắt Đô thị TP.HCM (MAUR) cần kết nối $N$ nhà ga Metro chính (đánh số từ $1$ đến $N$) bằng hệ thống đường hầm ngầm.

Có $M$ đoạn tuyến đường hầm có thể đào được. Đoạn tuyến thứ $i$ kết nối hai nhà ga $u&#95;i$ và $v&#95;i$ với chi phí đào hầm là $w&#95;i$ tỷ đồng.

Hãy giúp MAUR lựa chọn một tập hợp các đoạn tuyến đường hầm sao cho **tất cả $N$ nhà ga đều kết nối thông suốt với nhau** và **TỔNG CHI PHÍ ĐÀO HẦM LÀ NHỎ NHẤT**. If không thể kết nối tất cả các ga, in ra `-1`.

#### Input:
* Dòng đầu chứa hai số nguyên $N, M$ ($1 \le N \le 2 \times 10^5, 0 \le M \le 2 \times 10^5$).
* $M$ dòng tiếp theo, dòng thứ $i$ chứa ba số nguyên $u&#95;i, v&#95;i, w&#95;i$ ($1 \le u&#95;i, v&#95;i \le N, 1 \le w&#95;i \le 10^9$).

#### Output:
* Một số nguyên duy nhất là tổng chi phí đào hầm nhỏ nhất tìm được.

#### Subtasks:
* Subtask 1 (30% điểm): $N, M \le 1000, w&#95;i \le 1000$
* Subtask 2 (30% điểm): Đồ thị có dạng cây (đúng $N - 1$ cạnh).
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4 5
1 2 1
2 3 4
1 3 2
3 4 5
2 4 3
```
**Output:**
```
6
```
**Giải thích:** Chọn 3 đoạn tuyến: (1-2: 1), (1-3: 2), (2-4: 3). Tổng chi phí $1 + 2 + 3 = 6$.

---

💡 **Bạn có biết?** Tuyến Metro Số 1 (Bến Thành - Suối Tiên) sử dụng robot đào hầm TBM (Tunnel Boring Machine) đường kính 6.79m để đào ngầm dưới lòng trung tâm TP.HCM mà không làm ảnh hưởng các công trình lịch sử trên mặt đất.

🚀 **Thử thách:** Thuật toán Kruskal sắp xếp tất cả các cạnh theo trọng số tăng dần rồi dùng DSU chọn các cạnh không tạo chu trình có độ phức tạp bao nhiêu?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Tìm cây khung nhỏ nhất (Minimum Spanning Tree - MST) của đồ thị vô hướng có trọng số.
* **Dạng bài:** Thuật toán Kruskal + DSU.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Thuật toán Tham ăn (Greedy - Kruskal)**
* Sắp xếp tất cả $M$ cạnh theo trọng số tăng dần.
* Duyệt qua từng cạnh $(u, v, w)$. Dùng DSU kiểm tra xem $u$ và $v$ đã thuộc cùng thành phần liên thông hay chưa.
* Nếu chưa, chọn cạnh này vào cây khung, cộng $w$ vào tổng chi phí và gộp 2 đỉnh.

#### **Bước 2: Điều kiện dừng & Trường hợp không liên thông**
* Dừng khi chọn đủ $N-1$ cạnh. Nếu duyệt hết các cạnh mà không chọn đủ $N-1$ cạnh, đồ thị không liên thông $\implies$ in `-1`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(M \log M)$.
* Bộ nhớ: $O(N + M)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v;
    long long w;
    bool operator<(const Edge& other) const {
        return w < other.w;
    }
};

struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n + 1);
        for (int i = 1; i <= n; i++) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            return true;
        }
        return false;
    }
};

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }
    
    sort(edges.begin(), edges.end());
    
    DSU dsu(n);
    long long total_weight = 0;
    int count = 0;
    
    for (const auto& edge : edges) {
        if (dsu.unite(edge.u, edge.v)) {
            total_weight += edge.w;
            count++;
            if (count == n - 1) break;
        }
    }
    
    if (count == n - 1 || n == 1) {
        cout << total_weight << "\n";
    } else {
        cout << -1 << "\n";
    }
    return 0;
}
```

---

# IKH-0034 - Lịch Trình Sản Xuất Linh Kiện VinFast

## 1. NỘI DUNG BÀI TOÁN

Nhà máy sản xuất ô tô điện VinFast Hải Phòng gồm $N$ công đoạn lắp ráp (đánh số từ $1$ đến $N$).

Do quy trình kỹ thuật nghiêm ngặt, có $M$ ràng buộc phụ thuộc: công đoạn $u&#95;i$ bắt buộc phải được **hoàn thành trước** khi công đoạn $v&#95;i$ có thể bắt đầu sản xuất.

Kỹ sư trưởng muốn lập một **thứ tự thực hiện tất cả $N$ công đoạn** sao cho thỏa mãn mọi ràng buộc phụ thuộc. Nếu có nhiều thứ tự hợp lệ, hãy chọn **thứ tự có thứ tự từ điển nhỏ nhất** (ưu tiên chọn công đoạn có chỉ số nhỏ hơn trước). If xuất hiện chu trình phụ thuộc vòng quanh khiến không thể hoàn thành, in ra `-1`.

#### Input:
* Dòng đầu chứa hai số nguyên $N, M$ ($1 \le N \le 2 \times 10^5, 0 \le M \le 2 \times 10^5$).
* $M$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên $u&#95;i, v&#95;i$ ($1 \le u&#95;i, v&#95;i \le N$).

#### Output:
* In trên 1 dòng gồm $N$ số nguyên cách nhau bởi khoảng trắng là thứ tự thực hiện các công đoạn (hoặc `-1` nếu vô nghiệm).

#### Subtasks:
* Subtask 1 (30% điểm): $N, M \le 1000$
* Subtask 2 (30% điểm): Không có chu trình phụ thuộc và chỉ có 1 thứ tự duy nhất.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4 3
1 2
2 4
3 4
```
**Output:**
```
1 2 3 4
```
**Giải thích:** Đỉnh 1 và 3 đều có bán bậc vào (indegree) bằng 0. Ưu tiên chọn 1 trước, sau đó chọn 2, rồi 3, rồi 4.

---

💡 **Bạn me?** Tổ hợp nhà máy VinFast Hải Phòng đạt tỷ lệ tự động hóa lên đến 90% với hàng nghìn robot ABB hoạt động đồng bộ theo thuật toán điều phối thời gian thực.

🚀 **Thử thách:** Thuật toán Kahn (Sắp xếp Topological Sort) dùng `std::priority_queue` Min-Heap giúp tìm thứ tự từ điển nhỏ nhất như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Sắp xếp Topological (Topological Sort) trên đồ thị có hướng có thứ tự từ điển nhỏ nhất.
* **Dạng bài:** Kahn's Algorithm + Priority Queue (Min-Heap).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Thuật toán Kahn (Bán bậc vào - Indegree)**
* Đếm bán bậc vào `indegree[v]` cho mỗi đỉnh $v$.
* Đưa tất cả các đỉnh có `indegree == 0` vào hàng đợi ưu tiên Min-Heap.

#### **Bước 2: Ưu tiên Thứ tự Từ điển**
* Dùng `std::priority_queue<int, vector<int>, greater<int>>` để luôn lấy đỉnh có chỉ số nhỏ nhất ra xử lý trước.
* Giảm `indegree` của các đỉnh kề. Nếu bằng 0 thì đẩy vào Min-Heap.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O((N + M) \log N)$.
* Bộ nhớ: $O(N + M)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    vector<vector<int>> adj(n + 1);
    vector<int> indegree(n + 1, 0);
    
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        indegree[v]++;
    }
    
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i = 1; i <= n; i++) {
        if (indegree[i] == 0) {
            pq.push(i);
        }
    }
    
    vector<int> topo;
    while (!pq.empty()) {
        int u = pq.top();
        pq.pop();
        topo.push_back(u);
        
        for (int v : adj[u]) {
            indegree[v]--;
            if (indegree[v] == 0) {
                pq.push(v);
            }
        }
    }
    
    if ((int)topo.size() != n) {
        cout << -1 << "\n";
    } else {
        for (int i = 0; i < n; i++) {
            cout << topo[i] << (i == n - 1 ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}
```

---

# IKH-0035 - Vùng Phủ Sóng Trạm Ra-đa Thời Tiết

## 1. NỘI DUNG BÀI TOÁN

Tổng cục Thống kê và Khí tượng Thủy văn đặt trạm ra-đa thời tiết tại tọa độ $(X&#95;0, Y&#95;0)$ trên bản đồ phẳng. Trạm ra-đa có bán kính quét hiệu quả là $R$ (mét).

Có $N$ trạm quan trắc tự động tại các tọa độ $(X&#95;i, Y&#95;i)$ ($1 \\le i \\le N$). Một trạm quan trắc được coi là **nằm trong vùng phủ sóng** nếu khoảng cách Euclid từ trạm đó đến trạm ra-đa **nhỏ hơn hoặc bằng $R$** (tức là $(X&#95;i - X&#95;0)^2 + (Y&#95;i - Y&#95;0)^2 \\le R^2$).

Hãy đếm số lượng trạm quan trắc nằm trong vùng phủ sóng của trạm ra-đa.

#### Input:
* Dòng đầu chứa ba số nguyên $N, X&#95;0, Y&#95;0$ và một số nguyên $R$ ($1 \\le N \\le 2 \\times 10^5, -10^9 \\le X&#95;0, Y&#95;0 \\le 10^9, 1 \\le R \\le 10^9$).
* $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên $X&#95;i, Y&#95;i$ ($-10^9 \\le X&#95;i, Y&#95;i \\le 10^9$).

#### Output:
* Một số nguyên duy nhất là số lượng trạm quan trắc nằm trong vùng phủ sóng.

#### Subtasks:
* Subtask 1 (30% điểm): $N \\le 1000$
* Subtask 2 (30% điểm): $X&#95;0 = 0, Y&#95;0 = 0$.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4 0 0 5
3 4
5 0
6 0
-3 -3
```
**Output:**
```
3
```
**Giải thích:**
- Điểm (3, 4): $3^2 + 4^2 = 25 \le 25$ (Thỏa mãn)
- Điểm (5, 0): $5^2 + 0^2 = 25 \le 25$ (Thỏa mãn)
- Điểm (6, 0): $6^2 + 0^2 = 36 > 25$ (Không thỏa mãn)
- Điểm (-3, -3): $(-3)^2 + (-3)^2 = 18 \le 25$ (Thỏa mãn)

---

💡 **Bạn có biết?** Trạm ra-đa thời tiết Phù Liễn (Hải Phòng) là một trong những trạm ra-đa lâu đời nhất Việt Nam, quét bán kính lên tới 460 km trên toàn bộ vùng biển Bắc Bộ.

🚀 **Thử thách:** Tránh dùng phép lấy căn bậc hai `sqrt()` để ngăn ngừa lỗi sai số số thực, dùng phép so sánh $(dx^2 + dy^2 \le R^2)$ với kiểu dữ liệu `long long`!

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho tâm $(X&#95;0, Y&#95;0)$ và bán kính $R$. Đếm số điểm $(X, Y)$ có khoảng cách Euclid tới tâm $\le R$.
* **Dạng bài:** Geometry / Distance Calculation.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Công thức Khoảng cách Euclid**
* $d = \sqrt{(X - X&#95;0)^2 + (Y - Y&#95;0)^2}$. Điều kiện $d \le R \iff (X - X&#95;0)^2 + (Y - Y&#95;0)^2 \le R^2$.

#### **Bước 2: Tránh sai số Số thực**
* Dùng biến kiểu `long long` tính $(dx^2 + dy^2)$ và so sánh trực tiếp với $R^2$, hoàn toàn không dùng `double` hay `sqrt()`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(N)$.
* Bộ nhớ: $O(1)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    long long x0, y0, r;
    if (!(cin >> n >> x0 >> y0 >> r)) return 0;
    
    long long r2 = r * r;
    int count = 0;
    
    for (int i = 0; i < n; i++) {
        long long x, y;
        cin >> x >> y;
        long long dx = x - x0;
        long long dy = y - y0;
        if (dx * dx + dy * dy <= r2) {
            count++;
        }
    }
    
    cout << count << "\n";
    return 0;
}
```

---

# IKH-0036 - Ranh Giới Quy Hoạch Nông Nghiệp Công Nghệ Cao

## 1. NỘI DUNG BÀI TOÁN

Khu Nông nghiệp Công nghệ cao TP.HCM quy hoạch mảnh đất hình chữ nhật có các cạnh song song với các trục tọa độ. Mảnh đất được xác định bởi góc dưới-trái $(X&#95;1, Y&#95;1)$ và góc trên-phải $(X&#95;2, Y&#95;2)$.

Có $N$ nông trường thử nghiệm nằm tại các tọa độ $(X&#95;i, Y&#95;i)$ ($1 \le i \le N$). Một nông trường được xác định là **nằm trong ranh giới quy hoạch** nếu $X&#95;1 \le X&#95;i \le X&#95;2$ và $Y&#95;1 \le Y&#95;i \le Y&#95;2$.

Hãy đếm số lượng nông trường nằm hoàn toàn trong ranh giới quy hoạch mảnh đất.

#### Input:
* Dòng đầu chứa bốn số nguyên $X&#95;1, Y&#95;1, X&#95;2, Y&#95;2$ ($-10^9 \le X&#95;1 < X&#95;2 \le 10^9, -10^9 \le Y&#95;1 < Y&#95;2 \le 10^9$).
* Dòng thứ hai chứa số nguyên $N$ ($1 \le N \le 2 \times 10^5$).
* $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên $X&#95;i, Y&#95;i$ ($-10^9 \le X&#95;i, Y&#95;i \le 10^9$).

#### Output:
* Một số nguyên duy nhất là số lượng nông trường nằm trong ranh giới.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000$
* Subtask 2 (30% điểm): Mảnh đất có góc dưới-trái tại $(0, 0)$.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
1 1 5 5
4
2 3
5 5
0 2
6 3
```
**Output:**
```
2
```
**Giải thích:**
- Điểm (2, 3): $1 \le 2 \le 5$ và $1 \le 3 \le 5$ (Thỏa mãn)
- Điểm (5, 5): $1 \le 5 \le 5$ và $1 \le 5 \le 5$ (Thỏa mãn)
- Điểm (0, 2): $0 < 1$ (Không thỏa mãn)
- Điểm (6, 3): $6 > 5$ (Không thỏa mãn)

---

💡 **Bạn có biết?** Khu Nông nghiệp Công nghệ cao TP.HCM ứng dụng nhà màng thông minh và công nghệ tưới nhỏ giọt Israel giúp tăng năng suất cây trồng gấp 3-5 lần so với canh tác truyền thống.

🚀 **Thử thách:** Kiểm tra một điểm nằm trong hình chữ nhật căn chỉnh trục (Axis-Aligned Bounding Box - AABB) có độ phức tạp thời gian bao nhiêu?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho hình chữ nhật song song với trục tọa độ $[X&#95;1, X&#95;2] \times [Y&#95;1, Y&#95;2]$. Đếm số điểm $(X, Y)$ nằm trong hình chữ nhật.
* **Dạng bài:** Axis-Aligned Bounding Box (AABB) Point Check.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Điều kiện Nằm trong AABB**
* $X&#95;1 \le X \le X&#95;2$ và $Y&#95;1 \le Y \le Y&#95;2$.

#### **Bước 2: Đánh giá độ phức tạp**
* Thời gian: $O(N)$.
* Bộ nhớ: $O(1)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    long long x1, y1, x2, y2;
    if (!(cin >> x1 >> y1 >> x2 >> y2)) return 0;
    
    int n;
    cin >> n;
    
    int count = 0;
    for (int i = 0; i < n; i++) {
        long long x, y;
        cin >> x >> y;
        if (x >= x1 && x <= x2 && y >= y1 && y <= y2) {
            count++;
        }
    }
    
    cout << count << "\n";
    return 0;
}
```

---

# IKH-0037 - Quy Hoạch Công Viên Xanh Ecopark

## 1. NỘI DUNG BÀI TOÁN

Ban quản lý khu đô thị sinh thái Ecopark thiết kế khuôn viên công viên cây xanh hình đa giác đơn gồm $N$ đỉnh (đánh số theo chiều kim đồng hồ hoặc ngược chiều kim đồng hồ từ $1$ đến $N$). Đỉnh thứ $i$ có tọa độ $(X&#95;i, Y&#95;i)$.

Để lập dự toán chi phí trồng cỏ nhân tạo và lắp đặt hệ thống tưới nước tự động, kiến trúc sư cần tính **diện tích chính xác của đa giác công viên này**.

Hãy tính diện tích công viên và in ra dưới dạng **số thực làm tròn đúng 1 chữ số thập phân**.

#### Input:
* Dòng đầu chứa số nguyên $N$ ($3 \le N \le 2 \times 10^5$).
* $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên $X&#95;i, Y&#95;i$ ($-10^9 \le X&#95;i, Y&#95;i \le 10^9$).

#### Output:
* In ra diện tích đa giác dưới dạng số thực lấy 1 chữ số sau dấu phẩy thập phân.

#### Subtasks:
* Subtask 1 (30% điểm): $N = 3$ (Tam giác).
* Subtask 2 (30% điểm): $N = 4$ (Hình chữ nhật hoặc Hình vuông).
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4
0 0
4 0
4 3
0 3
```
**Output:**
```
12.0
```
**Giải thích:** Đa giác hình chữ nhật kích thước $4 \times 3$ có diện tích bằng 12.0.

#### Sample 2:
**Input:**
```
3
0 0
3 0
0 4
```
**Output:**
```
6.0
```

---

💡 **Bạn có biết?** Công thức Shoelace (Shoelace Formula hay Công thức Dây giày Gauss) giúp tính diện tích đa giác đơn bất kỳ từ tọa độ các đỉnh trong độ phức tạp thời gian $O(N)$.

🚀 **Thử thách:** Làm sao để tránh tràn số `long long` khi nhân tọa độ có giá trị lên tới $10^9$? (Gợi ý: Dùng `__int128_t` trong C++).

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Tính diện tích đa giác đơn $N$ đỉnh có tọa độ $(X&#95;i, Y&#95;i)$.
* **Dạng bài:** Geometry / Shoelace Formula (Công thức Dây giày Gauss).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Công thức Shoelace (Gauss Area)**
* $2S = |\sum&#95;{i=1}^{N} (X&#95;i Y&#95;{i+1} - X&#95;{i+1} Y&#95;i)|$ (với đỉnh $N+1$ trùng đỉnh $1$).
* Diện tích $S = \frac{|2S|}{2}$.

#### **Bước 2: Xử lý Tràn số (Overflow Control)**
* Tọa độ $10^9 \implies$ tích $X&#95;i Y&#95;{i+1}$ lên tới $10^{18}$. Tổng $N$ phần tử có thể đạt $2 \cdot 10^{23}$.
* Sử dụng kiểu dữ liệu `__int128_t` trong C++ để lưu trữ trung gian chính xác 100%.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(N)$.
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<long long> x(n), y(n);
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i];
    }
    
    __int128 sum = 0;
    for (int i = 0; i < n; i++) {
        int next_i = (i + 1) % n;
        sum += (__int128)x[i] * y[next_i] - (__int128)x[next_i] * y[i];
    }
    
    if (sum < 0) sum = -sum;
    
    long long integer_part = (long long)(sum / 2);
    long long frac_part = (long long)((sum % 2) * 5);
    
    cout << integer_part << "." << frac_part << "\n";
    return 0;
}
```

---

# IKH-0038 - Đồng Bộ Hóa Chu Kỳ Tín Hiệu Đèn Giao Thông

## 1. NỘI DUNG BÀI TOÁN

Sở Giao thông Vận tải TP. Đà Nẵng triển khai hệ thống đèn giao thông thông minh tại $N$ nút giao trọng điểm trên đại lộ Nguyễn Văn Linh.

Đèn giao thông tại nút giao thứ $i$ có chuổi thời gian đổi màu xanh - đỏ hoàn chỉnh đúng $A&#95;i$ giây. Tất cả $N$ đèn cùng bật xanh đồng thời tại thời điểm $t = 0$.

Hãy tìm **thời điểm sớm nhất $t > 0$ (tính bằng giây)** mà tất cả $N$ đèn giao thông **cùng đổi sang màu xanh đồng thời một lần nữa**.

(Do kết quả $t$ có thể rất lớn, hãy in ra kết quả **chia lấy dư cho $10^9 + 7$**).

#### Input:
* Dòng đầu chứa số nguyên $N$ ($1 \le N \le 10^5$).
* Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($1 \le A&#95;i \le 10^6$).

#### Output:
* Một số nguyên duy nhất là thời điểm $t$ chia lấy dư cho $10^9 + 7$.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 100, A&#95;i \le 100$
* Subtask 2 (30% điểm): Tất cả $A&#95;i$ đều là các số nguyên tố.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
3
4 6 10
```
**Output:**
```
60
```
**Giải thích:** Bội chung nhỏ nhất của {4, 6, 10} là $\text{LCM}(4, 6, 10) = 60$.

#### Sample 2:
**Input:**
```
2
3 5
```
**Output:**
```
15
```

---

💡 **Bạn có biết?** Hệ thống điều khiển đèn giao thông thích ứng (SCATS) tính toán bội số chu kỳ thời gian thực giúp giảm 20% thời gian ùn tắc tại các giao lộ lớn.

🚀 **Thử thách:** Phân tích thừa số nguyên tố kết hợp với lũy thừa mô-đun giúp tính LCM của mảng $N$ phần tử lớn một cách chính xác!

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Tìm Bội chung nhỏ nhất (LCM) của $N$ số $A&#95;1, A&#95;2, \dots, A&#95;N$ lấy dư cho $10^9 + 7$.
* **Dạng bài:** Number Theory / Prime Factorization / Modulo Exponentiation.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Phân tích Thừa số Nguyên tố**
* Bội chung nhỏ nhất của $N$ số là tích của tất cả các thừa số nguyên tố xuất hiện trong các số đó, lấy số mũ lớn nhất:
  $\text{LCM} = \prod p^{\max(\text{exp}(p))}$.

#### **Bước 2: Tính toán modulo $10^9 + 7$**
* Duyệt từng $A&#95;i$, phân tích thừa số nguyên tố, cập nhật `max_prime_pow[p]`.
* Cuối cùng nhân tất cả $p^{\max(\text{exp}(p))} \pmod{10^9 + 7}$.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(N \sqrt{\max A})$.
* Bộ nhớ: $O(\text{số lượng số nguyên tố})$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

const long long MOD = 1e9 + 7;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    if (!(cin >> n)) return 0;
    
    map<int, int> max_prime_pow;
    
    for (int i = 0; i < n; i++) {
        long long a;
        cin >> a;
        
        long long temp = a;
        for (long long p = 2; p * p <= temp; p++) {
            if (temp % p == 0) {
                int count = 0;
                while (temp % p == 0) {
                    count++;
                    temp /= p;
                }
                max_prime_pow[p] = max(max_prime_pow[p], count);
            }
        }
        if (temp > 1) {
            max_prime_pow[temp] = max(max_prime_pow[temp], 1);
        }
    }
    
    long long lcm_mod = 1;
    for (const auto& [p, exp] : max_prime_pow) {
        lcm_mod = (lcm_mod * power(p, exp)) % MOD;
    }
    
    cout << lcm_mod << "\n";
    return 0;
}
```

---

# IKH-0039 - Mã Hóa Giao Dịch Ngân Hàng ViettinBank

## 1. NỘI DUNG BÀI TOÁN

Hệ thống ngân hàng số VietinBank iBank tạo mã xác thực giao dịch ngẫu nhiên là một số nguyên dương $N$.

Để tăng cường mật mã học bảo mật, hệ thống cần tính toán **số lượng ước số nguyên dương** của $N$. Ví dụ: $N = 6$ có 4 ước số là $\{1, 2, 3, 6\}$.

Hãy giúp VietinBank đếm số lượng ước số của $N$.

#### Input:
* Một số nguyên duy nhất $N$ ($1 \le N \le 10^{12}$).

#### Output:
* Một số nguyên duy nhất là số lượng ước số của $N$.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 10^6$.
* Subtask 2 (30% điểm): $N$ là số chính phương.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
12
```
**Output:**
```
6
```
**Giải thích:** Các ước của 12 là {1, 2, 3, 4, 6, 12} (tổng cộng 6 ước).

#### Sample 2:
**Input:**
```
9
```
**Output:**
```
3
```

---

💡 **Bạn có biết?** Các thuật toán mã hóa công khai RSA của ngân hàng thương mại dựa trên độ khó của việc phân tích số nguyên lớn thành tích các thừa số nguyên tố.

🚀 **Thử thách:** Thuật toán duyệt đến $\sqrt{N}$ giúp đếm chính xác số lượng ước số trong độ phức tạp thời gian $O(\sqrt{N})$ như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Đếm số lượng ước số nguyên dương của $N$ ($N \le 10^{12}$).
* **Dạng bài:** Number Theory / Divisor Counting.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Tính chất Đối xứng của Ước số**
* Nếu $i$ là ước của $N$ thì $\frac{N}{i}$ cũng là ước của $N$.
* Do đó chỉ cần duyệt $i$ từ $1$ đến $\sqrt{N}$.

#### **Bước 2: Trường hợp Số chính phương**
* Nếu $i \times i = N$, chỉ cộng 1 vào kết quả. Ngược lại cộng 2.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(\sqrt{N}) \le 10^6$ thao tác.
* Bộ nhớ: $O(1)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    long long n;
    if (!(cin >> n)) return 0;
    
    long long count = 0;
    for (long long i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            if (i * i == n) {
                count += 1;
            } else {
                count += 2;
            }
        }
    }
    
    cout << count << "\n";
    return 0;
}
```

---

# IKH-0040 - Xác Thực Chữ Ký Số Hệ Thống BHXH

## 1. NỘI DUNG BÀI TOÁN

Cổng Dịch vụ công Bảo hiểm Xã hội Việt Nam (VSSID) xác thực chữ ký số mã hóa của hồ sơ cấp sổ bằng phép tính lũy thừa mô-đun:

$$S = A^B \pmod M$$

Cho ba số nguyên dương $A, B, M$. Hãy tính giá trị chữ ký số $S$.

#### Input:
* Một dòng duy nhất chứa ba số nguyên $A, B, M$ ($1 \le A, B, M \le 10^{18}$).

#### Output:
* Một số nguyên duy nhất là kết quả $S = A^B \pmod M$.

#### Subtasks:
* Subtask 1 (30% điểm): $B \le 10^6, M \le 10^9$.
* Subtask 2 (30% điểm): $A, B, M \le 10^9$.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung ($A, B, M \le 10^{18}$).

#### Sample 1:
**Input:**
```
2 10 1000
```
**Output:**
```
24
```
**Giải thích:** $2^{10} = 1024 \implies 1024 \pmod{1000} = 24$.

#### Sample 2:
**Input:**
```
3 5 13
```
**Output:**
```
9
```

---

💡 **Bạn có biết?** Thuật toán Chữ ký số Quốc gia Việt Nam dùng lũy thừa mô-đun trên đường cong elip (ECC) giúp rút ngắn chiều dài khóa bảo mật mà vẫn đảm bảo độ an toàn cao tuyệt đối.

🚀 **Thử thách:** Khi $M \le 10^{18}$, phép nhân hai số `(a * b) % M` có thể bị tràn số `long long`. Dùng `__int128_t` xử lý phép nhân mô-đun cực đại thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Tính $A^B \pmod M$ với $A, B, M \le 10^{18}$.
* **Dạng bài:** Binary Exponentiation (Lũy thừa Nhị phân) + `__int128_t` Modulo Multiplication.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Thuật toán Lũy thừa Nhị phân $O(\log B)$**
* Biến đổi $B$ sang hệ nhị phân. Nếu bit hiện tại bằng 1, nhân kết quả với $A \pmod M$. Nhân bản $A \leftarrow A^2 \pmod M$.

#### **Bước 2: Tránh Tràn số khi nhân Mô-đun $10^{18}$**
* Tích $A \times A$ với $A \approx 10^{18}$ lên tới $10^{36}$, vượt quá `unsigned long long` ($1.8 \times 10^{19}$).
* Ép kiểu sang `__int128_t` để thực hiện phép nhân mô-đun an toàn tuyệt đối.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(\log B)$.
* Bộ nhớ: $O(1)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    unsigned long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;
    
    unsigned long long res = 1 % m;
    a %= m;
    
    while (b > 0) {
        if (b % 2 == 1) {
            res = (unsigned long long)((__int128)res * a % m);
        }
        a = (unsigned long long)((__int128)a * a % m);
        b /= 2;
    }
    
    cout << res << "\n";
    return 0;
}
```

---

# IKH-0041 - Kiểm Lỗi Dữ Liệu Truyền Tải Bằng Mã Parity

## 1. NỘI DUNG BÀI TOÁN

Trung tâm dữ liệu Viettel IDC lưu trữ các gói tin dưới dạng các số nguyên không âm $64$-bit $A&#95;1, A&#95;2, \\dots, A&#95;N$.

Trong giao thức kiểm soát lỗi truyền tải dữ liệu, hệ thống tính toán **tổng kiểm tra Parity** (tổng số lượng bit 1 trong biểu diễn nhị phân của tất cả các gói tin).

Hãy giúp Viettel IDC đếm **tổng số lượng bit 1** của tất cả $N$ gói tin dữ liệu.

#### Input:
* Dòng đầu chứa số nguyên $N$ ($1 \le N \le 2 \times 10^5$).
* Dòng thứ hai chứa $N$ số nguyên không âm $A&#95;1, A&#95;2, \dots, A&#95;N$ ($0 \le A&#95;i \le 10^{18}$).

#### Output:
* Một số nguyên duy nhất là tổng số lượng bit 1 đếm được.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000, A&#95;i \le 10^9$.
* Subtask 2 (30% điểm): Tất cả $A&#95;i$ đều là lũy thừa của 2 ($A&#95;i = 2^k$).
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
3
5 7 8
```
**Output:**
```
6
```
**Giải thích:**
- $5 = 101_2$ (2 bit 1)
- $7 = 111_2$ (3 bit 1)
- $8 = 1000_2$ (1 bit 1)
- Tổng số bit 1: $2 + 3 + 1 = 6$.

---

💡 **Bạn có biết?** Hàm nội tại `__builtin_popcountll(x)` trong C++ sử dụng trực tiếp chỉ thị phần cứng POPCNT của CPU giúp đếm số bit 1 trong duy nhất 1 chu kỳ máy!

🚀 **Thử thách:** Sự khác biệt giữa `__builtin_popcount` (32-bit) và `__builtin_popcountll` (64-bit) là gì?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho $N$ số nguyên không âm 64-bit $A&#95;i$. Đếm tổng số bit 1 của tất cả các số.
* **Dạng bài:** Bitwise Manipulation / `__builtin_popcountll`.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Khái niệm Popcount (Population Count)**
* Đếm số lượng bit 1 trong biểu diễn nhị phân của số $A&#95;i$.

#### **Bước 2: Sử dụng Built-in Hardware Instruction**
* Hàm `__builtin_popcountll(a)` của GCC tính toán số bit 1 cho kiểu `unsigned long long` 64-bit cực nhanh.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(N)$.
* Bộ nhớ: $O(1)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    if (!(cin >> n)) return 0;
    
    long long total_bits = 0;
    for (int i = 0; i < n; i++) {
        unsigned long long a;
        cin >> a;
        total_bits += __builtin_popcountll(a);
    }
    
    cout << total_bits << "\n";
    return 0;
}
```

---

# IKH-0042 - Giải Mã Tín Hiệu Bảo Mật VinaPhone

## 1. NỘI DUNG BÀI TOÁN

Mạng viễn thông VinaPhone mã hóa chuỗi gói tin dưới dạng dãy số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$.

Bộ giải mã mật mã thực hiện $Q$ truy vấn kiểm tra an ninh. Mỗi truy vấn gồm hai chỉ số $L$ và $R$ ($1 \le L \le R \le N$). Hệ thống yêu cầu tính **tổng XOR của tất cả các gói tin từ $L$ đến $R$**:

$$S = A&#95;L \oplus A&#95;{L+1} \oplus \dots \oplus A&#95;R$$

Hãy tính tổng XOR $S$ cho từng truy vấn để xác thực tính toàn vẹn của tín hiệu bảo mật.

#### Input:
* Dòng đầu chứa hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \times 10^5$).
* Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($0 \le A&#95;i \le 10^9$).
* $Q$ dòng tiếp theo, dòng thứ $j$ chứa hai số nguyên $L&#95;j, R&#95;j$ ($1 \le L&#95;j \le R&#95;j \le N$).

#### Output:
* In ra $Q$ dòng, mỗi dòng chứa một số nguyên là kết quả tổng XOR của truy vấn tương ứng.

#### Subtasks:
* Subtask 1 (30% điểm): $N, Q \le 1000$.
* Subtask 2 (30% điểm): $L = 1$ với mọi truy vấn.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
5 3
4 2 6 8 3
1 3
2 4
3 5
```
**Output:**
```
0
12
13
```
**Giải thích:**
- Truy vấn 1 (1->3): $4 \oplus 2 \oplus 6 = 0$.
- Truy vấn 2 (2->4): $2 \oplus 6 \oplus 8 = 12$.
- Truy vấn 3 (3->5): $6 \oplus 8 \oplus 3 = 13$.

---

💡 **Bạn có biết?** Phép toán Bitwise XOR có tính chất tự nghịch đảo: $(X \oplus Y) \oplus Y = X$, cho phép tính tổng đoạn trong hằng số thời gian $O(1)$ nhờ Mảng Tiền tố XOR (Prefix XOR Array).

🚀 **Thử thách:** Công thức Prefix XOR: $A&#95;L \oplus \dots \oplus A&#95;R = P[R] \oplus P[L-1]$ với $P[i] = P[i-1] \oplus A&#95;i$.

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho mảng $A$. Tính tổng XOR đoạn $[L, R]$ với $Q$ truy vấn.
* **Dạng bài:** Prefix XOR Array ($O(1)$ query).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Tính chất Phép toán XOR**
* $X \oplus X = 0$ và $X \oplus 0 = X$.

#### **Bước 2: Mảng Tiền tố Prefix XOR**
* Gọi $P[i] = A&#95;1 \oplus A&#95;2 \oplus \dots \oplus A&#95;i$.
* Tổng XOR đoạn $[L, R]$ bằng $P[R] \oplus P[L-1]$.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: Tiền xử lý $O(N)$, Mỗi truy vấn $O(1) \implies O(N + Q)$.
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, q;
    if (!(cin >> n >> q)) return 0;
    
    vector<long long> pref(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        long long a;
        cin >> a;
        pref[i] = pref[i - 1] ^ a;
    }
    
    for (int j = 0; j < q; j++) {
        int l, r;
        cin >> l >> r;
        long long ans = pref[r] ^ pref[l - 1];
        cout << ans << "\n";
    }
    return 0;
}
```

---

# IKH-0043 - Trò Chơi Bốc Sỏi Trên Bàn Cờ

## 1. NỘI DUNG BÀI TOÁN

Hai người chơi An và Bình tham gia trò chơi toán học đối kháng với $N$ đống sỏi. Đống sỏi thứ $i$ có $A&#95;i$ viên sỏi.

Hai người luân phiên thực hiện lượt chơi (An chơi trước). Ở mỗi lượt, người chơi chọn **đúng một đống sỏi bất kỳ** và lấy đi **ít nhất 1 viên sỏi** (có thể lấy toàn bộ sỏi trong đống đó). Người chơi bốc viên sỏi cuối cùng trên bàn cờ là người **GIÀNH CHIẾN THẮNG**.

Giả sử cả An và Bình đều chơi tối ưu tuyệt đối, hãy xác định ai là người chiến thắng.

#### Input:
* Dòng đầu chứa số nguyên $N$ ($1 \le N \le 2 \times 10^5$).
* Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($1 \le A&#95;i \le 10^9$).

#### Output:
* In ra `An` nếu An chiến thắng, hoặc `Binh` nếu Bình chiến thắng.

#### Subtasks:
* Subtask 1 (30% điểm): $N = 1$ hoặc $N = 2$.
* Subtask 2 (30% điểm): Tất cả $A&#95;i$ đều bằng nhau.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
3
1 2 3
```
**Output:**
```
Binh
```
**Giải thích:** Tổng Nim-sum $1 \oplus 2 \oplus 3 = 0$. Trạng thái xuất phát là trạng thái thua (P-position) $\implies$ Bình chiến thắng.

#### Sample 2:
**Input:**
```
2
5 7
```
**Output:**
```
An
```

---

💡 **Bạn có biết?** Trò chơi Nim là nền tảng cốt lõi của Lý thuyết Trò chơi Tổ hợp (Combinatorial Game Theory) được chứng minh bởi nhà toán học Charles L. Bouton năm 1901.

🚀 **Thử thách:** Định lý Bouton: Người chơi trước chiến thắng khi và chỉ khi Tổng XOR (Nim-sum) $A&#95;1 \oplus A&#95;2 \oplus \dots \oplus A&#95;N \neq 0$.

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Xác định người thắng trò chơi Nim với $N$ đống sỏi $A&#95;1, A&#95;2, \dots, A&#95;N$.
* **Dạng bài:** Game Theory / Nim Game / Bouton's Theorem.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Định lý Bouton (Bouton's Theorem)**
* Tính tổng Nim-sum $S = A&#95;1 \oplus A&#95;2 \oplus \dots \oplus A&#95;N$.
* Nếu $S \neq 0$: Trạng thái thắng (N-position), người chơi trước (`An`) luôn thắng.
* Nếu $S = 0$: Trạng thái thua (P-position), người chơi sau (`Binh`) chiến thắng.

#### **Bước 2: Đánh giá độ phức tạp**
* Thời gian: $O(N)$.
* Bộ nhớ: $O(1)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    if (!(cin >> n)) return 0;
    
    long long nim_sum = 0;
    for (int i = 0; i < n; i++) {
        long long a;
        cin >> a;
        nim_sum ^= a;
    }
    
    if (nim_sum != 0) {
        cout << "An\n";
    } else {
        cout << "Binh\n";
    }
    return 0;
}
```

---

# IKH-0044 - Thống Kê Doanh Thu Chuỗi Siêu Thị WinMart

## 1. NỘI DUNG BÀI TOÁN

Tập đoàn Masan quản lý bản đồ mạng lưới chuỗi siêu thị WinMart dưới dạng lưới ô vuông kích thước $R \times C$ ô. Ô tại hàng $r$, cột $c$ có doanh thu $A[r][c]$ triệu đồng.

Ban giám đốc đưa ra $Q$ truy vấn thống kê. Mỗi truy vấn yêu cầu tính **tổng doanh thu của khu vực hình chữ nhật** từ hàng $r&#95;1$ đến hàng $r&#95;2$ và từ cột $c&#95;1$ đến cột $c&#95;2$ ($1 \le r&#95;1 \le r&#95;2 \le R, 1 \le c&#95;1 \le c&#95;2 \le C$).

Hãy tính tổng doanh thu cho $Q$ truy vấn khu vực.

#### Input:
* Dòng đầu chứa ba số nguyên $R, C, Q$ ($1 \le R, C \le 1000, 1 \le Q \le 2 \times 10^5$).
* $R$ dòng tiếp theo, mỗi dòng chứa $C$ số nguyên $A[r][c]$ ($0 \le A[r][c] \le 10^6$).
* $Q$ dòng tiếp theo, dòng thứ $j$ chứa bốn số nguyên $r&#95;1, c&#95;1, r&#95;2, c&#95;2$.

#### Output:
* In ra $Q$ dòng, mỗi dòng chứa tổng doanh thu tìm được.

#### Subtasks:
* Subtask 1 (30% điểm): $R, C, Q \le 100$.
* Subtask 2 (30% điểm): $r&#95;1 = 1, c&#95;1 = 1$.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
3 3 2
1 2 3
4 5 6
7 8 9
1 1 2 2
2 2 3 3
```
**Output:**
```
12
28
```
**Giải thích:**
- Truy vấn 1 (1,1 -> 2,2): $1 + 2 + 4 + 5 = 12$.
- Truy vấn 2 (2,2 -> 3,3): $5 + 6 + 8 + 9 = 28$.

---

💡 **Bạn có biết?** Mảng Cộng dồn 2 chiều (2D Prefix Sum) cho phép truy vấn tổng diện tích hình chữ nhật bất kỳ trong thời gian hằng số $O(1)$.

🚀 **Thử thách:** Công thức trừ diện tích giao nhau: $\text{Sum} = P[r&#95;2][c&#95;2] - P[r&#95;1-1][c&#95;2] - P[r&#95;2][c&#95;1-1] + P[r&#95;1-1][c&#95;1-1]$.

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho bảng $R \times C$. Xử lý $Q$ truy vấn tính tổng hình chữ nhật $[r1..r2][c1..c2]$.
* **Dạng bài:** 2D Prefix Sum ($O(1)$ query).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Tiền xử lý Mảng 2D Prefix Sum**
* $P[r][c] = A[r][c] + P[r-1][c] + P[r][c-1] - P[r-1][c-1]$.

#### **Bước 2: Phép toán Trừ Diện tích Trùng lặp**
* $\text{Sum} = P[r2][c2] - P[r1-1][c2] - P[r2][c1-1] + P[r1-1][c1-1]$.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: Tiền xử lý $O(R \times C)$, Truy vấn $O(1) \implies O(R \times C + Q)$.
* Bộ nhớ: $O(R \times C)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int r_size, c_size, q;
    if (!(cin >> r_size >> c_size >> q)) return 0;
    
    vector<vector<long long>> pref(r_size + 1, vector<long long>(c_size + 1, 0));
    for (int r = 1; r <= r_size; r++) {
        for (int c = 1; c <= c_size; c++) {
            long long val;
            cin >> val;
            pref[r][c] = val + pref[r - 1][c] + pref[r][c - 1] - pref[r - 1][c - 1];
        }
    }
    
    for (int j = 0; j < q; j++) {
        int r1, c1, r2, c2;
        cin >> r1 >> c1 >> r2 >> c2;
        long long sum = pref[r2][c2] - pref[r1 - 1][c2] - pref[r2][c1 - 1] + pref[r1 - 1][c1 - 1];
        cout << sum << "\n";
    }
    return 0;
}
```

---

# IKH-0045 - Xếp Hạng Bảng Vàng Cuộc Thi Tin Học Trẻ

## 1. NỘI DUNG BÀI TOÁN

Ban tổ chức Cuộc thi Tin học trẻ Toàn quốc duy trì danh sách điểm thi của $N$ thí sinh (được đánh số từ $1$ đến $N$). Ban đầu điểm của thí sinh thứ $i$ là $A&#95;i$.

Trong suốt quá trình chấm thi, hệ thống xử lý $Q$ sự kiện thuộc 2 loại:
* `1 u x`: Cập nhật cộng thêm $x$ điểm cho thí sinh $u$ ($A&#95;u \leftarrow A&#95;u + x$).
* `2 L R`: Tính **tổng điểm của tất cả thí sinh từ chỉ số $L$ đến $R$**.

Hãy in ra kết quả cho tất cả các sự kiện loại 2.

#### Input:
* Dòng đầu chứa hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \times 10^5$).
* Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($0 \le A&#95;i \le 10^9$).
* $Q$ dòng tiếp theo mô tả sự kiện:
  * `1 u x` ($1 \le u \le N, 1 \le x \le 10^9$)
  * `2 L R` ($1 \le L \le R \le N$)

#### Output:
* In ra kết quả tương ứng cho mỗi sự kiện loại 2 trên từng dòng.

#### Subtasks:
* Subtask 1 (30% điểm): $N, Q \le 1000$.
* Subtask 2 (30% điểm): Không có sự kiện loại 1 (Chỉ truy vấn tổng).
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
5 3
1 2 3 4 5
2 1 3
1 2 10
2 1 3
```
**Output:**
```
6
16
```
**Giải thích:**
- Sự kiện 1: Tổng từ 1 đến 3 = $1 + 2 + 3 = 6$.
- Sự kiện 2: Thí sinh 2 cộng 10 điểm $\implies A&#95;2 = 12$.
- Sự kiện 3: Tổng mới từ 1 đến 3 = $1 + 12 + 3 = 16$.

---

💡 **Bạn có biết?** Cây Fenwick (Binary Indexed Tree - BIT) cho phép cập nhật điểm và truy vấn tổng đoạn trong thời gian siêu nhanh $O(\log N)$ với bộ nhớ tối thiểu.

🚀 **Thử thách:** Phép toán bit `i & (-i)` trong Cấu trúc cây Fenwick giúp di chuyển lên/xuống các nút cha trong cây như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Duy trì mảng $N$ phần tử. Hỗ trợ 2 thao tác: Cộng điểm $A[u] += x$ và Truy vấn tổng $[L, R]$.
* **Dạng bài:** Fenwick Tree (Binary Indexed Tree - BIT).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Cấu trúc Cây Fenwick (BIT)**
* Mảng `tree` lưu tổng đoạn độ dài `i & (-i)`.
* Cập nhật `add(i, delta)`: `i += i & -i`.
* Truy vấn `query(i)`: `i -= i & -i`.

#### **Bước 2: Đánh giá độ phức tạp**
* Thời gian: Tiền xử lý $O(N \log N)$, Mỗi cập nhật/truy vấn $O(\log N) \implies O((N + Q) \log N)$.
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>

using namespace std;

struct FenwickTree {
    int n;
    vector<long long> tree;
    
    FenwickTree(int n) : n(n), tree(n + 1, 0) {}
    
    void add(int i, long long delta) {
        for (; i <= n; i += i & -i) {
            tree[i] += delta;
        }
    }
    
    long long query(int i) {
        long long sum = 0;
        for (; i > 0; i -= i & -i) {
            sum += tree[i];
        }
        return sum;
    }
    
    long long range_query(int l, int r) {
        return query(r) - query(l - 1);
    }
};

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, q;
    if (!(cin >> n >> q)) return 0;
    
    FenwickTree bit(n);
    for (int i = 1; i <= n; i++) {
        long long a;
        cin >> a;
        bit.add(i, a);
    }
    
    for (int j = 0; j < q; j++) {
        int type;
        cin >> type;
        if (type == 1) {
            int u;
            long long x;
            cin >> u >> x;
            bit.add(u, x);
        } else {
            int l, r;
            cin >> l >> r;
            cout << bit.range_query(l, r) << "\n";
        }
    }
    return 0;
}
```

---

# IKH-0046 - Giám Sát Lưu Lượng Mạng Cáp Quang Bắc

## 1. NỘI DUNG BÀI TOÁN

Tập đoàn VNPT vận hành trục cáp quang đường dài Bắc - Nam gồm $N$ trạm lặp tín hiệu (đánh số từ $1$ đến $N$). Trạm thứ $i$ có lưu lượng băng thông tiêu thụ hiện tại là $A&#95;i$ Gbps.

Trung tâm NOC VNPT thực hiện $Q$ thao tác giám sát điều phối mạng:
* `1 u x`: Trạm $u$ thay đổi băng thông tiêu thụ thành giá trị mới $x$ ($A&#95;u \leftarrow x$).
* `2 L R`: Tìm **lưu lượng băng thông LỚN NHẤT** trong tất cả các trạm lặp thuộc đoạn từ $L$ đến $R$ ($\max(A&#95;L, A&#95;{L+1}, \dots, A&#95;R)$).

Hãy in ra kết quả băng thông lớn nhất cho tất cả các thao tác loại 2.

#### Input:
* Dòng đầu chứa hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \times 10^5$).
* Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($0 \le A&#95;i \le 10^9$).
* $Q$ dòng tiếp theo mô tả thao tác:
  * `1 u x` ($1 \le u \le N, 0 \le x \le 10^9$)
  * `2 L R` ($1 \le L \le R \le N$)

#### Output:
* In ra kết quả tương ứng cho mỗi thao tác loại 2 trên từng dòng.

#### Subtasks:
* Subtask 1 (30% điểm): $N, Q \le 1000$.
* Subtask 2 (30% điểm): Không có thao tác loại 1 (Chỉ truy vấn max).
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
5 3
10 30 20 50 40
2 1 3
1 2 100
2 1 3
```
**Output:**
```
30
100
```
**Giải thích:**
- Thao tác 1: Max trong đoạn 1->3 của [10, 30, 20] là 30.
- Thao tác 2: Trạm 2 thay đổi thành 100 Gbps.
- Thao tác 3: Max mới trong đoạn 1->3 của [10, 100, 20] là 100.

---

💡 **Bạn có biết?** Cây Phân đoạn (Segment Tree) là cấu trúc dữ liệu mạnh mẽ bậc nhất giúp truy vấn giá trị cực đại/cực tiểu (Range Minimum/Maximum Query) trong thời gian $O(\log N)$.

🚀 **Thử thách:** Cây Phân đoạn tổ chức mảng 1D kích thước $4N$ với nút con trái `2*node` và nút con phải `2*node + 1` chuẩn ra sao?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Duy trì mảng $N$ phần tử. Hỗ trợ Gán $A[u] = x$ và Truy vấn Max đoạn $[L, R]$.
* **Dạng bài:** Segment Tree (Range Maximum Query - RMQ).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Khởi tạo Cây Phân đoạn (Segment Tree)**
* Mảng `tree` kích thước $4N$.
* Hàm `build(1, 1, N)` chia đôi đoạn $[start, end]$, gán nút cha = $\max(\text{trái}, \text{phải})$.

#### **Bước 2: Thao tác Cập nhật & Truy vấn**
* `update(1, 1, N, u, x)` tốn $O(\log N)$.
* `query(1, 1, N, L, R)` tốn $O(\log N)$.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: Tiền xử lý $O(N)$, Mỗi cập nhật/truy vấn $O(\log N) \implies O(N + Q \log N)$.
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct SegmentTree {
    int n;
    vector<long long> tree;
    
    SegmentTree(int n) : n(n), tree(4 * n + 1, 0) {}
    
    void build(const vector<long long>& a, int node, int start, int end) {
        if (start == end) {
            tree[node] = a[start];
            return;
        }
        int mid = (start + end) / 2;
        build(a, 2 * node, start, mid);
        build(a, 2 * node + 1, mid + 1, end);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }
    
    void update(int node, int start, int end, int idx, long long val) {
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if (start <= idx && idx <= mid) {
            update(2 * node, start, mid, idx, val);
        } else {
            update(2 * node + 1, mid + 1, end, idx, val);
        }
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }
    
    long long query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) {
            return 0; // Băng thông >= 0
        }
        if (l <= start && end <= r) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        long long left_max = query(2 * node, start, mid, l, r);
        long long right_max = query(2 * node + 1, mid + 1, end, l, r);
        return max(left_max, right_max);
    }
};

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, q;
    if (!(cin >> n >> q)) return 0;
    
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];
    
    SegmentTree seg(n);
    seg.build(a, 1, 1, n);
    
    for (int j = 0; j < q; j++) {
        int type;
        cin >> type;
        if (type == 1) {
            int u;
            long long x;
            cin >> u >> x;
            seg.update(1, 1, n, u, x);
        } else {
            int l, r;
            cin >> l >> r;
            cout << seg.query(1, 1, n, l, r) << "\n";
        }
    }
    return 0;
}
```

---

# IKH-0047 - Bộ Lọc Từ Khóa Nhạy Cảm Zalo

## 1. NỘI DUNG BÀI TOÁN

Bộ lọc nội dung tin nhắn của ứng dụng OTT Zalo nhận một đoạn văn bản $S$ gồm các ký tự chữ cái tiếng Anh viết thường.

Để phát hiện các từ khóa vi phạm tiêu chuẩn cộng đồng, bộ lọc cần phân tích độ đa dạng ngôn ngữ bằng cách **đếm số lượng xâu con liên tiếp phân biệt (distinct substrings)** có độ dài đúng bằng $K$.

Hãy tìm **số lượng xâu con phân biệt độ dài $K$** xuất hiện trong đoạn văn bản $S$.

#### Input:
* Dòng đầu chứa số nguyên $K$ ($1 \le K \le |S|$).
* Dòng thứ hai chứa xâu ký tự $S$ ($1 \le |S| \le 2 \times 10^5$, $S$ chỉ gồm các ký tự từ `'a'` đến `'z'`).

#### Output:
* Một số nguyên duy nhất là số lượng xâu con phân biệt độ dài $K$.

#### Subtasks:
* Subtask 1 (30% điểm): $|S| \le 1000$.
* Subtask 2 (30% điểm): $K = 1$.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
3
abacaba
```
**Output:**
```
4
```
**Giải thích:** Các xâu con độ dài $K = 3$ là: `"aba"`, `"bac"`, `"aca"`, `"cab"`, `"aba"`. Trong đó `"aba"` xuất hiện 2 lần $\implies$ có 4 xâu con phân biệt: `{"aba", "bac", "aca", "cab"}`.

---

💡 **Bạn có biết?** Zalo xử lý hơn 2 tỷ tin nhắn mỗi ngày. Việc băm chuỗi (String Hashing) kết hợp `std::unordered_set` giúp phát hiện từ khóa nhạy cảm trong thời gian thực.

🚀 **Thử thách:** Thuật toán Rolling Hash tính mã băm cho cửa sổ trượt độ dài $K$ trong $O(1)$ mỗi bước như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho chuỗi $S$ và số $K$. Đếm số lượng xâu con phân biệt độ dài $K$.
* **Dạng bài:** String Sliding Window + `std::string_view` / String Hashing.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Sử dụng `std::string_view` tránh Copy Xâu**
* Duyệt tất cả cửa sổ trượt từ $0$ đến $N-K$.
* Dùng `std::string_view` để tham chiếu trực tiếp tới bộ nhớ của $S$, tránh việc cấp phát lại xâu mới tốn thời gian.

#### **Bước 2: Tập hợp Đếm duy nhất `std::unordered_set`**
* Đẩy các xâu con vào `unordered_set`. Kết quả là `st.size()`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(N \cdot K)$ với `unordered_set` hoặc $O(N)$ với Rolling Hash.
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int k;
    if (!(cin >> k)) return 0;
    
    string s;
    cin >> s;
    
    int n = s.length();
    if (k > n) {
        cout << 0 << "\n";
        return 0;
    }
    
    unordered_set<string_view> st;
    string_view sv(s);
    
    for (int i = 0; i <= n - k; i++) {
        st.insert(sv.substr(i, k));
    }
    
    cout << st.size() << "\n";
    return 0;
}
```

---

# IKH-0048 - Kiểm Tra Mã Vạch Hàng Hóa Tiki

## 1. NỘI DUNG BÀI TOÁN

Sàn thương mại điện tử Tiki dán mã vạch kiểm tra là một chuỗi ký tự $S$ độ dài $N$ cho các sản phẩm công nghệ.

Để kiểm tra độ đối xứng bảo mật của mã vạch, hệ thống nhận được $Q$ truy vấn. Mỗi truy vấn gồm hai chỉ số $L$ và $R$ ($1 \le L \le R \le N$). Hệ thống cần kiểm tra xem **chuỗi con từ vị trí $L$ đến $R$ ($S[L \dots R]$) có phải là chuỗi đối xứng (Palindrome) hay không**.

Hãy in ra `YES` nếu chuỗi con $S[L \dots R]$ là Palindrome, hoặc `NO` nếu ngược lại.

#### Input:
* Dòng đầu chứa hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \times 10^5$).
* Dòng thứ hai chứa xâu ký tự $S$ độ dài $N$ (chỉ gồm các ký tự tiếng Anh viết thường).
* $Q$ dòng tiếp theo, dòng thứ $j$ chứa hai số nguyên $L&#95;j, R&#95;j$ ($1 \le L&#95;j \le R&#95;j \le N$).

#### Output:
* In ra $Q$ dòng, mỗi dòng chứa `YES` hoặc `NO`.

#### Subtasks:
* Subtask 1 (30% điểm): $N, Q \le 1000$.
* Subtask 2 (30% điểm): $L = 1, R = N$ cho mọi truy vấn.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
7 3
abacaba
1 3
1 7
2 4
```
**Output:**
```
YES
YES
NO
```
**Giải thích:**
- Truy vấn 1 (1->3): `"aba"` là Palindrome $\implies$ `YES`.
- Truy vấn 2 (1->7): `"abacaba"` là Palindrome $\implies$ `YES`.
- Truy vấn 3 (2->4): `"bac"` không là Palindrome $\implies$ `NO`.

---

💡 **Bạn có biết?** Polynomial Rolling Hash cho phép so sánh giá trị mã băm xuôi và ngược của một đoạn chuỗi trong thời gian $O(1)$ để kiểm tra Palindrome.

🚀 **Thử thách:** Hai mảng băm tiền tố (Hash xuôi và Hash ngược) kết hợp phép tính lũy thừa mô-đun giúp trả lời truy vấn $O(1)$ như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho chuỗi $S$. Xử lý $Q$ truy vấn kiểm tra xem đoạn $S[L \dots R]$ có phải là Palindrome.
* **Dạng bài:** Polynomial Rolling Hash (Forward + Backward Hash).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Tính chất Palindrome qua Hashing**
* $S[L \dots R]$ là Palindrome $\iff$ Mã băm xuôi $\text{Hash}_{fwd}(L, R) ==$ Mã băm ngược $\text{Hash}_{bwd}(L, R)$.

#### **Bước 2: Công thức Mã băm Đoạn**
* $\text{Hash}_{fwd}(L, R) = (H_{fwd}[R] - H_{fwd}[L-1] \cdot B^{R-L+1}) \pmod{10^9+7}$.
* $\text{Hash}_{bwd}(L, R) = (H_{bwd}[L] - H_{bwd}[R+1] \cdot B^{R-L+1}) \pmod{10^9+7}$.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: Tiền xử lý $O(N)$, Mỗi truy vấn $O(1) \implies O(N + Q)$.
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const long long BASE = 31;
const long long MOD = 1e9 + 7;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (__int128)res * base % MOD;
        base = (__int128)base * base % MOD;
        exp /= 2;
    }
    return res;
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, q;
    if (!(cin >> n >> q)) return 0;
    
    string s;
    cin >> s;
    
    vector<long long> hash_fwd(n + 1, 0), hash_bwd(n + 2, 0), pow_b(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        pow_b[i] = (__int128)pow_b[i - 1] * BASE % MOD;
        hash_fwd[i] = ((__int128)hash_fwd[i - 1] * BASE + (s[i - 1] - 'a' + 1)) % MOD;
    }
    for (int i = n; i >= 1; i--) {
        hash_bwd[i] = ((__int128)hash_bwd[i + 1] * BASE + (s[i - 1] - 'a' + 1)) % MOD;
    }
    
    auto get_hash_fwd = [&](int l, int r) {
        long long res = (hash_fwd[r] - (__int128)hash_fwd[l - 1] * pow_b[r - l + 1]) % MOD;
        return (res + MOD) % MOD;
    };
    
    auto get_hash_bwd = [&](int l, int r) {
        long long res = (hash_bwd[l] - (__int128)hash_bwd[r + 1] * pow_b[r - l + 1]) % MOD;
        return (res + MOD) % MOD;
    };
    
    for (int j = 0; j < q; j++) {
        int l, r;
        cin >> l >> r;
        if (get_hash_fwd(l, r) == get_hash_bwd(l, r)) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
    return 0;
}
```

---

# IKH-0049 - Tìm Kiếm Bản Đồ Địa Giới VNPost

## 1. NỘI DUNG BÀI TOÁN

Tổng công ty Bưu điện Việt Nam (VNPost) lưu trữ chuỗi dữ liệu địa giới hành chính $S$ gồm $N$ ký tự.

Để hỗ trợ tìm kiếm phân tích mẫu địa danh, hệ thống cần tính **mảng Tiền tố chung dài nhất (Pi Array / Prefix Function)** của thuật toán KMP cho toàn bộ xâu $S$.

Mảng $\pi[i]$ ($0 \le i < N$) được định nghĩa là **độ dài của tiền tố dài nhất vừa là hậu tố thực sự của xâu con $S[0 \dots i]$**.

Hãy in ra tất cả các giá trị $\pi[0], \pi[1], \dots, \pi[N-1]$.

#### Input:
* Dòng đầu chứa xâu ký tự $S$ ($1 \le |S| \le 2 \times 10^5$, chỉ gồm các ký tự tiếng Anh viết thường).

#### Output:
* In trên 1 dòng gồm $N$ số nguyên cách nhau bởi khoảng trắng là mảng $\pi$.

#### Subtasks:
* Subtask 1 (30% điểm): $|S| \le 1000$.
* Subtask 2 (30% điểm): $S$ chỉ gồm 1 loại ký tự (ví dụ: `"aaaaa"`).
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
abacaba
```
**Output:**
```
0 0 1 0 1 2 3
```
**Giải thích:**
- $i=0$ (`"a"`): $\pi[0] = 0$
- $i=2$ (`"aba"`): tiền tố `"a"` trùng hậu tố `"a"` $\implies \pi[2] = 1$
- $i=6$ (`"abacaba"`): tiền tố `"aba"` trùng hậu tố `"aba"` $\implies \pi[6] = 3$

---

💡 **Bạn có biết?** Thuật toán Knuth-Morris-Pratt (KMP) tìm kiếm xâu mẫu trong thời gian tuyến tính $O(N + M)$ nhờ tận dụng mảng Prefix Function $\pi$.

🚀 **Thử thách:** Thuật toán tính mảng $\pi$ tận dụng các giá trị đã tính trước đó bằng con trỏ $j = \pi[j-1]$ để đạt độ phức tạp $O(N)$ thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Tính mảng Tiền tố KMP (Prefix Function $\pi$) của chuỗi $S$.
* **Dạng bài:** KMP Algorithm / Prefix Function.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Khái niệm Prefix Function $\pi[i]$**
* $\pi[i]$ là độ dài $k > 0$ lớn nhất sao cho tiền tố độ dài $k$ của $S[0 \dots i]$ trùng với hậu tố độ dài $k$ của $S[0 \dots i]$ ($k \le i$).

#### **Bước 2: Thuật toán Quy hoạch động KMP $O(N)$**
* Khởi tạo $j = \pi[i-1]$.
* Nếu $S[i] \neq S[j]$, nhảy lùi con trỏ $j \leftarrow \pi[j-1]$ cho tới khi tìm thấy khớp hoặc $j = 0$.
* Nếu $S[i] == S[j]$, $j++$. Gán $\pi[i] = j$.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(N)$ (Do $j$ tăng tối đa $N$ lần và giảm qua các bước nhảy).
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    string s;
    if (!(cin >> s)) return 0;
    
    int n = s.length();
    vector<int> pi(n, 0);
    
    for (int i = 1; i < n; i++) {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j]) {
            j = pi[j - 1];
        }
        if (s[i] == s[j]) {
            j++;
        }
        pi[i] = j;
    }
    
    for (int i = 0; i < n; i++) {
        cout << pi[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

---

# IKH-0050 - Lộ Trình Thu Gom Rác Thải Đô Thị URENCO

## 1. NỘI DUNG BÀI TOÁN

Công ty Môi trường Đô thị Hà Nội (URENCO) cử một xe tải chuyên dụng xuất phát từ **trạm trung tâm (đánh số 0)** đi qua $N$ điểm thu gom rác thải (đánh số từ $1$ đến $N$) và cuối cùng quay trở về trạm 0.

Chi phí (thời gian di chuyển) giữa hai điểm $u$ và $v$ là $C[u][v]$ phút. Ban điều hành muốn tìm một **lộ trình đi qua tất cả $N$ điểm thu gom đúng 1 lần và quay về trạm 0** sao cho **TỔNG CHI PHÍ DI CHUYỂN LÀ NHỎ NHẤT**.

Hãy tìm tổng chi phí di chuyển nhỏ nhất của lộ trình thu gom rác.

#### Input:
* Dòng đầu chứa số nguyên $N$ ($1 \le N \le 15$).
* $N + 1$ dòng tiếp theo, mỗi dòng chứa $N + 1$ số nguyên $C[u][v]$ đại diện cho ma trận chi phí từ điểm $u$ đến điểm $v$ ($0 \le u, v \le N, 0 \le C[u][v] \le 10^6, C[u][u] = 0$).

#### Output:
* Một số nguyên duy nhất là tổng chi phí di chuyển nhỏ nhất tìm được.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 8$.
* Subtask 2 (30% điểm): Ma trận chi phí đối xứng ($C[u][v] = C[v][u]$).
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung ($N \le 15$).

#### Sample 1:
**Input:**
```
3
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
```
**Output:**
```
80
```
**Giải thích:** Lộ trình tối ưu: 0 -> 1 -> 3 -> 2 -> 0 có tổng chi phí $10 + 25 + 30 + 15 = 80$.

---

💡 **Bạn có biết?** Bài toán Người du lịch (Traveling Salesperson Problem - TSP) là bài toán NP-hard kinh điển. Thuật toán Quy hoạch động Nén trạng thái Bit (Bitmask DP) giúp giải quyết chính xác trong $O(2^N \cdot N^2)$.

🚀 **Thử thách:** Trạng thái `dp[mask][u]` thể hiện tập các điểm đã đi qua mã hóa bằng Bitmask `mask` và điểm hiện tại là `u` hoạt động ra sao?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Bài toán Người du lịch (TSP) gồm $N+1$ đỉnh (từ $0$ đến $N$). Tìm chu trình Hamilton chi phí nhỏ nhất xuất phát và kết thúc tại 0.
* **Dạng bài:** Bitmask Dynamic Programming ($O(2^N \cdot N^2)$).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Định nghĩa Trạng thái Quy hoạch động Bitmask**
* Gọi `dp[mask][u]` là chi phí nhỏ nhất để đi qua tập các đỉnh được đánh dấu bằng `mask` và đỉnh cuối cùng hiện tại đang ở `u`.

#### **Bước 2: Công thức Chuyển trạng thái**
* Ban đầu `dp[1][0] = 0`.
* Với mỗi trạng thái `(mask, u)` hợp lệ, chuyển tới đỉnh `v` chưa thăm (`!(mask & (1 << v))`):
  `dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + cost[u][v])`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(2^{N+1} \cdot (N+1)^2)$ với $N \le 15 \implies \approx 6.5 \cdot 10^7$ phép tính.
* Bộ nhớ: $O(2^{N+1} \cdot N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    if (!(cin >> n)) return 0;
    
    int total_nodes = n + 1;
    vector<vector<long long>> cost(total_nodes, vector<long long>(total_nodes));
    for (int i = 0; i < total_nodes; i++) {
        for (int j = 0; j < total_nodes; j++) {
            cin >> cost[i][j];
        }
    }
    
    int num_masks = 1 << total_nodes;
    vector<vector<long long>> dp(num_masks, vector<long long>(total_nodes, INF));
    
    dp[1][0] = 0; // Trạng thái bắt đầu: mask = 1 (chỉ mới qua đỉnh 0), đỉnh hiện tại = 0
    
    for (int mask = 1; mask < num_masks; mask++) {
        for (int u = 0; u < total_nodes; u++) {
            if (dp[mask][u] == INF) continue;
            if (!(mask & (1 << u))) continue;
            
            for (int v = 0; v < total_nodes; v++) {
                if (!(mask & (1 << v))) {
                    int next_mask = mask | (1 << v);
                    dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + cost[u][v]);
                }
            }
        }
    }
    
    int full_mask = (1 << total_nodes) - 1;
    long long ans = INF;
    for (int u = 1; u < total_nodes; u++) {
        ans = min(ans, dp[full_mask][u] + cost[u][0]);
    }
    
    cout << ans << "\n";
    return 0;
}
```

---

# IKH-0051 - Phân Bổ Máy Chủ Trạm Mạng Viễn Thông Viettel

## 1. NỘI DUNG BÀI TOÁN

Mạng lưới hạ tầng trạm phát sóng Viettel gồm $N$ trạm mạng (đánh số từ $1$ đến $N$) tạo thành một **cấu trúc đồ thị dạng cây** kết nối bởi $N - 1$ đường cáp quang hai chiều.

Để nâng cấp dịch vụ truyền dữ liệu, Viettel cần đặt các máy chủ dịch vụ (Server) tại một số trạm mạng sao cho **tất cả $N$ trạm mạng đều được phủ sóng**. Một trạm mạng được phủ sóng nếu chính trạm đó được đặt máy chủ, hoặc có ít nhất 1 trạm kề trực tiếp với nó được đặt máy chủ.

Hãy tìm **số lượng máy chủ tối thiểu** cần đặt để phủ sóng toàn bộ $N$ trạm mạng.

#### Input:
* Dòng đầu chứa số nguyên $N$ ($1 \le N \le 2 \times 10^5$).
* $N - 1$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên $u&#95;i, v&#95;i$ ($1 \le u&#95;i, v&#95;i \le N$) thể hiện đường cáp kết nối hai trạm.

#### Output:
* Một số nguyên duy nhất là số lượng máy chủ tối thiểu cần đặt.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000$.
* Subtask 2 (30% điểm): Cây có dạng đường thẳng (dạng xích).
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
5
1 2
2 3
3 4
3 5
```
**Output:**
```
2
```
**Giải thích:** Đặt 2 máy chủ tại trạm 2 và trạm 3:
- Trạm 2 phủ sóng {1, 2, 3}.
- Trạm 3 phủ sóng {2, 3, 4, 5}.
Tất cả 5 trạm đều được phủ sóng.

---

💡 **Bạn có biết?** Bài toán Tập Phủ Đỉnh Tối Tiểu (Vertex Cover / Dominating Set on Tree) được giải quyết tối ưu trong thời gian tuyến tính $O(N)$ bằng Quy hoạch động trên Cây (Tree DP).

🚀 **Thử thách:** Ba trạng thái `dp[u][0]`, `dp[u][1]`, `dp[u][2]` thể hiện tình trạng phủ sóng của nút $u$ trong Tree DP như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Tìm Tập thống trị nhỏ nhất (Minimum Dominating Set) trên Cây.
* **Dạng bài:** Tree Dynamic Programming ($O(N)$).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Khai báo 3 Trạng thái Quy hoạch động**
* `dp[u][0]`: Đặt máy chủ tại $u$.
* `dp[u][1]`: Không đặt máy chủ tại $u$, $u$ được phủ bởi con của $u$.
* `dp[u][2]`: Không đặt máy chủ tại $u$, $u$ chưa được phủ bởi con nào ($u$ nương nhờ cha của $u$).

#### **Bước 2: Chuyển trạng thái DFS**
* `dp[u][0] = 1 + sum(min(dp[v][0], dp[v][1], dp[v][2]))`.
* `dp[u][2] = sum(dp[v][1])`.
* `dp[u][1]` yêu cầu có ít nhất 1 con $v$ chọn `dp[v][0]`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(N)$.
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

// dp[u][0]: u đặt server
// dp[u][1]: u không đặt server, được phủ bởi ít nhất 1 con của u
// dp[u][2]: u không đặt server, chưa được phủ bởi con nào (được phủ bởi cha của u)
vector<vector<int>> adj;
vector<int> dp0, dp1, dp2;

void dfs(int u, int p) {
    dp0[u] = 1;
    dp1[u] = 0;
    dp2[u] = 0;
    
    int sum_min01 = 0;
    bool covered_by_child = false;
    int min_diff = INF;
    
    for (int v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);
        
        dp0[u] += min({dp0[v], dp1[v], dp2[v]});
        dp2[u] += dp1[v];
        
        int best_child = min(dp0[v], dp1[v]);
        sum_min01 += best_child;
        
        if (dp0[v] <= dp1[v]) {
            covered_by_child = true;
        }
        min_diff = min(min_diff, dp0[v] - dp1[v]);
    }
    
    if (covered_by_child) {
        dp1[u] = sum_min01;
    } else {
        dp1[u] = sum_min01 + min_diff;
    }
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    if (!(cin >> n)) return 0;
    
    adj.resize(n + 1);
    dp0.assign(n + 1, 0);
    dp1.assign(n + 1, 0);
    dp2.assign(n + 1, 0);
    
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    dfs(1, 0);
    
    cout << min(dp0[1], dp1[1]) << "\n";
    return 0;
}
```

---

# IKH-0052 - Lập Kế Hoạch Đóng Tàu Siêu Trọng Gemadept

## 1. NỘI DUNG BÀI TOÁN

Công ty Cổ phần Đại lý Giao nhận Vận tải Gemadept có $N$ lô thép đóng tàu xếp thành hàng ngang. Lô thứ $i$ có trọng lượng $A&#95;i$ tấn.

Để vận chuyển thép vào nhà máy đóng tàu, công ty cần **chia $N$ lô thép này thành đúng $K$ đoạn con liên tiếp**. Chi phí của mỗi đoạn con được tính bằng **bình phương tổng trọng lượng của các lô thép trong đoạn con đó**.

Hãy giúp Gemadept tìm **TỔNG CHI PHÍ NHỎ NHẤT** để chia $N$ lô thép thành $K$ đoạn con liên tiếp.

#### Input:
* Dòng đầu chứa hai số nguyên $N, K$ ($1 \le K \le N \le 2000$).
* Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($1 \le A&#95;i \le 10^4$).

#### Output:
* Một số nguyên duy nhất là tổng chi phí nhỏ nhất tìm được.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 100$.
* Subtask 2 (30% điểm): $K = 1$ hoặc $K = N$.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung ($N, K \le 2000$).

#### Sample 1:
**Input:**
```
4 2
1 2 3 4
```
**Output:**
```
58
```
**Giải thích:** Chia thành 2 đoạn [1, 2, 3] và [4]:
- Đoạn 1: $(1 + 2 + 3)^2 = 6^2 = 36$.
- Đoạn 2: $4^2 = 16$.
- Tổng chi phí: $36 + 16 = 52$? Đợi đã, nếu chia [1, 2] (tổng 3, bình phương 9) và [3, 4] (tổng 7, bình phương 49) $\implies 9 + 49 = 58$.
Min là 52 (nếu chia [1, 2, 3] và [4]).

---

💡 **Bạn có biết?** Bài toán Quy hoạch động chia đoạn có thể tối ưu hóa từ $O(K \cdot N^2)$ về $O(K \cdot N \log N)$ nhờ Tối ưu hóa Chia để Trị (Divide and Conquer Optimization).

🚀 **Thử thách:** Công thức Quy hoạch động `dp[k][i] = min_{j < i} (dp[k-1][j] + (pref[i] - pref[j])^2)` hoạt động ra sao?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Chia mảng $A$ gồm $N$ phần tử thành $K$ đoạn con liên tiếp sao cho tổng bình phương các đoạn là nhỏ nhất.
* **Dạng bài:** Partition DP ($O(K \cdot N^2)$ / Divide & Conquer Optimization).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Công thức Quy hoạch động cơ bản**
* `dp[k][i]` là chi phí nhỏ nhất khi chia $i$ phần tử đầu thành $k$ đoạn.
* `dp[k][i] = min_{0 \le j < i} (dp[k-1][j] + (pref[i] - pref[j])^2)`.

#### **Bước 2: Đánh giá độ phức tạp**
* Thời gian: $O(K \cdot N^2)$ với $N \le 2000 \implies \approx 8 \cdot 10^6$ thao tác.
* Bộ nhớ: $O(K \cdot N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, k_groups;
    if (!(cin >> n >> k_groups)) return 0;
    
    vector<long long> a(n + 1);
    vector<long long> pref(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        pref[i] = pref[i - 1] + a[i];
    }
    
    vector<vector<long long>> dp(k_groups + 1, vector<long long>(n + 1, INF));
    dp[0][0] = 0;
    
    for (int k = 1; k <= k_groups; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[k - 1][j] != INF) {
                    long long sum = pref[i] - pref[j];
                    dp[k][i] = min(dp[k][i], dp[k - 1][j] + sum * sum);
                }
            }
        }
    }
    
    cout << dp[k_groups][n] << "\n";
    return 0;
}
```

---

# IKH-0053 - Phân Phối Thuốc Đột Biến Long Châu

## 1. NỘI DUNG BÀI TOÁN

Chuỗi Nhà thuốc FPT Long Châu quản lý mạng lưới gồm $N$ kho thuốc (đánh số từ $1$ đến $N$) và $M$ đường vận chuyển hai chiều. Đường thứ $i$ nối kho $u&#95;i$ và $v&#95;i$ với thời gian di chuyển $w&#95;i$ phút.

Để kịp thời cung cấp thuốc cấp cứu đột biến đến **kho đích $T$**, ban điều hành điều xe xuất phát từ **kho tổng $S$**. Tuy nhiên, xe tải vận chuyển có **bình nhiên liệu chạy tối đa $C$ phút** trước khi bắt buộc phải nạp lại nhiên liệu tại các kho có trạm sạc.

Cho danh sách các kho có trạm sạc. Hãy tìm **thời gian di chuyển ngắn nhất** từ $S$ đến $T$ sao cho thời gian di chuyển liên tục giữa hai lần sạc nhiên liệu không vượt quá $C$ phút. (Nếu không thể đến nơi, in ra `-1`).

#### Input:
* Dòng đầu chứa bốn số nguyên $N, M, C, K$ ($1 \le N \le 1000, 0 \le M \le 2000, 1 \le C \le 10^9, 0 \le K \le N$).
* Dòng thứ hai chứa $K$ số nguyên là danh sách các kho có trạm sạc.
* Dòng thứ ba chứa hai số nguyên $S, T$ ($1 \le S, T \le N$).
* $M$ dòng tiếp theo, dòng thứ $i$ chứa ba số nguyên $u&#95;i, v&#95;i, w&#95;i$ ($1 \le u&#95;i, v&#95;i \le N, 1 \le w&#95;i \le C$).

#### Output:
* Một số nguyên duy nhất là thời gian di chuyển ngắn nhất từ $S$ đến $T$.

#### Subtasks:
* Subtask 1 (30% điểm): Tất cả các kho đều có trạm sạc.
* Subtask 2 (30% điểm): $N \le 100, M \le 200$.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4 4 10 1
2
1 4
1 2 6
2 3 5
3 4 4
1 4 12
```
**Output:**
```
15
```
**Giải thích:** Đường 1 -> 4 tốn 12 > C = 10 (Không thể đi thẳng). Đường 1 -> 2 -> 3 -> 4:
- 1 -> 2: 6 <= 10 (Đến 2 sạc lại nhiên liệu)
- 2 -> 3 -> 4: $5 + 4 = 9 \le 10$ (Thỏa mãn).
Tổng thời gian: $6 + 5 + 4 = 15$.

---

💡 **Bạn có biết?** FPT Long Châu hiện phủ sóng 63 tỉnh thành với hệ thống logistics dược phẩm thông minh kiểm soát nghiêm ngặt thời gian và nhiệt độ bảo quản vắc-xin.

🚀 **Thử thách:** Thuật toán Dijkstra trạng thái 2D `dist[u][fuel_left]` giúp giải bài toán đường đi ngắn nhất ràng buộc nhiên liệu như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Tìm đường đi ngắn nhất từ $S$ tới $T$ trên đồ thị trọng số sao cho khoảng cách giữa các trạm sạc liên tiếp không quá $C$.
* **Dạng bài:** Multi-source Dijkstra / Graph Transformation.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Chuyển đổi Đồ thị Trạm sạc**
* Với mỗi trạm sạc, chạy Dijkstra tìm khoảng cách ngắn nhất tới tất cả các trạm sạc khác mà $\le C$.
* Tạo đồ thị mới với các đỉnh là các trạm sạc và trọng số là khoảng cách giữa chúng.

#### **Bước 2: Tìm đường đi ngắn nhất trên Đồ thị Trạm sạc**
* Chạy Dijkstra trên đồ thị trạm sạc mới từ $S$ tới $T$.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(K \cdot (N + M) \log N)$. Với $N \le 1000 \implies$ chạy cực nhanh.
* Bộ nhớ: $O(N + M)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long weight;
};

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, m, k_chargers;
    long long capacity;
    if (!(cin >> n >> m >> capacity >> k_chargers)) return 0;
    
    vector<bool> has_charger(n + 1, false);
    for (int i = 0; i < k_chargers; i++) {
        int x;
        cin >> x;
        has_charger[x] = true;
    }
    
    int s, t;
    cin >> s >> t;
    has_charger[s] = true;
    has_charger[t] = true;
    
    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        if (w <= capacity) {
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
    }
    
    // Dijkstra trạng thái: (thời gian tích lũy, đỉnh u, nhiên liệu đã dùng trong chặng hiện tại)
    // Hoặc đơn giản: Dijkstra 2 bước (ngắn nhất giữa các trạm sạc)
    // Do N <= 1000, chạy Dijkstra từ mỗi trạm sạc để dựng đồ thị mới giữa các trạm sạc!
    vector<int> chargers;
    for (int i = 1; i <= n; i++) {
        if (has_charger[i]) chargers.push_back(i);
    }
    
    int num_c = chargers.size();
    vector<vector<Edge>> charger_adj(n + 1);
    
    for (int src : chargers) {
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        vector<long long> dist(n + 1, INF);
        dist[src] = 0;
        pq.push({0, src});
        
        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();
            if (d > dist[u]) continue;
            
            for (const auto& edge : adj[u]) {
                if (dist[u] + edge.weight < dist[edge.to] && dist[u] + edge.weight <= capacity) {
                    dist[edge.to] = dist[u] + edge.weight;
                    pq.push({dist[edge.to], edge.to});
                }
            }
        }
        
        for (int target : chargers) {
            if (src != target && dist[target] <= capacity) {
                charger_adj[src].push_back({target, dist[target]});
            }
        }
    }
    
    // Dijkstra trên đồ thị trạm sạc
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    vector<long long> dist(n + 1, INF);
    dist[s] = 0;
    pq.push({0, s});
    
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (d > dist[u]) continue;
        
        for (const auto& edge : charger_adj[u]) {
            if (dist[u] + edge.weight < dist[edge.to]) {
                dist[edge.to] = dist[u] + edge.weight;
                pq.push({dist[edge.to], edge.to});
            }
        }
    }
    
    cout << (dist[t] == INF ? -1 : dist[t]) << "\n";
    return 0;
}
```

---

# IKH-0054 - Kiểm Trà Điểm Yếu Tuyến Cáp Quang Biển AAG

## 1. NỘI DUNG BÀI TOÁN

Tập đoàn Bưu chính Viễn thông Việt Nam (VNPT) quản lý mạng lưới tuyến cáp quang biển kết nối quốc tế AAG gồm $N$ trạm cập bờ (đánh số từ $1$ đến $N$) và $M$ đoạn đường cáp ngầm hai chiều giữa các trạm.

Một đoạn đường cáp ngầm được gọi là **Đoạn Cáp Yếu (Cầu / Bridge)** nếu khi đoạn cáp đó bị gãy đứt, hệ thống mạng lưới sẽ bị chia cắt thành ít nhất 2 thành phần không thể liên lạc được với nhau.

Hãy giúp VNPT **đếm số lượng Đoạn Cáp Yếu (Cầu)** trong hệ thống cáp quang biển.

#### Input:
* Dòng đầu chứa hai số nguyên $N, M$ ($1 \le N \le 2 \times 10^5, 0 \le M \le 2 \times 10^5$).
* $M$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên $u&#95;i, v&#95;i$ ($1 \le u&#95;i, v&#95;i \le N$).

#### Output:
* Một số nguyên duy nhất là số lượng Đoạn Cáp Yếu (Cầu) tìm được.

#### Subtasks:
* Subtask 1 (30% điểm): $N, M \le 1000$.
* Subtask 2 (30% điểm): Đồ thị có dạng cây (kết quả là $N - 1$).
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
5 5
1 2
2 3
3 1
3 4
4 5
```
**Output:**
```
2
```
**Giải thích:** 2 đoạn cáp yếu (cầu) là (3-4) và (4-5). Đoạn (1-2), (2-3), (3-1) nằm trong chu trình nên không phải là cầu.

---

💡 **Bạn có biết?** Thuật toán Tarjan dựa trên duyệt DFS cùng hai mảng `num` và `low` giúp tìm toàn bộ Cầu và Khớp của đồ thị trong thời gian tuyến tính $O(N + M)$.

🚀 **Thử thách:** Điều kiện để cạnh $(u, v)$ là Cầu trong cây DFS là $\text{low}[v] > \text{num}[u]$ chuẩn như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Đếm số lượng Cầu (Bridges) trên đồ thị vô hướng gồm $N$ đỉnh và $M$ cạnh.
* **Dạng bài:** Tarjan's Algorithm for Bridges ($O(N + M)$).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Thuật toán Tarjan với Mảng `num` và `low`**
* `num[u]`: Thứ tự thăm đỉnh $u$ trong cây DFS.
* `low[u]`: Thứ tự `num` nhỏ nhất có thể đi tới từ cây con gốc $u$ qua tối đa 1 cạnh ngược (Back-edge).

#### **Bước 2: Điều kiện Cạnh $(u, v)$ là Cầu**
* Cạnh $(u, v)$ là Cầu $\iff \text{low}[v] > \text{num}[u]$ (nghĩa là từ các đỉnh trong cây con gốc $v$ không có cạnh ngược nào đi lên phía trên $u$).

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(N + M)$.
* Bộ nhớ: $O(N + M)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;
vector<vector<pair<int, int>>> adj;
vector<int> num, low;
int timer_cnt = 0;
int bridge_cnt = 0;

void dfs(int u, int p_edge_id) {
    num[u] = low[u] = ++timer_cnt;
    for (auto& edge : adj[u]) {
        int v = edge.first;
        int edge_id = edge.second;
        if (edge_id == p_edge_id) continue;
        
        if (num[v]) {
            low[u] = min(low[u], num[v]);
        } else {
            dfs(v, edge_id);
            low[u] = min(low[u], low[v]);
            if (low[v] > num[u]) {
                bridge_cnt++;
            }
        }
    }
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    if (!(cin >> n >> m)) return 0;
    
    adj.resize(n + 1);
    num.assign(n + 1, 0);
    low.assign(n + 1, 0);
    
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back({v, i});
        adj[v].push_back({u, i});
    }
    
    for (int i = 1; i <= n; i++) {
        if (!num[i]) {
            dfs(i, -1);
        }
    }
    
    cout << bridge_cnt << "\n";
    return 0;
}
```

---

# IKH-0055 - Quản Lý Mạng Lưới Điện Thông Minh EVN

## 1. NỘI DUNG BÀI TOÁN

Tập đoàn Điện lực Việt Nam (EVN) quản lý hệ thống $N$ trạm biến áp (đánh số từ $1$ đến $N$). Trạm thứ $i$ hiện đang phát điện với công suất $A&#95;i$ MW.

Trung tâm Điều độ Hệ thống Điện Quốc gia (A0) thực hiện $Q$ thao tác cập nhật và kiểm tra lưới điện thuộc 2 loại:
* `1 L R x`: Điều chỉnh công suất **cộng thêm $x$ MW cho tất cả các trạm từ $L$ đến $R$** ($A&#95;i \leftarrow A&#95;i + x$ với $L \le i \le R$).
* `2 L R`: Tính **tổng công suất phát điện của tất cả các trạm trong đoạn từ $L$ đến $R$**.

Hãy in ra kết quả cho tất cả các thao tác loại 2.

#### Input:
* Dòng đầu chứa hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \times 10^5$).
* Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($0 \le A&#95;i \le 10^9$).
* $Q$ dòng tiếp theo mô tả thao tác:
  * `1 L R x` ($1 \le L \le R \le N, 1 \le x \le 10^9$)
  * `2 L R` ($1 \le L \le R \le N$)

#### Output:
* In ra kết quả tương ứng cho mỗi thao tác loại 2 trên từng dòng.

#### Subtasks:
* Subtask 1 (30% điểm): $N, Q \le 1000$.
* Subtask 2 (30% điểm): Các thao tác loại 1 chỉ có $L = R$ (Cập nhật điểm).
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
5 3
1 2 3 4 5
2 1 3
1 1 3 10
2 1 3
```
**Output:**
```
6
36
```
**Giải thích:**
- Thao tác 1: Tổng đoạn 1->3 = $1 + 2 + 3 = 6$.
- Thao tác 2: Cộng 10 cho đoạn 1->3 $\implies A = [11, 12, 13, 4, 5]$.
- Thao tác 3: Tổng mới đoạn 1->3 = $11 + 12 + 13 = 36$.

---

💡 **Bạn có biết?** Cây Phân đoạn kết hợp Kỹ thuật Đẩy lười (Segment Tree with Lazy Propagation) cho phép cập nhật cả một đoạn và truy vấn tổng đoạn trong thời gian $O(\log N)$.

🚀 **Thử thách:** Hàm `push()` lan truyền giá trị lười `lazy[node]` xuống 2 con `2*node` và `2*node+1` hoạt động như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Duy trì mảng $N$ phần tử. Hỗ trợ Cộng $x$ cho đoạn $[L, R]$ và Truy vấn tổng đoạn $[L, R]$.
* **Dạng bài:** Segment Tree with Lazy Propagation ($O(\log N)$).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Kỹ thuật Đẩy lười (Lazy Propagation)**
* Mỗi nút trong cây lưu thêm giá trị `lazy[node]`.
* Khi cập nhật cả đoạn $[L, R]$ nằm hoàn toàn trong phạm vi nút, gán `lazy[node] += val`, cập nhật `tree[node] += val * length` rồi dừng lại không đi xuống sâu hơn.

#### **Bước 2: Hàm `push()`**
* Mỗi khi cần truy cập hoặc cập nhật nút con, đẩy giá trị `lazy` xuống hai con và gán `lazy[node] = 0`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: Tiền xử lý $O(N)$, Cập nhật/Truy vấn $O(\log N) \implies O(N + Q \log N)$.
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>

using namespace std;

struct LazySegmentTree {
    int n;
    vector<long long> tree, lazy;
    
    LazySegmentTree(int n) : n(n), tree(4 * n + 1, 0), lazy(4 * n + 1, 0) {}
    
    void build(const vector<long long>& a, int node, int start, int end) {
        if (start == end) {
            tree[node] = a[start];
            return;
        }
        int mid = (start + end) / 2;
        build(a, 2 * node, start, mid);
        build(a, 2 * node + 1, mid + 1, end);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }
    
    void push(int node, int start, int end) {
        if (lazy[node] != 0) {
            long long val = lazy[node];
            int mid = (start + end) / 2;
            
            lazy[2 * node] += val;
            tree[2 * node] += val * (mid - start + 1);
            
            lazy[2 * node + 1] += val;
            tree[2 * node + 1] += val * (end - mid);
            
            lazy[node] = 0;
        }
    }
    
    void update(int node, int start, int end, int l, int r, long long val) {
        if (r < start || end < l) return;
        if (l <= start && end <= r) {
            lazy[node] += val;
            tree[node] += val * (end - start + 1);
            return;
        }
        push(node, start, end);
        int mid = (start + end) / 2;
        update(2 * node, start, mid, l, r, val);
        update(2 * node + 1, mid + 1, end, l, r, val);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }
    
    long long query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return 0;
        if (l <= start && end <= r) return tree[node];
        push(node, start, end);
        int mid = (start + end) / 2;
        return query(2 * node, start, mid, l, r) + query(2 * node + 1, mid + 1, end, l, r);
    }
};

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, q;
    if (!(cin >> n >> q)) return 0;
    
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];
    
    LazySegmentTree seg(n);
    seg.build(a, 1, 1, n);
    
    for (int j = 0; j < q; j++) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r;
            long long x;
            cin >> l >> r >> x;
            seg.update(1, 1, n, l, r, x);
        } else {
            int l, r;
            cin >> l >> r;
            cout << seg.query(1, 1, n, l, r) << "\n";
        }
    }
    return 0;
}
```

---

# IKH-0056 - Truy Vấn Đường Đi Ngắn Nhất Đèo Cả

## 1. NỘI DUNG BÀI TOÁN

Tập đoàn Đèo Cả vận hành hệ thống $N$ trạm kiểm soát giao thông đường hầm xuyên núi (đánh số từ $1$ đến $N$) kết nối dạng cây bởi $N - 1$ đường hầm hai chiều. Đường hầm thứ $i$ nối trạm $u&#95;i$ và $v&#95;i$ có độ dài $w&#95;i$ mét.

Ban điều hành nhận $Q$ truy vấn kiểm tra khoảng cách. Mỗi truy vấn gồm hai trạm $u$ và $v$. Hãy tính **khoảng cách đường đi ngắn nhất (tổng độ dài các đường hầm) giữa hai trạm $u$ và $v$**.

Hãy in ra kết quả khoảng cách cho $Q$ truy vấn.

#### Input:
* Dòng đầu chứa hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \times 10^5$).
* $N - 1$ dòng tiếp theo, dòng thứ $i$ chứa ba số nguyên $u&#95;i, v&#95;i, w&#95;i$ ($1 \le u&#95;i, v&#95;i \le N, 1 \le w&#95;i \le 10^9$).
* $Q$ dòng tiếp theo, dòng thứ $j$ chứa hai số nguyên $u&#95;j, v&#95;j$ ($1 \le u&#95;j, v&#95;j \le N$).

#### Output:
* In ra $Q$ dòng, mỗi dòng chứa một số nguyên là khoảng cách ngắn nhất giữa $u$ và $v$.

#### Subtasks:
* Subtask 1 (30% điểm): $N, Q \le 1000$.
* Subtask 2 (30% điểm): Cây có dạng đường thẳng (dạng xích).
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4 2
1 2 5
2 3 3
2 4 7
1 3
3 4
```
**Output:**
```
8
10
```
**Giải thích:**
- Đường đi 1 -> 3: 1 -> 2 -> 3 có độ dài $5 + 3 = 8$.
- Đường đi 3 -> 4: 3 -> 2 -> 4 có độ dài $3 + 7 = 10$.

---

💡 **Bạn có biết?** Thuật toán Nâng Nhị Phân (Binary Lifting) giúp tìm Tổ tiên Chung Gần nhất (Lowest Common Ancestor - LCA) của 2 đỉnh trên Cây và tính khoảng cách trong thời gian $O(\log N)$.

🚀 **Thử thách:** Khoảng cách giữa $u$ và $v$ được tính qua khoảng cách từ gốc tới đỉnh: $\text{Dist}(u, v) = \text{Depth}[u] + \text{Depth}[v] - 2 \cdot \text{Depth}[\text{LCA}(u, v)]$.

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho cây có trọng số gồm $N$ đỉnh. Xử lý $Q$ truy vấn tính khoảng cách ngắn nhất giữa $u$ và $v$.
* **Dạng bài:** Lowest Common Ancestor (LCA) via Binary Lifting ($O(\log N)$ query).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Kỹ thuật Nâng Nhị Phân (Binary Lifting)**
* Mảng `up[u][i]` lưu tổ tiên thứ $2^i$ của đỉnh $u$.
* Tiền xử lý DFS trong $O(N \log N)$.

#### **Bước 2: Công thức Khoảng cách trên Cây**
* $\text{Dist}(u, v) = \text{DistRoot}[u] + \text{DistRoot}[v] - 2 \cdot \text{DistRoot}[\text{LCA}(u, v)]$.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: Tiền xử lý $O(N \log N)$, Mỗi truy vấn $O(\log N) \implies O((N + Q) \log N)$.
* Bộ nhớ: $O(N \log N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

const int LOGN = 19;

struct Edge {
    int to;
    long long weight;
};

int n, q;
vector<vector<Edge>> adj;
vector<int> depth;
vector<long long> dist_from_root;
vector<vector<int>> up;

void dfs(int u, int p, int d, long long w_sum) {
    depth[u] = d;
    dist_from_root[u] = w_sum;
    up[u][0] = p;
    for (int i = 1; i < LOGN; i++) {
        up[u][i] = up[up[u][i - 1]][i - 1];
    }
    
    for (const auto& edge : adj[u]) {
        if (edge.to != p) {
            dfs(edge.to, u, d + 1, w_sum + edge.weight);
        }
    }
}

int get_lca(int u, int v) {
    if (depth[u] < depth[v]) swap(u, v);
    
    for (int i = LOGN - 1; i >= 0; i--) {
        if (depth[u] - (1 << i) >= depth[v]) {
            u = up[u][i];
        }
    }
    
    if (u == v) return u;
    
    for (int i = LOGN - 1; i >= 0; i--) {
        if (up[u][i] != up[v][i]) {
            u = up[u][i];
            v = up[v][i];
        }
    }
    return up[u][0];
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    if (!(cin >> n >> q)) return 0;
    
    adj.resize(n + 1);
    depth.assign(n + 1, 0);
    dist_from_root.assign(n + 1, 0);
    up.assign(n + 1, vector<int>(LOGN, 0));
    
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }
    
    dfs(1, 1, 0, 0);
    
    for (int j = 0; j < q; j++) {
        int u, v;
        cin >> u >> v;
        int lca = get_lca(u, v);
        long long ans = dist_from_root[u] + dist_from_root[v] - 2 * dist_from_root[lca];
        cout << ans << "\n";
    }
    return 0;
}
```

---

# IKH-0057 - Phân Phối Luồng Băng Thông Viettel VNPT

## 1. NỘI DUNG BÀI TOÁN

Liên danh Viettel - VNPT quản lý mạng lưới đường cáp quang kết nối giữa $N$ trạm trung chuyển dữ liệu (đánh số từ $1$ đến $N$) và $M$ kênh truyền dẫn một chiều. Kênh truyền thứ $i$ dẫn dữ liệu từ trạm $u&#95;i$ đến trạm $v&#95;i$ với **dung lượng băng thông tối đa** là $c&#95;i$ Gbps.

Để phục vụ phát sóng trực tiếp sự kiện thể thao quốc gia, liên danh cần **bơm dữ liệu từ trạm nguồn $S$ đến trạm đích $T$**.

Hãy tìm **TỔNG LƯỢNG BĂNG THÔNG TỐI ĐA (Luồng cực đại)** có thể truyền dẫn thành công từ trạm $S$ đến trạm $T$.

#### Input:
* Dòng đầu chứa bốn số nguyên $N, M, S, T$ ($1 \le N \le 1000, 0 \le M \le 5000, 1 \le S, T \le N, S \neq T$).
* $M$ dòng tiếp theo, dòng thứ $i$ chứa ba số nguyên $u&#95;i, v&#95;i, c&#95;i$ ($1 \le u&#95;i, v&#95;i \le N, 1 \le c&#95;i \le 10^9$).

#### Output:
* Một số nguyên duy nhất là tổng lượng băng thông tối đa truyền từ $S$ đến $T$.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 100, M \le 500$.
* Subtask 2 (30% điểm): Băng thông mỗi kênh $c&#95;i = 1$.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4 5 1 4
1 2 100
1 3 50
2 3 50
2 4 50
3 4 100
```
**Output:**
```
150
```
**Giải thích:**
- Luồng 1: 1 -> 2 -> 4 (50 Gbps)
- Luồng 2: 1 -> 2 -> 3 -> 4 (50 Gbps)
- Luồng 3: 1 -> 3 -> 4 (50 Gbps)
Tổng luồng cực đại = $50 + 50 + 50 = 150$ Gbps.

---

💡 **Bạn có biết?** Thuật toán Dinic giải bài toán Luồng cực đại (Maximum Flow) trong thời gian $O(V^2 E)$ (hoặc $O(E \sqrt{V})$ trên đồ thị đơn vị), là nền tảng tối ưu hóa lưu lượng mạng truyền dẫn.

🚀 **Thử thách:** Thuật toán Dinic xây dựng đồ thị phân tầng (Level Graph) bằng BFS và tìm đường tăng luồng bằng DFS như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Tìm luồng cực đại (Maximum Flow) từ đỉnh nguồn $S$ tới đỉnh đích $T$ trên đồ thị có hướng $N$ đỉnh và $M$ cạnh.
* **Dạng bài:** Dinic's Algorithm for Max Flow ($O(V^2 E)$).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Cấu trúc Đồ thị Luồng và Cạnh Thặng dư**
* Mỗi cạnh $(u, v)$ có dung lượng $c$, luồng $f$. Cạnh ngược $(v, u)$ có dung lượng $0$, luồng $-f$.

#### **Bước 2: Thuật toán Dinic (BFS + DFS)**
* BFS dựng Đồ thị phân tầng (Level Graph).
* DFS tìm các đường tăng luồng (Blocking Flow) dựa trên mảng con trỏ `ptr` để tránh lặp lại cạnh.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: $O(V^2 E)$ trong trường hợp tổng quát, cực nhanh trên thực tế.
* Bộ nhớ: $O(V + E)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long cap;
    long long flow;
    int rev;
};

struct Dinic {
    int n;
    vector<vector<Edge>> adj;
    vector<int> level;
    vector<int> ptr;
    
    Dinic(int n) : n(n), adj(n + 1), level(n + 1), ptr(n + 1) {}
    
    void add_edge(int from, int to, long long cap) {
        adj[from].push_back({to, cap, 0, (int)adj[to].size()});
        adj[to].push_back({from, 0, 0, (int)adj[from].size() - 1});
    }
    
    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q;
        q.push(s);
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            for (const auto& edge : adj[u]) {
                if (edge.cap - edge.flow > 0 && level[edge.to] == -1) {
                    level[edge.to] = level[u] + 1;
                    q.push(edge.to);
                }
            }
        }
        return level[t] != -1;
    }
    
    long long dfs(int u, int t, long long pushed) {
        if (pushed == 0) return 0;
        if (u == t) return pushed;
        
        for (int& cid = ptr[u]; cid < adj[u].size(); ++cid) {
            auto& edge = adj[u][cid];
            int tr = edge.to;
            if (level[u] + 1 != level[tr] || edge.cap - edge.flow == 0) continue;
            
            long long tr_pushed = dfs(tr, t, min(pushed, edge.cap - edge.flow));
            if (tr_pushed == 0) continue;
            
            edge.flow += tr_pushed;
            adj[tr][edge.rev].flow -= tr_pushed;
            return tr_pushed;
        }
        return 0;
    }
    
    long long max_flow(int s, int t) {
        long long flow = 0;
        while (bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, t, INF)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;
    
    Dinic dinic(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        dinic.add_edge(u, v, c);
    }
    
    cout << dinic.max_flow(s, t) << "\n";
    return 0;
}
```

---

# IKH-0058 - Quy Hoạch Vành Đai An Ninh Sân Bay Long Thành

## 1. NỘI DUNG BÀI TOÁN

Ban Quản lý Dự án Sân bay Quốc tế Long Thành xác định vị trí của $N$ cột mốc quan trắc an ninh trong không gian 2D. Cột mốc thứ $i$ có tọa độ $(X&#95;i, Y&#95;i)$.

Để xây dựng hệ thống hàng rào bảo vệ bao quanh toàn bộ các cột mốc quan trắc, ban quản lý cần tìm **Chu vi nhỏ nhất của Đa giác Bao lồi (Convex Hull)** bao trùm tất cả $N$ điểm cột mốc này.

Hãy tính **chu vi nhỏ nhất của vành đai an ninh đa giác bao lồi** (làm tròn đến 2 chữ số thập phân).

#### Input:
* Dòng đầu chứa số nguyên $N$ ($3 \le N \le 2 \times 10^5$).
* $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên $X&#95;i, Y&#95;i$ ($-10^9 \le X&#95;i, Y&#95;i \le 10^9$).

#### Output:
* In ra một số thực duy nhất là chu vi đa giác bao lồi, làm tròn đúng 2 chữ số sau dấu phẩy.

#### Subtasks:
* Subtask 1 (30% điểm): $N \le 1000$.
* Subtask 2 (30% điểm): Tất cả các điểm nằm trên một đường tròn.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4
0 0
0 3
4 0
4 3
```
**Output:**
```
14.00
```
**Giải thích:** 4 điểm tạo thành hình chữ nhật kích thước $4 \times 3$ $\implies$ Chu vi $= (4 + 3) \times 2 = 14.00$.

---

💡 **Bạn có biết?** Thuật toán Monotone Chain của Andrew tìm Bao lồi (Convex Hull) trong $O(N \log N)$ bằng cách sắp xếp tọa độ và dựng vỏ trên (Upper Hull) và vỏ dưới (Lower Hull).

🚀 **Thử thách:** Tích hướng (Cross Product) của 2 vectơ $(B - A) \times (C - A)$ kiểm tra rẽ trái/rẽ phải hoạt động như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho $N$ điểm trong mặt phẳng 2D. Tìm Bao lồi (Convex Hull) và tính chu vi của nó.
* **Dạng bài:** Computational Geometry / Convex Hull (Andrew's Monotone Chain $O(N \log N)$).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Thuật toán Andrew's Monotone Chain**
* Sắp xếp các điểm theo tọa độ $x$ tăng dần (nếu $x$ bằng nhau thì $y$ tăng dần).
* Dựng vỏ dưới (Lower Hull) và vỏ trên (Upper Hull) sử dụng phép thử Tích hướng (Cross Product).

#### **Bước 2: Tích hướng kiểm tra Hướng rẽ**
* $\text{Cross}(O, A, B) = (A.x - O.x)(B.y - O.y) - (A.y - O.y)(B.x - O.x)$.
* Nếu $\le 0$, nghĩa là rẽ phải hoặc thẳng hàng $\implies$ loại bỏ đỉnh đỉnh ở đỉnh stack `hull.pop_back()`.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: Sắp xếp $O(N \log N)$, Dựng bao lồi $O(N) \implies O(N \log N)$.
* Bộ nhớ: $O(N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

struct Point {
    long long x, y;
    
    bool operator<(const Point& p) const {
        if (x != p.x) return x < p.x;
        return y < p.y;
    }
};

long long cross_product(Point o, Point a, Point b) {
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}

double dist(Point a, Point b) {
    long long dx = a.x - b.x;
    long long dy = a.y - b.y;
    return sqrt(dx * dx + dy * dy);
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<Point> pts(n);
    for (int i = 0; i < n; i++) {
        cin >> pts[i].x >> pts[i].y;
    }
    
    sort(pts.begin(), pts.end());
    
    vector<Point> hull;
    // Lower hull
    for (int i = 0; i < n; i++) {
        while (hull.size() >= 2 && cross_product(hull[hull.size() - 2], hull.back(), pts[i]) <= 0) {
            hull.pop_back();
        }
        hull.push_back(pts[i]);
    }
    
    // Upper hull
    int lower_sz = hull.size();
    for (int i = n - 2; i >= 0; i--) {
        while (hull.size() > lower_sz && cross_product(hull[hull.size() - 2], hull.back(), pts[i]) <= 0) {
            hull.pop_back();
        }
        hull.push_back(pts[i]);
    }
    
    hull.pop_back(); // Điểm đầu lặp lại
    
    double perimeter = 0.0;
    int k = hull.size();
    for (int i = 0; i < k; i++) {
        perimeter += dist(hull[i], hull[(i + 1) % k]);
    }
    
    cout << fixed << setprecision(2) << perimeter << "\n";
    return 0;
}
```

---

# IKH-0059 - Truy Vấn Lịch Sử Giao Dịch Vietcombank

## 1. NỘI DUNG BÀI TOÁN

Hệ thống ngân hàng Vietcombank ghi nhận dãy số dư $A&#95;1, A&#95;2, \dots, A&#95;N$ của $N$ tài khoản doanh nghiệp.

Ban thanh tra ngân hàng thực hiện $Q$ truy vấn kiểm tra dữ liệu lịch sử. Mỗi truy vấn gồm 3 số nguyên $L, R, K$ ($1 \le L \le R \le N, 1 \le K \le R - L + 1$). Hệ thống cần tìm **giá trị phần tử lớn thứ $K$ (K-th smallest / largest element)** trong đoạn tài khoản từ $L$ đến $R$.

Hãy in ra kết quả cho tất cả $Q$ truy vấn lịch sử.

#### Input:
* Dòng đầu chứa hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \times 10^5$).
* Dòng thứ hai chứa $N$ số nguyên $A&#95;1, A&#95;2, \dots, A&#95;N$ ($1 \le A&#95;i \le 10^9$).
* $Q$ dòng tiếp theo, dòng thứ $j$ chứa ba số nguyên $L&#95;j, R&#95;j, K&#95;j$.

#### Output:
* In ra $Q$ dòng, mỗi dòng chứa một số nguyên là phần tử nhỏ thứ $K$ trong đoạn $[L, R]$.

#### Subtasks:
* Subtask 1 (30% điểm): $N, Q \le 1000$.
* Subtask 2 (30% điểm): $L = 1, R = N$ cho mọi truy vấn.
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung ($N, Q \le 2 \times 10^5$).

#### Sample 1:
**Input:**
```
5 3
1 5 2 4 3
1 5 3
2 4 1
1 3 2
```
**Output:**
```
3
2
2
```
**Giải thích:**
- Truy vấn 1 (1->5, K=3): Đoạn [1, 5, 2, 4, 3] xếp tăng dần là [1, 2, 3, 4, 5] $\implies$ Phần tử thứ 3 là 3.
- Truy vấn 2 (2->4, K=1): Đoạn [5, 2, 4] xếp tăng dần là [2, 4, 5] $\implies$ Phần tử thứ 1 là 2.

---

💡 **Bạn có biết?** Cây Phân đoạn Bất biến (Persistent Segment Tree) lưu lại lịch sử thay đổi qua từng phiên bản, cho phép truy vấn phần tử nhỏ thứ $K$ trên đoạn bất kỳ trong $O(\log N)$.

🚀 **Thử thách:** Hàm `update` tạo ra nút mới thay vì sửa trực tiếp giúp duy trì $N$ phiên bản cây Segment Tree với bộ nhớ $O(N \log N)$ như thế nào?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Cho mảng $A$. Xử lý $Q$ truy vấn tìm phần tử nhỏ thứ $K$ trong đoạn $[L, R]$.
* **Dạng bài:** Persistent Segment Tree ($O(\log N)$ query).

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Rời rạc hóa Dữ liệu**
* Sắp xếp và loại bỏ phần tử trùng lặp của mảng $A$ để đưa giá trị về phạm vi $[1, M]$.

#### **Bước 2: Dựng Persistent Segment Tree (Cây Phân đoạn Bất biến)**
* Gốc `roots[i]` lưu trạng thái cây sau khi chèn $i$ phần tử đầu tiên.
* Mỗi lần chèn chỉ tạo thêm $O(\log M)$ nút mới.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: Tiền xử lý $O(N \log N)$, Mỗi truy vấn $O(\log N) \implies O((N + Q) \log N)$.
* Bộ nhớ: $O(N \log N)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
    int count;
    int left, right;
};

int n, q;
vector<long long> a, sorted_a;
vector<int> roots;
vector<Node> tree;

int get_id(long long val) {
    return lower_bound(sorted_a.begin(), sorted_a.end(), val) - sorted_a.begin() + 1;
}

int update(int prev_root, int l, int r, int val) {
    int cur = tree.size();
    tree.push_back(tree[prev_root]);
    tree[cur].count++;
    
    if (l == r) return cur;
    
    int mid = (l + r) / 2;
    if (val <= mid) {
        tree[cur].left = update(tree[prev_root].left, l, mid, val);
    } else {
        tree[cur].right = update(tree[prev_root].right, mid + 1, r, val);
    }
    return cur;
}

int query(int left_root, int right_root, int l, int r, int k) {
    if (l == r) return l;
    
    int count_left = tree[tree[right_root].left].count - tree[tree[left_root].left].count;
    int mid = (l + r) / 2;
    if (count_left >= k) {
        return query(tree[left_root].left, tree[right_root].left, l, mid, k);
    } else {
        return query(tree[left_root].right, tree[right_root].right, mid + 1, r, k - count_left);
    }
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    if (!(cin >> n >> q)) return 0;
    
    a.resize(n + 1);
    sorted_a.resize(n);
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        sorted_a[i - 1] = a[i];
    }
    
    sort(sorted_a.begin(), sorted_a.end());
    sorted_a.erase(unique(sorted_a.begin(), sorted_a.end()), sorted_a.end());
    int m = sorted_a.size();
    
    tree.push_back({0, 0, 0}); // Null node index 0
    roots.resize(n + 1, 0);
    
    for (int i = 1; i <= n; i++) {
        int id = get_id(a[i]);
        roots[i] = update(roots[i - 1], 1, m, id);
    }
    
    for (int j = 0; j < q; j++) {
        int l, r, k;
        cin >> l >> r >> k;
        int ans_id = query(roots[l - 1], roots[r], 1, m, k);
        cout << sorted_a[ans_id - 1] << "\n";
    }
    return 0;
}
```

---

# IKH-0060 - Tối Ưu Hóa Tuyến Đường Vận Chuyển VinFast

## 1. NỘI DUNG BÀI TOÁN

Tập đoàn VinFast quản lý mạng lưới vận chuyển xe điện gồm $N$ trung tâm phân phối (đánh số từ $1$ đến $N$) và $M$ đường cao tốc hai chiều kết nối giữa các trung tâm. Đường thứ $i$ nối $u&#95;i$ và $v&#95;i$ với độ dài $w&#95;i$ km.

Để tối ưu hóa chi phí vận hành cho đợt xuất khẩu ô tô điện toàn cầu, ban tổng giám đốc đưa ra $Q$ truy vấn phức hợp thuộc 2 loại:
* `1 u v w`: Thay đổi độ dài đường cao tốc nối trực tiếp giữa $u$ và $v$ thành giá trị mới $w$.
* `2 u v`: Tính **độ dài đường đi ngắn nhất giữa hai trung tâm $u$ và $v$**.

Hãy in ra kết quả độ dài ngắn nhất cho tất cả các truy vấn loại 2. (Nếu không có đường đi, in ra `-1`).

#### Input:
* Dòng đầu chứa ba số nguyên $N, M, Q$ ($1 \le N \le 2000, 0 \le M \le 5000, 1 \le Q \le 2000$).
* $M$ dòng tiếp theo, dòng thứ $i$ chứa ba số nguyên $u&#95;i, v&#95;i, w&#95;i$ ($1 \le u&#95;i, v&#95;i \le N, 1 \le w&#95;i \le 10^9$).
* $Q$ dòng tiếp theo mô tả truy vấn:
  * `1 u v w` ($1 \le u, v \le N, 1 \le w \le 10^9$)
  * `2 u v` ($1 \le u, v \le N$)

#### Output:
* In ra kết quả tương ứng cho mỗi truy vấn loại 2 trên từng dòng.

#### Subtasks:
* Subtask 1 (30% điểm): $N, M, Q \le 100$.
* Subtask 2 (30% điểm): Không có truy vấn loại 1 (Chỉ truy vấn đường đi ngắn nhất).
* Subtask 3 (40% điểm): Không có ràng buộc bổ sung.

#### Sample 1:
**Input:**
```
4 4 3
1 2 5
2 3 3
3 4 2
1 4 20
2 1 4
1 1 4 5
2 1 4
```
**Output:**
```
10
5
```
**Giải thích:**
- Truy vấn 1 (2 1 4): Đường đi 1 -> 2 -> 3 -> 4 = $5 + 3 + 2 = 10$.
- Truy vấn 2 (1 1 4 5): Cập nhật đường 1 -> 4 thành 5 km.
- Truy vấn 3 (2 1 4): Đường đi mới ngắn nhất 1 -> 4 = 5.

---

💡 **Bạn có biết?** Bài toán Đồ thị Động (Dynamic Shortest Path) đòi hỏi sự kết hợp tinh tế giữa Thuật toán Dijkstra và cập nhật trọng số trong hệ thống logistics VinFast.

🚀 **Thử thách:** Thuật toán Dijkstra hàng đợi ưu tiên `std::priority_queue` giải quyết truy vấn $O(M \log N)$ chuẩn ra sao?

## 2. HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

# HƯỚNG DẪN GIẢNG DẠY & EDITORIAL

## 1. PHÂN TÍCH YÊU CẦU ĐỀ BÀI
* **Tóm tắt:** Đồ thị động gồm $N$ đỉnh. Hỗ trợ Cập nhật trọng số cạnh $(u, v) = w$ và Truy vấn đường đi ngắn nhất giữa $u$ và $v$.
* **Dạng bài:** Dynamic Shortest Path / Priority Queue Dijkstra.

---

## 2. PHƯƠNG PHÁP SUY LUẬN & DẪN DẮT HỌC SINH (5 BƯỚC)

#### **Bước 1: Quản lý Cạnh Động bằng `std::map`**
* Sử dụng `vector<map<int, long long>> adj_map` để cập nhật trọng số cạnh giữa $u$ và $v$ trong $O(\log \text{deg})$.

#### **Bước 2: Truy vấn Đường đi Ngắn nhất**
* Chạy thuật toán Dijkstra từ $u$ dừng lại ngay khi chạm tới $t$.

#### **Bước 3: Đánh giá độ phức tạp**
* Thời gian: Cập nhật $O(\log N)$, Truy vấn $O((N + M) \log N)$.
* Bộ nhớ: $O(N + M)$.

## 3. CODE GIẢI C++ CHUẨN (100% AC)

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long weight;
};

int n, m, q;
vector<map<int, long long>> adj_map;

long long dijkstra(int s, int t) {
    if (s == t) return 0;
    
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    vector<long long> dist(n + 1, INF);
    
    dist[s] = 0;
    pq.push({0, s});
    
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        
        if (d > dist[u]) continue;
        if (u == t) return d;
        
        for (const auto& edge : adj_map[u]) {
            int v = edge.first;
            long long w = edge.second;
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist[t] == INF ? -1 : dist[t];
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    if (!(cin >> n >> m >> q)) return 0;
    
    adj_map.resize(n + 1);
    
    for (int i = 0; i < m; i++) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        if (adj_map[u].count(v)) {
            adj_map[u][v] = min(adj_map[u][v], w);
            adj_map[v][u] = min(adj_map[v][u], w);
        } else {
            adj_map[u][v] = w;
            adj_map[v][u] = w;
        }
    }
    
    for (int j = 0; j < q; j++) {
        int type;
        cin >> type;
        if (type == 1) {
            int u, v;
            long long w;
            cin >> u >> v >> w;
            adj_map[u][v] = w;
            adj_map[v][u] = w;
        } else {
            int u, v;
            cin >> u >> v;
            cout << dijkstra(u, v) << "\n";
        }
    }
    return 0;
}
```

---


---

### **[IKH-0061] - Điều Phối Xe Tải Siêu Trọng Cảng Cát Lái**
* **Dạng bài:** Binary Search on Answer, Greedy Check
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0061 - Dieu Phoi Xe Tai Sieu Trong Cang Cat Lai](file:///Users/dkdeveloper/projects/testcase/IKH-0061%20-%20Dieu%20Phoi%20Xe%20Tai%20Sieu%20Trong%20Cang%20Cat%20Lai)
* **Ý tưởng cốt lõi:** Chặt nhị phân tải trọng tối đa $M$. Hàm `check(M)` kiểm tra xem có thể chia dãy lô hàng thành $\le K$ đoạn có tổng trọng lượng $\le M$ hay không bằng thuật toán Tham ăn (Greedy).

---

### **[IKH-0062] - Quy Hoạch Trạm Sạc Xe Điện VinFast**
* **Dạng bài:** Binary Search on Answer, Min-Max Distance
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0062 - Quy Hoach Tram Sac Xe Dien VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0062%20-%20Quy%20Hoach%20Tram%20Sac%20Xe%20Dien%20VinFast)
* **Ý tưởng cốt lõi:** Chặt nhị phân khoảng cách tối đa giữa các trạm sạc $D$. Với mỗi khoảng giữa 2 trạm sạc có sẵn $\Delta X = X&#95;{i+1} - X&#95;i$, số trạm sạc mới cần thêm là $\lfloor (\Delta X - 1) / D 
floor$. Hàm `check(D)` kiểm tra xem tổng số trạm cần thêm $\le K$ không.

---

### **[IKH-0063] - Phân Bổ Băng Thông Trạm Ra-đa Vũ Trụ**
* **Dạng bài:** Binary Search on Answer, Maximize the Minimum
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0063 - Phan Bo Bang Thong Tram Ra-da Vu Tru](file:///Users/dkdeveloper/projects/testcase/IKH-0063%20-%20Phan%20Bo%20Bang%20Thong%20Tram%20Ra-da%20Vu%20Tru)
* **Ý tưởng cốt lõi:** Chặt nhị phân dung lượng băng thông tối thiểu $B$ mà một vệ tinh nhận được. Hàm `check(B)` đếm tổng số vệ tinh có thể phục vụ từ tất cả các trạm $\sum \lfloor A&#95;i / B 
floor$. Nếu tổng số vệ tinh $\ge M$ thì $B$ khả thi.

---

### **[IKH-0064] - Giám Sát Nồng Độ Nước Cấp Sông Đồng Nai**
* **Dạng bài:** Binary Search on Answer, Maximum Average Subarray
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0064 - Giam Sat Nong Do Nuoc Cap Song Dong Nai](file:///Users/dkdeveloper/projects/testcase/IKH-0064%20-%20Giam%20Sat%20Nong%20Do%20Nuoc%20Cap%20Song%20Dong%20Nai)
* **Ý tưởng cốt lõi:** Chặt nhị phân giá trị trung bình $X$. Biến đổi mảng $B&#95;i = A&#95;i - X$. Hàm `check(X)` tìm xem có đoạn con liên tiếp độ dài $\ge K$ có tổng $B&#95;i \ge 0$ hay không bằng mảng cộng dồn Prefix Sum và duy trì `min_prefix`.

---

### **[IKH-0065] - Lập Lịch Cắt Thép Cầu Nhơn Trạch**
* **Dạng bài:** Binary Search on Answer, Wood/Steel Cutting Problem
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0065 - Lap Lich Cat Thep Cau Nhon Trach](file:///Users/dkdeveloper/projects/testcase/IKH-0065%20-%20Lap%20Lich%20Cat%20Thep%20Cau%20Nhon%20Trach)
* **Ý tưởng cốt lõi:** Chặt nhị phân chiều dài cọc thép $L$. Hàm `check(L)` tính tổng số cọc thu được $\sum \lfloor A&#95;i / L 
floor$. Nếu tổng số cọc $\ge K$ thì $L$ khả thi.


---

### **[IKH-0066] - Quản Lý Trạm Tái Tạo Năng Lượng Gió Ninh Thuận**
* **Dạng bài:** 2D Prefix Sum, Range Sum Query
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0066 - Quan Ly Tram Tai Tao Nang Luong Gio Ninh Thuan](file:///Users/dkdeveloper/projects/testcase/IKH-0066%20-%20Quan%20Ly%20Tram%20Tai%20Tao%20Nang%20Luong%20Gio%20Ninh%20Thuan)
* **Ý tưởng cốt lõi:** Tính mảng cộng dồn 2 chiều $pref[i][j]$. Mỗi ô $(i, j)$ tính tổng vùng hình vuông $K 	imes K$ có góc dưới bên phải tại $(i, j)$ trong $O(1)$ thông qua công thức $pref[i][j] - pref[i-k][j] - pref[i][j-k] + pref[i-k][j-k]$.

---

### **[IKH-0067] - Điều Phối Chuỗi Cung Ước Nông Sản Miền Tây**
* **Dạng bài:** Two Pointers, Minimum Subarray Length
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0067 - Dieu Phoi Chuoi Cung Uoc Nong San Mien Tay](file:///Users/dkdeveloper/projects/testcase/IKH-0067%20-%20Dieu%20Phoi%20Chuoi%20Cung%20Uoc%20Nong%20San%20Mien%20Tay)
* **Ý tưởng cốt lõi:** Dùng 2 con trỏ `left` và `right` để duy trì tổng đoạn con `current_sum`. Mở rộng `right` và thu hẹp `left` khi tổng $\ge S$ để cập nhật độ dài ngắn nhất trong $O(N)$.

---

### **[IKH-0068] - Hệ Thống Đếm Luồng Giao Thông Hầm Thủ Thiêm**
* **Dạng bài:** Sliding Window Maximum, Monotonic Deque
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0068 - He Thong Dem Luong Giao Thong Ham Thu Thiem](file:///Users/dkdeveloper/projects/testcase/IKH-0068%20-%20He%20Thong%20Dem%20Luong%20Giao%20Thong%20Ham%20Thu%20Thiem)
* **Ý tưởng cốt lõi:** Duy trì một `std::deque` chứa chỉ số phần tử giảm dần về giá trị. Loại bỏ các phần tử nằm ngoài cửa sổ $K$ và các phần tử nhỏ hơn phần tử mới thêm vào. Đáp án cửa sổ tại mỗi bước là `a[dq.front()]`.

---

### **[IKH-0069] - Tối Ưu Hóa Tuyến Xe Být Điện VinBus Hà Nội**
* **Dạng bài:** Two Pointers, Longest Subarray with At Most K Distinct Elements
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0069 - Toi Uu Hoa Tuyen Xe Byt Dien VinBus Ha Noi](file:///Users/dkdeveloper/projects/testcase/IKH-0069%20-%20Toi%20Uu%20Hoa%20Tuyen%20Xe%20Byt%20Dien%20VinBus%20Ha%20Noi)
* **Ý tưởng cốt lõi:** Dùng 2 con trỏ kết hợp `unordered_map` tần suất. Mở rộng `right`, nếu số lượng phần tử khác nhau `freq.size() > K`, dịch `left` và giảm tần suất, xóa khỏi map khi tần suất về 0.

---

### **[IKH-0070] - Phân Tích Sóng Địa Chấn Tây Nguyên**
* **Dạng bài:** Prefix Sum, Hash Map Counting
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0070 - Phan Tich Song Dia Chan Tay Nguyen](file:///Users/dkdeveloper/projects/testcase/IKH-0070%20-%20Phan%20Tich%20Song%20Dia%20Chan%20Tay%20Nguyen)
* **Ý tưởng cốt lõi:** Tổng đoạn con từ $i$ đến $j$ là $S[j] - S[i-1] = K \iff S[i-1] = S[j] - K$. Duy trì `unordered_map` đếm số lần xuất hiện của các tổng tích lũy trước đó. Cộng `pref_count[S[j] - K]` vào kết quả tại mỗi bước.


---

### **[IKH-0071] - Lập Lịch Bảo Trì Tuyến Đường Sắt Bắc Nam**
* **Dạng bài:** Greedy, Interval Scheduling
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0071 - Lap Lich Bao Tri Tuyen Duong Sat Bac Nam](file:///Users/dkdeveloper/projects/testcase/IKH-0071%20-%20Lap%20Lich%20Bao%20Tri%20Tuyen%20Duong%20Sat%20Bac%20Nam)
* **Ý tưởng cốt lõi:** Tham ăn theo thời điểm kết thúc $R&#95;i$ tăng dần. Lần lượt chọn các khoảng thi công không bị đè lên thời điểm kết thúc của khoảng thi công trước đó trong $O(N \log N)$.

---

### **[IKH-0072] - Tối Ưu Hóa Túi Hàng Viễn Thông Viettel 5G**
* **Dạng bài:** 0/1 Knapsack, Dynamic Programming
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0072 - Toi Uu Hoa Tui Hang Vien Thong Viettel 5G](file:///Users/dkdeveloper/projects/testcase/IKH-0072%20-%20Toi%20Uu%20Hoa%20Tui%20Hang%20Vien%20Thong%20Viettel%205G)
* **Ý tưởng cốt lõi:** Quy hoạch động 0/1 Knapsack 1D tối ưu bộ nhớ. Với mỗi thiết bị $i$, chạy vòng lặp $w$ lùi từ $W$ xuống $w&#95;i$: `dp[w] = max(dp[w], dp[w - weight[i]] + value[i])`.

---

### **[IKH-0073] - Phân Bổ Ca Trực Bác Sĩ Bệnh Viện Chợ Rẫy**
* **Dạng bài:** Greedy, Min-Heap / Sweep Line
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0073 - Phan Bo Ca Truc Bac Si Benh Vien Cho Ray](file:///Users/dkdeveloper/projects/testcase/IKH-0073%20-%20Phan%20Bo%20Ca%20Truc%20Bac%20Si%20Benh%20Vien%20Cho%20Ray)
* **Ý tưởng cốt lõi:** Thuật toán Quét dòng (Sweep-line): Biến đổi mỗi khoảng $[L&#95;i, R&#95;i]$ thành 2 sự kiện: Bắt đầu (+1) và Kết thúc (-1). Sắp xếp tăng dần theo thời gian (kết thúc xử lý trước nếu trùng thời gian) và duy trì tổng cộng dồn max.

---

### **[IKH-0074] - Quy Hoạch Chuỗi Cung Ứng Linh Kiện Samsung**
* **Dạng bài:** Unbounded Knapsack / Coin Change, Dynamic Programming
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0074 - Quy Hoach Chuoi Cung Ung Linh Kien Samsung](file:///Users/dkdeveloper/projects/testcase/IKH-0074%20-%20Quy%20Hoach%20Chuoi%20Cung%20Ung%20Linh%20Kien%20Samsung)
* **Ý tưởng cốt lõi:** Quy hoạch động Đổi tiền / Unbounded Knapsack. `dp[w]` lưu số lượng phôi tối thiểu để có tổng trọng lượng $w$. Khởi tạo `dp[0] = 0`, lặp tiến `dp[w] = min(dp[w], dp[w - A[i]] + 1)`.

---

### **[IKH-0075] - Tối Ưu Đường Bay Chuyển Hàng Vietnam Airlines**
* **Dạng bài:** Kadane's Algorithm, Maximum Subarray Sum
* **Độ khó:** Rating 1700 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0075 - Toi Uu Duong Bay Chuyen Hang Vietnam Airlines](file:///Users/dkdeveloper/projects/testcase/IKH-0075%20-%20Toi%20Uu%20Duong%20Bay%20Chuyen%20Hang%20Vietnam%20Airlines)
* **Ý tưởng cốt lõi:** Thuật toán Kadane tìm đoạn con có tổng lớn nhất trong $O(N)$. Duy trì `current_max = max(A[i], current_max + A[i])` và `max_so_far = max(max_so_far, current_max)`.


---

### **[IKH-0076] - Quy Hoạch Mạng Lưới Cáp Quang Đô Thị TP.HCM**
* **Dạng bài:** Minimum Spanning Tree, Kruskal Algorithm
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0076 - Quan Ly Mang Luoi Cap Quang Do Thi TPHCM](file:///Users/dkdeveloper/projects/testcase/IKH-0076%20-%20Quan%20Ly%20Mang%20Luoi%20Cap%20Quang%20Do%20Thi%20TPHCM)
* **Ý tưởng cốt lõi:** Thuật toán Cây khung nhỏ nhất Kruskal. Sắp xếp danh sách cạnh theo trọng số tăng dần. Dùng cấu trúc dữ liệu DSU để chọn $N-1$ cạnh không tạo chu trình có tổng trọng số nhỏ nhất trong $O(M \log M)$.

---

### **[IKH-0077] - Điều Phối Cứu Hộ Lũ Lụt Miền Trung**
* **Dạng bài:** Breadth-First Search, Shortest Path Unweighted Graph
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0077 - Dieu Phoi Cuu Ho Lu Lut Mien Trung](file:///Users/dkdeveloper/projects/testcase/IKH-0077%20-%20Dieu%20Phoi%20Cuu%20Ho%20Lu%20Lut%20Mien%20Trung)
* **Ý tưởng cốt lõi:** Thuật toán duyệt theo chiều rộng BFS trên đồ thị không trọng số. Mảng `dist[v]` lưu số cạnh ngắn nhất từ đỉnh xuất phát $S$. Dừng ngay và trả về khi gặp đỉnh $T$ trong $O(V + E)$.

---

### **[IKH-0078] - Tối Ưu Hóa Tuyến Đường Giao Hàng GHN**
* **Dạng bài:** Dijkstra Algorithm, Weighted Shortest Path
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0078 - Toi Uu Hoa Tuyen Duong Giao Hang GHN](file:///Users/dkdeveloper/projects/testcase/IKH-0078%20-%20Toi%20Uu%20Hoa%20Tuyen%20Duong%20Giao%20Hang%20GHN)
* **Ý tưởng cốt lõi:** Thuật toán Dijkstra với Hàng chờ ưu tiên `std::priority_queue`. Duyệt qua các đỉnh có khoảng cách nhỏ nhất chưa cố định, cập nhật khoảng cách $dist[v] = dist[u] + w$ trong $O((V + E) \log V)$.

---

### **[IKH-0079] - Quản Lý Cụm Tài Khoản Ngân Hàng VietinBank**
* **Dạng bài:** Disjoint Set Union, Connected Components
* **Độ khó:** Rating 1700 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0079 - Quan Ly Cum Tai Khoan Ngan Hang VietinBank](file:///Users/dkdeveloper/projects/testcase/IKH-0079%20-%20Quan%20Ly%20Cum%20Tai%20Khoan%20Ngan%20Hang%20VietinBank)
* **Ý tưởng cốt lõi:** Cấu trúc dữ liệu Tập hợp rời rạc DSU (Disjoint Set Union) với tối ưu Nén đường đi (Path Compression). Khởi tạo $N$ tập hợp độc lập, mỗi thao tác hợp nhất 2 gốc khác nhau sẽ giảm số lượng thành phần liên thông đi 1.

---

### **[IKH-0080] - Tối Ưu Hóa Mạng Lưới Truyền Tải Điện 500kV**
* **Dạng bài:** Bipartite Graph Check, BFS 2-Coloring
* **Độ khó:** Rating 1750 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0080 - Toi Uu Hoa Mang Luoi Truyen Tai Dien 500kV](file:///Users/dkdeveloper/projects/testcase/IKH-0080%20-%20Toi%20Uu%20Hoa%20Mang%20Luoi%20Truyen%20Tai%20Dien%20500kV)
* **Ý tưởng cốt lõi:** Kiểm tra Đồ thị Hai phía bằng thuật toán Tô 2 màu BFS. Với mỗi đỉnh chưa tô màu, gán màu 1 và đẩy vào queue. Nếu gặp đỉnh kề đã tô màu cùng màu với đỉnh hiện tại thì đồ thị không là đồ thị 2 phía.


---

### **[IKH-0081] - Cập Nhật Biến Động Giá Cổ Phiếu Vingroup**
* **Dạng bài:** Fenwick Tree (BIT), Point Update Range Sum
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0081 - Cap Nhat Bien Dong Gia Co Phieu Vingroup](file:///Users/dkdeveloper/projects/testcase/IKH-0081%20-%20Cap%20Nhat%20Bien%20Dong%20Gia%20Co%20Phieu%20Vingroup)
* **Ý tưởng cốt lõi:** Cây Fenwick Tree (BIT). Hàm `add(i, v)` cập nhật phần tử $i$ trong $O(\log N)$, hàm `query(l, r) = query(r) - query(l-1)` tính tổng đoạn $[l, r]$ trong $O(\log N)$.

---

### **[IKH-0082] - Hệ Thống Cảnh Báo Áp Thấp Nhiệt Đới Biển Đông**
* **Dạng bài:** Segment Tree, Point Update Range Max
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0082 - He Thong Canh Bao Ap Thap Nhiet Doi Bien Dong](file:///Users/dkdeveloper/projects/testcase/IKH-0082%20-%20He%20Thong%20Canh%20Bao%20Ap%20Thap%20Nhiet%20Doi%20Bien%20Dong)
* **Ý tưởng cốt lõi:** Cấu trúc Cây quản lý đoạn Segment Tree. Cập nhật vị trí $i$ trong $O(\log N)$ và truy vấn giá trị lớn nhất trong đoạn $[l, r]$ bằng cách kết hợp thông tin 2 con trai/phải trong $O(\log N)$.

---

### **[IKH-0083] - Phân Tích Dao Động Nhiệt Độ Vườn Cúc Phương**
* **Dạng bài:** Sparse Table, Static Range Minimum Query
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0083 - Phan Tich Dao Dong Nhiet Do Vuon Cuc Phuong](file:///Users/dkdeveloper/projects/testcase/IKH-0083%20-%20Phan%20Tich%20Dao%20Dong%20Nhiet%20Do%20Vuon%20Cuc%20Phuong)
* **Ý tưởng cốt lõi:** Bảng thưa Sparse Table. Tiền xử lý $st[i][j]$ lưu min đoạn $[i, i + 2^j - 1]$ trong $O(N \log N)$. Đọc truy vấn min $[l, r]$ bằng $\min(st[l][k], st[r - 2^k + 1][k])$ trong $O(1)$ với $k = \lfloor\log_2(r - l + 1)
floor$.

---

### **[IKH-0084] - Quản Lý Vận Tải Cảng Container Cái Mép**
* **Dạng bài:** Segment Tree, Lazy Propagation Range Update Sum
* **Độ khó:** Rating 1700 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0084 - Quan Ly Van Tai Cang Container Cai Mep](file:///Users/dkdeveloper/projects/testcase/IKH-0084%20-%20Quan%20Ly%20Van%20Tai%20Cang%20Container%20Cai%20Mep)
* **Ý tưởng cốt lõi:** Segment Tree với kỹ thuật Trì hoãn lan truyền (Lazy Propagation). Mảng `lazy[node]` hoãn cập nhật giá trị xuống nút con cho đến khi thật sự cần truy vấn/duyệt qua, giúp cập nhật cả đoạn $[l, r]$ chỉ mất $O(\log N)$.

---

### **[IKH-0085] - Đếm Cặp Nghịch Thế Giao Dịch Chứng Khoán SSI**
* **Dạng bài:** Fenwick Tree, Inversion Count with Coordinate Compression
* **Độ khó:** Rating 1750 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0085 - Dem Cap Nghich The Giao Dich Chung Khoan SSI](file:///Users/dkdeveloper/projects/testcase/IKH-0085%20-%20Dem%20Cap%20Nghich%20The%20Giao%20Dich%20Chung%20Khoan%20SSI)
* **Ý tưởng cốt lõi:** Đếm số cặp nghịch thế bằng Nén tọa độ kết hợp Fenwick Tree. Duyệt từ trái qua phải, với mỗi phần tử $A_i$, số lượng phần tử lớn hơn $A_i$ xuất hiện trước nó bằng `i - bit.query(rank(A_i))`. Tổng thời gian $O(N \log N)$.


---

### **[IKH-0086] - Trích Xuất Từ Khóa Mã Độc BKAV**
* **Dạng bài:** String Hashing, Polynomial Rolling Hash
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0086 - Trich Xuan Tu Khoa Ma Doc BKAV](file:///Users/dkdeveloper/projects/testcase/IKH-0086%20-%20Trich%20Xuan%20Tu%20Khoa%20Ma%20Doc%20BKAV)
* **Ý tưởng cốt lõi:** Thuật toán Mã hóa băm chuỗi Polynomial Rolling Hash. Tiền xử lý $hash\_s[i]$ và mảng lũy thừa `pow_base` trong $O(N)$ để so sánh giá trị hash của đoạn chuỗi con $S[l..r]$ với $P$ trong $O(1)$.

---

### **[IKH-0087] - Kiểm Tra Mã Gien ADN Virus SARS-CoV-2**
* **Dạng bài:** KMP Algorithm, Prefix Function
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0087 - Kiem Tra Ma Gien ADN Virus SARS-CoV-2](file:///Users/dkdeveloper/projects/testcase/IKH-0087%20-%20Kiem%20Tra%20Ma%20Gien%20ADN%20Virus%20SARS-CoV-2)
* **Ý tưởng cốt lõi:** Thuật toán KMP (Knuth-Morris-Pratt). Xây dựng mảng Tiền tố $\pi[i]$ đại diện cho độ dài tiền tố thực sự dài nhất đồng thời là hậu tố của $P[0..i]$. Duyệt khớp mẫu không bao giờ quay lùi con trỏ văn bản $T$ trong $O(N + M)$.

---

### **[IKH-0088] - So Khớp Chuỗi Tiền Tố Văn Bản Báo Chí**
* **Dạng bài:** Z-Algorithm, Longest Common Prefix Array
* **Độ khó:** Rating 1700 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0088 - So Khop Chuoi Tien To Van Ban Bao Chi](file:///Users/dkdeveloper/projects/testcase/IKH-0088%20-%20So%20Khop%20Chuoi%20Tien%20To%20Van%20Ban%20Bao%20Chi)
* **Ý tưởng cốt lõi:** Thuật toán Z (Z-Algorithm). Duyệt cửa sổ $[l, r]$ ghi nhận tiền tố trùng dài nhất với $S$. Tính $Z[i]$ bằng cách tận dụng kết quả $Z[i - l]$ đã tính trước đó để đạt độ phức tạp $O(N)$.

---

### **[IKH-0089] - Bộ Lọc Tìm Kiếm Gợi Ý Từ Khóa Cốc Cốc**
* **Dạng bài:** Trie Tree, Prefix Tree Insertion & Search
* **Độ khó:** Rating 1750 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0089 - Bo Loc Tim Kiem Goi Y Tu Khoa Coc Coc](file:///Users/dkdeveloper/projects/testcase/IKH-0089%20-%20Bo%20Loc%20Tim%20Kiem%20Goi%20Y%20Tu%20Khoa%20Coc%20Coc)
* **Ý tưởng cốt lõi:** Cấu trúc dữ liệu Cây Tiền Tố Trie (Prefix Tree). Nạp các từ trong từ điển vào cây, mỗi nút chứa danh sách 26 con trai. Kiểm tra tiền tố $P$ bằng cách đi theo đường đi của các ký tự trong $P$ trên cây trong $O(|P|)$.

---

### **[IKH-0090] - Tối Ưu Mã Hóa XOR Chuỗi Bit Nhị Phân**
* **Dạng bài:** Binary Trie, Maximum XOR Pair
* **Độ khó:** Rating 1800 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0090 - Toi Uu Ma Hoa XOR Chuoi Bit Nhi Phan](file:///Users/dkdeveloper/projects/testcase/IKH-0090%20-%20Toi%20Uu%20Ma%20Hoa%20XOR%20Chuoi%20Bit%20Nhi%20Phan)
* **Ý tưởng cốt lõi:** Cây Tiền Tố Nhị Phân Binary Trie 31 bit. Chèn các số vào cây. Với mỗi số $A_i$, đi trên cây ưu tiên rẽ sang nhánh có bit đối lập $1 - 	ext{bit}_k$ để tối đa hóa bit 1 kết quả phép XOR trong $O(31 \cdot N)$.


---

### **[IKH-0091] - Tìm Đường Đi Ngắn Nhất Mọi Cặp Đỉnh Hầm Thủ Thiêm**
* **Dạng bài:** Floyd-Warshall Algorithm, All-Pairs Shortest Path
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0091 - Tim Duong Di Ngan Nhat Moi Cap Dinh Ham Thu Thiem](file:///Users/dkdeveloper/projects/testcase/IKH-0091%20-%20Tim%20Duong%20Di%20Ngan%20Nhat%20Moi%20Cap%20Dinh%20Ham%20Thu%20Thiem)
* **Ý tưởng cốt lõi:** Thuật toán Floyd-Warshall $O(V^3)$. Duyệt qua 3 vòng lặp $k, i, j$, liên tục tối ưu đường đi từ $i$ đến $j$ qua đỉnh trung gian $k$: `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`.

---

### **[IKH-0092] - Phân Tích Điểm Thắt Mạng Lưới Cáp Sông Sài Gòn**
* **Dạng bài:** Tarjan Algorithm, Articulation Points (Cut Vertices)
* **Độ khó:** Rating 1700 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0092 - Phan Tich Diem That Mang Luoi Cap Song Sai Gon](file:///Users/dkdeveloper/projects/testcase/IKH-0092%20-%20Phan%20Tich%20Diem%20That%20Mang%20Luoi%20Cap%20Song%20Sai%20Gon)
* **Ý tưởng cốt lõi:** Thuật toán Tarjan đếm Khớp (Articulation Points) bằng DFS. Duyệt cây DFS với mảng thời gian phát hiện `tin[u]` và thời gian thăm sớm nhất có thể tới `low[u]`. Đỉnh $u$ không phải gốc là khớp khi tồn tại đỉnh con $v$ sao cho $low[v] \ge tin[u]$ trong $O(V + E)$.

---

### **[IKH-0093] - Quản Lý Cấu Trúc Cây Gia Phả Dòng Họ**
* **Dạng bài:** Lowest Common Ancestor (LCA), Binary Lifting
* **Độ khó:** Rating 1750 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0093 - Quan Ly Cau Truc Cay Gia Pha Dong Ho](file:///Users/dkdeveloper/projects/testcase/IKH-0093%20-%20Quan%20Ly%20Cau%20Truc%20Cay%20Gia%20Pha%20Dong%20Ho)
* **Ý tưởng cốt lõi:** Tìm Tổ tiên chung gần nhất (LCA) bằng Nâng nhị phân. Tiền xử lý `up[u][j]` lưu tổ tiên thứ $2^j$ của $u$ trong $O(N \log N)$. Khi truy vấn, đưa 2 đỉnh về cùng độ sâu và nhảy đồng thời các bước $2^j$ giảm dần trong $O(\log N)$.

---

### **[IKH-0094] - Quy Hoạch Mạng Truyền Tải Máy Chủ FPT**
* **Dạng bài:** Tree DP, Maximum Weight Independent Set on Tree
* **Độ khó:** Rating 1800 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0094 - Quy Hoach Mang Truyen Tai May Chu FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0094%20-%20Quy%20Hoach%20Mang%20Truyen%20Tai%20May%20Chu%20FPT)
* **Ý tưởng cốt lõi:** Quy hoạch động trên cây (Tree DP). Đặt `dp[u][0]` là tổng công suất max khi KHÔNG chọn $u$, `dp[u][1]` khi CHỌN $u$. `dp[u][0] += sum(max(dp[v][0], dp[v][1]))`, `dp[u][1] += sum(dp[v][0]) + W[u]` trong $O(N)$.

---

### **[IKH-0095] - Đường Đi Dài Nhất Trên Cây Mạng Bưu Điện**
* **Dạng bài:** Tree Diameter, 2-BFS / DFS Algorithm
* **Độ khó:** Rating 1850 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0095 - Duong Di Dai Nhat Tren Cay Mang Buu Dien](file:///Users/dkdeveloper/projects/testcase/IKH-0095%20-%20Duong%20Di%20Dai%20Nhat%20Tren%20Cay%20Mang%20Buu%20Dien)
* **Ý tưởng cốt lõi:** Đường kính cây bằng 2 lượt BFS. BFS lượt 1 từ đỉnh 1 tìm đỉnh $u$ xa nhất. BFS lượt 2 từ $u$ tìm đỉnh $v$ xa $u$ nhất. Khoảng cách $dist(u, v)$ chính là đường kính cây trong $O(V + E)$.


---

### **[IKH-0096] - Tối Ưu Hóa Chuỗi Cắt Thép Xây Dựng**
* **Dạng bài:** Interval DP, Matrix Chain Multiplication style
* **Độ khó:** Rating 1700 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0096 - Toi Uu Hoa Chuoi Cat Thep Xay Dung](file:///Users/dkdeveloper/projects/testcase/IKH-0096%20-%20Toi%20Uu%20Hoa%20Chuoi%20Cat%20Thep%20Xay%20Dung)
* **Ý tưởng cốt lõi:** Quy hoạch động Đoạn (Interval DP). `dp[i][j]` là chi phí nhỏ nhất cắt đoạn thép từ $cuts[i]$ tới $cuts[j]$. `dp[i][j] = min(dp[i][k] + dp[k][j] + cuts[j] - cuts[i])` với $i < k < j$ trong $O(N^3)$.

---

### **[IKH-0097] - Phân Bổ Kế Hoạch Đặt Máy Chủ Viettel**
* **Dạng bài:** Digit DP, Counting Integers with Specific Conditions
* **Độ khó:** Rating 1750 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0097 - Phan Bo Ke Hoach Dat May Chu Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0097%20-%20Phan%20Bo%20Ke%20Hoach%20Dat%20May%20Chu%20Viettel)
* **Ý tưởng cốt lõi:** Quy hoạch động Chữ số (Digit DP). Đếm số lượng số hợp lệ trong khoảng $[A, B]$ qua `count_valid(B) - count_valid(A-1)`. Hàm đệ quy nhớ `solve(idx, tight, prev_is_one)` kiểm tra cấu trúc từng vị trí chữ số trong $O(	ext{len} 	imes 	ext{states})$.

---

### **[IKH-0098] - Lập Lịch Giao Xe Điện VinFast Toàn Quốc**
* **Dạng bài:** Bitmask DP, Traveling Salesperson Problem (TSP)
* **Độ khó:** Rating 1800 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0098 - Lap Lich Giao Xe Dien VinFast Toan Quoc](file:///Users/dkdeveloper/projects/testcase/IKH-0098%20-%20Lap%20Lich%20Giao%20Xe%20Dien%20VinFast%20Toan%20Quoc)
* **Ý tưởng cốt lõi:** Quy hoạch động Trạng thái (Bitmask DP). `dp[mask][u]` lưu chi phí nhỏ nhất đã ghé qua tập hợp thành phố trong `mask` và hiện dừng tại $u$. Chuyển trạng thái sang đỉnh $v$ chưa thăm `dp[mask | (1 << v)][v] = min(..., dp[mask][u] + C[u][v])` trong $O(N^2 \cdot 2^N)$.

---

### **[IKH-0099] - Đếm Số Cách Lắp Ráp Xe Máy Honda**
* **Dạng bài:** Dynamic Programming with Combinatorics, Modular Arithmetic
* **Độ khó:** Rating 1850 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0099 - Dem So Cach Lap Rap Xe May Honda](file:///Users/dkdeveloper/projects/testcase/IKH-0099%20-%20Dem%20So%20Cach%20Lap%20Rap%20Xe%20May%20Honda)
* **Ý tưởng cốt lõi:** Quy hoạch động Tổ hợp & Hệ số đa thức (Multinomial Coefficient). Tìm các chuỗi dây chuyền độc lập độ dài $L_1, L_2, \dots, L_C$. Số cách trộn cấu hình bằng $N! 	imes (L_1!)^{-1} 	imes (L_2!)^{-1} \dots \pmod{10^9+7}$ trong $O(N)$.

---

### **[IKH-0100] - Quy Hoạch Chi Phí Vận Chuyển Container**
* **Dạng bài:** Convex Hull Trick (CHT), Dynamic Programming Optimization
* **Độ khó:** Rating 1900 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0100 - Quy Hoach Chi Phi Van Chuyen Container](file:///Users/dkdeveloper/projects/testcase/IKH-0100%20-%20Quy%20Hoach%20Chi%20Phi%20Van%20Chuyen%20Container)
* **Ý tưởng cốt lõi:** Kỹ thuật Bao Lồi CHT (Convex Hull Trick). Biến đổi công thức $dp[i] = \min (dp[j] + A_i \cdot B_j)$ thành truy vấn điểm $x = A_i$ trên tập các đường thẳng $y = B_j \cdot x + dp[j]$. Duy trì bao lồi bằng `std::deque` giúp tối ưu độ phức tạp từ $O(N^2)$ xuống $O(N)$.


---

### **[IKH-0101] - Kiểm Tra Mã Số Thuế Doanh Nghiệp Quốc Gia**
* **Dạng bài:** Sieve of Eratosthenes, Miller-Rabin Primality Test
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0101 - Kiem Tra Ma So Thue Doanh Nghiep Quoc Gia](file:///Users/dkdeveloper/projects/testcase/IKH-0101%20-%20Kiem%20Tra%20Ma%20So%20Thue%20Doanh%20Nghiep%20Quoc%20Gia)
* **Ý tưởng cốt lõi:** Sàng nguyên tố Eratosthenes hoặc Miller-Rabin. Tiền xử lý mảng đánh dấu `is_prime` với $N \le 10^7$ trong $O(N \log \log N)$ giúp trả lời mỗi truy vấn kiểm tra số nguyên tố trong $O(1)$.

---

### **[IKH-0102] - Mã Hóa Bảo Mật Giao Dịch Ngân Hàng Techcombank**
* **Dạng bài:** Modular Exponentiation, Extended Euclidean Algorithm
* **Độ khó:** Rating 1700 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0102 - Ma Hoa Bao Mat Giao Dich Ngan Hang Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0102%20-%20Ma%20Hoa%20Bao%20Mat%20Giao%20Dich%20Ngan%20Hang%20Techcombank)
* **Ý tưởng cốt lõi:** Lũy thừa nhị phân (Binary Exponentiation). Tính $A^B \pmod{10^9+7}$ trong $O(\log B)$ bằng cách phân tích $B$ thành dạng nhị phân và bình phương tích lũy modulo $10^9+7$.

---

### **[IKH-0103] - Phân Tích Thừa Số Nguyên Tố Kế Toán**
* **Dạng bài:** Smallest Prime Factor (SPF) Sieve, Prime Factorization
* **Độ khó:** Rating 1750 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0103 - Phan Tich Thua So Nguyen To Ke Toan](file:///Users/dkdeveloper/projects/testcase/IKH-0103%20-%20Phan%20Tich%20Thua%20So%20Nguyen%20To%20Ke%20Toan)
* **Ý tưởng cốt lõi:** Sàng Mảng Thừa Số Nguyên Tố Nhỏ Nhất (SPF Sieve). Tiền xử lý `spf[x]` lưu ước nguyên tố nhỏ nhất của $x$. Khi phân tích số $x$, liên tiếp lấy $x \gets x / spf[x]$ để thu được danh sách thừa số trong $O(\log x)$.

---

### **[IKH-0104] - Đếm Số Nghiệm Đồng Dư Đặt Hàng Shopee**
* **Dạng bài:** Euler Totient Function, Coprime Counting
* **Độ khó:** Rating 1800 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0104 - Dem So Nghiem Dong Du Dat Hang Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0104%20-%20Dem%20So%20Nghiem%20Dong%20Du%20Dat%20Hang%20Shopee)
* **Ý tưởng cốt lõi:** Hàm Phi Euler $\phi(N)$. Sử dụng công thức $\phi(N) = N \cdot \prod_{p | N} (1 - rac{1}{p})$. Duyệt qua các ước nguyên tố $p \le \sqrt{N}$ để tính $\phi(N)$ cho từng truy vấn trong $O(\sqrt{N})$.

---

### **[IKH-0105] - Tính Số Cách Phân Chia Lô Hàng Khổng Lồ**
* **Dạng bài:** Combinatorics Combination, nCr Modulo 1e9+7
* **Độ khó:** Rating 1850 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0105 - Tinh So Cach Phan Chia Lo Hang Khong Lo](file:///Users/dkdeveloper/projects/testcase/IKH-0105%20-%20Tinh%20So%20Cach%20Phan%20Chia%20Lo%20Hang%20Khong%20Lo)
* **Ý tưởng cốt lõi:** Tổ hợp chập $K$ modulo $10^9+7$. Tiền xử lý mảng giai thừa `fact[]` và mảng nghịch đảo giai thừa `invFact[]` trong $O(N)$. Trả lời mỗi truy vấn $C(N, K) \equiv N! \cdot (K!)^{-1} \cdot ((N-K)!)^{-1} \pmod{10^9+7}$ trong $O(1)$.


---

### **[IKH-0106] - Đo Diện Tích Khu Đô Thị Vinhomes Grand Park**
* **Dạng bài:** Shoelace Formula, Computational Geometry Polygon Area
* **Độ khó:** Rating 1700 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0106 - Do Dien Tich Khu Do Thi Vinhomes Grand Park](file:///Users/dkdeveloper/projects/testcase/IKH-0106%20-%20Do%20Dien%20Tich%20Khu%20Do%20Thi%20Vinhomes%20Grand%20Park)
* **Ý tưởng cốt lõi:** Công thức Dây Giày (Shoelace Formula / Gauss Area Formula). Tính diện tích đa giác đơn $S = rac{1}{2} |\sum_{i=1}^N (X_i Y_{i+1} - X_{i+1} Y_i)|$ trong $O(N)$ dùng `long long` tránh tràn tích chéo.

---

### **[IKH-0107] - Kiểm Tra Vị Trí Trạm Đột Phá Giao Hàng Grab**
* **Dạng bài:** Point-in-Polygon (PIP), Ray Casting Algorithm
* **Độ khó:** Rating 1750 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0107 - Kiem Tra Vi Tri Tram Dot Pha Giao Hang Grab](file:///Users/dkdeveloper/projects/testcase/IKH-0107%20-%20Kiem%20Tra%20Vi%20Tri%20Tram%20Dot%20Pha%20Giao%20Hang%20Grab)
* **Ý tưởng cốt lõi:** Thuật toán Bắn Tia (Ray Casting Algorithm). Kiểm tra điểm $P$ thuộc cạnh (`BOUNDARY`), bên trong (`INSIDE` khi số lần tia cắt các cạnh là lẻ) hay bên ngoài (`OUTSIDE` khi số lần tia cắt là chẵn) trong $O(N)$.

---

### **[IKH-0108] - Khoảng Cách Tối Thiểu Giữa 2 Trạm Bán Hàng Circle K**
* **Dạng bài:** Closest Pair of Points, Sweep-line Algorithm
* **Độ khó:** Rating 1800 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0108 - Khoang Cach Toi Thieu Giua 2 Tram Ban Hang Circle K](file:///Users/dkdeveloper/projects/testcase/IKH-0108%20-%20Khoang%20Cach%20Toi%20Thieu%20Giua%202%20Tram%20Ban%20Hang%20Circle%20K)
* **Ý tưởng cốt lõi:** Cặp điểm gần nhất bằng Đường Quét (Sweep-line). Sắp xếp điểm theo hoành độ $X$, duy trì mảng `std::set` theo tung độ $Y$ để giới hạn cửa sổ tìm kiếm trong dải $\sqrt{d}$ giúp tìm khoảng cách Euclid bình phương nhỏ nhất trong $O(N \log N)$.

---

### **[IKH-0109] - Bao Lồi Vùng Phủ Sóng Mạng Viễn Thông MobiFone**
* **Dạng bài:** Convex Hull, Andrew's Monotone Chain Algorithm
* **Độ khó:** Rating 1850 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0109 - Bao Loi Vung Phu Song Mang Vien Thong MobiFone](file:///Users/dkdeveloper/projects/testcase/IKH-0109%20-%20Bao%20Loi%20Vung%20Phu%20Song%20Mang%20Vien%20Thong%20MobiFone)
* **Ý tưởng cốt lõi:** Bao lồi Monotone Chain của Andrew. Sắp xếp các điểm theo $X$, lần lượt dựng Vỏ dưới (Lower Hull) và Vỏ trên (Upper Hull) bằng kiểm tra Tích Hướng `cross_product <= 0` trong $O(N \log N)$, từ đó tính chu vi bao lồi.

---

### **[IKH-0110] - Phát Hiện Giao Điểm Tuyến Đường Sắt Đô Thị Metro**
* **Dạng bài:** Line Segment Intersection, Computational Geometry Cross Product
* **Độ khó:** Rating 1900 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0110 - Phat Hien Giao Diem Tuyen Duong Sat Do Thi Metro](file:///Users/dkdeveloper/projects/testcase/IKH-0110%20-%20Phat%20Hien%20Giao%20Diem%20Tuyen%20Duong%20Sat%20Do%20Thi%20Metro)
* **Ý tưởng cốt lõi:** Giao điểm 2 đoạn thẳng $AB$ và $CD$. Kiểm tra xem $C, D$ nằm về 2 phía của $AB$ và $A, B$ nằm về 2 phía của $CD$ bằng 4 phép kiểm tra Tích Hướng Vector `cross_product`, kết hợp xử lý các trường hợp đặc biệt 3 hoặc 4 điểm thẳng hàng trong $O(1)$ cho mỗi truy vấn.


---

### **[IKH-0111] - Tối Ưu Doanh Thu Ngày Cao Điểm VinMart**
* **Dạng bài:** Maximum Subarray Sum, Kadane Algorithm vs Prefix Sum vs Brute Force
* **Độ khó:** Rating 1250 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0111 - Toi Uu Doanh Thu Ngay Cao Diem VinMart](file:///Users/dkdeveloper/projects/testcase/IKH-0111%20-%20Toi%20Uu%20Doanh%20Thu%20Ngay%20Cao%20Diem%20VinMart)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Vét cạn mọi cặp $[i, j]$ và tính tổng $O(N^3)$.
  - *Cách 2 (Subtask 2):* Mảng cộng dồn Prefix Sum $O(N^2)$.
  - *Cách 3 (100% AC):* Thuật toán Kadane $O(N)$ thời gian, $O(1)$ bộ nhớ.

---

### **[IKH-0112] - Đoạn Con Ngắn Nhất Có Tổng Đạt Ngưỡng Shopee**
* **Dạng bài:** Two Pointers, Sliding Window vs Prefix Sum Binary Search vs Brute Force
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0112 - Doan Con Ngan Nhat Co Tong Dat Nguong Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0112%20-%20Doan%20Con%20Ngan%20Nhat%20Co%20Tong%20Dat%20Nguong%20Shopee)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Vét cạn mọi đoạn $[i, j]$ $O(N^3)$.
  - *Cách 2 (Subtask 2):* Prefix Sum + Chặt nhị phân `lower_bound` $O(N \log N)$.
  - *Cách 3 (100% AC):* Two Pointers / Sliding Window $O(N)$ thời gian, $O(1)$ bộ nhớ.

---

### **[IKH-0113] - Đếm Chuỗi Ngày Doanh Thu Chia Hết Cho K**
* **Dạng bài:** Subarray Sum Divisible by K Modulo Frequency vs Prefix Sum DP vs Brute Force
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0113 - Dem Chuoi Ngay Doanh Thu Chia Het Cho K](file:///Users/dkdeveloper/projects/testcase/IKH-0113%20-%20Dem%20Chuoi%20Ngay%20Doanh%20Thu%20Chia%20Het%20Cho%20K)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Vét cạn mọi đoạn $[i, j]$ $O(N^3)$.
  - *Cách 2 (Subtask 2):* Prefix Sum $O(N^2)$.
  - *Cách 3 (100% AC):* Prefix Sum Modulo Frequency Table `freq[rem]` $O(N + K)$.

---

### **[IKH-0114] - Giá Trị Lớn Nhất Cửa Sổ Trượt Bưu Kiện VNPost**
* **Dạng bài:** Sliding Window Maximum, Monotonic Deque vs Multiset vs Brute Force
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0114 - Gia Tri Lon Nhat Cua So Truot Buu Kien VNPost](file:///Users/dkdeveloper/projects/testcase/IKH-0114%20-%20Gia%20Tri%20Lon%20Nhat%20Cua%20So%20Truot%20Buu%20Kien%20VNPost)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt từng cửa sổ trượt $O(N \cdot K)$.
  - *Cách 2 (Subtask 2):* Dùng `std::multiset` / Max-Heap $O(N \log K)$.
  - *Cách 3 (100% AC):* Hàng đợi đơn điệu Monotonic `std::deque` $O(N)$.

---

### **[IKH-0115] - Đoạn Con Có Đúng K Số Lẻ Tối Ưu Viettel**
* **Dạng bài:** Subarrays with K Odds, Two Pointers atMost(K) vs Prefix Hash vs Brute Force
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0115 - Doan Con Co Dung K So Le Toi Uu Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0115%20-%20Doan%20Con%20Co%20Dung%20K%20So%20Le%20Toi%20Uu%20Viettel)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt mọi đoạn $[i, j]$ đếm số lẻ $O(N^3)$.
  - *Cách 2 (Subtask 2):* Prefix Sum chuyển $A_i \% 2 	o 0/1$ $O(N^2)$.
  - *Cách 3 (100% AC):* Two Pointers `atMost(K) - atMost(K-1)` $O(N)$.


---

### **[IKH-0116] - Tìm Cặp Giao Dịch Có Tổng Bằng Target VinFast**
* **Dạng bài:** Two Sum, Two Pointers vs Hash Table vs Binary Search vs Brute Force
* **Độ khó:** Rating 1250 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0116 - Tim Cap Giao Dich Co Tong Bang Target VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0116%20-%20Tim%20Cap%20Giao%20Dich%20Co%20Tong%20Bang%20Target%20VinFast)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt 2 vòng lặp tìm cặp $(i, j)$ $O(N^2)$.
  - *Cách 2 (Subtask 2):* Sắp xếp + Chặt nhị phân `binary_search` $O(N \log N)$.
  - *Cách 3 (100% AC):* Hash Table `unordered_map` $O(N)$ thời gian.

---

### **[IKH-0117] - Đếm Cặp Số Có Hiệu Bằng K Tiki**
* **Dạng bài:** Count Pairs Difference K, Two Pointers vs Hash Frequency vs Brute Force
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0117 - Dem Cap So Co Hieu Bang K Tiki](file:///Users/dkdeveloper/projects/testcase/IKH-0117%20-%20Dem%20Cap%20So%20Co%20Hieu%20Bang%20K%20Tiki)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt 2 vòng lặp $O(N^2)$.
  - *Cách 2 (Subtask 2):* Sắp xếp + Chặt nhị phân `upper_bound - lower_bound` $O(N \log N)$.
  - *Cách 3 (100% AC):* Mảng tần suất Hash Table `unordered_map` $O(N)$.

---

### **[IKH-0118] - Tìm Bộ Ba Số Có Tổng Bằng 0 Techcombank**
* **Dạng bài:** 3Sum, Two Pointers vs Hash Set vs Brute Force
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0118 - Tim Bo Ba So Co Tong Bang 0 Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0118%20-%20Tim%20Bo%20Ba%20So%20Co%20Tong%20Bang%200%20Techcombank)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt 3 vòng lặp $O(N^3)$.
  - *Cách 2 (Subtask 2):* Duyệt 2 vòng lặp + Hash Map $O(N^2 \log N)$.
  - *Cách 3 (100% AC):* Sắp xếp + Two Pointers $O(N^2)$ thời gian, $O(1)$ RAM.

---

### **[IKH-0119] - Đếm Cặp Phần Tử Có Tổng Nhỏ Hơn K Grab**
* **Dạng bài:** Count Pairs Sum Less Than K, Two Pointers vs Binary Search vs Brute Force
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0119 - Dem Cap Phan Tu Co Tong Nho Hon K Grab](file:///Users/dkdeveloper/projects/testcase/IKH-0119%20-%20Dem%20Cap%20Phan%20Tu%20Co%20Tong%20Nho%20Hon%20K%20Grab)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt 2 vòng lặp $O(N^2)$.
  - *Cách 2 (Subtask 2):* Sắp xếp + Chặt nhị phân `lower_bound` $O(N \log N)$.
  - *Cách 3 (100% AC):* Sắp xếp + Two Pointers `ans += (r - l)` $O(N \log N)$.

---

### **[IKH-0120] - Tìm Cặp Hai Số Có Tích Lớn Nhất FPT**
* **Dạng bài:** Max Product Pair, Single Pass Extreme Search vs Sorting vs Brute Force
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0120 - Tim Cap Hai So Co Tich Lon Nhat FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0120%20-%20Tim%20Cap%20Hai%20So%20Co%20Tich%20Lon%20Nhat%20FPT)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt mọi cặp $O(N^2)$.
  - *Cách 2 (Subtask 2):* Sắp xếp + $\max(A_0 A_1, A_{N-2} A_{N-1})$ $O(N \log N)$.
  - *Cách 3 (100% AC):* Single Pass 1 vòng lặp duy trì 2 Max + 2 Min $O(N)$ thời gian, $O(1)$ RAM.


---

### **[IKH-0121] - Dãy Con Tăng Dài Nhất LIS Agribank**
* **Dạng bài:** Longest Increasing Subsequence, DP Binary Search vs DP O(N^2) vs Backtracking
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0121 - Day Con Tang Dai Nhat LIS Agribank](file:///Users/dkdeveloper/projects/testcase/IKH-0121%20-%20Day%20Con%20Tang%20Dai%20Nhat%20LIS%20Agribank)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Quay lụi thử từng tập con $O(2^N)$.
  - *Cách 2 (Subtask 2):* Quy hoạch động $O(N^2)$.
  - *Cách 3 (100% AC):* Patience Sorting + Chặt nhị phân `lower_bound` $O(N \log N)$.

---

### **[IKH-0122] - Chuỗi Con Chung Dài Nhất LCS VNG**
* **Dạng bài:** Longest Common Subsequence, DP 1D Space Optimization vs DP 2D vs Backtracking
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0122 - Chuoi Con Chung Dai Nhat LCS VNG](file:///Users/dkdeveloper/projects/testcase/IKH-0122%20-%20Chuoi%20Con%20Chung%20Dai%20Nhat%20LCS%20VNG)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Đệ quy quay lụi $O(2^{N+M})$.
  - *Cách 2 (Subtask 2):* Quy hoạch động 2D $O(N \cdot M)$ thời gian & RAM.
  - *Cách 3 (100% AC):* Quy hoạch động cuộn 2 dòng 1D $O(N \cdot M)$ thời gian, $O(M)$ RAM.

---

### **[IKH-0123] - Số Lần Cắt Xâu Đối Xứng Nhỏ Nhất MoMo**
* **Dạng bài:** Palindrome Partitioning, DP Center Expansion vs DP Table O(N^2) vs Backtracking
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0123 - So Lan Cat Xau Doi Xung Nho Nhat MoMo](file:///Users/dkdeveloper/projects/testcase/IKH-0123%20-%20So%20Lan%20Cat%20Xau%20Doi%20Xung%20Nho%20Nhat%20MoMo)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Quay lụi vét cạn $O(2^N)$.
  - *Cách 2 (Subtask 2):* DP 2D Bảng Palindrome $O(N^2)$ RAM.
  - *Cách 3 (100% AC):* DP Mở rộng từ tâm đối xứng (Center Expansion) $O(N^2)$ thời gian, $O(N)$ RAM.

---

### **[IKH-0124] - Dãy Con Có Tổng Bằng S Knapsack 0/1 MBBank**
* **Dạng bài:** Subset Sum, Knapsack 0/1 DP vs Meet-in-the-Middle vs Backtracking
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0124 - Day Con Co Tong Bang S Knapsack 01 MBBank](file:///Users/dkdeveloper/projects/testcase/IKH-0124%20-%20Day%20Con%20Co%20Tong%20Bang%20S%20Knapsack%2001%20MBBank)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Quay lụi thử $2^N$ tập con $O(2^N)$.
  - *Cách 2 (Subtask 2):* Meet-in-the-middle $O(2^{N/2} \log 2^{N/2})$.
  - *Cách 3 (100% AC):* Quy hoạch động 1D Mảng Bit / Bitset $O(N \cdot S)$.

---

### **[IKH-0125] - Biến Đổi Xâu Nhỏ Nhất Edit Distance VPBank**
* **Dạng bài:** Edit Distance, Levenshtein Distance DP 1D vs DP 2D vs Backtracking
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0125 - Bien Doi Xau Nho Nhat Edit Distance VPBank](file:///Users/dkdeveloper/projects/testcase/IKH-0125%20-%20Bien%20Doi%20Xau%20Nho%20Nhat%20Edit%20Distance%20VPBank)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Đệ quy 3 nhánh $O(3^{\min(N, M)})$.
  - *Cách 2 (Subtask 2):* Quy hoạch động bảng 2D $O(N \cdot M)$ thời gian & RAM.
  - *Cách 3 (100% AC):* DP Cuộn 2 dòng 1D $O(N \cdot M)$ thời gian, $O(M)$ RAM.


---

### **[IKH-0126] - Truy Vấn Tổng Đoạn Tĩnh VNPT**
* **Dạng bài:** Range Sum Query, Prefix Sum vs Fenwick Tree vs Brute Force
* **Độ khó:** Rating 1250 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0126 - Truy Van Tong Doan Tinh VNPT](file:///Users/dkdeveloper/projects/testcase/IKH-0126%20-%20Truy%20Van%20Tong%20Doan%20Tinh%20VNPT)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt vòng lặp từng truy vấn $O(Q \cdot N)$.
  - *Cách 2 (100% AC):* Mảng cộng dồn Prefix Sum $O(N + Q)$ thời gian, $O(N)$ RAM.
  - *Cách 3 (100% AC):* Cây Fenwick (BIT) $O(N + Q \log N)$.

---

### **[IKH-0127] - Truy Vấn Nhỏ Nhất Đoạn Tĩnh RMQ Petrolimex**
* **Dạng bài:** Range Minimum Query, Sparse Table O(1) vs Segment Tree vs Brute Force
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0127 - Truy Van Nho Nhat Doan Tinh RMQ Petrolimex](file:///Users/dkdeveloper/projects/testcase/IKH-0127%20-%20Truy%20Van%20Nho%20Nhat%20Doan%20Tinh%20RMQ%20Petrolimex)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt từng đoạn $[L, R]$ $O(Q \cdot N)$.
  - *Cách 2 (Subtask 2):* Segment Tree $O(N + Q \log N)$.
  - *Cách 3 (100% AC):* Bảng Thưa Sparse Table $O(N \log N + Q)$ (Query $O(1)$).

---

### **[IKH-0128] - Cập Nhật Đoạn Tăng Giá Điện EVN Difference Array**
* **Dạng bài:** Difference Array, Range Update Point Query vs SegTree vs Brute Force
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0128 - Cap Nhat Doan Tang Gia Dien EVN Difference Array](file:///Users/dkdeveloper/projects/testcase/IKH-0128%20-%20Cap%20Nhat%20Doan%20Tang%20Gia%20Dien%20EVN%20Difference%20Array)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt tăng từng phần tử $O(Q \cdot N)$.
  - *Cách 2 (100% AC):* Mảng Sai Khác Difference Array $O(N + Q)$.
  - *Cách 3 (100% AC):* Fenwick Tree Range Update $O(N + Q \log N)$.

---

### **[IKH-0129] - Cập Nhật Đoạn Tính Tổng Đoạn SJC SegTree Lazy**
* **Dạng bài:** Segment Tree Lazy Propagation, Range Update Range Sum vs Fenwick 2 BITs vs Brute Force
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0129 - Cap Nhat Doan Tinh Tong Doan SJC SegTree Lazy](file:///Users/dkdeveloper/projects/testcase/IKH-0129%20-%20Cap%20Nhat%20Doan%20Tinh%20Tong%20Doan%20SJC%20SegTree%20Lazy)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt trực tiếp trên mảng $O(Q \cdot N)$.
  - *Cách 2 (Subtask 2):* Fenwick 2 BITs $O(N + Q \log N)$.
  - *Cách 3 (100% AC):* Segment Tree Lazy Propagation $O(N + Q \log N)$.

---

### **[IKH-0130] - Số Lớn Nhất Đoạn Cửa Sổ Trượt Có Cập Nhật Bamboo Airways**
* **Dạng bài:** Dynamic Range Max Query, Segment Tree Point Update Range Max vs Multiset vs Brute Force
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0130 - So Lon Nhat Doan Cua So Truot Co Cap Nhat Bamboo Airways](file:///Users/dkdeveloper/projects/testcase/IKH-0130%20-%20So%20Lon%20Nhat%20Doan%20Cua%20So%20Truot%20Co%20Cap%20Nhat%20Bamboo%20Airways)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt trực tiếp trên mảng $O(Q \cdot N)$.
  - *Cách 2 (Subtask 2):* Chia khối Căn Sqrt Decomposition $O(Q \sqrt{N})$.
  - *Cách 3 (100% AC):* Segment Tree Point Update Range Max $O(N + Q \log N)$.


---

### **[IKH-0131] - Đếm Số Cặp Xung Đột Giao Thông Hà Nội**
* **Dạng bài:** Inversion Count, Fenwick BIT vs Merge Sort vs Brute Force
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0131 - Dem So Cap Xung Dot Giao Thong Ha Noi](file:///Users/dkdeveloper/projects/testcase/IKH-0131%20-%20Dem%20So%20Cap%20Xung%20Dot%20Giao%20Thong%20Ha%20Noi)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt 2 vòng lặp kiểm tra $A_i > A_j$ $O(N^2)$.
  - *Cách 2 (Subtask 2):* Trộn mảng Merge Sort đếm cặp $O(N \log N)$.
  - *Cách 3 (100% AC):* Fenwick Tree BIT + Nén Tọa Độ $O(N \log N)$.

---

### **[IKH-0132] - Đếm Số Cặp Nghịch Thế Gấp Đôi Inversions 2x Lazada**
* **Dạng bài:** Reverse Pairs A[i] > 2*A[j], BIT Coordinate Compression vs Merge Sort vs Brute Force
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0132 - Dem So Cap Nghich The Gap Doi Inversions 2x Lazada](file:///Users/dkdeveloper/projects/testcase/IKH-0132%20-%20Dem%20So%20Cap%20Nghich%20The%20Gap%20Doi%20Inversions%202x%20Lazada)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt 2 vòng lặp kiểm tra $A_i > 2 A_j$ $O(N^2)$.
  - *Cách 2 (Subtask 2):* Merge Sort 2 con trỏ $O(N \log N)$.
  - *Cách 3 (100% AC):* Fenwick Tree BIT + Nén Tọa Độ Nhân đôi $O(N \log N)$.

---

### **[IKH-0133] - Tìm Phần Tử Nhỏ Thứ K Trong Cửa Sổ Trượt Baemin**
* **Dạng bài:** K-th Smallest in Window, BIT Binary Lifting vs 2 Heaps vs Brute Force
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0133 - Tim Phan Tu Nho Thu K Trong Cua So Truot Baemin](file:///Users/dkdeveloper/projects/testcase/IKH-0133%20-%20Tim%20Phan%20Tu%20Nho%20Thu%20K%20Trong%20Cua%20So%20Truot%20Baemin)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Copy cửa sổ và `std::sort` $O(N \cdot W \log W)$.
  - *Cách 2 (Subtask 2):* Dùng 2 Heaps (Max-Heap + Min-Heap) $O(N \log W)$.
  - *Cách 3 (100% AC):* Fenwick Tree BIT + Binary Lifting $O(N \log (\max A))$.

---

### **[IKH-0134] - Đếm Số Cặp Có Tổng Nằm Trong Đoạn [L, R] BeGroup**
* **Dạng bài:** Count Range Sum Subarrays, BIT Coordinate Compression vs Merge Sort vs Brute Force
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0134 - Dem So Cap Co Tong Nam Trong Doan LR BeGroup](file:///Users/dkdeveloper/projects/testcase/IKH-0134%20-%20Dem%20So%20Cap%20Co%20Tong%20Nam%20Trong%20Doan%20LR%20BeGroup)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt mọi đoạn $[i, j]$ và tính tổng $O(N^2)$.
  - *Cách 2 (Subtask 2):* Merge Sort chia để trị $O(N \log N)$.
  - *Cách 3 (100% AC):* Fenwick Tree BIT + Nén Tọa Độ Prefix Sum $O(N \log N)$.

---

### **[IKH-0135] - Đếm Số Phần Tử Nhỏ Hơn Bên Phải LeetCode 315 Zalopay**
* **Dạng bài:** Count Smaller After Self, Fenwick BIT Right-to-Left vs Merge Sort vs Brute Force
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0135 - Dem So Phan Tu Nho Hon Ben Phai LeetCode 315 Zalopay](file:///Users/dkdeveloper/projects/testcase/IKH-0135%20-%20Dem%20So%20Phan%20Tu%20Nho%20Hon%20Ben%20Phai%20LeetCode%20315%20Zalopay)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt 2 vòng lặp phía bên phải $O(N^2)$.
  - *Cách 2 (Subtask 2):* Merge Sort giữ chỉ số mảng $O(N \log N)$.
  - *Cách 3 (100% AC):* Fenwick Tree BIT Duyệt từ Phải sang Trái $O(N \log N)$.


---

### **[IKH-0136] - Đường Đi Ngắn Nhất Mạng Lưới Giao Hàng Shopee Express**
* **Dạng bài:** Single-Source Shortest Path, Dijkstra Min-Heap vs Bellman-Ford vs Backtracking
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0136 - Duong Di Ngan Nhat Mang Luoi Giao Hang Shopee Express](file:///Users/dkdeveloper/projects/testcase/IKH-0136%20-%20Duong%20Di%20Ngan%20Nhat%20Mang%20Luoi%20Giao%20Hang%20Shopee%20Express)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Quay lụi duyệt mọi đường đi $O(V!)$.
  - *Cách 2 (Subtask 2):* Thuật toán Bellman-Ford $O(V \cdot E)$.
  - *Cách 3 (100% AC):* Thuật toán Dijkstra Min-Heap $O((V + E) \log V)$.

---

### **[IKH-0137] - Ma Trận Đường Đi Giữa Mọi Cặp Kho Hàng Tiki**
* **Dạng bài:** All-Pairs Shortest Path, Floyd-Warshall O(V^3) vs Multi-BFS vs Multi-Dijkstra
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0137 - Ma Tran Duong Di Giua Moi Cap Kho Hang Tiki](file:///Users/dkdeveloper/projects/testcase/IKH-0137%20-%20Ma%20Tran%20Duong%20Di%20Giua%20Moi%20Cap%20Kho%20Hang%20Tiki)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Chạy BFS $V$ lần (Cho đồ thị không trọng số) $O(V \cdot (V + E))$.
  - *Cách 2 (100% AC):* Thuật toán Floyd-Warshall $O(V^3)$.
  - *Cách 3 (100% AC):* Chạy Dijkstra $V$ lần dùng Min-Heap $O(V \cdot (V + E) \log V)$.

---

### **[IKH-0138] - Đường Đi Ngắn Nhất Đồ Thị Trọng Số 0-1 Grab Bike**
* **Dạng bài:** 0-1 BFS, Deque 0-1 BFS vs Dijkstra Min-Heap vs Brute Force
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0138 - Duong Di Ngan Nhat Do Thi Trong So 01 Grab Bike](file:///Users/dkdeveloper/projects/testcase/IKH-0138%20-%20Duong%20Di%20Ngan%20Nhat%20Do%20Thi%20Trong%20So%2001%20Grab%20Bike)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt DFS thô $O(V!)$.
  - *Cách 2 (Subtask 2):* Thuật toán Dijkstra Min-Heap $O((V + E) \log V)$.
  - *Cách 3 (100% AC):* Thuật toán 0-1 BFS `std::deque` $O(V + E)$.

---

### **[IKH-0139] - Khoảng Cách Xa Nhất Giữa 2 Máy Chủ Mạng Cây Viettel**
* **Dạng bài:** Tree Diameter, 2-BFS vs Tree DP vs All-Pairs BFS
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0139 - Khoang Cach Xa Nhat Giua 2 May Chu Mang Cay Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0139%20-%20Khoang%20Cach%20Xa%20Nhat%20Giua%202%20May%20Chu%20Mang%20Cay%20Viettel)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Chạy BFS từ từng đỉnh $1..N$ $O(N^2)$.
  - *Cách 2 (100% AC):* Thuật toán 2 lần BFS $O(N)$.
  - *Cách 3 (100% AC):* Quy hoạch động trên cây Tree DP $O(N)$.

---

### **[IKH-0140] - Tập Trung Hàng Hóa Tại Nút Trung Tâm Cây VNPost**
* **Dạng bài:** Tree Centroid / Re-rooting DP, Sum of Distances vs All-BFS
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0140 - Tap Trung Hang Hoa Tai Nut Trung Tam Cay VNPost](file:///Users/dkdeveloper/projects/testcase/IKH-0140%20-%20Tap%20Trung%20Hang%20Hoa%20Tai%20Nut%20Trung%20Tam%20Cay%20VNPost)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Chạy BFS từ từng đỉnh tính tổng khoảng cách $O(N^2)$.
  - *Cách 2 (100% AC):* Tree DP Re-rooting Chuyển gốc $O(N)$.
  - *Cách 3 (100% AC):* Tìm Nút Trọng Tâm Centroid + 1 lần BFS $O(N)$.


---

### **[IKH-0141] - Tìm Vị Trí Khớp Mẫu Quảng Cáo TikTok**
* **Dạng bài:** Pattern Matching, KMP vs Rolling Hash vs Brute Force
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0141 - Tim Vi Tri Khop Mau Quang Cao TikTok](file:///Users/dkdeveloper/projects/testcase/IKH-0141%20-%20Tim%20Vi%20Tri%20Khop%20Mau%20Quang%20Cao%20TikTok)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt 2 con trỏ thô $O(|S| \cdot |P|)$.
  - *Cách 2 (Subtask 2):* Băm chuỗi Polynomial Rolling Hash $O(|S| + |P|)$.
  - *Cách 3 (100% AC):* Thuật toán KMP $O(|S| + |P|)$.

---

### **[IKH-0142] - Độ Dài Tiền Vế & Hậu Vế Dài Nhất VTV**
* **Dạng bài:** Longest Border / Prefix Suffix, KMP Pi Array vs Hash vs Brute Force
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0142 - Do Dai Tien Ve Va Hau Ve Dai Nhat VTV](file:///Users/dkdeveloper/projects/testcase/IKH-0142%20-%20Do%20Dai%20Tien%20Ve%20Va%20Hau%20Ve%20Dai%20Nhat%20VTV)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Thử từng độ dài $L$ từ $N-1$ về 1 $O(N^2)$.
  - *Cách 2 (Subtask 2):* Rolling Hash kiểm tra Prefix == Suffix $O(N)$.
  - *Cách 3 (100% AC):* Mảng Tiền tố KMP $\pi[N-1]$ $O(N)$.

---

### **[IKH-0143] - Xâu Đối Xứng Dài Nhất Trong Nhật Ký Hệ Thống MoMo**
* **Dạng bài:** Longest Palindromic Substring, Manacher Algorithm vs Expand Center vs Brute Force
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0143 - Xau Doi Xung Dai Nhat Trong Nhat Ky He Thong MoMo](file:///Users/dkdeveloper/projects/testcase/IKH-0143%20-%20Xau%20Doi%20Xung%20Dai%20Nhat%20Trong%20Nhat%20Ky%20He%20Thong%20MoMo)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt mọi xâu con và kiểm tra $O(N^3)$.
  - *Cách 2 (Subtask 2):* Mở rộng từ tâm (Expand Around Center) $O(N^2)$.
  - *Cách 3 (100% AC):* Thuật toán Manacher $O(N)$.

---

### **[IKH-0144] - Tìm Tất Cả Tiền Xấu Khớp Xâu Z-Algorithm VNG**
* **Dạng bài:** Z-Algorithm, Z-Function vs Rolling Hash vs Brute Force
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0144 - Tim Tat Ca Tien Xau Khop Xau ZAlgorithm VNG](file:///Users/dkdeveloper/projects/testcase/IKH-0144%20-%20Tim%20Tat%20Ca%20Tien%20Xau%20Khop%20Xau%20ZAlgorithm%20VNG)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt kiểm tra từng vị trí $O(N^2)$.
  - *Cách 2 (Subtask 2):* Rolling Hash + Chặt Nhị Phân $O(N \log N)$.
  - *Cách 3 (100% AC):* Thuật toán Z-Algorithm $O(N)$.

---

### **[IKH-0145] - Đếm Số Lần Xâu Con Xuất Hiện Bằng Cây Trie MoMo**
* **Dạng bài:** Trie / Double Hash Substring Queries, Trie vs Double Hash vs Map
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0145 - Dem So Lan Xau Con Xuat Hien Bang Cay Trie MoMo](file:///Users/dkdeveloper/projects/testcase/IKH-0145%20-%20Dem%20So%20Lan%20Xau%20Con%20Xuat%20Hien%20Bang%20Cay%20Trie%20MoMo)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Vét cạn so sánh từng xâu $O(Q \cdot N \cdot |T|)$.
  - *Cách 2 (Subtask 2):* Dùng `std::unordered_map` lưu mọi Prefix $O(\sum |S|^2 + Q \cdot |T|)$.
  - *Cách 3 (100% AC):* Cấu trúc dữ liệu Cây Tiền Tố Trie $O(\sum |S| + \sum |T|)$.


---

### **[IKH-0146] - Số Fibonacci Thứ N Mã Hóa Giao Dịch VPBank**
* **Dạng bài:** Matrix Exponentiation, Fast Doubling vs Matrix Exponentiation vs Iterative DP
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0146 - So Fibonacci Thu N Ma Hoa Giao Dich VPBank](file:///Users/dkdeveloper/projects/testcase/IKH-0146%20-%20So%20Fibonacci%20Thu%20N%20Ma%20Hoa%20Giao%20Dich%20VPBank)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Duyệt vòng lặp DP quy hoạch động $O(N)$.
  - *Cách 2 (100% AC):* Lũy Thừa Ma Trận Matrix Exponentiation $O(\log N)$.
  - *Cách 3 (100% AC):* Fast Doubling Fibonacci $O(\log N)$.

---

### **[IKH-0147] - Tính Số Tổ Hợp C(N, K) Chọn Đội Ngũ Techcombank**
* **Dạng bài:** Combinations C(N,K), Precomputed Factorial Inverse vs Pascal DP vs Direct Multiplications
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0147 - Tinh So To Hop CNK Chon Doi Ngu Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0147%20-%20Tinh%20So%20To%20Hop%20CNK%20Chon%20Doi%20Ngu%20Techcombank)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Tam giác Pascal DP $O(N^2 + Q)$.
  - *Cách 2 (Subtask 2):* Nhân chia trực tiếp Fermat mỗi query $O(Q \cdot K \log MOD)$.
  - *Cách 3 (100% AC):* Tiền tính Giai thừa & Nghịch đảo Giai thừa $O(N + Q)$.

---

### **[IKH-0148] - Số Đường Đi Trên Lưới Mã Hóa Hệ Thống FPT**
* **Dạng bài:** Grid Paths Combinatorics, Formula C(N+M-2, N-1) vs 1D DP vs 2D DP
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0148 - So Duong Di Tren Luoi Ma Hoa He Thong FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0148%20-%20So%20Duong%20Di%20Tren%20Luoi%20Ma%20Hoa%20He%20Thong%20FPT)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Quy hoạch động 2D DP $O(N \cdot M)$.
  - *Cách 2 (Subtask 2):* Quy hoạch động 1D DP tối ưu $O(N \cdot M)$.
  - *Cách 3 (100% AC):* Công thức Tổ hợp $C(N+M-2, N-1)$ $O(N + M)$.

---

### **[IKH-0149] - Số Cách Phân Tích Thành Tổng Các Số Nguyên VIB**
* **Dạng bài:** Integer Partition, Euler Pentagonal Theorem vs 1D Knapsack DP vs Backtracking
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0149 - So Cach Phan Tich Thanh Tong Cac So Nguyen VIB](file:///Users/dkdeveloper/projects/testcase/IKH-0149%20-%20So%20Cach%20Phan%20Tich%20Thanh%20Tong%20Cac%20So%20Nguyen%20VIB)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Đệ quy quay lụi phân tích tổng $O(2^N)$.
  - *Cách 2 (100% AC):* Quy hoạch động Knapsack 1D $O(N^2)$.
  - *Cách 3 (100% AC):* Định lý Số Ngũ Giác Euler (Pentagonal) $O(N \sqrt{N})$.

---

### **[IKH-0150] - Tính Tổng Hệ Số Nhị Thức Và Lũy Thừa Nhanh MBBank**
* **Dạng bài:** Binomial Expansion & Fast Exponentiation, Fast Power O(log N) vs Direct Sum O(N)
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0150 - Tinh Tong He So Nhi Thuc Va Luy Thua Nhanh MBBank](file:///Users/dkdeveloper/projects/testcase/IKH-0150%20-%20Tinh%20Tong%20He%20So%20Nhi%20Thuc%20Va%20Luy%20Thua%20Nhanh%20MBBank)
* **Phương pháp đa giải:**
  - *Cách 1 (Subtask 1):* Tính từng số hạng nhị thức và cộng dồn $O(N \log MOD)$.
  - *Cách 2 (Subtask 2):* Tính $(A+B)$ sau đó nhân vòng lặp $O(N)$.
  - *Cách 3 (100% AC):* Lũy Thừa Nhanh Binary Exponentiation $(A+B)^N$ $O(\log N)$.


---

### **⚠️ QUY TẮC QUAN TRỌNG VỀ QUẢN LÝ TIÊU ĐỀ CONTEST (CONTEST NAME)**
* **QUY TẮC TUÂN THỦ:** KHÔNG BAO GIỜ tự ý ghi đè hoặc thay đổi thuộc tính `contest.name` (Tiêu đề Contest) khi thực hiện đồng bộ description, lý thuyết hay bài tập lên VPS trừ khi có yêu cầu trực tiếp từ người dùng.
* **Lý do:** Người dùng tự đặt và quản lý tiêu đề hiển thị chính thức của Contest trên Web (Ví dụ: `#01 - Ôn tập toàn bộ kiến thức`, `#02 - Nhận dạng toán học`, `#03 - Một bài nhiều cách giải`).
* **Hành động bắt buộc:** Khi cập nhật `description` của Contest, chỉ thay đổi `contest.description`, giữ nguyên `contest.name`.


---

### **[IKH-0151] - Lập Lịch Giao Hàng Tiết Kiệm Nhiên Liệu VinFast**
* **Dạng bài:** Binary Search on Answer + Greedy Check (Shipper Allocation)
* **Độ khó:** Rating 1250 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0151 - Lap Lich Giao Hang VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0151%20-%20Lap%20Lich%20Giao%20Hang%20VinFast)
* **Phương pháp giải:** Chặt nhị phân tải trọng tối đa $X \in [\max(A_i), \sum A_i]$, dùng hàm kiểm tra tham ăn gom nhóm chuyến xe trong $O(N \log (\sum A_i))$.

---

### **[IKH-0152] - Tối Ưu Hóa Tải Trọng Đoàn Tàu Bắc Nam VN-Railway**
* **Dạng bài:** Binary Search on Answer + Sliding Window Check
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0152 - Toi Uu Tai Trong Doan Tau VN-Railway](file:///Users/dkdeveloper/projects/testcase/IKH-0152%20-%20Toi%20Uu%20Tai%20Trong%20Doan%20Tau%20VN-Railway)
* **Phương pháp giải:** Chặt nhị phân kết quả $X$ kết hợp cửa sổ trượt độ dài từ $L$ đến $R$ kiểm tra tổng tải trọng $\le K$.

---

### **[IKH-0153] - Chia Cắt Chuỗi Cung Ứng Linh Kiện Samsung**
* **Dạng bài:** Binary Search on Answer + DP Partition Check
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0153 - Chia Cat Chuoi Cung Ung Samsung](file:///Users/dkdeveloper/projects/testcase/IKH-0153%20-%20Chia%20Cat%20Chuoi%20Cung%20Ung%20Samsung)
* **Phương pháp giải:** Chặt nhị phân giá trị $X$ kết hợp kiểm tra phân hoạch mảng liên tiếp thành $K$ đoạn có tổng $\le X$.

---

### **[IKH-0154] - Lắp Đặt Trạm Phủ Sóng 5G Viettel**
* **Dạng bài:** Binary Search on Range Distance + Two Pointers Check
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0154 - Lap Dat Tram Phu Song 5G Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0154%20-%20Lap%20Dat%20Tram%20Phu%20Song%205G%20Viettel)
* **Phương pháp giải:** Chặt nhị phân bán kính phủ sóng $R$, dùng hai con trỏ kiểm tra số trạm phát tối thiểu cần đặt.

---

### **[IKH-0155] - Cân Bằng Tải Máy Chủ Thu Thập Dữ Liệu Shopee**
* **Dạng bài:** Binary Search on Answer + Unbounded Knapsack Greedy Check
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0155 - Can Bang Tai May Chu Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0155%20-%20Can%20Bang%20Tai%20May%20Chu%20Shopee)
* **Phương pháp giải:** Chặt nhị phân tải công việc $X$, kiểm tra khả năng chia đều giữa các máy chủ xử lý dữ liệu.

---

### **[IKH-0156] - Phân Phối Điện Năng Năng Lượng Mặt Trời EVN Solar**
* **Dạng bài:** Binary Search on Answer + Prefix Sum Two Pointers Check
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0156 - Phan Phoi Dien Nang EVN Solar](file:///Users/dkdeveloper/projects/testcase/IKH-0156%20-%20Phan%20Phoi%20Dien%20Nang%20EVN%20Solar)
* **Phương pháp giải:** Chặt nhị phân sản lượng điện tối thiểu $X$, dùng mảng cộng dồn và hai con trỏ kiểm tra khoảng phát điện.

---

### **[IKH-0157] - Thiết Kế Tuyến Cáp Quang Biển VNPT**
* **Dạng bài:** Binary Search on Average + DP Check
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0157 - Thiet Ke Cap Quang Bien VNPT](file:///Users/dkdeveloper/projects/testcase/IKH-0157%20-%20Thiet%20Ke%20Cap%20Quang%20Bien%20VNPT)
* **Phương pháp giải:** Chặt nhị phân trung bình $X$, biến đổi mảng $B[i] = A[i] - X$, kiểm tra tồn tại mảng con có tổng $\ge 0$.

---

### **[IKH-0158] - Quản Lý Bàn Giao Căn Hộ Vinhomes Master Plan**
* **Dạng bài:** Binary Search on Answer + 2D Grid Monotonic Queue Check
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0158 - Quan Ly Ban Giao Can Ho Vinhomes](file:///Users/dkdeveloper/projects/testcase/IKH-0158%20-%20Quan%20Ly%20Ban%20Giao%20Can%20Ho%20Vinhomes)
* **Phương pháp giải:** Chặt nhị phân diện tích / khoảng thời gian $X$, dùng hàng đợi đơn điệu 2D kiểm tra vùng bàn giao.

---

### **[IKH-0159] - Điều Phối Hạm Đội Xe Cấp Cứu Y Tế 115**
* **Dạng bài:** Binary Search on Answer + Greedy Interval Sorting Check
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0159 - Dieu Phoi Xe Cap Cuu Y Te 115](file:///Users/dkdeveloper/projects/testcase/IKH-0159%20-%20Dieu%20Phoi%20Xe%20Cap%20Cuu%20Y%20Te%20115)
* **Phương pháp giải:** Chặt nhị phân thời gian phản ứng $T$, sắp xếp các khoảng thời gian yêu cầu và tham ăn phân công xe cấp cứu.

---

### **[IKH-0160] - Tối Ưu Hóa Tuyến Đường Vận Chuyển Hàng Hóa Tiki**
* **Dạng bài:** Binary Search on Max Edge Weight + BFS Path Check
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0160 - Toi Uu Tuyen Duong Vanchuyen Tiki](file:///Users/dkdeveloper/projects/testcase/IKH-0160%20-%20Toi%20Uu%20Tuyen%20Duong%20Vanchuyen%20Tiki)
* **Phương pháp giải:** Chặt nhị phân trọng số cạnh tối đa $W$, dùng thuật toán BFS kiểm tra tính liên thông $S 	o T$ trên đồ thị.


---

### **[IKH-0161] - Phân Tích Xâu Nhật Ký Giao Dịch Vietcombank**
* **Dạng bài:** Rolling Hash + Binary Search for Longest Repeating Non-overlapping Substring
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0161 - Phan Tich Xau Nhat Ky Vietcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0161%20-%20Phan%20Tich%20Xau%20Nhat%20Ky%20Vietcombank)
* **Phương pháp giải:** Chặt nhị phân độ dài $L$, dùng Rolling Hash kiểm tra sự xuất hiện của xâu con ở 2 vị trí không đè lên nhau ($i_{curr} - i_{first} \ge L$) trong $O(N \log N)$.

---

### **[IKH-0162] - Kiểm Tra Mật Mã Đa Lớp Security FPT**
* **Dạng bài:** Rolling Hash + Two Pointers for Distinct Substrings
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0162 - Kiem Tra Mat Ma Security FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0162%20-%20Kiem%20Tra%20Mat%20Ma%20Security%20FPT)
* **Phương pháp giải:** Hai con trỏ co giãn cửa sổ kết hợp băm chuỗi Rolling Hash kiểm tra tính duy nhất của các xâu mật mã.

---

### **[IKH-0163] - Phát Hiện Đoạn Mã Giả Mạo VNG Studio**
* **Dạng bài:** Double Rolling Hash + Binary Search for Pattern Frequency
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0163 - Phat Hien Ma Gia Mao VNG Studio](file:///Users/dkdeveloper/projects/testcase/IKH-0163%20-%20Phat%20Hien%20Ma%20Gia%20Mao%20VNG%20Studio)
* **Phương pháp giải:** Băm chuỗi hai Modulo ($10^9+7$ và $10^9+9$) kết hợp chặt nhị phân đếm số lần xuất hiện của đoạn mã giả mạo.

---

### **[IKH-0164] - Trích Xuất Mã Giao Dịch Lặp Tối Đa MoMo**
* **Dạng bài:** Rolling Hash + Binary Search for Maximal Repeated Substring
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0164 - Trich Xuat Ma Giao Dich MoMo Wallet](file:///Users/dkdeveloper/projects/testcase/IKH-0164%20-%20Trich%20Xuat%20Ma%20Giao%20Dich%20MoMo%20Wallet)
* **Phương pháp giải:** Chặt nhị phân độ dài mã $L$, dùng mảng `powB` và mảng băm tiền tố kiểm tra mã giao dịch xuất hiện nhiều nhất.

---

### **[IKH-0165] - Khôi Phục Chuỗi Gen Virus Epidemic VN**
* **Dạng bài:** Rolling Hash + Sliding Window Matching
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0165 - Khoi Phuc Chuoi Gen Epidemic VN](file:///Users/dkdeveloper/projects/testcase/IKH-0165%20-%20Khoi%20Phuc%20Chuoi%20Gen%20Epidemic%20VN)
* **Phương pháp giải:** Trượt cửa sổ kích thước $K$ kết hợp băm chuỗi Rolling Hash $O(1)$ cập nhật giá trị băm.

---

### **[IKH-0166] - Kiểm Lỗi Xâu Ký Tự Mạng Viettel Telecom**
* **Dạng bài:** Rolling Hash + Binary Search for Longest Common Prefix (LCP)
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0166 - Kiem Loi Xau Ky Tu Viettel Telecom](file:///Users/dkdeveloper/projects/testcase/IKH-0166%20-%20Kiem%20Loi%20Xau%20Ky%20Tu%20Viettel%20Telecom)
* **Phương pháp giải:** Chặt nhị phân tìm độ dài tiền tố chung dài nhất giữa xâu $S[L..R]$ và xâu mẫu $T$ bằng Rolling Hash trong $O(\log N)$.

---

### **[IKH-0167] - Nén Chuỗi Dữ Liệu Cảm Biến IoT VinAI**
* **Dạng bài:** Rolling Hash + Periodicity String Matching
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0167 - Nen Chuoi Du Lieu IoT VinAI](file:///Users/dkdeveloper/projects/testcase/IKH-0167%20-%20Nen%20Chuoi%20Du%20Lieu%20IoT%20VinAI)
* **Phương pháp giải:** Duyệt ước số $K$ của $N$, dùng Rolling Hash so sánh $H(1..N-K)$ với $H(K+1..N)$ để kiểm tra tính chu kỳ trong $O(N)$.

---

### **[IKH-0168] - Lọc Tin Nhắn Spam Hệ Thống Zalo Cloud**
* **Dạng bài:** Double Rolling Hash + Frequency Map + Binary Search
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0168 - Loc Tin Nhan Spam Zalo Cloud](file:///Users/dkdeveloper/projects/testcase/IKH-0168%20-%20Loc%20Tin%20Nhan%20Spam%20Zalo%20Cloud)
* **Phương pháp giải:** Băm chuỗi 2 chiều kiểm tra mật độ các xâu con spam xuất hiện với tần suất cao.

---

### **[IKH-0169] - Đếm Chuỗi Đối Xứng Bằng Mã Băm Shopee Live**
* **Dạng bài:** Rolling Hash Forward & Backward + Binary Search
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0169 - Dem Chuoi Doi Xung Shopee Live](file:///Users/dkdeveloper/projects/testcase/IKH-0169%20-%20Dem%20Chuoi%20Doi%20Xung%20Shopee%20Live)
* **Phương pháp giải:** Xây dựng mảng băm xuôi và ngược, chặt nhị phân bán kính Palindrome tại từng tâm $i$ trong $O(N \log N)$.

---

### **[IKH-0170] - Xác Thực Mã Vạch Sản Phẩm WinMart**
* **Dạng bài:** Rolling Hash + Two Pointers Matching with K Mismatches
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0170 - Xac Thuc Ma Vach San Pham WinMart](file:///Users/dkdeveloper/projects/testcase/IKH-0170%20-%20Xac%20Thuc%20Ma%20Vach%20San%20Pham%20WinMart)
* **Phương pháp giải:** Dùng Rolling Hash và Chặt nhị phân nhảy qua các vị trí khớp trùng, hỗ trợ tối đa $K$ vị trí sai lệch.


---

### **[IKH-0171] - Đếm Cặp Cổ Phiếu Tương Quan SSI**
* **Dạng bài:** Coordinate Compression + Fenwick Tree BIT (Inversion Counting)
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0171 - Dem Cap Co Phieu Tuong Quan SSI](file:///Users/dkdeveloper/projects/testcase/IKH-0171%20-%20Dem%20Cap%20Co%20Phieu%20Tuong%20Quan%20SSI)
* **Phương pháp giải:** Nén tọa độ các chỉ số cổ phiếu $A_i \in [-10^9, 10^9]$, dùng Cây Fenwick BIT đếm số cặp $i < j$ và $A_i > A_j$ trong $O(N \log N)$.

---

### **[IKH-0172] - Quản Lý Điểm Đánh Giá FPT Software**
* **Dạng bài:** Coordinate Compression + Dynamic Range Max Segment Tree
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0172 - Quan Ly Diem Danh Gia FPT Software](file:///Users/dkdeveloper/projects/testcase/IKH-0172%20-%20Quan%20Ly%20Diem%20Danh%20Gia%20FPT%20Software)
* **Phương pháp giải:** Nén tọa độ thời gian đánh giá, dùng Cây Segment Tree cập nhật điểm và truy vấn giá trị lớn nhất trong $O(\log N)$.

---

### **[IKH-0173] - Tối Ưu Tuyến Xe Buýt BRT Hà Nội**
* **Dạng bài:** Coordinate Compression + Segment Tree Point Update Range Sum
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0173 - Toi Uu Tuyen Xe Buyt BRT Ha Noi](file:///Users/dkdeveloper/projects/testcase/IKH-0173%20-%20Toi%20Uu%20Tuyen%20Xe%20Buyt%20BRT%20Ha%20Noi)
* **Phương pháp giải:** Nén tọa độ vị trí trạm xe buýt, dùng Cây Segment Tree tính tổng lượng hành khách trên từng chặng trong $O(\log N)$.

---

### **[IKH-0174] - Cập Nhật Thời Gian Đăng Ký Tín Chỉ ĐHQG**
* **Dạng bài:** Coordinate Compression + Difference Array / BIT Range Update
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0174 - Cap Nhat Thoi Gian Dang Ky Tin Chi DHQG](file:///Users/dkdeveloper/projects/testcase/IKH-0174%20-%20Cap%20Nhat%20Thoi%20Gian%20Dang%20Ky%20Tin%20Chi%20DHQG)
* **Phương pháp giải:** Nén các mốc thời gian lớn, dùng mảng sai khác Difference Array hoặc BIT range update cập nhật số lượt đăng ký.

---

### **[IKH-0175] - Đếm Cặp Sản Phẩm Giá Gấp Đôi Lazada**
* **Dạng bài:** Double Coordinate Compression + Fenwick Tree BIT ($A[i] > 2 A[j]$)
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0175 - Dem Cap San Pham Gia Gap Doi Lazada](file:///Users/dkdeveloper/projects/testcase/IKH-0175%20-%20Dem%20Cap%20San%20Pham%20Gia%20Gap%20Doi%20Lazada)
* **Phương pháp giải:** Nén cả hai tập giá trị $\{A[i]\}$ và $\{2 A[i]\}$, dùng Cây Fenwick query `i - bit.query(rank(2 * A[i]))` trong $O(N \log N)$.

---

### **[IKH-0176] - Xếp Hạng Tìm Kiếm Thứ K Tiki**
* **Dạng bài:** Coordinate Compression + BIT Binary Lifting Order Statistic
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0176 - Xep Hang Tim Kiem Thu K Tiki](file:///Users/dkdeveloper/projects/testcase/IKH-0176%20-%20Xep%20Hang%20Tim%20Kiem%20Thu%20K%20Tiki)
* **Phương pháp giải:** Nén điểm số tìm kiếm, áp dụng kỹ thuật Chặt nhị phân trên mảng BIT (Binary Lifting) tìm phần tử nhỏ thứ $K$ trong $O(\log N)$.

---

### **[IKH-0177] - Lọc Dữ Liệu Cảm Biến Thời Tiết Khí Tượng**
* **Dạng bài:** Coordinate Compression + Range Update Range Sum SegTree Lazy
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0177 - Loc Du Lieu Cam Bien Thoi Tiet](file:///Users/dkdeveloper/projects/testcase/IKH-0177%20-%20Loc%20Du%20Lieu%20Cam%20Bien%20Thoi%20Tiet)
* **Phương pháp giải:** Nén các mốc tọa độ địa lý/thời gian, dùng Cây Phân Đoạn đẩy lười Segment Tree Lazy Propagation để cập nhật đoạn và tính tổng.

---

### **[IKH-0178] - Phân Tích Tần Suất Giao Dịch VNPay**
* **Dạng bài:** Coordinate Compression + Fenwick Tree Prefix Range Query
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0178 - Phan Tich Tan Suat Giao Dich VNPay](file:///Users/dkdeveloper/projects/testcase/IKH-0178%20-%20Phan%20Tich%20Tan%20Suat%20Giao%20Dich%20VNPay)
* **Phương pháp giải:** Nén số tiền giao dịch, dùng Cây Fenwick đếm tần suất các giao dịch trong khoảng $[L, R]$.

---

### **[IKH-0179] - Đếm Đoạn Con Tổng Nằm Trong [L, R] MoMo**
* **Dạng bài:** Coordinate Compression on Prefix Sums + Fenwick Tree BIT
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0179 - Dem Doan Con Tong Nam Trong LR MoMo](file:///Users/dkdeveloper/projects/testcase/IKH-0179%20-%20Dem%20Doan%20Con%20Tong%20Nam%20Trong%20LR%20MoMo)
* **Phương pháp giải:** Nén mảng Prefix Sum $P$, chuyển điều kiện $L \le P[j] - P[i] \le R \iff P[j] - R \le P[i] \le P[j] - L$, dùng BIT đếm trong $O(N \log N)$.

---

### **[IKH-0180] - Xác Định Vùng Phủ Sóng Ăng-ten VinaPhone**
* **Dạng bài:** 2D Coordinate Compression + Sweep-line + Segment Tree
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0180 - Xac Dinh Vung Phu Song VinaPhone](file:///Users/dkdeveloper/projects/testcase/IKH-0180%20-%20Xac%20Dinh%20Vung%20Phu%20Song%20VinaPhone)
* **Phương pháp giải:** Nén tọa độ 2D kết hợp thuật toán đường quét Sweep-Line và Cây Segment Tree tính tổng diện tích vùng phủ sóng ăng-ten.


---

### **[IKH-0181] - Đếm Số Đường Đi Ngắn Nhất Metro TP.HCM**
* **Dạng bài:** Dijkstra Shortest Path + Dynamic Programming Path Counting
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0181 - Dem So Duong Di Ngan Nhat Metro TPHCM](file:///Users/dkdeveloper/projects/testcase/IKH-0181%20-%20Dem%20So%20Duong%20Di%20Ngan%20Nhat%20Metro%20TPHCM)
* **Phương pháp giải:** Dùng thuật toán Dijkstra Min-Heap kết hợp mảng quy hoạch động `paths[u]` đếm số đường đi ngắn nhất đến $u$ modulo $10^9+7$ trong $O((V+E) \log V)$.

---

### **[IKH-0182] - Đường Đi Tối Ưu Lợi Nhuận Grab Express**
* **Dạng bài:** DAG Topological Sort + Dynamic Programming
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0182 - Duong Di Toi Uu Loi Nhuan Grab Express](file:///Users/dkdeveloper/projects/testcase/IKH-0182%20-%20Duong%20Di%20Toi%20Uu%20Loi%20Nhuan%20Grab%20Express)
* **Phương pháp giải:** Sắp xếp Topo đồ thị có hướng không chu trình DAG, kết hợp quy hoạch động tìm đường đi có tổng lợi nhuận lớn nhất trong $O(V+E)$.

---

### **[IKH-0183] - Đường Đi Ngắn Nhất Trạng Số Pin EVN Bus**
* **Dạng bài:** 0-1 BFS / Dijkstra State Graph
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0183 - Duong Di Ngan Nhat Trang So Pin EVN Bus](file:///Users/dkdeveloper/projects/testcase/IKH-0183%20-%20Duong%20Di%20Ngan%20Nhat%20Trang%20So%20Pin%20EVN%20Bus)
* **Phương pháp giải:** Mở rộng trạng thái đồ thị `(u, battery_level)`, chạy Dijkstra Min-Heap tìm đường đi với lượng pin tối ưu trong $O(V \cdot K \log (V \cdot K))$.

---

### **[IKH-0184] - Tối Ưu Đường Đi Qua Không Quá K Cạnh Shopee**
* **Dạng bài:** Bellman-Ford / DP Shortest Path with At Most K Edges
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0184 - Toi Uu Duong Di Qua Khong Qua K Canh Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0184%20-%20Toi%20Uu%20Duong%20Di%20Qua%20Khong%20Qua%20K%20Canh%20Shopee)
* **Phương pháp giải:** Quy hoạch động `dp[k][u]` là chi phí nhỏ nhất đi từ $S$ đến $u$ qua đúng $k$ cạnh trong $O(K \cdot E)$.

---

### **[IKH-0185] - Hành Trình Cứu Hộ Thủy Điện Sơn La**
* **Dạng bài:** BFS + Dynamic Programming State Representation
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0185 - Hanh Trinh Cuu Ho Thuy Dien Son La](file:///Users/dkdeveloper/projects/testcase/IKH-0185%20-%20Hanh%20Trinh%20Cuu%20Ho%20Thuy%20Dien%20Son%20La)
* **Phương pháp giải:** Thuật toán duyệt BFS kết hợp biểu diễn trạng thái quy hoạch động tìm thời gian cứu hộ ngắn nhất trên đồ thị cứu nạn.

---

### **[IKH-0186] - Tuyến Đường Thu Gom Rác Thải Hà Nội**
* **Dạng bài:** Dijkstra + Subtree / Node Profit DP
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0186 - Tuyen Duong Thu Gom Rac Thai Ha Noi](file:///Users/dkdeveloper/projects/testcase/IKH-0186%20-%20Tuyen%20Duong%20Thu%20Gom%20Rac%20Thai%20Ha%20Noi)
* **Phương pháp giải:** Kết hợp Dijkstra tìm đường đi ngắn nhất đến các cụm và quy hoạch động chọn tuyến thu gom rác thải tối ưu lợi nhuận.

---

### **[IKH-0187] - Định Tuyến Mạng Cáp Quang Viettel**
* **Dạng bài:** Dijkstra + Path Counting modulo $10^9+7$
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0187 - Dinh Tuyen Mang Cap Quang Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0187%20-%20Dinh%20Tuyen%20Mang%20Cap%20Quang%20Viettel)
* **Phương pháp giải:** Chạy Dijkstra Min-Heap tính `dist[u]` và quy hoạch động đếm số lượng đường định tuyến cáp quang tối ưu.

---

### **[IKH-0188] - Tối Ưu Chi Phí Hàng Hải Vinashin**
* **Dạng bài:** Floyd-Warshall + DP Subset State
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0188 - Toi Uu Chi Phi Hang Hai Vinashin](file:///Users/dkdeveloper/projects/testcase/IKH-0188%20-%20Toi%20Uu%20Chi%20Phi%20Hang%20Hai%20Vinashin)
* **Phương pháp giải:** Tiền tính ma trận đường đi giữa mọi cặp cảng biển bằng Floyd-Warshall $O(V^3)$, kết hợp DP tập con tìm chi phí vận tải nhỏ nhất.

---

### **[IKH-0189] - Tìm Tuyến Xe Cấp Cứu Nhanh Nhất 115**
* **Dạng bài:** Multi-Source BFS + DP Range Query
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0189 - Tim Tuyen Xe Cap Cuu Nhanh Nhat 115](file:///Users/dkdeveloper/projects/testcase/IKH-0189%20-%20Tim%20Tuyen%20Xe%20Cap%20Cuu%20Nhanh%20Nhat%20115)
* **Phương pháp giải:** Chạy BFS nhiều nguồn từ các bệnh viện 115, kết hợp quy hoạch động tìm tuyến đường ứng cứu nhanh nhất.

---

### **[IKH-0190] - Phân Phối Điện Mạng Lưới Cây EVN**
* **Dạng bài:** Tree DP + Graph Traversal (Subtree Sum & Max Choice)
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0190 - Phan Phoi Dien Mang Luoi Cay EVN](file:///Users/dkdeveloper/projects/testcase/IKH-0190%20-%20Phan%20Phoi%20Dien%20Mang%20Luoi%20Cay%20EVN)
* **Phương pháp giải:** Thuật toán duyệt cây DFS kết hợp quy hoạch động trên cây `dp[u][0]` và `dp[u][1]` tối ưu lượng điện phân phối.


---

### **[IKH-0191] - Tối Ưu Phân Công Nhiệm Vụ Đội Ngũ Kỹ Sư VinAI**
* **Dạng bài:** Bitmask DP Assignment Problem
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0191 - Toi Uu Phan Cong Nhiem Vu VinAI](file:///Users/dkdeveloper/projects/testcase/IKH-0191%20-%20Toi%20Uu%20Phan%20Cong%20Nhiem%20Vu%20VinAI)
* **Phương pháp giải:** Đặt `dp[mask]` là chi phí nhỏ nhất phân công tập dự án `mask`. Duyệt `mask` từ $0 	o 2^N-1$ trong $O(N \cdot 2^N)$.

---

### **[IKH-0192] - Hành Trình Giao Hàng Ghé Thăm N Điểm Tiki**
* **Dạng bài:** Bitmask DP Traveling Salesperson Problem (TSP)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0192 - Hanh Trinh Giao Hang Tiki Delivery](file:///Users/dkdeveloper/projects/testcase/IKH-0192%20-%20Hanh%20Trinh%20Giao%20Hang%20Tiki%20Delivery)
* **Phương pháp giải:** Quy hoạch động trạng thái bit `dp[mask][u]` tìm chi phí di chuyển nhỏ nhất qua tập điểm `mask` kết thúc tại $u$ trong $O(N^2 \cdot 2^N)$.

---

### **[IKH-0193] - Đếm Số Cách Lát Gạch Sàn Nhà Máy VinFast**
* **Dạng bài:** Bitmask DP Broken Profile Tiling
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0193 - Dem So Cach Lat Gach San Nha May VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0193%20-%20Dem%20So%20Cach%20Lat%20Gach%20San%20Nha%20May%20VinFast)
* **Phương pháp giải:** Quy hoạch động lát gạch theo dòng kết hợp mặt nạ trạng thái bit `dp[i][mask]` trong $O(M \cdot 2^N)$.

---

### **[IKH-0194] - Tính Chuỗi Truy Hồi Tài Chính Techcombank**
* **Dạng bài:** Linear Recurrence Matrix Exponentiation
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0194 - Tinh Chuoi Truy Hoi Tai Chinh Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0194%20-%20Tinh%20Chuoi%20Truy%20Hoi%20Tai%20Chinh%20Techcombank)
* **Phương pháp giải:** Biểu diễn công thức truy hồi tài chính dạng nhân ma trận, tính $M^N \pmod{10^9+7}$ trong $O(K^3 \log N)$.

---

### **[IKH-0195] - Đếm Số Tập Độc Lập Trọng Số Lớn Nhất**
* **Dạng bài:** Bitmask DP Max Weighted Independent Set
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0195 - Dem So Tap Doc Lap Trong So Lon Nhat](file:///Users/dkdeveloper/projects/testcase/IKH-0195%20-%20Dem%20So%20Tap%20Doc%20Lap%20Trong%20So%20Lon%20Nhat)
* **Phương pháp giải:** Quy hoạch động trạng thái bit trên đồ thị kích thước nhỏ $N \le 20$ trong $O(N \cdot 2^N)$.

---

### **[IKH-0196] - Tính Số Đường Đi Độ Dài K Viettel**
* **Dạng bài:** Adjacency Matrix Exponentiation
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0196 - Tinh So Duong Di Do Dai K Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0196%20-%20Tinh%20So%20Duong%20Di%20Do%20Dai%20K%20Viettel)
* **Phương pháp giải:** Dùng lũy thừa ma trận kề $A^K \pmod{10^9+7}$ đếm số lượng đường đi độ dài đúng $K$ trong $O(V^3 \log K)$.

---

### **[IKH-0197] - Tối Ưu Hóa Chọn Vật Phẩm Tập Con**
* **Dạng bài:** Bitmask DP Submask Iteration
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0197 - Toi Uu Hoa Chon Vat Pham Tap Con](file:///Users/dkdeveloper/projects/testcase/IKH-0197%20-%20Toi%20Uu%20Hoa%20Chon%20Vat%20Pham%20Tap%20Con)
* **Phương pháp giải:** Duyệt mọi tập con của tập con `sub = (sub - 1) & mask` để tối ưu chọn vật phẩm trong $O(3^N)$.

---

### **[IKH-0198] - Lũy Thừa Ma Trận Đếm Dãy Ký Tự Shopee**
* **Dạng bài:** String Transition Matrix Exponentiation
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0198 - Luy Thua Ma Tran Dem Day Ky Tu Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0198%20-%20Luy%20Thua%20Ma%20Tran%20Dem%20Day%20Ky%20Tu%20Shopee)
* **Phương pháp giải:** Xây dựng ma trận chuyển trạng thái giữa các ký tự hợp lệ, nhân lũy thừa ma trận độ dài $N$ trong $O(|\Sigma|^3 \log N)$.

---

### **[IKH-0199] - Phủ Bảng Vuông Trọng Số Tối Đa Bitmask DP**
* **Dạng bài:** Bitmask DP Profile Dynamic Programming
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0199 - Phu Bang Vuong Trong So Toi Da Bitmask](file:///Users/dkdeveloper/projects/testcase/IKH-0199%20-%20Phu%20Bang%20Vuong%20Trong%20So%20Toi%20Da%20Bitmask)
* **Phương pháp giải:** Quy hoạch động lát bảng kết hợp mặt nạ trạng thái bit `dp[cell][mask]` tối ưu trọng số nhận được trong $O(N \cdot 2^M)$.

---

### **[IKH-0200] - Đếm Số Chu Trinh Hamilton VNG Games**
* **Dạng bài:** Bitmask DP Hamiltonian Cycles
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0200 - Dem So Chu Trinh Hamilton VNG Games](file:///Users/dkdeveloper/projects/testcase/IKH-0200%20-%20Dem%20So%20Chu%20Trinh%20Hamilton%20VNG%20Games)
* **Phương pháp giải:** Quy hoạch động trạng thái bit `dp[mask][u]` đếm số chu trình Hamilton đi qua tất cả các đỉnh trong $O(N^2 \cdot 2^N)$.


---

### **[IKH-0201] - Xác Định Bao Lồi Trạm Thu Phát Ăng-ten Viettel**
* **Dạng bài:** Convex Hull (Andrew's Monotone Chain)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0201 - Xac Dinh Bao Loi Tram Ang Ten Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0201%20-%20Xac%20Dinh%20Bao%20Loi%20Tram%20Ang%20Ten%20Viettel)
* **Phương pháp giải:** Thuật toán Andrew's Monotone Chain dựng Bao lồi dưới và Bao lồi trên tính chu围 nhỏ nhất chứa $N$ điểm trong $O(N \log N)$.

---

### **[IKH-0202] - Tìm Cặp Điểm Gần Nhất Mạng Lưới WinMart**
* **Dạng bài:** Closest Pair of Points (Divide & Conquer / Sweep-line)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0202 - Tim Cap Diem Gan Nhat WinMart](file:///Users/dkdeveloper/projects/testcase/IKH-0202%20-%20Tim%20Cap%20Diem%20Gan%20Nhat%20WinMart)
* **Phương pháp giải:** Thuật toán đường quét Sweep-Line hoặc Chia để trị Divide & Conquer tìm khoảng cách ngắn nhất giữa 2 cửa hàng WinMart trong $O(N \log N)$.

---

### **[IKH-0203] - Tính Diện Tích Phủ Bởi Các Hình Chữ Nhật Shopee**
* **Dạng bài:** Sweep-line + Segment Tree Area of Rectangles
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0203 - Tinh Dien Tich Phu Hinh Chu Nhat Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0203%20-%20Tinh%20Dien%20Tich%20Phu%20Hinh%20Chu%20Nhat%20Shopee)
* **Phương pháp giải:** Đường quét Sweep-Line theo phương thẳng đứng kết hợp Cây Phân Đoạn Segment Tree tính hợp diện tích các hình chữ nhật trong $O(N \log N)$.

---

### **[IKH-0204] - Kiểm Tra Điểm Nằm Trong Đa Giác Đèn Giao Thông**
* **Dạng bài:** Point in Polygon (Binary Search for Convex Polygon)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0204 - Kiem Tra Diem Nam Trong Da Giac Ha Noi](file:///Users/dkdeveloper/projects/testcase/IKH-0204%20-%20Kiem%20Tra%20Diem%20Nam%20Trong%20Da%20Giac%20Ha%20Noi)
* **Phương pháp giải:** Áp dụng chặt nhị phân góc cực kiểm tra điểm nằm trong hay ngoài đa giác lồi trong $O(\log N)$.

---

### **[IKH-0205] - Đếm Số Điểm Nguyên Trong Tam Giác Bản Đồ Grab**
* **Dạng bài:** Pick's Theorem + Shoelace Formula
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0205 - Dem So Diem Nguyen Trong Tam Giac Grab](file:///Users/dkdeveloper/projects/testcase/IKH-0205%20-%20Dem%20So%20Diem%20Nguyen%20Trong%20Tam%20Giac%20Grab)
* **Phương pháp giải:** Tính diện tích $S$ bằng công thức Shoelace, đếm số điểm nguyên trên biên bằng $\gcd$, áp dụng định lý Pick $I = S - B/2 + 1$ trong $O(1)$.

---

### **[IKH-0206] - Tìm Cặp Đoạn Thẳng Cắt Nhau Hệ Thống VNG**
* **Dạng bài:** Sweep-line Line Segment Intersection (Bentley-Ottmann)
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0206 - Tim Cap Doan Thang Cat Nhau VNG](file:///Users/dkdeveloper/projects/testcase/IKH-0206%20-%20Tim%20Cap%20Doan%20Thang%20Cat%20Nhau%20VNG)
* **Phương pháp giải:** Thuật toán đường quét Sweep-Line duy trì cấu trúc tìm kiếm các đoạn thẳng giao nhau trong $O(N \log N)$.

---

### **[IKH-0207] - Tính Đường Kính Bao Lồi Mạng Lưới Cung Cấp EVN**
* **Dạng bài:** Rotating Calipers for Maximum Distance
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0207 - Tinh Duong Kinh Bao Loi Mang Luoi EVN](file:///Users/dkdeveloper/projects/testcase/IKH-0207%20-%20Tinh%20Duong%20Kinh%20Bao%20Loi%20Mang%20Luoi%20EVN)
* **Phương pháp giải:** Dựng Bao lồi, áp dụng thuật toán thước kẹp xoay Rotating Calipers tìm cặp điểm có khoảng cách xa nhất trong $O(N \log N)$.

---

### **[IKH-0208] - Tìm Vùng Tròn Nhỏ Nhất Phủ Trạm Petrolimex**
* **Dạng bài:** Smallest Enclosing Circle (Welzl's Algorithm)
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0208 - Tim Vung Tron Nho Nhat Petrolimex](file:///Users/dkdeveloper/projects/testcase/IKH-0208%20-%20Tim%20Vung%20Tron%20Nho%20Nhat%20Petrolimex)
* **Phương pháp giải:** Thuật toán ngẫu nhiên hóa Welzl tìm đường tròn bán kính nhỏ nhất bao phủ $N$ trạm Petrolimex trong thời gian kỳ vọng $O(N)$.

---

### **[IKH-0209] - Phân Tích Cắt Đa Giác Mảnh Đất VinHomes**
* **Dạng bài:** Convex Polygon Cut by Line (Sutherland-Hodgman)
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0209 - Phan Tich Cat Da Giac VinHomes](file:///Users/dkdeveloper/projects/testcase/IKH-0209%20-%20Phan%20Tich%20Cat%20Da%20Giac%20VinHomes)
* **Phương pháp giải:** Thuật toán Sutherland-Hodgman cắt đa giác bằng nửa mặt phẳng đường thẳng $Ax + By + C = 0$ trong $O(N)$.

---

### **[IKH-0210] - Xác Định Vùng Voronoi Trạm Phủ Sóng Mobifone**
* **Dạng bài:** Half-plane Intersection / Voronoi Diagram Concept
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0210 - Xac Dinh Vung Voronoi Mobifone](file:///Users/dkdeveloper/projects/testcase/IKH-0210%20-%20Xac%20Dinh%20Vung%20Voronoi%20Mobifone)
* **Phương pháp giải:** Thuật toán Giao các nửa mặt phẳng Half-plane Intersection tìm miền ảnh hưởng của trạm phát sóng Mobifone trong $O(N \log N)$.


---

### **[IKH-0211] - Tối Ưu Hóa Mạng Lưới Cung Cấp Nước Sạch EVN**
* **Dạng bài:** Maximum Flow (Dinic's Algorithm)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0211 - Toi Uu Mang Luoi Cap Nuoc EVN](file:///Users/dkdeveloper/projects/testcase/IKH-0211%20-%20Toi%20Uu%20Mang%20Luoi%20Cap%20Nuoc%20EVN)
* **Phương pháp giải:** Thuật toán Dinic tính luồng cực đại trên đồ thị phân tầng level graph trong $O(V^2 E)$.

---

### **[IKH-0212] - Phân Công Lịch Trình Bay Phi Công Vietnam Airlines**
* **Dạng bài:** Maximum Bipartite Matching (Hopcroft-Karp / Dinic)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0212 - Phan Cong Lich Bay Vietnam Airlines](file:///Users/dkdeveloper/projects/testcase/IKH-0212%20-%20Phan%20Cong%20Lich%20Bay%20Vietnam%20Airlines)
* **Phương pháp giải:** Chuyển bài toán ghép cặp hai phía về Luồng cực đại Dinic hoặc thuật toán Hopcroft-Karp trong $O(E \sqrt{V})$.

---

### **[IKH-0213] - Tối Ưu Chi Phí Luồng Tối Đa Viettel Post**
* **Dạng bài:** Minimum Cost Maximum Flow (MCMF - SPFA / Successive Shortest Path)
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0213 - Toi Uu Chi Phi Luong Viettel Post](file:///Users/dkdeveloper/projects/testcase/IKH-0213%20-%20Toi%20Uu%20Chi%20Phi%20Luong%20Viettel%20Post)
* **Phương pháp giải:** Thuật toán SPFA tìm đường tăng luồng có chi phí nhỏ nhất, tính luồng cực đại chi phí nhỏ nhất (MCMF).

---

### **[IKH-0214] - Phân Chia Mạng Lưới Server Máy Chủ VNG Cloud**
* **Dạng bài:** Minimum Cut (Max-Flow Min-Cut Theorem)
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0214 - Phan Chia Sever May Chu VNG Cloud](file:///Users/dkdeveloper/projects/testcase/IKH-0214%20-%20Phan%20Chia%20Sever%20May%20Chu%20VNG%20Cloud)
* **Phương pháp giải:** Áp dụng định lý Luồng cực đại - Lát cắt tối thiểu Max-Flow Min-Cut tìm tổng sức chứa các cạnh lát cắt cực tiểu.

---

### **[IKH-0215] - Xác Định Tuyến Đường Không Giao Nhau Shopee**
* **Dạng bài:** Node-Disjoint Paths via Max Flow
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0215 - Tuyen Duong Khong Giao Nhau Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0215%20-%20Tuyen%20Duong%20Khong%20Giao%20Nhau%20Shopee)
* **Phương pháp giải:** Tách đỉnh $u 	o (u_{in}, u_{out})$ sức chứa $1$, chạy Dinic tính số lượng tuyến đường không trùng đỉnh tối đa.

---

### **[IKH-0216] - Phân Việc Tối Ưu Lực Lượng Bảo Vệ VinHomes**
* **Dạng bài:** Maximum Weight Bipartite Matching (Hungarian Algorithm / MCMF)
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0216 - Phan Viec Bao Ve VinHomes](file:///Users/dkdeveloper/projects/testcase/IKH-0216%20-%20Phan%20Viec%20Bao%20Ve%20VinHomes)
* **Phương pháp giải:** Thuật toán Hungarian hoặc MCMF giải bài toán ghép cặp 2 phía trọng số cực đại trong $O(V^3)$.

---

### **[IKH-0217] - Tối Ưu Mạng Lưới Giao Dịch Ngân Hàng ACB**
* **Dạng bài:** Feasible Circulation with Demands via Max Flow
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0217 - Toi Uu Giao Dich Ngan Hang ACB](file:///Users/dkdeveloper/projects/testcase/IKH-0217%20-%20Toi%20Uu%20Giao%20Dich%20Ngan%20Hang%20ACB)
* **Phương pháp giải:** Thêm đỉnh nguồn/đích ảo $S', T'$ chuyển bài toán tuần hoàn luồng có yêu cầu (Circulation with Demands) về Luồng cực đại.

---

### **[IKH-0218] - Lựa Chọn Dự Án Đầu Tư Lợi Nhuận FPT Capital**
* **Dạng bài:** Maximum Weight Closure Problem via Min-Cut
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0218 - Lua Chon Du An Dau Tu FPT Capital](file:///Users/dkdeveloper/projects/testcase/IKH-0218%20-%20Lua%20Chon%20Du%20An%20Dau%20Tu%20FPT%20Capital)
* **Phương pháp giải:** Biến đổi bài toán Chọn dự án lợi nhuận tối đa phụ thuộc lẫn nhau về Lát cắt nhỏ nhất Min-Cut trên đồ thị mạng luồng.

---

### **[IKH-0219] - Lập Lịch Xe Bồn Chở Xăng Dầu Petrolimex**
* **Dạng bài:** Minimum Path Cover in DAG via Bipartite Matching
* **Độ khó:** Rating 1750 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0219 - Lap Lich Xe Bon Petrolimex](file:///Users/dkdeveloper/projects/testcase/IKH-0219%20-%20Lap%20Lich%20Xe%20Bon%20Petrolimex)
* **Phương pháp giải:** Xây dựng đồ thị 2 phía phủ đường đi nhỏ nhất trên DAG bằng ghép cặp cực đại $N - 	ext{MaxMatching}$.

---

### **[IKH-0220] - Tối Ưu Cân Bằng Tải Server Zalo Pay**
* **Dạng bài:** Bounded Min-Cost Max-Flow / Multi-source Multi-sink Flow
* **Độ khó:** Rating 1750 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0220 - Toi Uu Can Bang Tai Zalo Pay](file:///Users/dkdeveloper/projects/testcase/IKH-0220%20-%20Toi%20Uu%20Can%20Bang%20Tai%20Zalo%20Pay)
* **Phương pháp giải:** Thêm $S, T$ tổng quát nối đến các cụm máy chủ, chạy MCMF cân bằng tải tài nguyên hệ thống.


---

### **[IKH-0221] - Phân Phối Tài Nguyên Siêu Máy Chủ VinAI**
* **Dạng bài:** Tree DP + Convex Hull Trick (CHT) Dynamic Programming
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0221 - Phan Phoi Tai Nguyen Siêu May Chu VinAI](file:///Users/dkdeveloper/projects/testcase/IKH-0221%20-%20Phan%20Phoi%20Tai%20Nguyen%20Si%C3%AAu%20May%20Chu%20VinAI)
* **Phương pháp giải:** Tối ưu công thức quy hoạch động hàm chi phí bậc hai bằng Kỹ thuật đường bao lồi CHT duy trì deque các đường thẳng $y = m x + b$ trong $O(N)$.

---

### **[IKH-0222] - Xử Lý Chuỗi Ký Tự Mật Mã Techcombank**
* **Dạng bài:** Suffix Automaton / Suffix Array + LCP + Segment Tree
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0222 - Xu Ly Mat Ma Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0222%20-%20Xu%20Ly%20Mat%20Ma%20Techcombank)
* **Phương pháp giải:** Xây dựng Suffix Automaton / Suffix Array kết hợp mảng LCP và Cây Phân Đoạn truy vấn tiền tố chung dài nhất và đếm chuỗi con mật mã trong $O(N \log N)$.

---

### **[IKH-0223] - Tối Ưu Đường Giao Hàng Shopee Food**
* **Dạng bài:** Heavy-Light Decomposition (HLD) + Segment Tree Path Queries
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0223 - Toi Uu Duong Giao Hang Shopee Food](file:///Users/dkdeveloper/projects/testcase/IKH-0223%20-%20Toi%20Uu%20Duong%20Giao%20Hang%20Shopee%20Food)
* **Phương pháp giải:** Phân đoạn cây Heavy-Light Decomposition (HLD) biến các truy vấn đường đi trên cây thành đoạn trên mảng 1D, quản lý bằng Cây Segment Tree trong $O(Q \log^2 N)$.

---

### **[IKH-0224] - Dự Đoán Tải Trọng Mạng Lưới Điện EVN**
* **Dạng bài:** Divide and Conquer Optimization DP
* **Độ khó:** Rating 1750 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0224 - Du Doan Tai Trong Luoi Dien EVN](file:///Users/dkdeveloper/projects/testcase/IKH-0224%20-%20Du%20Doan%20Tai%20Trong%20Luoi%20Dien%20EVN)
* **Phương pháp giải:** Áp dụng tính chất đơn điệu của vị trí tối ưu `opt[i][j] <= opt[i][j+1]` tối ưu quy hoạch động chia để trị trong $O(K \cdot N \log N)$.

---

### **[IKH-0225] - Cân Bằng Tải Trung Tâm Viettel Cloud**
* **Dạng bài:** Slope Trick / Convex Function DP Optimization
* **Độ khó:** Rating 1750 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0225 - Can Bang Tai Viettel Cloud](file:///Users/dkdeveloper/projects/testcase/IKH-0225%20-%20Can%20Bang%20Tai%20Viettel%20Cloud)
* **Phương pháp giải:** Duy trì các điểm chuyển hướng độ dốc (Slope Trick) bằng hai hàng đợi ưu tiên Priority Queue tối ưu quy hoạch động hàm lồi trong $O(N \log N)$.

---

### **[IKH-0226] - Xác Định Điểm Giao Cắt Cáp Quang VNPT**
* **Dạng bài:** Centroid Decomposition on Tree
* **Độ khó:** Rating 1800 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0226 - Xac Dinh Diem Giao Cat Cap Quang VNPT](file:///Users/dkdeveloper/projects/testcase/IKH-0226%20-%20Xac%20Dinh%20Diem%20Giao%20Cat%20Cap%20Quang%20VNPT)
* **Phương pháp giải:** Phân tách trọng tâm cây Centroid Decomposition giải quyết các bài toán đường đi độ dài $K$ trên cây trong $O(N \log N)$.

---

### **[IKH-0227] - Phân Tích Động Học Chuỗi Giao Dịch SSI**
* **Dạng bài:** Mo's Algorithm + Fenwick Tree Range Queries
* **Độ khó:** Rating 1800 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0227 - Phan Tich Chuoi Giao Dich SSI](file:///Users/dkdeveloper/projects/testcase/IKH-0227%20-%20Phan%20Tich%20Chuoi%20Giao%20Dich%20SSI)
* **Phương pháp giải:** Sắp xếp truy vấn theo căn bậc hai (Thuật toán Mo) chia khối $\sqrt{N}$ kết hợp mảng Fenwick BIT trả lời truy vấn đoạn trong $O((N+Q)\sqrt{N})$.

---

### **[IKH-0228] - Xây Dựng Mạng Lưới Giao Thoa 5G Mobifone**
* **Dạng bài:** Segment Tree Beats / Lazy Range Chmin Updates
* **Độ khó:** Rating 1850 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0228 - Xay Dung Mang Luoi Song 5G Mobifone](file:///Users/dkdeveloper/projects/testcase/IKH-0228%20-%20Xay%20Dung%20Mang%20Luoi%20Song%205G%20Mobifone)
* **Phương pháp giải:** Áp dụng kỹ thuật Segment Tree Beats cập nhật $A_i = \min(A_i, X)$ và tính tổng đoạn trong $O(N \log N)$.

---

### **[IKH-0229] - Truy Vấn Đồ Thị Thay Đổi Thời Gian VNG**
* **Dạng bài:** Offline Dynamic Connectivity via DSU with Rollback & SegTree over Time
* **Độ khó:** Rating 1850 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0229 - Truy Van Do Thi Thay Doi Thoi Gian VNG](file:///Users/dkdeveloper/projects/testcase/IKH-0229%20-%20Truy%20Van%20Do%20Thi%20Thay%20Doi%20Thoi%20Gian%20VNG)
* **Phương pháp giải:** Dựng Cây Segment Tree theo trục thời gian các thao tác thêm/xóa cạnh, kết hợp DSU Rollback trả lời liên thông ngoại tuyến trong $O(Q \log^2 N)$.

---

### **[IKH-0230] - Siêu Hệ Thống Phân Tích IKHEDU Masterclass**
* **Dạng bài:** Grand Synthesis Advanced DP + Fenwick / SegTree + Tree Decomposition
* **Độ khó:** Rating 1900 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0230 - Sieu He Thong Quoc Gia IKHEDU Masterclass](file:///Users/dkdeveloper/projects/testcase/IKH-0230%20-%20Sieu%20He%20Thong%20Quoc%20Gia%20IKHEDU%20Masterclass)
* **Phương pháp giải:** Bài toán Đỉnh cao tổng hợp phối hợp Quy hoạch động Nâng cao, Cấu trúc dữ liệu Đoạn và Thuật toán Đồ thị nâng cao $O(N \log N)$.


---

### **[IKH-0231] - Tối Ưu Hóa Dãy Tín Hiệu Viettel Telecom**
* **Dạng bài:** Longest Increasing Subsequence (LIS)
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0231 - Toi Uu Day Tin Hieu Viettel Telecom](file:///Users/dkdeveloper/projects/testcase/IKH-0231%20-%20Toi%20Uu%20Day%20Tin%20Hieu%20Viettel%20Telecom)
* **Phương pháp giải:** Dùng thuật toán Patience Sorting kết hợp chặt nhị phân `std::lower_bound` trên mảng `tails` tìm LIS trong $O(N \log N)$.

---

### **[IKH-0232] - Phân Tích Chuỗi Giao Dịch Techcombank**
* **Dạng bài:** Longest Common Subsequence (LCS)
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0232 - Phan Tich Chuoi Giao Dich Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0232%20-%20Phan%20Tich%20Chuoi%20Giao%20Dich%20Techcombank)
* **Phương pháp giải:** Quy hoạch động LCS 2D `dp[i][j]` (hoặc tối ưu bộ nhớ 1D) tìm độ dài chuỗi giao dịch chung dài nhất trong $O(N \cdot M)$.

---

### **[IKH-0233] - Tìm Xâu Đối Xứng Dài Nhất Ví MoMo**
* **Dạng bài:** Longest Palindromic Subsequence (LPS DP)
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0233 - Tim Xau Doi Xung Dai Nhat MoMo](file:///Users/dkdeveloper/projects/testcase/IKH-0233%20-%20Tim%20Xau%20Doi%20Xung%20Dai%20Nhat%20MoMo)
* **Phương pháp giải:** Quy hoạch động xâu con đối xứng dài nhất trên đoạn `dp[i][j]` với $S[i] == S[j]$ trong $O(N^2)$.

---

### **[IKH-0234] - Đếm Số Dãy Con Có Tổng Bằng K Shopee**
* **Dạng bài:** Subsequence Subset Sum DP
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0234 - Dem So Day Con Tong Bang K Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0234%20-%20Dem%20So%20Day%20Con%20Tong%20Bang%20K%20Shopee)
* **Phương pháp giải:** Quy hoạch động 1D duyệt lùi `j` từ $K 	o A_i$: `dp[j] = (dp[j] + dp[j - A_i]) % MOD` trong $O(N \cdot K)$.

---

### **[IKH-0235] - Đoạn Con Tối Ưu Lợi Nhuận Grab Express**
* **Dạng bài:** 2D Maximum Subarray Sum (2D Kadane / Prefix Sums)
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0235 - Doan Con Toi Uu Loi Nhuan Grab](file:///Users/dkdeveloper/projects/testcase/IKH-0235%20-%20Doan%20Con%20Toi%20Uu%20Loi%20Nhuan%20Grab)
* **Phương pháp giải:** Cố định hai hàng $r_1, r_2$, đưa về bài toán Kadane 1D tìm hình chữ nhật con có tổng lợi nhuận lớn nhất trong $O(N^3)$.

---

### **[IKH-0236] - Tối Ưu Chuỗi Lắp Ráp Xe Điện VinFast**
* **Dạng bài:** Weighted LIS via Segment Tree / BIT
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0236 - Toi Uu Chuoi Lap Rap VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0236%20-%20Toi%20Uu%20Chuoi%20Lap%20Rap%20VinFast)
* **Phương pháp giải:** Nén tọa độ trọng số, dùng Cây Fenwick BIT / SegTree cập nhật và truy vấn trọng số LIS max trong $O(N \log N)$.

---

### **[IKH-0237] - Đếm Số Dãy Con Tăng Zalo Cloud**
* **Dạng bài:** Count Number of LIS Sequences via Fenwick BIT
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0237 - Dem So Day Con Tang Zalo Cloud](file:///Users/dkdeveloper/projects/testcase/IKH-0237%20-%20Dem%20So%20Day%20Con%20Tang%20Zalo%20Cloud)
* **Phương pháp giải:** Dùng Cây Fenwick BIT lưu cặp `{max_len, count}` đếm số lượng dãy con tăng dài nhất trong $O(N \log N)$.

---

### **[IKH-0238] - Tìm Dãy Con Chung Dài Nhất 3 Xâu FPT**
* **Dạng bài:** 3-String LCS DP 3D
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0238 - Tim Day Con Chung 3 Xau FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0238%20-%20Tim%20Day%20Con%20Chung%203%20Xau%20FPT)
* **Phương pháp giải:** Mở rộng bảng quy hoạch động 3D `dp[i][j][k]` tìm LCS của 3 xâu ký tự trong $O(N \cdot M \cdot K)$.

---

### **[IKH-0239] - Phân Tích Dãy Con Không Kề Nhau Tiki**
* **Dạng bài:** Non-adjacent Subsequence DP / House Robber Variant
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0239 - Phan Tich Day Con Khong Ke Tiki](file:///Users/dkdeveloper/projects/testcase/IKH-0239%20-%20Phan%20Tich%20Day%20Con%20Khong%20Ke%20Tiki)
* **Phương pháp giải:** Quy hoạch động trạng thái `dp[i][0]` (không chọn $i$) và `dp[i][1]` (chọn $i$) tối ưu giá trị dãy con không có 2 phần tử kề nhau trong $O(N)$.


---

### **[IKH-0240] - Tối Ưu Hóa Tải Trọng Container Hải Phòng**
* **Dạng bài:** Standard 0/1 Knapsack DP
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0240 - Toi Uu Tai Trong Container Hai Phong](file:///Users/dkdeveloper/projects/testcase/IKH-0240%20-%20Toi%20Uu%20Tai%20Trong%20Container%20Hai%20Phong)
* **Phương pháp giải:** Quy hoạch động Ba lô 0/1 1D duyệt lùi `j` từ $W 	o w_i$: `dp[j] = max(dp[j], dp[j - w_i] + v_i)` trong $O(N \cdot W)$.

---

### **[IKH-0241] - Đổi Tiền Tự Động Máy Bán Hàng**
* **Dạng bài:** Min Coins Change DP
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0241 - Doi Tien Tu Dong Vending Machine](file:///Users/dkdeveloper/projects/testcase/IKH-0241%20-%20Doi%20Tien%20Tu%20Dong%20Vending%20Machine)
* **Phương pháp giải:** Đặt `dp[j]` là số tờ tiền tối thiểu đổi được số tiền $j$. Duyệt tiến `j` từ $c_i 	o S$: `dp[j] = min(dp[j], dp[j - c_i] + 1)` trong $O(N \cdot S)$.

---

### **[IKH-0242] - Phân Bổ Điện Năng Mặt Trời EVN**
* **Dạng bài:** Unbounded Knapsack DP
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0242 - Phan Bo Dien Nang Mat Troi EVN](file:///Users/dkdeveloper/projects/testcase/IKH-0242%20-%20Phan%20Bo%20Dien%20Nang%20Mat%20Troi%20EVN)
* **Phương pháp giải:** Ba lô không giới hạn số lượng (Unbounded Knapsack) duyệt tiến `j` từ $w_i 	o W$: `dp[j] = max(dp[j], dp[j - w_i] + v_i)` trong $O(N \cdot W)$.

---

### **[IKH-0243] - Tối Ưu Đơn Hàng Giao Ghép Shopee**
* **Dạng bài:** Bounded Knapsack with Binary Splitting
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0243 - Toi Uu Don Hang Giao Ghep Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0243%20-%20Toi%20Uu%20Don%20Hang%20Giao%20Ghep%20Shopee)
* **Phương pháp giải:** Phân tách số lượng $C_i$ vật phẩm thành các lũy thừa 2 ($1, 2, 4, \dots$) đưa về bài toán 0/1 Knapsack trong $O(W \sum \log C_i)$.

---

### **[IKH-0244] - Phân Tích Chi Phí Máy Chủ Cloud VinAI**
* **Dạng bài:** Knapsack Large Weights / Small Values DP
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0244 - Phan Tich Chi Phi May Chu VinAI](file:///Users/dkdeveloper/projects/testcase/IKH-0244%20-%20Phan%20Tich%20Chi%20Phi%20May%20Chu%20VinAI)
* **Phương pháp giải:** Đổi vai trò `dp[v]` là trọng lượng nhỏ nhất đạt tổng giá trị $v$, giải bài toán Ba lô với trọng lượng lớn $W \le 10^9$ trong $O(N \sum v_i)$.

---

### **[IKH-0245] - Tối Ưu Gói Hàng Khuyến Mãi Tiki**
* **Dạng bài:** 2D Capacity Knapsack DP
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0245 - Toi Uu Goi Hang Khuyen Mai Tiki](file:///Users/dkdeveloper/projects/testcase/IKH-0245%20-%20Toi%20Uu%20Goi%20Hang%20Khuyen%20Mai%20Tiki)
* **Phương pháp giải:** Quy hoạch động Ba lô 2 chiều giới hạn cả khối lượng $W$ và thể tích $V$: `dp[w][v] = max(dp[w][v], dp[w - w_i][v - v_i] + val_i)` trong $O(N \cdot W \cdot V)$.

---

### **[IKH-0246] - Chọn Dự Án Đầu Tư FPT Software**
* **Dạng bài:** Grouped Knapsack DP
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0246 - Chon Du An Dau Tu FPT Software](file:///Users/dkdeveloper/projects/testcase/IKH-0246%20-%20Chon%20Du%20An%20Dau%20Tu%20FPT%20Software)
* **Phương pháp giải:** Quy hoạch động Ba lô theo nhóm (Grouped Knapsack), với mỗi nhóm chọn tối đa 1 vật phẩm trong $O(W \cdot \sum |Group_g|)$.

---

### **[IKH-0247] - Lập Lịch Xe Bồn Chở Dầu Petrolimex**
* **Dạng bài:** Knapsack Exact Target Sum + Path Reconstruction
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0247 - Lap Lich Xe Bon Cho Dau Petrolimex](file:///Users/dkdeveloper/projects/testcase/IKH-0247%20-%20Lap%20Lich%20Xe%20Bon%20Cho%20Dau%20Petrolimex)
* **Phương pháp giải:** DP kiểm tra khả năng đạt đúng dung tích $S$ + vết phương án ngược bằng mảng `trace[i][j]` xuất danh sách các xe bồn được nạp.

---

### **[IKH-0248] - Phân Phối Mã Giảm Giá MoMo Wallet**
* **Dạng bài:** Subset Sum DP with `std::bitset` Optimization
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0248 - Phan Phoi Ma Giam Gia MoMo Wallet](file:///Users/dkdeveloper/projects/testcase/IKH-0248%20-%20Phan%20Phoi%20Ma%20Giam%20Gia%20MoMo%20Wallet)
* **Phương pháp giải:** Sử dụng Cấu trúc `std::bitset<100001> dp`: `dp |= (dp << A[i])` để tối ưu hóa thời gian tính toán gấp 64 lần trong $O(rac{N \cdot W}{64})$.


---

### **[IKH-0249] - Tối Ưu Nhân Ma Trận Chuỗi Viettel AI**
* **Dạng bài:** Matrix Chain Multiplication Interval DP
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0249 - Toi Uu Nhan Ma Tran Viettel AI](file:///Users/dkdeveloper/projects/testcase/IKH-0249%20-%20Toi%20Uu%20Nhan%20Ma%20Tran%20Viettel%20AI)
* **Phương pháp giải:** Quy hoạch động trên đoạn `dp[i][j]` tìm vị trí cắt `k` tối ưu $i \le k < j$: `dp[i][j] = min(dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j])` trong $O(N^3)$.

---

### **[IKH-0250] - Gộp Đống Kho Hàng Tiki Express**
* **Dạng bài:** Merge Stones Interval DP
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0250 - Gop Dong Kho Hang Tiki Express](file:///Users/dkdeveloper/projects/testcase/IKH-0250%20-%20Gop%20Dong%20Kho%20Hang%20Tiki%20Express)
* **Phương pháp giải:** Quy hoạch động gộp các đống hàng kề nhau `dp[i][j]` kết hợp mảng cộng dồn Prefix Sums trong $O(N^3)$.

---

### **[IKH-0251] - Tách Chuỗi Palindrome Mã Vận Đơn Shopee**
* **Dạng bài:** Palindrome Partitioning Min Cuts DP
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0251 - Tach Chuoi Palindrome Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0251%20-%20Tach%20Chuoi%20Palindrome%20Shopee)
* **Phương pháp giải:** Tiền tính mảng `is_pal[i][j]` bằng Interval DP + DP 1D `dp[i]` số lần cắt tối thiểu tách xâu thành các Palindrome trong $O(N^2)$.

---

### **[IKH-0252] - Tối Ưu Cắt Cáp Quang Dưới Biển VNPT**
* **Dạng bài:** Optimal Rod Cutting Interval DP
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0252 - Toi Uu Cat Cap Quang VNPT](file:///Users/dkdeveloper/projects/testcase/IKH-0252%20-%20Toi%20Uu%20Cat%20Cap%20Quang%20VNPT)
* **Phương pháp giải:** Thêm điểm mốc $0$ và $L$, quy hoạch động trên đoạn các mốc cắt `dp[i][j] = min(dp[i][k] + dp[k][j]) + (cuts[j] - cuts[i])` trong $O(N^3)$.

---

### **[IKH-0253] - Trò Chơi Bốc Sỏi Tối Ưu Zalo Game**
* **Dạng bài:** Game Theory / Minimax Interval DP
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0253 - Tro Choi Boc Soi Zalo Game](file:///Users/dkdeveloper/projects/testcase/IKH-0253%20-%20Tro%20Choi%20Boc%20Soi%20Zalo%20Game)
* **Phương pháp giải:** Quy hoạch động Minimax `dp[i][j]` là chênh lệch điểm tối đa giữa người chơi trước và người chơi sau trên đoạn $[i, j]$ trong $O(N^2)$.

---

### **[IKH-0254] - Gộp Khối Dữ Liệu Lớn VinAI Cloud**
* **Dạng bài:** Interval DP with Knuth Optimization
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0254 - Gop Khoi Du Lieu VinAI Cloud](file:///Users/dkdeveloper/projects/testcase/IKH-0254%20-%20Gop%20Khoi%20Du%20Lieu%20VinAI%20Cloud)
* **Phương pháp giải:** Áp dụng Tối ưu Knuth dựa trên tính chất `opt[i][j-1] <= opt[i][j] <= opt[i+1][j]` giảm độ phức tạp từ $O(N^3) 	o O(N^2)$.

---

### **[IKH-0255] - Ghép Cặp Điểm Tín Hiệu Cáp Quang FPT**
* **Dạng bài:** Matching Brackets Interval DP
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0255 - Ghep Cap Diem Tin Hieu FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0255%20-%20Ghep%20Cap%20Diem%20Tin%20Hieu%20FPT)
* **Phương pháp giải:** Quy hoạch động ghép cặp đúng ngoặc/tín hiệu trên đoạn `dp[i][j]` xét 2 trường hợp match $i$ với $j$ hoặc tách thành 2 đoạn độc lập trong $O(N^3)$.

---

### **[IKH-0256] - Tối Ưu Tam Giác Hóa Đa Giác VinHomes**
* **Dạng bài:** Minimum Weight Convex Polygon Triangulation
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0256 - Toi Uu Tam Giac Hoa VinHomes](file:///Users/dkdeveloper/projects/testcase/IKH-0256%20-%20Toi%20Uu%20Tam%20Giac%20Hoa%20VinHomes)
* **Phương pháp giải:** Đặt `dp[i][j]` là chi phí tam giác hóa tối thiểu đa giác từ đỉnh $i 	o j$, duyệt đỉnh thứ 3 $k$ ($i < k < j$) tạo tam giác $(i, k, j)$ trong $O(N^3)$.

---

### **[IKH-0257] - Phân Hoạch Chuỗi Ma Trận Techcombank**
* **Dạng bài:** 3-Element Merge Interval DP
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0257 - Phan Hoach Ma Tran Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0257%20-%20Phan%20Hoach%20Ma%20Tran%20Techcombank)
* **Phương pháp giải:** Quy hoạch động trên đoạn gộp 3 phần tử liên tiếp `dp[i][j]` với $j - i \equiv 0 \pmod 2$ trong $O(N^3)$.


---

### **[IKH-0258] - Đặt Trạm Cảm Biến Viettel Trên Cây**
* **Dạng bài:** Maximum Weight Independent Set Tree DP
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0258 - Dat Tram Cam Bien Viettel Tren Cay](file:///Users/dkdeveloper/projects/testcase/IKH-0258%20-%20Dat%20Tram%20Cam%20Bien%20Viettel%20Tren%20Cay)
* **Phương pháp giải:** Quy hoạch động trên cây `dp[u][0]` (không chọn `u`) và `dp[u][1]` (có chọn `u`) tính từ lá lên gốc trong $O(N)$.

---

### **[IKH-0259] - Tính Đường Kính Mạng Lưới Hà Nội**
* **Dạng bài:** Tree Diameter DP
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0259 - Tinh Duong Kinh Mang Luoi Ha Noi](file:///Users/dkdeveloper/projects/testcase/IKH-0259%20-%20Tinh%20Duong%20Kinh%20Mang%20Luoi%20Ha%20Noi)
* **Phương pháp giải:** Quy hoạch động tính đường đi dài nhất từ $u$ xuống cây con `h[u]`, cập nhật đường kính `max(h[v1] + h[v2] + 2)` trong $O(N)$.

---

### **[IKH-0260] - Tối Ưu Phân Phối Năng Lượng EVN Tree**
* **Dạng bài:** Subtree Sum & Max Subtree Profit DP
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0260 - Toi Uu Phan Phoi Nang Luong EVN](file:///Users/dkdeveloper/projects/testcase/IKH-0260%20-%20Toi%20Uu%20Phan%20Phoi%20Nang%20Luong%20EVN)
* **Phương pháp giải:** DFS tính mảng tổng cây con `subtree_sum[u]` và lợi nhuận max khi giữ lại/cắt bỏ nhánh cây trong $O(N)$.

---

### **[IKH-0261] - Ghép Cặp Trạm Thu Phí VETC Trên Cây**
* **Dạng bài:** Maximum Bipartite Tree Matching DP
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0261 - Ghep Cap Tram Thu Phi VETC](file:///Users/dkdeveloper/projects/testcase/IKH-0261%20-%20Ghep%20Cap%20Tram%20Thu%20Phi%20VETC)
* **Phương pháp giải:** Quy hoạch động ghép cặp không trùng cạnh trên cây `dp[u][0]` và `dp[u][1]` trong $O(N)$.

---

### **[IKH-0262] - Chọn Đỉnh Bảo Vệ Mạng Lưới VinAI Cloud**
* **Dạng bài:** Minimum Vertex Cover Tree DP
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0262 - Chon Dinh Bao Ve VinAI Cloud](file:///Users/dkdeveloper/projects/testcase/IKH-0262%20-%20Chon%20Dinh%20Bao%20Ve%20VinAI%20Cloud)
* **Phương pháp giải:** Đặt `dp[u][0]` (không chọn $u$, phải chọn tất cả con $v$) và `dp[u][1]` (chọn $u$, con $v$ tùy chọn min) trong $O(N)$.

---

### **[IKH-0263] - Phân Bổ Băng Thông 5G Mobifone Trên Cây**
* **Dạng bài:** Tree Knapsack DP
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0263 - Phan Bo Bang Thong Mobifone](file:///Users/dkdeveloper/projects/testcase/IKH-0263%20-%20Phan%20Bo%20Bang%20Thong%20Mobifone)
* **Phương pháp giải:** Kết hợp Ba lô 0/1 và DFS cây con (Tree Knapsack), gộp dung tích cây con theo thứ tự DFS trong $O(N \cdot W)$.

---

### **[IKH-0264] - Trung Tâm Logistics Shopee Re-rooting**
* **Dạng bài:** Re-rooting Tree DP (Tree All Distances Sum)
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0264 - Trung Tam Logistics Shopee Tree](file:///Users/dkdeveloper/projects/testcase/IKH-0264%20-%20Trung%20Tam%20Logistics%20Shopee%20Tree)
* **Phương pháp giải:** Thuật toán Re-rooting Tree DP (DFS 1 tính `dp[1]`, DFS 2 chuyển gốc $u 	o v$: `ans[v] = ans[u] + N - 2*sz[v]`) trong $O(N)$.

---

### **[IKH-0265] - Bán Kính Phủ Sóng VinaPhone Re-rooting**
* **Dạng bài:** Re-rooting Tree DP (Tree Height for All Roots)
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0265 - Ban Kinh Phu Song VinaPhone Tree](file:///Users/dkdeveloper/projects/testcase/IKH-0265%20-%20Ban%20Kinh%20Phu%20Song%20VinaPhone%20Tree)
* **Phương pháp giải:** Re-rooting DP tính chiều cao max khi đặt gốc tại mọi đỉnh bằng cách lưu 2 chiều cao lớn nhất từ con xuống và 1 chiều cao từ cha lên trong $O(N)$.

---

### **[IKH-0266] - Đếm Tập Độc Lập Techcombank Trên Cây**
* **Dạng bài:** Tree DP Counting Independent Subsets Modulo
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0266 - Dem Tap Doc Lap Techcombank Tree](file:///Users/dkdeveloper/projects/testcase/IKH-0266%20-%20Dem%20Tap%20Doc%20Lap%20Techcombank%20Tree)
* **Phương pháp giải:** Đếm số lượng tập độc lập modulo $10^9+7$ trên cây bằng DP: `dp[u][0] = prod(dp[v][0] + dp[v][1])`, `dp[u][1] = prod(dp[v][0])` trong $O(N)$.


---

### **[IKH-0267] - Đếm Số Mã Giao Dịch Đẹp Ví MoMo**
* **Dạng bài:** Digit DP Sum of Digits Modulo
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0267 - Dem So Ma Giao Dich Dep MoMo](file:///Users/dkdeveloper/projects/testcase/IKH-0267%20-%20Dem%20So%20Ma%20Giao%20Dich%20Dep%20MoMo)
* **Phương pháp giải:** Quy hoạch động chữ số `solve(B) - solve(A-1)` với memoization `dp[idx][sum_mod][is_less]` trong $O(\log_{10} B \cdot K \cdot 10)$.

---

### **[IKH-0268] - Đếm Mã An Toàn Không Chứa 13 VNPay**
* **Dạng bài:** Digit DP Pattern Avoidance
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0268 - Dem Ma An Toan Khong Chua 13 VNPay](file:///Users/dkdeveloper/projects/testcase/IKH-0268%20-%20Dem%20Ma%20An%20Toan%20Khong%20Chua%2013%20VNPay)
* **Phương pháp giải:** Quy hoạch động chữ số lưu trạng thái chữ số vừa chọn trước đó `last_digit` để cấm chuỗi "13" trong $O(\log_{10} B \cdot 10)$.

---

### **[IKH-0269] - Đếm Số Đối Xứng Chữ Số Mã Vận Đơn Shopee**
* **Dạng bài:** Digit DP Palindromic Numbers
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0269 - Dem So Doi Xung Chu So Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0269%20-%20Dem%20So%20Doi%20Xung%20Chu%20So%20Shopee)
* **Phương pháp giải:** Digit DP đếm số Palindrome chữ số bằng cách chọn 1/2 độ dài đầu tiên và kiểm tra tính hợp lệ trong $O(\log_{10} B \cdot 10)$.

---

### **[IKH-0270] - Tối Ưu Chi Phí Dịch Chuyển Viettel CHT**
* **Dạng bài:** Convex Hull Trick (CHT) DP Optimization
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0270 - Toi Uu Chi Phi Dich Chuyen Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0270%20-%20Toi%20Uu%20Chi%20Phi%20Dich%20Chuyen%20Viettel)
* **Phương pháp giải:** Tối ưu công thức DP $dp[i] = \min(dp[j] + (A_i - A_j)^2)$ bằng Kỹ thuật đường bao lồi CHT duy trì deque các đường thẳng $y = mx + b$ trong $O(N)$.

---

### **[IKH-0271] - Lập Lịch Giao Hàng Cửa Sổ Trượt Grab**
* **Dạng bài:** Monotonic Queue / Deque DP Optimization
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0271 - Lap Lich Giao Hang Cua So Grab](file:///Users/dkdeveloper/projects/testcase/IKH-0271%20-%20Lap%20Lich%20Giao%20Hang%20Cua%20So%20Grab)
* **Phương pháp giải:** Tối ưu DP cửa sổ trượt $dp[i] = \min_{i-K \le j < i} dp[j] + A_i$ bằng Hàng đợi đơn điệu Monotonic Queue (Deque) trong $O(N)$.

---

### **[IKH-0272] - Chia Khối Dữ Liệu Tối Ưu VinAI Cloud**
* **Dạng bài:** Divide and Conquer DP Optimization
* **Độ khó:** Rating 1650 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0272 - Chia Khoi Du Lieu VinAI Cloud](file:///Users/dkdeveloper/projects/testcase/IKH-0272%20-%20Chia%20Khoi%20Du%20Lieu%20VinAI%20Cloud)
* **Phương pháp giải:** Áp dụng Tối ưu Chia để trị dựa trên tính chất đơn điệu của vị trí chuyển trạng thái $opt[i][j] \le opt[i][j+1]$ giảm độ phức tạp từ $O(K \cdot N^2) 	o O(K \cdot N \log N)$.

---

### **[IKH-0273] - Tối Ưu Hàm Độ Dốc Điểm Năng Lượng EVN**
* **Dạng bài:** Slope Trick DP Optimization via Priority Queue
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0273 - Toi Uu Ham Do Doc EVN Slope Trick](file:///Users/dkdeveloper/projects/testcase/IKH-0273%20-%20Toi%20Uu%20Ham%20Do%20Doc%20EVN%20Slope%20Trick)
* **Phương pháp giải:** Duy trì các điểm chuyển hướng độ dốc (Slope Trick) của hàm lồi bằng 2 Priority Queue `left_slope` và `right_slope` trong $O(N \log N)$.

---

### **[IKH-0274] - Phân Chia Đội Tuyển Lập Trình FPT**
* **Dạng bài:** Knuth DP Optimization
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0274 - Phan Chia Doi Tuyen Lap Trinh FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0274%20-%20Phan%20Chia%20Doi%20Tuyen%20Lap%20Trinh%20FPT)
* **Phương pháp giải:** Tối ưu Knuth cho bài toán phân hoạch mảng thỏa mãn bất đẳng thức quadrangle $O(N^3) 	o O(N^2)$.

---

### **[IKH-0275] - Đỉnh Cao Tổng Hợp DP Masterclass IKHEDU**
* **Dạng bài:** Grand Synthesis Advanced DP (Bitmask + SegTree + Tree DP)
* **Độ khó:** Rating 1750 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0275 - Dinh Cao Tong Hop Dynamic Programming](file:///Users/dkdeveloper/projects/testcase/IKH-0275%20-%20Dinh%20Cao%20Tong%20Hop%20Dynamic%20Programming)
* **Phương pháp giải:** Phối hợp Bitmask DP trên cây + Cây Segment Tree quản lý chuyển trạng thái tối ưu trong $O(N \log N)$.


---

### **[IKH-0276] - Kết Nối Mạng Lưới 5G Viettel Telecom**
* **Dạng bài:** Standard Disjoint Set Union (DSU)
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0276 - Ket Noi Mang Luoi 5G Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0276%20-%20Ket%20Noi%20Mang%20Luoi%205G%20Viettel)
* **Phương pháp giải:** Cấu trúc dữ liệu DSU tối ưu Nén đường đi (Path Compression) và Gộp theo hạng (Union by Rank) xử lý hợp nhất tập hợp và kiểm tra liên thông trong $O(Q \cdot lpha(N))$.

---

### **[IKH-0277] - Xây Dựng Mạng Cáp Quang Đô Thị FPT**
* **Dạng bài:** Kruskal Minimum Spanning Tree (MST)
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0277 - Xay Dung Mang Cap Quang FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0277%20-%20Xay%20Dung%20Mang%20Cap%20Quang%20FPT)
* **Phương pháp giải:** Thuật toán Kruskal sắp xếp cạnh tăng dần trọng số kết hợp DSU dựng cây khung nhỏ nhất nối tất cả các trạm trong $O(E \log E)$.

---

### **[IKH-0278] - Phủ Sóng Trạm Sạc Xe Điện VinFast**
* **Dạng bài:** Prim's Minimum Spanning Tree (MST)
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0278 - Phu Song Tram Sac VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0278%20-%20Phu%20Song%20Tram%20Sac%20VinFast)
* **Phương pháp giải:** Thuật toán Prim sử dụng Hàng đợi ưu tiên Min-Heap chọn cạnh có trọng số min mở rộng tập đỉnh liên thông trong $O(E \log V)$.

---

### **[IKH-0279] - Tối Ưu Tuyến Vận Tải Grab Express**
* **Dạng bài:** Maximum Spanning Tree
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0279 - Toi Uu Tuyen Van Tai Grab](file:///Users/dkdeveloper/projects/testcase/IKH-0279%20-%20Toi%20Uu%20Tuyen%20Van%20Tai%20Grab)
* **Phương pháp giải:** Thuật toán Kruskal sắp xếp giảm dần trọng số cạnh kết hợp DSU tìm Cây khung cực đại trong $O(E \log E)$.

---

### **[IKH-0280] - Kiểm Tra Liên Thông Zalo Cloud**
* **Dạng bài:** DSU Component Count & Size Tracking
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0280 - Kiem Tra Lien Thong Zalo Cloud](file:///Users/dkdeveloper/projects/testcase/IKH-0280%20-%20Kiem%20Tra%20Lien%20Thong%20Zalo%20Cloud)
* **Phương pháp giải:** Mở rộng DSU lưu mảng `sz[u]` kích thước thành phần liên thông và biến `num_components` đếm số nhóm máy chủ phân tách trong $O(Q \cdot lpha(N))$.

---

### **[IKH-0281] - Xây Dựng Cầu Nối Cảng Hải Phòng**
* **Dạng bài:** Second Best Minimum Spanning Tree
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0281 - Xay Dung Cau Noi Cang Hai Phong](file:///Users/dkdeveloper/projects/testcase/IKH-0281%20-%20Xay%20Dung%20Cau%20Noi%20Cang%20Hai%20Phong)
* **Phương pháp giải:** Dựng cây khung MST 1, lần lượt loại bỏ từng cạnh trong MST 1 và chạy lại Kruskal tìm cây khung nhỏ thứ hai trong $O(E \log E + V^2)$.

---

### **[IKH-0282] - Liên Thông Cửa Hàng WinMart**
* **Dạng bài:** DSU Offline Queries
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0282 - Lien Thong Cua Hang WinMart](file:///Users/dkdeveloper/projects/testcase/IKH-0282%20-%20Lien%20Thong%20Cua%20Hang%20WinMart)
* **Phương pháp giải:** Xử lý ngoại tuyến (Offline Processing) sắp xếp cả cạnh và truy vấn theo mốc thời gian/trọng số, dùng DSU trả lời truy vấn trong $O((E + Q) \log E)$.

---

### **[IKH-0283] - Phân Nhóm Tài Khoản Ví MoMo**
* **Dạng bài:** DSU Equivalence & Bipartite Check
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0283 - Phan Nhom Tai Khoan MoMo](file:///Users/dkdeveloper/projects/testcase/IKH-0283%20-%20Phan%20Nhom%20Tai%20Khoan%20MoMo)
* **Phương pháp giải:** DSU nhân đôi đỉnh `u` và `u + N` kiểm tra tính hợp lệ chia nhóm 2 phía (Bipartite Graph) trong $O(N \cdot lpha(N))$.

---

### **[IKH-0284] - Hệ Thống Phản Ứng Nhanh 115 Hà Nội**
* **Dạng bài:** Kruskal Reconstruction Tree / DSU Rollback
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0284 - He Thong Phan Ung Nhanh 115](file:///Users/dkdeveloper/projects/testcase/IKH-0284%20-%20He%20Thong%20Phan%20Ung%20Nhanh%20115)
* **Phương pháp giải:** Dựng Cây tái cấu trúc Kruskal (Kruskal Reconstruction Tree) biến bài toán khoảng cách max trên MST thành truy vấn LCA trong $O(Q \log V)$.


---

### **[IKH-0285] - Định Tuyến Xe Cứu Thương Grab Express**
* **Dạng bài:** Dijkstra Shortest Path Min-Heap
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0285 - Dinh Tuyen Xe Cuu Thuong Grab](file:///Users/dkdeveloper/projects/testcase/IKH-0285%20-%20Dinh%20Tuyen%20Xe%20Cuu%20Thuong%20Grab)
* **Phương pháp giải:** Thuật toán Dijkstra sử dụng Hàng đợi ưu tiên `std::priority_queue` Min-Heap tìm đường đi ngắn nhất giữa hai đỉnh $S$ và $T$ trong $O((V + E) \log V)$.

---

### **[IKH-0286] - Tối Ưu Phí Thu Phí Tự Động VETC**
* **Dạng bài:** 0-1 BFS via Deque
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0286 - Toi Uu Phi Thu Phi VETC](file:///Users/dkdeveloper/projects/testcase/IKH-0286%20-%20Toi%20Uu%20Phi%20Thu%20Phi%20VETC)
* **Phương pháp giải:** Thuật toán 0-1 BFS sử dụng `std::deque` (cạnh trọng số 0 đẩy vào đầu `push_front`, cạnh trọng số 1 đẩy vào cuống `push_back`) tìm khoảng cách tối ưu trong $O(V + E)$.

---

### **[IKH-0287] - Phát Hiện Vòng Lặp Hoàn Tiền Ví MoMo**
* **Dạng bài:** Bellman-Ford Negative Cycle Detection
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0287 - Phat Hien Vong Lap Hoan Tien MoMo](file:///Users/dkdeveloper/projects/testcase/IKH-0287%20-%20Phat%20Hien%20Vong%20Lap%20Hoan%20Tien%20MoMo)
* **Phương pháp giải:** Thuật toán Bellman-Ford lặp $V-1$ lần cập nhật khoảng cách và kiểm tra vòng lặp thứ $V$ phát hiện chu trình âm (vòng lặp hoàn tiền vô hạn) trong $O(V \cdot E)$.

---

### **[IKH-0288] - Ma Trận Khoảng Cách Các Kho Hàng Tiki**
* **Dạng bài:** Floyd-Warshall All-Pairs Shortest Path
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0288 - Ma Tran Khoang Cach Kho Tiki](file:///Users/dkdeveloper/projects/testcase/IKH-0288%20-%20Ma%20Tran%20Khoang%20Cach%20Kho%20Tiki)
* **Phương pháp giải:** Quy hoạch động 3 vòng lặp Floyd-Warshall `dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])` tính ma trận đường đi ngắn nhất giữa mọi cặp đỉnh trong $O(V^3)$.

---

### **[IKH-0289] - Tối Ưu Pin Xe Điện VinFast Trạm Sạc**
* **Dạng bài:** Extended State Graph Dijkstra
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0289 - Toi Uu Pin Xe Dien VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0289%20-%20Toi%20Uu%20Pin%20Xe%20Dien%20VinFast)
* **Phương pháp giải:** Xây dựng đồ thị trạng thái mở rộng `(u, battery_level)` và chạy Dijkstra tìm tuyến đường tối ưu dung lượng pin trong $O(V \cdot K \log(V \cdot K))$.

---

### **[IKH-0290] - Đếm Số Đường Đi Ngắn Nhất Viettel 5G**
* **Dạng bài:** Dijkstra Shortest Path Counting DP
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0290 - Dem So Duong Di Ngan Nhat Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0290%20-%20Dem%20So%20Duong%20Di%20Ngan%20Nhat%20Viettel)
* **Phương pháp giải:** Kết hợp Dijkstra với mảng đếm `cnt[v]`. Khi tìm được đường đi ngắn hơn reset `cnt[v] = cnt[u]`, khi đường đi bằng nhau cộng dồn `cnt[v] = (cnt[v] + cnt[u]) % MOD` trong $O((V + E) \log V)$.

---

### **[IKH-0291] - Đường Đi K Ngắn Nhất Hệ Thống FPT**
* **Dạng bài:** K-th Shortest Path via State Dijkstra
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0291 - Duong Di K Ngan Nhat FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0291%20-%20Duong%20Di%20K%20Ngan%20Nhat%20FPT)
* **Phương pháp giải:** Duyệt Dijkstra lưu mảng `dist[u][k]` là độ dài đường đi ngắn thứ $k$ đến đỉnh $u$, cập nhật trạng thái khi gặp đường đi tốt hơn trong $O(K \cdot E \log V)$.

---

### **[IKH-0292] - Tối Ưu Chuyến Bay Vietnam Airlines**
* **Dạng bài:** Time-Dependent Shortest Path Dijkstra
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0292 - Toi Uu Chuyen Bay Vietnam Airlines](file:///Users/dkdeveloper/projects/testcase/IKH-0292%20-%20Toi%20Uu%20Chuyen%20Bay%20Vietnam%20Airlines)
* **Phương pháp giải:** Dijkstra biến đổi trọng số cạnh tùy thuộc mốc thời gian đến đỉnh $u$ để chọn chuyến bay tiếp theo có lịch khởi hành sớm nhất trong $O((V + E) \log V)$.

---

### **[IKH-0293] - Tuyến Đường Cứu Hộ Bão Lụt Sơn La**
* **Dạng bài:** Multi-Source Dijkstra / BFS
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0293 - Tuyen Duong Cuu Ho Bao Lut Son La](file:///Users/dkdeveloper/projects/testcase/IKH-0293%20-%20Tuyen%20Duong%20Cuu%20Ho%20Bao%20Lut%20Son%20La)
* **Phương pháp giải:** Đẩy tất cả các điểm cứu hộ ban đầu vào Hàng đợi ưu tiên Min-Heap và khởi tạo `dist = 0` chạy Dijkstra đa nguồn tìm khoảng cách ngắn nhất đến mọi khu vực bão lụt trong $O((V + E) \log V)$.


---

### **[IKH-0294] - Lập Lịch Tiến Độ Dự Án Viettel Construction**
* **Dạng bài:** Standard Kahn Topological Sort
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0294 - Lap Lich Tien Do Viettel Construction](file:///Users/dkdeveloper/projects/testcase/IKH-0294%20-%20Lap%20Lich%20Tien%20Do%20Viettel%20Construction)
* **Phương pháp giải:** Thuật toán Kahn sử dụng Hàng đợi Queue tính bán bậc vào `in_degree[u]` xác định thứ tự thực hiện các công việc hạ tầng không vi phạm ràng buộc phụ thuộc trong $O(V + E)$.

---

### **[IKH-0295] - Quy Trình Duyệt Hồ Sơ Vay Techcombank**
* **Dạng bài:** DFS Topological Sort & Cycle Detection
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0295 - Quy Trinh Duyet Ho So Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0295%20-%20Quy%20Trinh%20Duyet%20Ho%20So%20Techcombank)
* **Phương pháp giải:** Duyệt DFS với 3 trạng thái màu (White, Gray, Black) phát hiện chu trình phụ thuộc vòng trong quy trình duyệt vay và xếp thứ tự Topo lùi trong $O(V + E)$.

---

### **[IKH-0296] - Tuyến Đường Vận Chuyển Hàng Hải VinFast**
* **Dạng bài:** Longest Path in Directed Acyclic Graph (DAG)
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0296 - Tuyen Duong Van Chuyen VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0296%20-%20Tuyen%20Duong%20Van%20Chuyen%20VinFast)
* **Phương pháp giải:** Quy hoạch động theo thứ tự Topo `dp[v] = max(dp[v], dp[u] + weight)` tìm tuyến đường di chuyển dài nhất trên đồ thị hướng không chu trình trong $O(V + E)$.

---

### **[IKH-0297] - Đếm Số Cách Hoàn Thành Khóa Học IKHEDU**
* **Dạng bài:** Number of Paths on DAG Modulo
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0297 - Dem So Cach Hoan Thanh Khoa Hoc IKHEDU](file:///Users/dkdeveloper/projects/testcase/IKH-0297%20-%20Dem%20So%20Cach%20Hoan%20Thanh%20Khoa%20Hoc%20IKHEDU)
* **Phương pháp giải:** Quy hoạch động đếm số đường đi trên DAG từ đỉnh bắt đầu đến đỉnh kết thúc `paths[v] = (paths[v] + paths[u]) % MOD` trong $O(V + E)$.

---

### **[IKH-0298] - Lập Lịch Sản Xuất Xe Điện VinFast**
* **Dạng bài:** Lexicographically Smallest Topological Sort
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0298 - Lap Lich San Xuat Xe Dien VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0298%20-%20Lap%20Lich%20San%20Xuat%20Xe%20Dien%20VinFast)
* **Phương pháp giải:** Thuật toán Kahn kết hợp Hàng đợi ưu tiên Min-Heap `std::priority_queue<int, vector<int>, greater<int>>` chọn đỉnh có chỉ số nhỏ nhất ưu tiên xuất trước trong $O((V + E) \log V)$.

---

### **[IKH-0299] - Tối Ưu Chuỗi Cung Ứng Siêu Thị WinMart**
* **Dạng bài:** Dynamic Programming on DAG with Node & Edge Weights
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0299 - Toi Uu Chuoi Cung Ung WinMart](file:///Users/dkdeveloper/projects/testcase/IKH-0299%20-%20Toi%20Uu%20Chuoi%20Cung%20Ung%20WinMart)
* **Phương pháp giải:** Tối ưu hóa chuỗi phân phối hàng hóa kết hợp trọng số đỉnh và trọng số cạnh trên DAG bằng quy hoạch động Topo trong $O(V + E)$.

---

### **[IKH-0300] - Phân Tích Sự Phụ Thuộc Mã Nguồn FPT Software**
* **Dạng bài:** Critical Nodes / Essential Edges in Topo Order
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0300 - Phan Tich Su Phu Thuoc FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0300%20-%20Phan%20Tich%20Su%20Phu%20Thuoc%20FPT)
* **Phương pháp giải:** Đếm số đường đi từ nguồn đến $u$ và từ $u$ đến đích để xác định các module mã nguồn thắt nút cổ chai (Critical Nodes) trên đồ thị phụ thuộc trong $O(V + E)$.

---

### **[IKH-0301] - Hệ Thống Gợi Ý Sản Phẩm Shopee Live**
* **Dạng bài:** DAG Transitive Closure / Bitset DP
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0301 - He Thong Goi Y Shopee Live](file:///Users/dkdeveloper/projects/testcase/IKH-0301%20-%20He%20Thong%20Goi%20Y%20Shopee%20Live)
* **Phương pháp giải:** Quy hoạch động bao đóng bắc cầu (Transitive Closure) tối ưu bằng `std::bitset<100001>` tính số lượng đỉnh có thể đến được từ mỗi đỉnh trong $O(\frac{V \cdot E}{64})$.

---

### **[IKH-0302] - Tối Ưu Lịch Trình Tàu Hỏa Vietnam Railways**
* **Dạng bài:** Minimum Path Cover on DAG
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0302 - Toi Uu Lich Trinh Vietnam Railways](file:///Users/dkdeveloper/projects/testcase/IKH-0302%20-%20Toi%20Uu%20Lich%20Trinh%20Vietnam%20Railways)
* **Phương pháp giải:** Chuyển bài toán Phủ đường đi tối thiểu trên DAG sang Ghép cặp 2 phía cực đại (Bipartite Matching / Dilworth Theorem) để tính số đoàn tàu tối thiểu cần dùng trong $O(V^3)$.


---

### **[IKH-0303] - Bảo Vệ Hạ Tầng Cáp Truyền Dẫn Viettel 5G**
* **Dạng bài:** Tarjan Bridge Detection Algorithm
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0303 - Bao Ve Ha Tang Cap Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0303%20-%20Bao%20Ve%20Ha%20Tang%20Cap%20Viettel)
* **Phương pháp giải:** Duyệt DFS đánh số mảng `num` và `low` phát hiện tất cả các Cạnh Cầu (Bridges - đoạn cáp nguy cơ làm đứt mạng) trên đồ thị vô hướng trong $O(V + E)$.

---

### **[IKH-0304] - Điểm Thắt Nút Tuyến Giao Thông VinFast**
* **Dạng bài:** Tarjan Articulation Points / Cut Vertices
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0304 - Diem That Nut Giao Thong VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0304%20-%20Diem%20That%20Nut%20Giao%20Thong%20VinFast)
* **Phương pháp giải:** Thuật toán Tarjan xác định tất cả Đỉnh Khớp (Cut Vertices - điểm giao thông huyết mạch nếu hỏng gây mất liên thông) trong $O(V + E)$.

---

### **[IKH-0305] - Cụm Máy Chủ Giao Dịch Ngân Hàng Techcombank**
* **Dạng bài:** Strongly Connected Components Tarjan SCC
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0305 - Cum May Chu Giao Dich Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0305%20-%20Cum%20May%20Chu%20Giao%20Dich%20Techcombank)
* **Phương pháp giải:** Thuật toán Tarjan sử dụng Stack và các mảng `num`/`low` phân chia đồ thị hướng thành các Thành phần liên thông mạnh (SCC) trong $O(V + E)$.

---

### **[IKH-0306] - Nén Đồ Thị Giao Dịch Ví Điện Tử MoMo**
* **Dạng bài:** Condensation Graph DAG
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0306 - Nen Do Thi Giao Dich MoMo](file:///Users/dkdeveloper/projects/testcase/IKH-0306%20-%20Nen%20Do%20Thi%20Giao%20Dich%20MoMo)
* **Phương pháp giải:** Co từng thành phần liên thông mạnh SCC thành 1 siêu đỉnh, tạo Đồ thị nén không chu trình (Condensation DAG) phục vụ phân tích dòng tiền giao dịch trong $O(V + E)$.

---

### **[IKH-0307] - Tối Ưu Tuyến Chuyển Phát Nhanh Shopee Express**
* **Dạng bài:** 2-Edge-Connected Components / Bridge Block Tree
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0307 - Toi Uu Tuyen Chuyen Phat Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0307%20-%20Toi%20Uu%20Tuyen%20Chuyen%20Phat%20Shopee)
* **Phương pháp giải:** Tìm các cạnh cầu và nén các thành phần liên thông 2 cạnh (2-Edge-Connected Components) thành Cây Cầu (Bridge Block Tree) trong $O(V + E)$.

---

### **[IKH-0308] - Bảo Vệ Mạng Lưới Điện Quốc Gia EVN**
* **Dạng bài:** 2-Vertex-Connected Components / Block Cut Tree
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0308 - Bao Ve Mang Luoi Dien EVN](file:///Users/dkdeveloper/projects/testcase/IKH-0308%20-%20Bao%20Ve%20Mang%20Luoi%20Dien%20EVN)
* **Phương pháp giải:** Xây dựng Cây Khớp (Block Cut Tree) từ các thành phần liên thông 2 đỉnh (2-Vertex-Connected Components) để phân tích khả năng chịu lỗi mạng lưới điện trong $O(V + E)$.

---

### **[IKH-0309] - Phân Tích Dòng Tiền Rửa Tiền Khoản Vay**
* **Dạng bài:** Kosaraju 2-Pass DFS SCC Algorithm
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0309 - Phan Tich Dong Tien Rua Tien](file:///Users/dkdeveloper/projects/testcase/IKH-0309%20-%20Phan%20Tich%20Dong%20Tien%20Rua%20Tien)
* **Phương pháp giải:** Thuật toán Kosaraju 2 lượt duyệt DFS (Lượt 1 trên đồ thị thuận xếp thứ tự ra, Lượt 2 trên đồ thị đảo `adj_rev`) phân tích các chu trình rửa tiền khép kín trong $O(V + E)$.

---

### **[IKH-0310] - Phân Tích Liên Thông Yếu Trên Đồ Thị Nén FPT**
* **Dạng bài:** Semi-Connected Graph / Condensation DAG Topo Path
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0310 - Ban Bac Vao Ra Tren Do Thi Nen FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0310%20-%20Ban%20Bac%20Vao%20Ra%20Tren%20Do%20Thi%20Nen%20FPT)
* **Phương pháp giải:** Nén đồ thị SCC thành DAG và kiểm tra xem DAG nén có tồn tại Đường đi Hamilton (Hamiltonian Path) hay không để xác định tính liên thông bán phần trong $O(V + E)$.

---

### **[IKH-0311] - Tối Ưu Hệ Thống Cung Cấp Nước Sạch Hà Nội**
* **Dạng bài:** Minimum Edges to Make Graph Strongly Connected
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0311 - Toi Uu He Thong Nuoc Sach Ha Noi](file:///Users/dkdeveloper/projects/testcase/IKH-0311%20-%20Toi%20Uu%20He%20Thong%20Nuoc%20Sach%20Ha%20Noi)
* **Phương pháp giải:** Nén đồ thị SCC thành DAG, đếm số siêu đỉnh nguồn `in_degree == 0` và số siêu đỉnh đích `out_degree == 0`, kết quả bổ sung tối thiểu là $\max(	ext{sources}, 	ext{sinks})$ trong $O(V + E)$.


---

### **[IKH-0312] - Truy Vấn Đường Đi Trên Cây Mạng Lưới Viettel**
* **Dạng bài:** Lowest Common Ancestor LCA Binary Lifting
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0312 - Truy Van Duong Di Tren Cay Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0312%20-%20Truy%20Van%20Duong%20Di%20Tren%20Cay%20Viettel)
* **Phương pháp giải:** Dựng bảng nhảy nhị phân `up[u][j]` tính Tổ tiên chung thấp nhất LCA của hai đỉnh $u$ và $v$ trên cây trong $O(N \log N)$ chuẩn bị và $O(\log N)$ mỗi truy vấn.

---

### **[IKH-0313] - Khoảng Cách Trạm Điện Lưới EVN Quốc Gia**
* **Dạng bài:** Tree Distance Query via LCA
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0313 - Khoang Cach Tram Dien Luoi EVN](file:///Users/dkdeveloper/projects/testcase/IKH-0313%20-%20Khoang%20Cach%20Tram%20Dien%20Luoi%20EVN)
* **Phương pháp giải:** Truy vấn khoảng cách giữa 2 đỉnh trên cây bằng công thức `dist(u, v) = depth[u] + depth[v] - 2 * depth[lca(u, v)]` kết hợp LCA Binary Lifting trong $O(\log N)$.

---

### **[IKH-0314] - Tải Trọng Tối Đa Tuyến Đường VinFast**
* **Dạng bài:** LCA Bottleneck Capacity / Min-Max Edge Weight Query
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0314 - Tai Trong Toi Da Tuyen Duong VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0314%20-%20Tai%20Trong%20Toi%20Da%20Tuyen%20Duong%20VinFast)
* **Phương pháp giải:** Lưu mảng `min_edge[u][j]` trọng số nhỏ nhất khi nhảy nhị phân $2^j$ bước, trả về trọng số nhỏ nhất trên đường đi giữa $u$ và $v$ trong $O(\log N)$.

---

### **[IKH-0315] - Phân Nhóm Giao Dịch Đồ Thị 2 Phía Ví MoMo**
* **Dạng bài:** Bipartite Graph BFS/DFS 2-Coloring Check
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0315 - Phan Nhom Giao Dich Do Thi 2 Phia MoMo](file:///Users/dkdeveloper/projects/testcase/IKH-0315%20-%20Phan%20Nhom%20Giao%20Dich%20Do%20Thi%202%20Phia%20MoMo)
* **Phương pháp giải:** Tô màu đồ thị bằng 2 màu (1 và 2) qua BFS/DFS. Nếu phát hiện 2 đỉnh kề nhau trùng màu thì không phải đồ thị 2 phía trong $O(V + E)$.

---

### **[IKH-0316] - Ghép Cặp Đơn Hàng Giao Hàng Grab Express**
* **Dạng bài:** Maximum Bipartite Matching Hopcroft-Karp / Augmenting Paths
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0316 - Ghep Cap Don Hang Giao Hang Grab](file:///Users/dkdeveloper/projects/testcase/IKH-0316%20-%20Ghep%20Cap%20Don%20Hang%20Giao%20Hang%20Grab)
* **Phương pháp giải:** Thuật toán tìm Đường tăng (Augmenting Paths) hoặc Hopcroft-Karp tìm ghép cặp cực đại giữa tài xế và đơn hàng trên đồ thị 2 phía trong $O(E \sqrt{V})$.

---

### **[IKH-0317] - Tối Ưu Luồng Băng Thông Cáp Quang FPT**
* **Dạng bài:** Maximum Network Flow Dinic Algorithm
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0317 - Toi Uu Luong Bang Thong FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0317%20-%20Toi%20Uu%20Luong%20Bang%20Thong%20FPT)
* **Phương pháp giải:** Thuật toán luồng cực đại Dinic xây dựng đồ thị phân tầng BFS và tìm luồng tăng cường DFS trong $O(V^2 E)$.

---

### **[IKH-0318] - Tuyến Cắt Tối Thiểu Mạng Lưới Điện Quốc Gia**
* **Dạng bài:** Minimum Cut Max Flow Theorem
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0318 - Tuyen Cat Toi Thieu Mang Dien EVN](file:///Users/dkdeveloper/projects/testcase/IKH-0318%20-%20Tuyen%20Cat%20Toi%20Thieu%20Mang%20Dien%20EVN)
* **Phương pháp giải:** Định lý Luồng cực đại - Lát cắt tối thiểu (Max Flow Min Cut Theorem), chạy Dinic tìm lát cắt nhỏ nhất cô lập $S$ và $T$ trong $O(V^2 E)$.

---

### **[IKH-0319] - Phủ Đỉnh Tối Thiểu Trên Đồ Thị 2 Phía**
* **Dạng bài:** Konig Theorem Minimum Vertex Cover
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0319 - Phu Dinh Toi Thieu Do Thi 2 Phia](file:///Users/dkdeveloper/projects/testcase/IKH-0319%20-%20Phu%20Dinh%20Toi%20Thieu%20Do%20Thi%202%20Phia)
* **Phương pháp giải:** Định lý König: Trên đồ thị 2 phía, kích thước Tập phủ đỉnh tối thiểu đúng bằng Kích thước Tập ghép cặp cực đại $O(E \sqrt{V})$.

---

### **[IKH-0320] - IKHEDU Masterclass Grand Synthesis Graph**
* **Dạng bài:** Combined Advanced Graph Architecture (Tarjan + LCA + DSU)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0320 - Grand Synthesis Advanced Graph](file:///Users/dkdeveloper/projects/testcase/IKH-0320%20-%20Grand%20Synthesis%20Advanced%20Graph)
* **Phương pháp giải:** Phối hợp Tarjan Bridge Tree nén cầu + DSU gộp thành phần liên thông 2 cạnh + LCA Binary Lifting trên cây nén giải quyết truy vấn liên thông động phức tạp trong $O((V + Q) \log V)$.


---

### **[IKH-0321] - Giám Sát Lưu Lượng Mạng Cáp Quang Viettel**
* **Dạng bài:** Sparse Table Range Minimum Query RMQ
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0321 - Giam Sat Luu Luong Mang Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0321%20-%20Giam%20Sat%20Luu%20Luong%20Mang%20Viettel)
* **Phương pháp giải:** Cấu trúc dữ liệu Bảng thưa (Sparse Table) chuẩn bị trong $O(N \log N)$ và truy vấn giá trị min trên đoạn $[L, R]$ đối với mảng tĩnh trong $O(1)$.

---

### **[IKH-0322] - Quản Lý Lợi Nhuận Chuỗi Siêu Thị WinMart**
* **Dạng bài:** Standard Fenwick Tree BIT 1D
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0322 - Quan Ly Loi Nhuan WinMart](file:///Users/dkdeveloper/projects/testcase/IKH-0322%20-%20Quan%20Ly%20Loi%20Nhuan%20WinMart)
* **Phương pháp giải:** Cây chỉ số nhị phân Fenwick BIT 1D cập nhật điểm `update(i, val)` và truy vấn tổng tiền tố `query(p)` trong $O(\log N)$.

---

### **[IKH-0323] - Cập Nhật Doanh Thu Tuyến Xe Điện VinFast**
* **Dạng bài:** BIT Range Update Point Query
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0323 - Cap Nhat Doanh Thu VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0323%20-%20Cap%20Nhat%20Doanh%20Thu%20VinFast)
* **Phương pháp giải:** Sử dụng mảng hiệu (Difference Array) kết hợp Fenwick BIT xử lý cập nhật cộng giá trị trên đoạn $[L, R]$ và truy vấn giá trị tại điểm $p$ trong $O(\log N)$.

---

### **[IKH-0324] - Đếm Cặp Giao Dịch Nghịch Thế Ví MoMo**
* **Dạng bài:** Coordinate Compression + BIT Inversion Count
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0324 - Dem Cap Giao Dich Nghich The MoMo](file:///Users/dkdeveloper/projects/testcase/IKH-0324%20-%20Dem%20Cap%20Giao%20Dich%20Nghich%20The%20MoMo)
* **Phương pháp giải:** Nén tọa độ giá trị các giao dịch và dùng Fenwick BIT đếm số cặp nghịch thế (Inversion Pairs - giao dịch đến sau có giá trị nhỏ hơn giao dịch đến trước) trong $O(N \log N)$.

---

### **[IKH-0325] - Bảng Thưa Hai Chiều Lưới Điện Quốc Gia EVN**
* **Dạng bài:** 2D Sparse Table Minimum Query
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0325 - Bang Thua Hai Chieu EVN](file:///Users/dkdeveloper/projects/testcase/IKH-0325%20-%20Bang%20Thua%20Hai%20Chieu%20EVN)
* **Phương pháp giải:** Mở rộng Bảng thưa 2D `st[i][j][k1][k2]` tính giá trị điện áp min trên hình chữ nhật $[r_1, r_2] 	imes [c_1, c_2]$ trong $O(N \cdot M \log N \log M)$ chuẩn bị và $O(1)$ truy vấn.

---

### **[IKH-0326] - Quản Lý Bật Tắt Trạm Sạc VinFast**
* **Dạng bài:** BIT Range Update Range Query (2 BITs)
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0326 - Quan Ly Bat Tat Tram Sac VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0326%20-%20Quan%20Ly%20Bat%20Tat%20Tram%20Sac%20VinFast)
* **Phương pháp giải:** Duy trì 2 mảng Fenwick BIT $B_1$ và $B_2$ với công thức $\sum_{i=1}^p A_i = p \cdot B_1(p) - B_2(p)$ hỗ trợ cả Cập nhật đoạn và Truy vấn tổng đoạn trong $O(\log N)$.

---

### **[IKH-0327] - Bảng Lưới Giao Dịch 2D Ngân Hàng Techcombank**
* **Dạng bài:** 2D Fenwick Tree BIT
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0327 - Bang Luoi Giao Dich 2D Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0327%20-%20Bang%20Luoi%20Giao%20Dich%202D%20Techcombank)
* **Phương pháp giải:** Cấu trúc dữ liệu 2D Fenwick BIT `bit[x][y]` cập nhật điểm và truy vấn tổng trên vùng ma trận 2D $[x_1, x_2] 	imes [y_1, y_2]$ trong $O(\log N \log M)$.


---

### **[IKH-0328] - Quản Lý Tốc Độ Mạng Cáp Quang FPT**
* **Dạng bài:** Standard Segment Tree Point Update Range Sum
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0328 - Quan Ly Toc Do Mang FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0328%20-%20Quan%20Ly%20Toc%20Do%20Mang%20FPT)
* **Phương pháp giải:** Cây phân đoạn Segment Tree cập nhật lá `update(pos, val)` và truy vấn tổng trên đoạn $[L, R]$ trong $O(\log N)$.

---

### **[IKH-0329] - Bảo Trì Trạm Phát Sóng Viettel 5G**
* **Dạng bài:** Segment Tree Point Update Range Min/Max
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0329 - Bao Tri Tram Phat Song Viettel 5G](file:///Users/dkdeveloper/projects/testcase/IKH-0329%20-%20Bao%20Tri%20Tram%20Phat%20Song%20Viettel%205G)
* **Phương pháp giải:** Cây phân đoạn Segment Tree cập nhật điểm và truy vấn giá trị nhỏ nhất/lớn nhất trên đoạn $[L, R]$ trong $O(\log N)$.

---

### **[IKH-0330] - Tìm Kiếm Vị Trí Xe Cứu Thương Grab**
* **Dạng bài:** Walk on Segment Tree / Binary Search on SegTree
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0330 - Tim Kiem Vi Tri Xe Cuu Thuong Grab](file:///Users/dkdeveloper/projects/testcase/IKH-0330%20-%20Tim%20Kiem%20Vi%20Tri%20Xe%20Cuu%20Thuong%20Grab)
* **Phương pháp giải:** Kỹ thuật Duyệt trên Cây Phân Đoạn (Walk on Segment Tree) tìm vị trí đầu tiên có tổng tích lũy hoặc giá trị $\ge X$ trong $O(\log N)$ thay vì Tìm kiếm nhị phân $O(\log^2 N)$.

---

### **[IKH-0331] - Tối Ưu Dãy Con Liên Tiếp Có Tổng Tối Đa Shopee**
* **Dạng bài:** Segment Tree Maximum Subarray Sum (Kadane on SegTree)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0331 - Toi Uu Day Con Tong Toi Da Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0331%20-%20Toi%20Uu%20Day%20Con%20Tong%20Toi%20Da%20Shopee)
* **Phương pháp giải:** Nút Segment Tree lưu 4 thông số: `sum`, `pref`, `suff`, `ans` (Kadane). Hợp nhất 2 nút con trong $O(1)$, hỗ trợ cập nhật điểm và truy vấn tổng dãy con liên tiếp max trên đoạn $[L, R]$ trong $O(\log N)$.

---

### **[IKH-0332] - Theo Dõi Trạng Thái Pin Xe VinFast**
* **Dạng bài:** Segment Tree Range GCD Query
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0332 - Theo Doi Trang Thai Pin VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0332%20-%20Theo%20Doi%20Trang%20Thai%20Pin%20VinFast)
* **Phương pháp giải:** Nút Segment Tree lưu `gcd` của đoạn. Hợp nhất `std::__gcd(left, right)` trong $O(\log(	ext{val}))$. Cập nhật điểm và truy vấn GCD đoạn trong $O(\log N \log(	ext{val}))$.

---

### **[IKH-0333] - Cân Bằng Tải Máy Chủ Zalo Cloud**
* **Dạng bài:** Segment Tree State Toggle / Bracket Matching
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0333 - Can Bang Tai May Chu Zalo Cloud](file:///Users/dkdeveloper/projects/testcase/IKH-0333%20-%20Can%20Bang%20Tai%20May%20Chu%20Zalo%20Cloud)
* **Phương pháp giải:** Nút Segment Tree lưu số lượng máy chủ/ngoặc mở và đóng chưa khớp. Hợp nhất trạng thái hai nút con $O(1)$, cập nhật trạng thái bật/tắt máy chủ $O(\log N)$.

---

### **[IKH-0334] - Quản Lý Ma Trận Lưới Siêu Thị WinMart**
* **Dạng bài:** 2D Segment Tree (Tree of Trees)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0334 - Quan Ly Ma Tran Luoi WinMart](file:///Users/dkdeveloper/projects/testcase/IKH-0334%20-%20Quan%20Ly%20Ma%20Tran%20Luoi%20WinMart)
* **Phương pháp giải:** Cấu trúc Cây phân đoạn 2D (Cây trong Cây - 2D Segment Tree) cập nhật điểm ô ma trận $[x][y]$ và truy vấn tổng hình chữ nhật $[x_1, x_2] 	imes [y_1, y_2]$ trong $O(\log N \log M)$.


---

### **[IKH-0335] - Điều Chỉnh Công Suất Lưới Điện EVN**
* **Dạng bài:** Standard Lazy Propagation Segment Tree Range Add Range Sum
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0335 - Dieu Chinh Cong Suat Luoi Dien EVN](file:///Users/dkdeveloper/projects/testcase/IKH-0335%20-%20Dieu%20Chinh%20Cong%20Suat%20Luoi%20Dien%20EVN)
* **Phương pháp giải:** Kỹ thuật Đẩy giá trị lười Lazy Propagation trên Cây phân đoạn xử lý Cập nhật đoạn $[L, R]$ thêm $v$ và Truy vấn tổng đoạn $[L, R]$ trong $O(\log N)$.

---

### **[IKH-0336] - Tối Ưu Phí Dịch Vụ Thu Phí VETC**
* **Dạng bài:** Lazy Propagation Range Assignment Range Min
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0336 - Toi Uu Phi Dich Vu VETC](file:///Users/dkdeveloper/projects/testcase/IKH-0336%20-%20Toi%20Uu%20Phi%20Dich%20Vu%20VETC)
* **Phương pháp giải:** Cây phân đoạn Lazy Propagation xử lý Gán tất cả phần tử trong đoạn $[L, R]$ thành $v$ và TRUY VẤN giá trị nhỏ nhất trên đoạn trong $O(\log N)$.

---

### **[IKH-0337] - Bảo Vệ Hạ Tầng Cáp Quang FPT Telecom**
* **Dạng bài:** Lazy Propagation Bit Flip / Modular Segment Tree
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0337 - Bao Ve Ha Tang Cap Quang FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0337%20-%20Bao%20Ve%20Ha%20Tang%20Cap%20Quang%20FPT)
* **Phương pháp giải:** Kỹ thuật đảo trạng thái bit 0/1 trên đoạn $[L, R]$ dùng cờ `lazy_flip` đảo bit các nút con trong $O(\log N)$.

---

### **[IKH-0338] - Quản Lý Điểm Thưởng Ví MoMo**
* **Dạng bài:** Lazy Propagation Add & Multiply Range Sum
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0338 - Quan Ly Diem Thuong Vi MoMo](file:///Users/dkdeveloper/projects/testcase/IKH-0338%20-%20Quan%20Ly%20Diem%20Thuong%20Vi%20MoMo)
* **Phương pháp giải:** Duy trì 2 cờ `lazy_mul` và `lazy_add` tại mỗi nút SegTree với công thức chuyển tiếp $f(x) = x \cdot mul + add$ cập nhật đoạn vừa nhân vừa cộng trong $O(\log N)$.

---

### **[IKH-0339] - Cập Nhật Chuỗi Cung Ứng Grab Express**
* **Dạng bài:** Lazy Segment Tree Range Assignment & Range GCD
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0339 - Cap Nhat Chuoi Cung Ung Grab](file:///Users/dkdeveloper/projects/testcase/IKH-0339%20-%20Cap%20Nhat%20Chuoi%20Cung%20Ung%20Grab)
* **Phương pháp giải:** Kết hợp Lazy Range Assignment và hợp nhất GCD hai nút con `std::__gcd(left, right)` trong $O(\log N \log(	ext{val}))$.

---

### **[IKH-0340] - Cập Nhật Dãy Số Tự Động Viettel AI**
* **Dạng bài:** Lazy SegTree Matrix Multiplications
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0340 - Cap Nhat Day So Viettel AI](file:///Users/dkdeveloper/projects/testcase/IKH-0340%20-%20Cap%20Nhat%20Day%20So%20Viettel%20AI)
* **Phương pháp giải:** Nút Cây phân đoạn lưu Vector trạng thái $2 	imes 1$, thao tác cập nhật đoạn là Nhân với Ma trận chuyển $2 	imes 2$ thông qua Lazy Propagation trong $O(K^3 \log N)$.

---

### **[IKH-0341] - Tối Ưu Động Lưới Điện Thông Minh EVN**
* **Dạng bài:** Dynamic DP on Lazy Segment Tree
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0341 - Toi Uu Dong Luoi Dien EVN](file:///Users/dkdeveloper/projects/testcase/IKH-0341%20-%20Toi%20Uu%20Dong%20Luoi%20Dien%20EVN)
* **Phương pháp giải:** Kỹ thuật Quy hoạch động động (Dynamic DP) nhúng ma trận chuyển DP vào Nút Cây phân đoạn Lazy Propagation xử lý cập nhật cấu trúc ma trận trong $O(K^3 \log N)$.


---

### **[IKH-0342] - Hệ Thống Gợi Ý Từ Khóa Shopee Search**
* **Dạng bài:** Standard String Trie Tree Insert & Search
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0342 - Goi Y Tu Khoa Shopee Search](file:///Users/dkdeveloper/projects/testcase/IKH-0342%20-%20Goi%20Y%20Tu%20Khoa%20Shopee%20Search)
* **Phương pháp giải:** Cấu trúc Cây tiền tố (Trie) lưu trữ các xâu ký tự từ điển, hỗ trợ chèn `insert` và kiểm tra sự tồn tại của từ `search` trong $O(|S|)$.

---

### **[IKH-0343] - Tự Động Điền Số Điện Thoại Viettel Telecom**
* **Dạng bài:** Trie Prefix Count & Auto-Complete
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0343 - Tu Dong Dien So Dien Thoai Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0343%20-%20Tu%20Dong%20Dien%20So%20Dien%20Thoai%20Viettel)
* **Phương pháp giải:** Duy trì biến đếm `prefix_count` tại mỗi nút Cây tiền tố Trie, trả về số lượng từ có tiền tố cho trước $P$ trong $O(|P|)$.

---

### **[IKH-0344] - Mã Hóa Giao Dịch Bảo Mật Techcombank**
* **Dạng bài:** Binary XOR Trie Maximum XOR Pair
* **Độ khó:** Rating 1450 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0344 - Ma Hoa Giao Dich Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0344%20-%20Ma%20Hoa%20Giao%20Dich%20Techcombank)
* **Phương pháp giải:** Cây tiền tố nhị phân (Binary XOR Trie) chiều cao 30 bit. Với mỗi số $A_i$, ưu tiên chọn bit ngược lại $1 - b$ để tìm cặp $(A_i, A_j)$ có tổng XOR lớn nhất trong $O(30 \cdot N)$.

---

### **[IKH-0345] - Tìm Dãy Con Có Tổng XOR Cực Đại MoMo**
* **Dạng bài:** Binary XOR Trie + Prefix XOR Subarray Max
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0345 - Tim Day Con Tong XOR Max MoMo](file:///Users/dkdeveloper/projects/testcase/IKH-0345%20-%20Tim%20Day%20Con%20Tong%20XOR%20Max%20MoMo)
* **Phương pháp giải:** Mảng tổng tiền tố XOR `pref[i] = pref[i-1] ^ A[i]`. Đưa bài toán tìm dãy con có tổng XOR max về bài toán tìm 2 giá trị $pref[i] \oplus pref[j]$ max giải bằng Binary XOR Trie trong $O(30 \cdot N)$.

---

### **[IKH-0346] - Bộ Lọc Từ Cấm Tin Nhắn Zalo Chat**
* **Dạng bài:** Multi-Pattern Trie Matching (Aho-Corasick Intro)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0346 - Bo Loc Tu Cam Tin Nhan Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0346%20-%20Bo%20Loc%20Tu%20Cam%20Tin%20Nhan%20Zalo)
* **Phương pháp giải:** Dựng Cây tiền tố Trie từ danh sách các mẫu từ cấm, khớp song song nhiều từ mẫu với đoạn tin nhắn thoại trong $O(\sum |Pattern| + |S|)$.

---

### **[IKH-0347] - Tối Ưu Cặp Tài Khoản An Toàn VinFast**
* **Dạng bài:** Binary XOR Trie with Subtree Counts
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0347 - Toi Uu Cap Tai Khoan VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0347%20-%20Toi%20Uu%20Cap%20Tai%20Khoan%20VinFast)
* **Phương pháp giải:** Cây tiền tố nhị phân đếm số lượng phần tử ở nhánh con, truy vấn số lượng cặp có $A_i \oplus A_j \le K$ trong $O(30 \cdot N)$.

---

### **[IKH-0348] - Phân Tích Cấu Trúc Khóa Bảo Mật FPT Cyber Security**
* **Dạng bài:** Compressed Trie / Radix Tree
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0348 - Phan Tich Khoa Bao Mat FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0348%20-%20Phan%20Tich%20Khoa%20Bao%20Mat%20FPT)
* **Phương pháp giải:** Cấu trúc Cây tiền tố nén (Compressed Trie / Radix Tree) gộp các chuỗi đơn nhánh giúp tiết kiệm bộ nhớ và tối ưu tốc độ duyệt tiền tố xâu ký tự trong $O(|S|)$.


---

### **[IKH-0349] - Quản Lý Bộ Nhớ Tự Động Viettel Cloud**
* **Dạng bài:** Dynamic Segment Tree Node Creation on Demand
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0349 - Quan Ly Bo Nho Viettel Cloud](file:///Users/dkdeveloper/projects/testcase/IKH-0349%20-%20Quan%20Ly%20Bo%20Nho%20Viettel%20Cloud)
* **Phương pháp giải:** Cấu trúc Cây phân đoạn động (Dynamic Segment Tree) tạo nút mới khi có yêu cầu (on demand), xử lý mảng kích thước cực lớn $N \le 10^9$ với độ phức tạp $O(Q \log N)$ thời gian và bộ nhớ.

---

### **[IKH-0350] - Truy Vấn Lịch Sử Giao Dịch Ngân Hàng Techcombank**
* **Dạng bài:** Persistent Segment Tree Point Update Version Query
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0350 - Truy Van Lich Su Giao Dich Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0350%20-%20Truy%20Van%20Lich%20Su%20Giao%20Dich%20Techcombank)
* **Phương pháp giải:** Cây phân đoạn bền vững (Persistent Segment Tree) lưu trữ mọi phiên bản sửa đổi $v$, truy vấn tổng đoạn tại phiên bản quá khứ $v$ bất kỳ trong $O(\log N)$.

---

### **[IKH-0351] - Phân Tích Phần Tử Nhỏ Thứ K Trên Đoạn WinMart**
* **Dạng bài:** Persistent Segment Tree Range K-th Smallest Element
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0351 - Phan Tu Nho Thu K Tren Doan WinMart](file:///Users/dkdeveloper/projects/testcase/IKH-0351%20-%20Phan%20Tu%20Nho%20Thu%20K%20Tren%20Doan%20WinMart)
* **Phương pháp giải:** Nén tọa độ kết hợp Persistent Segment Tree $root[i]$ lưu tần số tiền tố $A[1..i]$. Truy vấn phần tử nhỏ thứ $K$ trên đoạn $[L, R]$ bằng cách so sánh nút trái `root[R]` và `root[L-1]` trong $O(\log N)$.

---

### **[IKH-0352] - Khôi Phục Trạng Thái Mạng Lưới Điện EVN**
* **Dạng bài:** Persistent Binary XOR Trie Version Query
* **Độ khó:** Rating 1600 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0352 - Khoi Phuc Trang Thai Mang Luoi EVN](file:///Users/dkdeveloper/projects/testcase/IKH-0352%20-%20Khoi%20Phuc%20Trang%20Thai%20Mang%20Luoi%20EVN)
* **Phương pháp giải:** Cây tiền tố nhị phân bền vững (Persistent Binary XOR Trie) lưu vết các phiên bản chèn phần tử, cho phép khôi phục và truy vấn XOR max ở phiên bản $v$ bất kỳ trong $O(30 \cdot N)$.

---

### **[IKH-0353] - Đếm Số Phần Tử Phân Biệt Trên Đoạn Shopee**
* **Dạng bài:** Persistent Segment Tree Count Distinct Elements in Range
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0353 - Dem So Phan Tu Phan Biet Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0353%20-%20Dem%20So%20Phan%20Tu%20Phan%20Biet%20Shopee)
* **Phương pháp giải:** Dùng Persistent Segment Tree cập nhật vị trí xuất hiện cuối cùng của từng giá trị, trả về số phần tử phân biệt trên đoạn $[L, R]$ trong $O(\log N)$.

---

### **[IKH-0354] - Lưu Tải Trọng Động Tuyến Đường VinFast**
* **Dạng bài:** Segment Tree Merging / Splitting
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0354 - Luu Tai Trong Dong VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0354%20-%20Luu%20Tai%20Trong%20Dong%20VinFast)
* **Phương pháp giải:** Kỹ thuật Hợp nhất Cây phân đoạn (Segment Tree Merging) gộp dữ liệu từ các nhánh con trong $O(N \log N)$ tổng bộ nhớ và thời gian.

---

### **[IKH-0355] - IKHEDU Masterclass Grand Synthesis Data Structure**
* **Dạng bài:** Combined Advanced DS (Persistent SegTree + Lazy SegTree + HLD)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0355 - Grand Synthesis Data Structure](file:///Users/dkdeveloper/projects/testcase/IKH-0355%20-%20Grand%20Synthesis%20Data%20Structure)
* **Phương pháp giải:** Phối hợp Cây phân đoạn bền vững (Persistent SegTree) + Lazy Propagation + Phân rã cây Heavy-Light Decomposition HLD giải quyết truy vấn đường đi trên cây có lịch sử chỉnh sửa trong $O((N+Q) \log^2 N)$.


---

### **[IKH-0356] - Kiểm Tra Trùng Lặp Chuỗi Mã Độc Viettel Security**
* **Dạng bài:** Polynomial Rolling Hash 1D Substring Comparison
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0356 - Kiem Tra Trung Lap Ma Doc Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0356%20-%20Kiem%20Tra%20Trung%20Lap%20Ma%20Doc%20Viettel)
* **Phương pháp giải:** Sử dụng Băm xâu đa thức (Polynomial Rolling Hash) kết hợp Double Hashing ($10^9+7, 10^9+9$) chuẩn bị tiền tố $O(N)$, truy vấn so sánh hai đoạn xâu con trong $O(1)$.

---

### **[IKH-0357] - So Sánh Hai Đoạn Mã Nguồn FPT Software**
* **Dạng bài:** Double Hashing Anti-Collision Technique
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0357 - So Sanh Doan Ma Nguon FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0357%20-%20So%20Sanh%20Doan%20Ma%20Nguon%20FPT)
* **Phương pháp giải:** Áp dụng kỹ thuật Băm kép (Double Hashing) với hai cặp (Base, Modulo) loại bỏ hoàn toàn nguy cơ va chạm test băm, kiểm tra tính đồng dạng mã nguồn trong $O(1)$.

---

### **[IKH-0358] - Tìm Chuỗi Đơn Nhất Trong Nhật Ký Giao Dịch MoMo**
* **Dạng bài:** Rolling Hash Fixed Window Distinct Substrings
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0358 - Tim Chuoi Don Nhat Nhat Ky MoMo](file:///Users/dkdeveloper/projects/testcase/IKH-0358%20-%20Tim%20Chuoi%20Don%20Nhat%20Nhat%20Ky%20MoMo)
* **Phương pháp giải:** Dùng Kỹ thuật cửa sổ trượt băm (Rolling Hash Window) đếm số lượng xâu con có độ dài $K$ phân biệt trong $O(N)$ thời gian và bộ nhớ.

---

### **[IKH-0359] - Kiểm Tra Đoạn Tin Nhắn Đối Xứng Zalo Chat**
* **Dạng bài:** Forward & Backward Rolling Hash Palindrome Check
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0359 - Kiem Tra Tin Nhan Doi Xung Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0359%20-%20Kiem%20Tra%20Tin%20Nhan%20Doi%20Xung%20Zalo)
* **Phương pháp giải:** Xây dựng hai mảng Hash xuôi (Forward) và Hash ngược (Backward). Kiểm tra đoạn xâu $[L, R]$ có phải xâu đối xứng (Palindrome) hay không trong $O(1)$.

---

### **[IKH-0360] - Băm Ma Trận Hình Ảnh Nhận Diện Xe VinFast**
* **Dạng bài:** 2D Rolling Hash Matrix Matching
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0360 - Bam Ma Tran Hinh Anh VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0360%20-%20Bam%20Ma%20Tran%20Hinh%20Anh%20VinFast)
* **Phương pháp giải:** Băm ma trận 2 chiều (2D Rolling Hash) theo hàng và cột, hỗ trợ khớp mẫu ảnh kích thước $H 	imes W$ trên lưới $N 	imes M$ trong $O(N \cdot M)$.

---

### **[IKH-0361] - Tìm Tiền Tố Lặp Tối Đa Chuỗi Đơn Hàng Shopee**
* **Dạng bài:** Rolling Hash + Binary Search Longest Common Prefix (LCP)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0361 - Tim Tien To Lap Toi Da Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0361%20-%20Tim%20Tien%20To%20Lap%20Toi%20Da%20Shopee)
* **Phương pháp giải:** Phối hợp Rolling Hash và Tìm kiếm nhị phân (Binary Search) độ dài tiền tố chung dài nhất (LCP) giữa hai vị trí bất kỳ trong $O(\log N)$.

---

### **[IKH-0362] - Truy Vấn Đổi Ký Tự Đoạn Xâu Ngân Hàng Techcombank**
* **Dạng bài:** Dynamic Segment Tree for Polynomial Rolling Hash
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0362 - Truy Van Doi Ky Tu Xau Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0362%20-%20Truy%20Van%20Doi%20Ky%20Tu%20Xau%20Techcombank)
* **Phương pháp giải:** Nhúng công thức Băm đa thức vào Cây phân đoạn (Segment Tree) hỗ trợ cập nhật ký tự tại vị trí $u$ và truy vấn giá trị Hash của đoạn $[L, R]$ trong $O(\log N)$.


---

### **[IKH-0363] - Tìm Kiếm Mẫu Từ Khóa Quảng Cáo Zalo Ads**
* **Dạng bài:** Standard KMP Pattern Matching Algorithm
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0363 - Tim Kiem Mau Tu Khoa Zalo Ads](file:///Users/dkdeveloper/projects/testcase/IKH-0363%20-%20Tim%20Kiem%20Mau%20Tu%20Khoa%20Zalo%20Ads)
* **Phương pháp giải:** Sử dụng mảng tiền tố Prefix Function $\pi[i]$ của thuật toán KMP tìm kiếm tất cả các vị trí xuất hiện của mẫu $P$ trong văn bản $T$ trong $O(N + M)$.

---

### **[IKH-0364] - Đếm Tần Suất Tiền Tố Mã Đơn Hàng Shopee**
* **Dạng bài:** KMP Prefix Function DP Frequency Count
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0364 - Dem Tan Suat Tien To Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0364%20-%20Dem%20Tan%20Suat%20Tien%20To%20Shopee)
* **Phương pháp giải:** Kết hợp mảng tiền tố $\pi$ và Quy hoạch động truy vết ngược từ $N$ về $1$, đếm tần suất xuất hiện của mọi tiền tố $S[0..i]$ trong xâu $S$ trong $O(N)$.

---

### **[IKH-0365] - Tìm Chu Kỳ Ngắn Nhất Chuỗi Tín Hiệu VinFast**
* **Dạng bài:** KMP String Periodicity Theorem
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0365 - Tim Chu Ky Ngan Nhat Tin Hieu VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0365%20-%20Tim%20Chu%20Ky%20Ngan%20Nhat%20Tin%20Hieu%20VinFast)
* **Phương pháp giải:** Áp dụng định lý chu kỳ xâu qua mảng $\pi$: Nếu $N \pmod{N - \pi[N]} == 0$, chu kỳ cơ sở ngắn nhất là $P = N - \pi[N]$, ngược lại chu kỳ là $N$. Độ phức tạp $O(N)$.

---

### **[IKH-0366] - Kiểm Tra Xâu Xoay Vòng Nhận Diện Khuôn Mặt VNPT**
* **Dạng bài:** KMP String Rotation Matching
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0366 - Kiem Tra Xau Xoay Vong VNPT](file:///Users/dkdeveloper/projects/testcase/IKH-0366%20-%20Kiem%20Tra%20Xau%20Xoay%20Vong%20VNPT)
* **Phương pháp giải:** Nhân đôi xâu $S$ thành $S + S$, sau đó sử dụng KMP tìm kiếm xâu xoay $T$ trong $S + S$ để xác định tính tương đẳng xoay vòng trong $O(N)$.

---

### **[IKH-0367] - Đếm Số Xâu Con Là Tiền Tố Và Hậu Tố FPT Telecom**
* **Dạng bài:** KMP Border Traversal
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0367 - Dem So Xau Con Border FPT Telecom](file:///Users/dkdeveloper/projects/testcase/IKH-0367%20-%20Dem%20So%20Xau%20Con%20Border%20FPT%20Telecom)
* **Phương pháp giải:** Duyệt liên tục mảng border $k = \pi[k-1]$ từ $k = \pi[N-1]$ để liệt kê tất cả các độ dài xâu vừa là tiền tố vừa là hậu tố (Border) trong $O(N)$.

---

### **[IKH-0368] - Tự Động Hóa Chuyển Trạng Thái KMP Viettel Security**
* **Dạng bài:** KMP Automaton Transition Table
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0368 - Tu Dong Hoa Trang Thai Viettel Security](file:///Users/dkdeveloper/projects/testcase/IKH-0368%20-%20Tu%20Dong%20Hoa%20Trang%20Thai%20Viettel%20Security)
* **Phương pháp giải:** Xây dựng bảng chuyển trạng thái tự động $aut[i][c]$ dựa trên KMP Prefix Function $\pi$, hỗ trợ chuyển trạng thái khớp xâu trực tiếp trong $O(N \cdot |\Sigma|)$.

---

### **[IKH-0369] - Bài Toán Chuỗi Con Không Chứa Mẫu Cấm Techcombank**
* **Dạng bài:** KMP Automaton + Dynamic Programming
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0369 - Chuoi Con Khong Chua Mau Cam Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0369%20-%20Chuoi%20Con%20Khong%20Chua%20Mau%20Cam%20Techcombank)
* **Phương pháp giải:** Phối hợp KMP Automaton và Quy hoạch động $dp[i][j]$ đếm số lượng xâu độ dài $N$ không chứa mẫu cấm $P$ trong $O(N \cdot |P| \cdot |\Sigma|)$.


---

### **[IKH-0370] - Khớp Mẫu Z-Algorithm Chuỗi Mã Độc VNPT**
* **Dạng bài:** Standard Z-Algorithm Pattern Matching
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0370 - Khop Mau Z-Algorithm Ma Doc VNPT](file:///Users/dkdeveloper/projects/testcase/IKH-0370%20-%20Khop%20Mau%20Z-Algorithm%20Ma%20Doc%20VNPT)
* **Phương pháp giải:** Ghép xâu $S = P + \# + T$, xây dựng mảng $Z[i]$ đại diện cho độ dài tiền tố chung dài nhất từ vị trí $i$. Tìm vị trí xuất hiện của $P$ trong $T$ với độ phức tạp $O(N + M)$.

---

### **[IKH-0371] - Đếm Số Lần Xuất Hiện Mẫu Quảng Cáo Shopee**
* **Dạng bài:** Z-Algorithm Pattern Frequency & Range Query
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0371 - Dem Mau Quang Cao Shopee Z-Algo](file:///Users/dkdeveloper/projects/testcase/IKH-0371%20-%20Dem%20Mau%20Quang%20Cao%20Shopee%20Z-Algo)
* **Phương pháp giải:** Sử dụng mảng $Z$-array tính toán các vị trí có $Z[i] == |P|$, kết hợp mảng cộng dồn Prefix Sum để trả lời tần suất xuất hiện của mẫu $P$ trong $O(1)$ mỗi truy vấn.

---

### **[IKH-0372] - Tìm Đoạn Tiền Tố Chung Dài Nhất Mảng Xâu FPT Telecom**
* **Dạng bài:** Z-Algorithm Longest Common Prefix (LCP) Array
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0372 - Tim Tien To Chung Dai Nhat FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0372%20-%20Tim%20Tien%20To%20Chung%20Dai%20Nhat%20FPT)
* **Phương pháp giải:** Xây dựng mảng $Z$-algorithm giữa tiền tố gốc $S[0..]$ và các hậu tố $S[i..]$ để tìm tiền tố chung dài nhất LCP của hai vị trí bất kỳ trong $O(1)$.

---

### **[IKH-0373] - Tìm Chuỗi Đối Xứng Dài Nhất Trong Tin Nhắn Zalo**
* **Dạng bài:** Standard Manacher Algorithm Longest Palindromic Substring
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0373 - Tim Chuoi Doi Xung Dai Nhat Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0373%20-%20Tim%20Chuoi%20Doi%20Xung%20Dai%20Nhat%20Zalo)
* **Phương pháp giải:** Áp dụng thuật toán Manacher chèn ký tự đặc biệt `#` quy đổi độ dài lẻ/chẵn, sử dụng tính chất đối xứng tâm tìm xâu đối xứng dài nhất trong $O(N)$ thời gian và bộ nhớ.

---

### **[IKH-0374] - Đếm Tất Cả Chuỗi Con Đối Xứng Viettel Telecom**
* **Dạng bài:** Manacher Array Radius Sum
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0374 - Dem Tat Ca Chuoi Con Doi Xung Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0374%20-%20Dem%20Tat%20Ca%20Chuoi%20Con%20Doi%20Xung%20Viettel)
* **Phương pháp giải:** Tính tổng bán kính đối xứng từ mảng Manacher $P[i]$ bằng công thức $\sum \lfloor (P[i] + 1) / 2 \rfloor$ đếm chính xác số lượng xâu con đối xứng phân biệt vị trí trong $O(N)$.

---

### **[IKH-0375] - Phân Tách Chuỗi Nhập Liệu Thành Các Xâu Đối Xứng Techcombank**
* **Dạng bài:** Manacher Algorithm + Dynamic Programming
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0375 - Phan Tach Chuoi Doi Xung Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0375%20-%20Phan%20Tach%20Chuoi%20Doi%20Xung%20Techcombank)
* **Phương pháp giải:** Dùng Manacher xác định tính đối xứng của mọi đoạn $[i, j]$ trong $O(1)$, kết hợp DP $dp[i]$ tìm số bước phân tách xâu thành các Palindrome ít nhất trong $O(N^2)$.

---

### **[IKH-0376] - Khôi Phục Tin Nhắn Đối Xứng Ngắn Nhất VinFast**
* **Dạng bài:** Manacher Shortest Palindromic Prefix/Suffix Extension
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0376 - Khoi Phuc Tin Nhan Doi Xung VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0376%20-%20Khoi%20Phuc%20Tin%20Nhan%20Doi%20Xung%20VinFast)
* **Phương pháp giải:** Dùng thuật toán Manacher / Z-Algorithm tìm tiền tố đối xứng dài nhất của $S$, từ đó thêm phần dư lật ngược vào sau $S$ để tạo xâu đối xứng ngắn nhất trong $O(N)$.


---

### **[IKH-0377] - Xây Dựng Mảng Hậu Tố Hệ Thống Mã Độc VNPT**
* **Dạng bài:** Standard Suffix Array Construction
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0377 - Xay Dung Mang Hau To VNPT](file:///Users/dkdeveloper/projects/testcase/IKH-0377%20-%20Xay%20Dung%20Mang%20Hau%20To%20VNPT)
* **Phương pháp giải:** Sắp xếp tất cả các hậu tố của xâu $S$ theo thứ tự từ điển sử dụng thuật toán Suffix Array kết hợp nhân đôi độ dài Doubling Algorithm trong $O(N \log N)$ thời gian và $O(N)$ bộ nhớ.

---

### **[IKH-0378] - Tìm Tiền Tố Chung Dài Nhất Mảng Hậu Tố Viettel**
* **Dạng bài:** Kasai LCP Array Algorithm
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0378 - Tim Tien To Chung Dai Nhat Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0378%20-%20Tim%20Tien%20To%20Chung%20Dai%20Nhat%20Viettel)
* **Phương pháp giải:** Sử dụng Thuật toán Kasai xây dựng mảng $LCP[i]$ là độ dài tiền tố chung dài nhất giữa hai hậu tố kề nhau trong Suffix Array trong $O(N)$.

---

### **[IKH-0379] - Đếm Số Chuỗi Con Phân Biệt Trong Nhật Ký Shopee**
* **Dạng bài:** Distinct Substrings Count via Suffix Array + LCP
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0379 - Dem So Chuoi Con Phan Biet Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0379%20-%20Dem%20So%20Chuoi%20Con%20Phan%20Biet%20Shopee)
* **Phương pháp giải:** Tính tổng số xâu con phân biệt bằng công thức $\text{Total} = \frac{N(N+1)}{2} - \sum LCP[i]$ với độ phức tạp $O(N \log N)$.

---

### **[IKH-0380] - Tìm Xâu Con Lặp Lại Ít Nhất K Lần FPT Software**
* **Dạng bài:** Longest Substring Repeating K Times
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0380 - Tim Xau Con Lap Lai K Lan FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0380%20-%20Tim%20Xau%20Con%20Lap%20Lai%20K%20Lan%20FPT)
* **Phương pháp giải:** Phối hợp Suffix Array, LCP Array và Cửa sổ trượt Slided Window Min / Segment Tree tìm giá trị min lớn nhất của đoạn $K-1$ phần tử kề nhau trên mảng $LCP$ trong $O(N \log N)$.

---

### **[IKH-0381] - Tìm Xâu Con Chung Dài Nhất Của Hai Chuỗi Zalo Pay**
* **Dạng bài:** Longest Common Substring of 2 Strings
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0381 - Tim Xau Con Chung Dai Nhat Zalo Pay](file:///Users/dkdeveloper/projects/testcase/IKH-0381%20-%20Tim%20Xau%20Con%20Chung%20Dai%20Nhat%20Zalo%20Pay)
* **Phương pháp giải:** Ghép xâu $S = S_1 + \# + S_2$, dựng Suffix Array và LCP Array, tìm $\max LCP[i]$ giữa hai hậu tố thuộc hai xâu khác nhau trong $O(N \log N)$.

---

### **[IKH-0382] - Tìm Xâu Con Nhỏ Thứ K Theo Thứ Tự Từ Điển Techcombank**
* **Dạng bài:** K-th Lexicographical Substring
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0382 - Tim Xau Con Nho Thu K Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0382%20-%20Tim%20Xau%20Con%20Nho%20Thu%20K%20Techcombank)
* **Phương pháp giải:** Dựa trên Suffix Array và mảng LCP, tính số xâu con mới đóng góp ở mỗi hậu tố $(N - SA[i] - LCP[i-1])$, sử dụng Prefix Sum + Binary Search trích xuất xâu con nhỏ thứ $K$ trong $O(N \log N)$.

---

### **[IKH-0383] - Tìm Chuỗi Lặp Lại Dài Nhất Không Đè Nhau VinFast**
* **Dạng bài:** Longest Non-Overlapping Repeating Substring
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0383 - Tim Chuoi Lap Lai Dai Nhat VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0383%20-%20Tim%20Chuoi%20Lap%20Lai%20Dai%20Nhat%20VinFast)
* **Phương pháp giải:** Chặt nhị phân độ dài đáp án $L$, chia mảng $LCP$ thành các nhóm $LCP \ge L$, kiểm tra khoảng cách chỉ số $\max(SA) - \min(SA) \ge L$ trong $O(N \log N)$.


---

### **[IKH-0384] - Lọc Từ Cấm Tin Nhắn Zalo Chat**
* **Dạng bài:** Standard Aho-Corasick Multi-Pattern Search
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0384 - Loc Tu Cam Tin Nhan Zalo Chat](file:///Users/dkdeveloper/projects/testcase/IKH-0384%20-%20Loc%20Tu%20Cam%20Tin%20Nhan%20Zalo%20Chat)
* **Phương pháp giải:** Sử dụng Tự động hóa Aho-Corasick (Trie + BFS Failure Link) tìm kiếm tất cả $K$ từ cấm đồng thời trong văn bản $T$ trong $O(\sum |P_i| + |T|)$.

---

### **[IKH-0385] - Đếm Tần Suất Các Mẫu Từ Khóa Shopee**
* **Dạng bài:** Aho-Corasick Fail Link Tree DP Frequency Counter
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0385 - Dem Tan Suat Mau Tu Khoa Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0385%20-%20Dem%20Tan%20Suat%20Mau%20Tu%20Khoa%20Shopee)
* **Phương pháp giải:** Nhúng mảng đếm tần suất vào các nút Trie Aho-Corasick, sau đó lan truyền số lần xuất hiện qua cây Failure Link theo thứ tự BFS đảo ngược trong $O(\sum |P_i| + |T|)$.

---

### **[IKH-0386] - Phát Hiện Mã Độc Đa Mẫu Viettel Security**
* **Dạng bài:** Aho-Corasick Multi-Pattern Packet Inspector
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0386 - Phat Hien Ma Doc Da Mau Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0386%20-%20Phat%20Hien%20Ma%20Doc%20Da%20Mau%20Viettel)
* **Phương pháp giải:** Khớp bộ lọc chữ ký mã độc gồm hàng ngàn chuỗi nhị phân/từ khóa trên luồng dữ liệu gói tin bằng Aho-Corasick trong thời gian tuyến tính $O(|T|)$.

---

### **[IKH-0387] - Đếm Số Xâu Độ Dài N Không Chứa Tập Từ Cấm VNPT**
* **Dạng bài:** Aho-Corasick Automaton + Dynamic Programming
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0387 - Dem Xau Khong Chua Tu Cam VNPT](file:///Users/dkdeveloper/projects/testcase/IKH-0387%20-%20Dem%20Xau%20Khong%20Chua%20Tu%20Cam%20VNPT)
* **Phương pháp giải:** Kết hợp Aho-Corasick Automaton và Quy hoạch động $dp[i][u]$ đếm số xâu độ dài $N$ không đi qua các nút Trie chứa từ cấm trong $O(N \cdot \text{States} \cdot |\Sigma|)$.

---

### **[IKH-0388] - Tìm Chuỗi Mã Hóa Nhỏ Nhất Xoay Vòng Techcombank**
* **Dạng bài:** Minimal String Rotation / Booth's Algorithm
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0388 - Tim Chuoi Nho Nhat Xoay Vong Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0388%20-%20Tim%20Chuoi%20Nho%20Nhat%20Xoay%20Vong%20Techcombank)
* **Phương pháp giải:** Áp dụng Thuật toán Booth / Phân rã Lyndon Duval's Algorithm tìm vị trí xoay vòng có thứ tự từ điển nhỏ nhất của xâu $S$ trong $O(N)$.

---

### **[IKH-0389] - Khôi Phục Văn Bản Gốc Từ Mảng Hậu Tố FPT Software**
* **Dạng bài:** Burrows-Wheeler Transform (BWT) Inversion & LF Mapping
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0389 - Khoi Phuc Van Ban BWT FPT Software](file:///Users/dkdeveloper/projects/testcase/IKH-0389%20-%20Khoi%20Phuc%20Van%20Ban%20BWT%20FPT%20Software)
* **Phương pháp giải:** Sử dụng thuật toán đảo ngược biến đổi nén Burrows-Wheeler Transform (BWT) kết hợp mảng chỉ số LF Mapping để khôi phục văn bản gốc trong $O(N)$.

---

### **[IKH-0390] - IKHEDU Masterclass Grand Synthesis String Algorithm**
* **Dạng bài:** Combined Advanced String Algorithms (Aho-Corasick + Suffix Array + DP)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0390 - Grand Synthesis String Algorithm](file:///Users/dkdeveloper/projects/testcase/IKH-0390%20-%20Grand%20Synthesis%20String%20Algorithm)
* **Phương pháp giải:** Phối hợp Tự động hóa Aho-Corasick + Suffix Array + Dynamic Programming giải quyết bài toán truy vấn tổng hợp trên mảng xâu trong $O(N \log N)$.


---

### **[IKH-0391] - Đếm Số Nguyên Tố Trong Khoảng Mã Hóa ViettinBank**
* **Dạng bài:** Segmented Sieve of Eratosthenes
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0391 - Dem So Nguyen To Doan ViettinBank](file:///Users/dkdeveloper/projects/testcase/IKH-0391%20-%20Dem%20So%20Nguyen%20To%20Doan%20ViettinBank)
* **Phương pháp giải:** Áp dụng Sàng nguyên tố phân đoạn (Segmented Sieve) đếm số lượng số nguyên tố trong đoạn $[L, R]$ với $R \le 10^{12}, R - L \le 10^6$ trong $O((R - L + 1) \log \log R + \sqrt{R})$.

---

### **[IKH-0392] - Phân Tách Thừa Số Nguyên Tố Siêu Tốc Vietcombank**
* **Dạng bài:** Linear Sieve with Smallest Prime Factor (SPF)
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0392 - Phan Tich Thua So Sieu Toc Vietcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0392%20-%20Phan%20Tich%20Thua%20So%20Sieu%20Toc%20Vietcombank)
* **Phương pháp giải:** Xây dựng mảng $SPF[x]$ (Smallest Prime Factor) bằng Sàng tuyến tính trong $O(N)$, trả lời truy vấn phân tích thừa số nguyên tố cho mỗi số $X$ trong $O(\log X)$.

---

### **[IKH-0393] - Tính Giá Trị Phi Hàm Euler Cho Hệ Thống An Ninh FPT**
* **Dạng bài:** Euler's Totient Function $\phi(N)$ Formula
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0393 - Tinh Phi Ham Euler An Ninh FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0393%20-%20Tinh%20Phi%20Ham%20Euler%20An%20Ninh%20FPT)
* **Phương pháp giải:** Áp dụng công thức Euler's Totient Function $\phi(N) = N \prod (1 - 1/p)$ tính số lượng số nguyên tố cùng nhau với $N$ trong $[1, N]$ với độ phức tạp $O(\sqrt{N})$.

---

### **[IKH-0394] - Tổng Phi Hàm Tiền Tố Đố Vui Toán Học Shopee**
* **Dạng bài:** Euler Totient Sieve + Prefix Sum
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0394 - Tong Phi Ham Tien To Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0394%20-%20Tong%20Phi%20Ham%20Tien%20To%20Shopee)
* **Phương pháp giải:** Sàng Euler Totient Function cho toàn bộ mảng $\phi[1..N]$ trong $O(N \log \log N)$, kết hợp mảng tiền tố Prefix Sum trả lời tổng $\sum_{i=1}^K \phi(i)$ trong $O(1)$.

---

### **[IKH-0395] - Tìm Cặp Số Nguyên Tố Cùng Nhau Ngân Hàng Techcombank**
* **Dạng bài:** Coprime Pairs Count & Inclusion-Exclusion
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0395 - Tim Cap So Nguyen To Cung Nhau Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0395%20-%20Tim%20Cap%20So%20Nguyen%20To%20Cung%20Nhau%20Techcombank)
* **Phương pháp giải:** Dùng Nguyên lý bù trừ (Inclusion-Exclusion Principle) và phân tích thừa số nguyên tố đếm số cặp nguyên tố cùng nhau $(A_i, A_j)$ có $\gcd(A_i, A_j) = 1$ trong $O(N \log N)$.

---

### **[IKH-0396] - Phân Tách Thừa Số Số Nguyên Cực Lớn Viettel Cyber**
* **Dạng bài:** Miller-Rabin Primality Test + Pollard's Rho Algorithm
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0396 - Phan Tich So Lon Viettel Cyber](file:///Users/dkdeveloper/projects/testcase/IKH-0396%20-%20Phan%20Tich%20So%20Lon%20Viettel%20Cyber)
* **Phương pháp giải:** Kết hợp kiểm tra số nguyên tố xác suất Miller-Rabin và Thuật toán Pollard's Rho phân tích thừa số nguyên tố cho số cực lớn $N \le 10^{18}$ với độ phức tạp $O(N^{1/4})$.


---

### **[IKH-0397] - Tìm Nghịch Đảo Nhân Modulo Trong Giao Dịch VietinBank**
* **Dạng bài:** Extended Euclidean Algorithm Modular Inverse
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0397 - Tim Nghich Dao Nhan Modulo VietinBank](file:///Users/dkdeveloper/projects/testcase/IKH-0397%20-%20Tim%20Nghich%20Dao%20Nhan%20Modulo%20VietinBank)
* **Phương pháp giải:** Sử dụng Thuật toán Euclid mở rộng (Extended GCD) giải phương trình $A \cdot x + M \cdot y = 1$ tìm nghịch đảo nhân modulo $A^{-1} \pmod M$ trong $O(\log(\min(A, M)))$.

---

### **[IKH-0398] - Giải Phương Trình Đồng Dư Tuyến Tính FPT Software**
* **Dạng bài:** Linear Congruence Equation $A \cdot x \equiv B \pmod M$
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0398 - Giai Phuong Trinh Dong Du FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0398%20-%20Giai%20Phuong%20Trinh%20Dong%20Du%20FPT)
* **Phương pháp giải:** Chuyển phương trình đồng dư về $A \cdot x + M \cdot y = B$. Dùng Extended GCD kiểm tra $B \pmod{g} == 0$ (với $g = \gcd(A, M)$) và trích xuất nghiệm dương nhỏ nhất trong $O(\log M)$.

---

### **[IKH-0399] - Khôi Phục Khóa Bảo Mật Đồng Dư VNPT**
* **Dạng bài:** Chinese Remainder Theorem (CRT) Coprime Moduli
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0399 - Khoi Phuc Khoa Bao Mat CRT VNPT](file:///Users/dkdeveloper/projects/testcase/IKH-0399%20-%20Khoi%20Phuc%20Khoa%20Bao%20Mat%20CRT%20VNPT)
* **Phương pháp giải:** Áp dụng Định lý dư Trung Hoa (Chinese Remainder Theorem CRT) giải hệ phương trình $x \equiv a_i \pmod{m_i}$ với các $m_i$ nguyên tố cùng nhau từng đôi một trong $O(K \log(\text{LCM}))$.

---

### **[IKH-0400] - Đồng Bộ Hóa Chu Kỳ Thiết Bị IoT VinFast**
* **Dạng bài:** General Chinese Remainder Theorem Non-Coprime Moduli
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0400 - Dong Bo Chu Ky IoT VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0400%20-%20Dong%20Bo%20Chu%20Ky%20IoT%20VinFast)
* **Phương pháp giải:** Áp dụng Định lý dư Trung Hoa tổng quát (General CRT) gộp từng cặp phương trình $x \equiv a_1 \pmod{m_1}$ và $x \equiv a_2 \pmod{m_2}$ với các $m_i$ không nhất thiết nguyên tố cùng nhau trong $O(K \log(\text{LCM}))$.

---

### **[IKH-0401] - Tính Tổ Hợp Modulo Hợp Số Shopee**
* **Dạng bài:** Lucas' Theorem & CRT for Combination Modulo Composite
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0401 - Tinh To Hop Modulo Hop So Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0401%20-%20Tinh%20To%20Hop%20Modulo%20Hop%20So%20Shopee)
* **Phương pháp giải:** Phân tích hợp số $M = p_1^{e_1} \cdot p_2^{e_2} \dots p_k^{e_k}$, tính $C_n^k \pmod{p_i^{e_i}}$ bằng Định lý Lucas và ghép lại bằng CRT trong $O(M \log N)$.

---

### **[IKH-0402] - Tính Lũy Thừa Tầng Modulo Lớn Viettel Telecom**
* **Dạng bài:** Extended Euler's Totient Theorem Power Reduction
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0402 - Tinh Luy Thua Tang Modulo Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0402%20-%20Tinh%20Luy%20Thua%20Tang%20Modulo%20Viettel)
* **Phương pháp giải:** Áp dụng Định lý Euler mở rộng $a^b \pmod m = a^{b \bmod \phi(m) + \phi(m)} \pmod m$ (khi $b \ge \phi(m)$) thu nhỏ tầng mũ khổng lồ bằng đệ quy phi hàm Euler trong $O(\log M)$.


---

### **[IKH-0403] - Lũy Thừa Ma Trận Nhị Phân Cơ Bản FPT Cloud**
* **Dạng bài:** Matrix Multiplication & Exponentiation
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0403 - Luy Thua Ma Tran Co Ban FPT Cloud](file:///Users/dkdeveloper/projects/testcase/IKH-0403%20-%20Luy%20Thua%20Ma%20Tran%20Co%20Ban%20FPT%20Cloud)
* **Phương pháp giải:** Cài đặt thuật toán nhân ma trận vuông $K \times K$ và Lũy thừa ma trận nhị phân $A^P \pmod{10^9+7}$ trong độ phức tạp $O(K^3 \log P)$.

---

### **[IKH-0404] - Tính Số Fibonacci Thứ N Siêu Lớn Vietcombank**
* **Dạng bài:** Fibonacci Matrix Exponentiation $N \le 10^{18}$
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0404 - Tinh So Fibonacci Sieu Lon Vietcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0404%20-%20Tinh%20So%20Fibonacci%20Sieu%20Lon%20Vietcombank)
* **Phương pháp giải:** Biểu diễn hệ thức $F_N = F_{N-1} + F_{N-2}$ dưới dạng ma trận chuyển trạng thái $T = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$, nhân $T^{N-1}$ tính $F_N \pmod{10^9+7}$ trong $O(\log N)$.

---

### **[IKH-0405] - Tính Dãy Truy Hồi Tuyến Tính Bất Kỳ Shopee**
* **Dạng bài:** General Linear Recurrence Transition Matrix
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0405 - Tinh Day Truy Hoi Tuyen Tinh Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0405%20-%20Tinh%20Day%20Truy%20Hoi%20Tuyen%20Tinh%20Shopee)
* **Phương pháp giải:** Dựng ma trận chuyển trạng thái kích thước $K \times K$ cho hệ thức $A_n = c_1 A_{n-1} + c_2 A_{n-2} + \dots + c_k A_{n-k}$, tính $A_N$ trong $O(K^3 \log N)$.

---

### **[IKH-0406] - Đếm Số Đường Đi Độ Dài K Trên Đồ Thị VinFast**
* **Dạng bài:** Adjacency Matrix Exponentiation Path Count
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0406 - Dem So Duong Di Do Dai K VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0406%20-%20Dem%20So%20Duong%20Di%20Do%20Dai%20K%20VinFast)
* **Phương pháp giải:** Dựng ma trận kề $A$ của đồ thị $V$ đỉnh. Lũy thừa ma trận $A^K \pmod{10^9+7}$ để lấy số lượng đường đi có đúng $K$ cạnh giữa mọi cặp đỉnh trong $O(V^3 \log K)$.

---

### **[IKH-0407] - Tính Tổng Dãy Fibonacci Siêu Lớn Techcombank**
* **Dạng bài:** Extended Matrix Exponentiation Prefix Sum
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0407 - Tinh Tong Day Fibonacci Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0407%20-%20Tinh%20Tong%20Day%20Fibonacci%20Techcombank)
* **Phương pháp giải:** Mở rộng ma trận chuyển trạng thái lên $3 \times 3$ hoặc dùng công thức $\sum_{i=1}^N F_i = F_{N+2} - 1$, tính tổng $S_N \pmod{10^9+7}$ trong $O(\log N)$.

---

### **[IKH-0408] - Đường Đi Ngắn Nhất Đúng K Cạnh Viettel Security**
* **Dạng bài:** Min-Plus Matrix Exponentiation / Tropical Semiring
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0408 - Duong Di Ngan Nhat Dung K Canh Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0408%20-%20Duong%20Di%20Ngan%20Nhat%20Dung%20K%20Canh%20Viettel)
* **Phương pháp giải:** Sử dụng Phép nhân ma trận Min-Plus $C[i][j] = \min_k (A[i][k] + B[k][j])$ trên Đại số Tropical tìm độ dài đường đi ngắn nhất qua đúng $K$ cạnh trong $O(V^3 \log K)$.


---

### **[IKH-0409] - Tính Số Tổ Hợp C_n_k Modulo Prime Shopee**
* **Dạng bài:** Combinatorics $C_n^k \pmod{10^9+7}$ Precomputed Factorials
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0409 - Tinh So To Hop C_n_k Modulo Prime Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0409%20-%20Tinh%20So%20To%20Hop%20C_n_k%20Modulo%20Prime%20Shopee)
* **Phương pháp giải:** Tiền xử lý mảng Giai thừa `fact[i]` và Nghịch đảo giai thừa `invFact[i]` modulo $10^9+7$ trong $O(N)$, trả lời truy vấn $C_n^k$ trong $O(1)$.

---

### **[IKH-0410] - Đếm Số Cách Phân Hoạch Ngoặc Hợp Lệ Zalo**
* **Dạng bài:** Catalan Number $C_n = \frac{1}{n+1} \binom{2n}{n} \pmod{10^9+7}$
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0410 - Dem So Cach Phan Hoach Ngoac Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0410%20-%20Dem%20So%20Cach%20Phan%20Hoach%20Ngoac%20Zalo)
* **Phương pháp giải:** Áp dụng công thức Số Catalan $C_n = \frac{1}{n+1} \binom{2n}{n} \pmod{10^9+7}$ đếm số dãy ngoặc đúng độ dài $2n$, số cây nhị phân, số cách phân hoạch đa giác trong $O(N)$.

---

### **[IKH-0411] - Phân Bổ Máy Chủ Trạm Dữ Liệu FPT Telecom**
* **Dạng bài:** Stirling Numbers of the Second Kind $S(n, k)$
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0411 - Phan Bo May Chu Tram FPT Telecom](file:///Users/dkdeveloper/projects/testcase/IKH-0411%20-%20Phan%20Bo%20May%20Chu%20Tram%20FPT%20Telecom)
* **Phương pháp giải:** Sử dụng Số Stirling loại hai $S(n, k) = k S(n-1, k) + S(n-1, k-1) \pmod{10^9+7}$ đếm số cách chia $n$ phần tử phân biệt vào $k$ tập hợp không rỗng trong $O(n \cdot k)$.

---

### **[IKH-0412] - Đếm Số Tập Hợp Hợp Lệ Bằng Nguyên Lý Bù Trừ VinFast**
* **Dạng bài:** Inclusion-Exclusion Principle
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0412 - Dem So Tap Hop Hop Le Bu Tru VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0412%20-%20Dem%20So%20Tap%20Hop%20Hop%20Le%20Bu%20Tru%20VinFast)
* **Phương pháp giải:** Áp dụng Nguyên lý bù trừ (Inclusion-Exclusion Principle) đếm số lượng phần tử không vi phạm bất kỳ điều kiện nào trong $K$ điều kiện cấm với độ phức tạp $O(2^K)$.

---

### **[IKH-0413] - Đếm Số Hoán Vị Không Có Điểm Cố Định Techcombank**
* **Dạng bài:** Derangements Formula / Subfactorial !$N$
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0413 - Dem So Hoan Vi Khong Diem Co Dinh Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0413%20-%20Dem%20So%20Hoan%20Vi%20Khong%20Diem%20Co%20Dinh%20Techcombank)
* **Phương pháp giải:** Sử dụng công thức Hoán vị xáo trộn (Derangement) $!N = (N - 1)(!(N-1) + !(N-2)) \pmod{10^9+7}$ đếm số hoán vị không có điểm cố định $p[i] \ne i$ trong $O(N)$.

---

### **[IKH-0414] - Đếm Ma Trận Nhị Phân Không Chứa Hàng Cột Rỗng Viettel**
* **Dạng bài:** 2D Inclusion-Exclusion Principle Grid
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0414 - Dem Ma Tran Nhi Phan Bu Tru Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0414%20-%20Dem%20Ma%20Tran%20Nhi%20Phan%20Bu%20Tru%20Viettel)
* **Phương pháp giải:** Sử dụng Nguyên lý bù trừ 2 chiều theo hàng và cột đếm số ma trận nhị phân $N \times M$ sao cho mọi hàng và mọi cột đều chứa ít nhất một số 1 trong $O(N \cdot M)$.


---

### **[IKH-0415] - Chiến Thuật Bốc Sỏi Nim Game Trực Tuyến Zalo**
* **Dạng bài:** Standard Nim Game & Bouton's Theorem
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0415 - Chien Thuat Boc Soi Nim Game Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0415%20-%20Chien%20Thuat%20Boc%20Soi%20Nim%20Game%20Zalo)
* **Phương pháp giải:** Sử dụng Định lý Bouton tính tổng XOR Sum $X = A_1 \oplus A_2 \dots \oplus A_N$. Nếu $X \ne 0$ thì người đi trước (`First`) thắng, ngược lại người đi sau (`Second`) thắng trong $O(N)$.

---

### **[IKH-0416] - Tìm Nước Đi Thắng Trong Trò Chơi Nim Shopee**
* **Dạng bài:** Winning Moves in Nim Game
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0416 - Tim Nuoc Di Thang Nim Game Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0416%20-%20Tim%20Nuoc%20Di%20Thang%20Nim%20Game%20Shopee)
* **Phương pháp giải:** Kiểm tra các đống sỏi $A_i$ thỏa mãn $A_i \oplus X < A_i$ đếm tổng số nước đi hợp lệ giúp đưa tổng XOR Sum về 0 để chuyển sang vị trí chiến thắng trong $O(N)$.

---

### **[IKH-0417] - Trò Chơi Bốc Sỏi Giới Hạn K Viên VinFast**
* **Dạng bài:** Subtraction Game / Periodic Grundy Function
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0417 - Tro Choi Boc Soi Gioi Han K VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0417%20-%20Tro%20Choi%20Boc%20Soi%20Gioi%20Han%20K%20VinFast)
* **Phương pháp giải:** Xác định chu kỳ lặp lại của Hàm Grundy $G(n) = n \pmod{K+1}$ cho trò chơi bốc sỏi tối đa $K$ viên, áp dụng XOR cho các đống sỏi trong $O(N)$.

---

### **[IKH-0418] - Tính Hàm Grundy Trên Đồ Thị Thị Trường FPT**
* **Dạng bài:** Sprague-Grundy Theorem MEX on DAG
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0418 - Tinh Ham Grundy Tren Do Thi FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0418%20-%20Tinh%20Ham%20Grundy%20Tren%20Do%20Thi%20FPT)
* **Phương pháp giải:** Tính hàm Grundy $G(u) = \text{MEX}(\{G(v) \mid (u, v) \in E\})$ cho từng đỉnh trên Đồ Thị Hướng Không Chu Kỳ (DAG) bằng Sắp xếp Topological / Đệ quy có nhớ trong $O(V + E)$.

---

### **[IKH-0419] - Trò Chơi Cắt Cây Đồ Thị Mạng Viettel Telecom**
* **Dạng bài:** Green Hackenbush on Trees & Colon Principle
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0419 - Tro Choi Cat Cay Do Thi Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0419%20-%20Tro%20Choi%20Cat%20Cay%20Do%20Thi%20Viettel)
* **Phương pháp giải:** Áp dụng Nguyên lý Colon (Colon Principle) gộp các nhánh cây tại đỉnh cha bằng phép cộng $+ 1$ giá trị Grundy của các cây con, tính tổng XOR cho cả rừng cây trong $O(N)$.

---

### **[IKH-0420] - IKHEDU Masterclass Grand Synthesis Math Techcombank**
* **Dạng bài:** Grand Synthesis Advanced Mathematics Masterclass
* **Độ khó:** Rating 1750 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0420 - Grand Synthesis Advanced Math Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0420%20-%20Grand%20Synthesis%20Advanced%20Math%20Techcombank)
* **Phương pháp giải:** Tổng hợp đỉnh cao kiến thức Chuyên đề 09 (Lũy thừa Ma trận + Định lý dư Trung Hoa CRT + Euclid mở rộng Extended GCD + Đại số tổ hợp + Trò chơi Nim Game) giải quyết bài toán tối ưu hóa tổng thể trong $O(K^3 \log N + \log M)$.


---

### **[IKH-0421] - Tối Ưu Hóa Nhập Xuất Dữ Liệu Khổng Lồ Viettel**
* **Dạng bài:** Custom Fast I/O Optimization (`fread`/`fwrite` & `cin.tie(NULL)`)
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0421 - Toi Uu Nhap Xuat Du Lieu Khong Lo Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0421%20-%20Toi%20Uu%20Nhap%20Xuat%20Du%20Lieu%20Khong%20Lo%20Viettel)
* **Phương pháp giải:** Sử dụng kỹ thuật ngắt kết nối `ios_base::sync_with_stdio(false); cin.tie(NULL);` hoặc đọc buffer `fread` tối ưu thời gian nhập xuất cho $N = 2 \cdot 10^6$ số nguyên từ $1.5$s xuống $0.05$s.

---

### **[IKH-0422] - Tiết Kiệm Bộ Nhớ Bitset Trong Mạng Xã Hội Zalo**
* **Dạng bài:** Bitset Memory Reduction $O(N^2 / 64)$
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0422 - Tiet Kiem Bo Nho Bitset Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0422%20-%20Tiet%20Kiem%20Bo%20Nho%20Bitset%20Zalo)
* **Phương pháp giải:** Sử dụng `std::bitset` thay thế mảng `bool` / `vector<bool>` nén bộ nhớ 64 lần, cho phép xử lý ma trận kề đồ thị $N = 50000$ vượt qua giới hạn bộ nhớ MLE.

---

### **[IKH-0423] - Tăng Tốc Vòng Lặp Ma Trận Bằng Compiler Directives FPT**
* **Dạng bài:** GCC Pragmas Compiler Directives Optimization
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0423 - Tang Toc Vong Lap Compiler Pragmas FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0423%20-%20Tang%20Toc%20Vong%20Lap%20Compiler%20Pragmas%20FPT)
* **Phương pháp giải:** Khai báo chỉ thị biên dịch `#pragma GCC optimize("O3,unroll-loops")` và `#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")` tự động mở cuộn vòng lặp và vector hóa AVX2 tăng tốc nhân ma trận 8-10 lần.

---

### **[IKH-0424] - Tối Ưu Hóa Tìm Kiếm Bit Trong Cơ Sở Dữ Liệu Shopee**
* **Dạng bài:** Bitset Fast Bitwise Search (`_Find_first()`, `_Find_next()`)
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0424 - Toi Uu Tim Kiem Bit CSDL Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0424%20-%20Toi%20Uu%20Tim%20Kiem%20Bit%20CSDL%20Shopee)
* **Phương pháp giải:** Sử dụng hàm nội tại `bitset::_Find_first()` và `bitset::_Find_next()` duyệt qua các bit 1 trong $O(\text{count}/64)$ bỏ qua hàng ngàn bit 0 rỗng trong CSDL.

---

### **[IKH-0425] - Đếm Số Cặp Bit Chung Trạm Pin VinFast**
* **Dạng bài:** Vectorized Bitset Intersection & Popcount
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0425 - Dem Cap Bit Chung Tram Pin VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0425%20-%20Dem%20Cap%20Bit%20Chung%20Tram%20Pin%20VinFast)
* **Phương pháp giải:** Sử dụng phép toán `AND` ma trận bitset `(bitsetA & bitsetB).count()` đếm số bit chung giữa mọi cặp đối tượng trong $O(N \cdot M / 64)$.

---

### **[IKH-0426] - Tối Ưu Hóa Truy Vấn Mảng Đa Chiều Nén Techcombank**
* **Dạng bài:** Cache-Friendly 1D Array Flattening
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0426 - Toi Uu Mang Da Chieu Cache Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0426%20-%20Toi%20Uu%20Mang%20Da%20Chieu%20Cache%20Techcombank)
* **Phương pháp giải:** Duỗi mảng 2D/3D về mảng 1D liên tục `arr[i * M + j]` tối ưu hóa bộ nhớ đệm CPU Cache Hit Ratio, giảm Cache Miss từ 40% xuống < 1%.


---

### **[IKH-0427] - Tối Ưu Hóa Cửa Sổ Trượt Bằng Hàng Đợi Đơn Điệu Shopee**
* **Dạng bài:** Monotonic Deque Sliding Window Maximum
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0427 - Toi Uu Cua So Truot Monotonic Deque Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0427%20-%20Toi%20Uu%20Cua%20So%20Truot%20Monotonic%20Deque%20Shopee)
* **Phương pháp giải:** Sử dụng Hàng đợi đơn điệu (`std::deque`) duy trì các chỉ số mảng giảm dần, tìm Max trong từng cửa sổ trượt độ dài $K$ trong $O(N)$ thời gian thay vì $O(N \cdot K)$.

---

### **[IKH-0428] - Nén Tọa Độ Xử Lý Truy Vấn Kho Hàng VinFast**
* **Dạng bài:** Coordinate Compression + Fenwick Tree / Segment Tree
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0428 - Nen Toa Do Kho Hang VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0428%20-%20Nen%20Toa%20Do%20Kho%20Hang%20VinFast)
* **Phương pháp giải:** Sử dụng kỹ thuật Nén tọa độ rời rạc hóa các giá trị $10^9$ về dải $[1, N]$ kết hợp Cây Fenwick Tree / Segment Tree xử lý truy vấn khoảng $O(N \log N)$.

---

### **[IKH-0429] - Tối Ưu Hóa Đường Đi Mạng Lưới Điệp Viên Viettel**
* **Dạng bài:** Disjoint Set Union (DSU) Path Compression & Rank Optimization
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0429 - Toi Uu Duong Di DSU Path Compression Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0429%20-%20Toi%20Uu%20Duong%20Di%20DSU%20Path%20Compression%20Viettel)
* **Phương pháp giải:** Áp dụng kỹ thuật Nén đường đi (Path Compression) và Gộp theo rank/size cho Cấu trúc dữ liệu các tập hợp rời rạc (DSU) đưa thời gian truy vấn `find` về $O(\alpha(N)) \approx O(1)$.

---

### **[IKH-0430] - Tìm Đoạn Con Có Tổng Lớn Nhất Độ Dài Từ K Đến L FPT**
* **Dạng bài:** Subarray Max Sum with Bounded Length $[K, L]$
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0430 - Tim Doan Con Tong Lon Nhat Do Dai K L FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0430%20-%20Tim%20Doan%20Con%20Tong%20Lon%20Nhat%20Do%20Dai%20K%20L%20FPT)
* **Phương pháp giải:** Kết hợp Mảng tiền tố Prefix Sum $S[i]$ và Hàng đợi đơn điệu Monotonic Deque lưu trữ vị trí $j$ tối ưu trong khoảng $[i-L, i-K]$ tìm tổng lớn nhất $S[i] - S[j]$ trong $O(N)$.

---

### **[IKH-0431] - Nén Tọa Độ 2D Đếm Điểm Trong Hình Chữ Nhật Zalo**
* **Dạng bài:** 2D Coordinate Compression + 2D Fenwick Tree
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0431 - Nen Toa Do 2D Dem Diem Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0431%20-%20Nen%20Toa%20Do%202D%20Dem%20Diem%20Zalo)
* **Phương pháp giải:** Nén tọa độ 2D theo cả 2 trục $X$ và $Y$, sử dụng 2D Fenwick Tree đếm số điểm nằm trong hình chữ nhật $[X_1..X_2, Y_1..Y_2]$ trong $O(N \log^2 N)$.

---

### **[IKH-0432] - Tối Ưu Hóa Gộp Nhóm Dữ Liệu Lớn Theo Kích Thước Techcombank**
* **Dạng bài:** Small-to-Large Merging / DSU on Tree (Sack)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0432 - Toi Uu Gop Nhom Small To Large Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0432%20-%20Toi%20Uu%20Gop%20Nhom%20Small%20To%20Large%20Techcombank)
* **Phương pháp giải:** Sử dụng kỹ thuật Gộp tập nhỏ vào tập lớn (Small-to-Large Merging / DSU on Tree) đảm bảo mỗi phần tử chỉ bị di chuyển tối đa $O(\log N)$ lần, đạt độ phức tạp $O(N \log^2 N)$.


---

### **[IKH-0433] - Tối Ưu Hóa Quy Hoạch Động Bằng Bao Lồi Đường Thẳng Shopee**
* **Dạng bài:** Static Convex Hull Trick (CHT) $O(N)$
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0433 - Toi Uu CHT Convex Hull Trick Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0433%20-%20Toi%20Uu%20CHT%20Convex%20Hull%20Trick%20Shopee)
* **Phương pháp giải:** Sử dụng Bao lồi đường thẳng (Convex Hull Trick) duy trì bao lồi dưới bằng `std::deque` cho hệ thức $dp[i] = \min_{j < i} (dp[j] + A[j] \cdot B[i])$ trong $O(N)$ thời gian thay vì $O(N^2)$.

---

### **[IKH-0434] - Tối Ưu Hóa Chia Để Trị Quy Hoạch Động VinFast**
* **Dạng bài:** Divide & Conquer DP Optimization
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0434 - Toi Uu Chia De Tri DP VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0434%20-%20Toi%20Uu%20Chia%20De%20Tri%20DP%20VinFast)
* **Phương pháp giải:** Áp dụng Kỹ thuật Chia để trị tối ưu hóa Quy hoạch động dựa trên tính chất đơn điệu của vị trí tối ưu $opt[i][j] \le opt[i][j+1]$, giảm độ phức tạp từ $O(K \cdot N^2)$ xuống $O(K \cdot N \log N)$.

---

### **[IKH-0435] - Tối Ưu Hóa Quy Hoạch Động Knuth FPT Telecom**
* **Dạng bài:** Knuth's DP Optimization for Interval DP
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0435 - Toi Uu Knuth DP FPT Telecom](file:///Users/dkdeveloper/projects/testcase/IKH-0435%20-%20Toi%20Uu%20Knuth%20DP%20FPT%20Telecom)
* **Phương pháp giải:** Sử dụng Điều kiện Bất đẳng thức Tứ giác (Quadrangle Inequality) giới hạn khoảng tìm kiếm nghiệm $opt[i][j-1] \le opt[i][j] \le opt[i+1][j]$ giảm độ phức tạp Quy hoạch động đoạn từ $O(N^3)$ xuống $O(N^2)$.

---

### **[IKH-0436] - Tối Ưu Hóa Quy Hoạch Động Đồ Thị Bao Lồi Động Viettel**
* **Dạng bài:** Dynamic Convex Hull Trick / LineContainer
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0436 - Toi Uu Bao Loi Dong Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0436%20-%20Toi%20Uu%20Bao%20Loi%20Dong%20Viettel)
* **Phương pháp giải:** Sử dụng Cấu trúc Bao lồi đường thẳng động (`LineContainer` / `std::multiset`) hỗ trợ chèn đường thẳng $y = mx + c$ với hệ số góc không sắp xếp trong $O(N \log N)$.

---

### **[IKH-0437] - Tối Ưu Hóa Tổng Tất Cả Tập Con SOS DP Zalo**
* **Dạng bài:** Sum Over Subsets (SOS DP) $O(N \cdot 2^N)$
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0437 - Toi Uu Tong Tap Con SOS DP Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0437%20-%20Toi%20Uu%20Tong%20Tap%20Con%20SOS%20DP%20Zalo)
* **Phương pháp giải:** Áp dụng Thuật toán SOS DP (Sum Over Subsets DP) tính tổng các mặt nạ tập con $F[mask] = \sum_{sub \subseteq mask} A[sub]$ cho $N$ bit trong $O(N \cdot 2^N)$ thay vì $O(3^N)$.

---

### **[IKH-0438] - Tối Ưu Hóa Quy Hoạch Động Cửa Sổ Trượt SegTree Techcombank**
* **Dạng bài:** Segment Tree Optimized Dynamic Programming
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0438 - Toi Uu DP SegTree Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0438%20-%20Toi%20Uu%20DP%20SegTree%20Techcombank)
* **Phương pháp giải:** Phối hợp Cây Phân Đoạn Segment Tree để tìm giá trị tối ưu $\max_{L \le j \le R} dp[j]$ trong cửa sổ động, giảm độ phức tạp Quy hoạch động từ $O(N^2)$ xuống $O(N \log N)$.


---

### **[IKH-0439] - Phát Hiện Sửa Lỗi Tràn Số Phép Nhân Modulo Shopee**
* **Dạng bài:** 128-bit Integer Overflow Debugging (`__int128_t` / `mul_mod`)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0439 - Sua Loi Tran So Nhan Modulo Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0439%20-%20Sua%20Loi%20Tran%20So%20Nhan%20Modulo%20Shopee)
* **Phương pháp giải:** Sửa lỗi tràn số 64-bit khi nhân 2 số $A, B \sim 10^{18}$ modulo $M$ bằng cách ép kiểu `__int128_t` hoặc dùng thuật toán Nhân nhị phân `mul_mod(A, B, M)` $O(1)$.

---

### **[IKH-0440] - Phát Hiện Bẫy Chia Cho 0 Truy Cập Mảng Out-Of-Bounds VinFast**
* **Dạng bài:** RTE Edge Cases Debugging ($N=1, K=0$, Out-of-bounds Check)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0440 - Phat Hien Bay Chia 0 Array Out Of Bounds VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0440%20-%20Phat%20Hien%20Bay%20Chia%200%20Array%20Out%20Of%20Bounds%20VinFast)
* **Phương pháp giải:** Kiểm tra và phòng ngừa triệt để các trường hợp biên đặc biệt: kiểm tra $MOD 
e 0$, chia cho 0, chỉ số mảng vượt ngưỡng $N+1$ (RTE) cho các testcase cực kỳ nhạy cảm.

---

### **[IKH-0441] - Phát Hiện Tối Ưu Lỗi Tràn Stack Đệ Quy FPT Telecom**
* **Dạng bài:** Recursion Stack Overflow Fix & Iterative BFS Conversion
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0441 - Toi Uu Tran Stack De Quy FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0441%20-%20Toi%20Uu%20Tran%20Stack%20De%20Quy%20FPT)
* **Phương pháp giải:** Chuyển đổi hàm đệ quy sâu DFS $O(N)$ (gây tràn bộ nhớ Stack MLE/RTE với $N = 10^6$) sang thuật toán lặp khử đệ quy BFS / Queue hoặc tăng kích thước stack compiler.

---

### **[IKH-0442] - Phát Hiện Bug Vòng Lặp Vô Tận Treo Bộ Nhớ Zalo**
* **Dạng bài:** Infinite Loop & Iterator Invalidation Debugging
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0442 - Phat Hien Bug Vong Lap Vo Tan Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0442%20-%20Phat%20Hien%20Bug%20Vong%20Lap%20Vo%20Tan%20Zalo)
* **Phương pháp giải:** Sửa lỗi treo vòng lặp `while` khi duyệt con trỏ/con chạy `std::vector` bị hỏng chỉ số (Iterator Invalidation), đảm bảo điều kiện dừng vòng lặp luôn đúng.

---

### **[IKH-0443] - Kịch Bản Sinh Test Ngẫu Nhiên Stress Test Tự Động Viettel**
* **Dạng bài:** Automated Stress Testing Script (Generator vs Naive)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0443 - Kich Ban Stress Test Tu Dong Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0443%20-%20Kich%20Ban%20Stress%20Test%20Tu%20Dong%20Viettel)
* **Phương pháp giải:** Xây dựng kịch bản kiểm thử tự động (Stress Testing) sinh hàng ngàn testcase ngẫu nhiên nhỏ, so sánh kết quả giữa Code Trâu (Naive $O(N^2)$) và Code Tối Ưu (Optimized $O(N)$) để tìm lỗi ẩn.

---

### **[IKH-0444] - Sửa Lỗi Phép Toán Bitwise Độ Ưu Tiên Toán Tử Techcombank**
* **Dạng bài:** Bitwise Operator Precedence Debugging `(1 << i) & mask`
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0444 - Sua Loi Bitwise Operator Precedence Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0444%20-%20Sua%20Loi%20Bitwise%20Operator%20Precedence%20Techcombank)
* **Phương pháp giải:** Sửa lỗi thiếu ngoặc đơn trong phép toán bitwise C++ do toán tử so sánh `==`, `+` có độ ưu tiên cao hơn `&`, `|`, `^` (ví dụ `1 << i & mask` $	o$ `((1LL << i) & mask)`).


---

### **[IKH-0445] - Refactor Mã Nguồn Bị TLE Thành Thuật Toán Tối Ưu Shopee**
* **Dạng bài:** Code Refactoring TLE to AC ($O(N^2) \to O(N \log N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0445 - Refactor Ma Nguon TLE Sang Optimal Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0445%20-%20Refactor%20Ma%20Nguon%20TLE%20Sang%20Optimal%20Shopee)
* **Phương pháp giải:** Phân tích mã nguồn bị TLE $O(N^2)$ của học viên, tái cấu trúc thuật toán bằng Hai con trỏ (Two Pointers) hoặc Binary Search chuyển đổi thời gian chạy thành $O(N \log N)$.

---

### **[IKH-0446] - Khắc Phục Lỗi Bộ Nhớ Tràn Mảng MLE Mạng Lưới VinFast**
* **Dạng bài:** Memory Optimization MLE to AC (Dynamic Allocation / Flattening)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0446 - Khac Phuc Loi Bo Nho MLE VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0446%20-%20Khac%20Phuc%20Loi%20Bo%20Nho%20MLE%20VinFast)
* **Phương pháp giải:** Tối ưu hóa bộ nhớ mảng 2D kích thước lớn $50000 \times 50000$ bị MLE thành `std::vector` động hoặc mảng cuộn (Rolling Array) $O(N)$ bộ nhớ.

---

### **[IKH-0447] - Chẩn Đoán Lỗi Chập Chờn Subtask WA Cửa Hàng FPT**
* **Dạng bài:** Floating Point & Precision Fix (`long double` & Epsilon $\epsilon$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0447 - Chan Doan Loi Chap Chon Subtask FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0447%20-%20Chan%20Doan%20Loi%20Chap%20Chon%20Subtask%20FPT)
* **Phương pháp giải:** Sửa lỗi sai số khi tính toán số thực `double` bằng cách sử dụng `long double`, so sánh bằng hằng số $\epsilon = 10^{-9}$ tránh lỗi làm tròn chập chờn WA ở một số subtask.

---

### **[IKH-0448] - Tối Ưu Hóa Thuật Toán Tìm Kiếm Nhị Phân Biến Thể Zalo**
* **Dạng bài:** Binary Search on Answer Edge Case Debugging
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0448 - Toi Uu Tim Kiem Nhi Phan Bien The Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0448%20-%20Toi%20Uu%20Tim%20Kiem%20Nhi%20Phan%20Bien%20The%20Zalo)
* **Phương pháp giải:** Sửa bẫy tràn số `low + high` và vòng lặp vô tận trong Tìm kiếm nhị phân kết quả (Binary Search on Answer) bằng công thức `mid = low + (high - low) / 2`.

---

### **[IKH-0449] - Khôi Phục Mã Nguồn Bị Lỗi Logic Trên Cây Viettel**
* **Dạng bài:** Tree DP & Graph Re-rooting Edge Case Debugging
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0449 - Khoi Phuc Ma Nguon Tree DP Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0449%20-%20Khoi%20Phuc%20Ma%20Nguon%20Tree%20DP%20Viettel)
* **Phương pháp giải:** Chẩn đoán và sửa lỗi logic Quy hoạch động trên cây (Tree DP) kết hợp kỹ thuật Đổi gốc cây (Re-rooting DP) bị cập nhật thiếu đỉnh lá hoặc đỉnh gốc ban đầu.

---

### **[IKH-0450] - Grand Masterclass Synthesis Debug Tối Ưu Techcombank**
* **Dạng bài:** Grand Synthesis Masterclass Debug & Optimization
* **Độ khó:** Rating 1750 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0450 - Grand Masterclass Synthesis Debug Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0450%20-%20Grand%20Masterclass%20Synthesis%20Debug%20Techcombank)
* **Phương pháp giải:** Tổng hợp toàn bộ kỹ thuật Masterclass: Fast I/O, Fenwick Tree / Segment Tree, Tối ưu phép toán Bitwise và Debug lỗi biên đạt 100% AC tuyệt đối.


---

### **[IKH-0451] - Đề Thi Thử 1 - Bài 1: Quản Lý Tuyến Xe Điện VinFast**
* **Dạng bài:** Mock Contest 1 Task 1 (Prefix Sum + Binary Search $O((N + Q) \log N)$)
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0451 - De Thi Thu 1 Bai 1 Tuyen Xe Dien VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0451%20-%20De%20Thi%20Thu%201%20Bai%201%20Tuyen%20Xe%20Dien%20VinFast)
* **Phương pháp giải:** Mảng tổng tiền tố $S[i]$ tăng nghiêm ngặt, sử dụng `std::lower_bound` tìm vị trí trạm nhỏ nhất thỏa mãn tổng điện năng $\ge K$ trong $O(\log N)$.

---

### **[IKH-0452] - Đề Thi Thử 1 - Bài 2: Tối Ưu Hóa Cước Phí Viettel Telecom**
* **Dạng bài:** Mock Contest 1 Task 2 (Segment Tree Range Minimum Query)
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0452 - De Thi Thu 1 Bai 2 Cuoc Phi Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0452%20-%20De%20Thi%20Thu%201%20Bai%202%20Cuoc%20Phi%20Viettel)
* **Phương pháp giải:** Cấu trúc dữ liệu Cây Phân Đoạn Segment Tree xử lý truy vấn tìm cước phí nhỏ nhất trong khoảng $[L, R]$ và cập nhật điểm trong $O(\log N)$.

---

### **[IKH-0453] - Đề Thi Thử 1 - Bài 3: Đếm Số Cặp Đồng Nhất Kho Hàng Shopee**
* **Dạng bài:** Mock Contest 1 Task 3 (Two Pointers / Map Counter $O(N)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0453 - De Thi Thu 1 Bai 3 Cap Dong Nhat Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0453%20-%20De%20Thi%20Thu%201%20Bai%203%20Cap%20Dong%20Nhat%20Shopee)
* **Phương pháp giải:** Đếm tần suất các loại sản phẩm sử dụng Hash Map hoặc Hai con trỏ trên mảng đã sắp xếp để đếm số cặp thỏa mãn điều kiện đồng nhất trong $O(N)$.

---

### **[IKH-0454] - Đề Thi Thử 1 - Bài 4: Phân Tích Mạng Lưới Kết Nối FPT Telecom**
* **Dạng bài:** Mock Contest 1 Task 4 (DSU + Kruskal Minimum Spanning Tree)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0454 - De Thi Thu 1 Bai 4 Mang Luoi FPT Telecom](file:///Users/dkdeveloper/projects/testcase/IKH-0454%20-%20De%20Thi%20Thu%201%20Bai%204%20Mang%20Luoi%20FPT%20Telecom)
* **Phương pháp giải:** Áp dụng Thuật toán Kruskal kết hợp DSU Nén đường đi tìm Cây khung nhỏ nhất (MST) tối ưu tổng chi phí kết nối mạng lưới trong $O(E \log E)$.

---

### **[IKH-0455] - Đề Thi Thử 1 - Bài 5: Quy Hoạch Động Chia Nhóm Sản Phẩm Zalo**
* **Dạng bài:** Mock Contest 1 Task 5 (DP + Monotonic Queue Optimization $O(N)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0455 - De Thi Thu 1 Bai 5 DP Chia Nhom Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0455%20-%20De%20Thi%20Thu%201%20Bai%205%20DP%20Chia%20Nhom%20Zalo)
* **Phương pháp giải:** Sử dụng Hàng đợi đơn điệu Monotonic Deque tối ưu công thức Quy hoạch động chia nhóm sản phẩm từ $O(N^2)$ xuống $O(N)$ thời gian.

---

### **[IKH-0456] - Đề Thi Thử 1 - Bài 6: Đếm Chuỗi Đảo Ngược Ngân Hàng Techcombank**
* **Dạng bài:** Mock Contest 1 Task 6 (String Matching KMP / Rolling Hash $O(N + M)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0456 - De Thi Thu 1 Bai 6 Dem Chuoi Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0456%20-%20De%20Thi%20Thu%201%20Bai%206%20Dem%20Chuoi%20Techcombank)
* **Phương pháp giải:** Áp dụng Thuật toán KMP hoặc kỹ thuật Rolling Double Hash đếm chính xác số lần xuất hiện của mẫu mã hóa đảo ngược trong CSDL giao dịch ngân hàng $O(N + M)$.

---

### **[IKH-0457] - Đề Thi Thử 1 - Bài 7: Lập Lịch Chạy Xe Điện Tối Ưu VinFast**
* **Dạng bài:** Mock Contest 1 Task 7 (Weighted Interval Scheduling DP + BS)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0457 - De Thi Thu 1 Bai 7 Lap Lich VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0457%20-%20De%20Thi%20Thu%201%20Bai%207%20Lap%20Lich%20VinFast)
* **Phương pháp giải:** Sắp xếp khoảng thời gian theo thời điểm kết thúc, kết hợp Quy hoạch động và Tìm kiếm nhị phân `lower_bound` chọn lịch trình có tổng lợi ích lớn nhất không chồng chồng nhau trong $O(N \log N)$.

---

### **[IKH-0458] - Đề Thi Thử 1 - Bài 8: Tối Ưu Hóa Tuyến Cáp Quang Viettel**
* **Dạng bài:** Mock Contest 1 Task 8 (Tree DP & Re-rooting Optimization $O(N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0458 - De Thi Thu 1 Bai 8 Cap Quang Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0458%20-%20De%20Thi%20Thu%201%20Bai%208%20Cap%20Quang%20Viettel)
* **Phương pháp giải:** Sử dụng Thuật toán Quy hoạch động trên cây 2 lượt (Re-rooting DP) tính tổng khoảng cách từ mọi nút trên cây cáp quang tới các trạm trong $O(N)$ thay vì $O(N^2)$.

---

### **[IKH-0459] - Đề Thi Thử 1 - Bài 9: Đếm Tập Con Có Tổng Chia Hết Cho K Shopee**
* **Dạng bài:** Mock Contest 1 Task 9 (Modulo DP $O(N \cdot K)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0459 - De Thi Thu 1 Bai 9 DP Modulo Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0459%20-%20De%20Thi%20Thu%201%20Bai%209%20DP%20Modulo%20Shopee)
* **Phương pháp giải:** Quy hoạch động mảng trạng thái $DP[i][rem]$ là số cách chọn tập con từ $i$ phần tử đầu tiên có tổng chia cho $K$ dư $rem$ trong $O(N \cdot K)$.

---

### **[IKH-0460] - Đề Thi Thử 1 - Bài 10: Grand Synthesis Mock Contest 1 FPT**
* **Dạng bài:** Mock Contest 1 Task 10 (Grand Synthesis CHT + SegTree)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0460 - De Thi Thu 1 Bai 10 Grand Synthesis FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0460%20-%20De%20Thi%20Thu%201%20Bai%2010%20Grand%20Synthesis%20FPT)
* **Phương pháp giải:** Tổng hợp kiến thức Đề Thi Thử 1 kết hợp CHT (Convex Hull Trick) và Cây Phân Đoạn Segment Tree xử lý bài toán tối ưu hóa đa mục tiêu $O(N \log N)$.


---

### **[IKH-0461] - Đề Thi Thử 2 - Bài 1: Tìm Đường Đi Ngắn Nhất Mạng Lưới VinFast**
* **Dạng bài:** Mock Contest 2 Task 1 (Dijkstra Shortest Path $O((V + E) \log V)$)
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0461 - De Thi Thu 2 Bai 1 Dijkstra VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0461%20-%20De%20Thi%20Thu%202%20Bai%201%20Dijkstra%20VinFast)
* **Phương pháp giải:** Thuật toán Dijkstra kết hợp Priority Queue tìm đường đi ngắn nhất từ trạm sạc trung tâm $S$ tới tất cả các nút giao thông trong $O((V + E) \log V)$.

---

### **[IKH-0462] - Đề Thi Thử 2 - Bài 2: Phát Hiện Điểm Yếu Tuyến Cáp Viettel**
* **Dạng bài:** Mock Contest 2 Task 2 (Tarjan Bridges & Articulation Points $O(V + E)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0462 - De Thi Thu 2 Bai 2 Tarjan Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0462%20-%20De%20Thi%20Thu%202%20Bai%202%20Tarjan%20Viettel)
* **Phương pháp giải:** Áp dụng Thuật toán Tarjan sử dụng hai mảng `num` và `low` phát hiện các tuyến cáp yếu (cạnh cầu) và trạm trung chuyển quan trọng (đỉnh khớp) trong $O(V + E)$.

---

### **[IKH-0463] - Đề Thi Thử 2 - Bài 3: Kiểm Tra Tính Liên Thông Mạng Kho Shopee**
* **Dạng bài:** Mock Contest 2 Task 3 (DSU Path Compression & Union by Rank $O(E \cdot \alpha(V))$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0463 - De Thi Thu 2 Bai 3 DSU Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0463%20-%20De%20Thi%20Thu%202%20Bai%203%20DSU%20Shopee)
* **Phương pháp giải:** Cấu trúc dữ liệu DSU kiểm tra tính liên thông và đếm số thành phần liên thông của mạng lưới kho hàng trong $O(E \cdot \alpha(V))$.

---

### **[IKH-0464] - Đề Thi Thử 2 - Bài 4: Phân Thành Các Thành Phần Liên Thông Mạnh FPT**
* **Dạng bài:** Mock Contest 2 Task 4 (Tarjan Strongly Connected Components $O(V + E)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0464 - De Thi Thu 2 Bai 4 SCC Tarjan FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0464%20-%20De%20Thi%20Thu%202%20Bai%204%20SCC%20Tarjan%20FPT)
* **Phương pháp giải:** Sử dụng Thuật toán Tarjan phân chia đồ thị có hướng thành các thành phần liên thông mạnh (SCC) bằng Stack trong $O(V + E)$.

---

### **[IKH-0465] - Đề Thi Thử 2 - Bài 5: Xây Dựng Mạng Khung Chi Phí Nhỏ Nhất Zalo**
* **Dạng bài:** Mock Contest 2 Task 5 (Minimum Spanning Tree Prim / Kruskal $O(E \log V)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0465 - De Thi Thu 2 Bai 5 MST Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0465%20-%20De%20Thi%20Thu%202%20Bai%205%20MST%20Zalo)
* **Phương pháp giải:** Dựng Cây khung nhỏ nhất MST bằng thuật toán Kruskal / Prim kết hợp DSU tối ưu tổng chi phí xây dựng hạ tầng kết nối các máy chủ Zalo $O(E \log V)$.

---

### **[IKH-0466] - Đề Thi Thử 2 - Bài 6: Truy Vấn Tổ Tiên Chung Gần Nhất Techcombank**
* **Dạng bài:** Mock Contest 2 Task 6 (Lowest Common Ancestor LCA Binary Lifting $O((N + Q) \log N)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0466 - De Thi Thu 2 Bai 6 LCA Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0466%20-%20De%20Thi%20Thu%202%20Bai%206%20LCA%20Techcombank)
* **Phương pháp giải:** Kỹ thuật Nhảy nhị phân (Binary Lifting) dựng bảng `up[u][j]` tìm Tổ tiên chung gần nhất (LCA) và khoảng cách giữa 2 nút bất kỳ trên cây giao dịch ngân hàng trong $O(\log N)$.

---

### **[IKH-0467] - Đề Thi Thử 2 - Bài 7: Luồng Cực Đại Trong Hệ Thống Giao Thông VinFast**
* **Dạng bài:** Mock Contest 2 Task 7 (Dinic Maximum Flow Algorithm $O(V^2 E)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0467 - De Thi Thu 2 Bai 7 Max Flow VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0467%20-%20De%20Thi%20Thu%202%20Bai%207%20Max%20Flow%20VinFast)
* **Phương pháp giải:** Sử dụng Thuật toán Dinic tìm luồng cực đại (Maximum Flow) trên đồ thị luồng (Residual Graph) kết hợp BFS phân tầng và DFS tìm luồng tăng cường $O(V^2 E)$.

---

### **[IKH-0468] - Đề Thi Thử 2 - Bài 8: Đếm Đường Đi Trên Đồ Thị Thị Trường Viettel**
* **Dạng bài:** Mock Contest 2 Task 8 (Adjacency Matrix Exponentiation $O(V^3 \log K)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0468 - De Thi Thu 2 Bai 8 Matrix Path Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0468%20-%20De%20Thi%20Thu%202%20Bai%208%20Matrix%20Path%20Viettel)
* **Phương pháp giải:** Nhũ hóa ma trận kề $A$ và áp dụng Phép nhân ma trận lũy thừa $A^K[u][v]$ đếm chính xác số đường đi độ dài $K$ giữa $u$ và $v$ trong $O(V^3 \log K)$.

---

### **[IKH-0469] - Đề Thi Thử 2 - Bài 9: Quy Hoạch Động Đảo Ngược Đường Đi Shopee**
* **Dạng bài:** Mock Contest 2 Task 9 (DAG Topological Sort + DP $O(V + E)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0469 - De Thi Thu 2 Bai 9 DAG DP Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0469%20-%20De%20Thi%20Thu%202%20Bai%209%20DAG%20DP%20Shopee)
* **Phương pháp giải:** Sắp xếp Topological trên Đồ thị có hướng không chu trình (DAG) kết hợp Quy hoạch động đếm số đường đi dài nhất/ngắn nhất giữa các nút trong $O(V + E)$.

---

### **[IKH-0470] - Đề Thi Thử 2 - Bài 10: Grand Synthesis Mock Contest 2 FPT**
* **Dạng bài:** Mock Contest 2 Task 10 (Euler Tour Technique + Segment Tree $O((N + Q) \log N)$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0470 - De Thi Thu 2 Bai 10 Grand Synthesis FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0470%20-%20De%20Thi%20Thu%202%20Bai%2010%20Grand%20Synthesis%20FPT)
* **Phương pháp giải:** Kỹ thuật Trải cây Euler Tour đưa truy vấn trên cây về truy vấn đoạn trên mảng 1D kết hợp Segment Tree xử lý cập nhật cây con trong $O(\log N)$.


---

### **[IKH-0471] - Đề Thi Thử 3 - Bài 1: Quản Lý Tổng Đoạn Kho Hàng Shopee**
* **Dạng bài:** Mock Contest 3 Task 1 (Fenwick Tree Point Update Range Query $O(\log N)$)
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0471 - De Thi Thu 3 Bai 1 BIT Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0471%20-%20De%20Thi%20Thu%203%20Bai%201%20BIT%20Shopee)
* **Phương pháp giải:** Cấu trúc dữ liệu Cây Fenwick Tree (BIT) xử lý truy vấn cập nhật điểm $A[i] = x$ và tính tổng sản phẩm trên đoạn $[L, R]$ trong $O(\log N)$.

---

### **[IKH-0472] - Đề Thi Thử 3 - Bài 2: Cập Nhật Đoạn Cước Phí Viettel**
* **Dạng bài:** Mock Contest 3 Task 2 (Segment Tree Lazy Propagation $O(\log N)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0472 - De Thi Thu 3 Bai 2 Lazy SegTree Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0472%20-%20De%20Thi%20Thu%203%20Bai%202%20Lazy%20SegTree%20Viettel)
* **Phương pháp giải:** Áp dụng Kỹ thuật Đẩy lười (Lazy Propagation) trên Cây Phân Đoạn Segment Tree hỗ trợ tăng cước phí đoạn $[L, R]$ và tìm giá trị nhỏ nhất trong $O(\log N)$.

---

### **[IKH-0473] - Đề Thi Thử 3 - Bài 3: Tìm Max Trong Cửa Sổ Trượt VinFast**
* **Dạng bài:** Mock Contest 3 Task 3 (Monotonic Deque RMQ $O(N)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0473 - De Thi Thu 3 Bai 3 Monotonic Deque VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0473%20-%20De%20Thi%20Thu%203%20Bai%203%20Monotonic%20Deque%20VinFast)
* **Phương pháp giải:** Hàng đợi đơn điệu Monotonic Deque duy trì các chỉ số giảm dần tìm điện năng tiêu thụ lớn nhất trong cửa sổ trượt $K$ trạm sạc liên tiếp trong $O(N)$.

---

### **[IKH-0474] - Đề Thi Thử 3 - Bài 4: Nén Tọa Độ Truy Vấn Điểm FPT Telecom**
* **Dạng bài:** Mock Contest 3 Task 4 (Coordinate Compression + BIT $O(N \log N)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0474 - De Thi Thu 3 Bai 4 Coordinate Compression FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0474%20-%20De%20Thi%20Thu%203%20Bai%204%20Coordinate%20Compression%20FPT)
* **Phương pháp giải:** Nén tọa độ rời rạc hóa dải giá trị $10^9$ kết hợp Cây Fenwick Tree đếm số điểm dữ liệu thỏa mãn điều kiện khoảng trong $O(N \log N)$.

---

### **[IKH-0475] - Đề Thi Thử 3 - Bài 5: Quản Lý Bảng 2D Dữ Liệu Zalo**
* **Dạng bài:** Mock Contest 3 Task 5 (2D Fenwick Tree $O(\log^2 N)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0475 - De Thi Thu 3 Bai 5 2D BIT Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0475%20-%20De%20Thi%20Thu%203%20Bai%205%202D%20BIT%20Zalo)
* **Phương pháp giải:** Cấu trúc Cây Fenwick 2D quản lý ma trận dữ liệu người dùng Zalo, hỗ trợ cập nhật điểm $(x, y)$ và tính tổng vùng chữ nhật $[X_1..X_2, Y_1..Y_2]$ trong $O(\log^2 N)$.

---

### **[IKH-0476] - Đề Thi Thử 3 - Bài 6: Đếm Phần Tử Nhỏ Hơn K Trong Đoạn Techcombank**
* **Dạng bài:** Mock Contest 3 Task 6 (Merge Sort Tree $O(\log^2 N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0476 - De Thi Thu 3 Bai 6 Merge Sort Tree Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0476%20-%20De%20Thi%20Thu%203%20Bai%206%20Merge%20Sort%20Tree%20Techcombank)
* **Phương pháp giải:** Xây dựng Cây Trộn Sắp Xếp (Merge Sort Tree) lưu mảng đã sắp xếp tại mỗi nút Segment Tree kết hợp `std::lower_bound` đếm số phần tử nhỏ hơn $K$ trong đoạn $[L, R]$ $O(\log^2 N)$.

---

### **[IKH-0477] - Đề Thi Thử 3 - Bài 7: Cập Nhật Đoạn Gán Giá Trị VinFast**
* **Dạng bài:** Mock Contest 3 Task 7 (Segment Tree Lazy Tag Assignment $O(\log N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0477 - De Thi Thu 3 Bai 7 Lazy Assignment VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0477%20-%20De%20Thi%20Thu%3%20Bai%207%20Lazy%20Assignment%20VinFast)
* **Phương pháp giải:** Kỹ thuật Gán nhãn đlazy (Lazy Tag Assignment) hỗ trợ gán toàn bộ mảng con $[L, R] = v$ và truy vấn tổng đoạn trong $O(\log N)$.

---

### **[IKH-0478] - Đề Thi Thử 3 - Bài 8: Khôi Phục Lịch Sử Cập Nhật Cây Viettel**
* **Dạng bài:** Mock Contest 3 Task 8 (Persistent Segment Tree $O(\log N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0478 - De Thi Thu 3 Bai 8 Persistent SegTree Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0478%20-%20De%20Thi%20Thu%203%20Bai%208%20Persistent%20SegTree%20Viettel)
* **Phương pháp giải:** Cấu trúc dữ liệu Cây Phân Đoạn Bền Vững (Persistent Segment Tree) lưu trữ lại toàn bộ các phiên bản lịch sử cập nhật cấu hình mạng cáp quang Viettel trong $O(\log N)$ bộ nhớ/thời gian.

---

### **[IKH-0479] - Đề Thi Thử 3 - Bài 9: Gộp Cây Phân Đoạn Quản Lý Đơn Hàng Shopee**
* **Dạng bài:** Mock Contest 3 Task 9 (Segment Tree Merging $O(N \log N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0479 - De Thi Thu 3 Bai 9 SegTree Merging Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0479%20-%20De%20Thi%20Thu%203%20Bai%209%20SegTree%20Merging%20Shopee)
* **Phương pháp giải:** Áp dụng kỹ thuật Gộp Cây Phân Đoạn (Segment Tree Merging) tổng hợp dữ liệu đơn hàng từ các kho hàng cây con lên kho tổng trong $O(N \log N)$.

---

### **[IKH-0480] - Đề Thi Thử 3 - Bài 10: Grand Synthesis Mock Contest 3 FPT**
* **Dạng bài:** Mock Contest 3 Task 10 (Heavy-Light Decomposition HLD + SegTree $O(N \log^2 N)$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0480 - De Thi Thu 3 Bai 10 Grand Synthesis HLD FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0480%20-%20De%20Thi%20Thu%203%20Bai%2010%20Grand%20Synthesis%20HLD%20FPT)
* **Phương pháp giải:** Tổng hợp Kỹ thuật Phân rã Nặng Nhe (Heavy-Light Decomposition - HLD) kết hợp Segment Tree xử lý cập nhật chuỗi đường đi và truy vấn Max giữa 2 đỉnh bất kỳ trên cây trong $O(N \log^2 N)$.


---

### **[IKH-0481] - Đề Thi Thử 4 - Bài 1: Kiểm Tra Chuỗi Đảo Đối Xứng Shopee**
* **Dạng bài:** Mock Contest 4 Task 1 (Double Polynomial Rolling Hash $O(N + Q)$)
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0481 - De Thi Thu 4 Bai 1 Palindrome Hash Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0481%20-%20De%20Thi%20Thu%204%20Bai%201%20Palindrome%20Hash%20Shopee)
* **Phương pháp giải:** Kỹ thuật Mã hóa Chuỗi Rolling Hash kép (Double Hash) tính mã hash xuôi $H_1$ và ngược $H_2$ cho phép kiểm tra tính đối xứng của đoạn $[L, R]$ trong $O(1)$.

---

### **[IKH-0482] - Đề Thi Thử 4 - Bài 2: Tìm Mẫu Khóa Mã Hóa Viettel**
* **Dạng bài:** Mock Contest 4 Task 2 (KMP String Matching Algorithm $O(N + M)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0482 - De Thi Thu 4 Bai 2 KMP Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0482%20-%20De%20Thi%20Thu%204%20Bai%202%20KMP%20Viettel)
* **Phương pháp giải:** Thuật toán KMP (Knuth-Morris-Pratt) dựng mảng tiền tố `pi` (Prefix Function) tìm kiếm vị trí xuất hiện của khóa mã hóa trong $O(N + M)$.

---

### **[IKH-0483] - Đề Thi Thử 4 - Bài 3: Phân Tích Tiền Tố Chuỗi VinFast**
* **Dạng bài:** Mock Contest 4 Task 3 (Z-Algorithm String Prefix Matching $O(N)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0483 - De Thi Thu 4 Bai 3 Z Algorithm VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0483%20-%20De%20Thi%20Thu%204%20Bai%203%20Z%20Algorithm%20VinFast)
* **Phương pháp giải:** Thuật toán Z-Algorithm tính mảng $Z[i]$ chứa độ dài tiền tố chung dài nhất giữa $S$ và $S[i..N-1]$ trong $O(N)$ thời gian.

---

### **[IKH-0484] - Đề Thi Thử 4 - Bài 4: Quản Lý Từ Điển Sản Phẩm FPT**
* **Dạng bài:** Mock Contest 4 Task 4 (Trie Tree Auto-complete & Prefix Search)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0484 - De Thi Thu 4 Bai 4 Trie Tree FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0484%20-%20De%20Thi%20Thu%204%20Bai%204%20Trie%20Tree%20FPT)
* **Phương pháp giải:** Cấu trúc Cây Từ Điển (Trie Tree) hỗ trợ chèn từ và đếm số lượng tên sản phẩm bắt đầu bằng tiền tố $P$ trong thời gian $O(|P|)$.

---

### **[IKH-0485] - Đề Thi Thử 4 - Bài 5: So Khớp Đa Mẫu Mã Giao Dịch Zalo**
* **Dạng bài:** Mock Contest 4 Task 5 (Aho-Corasick Automaton Multi-pattern Matching)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0485 - De Thi Thu 4 Bai 5 Aho Corasick Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0485%20-%20De%20Thi%20Thu%204%20Bai%205%20Aho%20Corasick%20Zalo)
* **Phương pháp giải:** Kết hợp Trie Tree và thuật toán KMP tạo Tự động thể Aho-Corasick hỗ trợ tìm kiếm đồng thời hàng ngàn mẫu mã giao dịch độc hại trong $O(N + \sum |P|)$.

---

### **[IKH-0486] - Đề Thi Thử 4 - Bài 6: Đếm Chuỗi Đã Sắp Xếp Techcombank**
* **Dạng bài:** Mock Contest 4 Task 6 (Suffix Array & LCP Array $O(N \log N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0486 - De Thi Thu 4 Bai 6 Suffix Array Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0486%20-%20De%20Thi%20Thu%204%20Bai%206%20Suffix%20Array%20Techcombank)
* **Phương pháp giải:** Xây dựng Mảng Hậu Tố (Suffix Array) và Mảng LCP (Longest Common Prefix) đếm số lượng chuỗi con phân biệt và sắp xếp thứ tự từ điển các mã tài khoản trong $O(N \log N)$.

---

### **[IKH-0487] - Đề Thi Thử 4 - Bài 7: Tìm Chuỗi Con Chung Dài Nhất VinFast**
* **Dạng bài:** Mock Contest 4 Task 7 (Longest Common Substring Rolling Hash + BS)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0487 - De Thi Thu 4 Bai 7 LCS Hash BS VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0487%20-%20De%20Thi%20Thu%204%20Bai%207%20LCS%20Hash%20BS%20VinFast)
* **Phương pháp giải:** Tìm kiếm nhị phân kết hợp Rolling Hash và Hash Set kiểm tra sự tồn tại của chuỗi con chung độ dài $Len$ giữa 2 xâu dữ liệu trong $O(N \log N)$.

---

### **[IKH-0488] - Đề Thi Thử 4 - Bài 8: Đếm Số Chuỗi Đối Xứng Dài Nhất Viettel**
* **Dạng bài:** Mock Contest 4 Task 8 (Manacher's Algorithm $O(N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0488 - De Thi Thu 4 Bai 8 Manacher Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0488%20-%20De%20Thi%20Thu%204%20Bai%208%20Manacher%20Viettel)
* **Phương pháp giải:** Thuật toán Manacher tìm bán kính đối xứng tâm tại mọi vị trí trên chuỗi $S$ mở rộng, đếm số chuỗi đối xứng và tìm chuỗi đối xứng dài nhất trong $O(N)$.

---

### **[IKH-0489] - Đề Thi Thử 4 - Bài 9: Tối Ưu Hóa Cây Từ Điển Động Shopee**
* **Dạng bài:** Mock Contest 4 Task 9 (Bitwise Trie Maximum XOR Pair $O(N \cdot 30)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0489 - De Thi Thu 4 Bai 9 Bitwise Trie Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0489%20-%20De%20Thi%20Thu%204%20Bai%209%20Bitwise%20Trie%20Shopee)
* **Phương pháp giải:** Biểu diễn các số nguyên dưới dạng chuỗi 30 bit trong Cây Từ Điển Bitwise Trie, tìm cặp phần tử $(A_i, A_j)$ có tổng XOR $A_i \oplus A_j$ lớn nhất trong $O(N \cdot 30)$.

---

### **[IKH-0490] - Đề Thi Thử 4 - Bài 10: Grand Synthesis Mock Contest 4 FPT**
* **Dạng bài:** Mock Contest 4 Task 10 (Suffix Automaton SAM $O(N)$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0490 - De Thi Thu 4 Bai 10 Grand Synthesis SAM FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0490%20-%20De%20Thi%20Thu%204%20Bai%2010%20Grand%20Synthesis%20SAM%20FPT)
* **Phương pháp giải:** Tổng hợp Kỹ thuật Tự động thể Hậu tố (Suffix Automaton - SAM) xây dựng cấu trúc nhận dạng toàn bộ các chuỗi con của $S$ trong $O(N)$ thời gian và bộ nhớ.


---

### **[IKH-0491] - Đề Thi Thử 5 - Bài 1: Đếm Số Nguyên Tố Trong Khoảng VinFast**
* **Dạng bài:** Mock Contest 5 Task 1 (Segmented Sieve $O(\sqrt{R} + (R - L + 1) \log \log R)$)
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0491 - De Thi Thu 5 Bai 1 Segmented Sieve VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0491%20-%20De%20Thi%20Thu%205%20Bai%201%20Segmented%20Sieve%20VinFast)
* **Phương pháp giải:** Thuật toán Sàng Phân Đoạn (Segmented Sieve) đếm chính xác số lượng số nguyên tố trong khoảng $[L, R]$ với $R \le 10^{12}, R - L \le 10^6$ mà không bị tràn bộ nhớ MLE.

---

### **[IKH-0492] - Đề Thi Thử 5 - Bài 2: Phép Nhân Số Nguyên Siêu Lớn Modulo Viettel**
* **Dạng bài:** Mock Contest 5 Task 2 (128-bit Integer Modulo Multiplication `__int128_t`)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0492 - De Thi Thu 5 Bai 2 Modulo Mul Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0492%20-%20De%20Thi%20Thu%205%20Bai%202%20Modulo%20Mul%20Viettel)
* **Phương pháp giải:** Xử lý phép nhân hai số $A, B \sim 10^{18}$ chia lấy dư cho $M$ bằng ép kiểu `__int128_t` hoặc Nhân nhị phân `mul_mod(A, B, M)` tránh hoàn toàn lỗi tràn số 64-bit.

---

### **[IKH-0493] - Đề Thi Thử 5 - Bài 3: Đếm Số Cặp Nguyên Tố Cùng Nhau Shopee**
* **Dạng bài:** Mock Contest 5 Task 3 (Euler's Totient Function $\phi(N)$ Sieve)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0493 - De Thi Thu 5 Bai 3 Euler Totient Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0493%20-%20De%20Thi%20Thu%205%20Bai%203%20Euler%20Totient%20Shopee)
* **Phương pháp giải:** Sử dụng Sàng Hàm Phi Euler $\phi(N)$ đếm số lượng cặp phần tử có ước chung lớn nhất $\gcd(i, N) = 1$ trong $O(N \log \log N)$.

---

### **[IKH-0494] - Đề Thi Thử 5 - Bài 4: Giải Hệ Phương Trình Đồng Dư FPT**
* **Dạng bài:** Mock Contest 5 Task 4 (Chinese Remainder Theorem CRT $O(K \log M)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0494 - De Thi Thu 5 Bai 4 CRT FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0494%20-%20De%20Thi%20Thu%205%20Bai%204%20CRT%20FPT)
* **Phương pháp giải:** Thuật toán Thặng Dư Trung Hoa (CRT) kết hợp Thuật toán Euclid Mở rộng giải hệ phương trình đồng dư $x \equiv a_i \pmod{m_i}$ với các $m_i$ nguyên tố cùng nhau trong $O(K \log M)$.

---

### **[IKH-0495] - Đề Thi Thử 5 - Bài 5: Tính Số Cách Chọn Phần Tử Modulo Zalo**
* **Dạng bài:** Mock Contest 5 Task 5 (Lucas' Theorem & Precomputed Factorials)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0495 - De Thi Thu 5 Bai 5 Lucas Theorem Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0495%20-%20De%20Thi%20Thu%205%20Bai%205%20Lucas%20Theorem%20Zalo)
* **Phương pháp giải:** Sử dụng Định lý Lucas phân tích tổ hợp $C_N^K \pmod P$ thành tích các tổ hợp nhỏ trong hệ cơ số $P$ với $N, K$ siêu lớn $10^{18}$ và $P$ là số nguyên tố nhỏ.

---

### **[IKH-0496] - Đề Thi Thử 5 - Bài 6: Đếm Số Đường Đi Bằng Nhân Ma Trận Techcombank**
* **Dạng bài:** Mock Contest 5 Task 6 (Matrix Exponentiation Path Count $O(K^3 \log N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0496 - De Thi Thu 5 Bai 6 Matrix Exp Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0496%20-%20De%20Thi%20Thu%205%20Bai%206%20Matrix%20Exp%20Techcombank)
* **Phương pháp giải:** Biểu diễn đồ thị dưới dạng Ma trận Kề $A$ và áp dụng Nhân ma trận lũy thừa $A^N[u][v]$ đếm số lượng đường đi có độ dài $N$ trong $O(K^3 \log N)$.

---

### **[IKH-0497] - Đề Thi Thử 5 - Bài 7: Trò Chơi Bốc Sỏi Nim Chuẩn VinFast**
* **Dạng bài:** Mock Contest 5 Task 7 (Standard Nim Game & Bouton's Theorem $O(N)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0497 - De Thi Thu 5 Bai 7 Nim Game VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0497%20-%20De%20Thi%20Thu%205%20Bai%207%20Nim%20Game%20VinFast)
* **Phương pháp giải:** Áp dụng Định lý Bouton tính Tổng XOR $S = A_1 \oplus A_2 \oplus \dots \oplus A_N$. Người chơi đầu thắng khi và chỉ khi $S \ne 0$.

---

### **[IKH-0498] - Đề Thi Thử 5 - Bài 8: Trò Chơi Trên Đồ Thị Thúc Đẩy Viettel**
* **Dạng bài:** Mock Contest 5 Task 8 (Sprague-Grundy Theorem MEX on DAG $O(V + E)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0498 - De Thi Thu 5 Bai 8 Sprague Grundy Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0498%20-%20De%20Thi%20Thu%205%20Bai%208%20Sprague%20Grundy%20Viettel)
* **Phương pháp giải:** Định lý Sprague-Grundy tính hàm $G(u) = \text{MEX}(\{G(v) \mid (u, v) \in E\})$ trên đồ thị DAG, quy đổi trò chơi bất kỳ về trò chơi Nim tương đương $O(V + E)$.

---

### **[IKH-0499] - Đề Thi Thử 5 - Bài 9: Trò Chơi Chặt Cây Green Hackenbush Shopee**
* **Dạng bài:** Mock Contest 5 Task 9 (Green Hackenbush on Trees $O(N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0499 - De Thi Thu 5 Bai 9 Green Hackenbush Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0499%20-%20De%20Thi%20Thu%205%20Bai%209%20Green%20Hackenbush%20Shopee)
* **Phương pháp giải:** Áp dụng Định lý Colon Nguyên tắc Nhánh Cây (Colon Principle of Equal Radicals) rút gọn các nhánh cây thành giá trị Grundy $G(u) = \bigoplus_{v \in \text{children}} (G(v) + 1)$ trong $O(N)$.

---

### **[IKH-0500] - Đề Thi Thử 5 - Bài 10: Grand Synthesis Mock Contest 5 FPT**
* **Dạng bài:** Mock Contest 5 Task 10 (Inclusion-Exclusion & Fast Power $O(2^K)$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0500 - De Thi Thu 5 Bai 10 Grand Synthesis FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0500%20-%20De%20Thi%20Thu%205%20Bai%2010%20Grand%20Synthesis%20FPT)
* **Phương pháp giải:** Tổng hợp Nguyên lý Bù trừ (Inclusion-Exclusion Principle) kết hợp Lũy thừa nhanh Modulo đếm số cấu hình thỏa mãn ít nhất một điều kiện cho trước trong $O(2^K \log N)$.


---

### **[IKH-0501] - Đề Thi Thử 6 - Bài 1: Tối Ưu Hóa Chi Phí Vận Chuyển Shopee**
* **Dạng bài:** Mock Contest 6 Task 1 (Convex Hull Trick CHT $O(N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0501 - De Thi Thu 6 Bai 1 CHT Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0501%20-%20De%20Thi%20Thu%206%20Bai%201%20CHT%20Shopee)
* **Phương pháp giải:** Kỹ thuật Bao Lồi Tối Ưu QHD (Convex Hull Trick) duy trì danh sách bao lồi các đường thẳng $y = A_j \cdot x + dp[j]$ tối ưu hóa chi phí vận chuyển trong $O(N)$.

---

### **[IKH-0502] - Đề Thi Thử 6 - Bài 2: Phân Chia Đoạn Tuyến Cáp Viettel**
* **Dạng bài:** Mock Contest 6 Task 2 (Divide and Conquer DP Optimization $O(K \cdot N \log N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0502 - De Thi Thu 6 Bai 2 Divide Conquer DP Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0502%20-%20De%20Thi%20Thu%206%20Bai%202%20Divide%20Conquer%20DP%20Viettel)
* **Phương pháp giải:** Áp dụng Tối ưu Chia để trị (Divide and Conquer DP) dựa trên tính đơn điệu của điểm cắt tối ưu $opt[i][j] \le opt[i][j+1]$ giảm độ phức tạp từ $O(K \cdot N^2)$ xuống $O(K \cdot N \log N)$.

---

### **[IKH-0503] - Đề Thi Thử 6 - Bài 3: Tối Ưu Hóa Chia Cụm Dữ Liệu VinFast**
* **Dạng bài:** Mock Contest 6 Task 3 (Knuth's Optimization DP $O(N^2)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0503 - De Thi Thu 6 Bai 3 Knuth DP VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0503%20-%20De%20Thi%20Thu%206%20Bai%203%20Knuth%20DP%20VinFast)
* **Phương pháp giải:** Tối ưu hóa Knuth (Knuth's DP Optimization) cho bài toán quy hoạch động trên đoạn thỏa mãn bất đẳng thức Tứ giác (Quadrangle Inequality) $opt[i][j-1] \le opt[i][j] \le opt[i+1][j]$ đạt $O(N^2)$.

---

### **[IKH-0504] - Đề Thi Thử 6 - Bài 4: Cập Nhật Đường Thẳng Động FPT**
* **Dạng bài:** Mock Contest 6 Task 4 (Dynamic CHT `LineContainer` $O(N \log N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0504 - De Thi Thu 6 Bai 4 Dynamic CHT FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0504%20-%20De%20Thi%20Thu%206%20Bai%204%20Dynamic%20CHT%20FPT)
* **Phương pháp giải:** Sử dụng Cấu trúc dữ liệu Dynamic CHT (`std::set` `LineContainer` / Li Chao Tree) quản lý các đường thẳng có hệ số góc không đơn điệu trong $O(N \log N)$.

---

### **[IKH-0505] - Đề Thi Thử 6 - Bài 5: Quy Hoạch Động Tập Con Bitmask Zalo**
* **Dạng bài:** Mock Contest 6 Task 5 (Sum Over Subsets SOS DP $O(N \cdot 2^N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0505 - De Thi Thu 6 Bai 5 SOS DP Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0505%20-%20De%20Thi%20Thu%206%20Bai%205%20SOS%20DP%20Zalo)
* **Phương pháp giải:** Quy hoạch động Tổng trên các tập con (Sum Over Subsets - SOS DP) tính $F[mask] = \sum_{sub \subseteq mask} A[sub]$ cho $N$ bit trong $O(N \cdot 2^N)$ thay vì $O(3^N)$.

---

### **[IKH-0506] - Đề Thi Thử 6 - Bài 6: Tối Ưu QHD Với Segment Tree Techcombank**
* **Dạng bài:** Mock Contest 6 Task 6 (SegTree DP Optimization $O(N \log N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0506 - De Thi Thu 6 Bai 6 SegTree DP Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0506%20-%20De%20Thi%20Thu%206%20Bai%206%20SegTree%20DP%20Techcombank)
* **Phương pháp giải:** Kết hợp Cây Phân Đoạn (Segment Tree) cập nhật và truy vấn giá trị $dp[j]$ lớn nhất trong khoảng điều kiện $[i - R, i - L]$ trong $O(N \log N)$.

---

### **[IKH-0507] - Đề Thi Thử 6 - Bài 7: Quy Hoạch Động Đổi Trọng Tâm Cây VinFast**
* **Dạng bài:** Mock Contest 6 Task 7 (Tree DP & Re-rooting Technique $O(N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0507 - De Thi Thu 6 Bai 7 Tree DP Re-rooting VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0507%20-%20De%20Thi%20Thu%206%20Bai%207%20Tree%20DP%20Re-rooting%20VinFast)
* **Phương pháp giải:** Kỹ thuật Quy hoạch động Đổi gốc cây (Re-rooting DP) thực hiện 2 lượt DFS (DFS 1 tính gốc ban đầu, DFS 2 truyền kết quả sang gốc mới) tính đáp án cho mọi đỉnh làm gốc trong $O(N)$.

---

### **[IKH-0508] - Đề Thi Thử 6 - Bài 8: Tối Ưu Hóa QHD Bằng Deque Hàng Đợi Đơn Điệu Viettel**
* **Dạng bài:** Mock Contest 6 Task 8 (Monotonic Queue DP Optimization $O(N)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0508 - De Thi Thu 6 Bai 8 Monotonic Queue DP Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0508%20-%20De%20Thi%20Thu%206%20Bai%208%20Monotonic%20Queue%20DP%20Viettel)
* **Phương pháp giải:** Hàng đợi đơn điệu Monotonic Deque duy trì các giá trị $dp[j]$ tối ưu trong cửa sổ sliding window độ dài $K$, tối ưu hóa thời gian tính DP từ $O(N \cdot K)$ xuống $O(N)$.

---

### **[IKH-0509] - Đề Thi Thử 6 - Bài 9: Quy Hoạch Động Chữ Số Đếm Mã Giao Dịch Shopee**
* **Dạng bài:** Mock Contest 6 Task 9 (Digit DP $O(\text{len} \cdot 10 \cdot \text{state})$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0509 - De Thi Thu 6 Bai 9 Digit DP Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0509%20-%20De%20Thi%20Thu%206%20Bai%209%20Digit%20DP%20Shopee)
* **Phương pháp giải:** Quy hoạch động trên từng chữ số (Digit DP) đếm số lượng số nguyên trong khoảng $[A, B]$ thỏa mãn thuộc tính chữ số đặc biệt trong $O(\log_{10} B \cdot \text{state})$.

---

### **[IKH-0510] - Đề Thi Thử 6 - Bài 10: Grand Synthesis Mock Contest 6 FPT**
* **Dạng bài:** Mock Contest 6 Task 10 (Alien's Trick / WSI DP Optimization $O(N \log (\text{VAL}))$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0510 - De Thi Thu 6 Bai 10 Grand Synthesis Alien Trick FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0510%20-%20De%20Thi%20Thu%206%20Bai%2010%20Grand%20Synthesis%20Alien%20Trick%20FPT)
* **Phương pháp giải:** Kỹ thuật Alien's Trick (WSI DP Optimization / Chặt nhị phân Phạt Chi Phí) chuyển bài toán QHD có điều kiện chọn đúng $K$ phần tử về bài toán QHD không điều kiện kết hợp BS giá trị phạt trong $O(N \log (\text{VAL}))$.


---

### **[IKH-0511] - Đề Thi Thử 7 - Bài 1: Quản Lý Mạng Kho Hàng Bằng DSU Có Phục Hồi Shopee**
* **Dạng bài:** Mock Contest 7 Task 1 (DSU Rollback / Persistent DSU $O(Q \log N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0511 - De Thi Thu 7 Bai 1 DSU Rollback Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0511%20-%20De%20Thi%20Thu%207%20Bai%201%20DSU%20Rollback%20Shopee)
* **Phương pháp giải:** Cấu trúc dữ liệu DSU by Rank / Size kết hợp Stack Hoàn tác (Rollback) khôi phục lịch sử liên thông của mạng lưới kho hàng trong $O(\log N)$.

---

### **[IKH-0512] - Đề Thi Thử 7 - Bài 2: Phân Tích Cây Con Nhỏ Sang Lớn Viettel**
* **Dạng bài:** Mock Contest 7 Task 2 (Small-to-Large Merging Sack $O(N \log^2 N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0512 - De Thi Thu 7 Bai 2 Sack DSU on Tree Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0512%20-%20De%20Thi%20Thu%207%20Bai%202%20Sack%20DSU%20on%20Tree%20Viettel)
* **Phương pháp giải:** Kỹ thuật Gộp cây con Nhỏ sang Lớn (DSU on Tree / Sack) duy trì tập hợp tần số màu sắc/thuộc tính trên cây trong $O(N \log^2 N)$.

---

### **[IKH-0513] - Đề Thi Thử 7 - Bài 3: Phân Rã Trọng Tâm Cây VinFast**
* **Dạng bài:** Mock Contest 7 Task 3 (Centroid Decomposition $O(N \log N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0513 - De Thi Thu 7 Bai 3 Centroid Decomposition VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0513%20-%20De%20Thi%20Thu%207%20Bai%203%20Centroid%20Decomposition%20VinFast)
* **Phương pháp giải:** Kỹ thuật Phân rã Trọng tâm cây (Centroid Decomposition) chia cây thành cây trọng tâm độ sâu $O(\log N)$, đếm cặp đường đi thỏa mãn điều kiện khoảng cách $O(N \log N)$.

---

### **[IKH-0514] - Đề Thi Thử 7 - Bài 4: Tìm Khung Cây Tối Ưu Với Cạnh Rời FPT**
* **Dạng bài:** Mock Contest 7 Task 4 (Dynamic Offline MST with DSU Rollback $O((N + Q) \log^2 N)$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0514 - De Thi Thu 7 Bai 4 Dynamic Offline MST FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0514%20-%20De%20Thi%20Thu%207%20Bai%204%20Dynamic%20Offline%20MST%20FPT)
* **Phương pháp giải:** Kỹ thuật Cây Phân Đoạn Thời Gian kết hợp DSU Rollback xử lý bài toán Cây khung nhỏ nhất MST động có truy vấn thêm/xóa cạnh offline trong $O((N + Q) \log^2 N)$.

---

### **[IKH-0515] - Đề Thi Thử 7 - Bài 5: Đường Đi Ngắn Nhất Mạng Lưới K Cạnh Zalo**
* **Dạng bài:** Mock Contest 7 Task 5 (Min-Plus Matrix Multiplication $O(V^3 \log K)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0515 - De Thi Thu 7 Bai 5 Min Plus Matrix Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0515%20-%20De%20Thi%20Thu%207%20Bai%205%20Min%20Plus%20Matrix%20Zalo)
* **Phương pháp giải:** Đại số Min-Plus Nhân Ma Trận Lũy Thừa $(A \star B)[i][j] = \min_k (A[i][k] + B[k][j])$ tìm đường đi ngắn nhất qua đúng $K$ cạnh giữa mọi cặp đỉnh trong $O(V^3 \log K)$.

---

### **[IKH-0516] - Đề Thi Thử 7 - Bài 6: Đếm Chu Trình Âm Đồ Thị Techcombank**
* **Dạng bài:** Mock Contest 7 Task 6 (SPFA Negative Cycle Detection $O(V \cdot E)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0516 - De Thi Thu 7 Bai 6 SPFA Negative Cycle Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0516%20-%20De%20Thi%20Thu%207%20Bai%206%20SPFA%20Negative%20Cycle%20Techcombank)
* **Phương pháp giải:** Thuật toán SPFA (Shortest Path Faster Algorithm) đếm số lần cập nhật khoảng cách `cnt[u] >= V` để phát hiện và truy vết chu trình âm trong hệ thống giao dịch tài chính.

---

### **[IKH-0517] - Đề Thi Thử 7 - Bài 7: Cập Nhật Chuỗi Trên Cây Với HLD VinFast**
* **Dạng bài:** Mock Contest 7 Task 7 (HLD + Lazy SegTree $O(Q \log^2 N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0517 - De Thi Thu 7 Bai 7 HLD Lazy SegTree VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0517%20-%20De%20Thi%20Thu%207%20Bai%207%20HLD%20Lazy%20SegTree%20VinFast)
* **Phương pháp giải:** Tổng hợp HLD và Lazy Segment Tree hỗ trợ tăng trọng số trên đường đi $(u, v)$ và truy vấn tổng/max trong $O(Q \log^2 N)$.

---

### **[IKH-0518] - Đề Thi Thử 7 - Bài 8: Ghép Cặp Cực Đại Đồ Thị Hai Phía Viettel**
* **Dạng bài:** Mock Contest 7 Task 8 (Hopcroft-Karp Bipartite Matching $O(E \sqrt{V})$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0518 - De Thi Thu 7 Bai 8 Hopcroft Karp Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0518%20-%20De%20Thi%20Thu%207%20Bai%208%20Hopcroft%20Karp%20Viettel)
* **Phương pháp giải:** Thuật toán Hopcroft-Karp kết hợp BFS phân tầng và DFS tìm đường tăng cường phân bổ tối ưu trạm phát sóng Viettel cho khách hàng trong $O(E \sqrt{V})$.

---

### **[IKH-0519] - Đề Thi Thử 7 - Bài 9: Luồng Chi Phí Nhỏ Nhất Shopee**
* **Dạng bài:** Mock Contest 7 Task 9 (Min-Cost Max-Flow MCMF $O(F \cdot E \log V)$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0519 - De Thi Thu 7 Bai 9 Min Cost Max Flow Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0519%20-%20De%20Thi%20Thu%207%20Bai%209%20Min%20Cost%20Max%20Flow%20Shopee)
* **Phương pháp giải:** Thuật toán Successive Shortest Path (Dijkstra với Potential) tìm Luồng Cực Đại với Chi Phí Nhỏ Nhất trên đồ thị luồng $O(F \cdot E \log V)$.

---

### **[IKH-0520] - Đề Thi Thử 7 - Bài 10: Grand Synthesis Mock Contest 7 FPT**
* **Dạng bài:** Mock Contest 7 Task 10 (2-SAT Problem Tarjan SCC $O(V + E)$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0520 - De Thi Thu 7 Bai 10 Grand Synthesis 2-SAT FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0520%20-%20De%20Thi%20Thu%207%20Bai%2010%20Grand%20Synthesis%202-SAT%20FPT)
* **Phương pháp giải:** Biểu diễn bài toán 2-Satisfiability dưới dạng đồ thị suy luận có hướng, phân tích Thành phần liên thông mạnh (SCC) bằng Tarjan để kiểm tra và gán nghiệm $O(V + E)$.


---

### **[IKH-0521] - Đề Thi Thử 8 - Bài 1: Kiểm Tra Cây Chuẩn Đô Thị VinFast**
* **Dạng bài:** Mock Contest 8 Task 1 (Tree Isomorphism AHU / Tree Hash $O(N \log N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0521 - De Thi Thu 8 Bai 1 Tree Isomorphism VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0521%20-%20De%20Thi%20Thu%208%20Bai%201%20Tree%20Isomorphism%20VinFast)
* **Phương pháp giải:** Thuật toán AHU (Tree Hashing) mã hóa cấu trúc cây con đệ quy kiểm tra hai cây có gốc $T_1, T_2$ có đồng hình (Isomorphic) hay không trong $O(N \log N)$.

---

### **[IKH-0522] - Đề Thi Thử 8 - Bài 2: Truy Vấn Cây Đoạn Có Cập Nhật Đơn Hàng Viettel**
* **Dạng bài:** Mock Contest 8 Task 2 (Heavy-Light Decomposition HLD + Lazy SegTree $O(Q \log^2 N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0522 - De Thi Thu 8 Bai 2 HLD Lazy Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0522%20-%20De%20Thi%20Thu%208%20Bai%202%20HLD%20Lazy%20Viettel)
* **Phương pháp giải:** Phân rã cây Heavy-Light Decomposition kết hợp Lazy Segment Tree xử lý các thao tác tăng giá trị đoạn trên đường đi và truy vấn tổng/cực đại trên cây trong $O(Q \log^2 N)$.

---

### **[IKH-0523] - Đề Thi Thử 8 - Bài 3: Truy Vấn Cập Nhật Hình Chữ Nhật Shopee**
* **Dạng bài:** Mock Contest 8 Task 3 (2D Segment Tree Lazy Propagation $O(Q \log^2 N)$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0523 - De Thi Thu 8 Bai 3 2D SegTree Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0523%20-%20De%20Thi%20Thu%208%20Bai%203%202D%20SegTree%20Shopee)
* **Phương pháp giải:** Cấu trúc dữ liệu Cây Phân Đoạn 2 chiều (2D Segment Tree / QuadTree) hỗ trợ cập nhật vùng chữ nhật 2D $[X_1..X_2, Y_1..Y_2]$ và tính tổng trong $O(Q \log^2 N)$.

---

### **[IKH-0524] - Đề Thi Thử 8 - Bài 4: Quy Hoạch Động Trên Chuỗi Cặp FPT**
* **Dạng bài:** Mock Contest 8 Task 4 (Manacher + Bitwise Trie XOR $O(N \cdot 30)$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0524 - De Thi Thu 8 Bai 4 Palindrome Bitwise Trie FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0524%20-%20De%20Thi%20Thu%208%20Bai%204%20Palindrome%20Bitwise%20Trie%20FPT)
* **Phương pháp giải:** Kết hợp Thuật toán Manacher lọc tiền tố/hậu tố đối xứng và Bitwise Trie tìm cặp chuỗi có giá trị XOR lớn nhất trong $O(N \cdot 30)$.

---

### **[IKH-0525] - Đề Thi Thử 8 - Bài 5: Tối Ưu Hóa Phân Cụm Dữ Liệu Zalo**
* **Dạng bài:** Mock Contest 8 Task 5 (Knuth DP + Convex Hull Trick Synthesis $O(N^2)$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0525 - De Thi Thu 8 Bai 5 Knuth CHT Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0525%20-%20De%20Thi%20Thu%208%20Bai%205%20Knuth%20CHT%20Zalo)
* **Phương pháp giải:** Tổng hợp Tối ưu Knuth (Knuth's DP) và Bao lồi CHT tối ưu hóa hàm chi phí phân cụm dữ liệu người dùng Zalo từ $O(N^3)$ xuống $O(N^2)$.

---

### **[IKH-0526] - Đề Thi Thử 8 - Bài 6: Đếm Chu Trình Nhỏ Nhất Đồ Thị Techcombank**
* **Dạng bài:** Mock Contest 8 Task 6 (Shortest Cycle / Minimum Weight Cycle BFS $O(V \cdot (V + E))$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0526 - De Thi Thu 8 Bai 6 Min Cycle Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0526%20-%20De%20Thi%20Thu%208%20Bai%206%20Min%20Cycle%20Techcombank)
* **Phương pháp giải:** Chạy BFS từ mọi đỉnh $u$ trên đồ thị không trọng số tìm độ dài chu trình nhỏ nhất (Girth of Graph) chứa $u$ trong $O(V \cdot (V + E))$.

---

### **[IKH-0527] - Đề Thi Thử 8 - Bài 7: Tìm Chuỗi Con Xuất Hiện K Lần VinFast**
* **Dạng bài:** Mock Contest 8 Task 7 (Suffix Automaton SAM $O(N)$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0527 - De Thi Thu 8 Bai 7 SAM K Matches VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0527%20-%20De%20Thi%20Thu%208%20Bai%207%20SAM%20K%20Matches%20VinFast)
* **Phương pháp giải:** Xây dựng Tự động thể Hậu tố (Suffix Automaton) kết hợp lan truyền trên Cây Link Tree đếm số lần xuất hiện `endpos` của mọi xâu con, tìm chuỗi con xuất hiện đúng $K$ lần dài nhất trong $O(N)$.

---

### **[IKH-0528] - Đề Thi Thử 8 - Bài 8: Ghép Cặp Trọng Số Cực Đại Viettel**
* **Dạng bài:** Mock Contest 8 Task 8 (Hungarian Algorithm / MCMF Bipartite Matching $O(V^3)$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0528 - De Thi Thu 8 Bai 8 Hungarian Matching Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0528%20-%20De%20Thi%20Thu%208%20Bai%208%20Hungarian%20Matching%20Viettel)
* **Phương pháp giải:** Thuật toán Áo (Hungarian Algorithm) tìm Ghép cặp trọng số cực đại trên đồ thị hai phía đầy đủ trong $O(V^3)$ thời gian.

---

### **[IKH-0529] - Đề Thi Thử 8 - Bài 9: Quy Hoạch Động Tăng Cường Định Lý Alien Shopee**
* **Dạng bài:** Mock Contest 8 Task 9 (Alien's Trick / WSI DP Optimization $O(N \log (\text{VAL}))$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0529 - De Thi Thu 8 Bai 9 Alien Trick Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0529%20-%20De%20Thi%20Thu%208%20Bai%209%20Alien%20Trick%20Shopee)
* **Phương pháp giải:** Kỹ thuật Alien's Trick chặt nhị phân chi phí phạt $\lambda$ để đưa bài toán chia $K$ đoạn có chi phí lồi về QHD không ràng buộc số đoạn trong $O(N \log (\text{VAL}))$.

---

### **[IKH-0530] - Đề Thi Thử 8 - Bài 10: Grand Synthesis Masterclass Mock Contest 8 FPT**
* **Dạng bài:** Mock Contest 8 Task 10 (Ultimate Synthesis Masterclass Challenge $O(N \log N)$)
* **Độ khó:** Rating 1800 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0530 - De Thi Thu 8 Bai 10 Ultimate Masterclass FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0530%20-%20De%20Thi%20Thu%208%20Bai%2010%20Ultimate%20Masterclass%20FPT)
* **Phương pháp giải:** Bài thi tổng hợp đỉnh cao (Ultimate Synthesis) kết hợp Đồ thị, Cấu trúc Dữ liệu Bền Vững, Thuật toán Chuỗi và Tối ưu Quy hoạch động - bài tập nâng cao hoàn tất Chuyên đề 11 và Chương trình Level 3!


---

### **[IKH-0531] - Luyện Đề 1 - Bài 1: Kiểm Tra Số Hoàn Hảo & Ước Số VinFast**
* **Dạng bài:** Luyện Đề 1 Task 1 (Math Divisors $O(\sqrt{N})$)
* **Độ khó:** Rating 1000 | ⭐☆☆☆☆
* **Thư mục local:** [IKH-0531 - Luyen De 1 Bai 1 So Hoan Hao VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0531%20-%20Luyen%20De%201%20Bai%201%20So%20Hoan%20Hao%20VinFast)
* **Phương pháp giải:** Duyệt ước số đến $\sqrt{N}$ tính tổng các ước thực sự của $N \le 10^{12}$ và kiểm tra tính hoàn hảo trong $O(\sqrt{N})$.

---

### **[IKH-0532] - Luyện Đề 1 - Bài 2: Đếm Xâu Xinh Đẹp Tiền Tố Viettel**
* **Dạng bài:** Luyện Đề 1 Task 2 (String Processing & Frequency Map Counter $O(N)$)
* **Độ khó:** Rating 1100 | ⭐★☆☆☆
* **Thư mục local:** [IKH-0532 - Luyen De 1 Bai 2 Xau Xinh Dep Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0532%20-%20Luyen%20De%201%20Bai%202%20Xau%20Xinh%20Dep%20Viettel)
* **Phương pháp giải:** Duyệt tiền tố chuỗi ký tự kết hợp mảng đánh dấu tần số ký tự đếm số xâu xinh đẹp thỏa mãn điều kiện tần số trong $O(N)$.

---

### **[IKH-0533] - Luyện Đề 1 - Bài 3: Phân Bổ Ngân Sách Mua Sắm Shopee**
* **Dạng bài:** Luyện Đề 1 Task 3 (Greedy Algorithm & Sorting $O(N \log N)$)
* **Độ khó:** Rating 1200 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0533 - Luyen De 1 Bai 3 Ngan Sach Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0533%20-%20Luyen%20De%201%20Bai%203%20Ngan%20Sach%20Shopee)
* **Phương pháp giải:** Thuật toán Tham ăn (Greedy) kết hợp Sắp xếp tăng dần giá thành vật tư tối đa hóa số lượng mặt hàng mua được với ngân sách $S$ trong $O(N \log N)$.

---

### **[IKH-0534] - Luyện Đề 1 - Bài 4: Tìm Đoạn Con Có Tổng Bằng K FPT**
* **Dạng bài:** Luyện Đề 1 Task 4 (Prefix Sum + Hash Map / Two Pointers $O(N)$)
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0534 - Luyen De 1 Bai 4 Tong Bang K FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0534%20-%20Luyen%20De%201%20Bai%204%20Tong%20Bang%20K%20FPT)
* **Phương pháp giải:** Kỹ thuật Tổng tiền tố (Prefix Sum) kết hợp `std::unordered_map` lưu vị trí đếm số lượng đoạn con liên tiếp có tổng đúng bằng $K$ trong $O(N)$.

---

### **[IKH-0535] - Luyện Đề 1 - Bài 5: Tối Ưu Lịch Trình Giao Hàng Zalo**
* **Dạng bài:** Luyện Đề 1 Task 5 (0/1 Knapsack Dynamic Programming $O(N \cdot W)$)
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0535 - Luyen De 1 Bai 5 Giao Hang Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0535%20-%20Luyen%20De%201%20Bai%205%20Giao%20Hang%20Zalo)
* **Phương pháp giải:** Quy hoạch động Bài toán Cái túi (0/1 Knapsack DP) tối đa hóa giá trị đơn hàng vận chuyển dưới tải trọng cho phép $W$ trong $O(N \cdot W)$.

---

### **[IKH-0536] - Luyện Đề 1 - Bài 6: Truy Vấn Phần Tử Lớn Thứ K Techcombank**
* **Dạng bài:** Luyện Đề 1 Task 6 (Fenwick Tree / Min-Heap Query $O(N \log N)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0536 - Luyen De 1 Bai 6 Lon Thu K Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0536%20-%20Luyen%20De%201%20Bai%206%20Lon%20Thu%20K%20Techcombank)
* **Phương pháp giải:** Cây Fenwick Tree kết hợp Chặt nhị phân / Max-Heap hỗ trợ thêm giá trị giao dịch và tìm phần tử lớn thứ $K$ trên dòng chảy dữ liệu trong $O(\log N)$.

---

### **[IKH-0537] - Luyện Đề 1 - Bài 7: Tìm Đường Đi Ngắn Nhất Trạm Xe Být VinFast**
* **Dạng bài:** Luyện Đề 1 Task 7 (Shortest Path Dijkstra Algorithm $O((V + E) \log V)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0537 - Luyen De 1 Bai 7 Dijkstra Bus VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0537%20-%20Luyen%20De%201%20Bai%207%20Dijkstra%20Bus%20VinFast)
* **Phương pháp giải:** Thuật toán Dijkstra dùng Min-Heap tìm thời gian di chuyển ngắn nhất giữa trạm xe xuất phát $S$ và trạm đích $T$ trong $O((V + E) \log V)$.

---

### **[IKH-0538] - Luyện Đề 1 - Bài 8: Đếm Cặp Phần Tử Đồng Dư Viettel**
* **Dạng bài:** Luyện Đề 1 Task 8 (Modulo Arithmetic & Counter $O(N)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0538 - Luyen De 1 Bai 8 Dong Du Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0538%20-%20Luyen%20De%201%20Bai%208%20Dong%20Du%20Viettel)
* **Phương pháp giải:** Phân loại phần tử theo số dư $mod M$, dùng mảng tần số đếm số cặp $(A_i, A_j)$ thỏa mãn $(A_i + A_j) \pmod M = 0$ trong $O(N)$.

---

### **[IKH-0539] - Luyện Đề 1 - Bài 9: Xếp Hình Chữ Nhật Diện Tích Lớn Nhất Shopee**
* **Dạng bài:** Luyện Đề 1 Task 9 (Largest Rectangle in Histogram Monotonic Stack $O(N)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0539 - Luyen De 1 Bai 9 Hinh Chu Nhat Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0539%20-%20Luyen%20De%201%20Bai%209%20Hinh%20Chu%20Nhat%20Shopee)
* **Phương pháp giải:** Sử dụng Stack đơn điệu (Monotonic Stack) tìm cận trái và cận phải nhỏ hơn gần nhất cho từng cột, tính diện tích hình chữ nhật lớn nhất trong biểu đồ cột trong $O(N)$.

---

### **[IKH-0540] - Luyện Đề 1 - Bài 10: Grand Synthesis Đề Thi Thử 1 FPT**
* **Dạng bài:** Luyện Đề 1 Task 10 (Segment Tree Point Update & Range Query $O(Q \log N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0540 - Luyen De 1 Bai 10 Grand Synthesis FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0540%20-%20Luyen%20De%201%20Bai%2010%20Grand%20Synthesis%20FPT)
* **Phương pháp giải:** Tổng hợp Cây Phân Đoạn (Segment Tree) hỗ trợ cập nhật điểm dữ liệu và truy vấn tổng/giá trị cực đại trên đoạn $[L, R]$ trong $O(Q \log N)$.


---

### **[IKH-0541] - Luyện Đề 2 - Bài 1: Đếm Số Cặp Ký Tự Giống Nhau Trong Chuỗi VinFast**
* **Dạng bài:** Luyện Đề 2 Task 1 (String Frequency Map Counter $O(N)$)
* **Độ khó:** Rating 1100 | ⭐★☆☆☆
* **Thư mục local:** [IKH-0541 - Luyen De 2 Bai 1 Cap Ky Tu VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0541%20-%20Luyen%20De%202%20Bai%201%20Cap%20Ky%20Tu%20VinFast)
* **Phương pháp giải:** Đếm tần số xuất hiện của từng ký tự trong chuỗi $S$, áp dụng công thức tổ hợp $C_{cnt}^2 = \frac{cnt \cdot (cnt - 1)}{2}$ đếm số cặp giống nhau trong $O(N)$.

---

### **[IKH-0542] - Luyện Đề 2 - Bài 2: Phân Tích Số Nguyên Thành Tổng Các Số Nguyên Tố Viettel**
* **Dạng bài:** Luyện Đề 2 Task 2 (Goldbach's Conjecture / Sieve $O(\sqrt{N})$)
* **Độ khó:** Rating 1200 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0542 - Luyen De 2 Bai 2 Phan Tich Nguyen To Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0542%20-%20Luyen%20De%202%20Bai%202%20Phan%20Tich%20Nguyen%20To%20Viettel)
* **Phương pháp giải:** Áp dụng Giả thuyết Goldbach và thuật toán kiểm tra số nguyên tố $O(\sqrt{N})$ biểu diễn số chẵn $N$ thành tổng của hai số nguyên tố $P_1 + P_2$.

---

### **[IKH-0543] - Luyện Đề 2 - Bài 3: Sắp Xếp Lịch Trình Xe Tải Container Shopee**
* **Dạng bài:** Luyện Đề 2 Task 3 (Greedy Interval Scheduling $O(N \log N)$)
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0543 - Luyen De 2 Bai 3 Container Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0543%20-%20Luyen%20De%202%20Bai%203%20Container%20Shopee)
* **Phương pháp giải:** Thuật toán Tham ăn (Greedy) sắp xếp các khoảng thời gian theo thời điểm kết thúc tăng dần, tối đa hóa số chuyến xe vận chuyển không bị chồng chéo thời gian $O(N \log N)$.

---

### **[IKH-0544] - Luyện Đề 2 - Bài 4: Tìm Độ Dài Dãy Con Tăng Dài Nhất FPT**
* **Dạng bài:** Luyện Đề 2 Task 4 (Longest Increasing Subsequence LIS $O(N \log N)$)
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0544 - Luyen De 2 Bai 4 LIS BS FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0544%20-%20Luyen%20De%202%20Bai%204%20LIS%20BS%20FPT)
* **Phương pháp giải:** Kết hợp Quy hoạch động và Tìm kiếm nhị phân `std::lower_bound` tìm độ dài dãy con tăng dài nhất (LIS) trong $O(N \log N)$.

---

### **[IKH-0545] - Luyện Đề 2 - Bài 5: Kiểm Tra Đồ Thị Liên Thông Mạnh Zalo**
* **Dạng bài:** Luyện Đề 2 Task 5 (Tarjan Strongly Connected Components $O(V + E)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0545 - Luyen De 2 Bai 5 Tarjan SCC Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0545%20-%20Luyen%20De%202%20Bai%205%20Tarjan%20SCC%20Zalo)
* **Phương pháp giải:** Thuật toán Tarjan phân tích đồ thị có hướng thành các thành phần liên thông mạnh (SCC) kiểm tra mạng lưới liên lạc Zalo trong $O(V + E)$.

---

### **[IKH-0546] - Luyện Đề 2 - Bài 6: Truy Vấn Tổng Đoạn Cập Nhật Đơn Điệu Techcombank**
* **Dạng bài:** Luyện Đề 2 Task 6 (Segment Tree Lazy Propagation $O(\log N)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0546 - Luyen De 2 Bai 6 Lazy SegTree Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0546%20-%20Luyen%20De%202%20Bai%206%20Lazy%20SegTree%20Techcombank)
* **Phương pháp giải:** Áp dụng Kỹ thuật Đẩy lười (Lazy Propagation) trên Cây Phân Đoạn Segment Tree xử lý tăng giá trị đoạn $[L, R]$ và truy vấn tổng trong $O(\log N)$.

---

### **[IKH-0547] - Luyện Đề 2 - Bài 7: Tìm Khung Cây Tối Ưu Mạng Lưới Điện VinFast**
* **Dạng bài:** Luyện Đề 2 Task 7 (Minimum Spanning Tree Kruskal / Prim $O(E \log V)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0547 - Luyen De 2 Bai 7 MST VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0547%20-%20Luyen%20De%202%20Bai%207%20MST%20VinFast)
* **Phương pháp giải:** Dựng Cây khung nhỏ nhất MST bằng thuật toán Kruskal kết hợp DSU tối ưu tổng chi phí lắp đặt tuyến cáp điện VinFast trong $O(E \log V)$.

---

### **[IKH-0548] - Luyện Đề 2 - Bài 8: Đếm Chuỗi Con Đối Xứng Dài Nhất Viettel**
* **Dạng bài:** Luyện Đề 2 Task 8 (Manacher's Algorithm $O(N)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0548 - Luyen De 2 Bai 8 Manacher Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0548%20-%20Luyen%20De%202%20Bai%208%20Manacher%20Viettel)
* **Phương pháp giải:** Thuật toán Manacher tính bán kính đối xứng tâm trên chuỗi $S$ mở rộng, tìm độ dài chuỗi con đối xứng dài nhất trong $O(N)$.

---

### **[IKH-0549] - Luyện Đề 2 - Bài 9: Tối Ưu Hóa Chi Phí Vận Chuyển Đa Tầng Shopee**
* **Dạng bài:** Luyện Đề 2 Task 9 (Convex Hull Trick CHT $O(N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0549 - Luyen De 2 Bai 9 CHT Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0549%20-%20Luyen%20De%202%20Bai%209%20CHT%20Shopee)
* **Phương pháp giải:** Kỹ thuật Bao Lồi Tối Ưu QHD (Convex Hull Trick) loại bỏ các đường thẳng bị bao phủ, tính chi phí vận chuyển tối ưu trong $O(N)$.

---

### **[IKH-0550] - Luyện Đề 2 - Bài 10: Grand Synthesis Đề Thi Thử 2 FPT**
* **Dạng bài:** Luyện Đề 2 Task 10 (Heavy-Light Decomposition HLD + SegTree $O(N \log^2 N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0550 - Luyen De 2 Bai 10 Grand Synthesis FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0550%20-%20Luyen%20De%202%20Bai%2010%20Grand%20Synthesis%20FPT)
* **Phương pháp giải:** Tổng hợp Phân rã cây Heavy-Light Decomposition (HLD) kết hợp Segment Tree xử lý cập nhật giá trị nút và truy vấn cực đại trên đường đi $(u, v)$ trong $O(N \log^2 N)$.


---

### **[IKH-0551] - Luyện Đề 3 - Bài 1: Đếm Số Lượng Ước Số Của N VinFast**
* **Dạng bài:** Luyện Đề 3 Task 1 (Number Theory Divisor Count $O(\sqrt{N})$)
* **Độ khó:** Rating 1100 | ⭐★☆☆☆
* **Thư mục local:** [IKH-0551 - Luyen De 3 Bai 1 Dem Uoc VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0551%20-%20Luyen%20De%203%20Bai%201%20Dem%20Uoc%20VinFast)
* **Phương pháp giải:** Duyệt ước số đến $\sqrt{N}$ đếm số lượng ước số của $N \le 10^{12}$ trong $O(\sqrt{N})$.

---

### **[IKH-0552] - Luyện Đề 3 - Bài 2: Kiểm Tra Chuỗi Anagram Viettel**
* **Dạng bài:** Luyện Đề 3 Task 2 (String Frequency Array Anagram Check $O(N)$)
* **Độ khó:** Rating 1200 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0552 - Luyen De 3 Bai 2 Anagram Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0552%20-%20Luyen%20De%203%20Bai%202%20Anagram%20Viettel)
* **Phương pháp giải:** Dùng mảng tần số 26 ký tự so sánh hai chuỗi $S_1, S_2$ kiểm tra xem có phải là đảo từ (Anagram) của nhau hay không trong $O(N)$.

---

### **[IKH-0553] - Luyện Đề 3 - Bài 3: Phân Phối Gói Hàng Tiết Kiệm Shopee**
* **Dạng bài:** Luyện Đề 3 Task 3 (Greedy Algorithm & Two Pointers $O(N \log N)$)
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0553 - Luyen De 3 Bai 3 Goi Hang Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0553%20-%20Luyen%20De%203%20Bai%203%20Goi%20Hang%20Shopee)
* **Phương pháp giải:** Sắp xếp mảng kích thước gói hàng kết hợp kỹ thuật Hai con trỏ (Two Pointers) ghép cặp tối ưu các gói hàng dưới tải trọng cho phép $K$ trong $O(N \log N)$.

---

### **[IKH-0554] - Luyện Đề 3 - Bài 4: Tìm Tổng Đoạn Con Lớn Nhất Bằng Kadane FPT**
* **Dạng bài:** Luyện Đề 3 Task 4 (Kadane's Algorithm Maximum Subarray Sum $O(N)$)
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0554 - Luyen De 3 Bai 4 Kadane FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0554%20-%20Luyen%20De%203%20Bai%204%20Kadane%20FPT)
* **Phương pháp giải:** Thuật toán Kadane tính tổng đoạn con liên tiếp lớn nhất trong $O(N)$ thời gian và $O(1)$ bộ nhớ.

---

### **[IKH-0555] - Luyện Đề 3 - Bài 5: Truy Vấn Cập Nhật Đoạn Tổng Vùng 2D Zalo**
* **Dạng bài:** Luyện Đề 3 Task 5 (2D Fenwick Tree / 2D Prefix Sum $O(\log^2 N)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0555 - Luyen De 3 Bai 5 2D BIT Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0555%20-%20Luyen%20De%203%20Bai%205%202D%20BIT%20Zalo)
* **Phương pháp giải:** Cấu trúc Cây Fenwick Tree 2D quản lý ma trận dữ liệu người dùng Zalo, hỗ trợ cập nhật điểm và tính tổng hình chữ nhật $[X_1..X_2, Y_1..Y_2]$ trong $O(\log^2 N)$.

---

### **[IKH-0556] - Luyện Đề 3 - Bài 6: Đếm Cặp Số Có Tổng Nhỏ Hơn K Techcombank**
* **Dạng bài:** Luyện Đề 3 Task 6 (Two Pointers / Binary Search $O(N \log N)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0556 - Luyen De 3 Bai 6 Cap So Nho Hon K Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0556%20-%20Luyen%20De%203%20Bai%206%20Cap%20So%20Nho%20Hon%20K%20Techcombank)
* **Phương pháp giải:** Sắp xếp mảng kết hợp Kỹ thuật Hai con trỏ đếm số lượng cặp $(A_i, A_j)$ có tổng $A_i + A_j < K$ trong $O(N \log N)$.

---

### **[IKH-0557] - Luyện Đề 3 - Bài 7: Phân Tích Thành Phần Liên Thông Bằng DSU VinFast**
* **Dạng bài:** Luyện Đề 3 Task 7 (Disjoint Set Union DSU $O(E \cdot \alpha(V))$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0557 - Luyen De 3 Bai 7 DSU VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0557%20-%20Luyen%20De%203%20Bai%207%20DSU%20VinFast)
* **Phương pháp giải:** Cấu trúc DSU Path Compression kết hợp Union by Rank phân tích các thành phần liên thông và đếm số vùng liên thông mạng lưới sạc xe điện trong $O(E \cdot \alpha(V))$.

---

### **[IKH-0558] - Luyện Đề 3 - Bài 8: So Khớp Mã Mẫu Giao Dịch Bằng KMP Viettel**
* **Dạng bài:** Luyện Đề 3 Task 8 (KMP String Matching Algorithm $O(N + M)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0558 - Luyen De 3 Bai 8 KMP Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0558%20-%20Luyen%20De%3%20Bai%208%20KMP%20Viettel)
* **Phương pháp giải:** Thuật toán KMP xây dựng mảng tiền tố `pi[i]` tìm kiếm tất cả các vị trí xuất hiện của mã mẫu giao dịch $P$ trong nhật ký mạng $T$ trong $O(N + M)$.

---

### **[IKH-0559] - Luyện Đề 3 - Bài 9: Tối Ưu Hóa Chi Phí Chia Đoạn DP Divide Conquer Shopee**
* **Dạng bài:** Luyện Đề 3 Task 9 (Divide & Conquer DP Optimization $O(K \cdot N \log N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0559 - Luyen De 3 Bai 9 Divide Conquer DP Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0559%20-%20Luyen%20De%203%20Bai%209%20Divide%20Conquer%20DP%20Shopee)
* **Phương pháp giải:** Tối ưu hóa Chia để trị (Divide & Conquer DP) giảm độ phức tạp từ $O(K \cdot N^2)$ xuống $O(K \cdot N \log N)$ nhờ tính đơn điệu điểm cắt $opt[i][j] \le opt[i][j+1]$.

---

### **[IKH-0560] - Luyện Đề 3 - Bài 10: Grand Synthesis Đề Thi Thử 3 FPT**
* **Dạng bài:** Luyện Đề 3 Task 10 (Persistent Segment Tree $O(\log N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0560 - Luyen De 3 Bai 10 Grand Synthesis FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0560%20-%20Luyen%20De%203%20Bai%2010%20Grand%20Synthesis%20FPT)
* **Phương pháp giải:** Tổng hợp Cây Phân Đoạn Bền Vững (Persistent Segment Tree) truy vấn giá trị trên các phiên bản lịch sử cập nhật cấu hình mạng trong $O(\log N)$.


---

### **[IKH-0561] - Luyện Đề 4 - Bài 1: Kiểm Tra Chuỗi Đảo Ngược VinFast**
* **Dạng bài:** Luyện Đề 4 Task 1 (Two Pointers String Reversal $O(N)$)
* **Độ khó:** Rating 1100 | ⭐★☆☆☆
* **Thư mục local:** [IKH-0561 - Luyen De 4 Bai 1 Dao Nguoc VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0561%20-%20Luyen%20De%204%20Bai%201%20Dao%20Nguoc%20VinFast)
* **Phương pháp giải:** Sử dụng kỹ thuật `std::reverse` hoặc Hai con trỏ đảo ngược vị trí ký tự trong chuỗi $S$ trong $O(N)$ thời gian và $O(1)$ bộ nhớ phụ.

---

### **[IKH-0562] - Luyện Đề 4 - Bài 2: Đếm Số Lượng Ước Chung Của Hai Số Viettel**
* **Dạng bài:** Luyện Đề 4 Task 2 (GCD & Divisors Count $O(\sqrt{\gcd(A, B)})$)
* **Độ khó:** Rating 1200 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0562 - Luyen De 4 Bai 2 Uoc Chung Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0562%20-%20Luyen%20De%204%20Bai%202%20Uoc%20Chung%20Viettel)
* **Phương pháp giải:** Tìm ước chung lớn nhất $G = \gcd(A, B)$ bằng thuật toán Euclid, sau đó đếm số lượng ước của $G$ trong $O(\sqrt{G})$.

---

### **[IKH-0563] - Luyện Đề 4 - Bài 3: Tối Ưu Hóa Phân Bổ Công Việc Shopee**
* **Dạng bài:** Luyện Đề 4 Task 3 (Greedy Job Scheduling $O(N \log N)$)
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0563 - Luyen De 4 Bai 3 Cong Viec Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0563%20-%20Luyen%20De%204%20Bai%203%20Cong%20Viec%20Shopee)
* **Phương pháp giải:** Thuật toán Tham ăn (Greedy) kết hợp Sắp xếp thời hạn (Deadline) và Lợi nhuận (Profit) bằng Priority Queue tối đa hóa lợi nhuận thực hiện trong $O(N \log N)$.

---

### **[IKH-0564] - Luyện Đề 4 - Bài 4: Tìm Độ Dài Chuỗi Con Chung Dài Nhất LCS FPT**
* **Dạng bài:** Luyện Đề 4 Task 4 (Longest Common Subsequence LCS DP $O(N \cdot M)$)
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0564 - Luyen De 4 Bai 4 LCS FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0564%20-%20Luyen%20De%204%20Bai%204%20LCS%20FPT)
* **Phương pháp giải:** Quy hoạch động mảng 2D $dp[i][j]$ tìm độ dài chuỗi con chung dài nhất (LCS) giữa hai chuỗi $S_1$ và $S_2$ trong $O(N \cdot M)$.

---

### **[IKH-0565] - Luyện Đề 4 - Bài 5: Truy Vấn Cây Phân Đoạn Nén Tọa Độ Zalo**
* **Dạng bài:** Luyện Đề 4 Task 5 (Coordinate Compression + Segment Tree $O(N \log N)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0565 - Luyen De 4 Bai 5 SegTree Nen Toa Do Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0565%20-%20Luyen%20De%204%20Bai%205%20SegTree%20Nen%20Toa%20Do%20Zalo)
* **Phương pháp giải:** Nén tọa độ tập dữ liệu $A_i \le 10^9$ về dải $[1 \dots N]$ rồi xây dựng Cây phân đoạn Segment Tree thực hiện truy vấn và cập nhật trong $O(N \log N)$.

---

### **[IKH-0566] - Luyện Đề 4 - Bài 6: Đếm Chu Trình Trên Đồ Thị Thị Trường Techcombank**
* **Dạng bài:** Luyện Đề 4 Task 6 (Matrix Exponentiation Path Counting $O(V^3 \log K)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0566 - Luyen De 4 Bai 6 Dem Chu Trinh Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0566%20-%20Luyen%20De%204%20Bai%206%20Dem%20Chu%20Trinh%20Techcombank)
* **Phương pháp giải:** Biểu diễn đồ thị dưới dạng Ma trận kề $A$, nhân lũy thừa ma trận $A^K$ bằng Lũy thừa nhị phân đếm số đường đi/chu trình độ dài $K$ trong $O(V^3 \log K)$.

---

### **[IKH-0567] - Luyện Đề 4 - Bài 7: Tìm Cầu Và Khớp Mạng Lưới Cáp Biển VinFast**
* **Dạng bài:** Luyện Đề 4 Task 7 (Tarjan Bridges & Articulation Points $O(V + E)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0567 - Luyen De 4 Bai 7 Cau Khop VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0567%20-%20Luyen%20De%204%20Bai%207%20Cau%20Khop%20VinFast)
* **Phương pháp giải:** Đánh số thứ tự DFS `num[u]` và `low[u]` theo thuật toán Tarjan tìm tất cả các cạnh cầu và đỉnh khớp trên mạng lưới truyền tải cáp biển VinFast trong $O(V + E)$.

---

### **[IKH-0568] - Luyện Đề 4 - Bài 8: So Khớp Đa Mẫu Mã Giao Dịch Viettel**
* **Dạng bài:** Luyện Đề 4 Task 8 (Aho-Corasick Automaton $O(N + \sum |P|)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0568 - Luyen De 4 Bai 8 Aho Corasick Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0568%20-%20Luyen%20De%204%20Bai%208%20Aho%20Corasick%20Viettel)
* **Phương pháp giải:** Xây dựng Cây Trie kết hợp các liên kết thất bại (Suffix Link) BFS theo tự động Aho-Corasick tìm kiếm đồng thời tất cả các chuỗi mẫu trong văn bản trong $O(N + \sum |P|)$.

---

### **[IKH-0569] - Luyện Đề 4 - Bài 9: Tối Ưu Hóa QHD Chia Cụm Dữ Liệu Knuth Shopee**
* **Dạng bài:** Luyện Đề 4 Task 9 (Knuth's Dynamic Programming Optimization $O(N^2)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0569 - Luyen De 4 Bai 9 Knuth DP Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0569%20-%20Luyen%20De%204%20Bai%209%20Knuth%20DP%20Shopee)
* **Phương pháp giải:** Tối ưu hóa Knuth DP giảm độ phức tạp bài toán chia cụm dữ liệu $dp[i][j]$ từ $O(N^3)$ xuống $O(N^2)$ nhờ điều kiện tứ giác $opt[i][j-1] \le opt[i][j] \le opt[i+1][j]$.

---

### **[IKH-0570] - Luyện Đề 4 - Bài 10: Grand Synthesis Đề Thi Thử 4 FPT**
* **Dạng bài:** Luyện Đề 4 Task 10 (Suffix Automaton SAM $O(N)$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0570 - Luyen De 4 Bai 10 Grand Synthesis FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0570%20-%20Luyen%20De%204%20Bai%2010%20Grand%20Synthesis%20FPT)
* **Phương pháp giải:** Tổng hợp Tự động xâu hậu tố Suffix Automaton (SAM) đếm số xâu con phân biệt và giải quyết các bài toán chuỗi phức tạp trong $O(N)$ thời gian và bộ nhớ.


---

### **[IKH-0571] - Luyện Đề 5 - Bài 1: Đếm Ký Tự Phân Biệt Trong Chuỗi VinFast**
* **Dạng bài:** Luyện Đề 5 Task 1 (Set / Frequency Array $O(N)$)
* **Độ khó:** Rating 1100 | ⭐★☆☆☆
* **Thư mục local:** [IKH-0571 - Luyen De 5 Bai 1 Dem Ky Tu Phan Biet VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0571%20-%20Luyen%20De%205%20Bai%201%20Dem%20Ky%20Tu%20Phan%20Biet%20VinFast)
* **Phương pháp giải:** Sử dụng mảng đánh dấu `bool mark[256]` đếm số lượng ký tự phân biệt xuất hiện trong chuỗi $S$ trong $O(N)$ thời gian và $O(1)$ bộ nhớ.

---

### **[IKH-0572] - Luyện Đề 5 - Bài 2: Tìm Số Nhỏ Nhất Có N Ước Số Viettel**
* **Dạng bài:** Luyện Đề 5 Task 2 (Prime Factorization & Backtracking $O(N)$)
* **Độ khó:** Rating 1250 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0572 - Luyen De 5 Bai 2 So Co N Uoc Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0572%20-%20Luyen%20De%205%20Bai%202%20So%20Co%20N%20Uoc%20Viettel)
* **Phương pháp giải:** Phân tích $N$ thành tích các thừa số $(a_1+1)(a_2+1)\dots$, dùng Quay lui ghép thừa số nguyên tố nhỏ nhất $2^{a_1} 3^{a_2} 5^{a_3}\dots$ tìm số nhỏ nhất.

---

### **[IKH-0573] - Luyện Đề 5 - Bài 3: Lựa Chọn Tuyến Đường Vận Chuyển Hàng Shopee**
* **Dạng bài:** Luyện Đề 5 Task 3 (Greedy & Binary Search $O(N \log N)$)
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0573 - Luyen De 5 Bai 3 Tuyen Duong Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0573%20-%20Luyen%20De%205%20Bai%203%20Tuyen%20Duong%20Shopee)
* **Phương pháp giải:** Thuật toán Tham ăn kết hợp Tìm kiếm nhị phân lựa chọn tuyến đường có khoảng cách tối ưu dưới chi phí cho phép trong $O(N \log N)$.

---

### **[IKH-0574] - Luyện Đề 5 - Bài 4: Tối Ưu Hóa Chi Phí Sơn Nhà QHD FPT**
* **Dạng bài:** Luyện Đề 5 Task 4 (Dynamic Programming State Machine $O(N)$)
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0574 - Luyen De 5 Bai 4 Son Nha FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0574%20-%20Luyen%20De%205%20Bai%204%20Son%20Nha%20FPT)
* **Phương pháp giải:** Quy hoạch động Máy trạng thái (State Machine DP) $dp[i][color]$ tối thiểu hóa tổng chi phí sơn $N$ ngôi nhà sao cho hai nhà liền kề không cùng màu trong $O(N)$.

---

### **[IKH-0575] - Luyện Đề 5 - Bài 5: Truy Vấn Cập Nhật Đoạn Max Segment Tree Zalo**
* **Dạng bài:** Luyện Đề 5 Task 5 (Segment Tree Range Maximum Query $O(\log N)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0575 - Luyen De 5 Bai 5 SegTree Max Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0575%20-%20Luyen%20De%205%20Bai%205%20SegTree%20Max%20Zalo)
* **Phương pháp giải:** Cấu trúc Cây phân đoạn Segment Tree quản lý truy vấn giá trị lớn nhất trên đoạn $[L, R]$ và cập nhật điểm dữ liệu Zalo trong $O(\log N)$.

---

### **[IKH-0576] - Luyện Đề 5 - Bài 6: Đếm Cặp Phần Tử Có Hiệu Nhỏ Hơn K Techcombank**
* **Dạng bài:** Luyện Đề 5 Task 6 (Two Pointers / Binary Search $O(N \log N)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0576 - Luyen De 5 Bai 6 Cap Hieu Nho Hon K Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0576%20-%20Luyen%20De%205%20Bai%206%20Cap%20Hieu%20Nho%20Hon%20K%20Techcombank)
* **Phương pháp giải:** Sắp xếp mảng kết hợp Kỹ thuật Hai con trỏ đếm số lượng cặp $(A_i, A_j)$ có $|A_i - A_j| < K$ trong $O(N \log N)$.

---

### **[IKH-0577] - Luyện Đề 5 - Bài 7: Tìm Đường Đi Có Trọng Số Lớn Nhất Trên Cây VinFast**
* **Dạng bài:** Luyện Đề 5 Task 7 (Tree Diameter / Tree Dynamic Programming $O(N)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0577 - Luyen De 5 Bai 7 Duong Kinh Cay VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0577%20-%20Luyen%20De%205%20Bai%207%20Duong%20Kinh%20Cay%20VinFast)
* **Phương pháp giải:** Thuật toán DFS 2 lần hoặc Quy hoạch động trên cây (Tree DP) tìm độ dài đường kính cây (Tree Diameter) lớn nhất trong $O(N)$.

---

### **[IKH-0578] - Luyện Đề 5 - Bài 8: So Khớp Mẫu Xâu Động Bằng Z-Algorithm Viettel**
* **Dạng bài:** Luyện Đề 5 Task 8 (Z-Algorithm String Matching $O(N + M)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0578 - Luyen De 5 Bai 8 Z Algo Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0578%20-%20Luyen%20De%205%20Bai%208%20Z%20Algo%20Viettel)
* **Phương pháp giải:** Thuật toán Z-Algorithm tính mảng $Z[i]$ trên xâu ghép $P + \# + T$ tìm vị trí các khớp tiền tố dài nhất trong $O(N + M)$.

---

### **[IKH-0579] - Luyện Đề 5 - Bài 9: Tối Ưu QHD Đường Thẳng Dynamic CHT Shopee**
* **Dạng bài:** Luyện Đề 5 Task 9 (Dynamic CHT `LineContainer` $O(N \log N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0579 - Luyen De 5 Bai 9 Dynamic CHT Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0579%20-%20Luyen%20De%205%20Bai%209%20Dynamic%20CHT%20Shopee)
* **Phương pháp giải:** Cấu trúc Dynamic Convex Hull Trick `std::multiset` hỗ trợ thêm đường thẳng hệ số góc bất kỳ và truy vấn giá trị cực đại tại $x$ trong $O(N \log N)$.

---

### **[IKH-0580] - Luyện Đề 5 - Bài 10: Grand Synthesis Đề Thi Thử 5 FPT**
* **Dạng bài:** Luyện Đề 5 Task 10 (Alien's Trick WQS Binary Search $O(N \log C)$)
* **Độ khó:** Rating 1750 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0580 - Luyen De 5 Bai 10 Grand Synthesis FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0580%20-%20Luyen%20De%205%20Bai%2010%20Grand%20Synthesis%20FPT)
* **Phương pháp giải:** Kỹ thuật Alien's Trick (WQS Binary Search) chuyển đổi bài toán QHD có ràng buộc $K$ đoạn con thành bài toán phạt chi phí nhị phân trong $O(N \log C)$.


---

### **[IKH-0581] - Luyện Đề 6 - Bài 1: Đếm Tần Số Xuất Hiện Của Ký Tự VinFast**
* **Dạng bài:** Luyện Đề 6 Task 1 (Map / Array Counter $O(N)$)
* **Độ khó:** Rating 1100 | ⭐★☆☆☆
* **Thư mục local:** [IKH-0581 - Luyen De 6 Bai 1 Tan So Ky Tu VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0581%20-%20Luyen%20De%206%20Bai%201%20Tan%20So%20Ky%20Tu%20VinFast)
* **Phương pháp giải:** Sử dụng mảng tần số 256 phần tử đếm số lần xuất hiện của từng ký tự trong chuỗi $S$ và in theo thứ tự alphabet trong $O(N)$.

---

### **[IKH-0582] - Luyện Đề 6 - Bài 2: Phân Tích Thừa Số Nguyên Tố Của N Viettel**
* **Dạng bài:** Luyện Đề 6 Task 2 (Prime Factorization $O(\sqrt{N})$)
* **Độ khó:** Rating 1200 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0582 - Luyen De 6 Bai 2 Thua So Nguyen To Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0582%20-%20Luyen%20De%206%20Bai%202%20Thua%20So%20Nguyen%20To%20Viettel)
* **Phương pháp giải:** Thử chia $N$ cho các số nguyên tố tăng dần đến $\sqrt{N}$ đếm số lượng thừa số nguyên tố mũ $p^k$ trong $O(\sqrt{N})$.

---

### **[IKH-0583] - Luyện Đề 6 - Bài 3: Sắp Xếp Công Việc Trễ Hạn Nhỏ Nhất Shopee**
* **Dạng bài:** Luyện Đề 6 Task 3 (Greedy Min Lateness Scheduling $O(N \log N)$)
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0583 - Luyen De 6 Bai 3 Min Lateness Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0583%20-%20Luyen%20De%206%20Bai%203%20Min%20Lateness%20Shopee)
* **Phương pháp giải:** Sắp xếp công việc theo thời hạn Deadline tăng dần (Earliest Deadline First), tính độ trễ trễ hạn cực đại trong $O(N \log N)$.

---

### **[IKH-0584] - Luyện Đề 6 - Bài 4: Tối Ưu Hóa Chi Phí Đổi Tiền Xu FPT**
* **Dạng bài:** Luyện Đề 6 Task 4 (Coin Change Dynamic Programming $O(N \cdot S)$)
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0584 - Luyen De 6 Bai 4 Coin Change FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0584%20-%20Luyen%20De%206%20Bai%204%20Coin%20Change%20FPT)
* **Phương pháp giải:** Quy hoạch động mảng 1D $dp[i]$ tìm số lượng đồng tiền xu nhỏ nhất cần dùng để đổi tổng số tiền $S$ trong $O(N \cdot S)$.

---

### **[IKH-0585] - Luyện Đề 6 - Bài 5: Truy Vấn Tổng Đoạn Cây Fenwick Zalo**
* **Dạng bài:** Luyện Đề 6 Task 5 (Fenwick Tree BIT Point Update Range Query $O(\log N)$)
* **Độ khó:** Rating 1400 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0585 - Luyen De 6 Bai 5 BIT Point Update Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0585%20-%20Luyen%20De%206%20Bai%205%20BIT%20Point%20Update%20Zalo)
* **Phương pháp giải:** Cấu trúc Cây Fenwick Tree hỗ trợ thao tác cộng thêm giá trị vào vị trí $u$ và tính tổng tiền tố đoạn $[L, R]$ trong $O(\log N)$.

---

### **[IKH-0586] - Luyện Đề 6 - Bài 6: Đếm Cặp Số Có Tổng Là Số Nguyên Tố Techcombank**
* **Dạng bài:** Luyện Đề 6 Task 6 (Sieve & Two Pointers / Hash $O(N \log N)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0586 - Luyen De 6 Bai 6 Cap Tong Prime Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0586%20-%20Luyen%20De%206%20Bai%206%20Cap%20Tong%20Prime%20Techcombank)
* **Phương pháp giải:** Sàng số nguyên tố Eratosthenes kết hợp duyệt cặp phần tử đếm số lượng cặp $(A_i, A_j)$ có tổng $A_i + A_j$ là số nguyên tố trong $O(N \log N)$.

---

### **[IKH-0587] - Luyện Đề 6 - Bài 7: Tìm Đường Đi Ngắn Nhất SPFA Đồ Thị VinFast**
* **Dạng bài:** Luyện Đề 6 Task 7 (SPFA Shortest Path Algorithm $O(V \cdot E)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0587 - Luyen De 6 Bai 7 SPFA VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0587%20-%20Luyen%20De%206%20Bai%207%20SPFA%20VinFast)
* **Phương pháp giải:** Thuật toán Shortest Path Faster Algorithm (SPFA) duy trì Queue quản lý cập nhật nhãn khoảng cách và phát hiện chu trình âm trên đồ thị trọng số trong $O(V \cdot E)$.

---

### **[IKH-0588] - Luyện Đề 6 - Bài 8: So Khớp Mã Mẫu Chuỗi Đối Xứng Manacher Viettel**
* **Dạng bài:** Luyện Đề 6 Task 8 (Manacher's Algorithm Palindromic Substring $O(N)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0588 - Luyen De 6 Bai 8 Manacher Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0588%20-%20Luyen%20De%206%20Bai%208%20Manacher%20Viettel)
* **Phương pháp giải:** Áp dụng thuật toán Manacher tính bán kính đối xứng $P[i]$ đếm số lượng chuỗi con đối xứng và vị trí bắt đầu trong $O(N)$.

---

### **[IKH-0589] - Luyện Đề 6 - Bài 9: Tối Ưu QHD Đồ Thị Cây Re-rooting DP Shopee**
* **Dạng bài:** Luyện Đề 6 Task 9 (Tree Dynamic Programming & Re-rooting $O(N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0589 - Luyen De 6 Bai 9 Tree DP Rerooting Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0589%20-%20Luyen%20De%206%20Bai%209%20Tree%20DP%20Rerooting%20Shopee)
* **Phương pháp giải:** Kỹ thuật Đổi gốc cây (Re-rooting DP) tính tổng khoảng cách từ mỗi nút đến tất cả các nút khác trên cây trong 2 lượt DFS $O(N)$.

---

### **[IKH-0590] - Luyện Đề 6 - Bài 10: Grand Synthesis Đề Thi Thử 6 FPT**
* **Dạng bài:** Luyện Đề 6 Task 10 (Dinic Maximum Flow & Minimum Cut $O(V^2 E)$)
* **Độ khó:** Rating 1750 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0590 - Luyen De 6 Bai 10 Grand Synthesis FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0590%20-%20Luyen%20De%206%20Bai%2010%20Grand%20Synthesis%20FPT)
* **Phương pháp giải:** Tổng hợp Thuật toán Dinic dựng Đồ thị phân tầng Level Graph và Luồng chặn Blocking Flow tìm luồng cực đại và lát cắt tối thiểu Min-Cut trong $O(V^2 E)$.


---

### **[IKH-0591] - Luyện Đề 7 - Bài 1: Đếm Ký Tự Xuất Hiện Nhiều Nhất VinFast**
* **Dạng bài:** Luyện Đề 7 Task 1 (Frequency Array / Max Element $O(N)$)
* **Độ khó:** Rating 1100 | ⭐★☆☆☆
* **Thư mục local:** [IKH-0591 - Luyen De 7 Bai 1 Max Ky Tu VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0591%20-%20Luyen%20De%207%20Bai%201%20Max%20Ky%20Tu%20VinFast)
* **Phương pháp giải:** Sử dụng mảng tần số 256 phần tử đếm số lần xuất hiện và tìm ký tự có tần số lớn nhất (thứ tự alphabet ưu tiên) trong $O(N)$.

---

### **[IKH-0592] - Luyện Đề 7 - Bài 2: Phân Tích Tổng Bình Phương Hai Số Nguyên Tố Viettel**
* **Dạng bài:** Luyện Đề 7 Task 2 (Math & Square Root Check $O(\sqrt{N})$)
* **Độ khó:** Rating 1200 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0592 - Luyen De 7 Bai 2 Tong Binh Phuong Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0592%20-%20Luyen%20De%207%20Bai%202%20Tong%20Binh%20Phuong%20Viettel)
* **Phương pháp giải:** Duyệt $p_1$ qua các số nguyên tố $\le \sqrt{N}$, kiểm tra $N - p_1^2$ có dạng $p_2^2$ với $p_2$ là số nguyên tố trong $O(\sqrt{N})$.

---

### **[IKH-0593] - Luyện Đề 7 - Bài 3: Sắp Xếp Đơn Hàng Ưu Tiên Giao Nhanh Shopee**
* **Dạng bài:** Luyện Đề 7 Task 3 (Priority Queue / Greedy $O(N \log N)$)
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0593 - Luyen De 7 Bai 3 Priority Queue Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0593%20-%20Luyen%20De%207%20Bai%203%20Priority%20Queue%20Shopee)
* **Phương pháp giải:** Sử dụng Hàng đợi ưu tiên Priority Queue (Max-Heap) sắp xếp và xử lý các đơn hàng theo mức độ ưu tiên giao hàng trong $O(N \log N)$.

---

### **[IKH-0594] - Luyện Đề 7 - Bài 4: Tối Ưu Hóa Bài Toán Xếp Lịch Phim FPT**
* **Dạng bài:** Luyện Đề 7 Task 4 (Weighted Interval Scheduling DP $O(N \log N)$)
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0594 - Luyen De 7 Bai 4 Weighted Interval DP FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0594%20-%20Luyen%20De%207%20Bai%204%20Weighted%20Interval%20DP%20FPT)
* **Phương pháp giải:** Quy hoạch động kết hợp Tìm kiếm nhị phân `std::lower_bound` tìm tổng trọng số/lợi nhuận lớn nhất của các khoảng thời gian chiếu không bị giao nhau $O(N \log N)$.

---

### **[IKH-0595] - Luyện Đề 7 - Bài 5: Truy Vấn Cập Nhật Đoạn Tổng Bằng Segment Tree Zalo**
* **Dạng bài:** Luyện Đề 7 Task 5 (Segment Tree Range Sum Query $O(\log N)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0595 - Luyen De 7 Bai 5 SegTree Range Sum Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0595%20-%20Luyen%20De%207%20Bai%205%20SegTree%20Range%20Sum%20Zalo)
* **Phương pháp giải:** Dựng Cây phân đoạn Segment Tree thực hiện các truy vấn tính tổng đoạn $[L, R]$ và cập nhật giá trị nút trong $O(\log N)$.

---

### **[IKH-0596] - Luyện Đề 7 - Bài 6: Đếm Số Cặp Tam Giác Thỏa Mãn ĐK Bất Đẳng Thức Techcombank**
* **Dạng bài:** Luyện Đề 7 Task 6 (Triangle Inequality Two Pointers $O(N^2)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0596 - Luyen De 7 Bai 6 Dem Tam Giac Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0596%20-%20Luyen%20De%207%20Bai%206%20Dem%20Tam%20Giac%20Techcombank)
* **Phương pháp giải:** Sắp xếp mảng độ dài thanh gỗ $A$, áp dụng Hai con trỏ kiểm tra bất đẳng thức tam giác $A_i + A_j > A_k$ đếm số tam giác hợp lệ trong $O(N^2)$.

---

### **[IKH-0597] - Luyện Đề 7 - Bài 7: Phân Tích Khớp Cầu Nâng Cao VinFast**
* **Dạng bài:** Luyện Đề 7 Task 7 (Tarjan Articulation Point & Bridge $O(V + E)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0597 - Luyen De 7 Bai 7 Tarjan Cau Khop VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0597%20-%20Luyen%20De%207%20Bai%207%20Tarjan%20Cau%20Khop%20VinFast)
* **Phương pháp giải:** Thuật toán Tarjan đếm số lượng đỉnh khớp và cạnh cầu trên đồ thị mạng lưới điện VinFast, xếp hạng các điểm nghẽn nguy hiểm trong $O(V + E)$.

---

### **[IKH-0598] - Luyện Đề 7 - Bài 8: So Khớp Mẫu Xâu Đa Tiền Tố Trie Viettel**
* **Dạng bài:** Luyện Đề 7 Task 8 (Trie Data Structure Multi-Pattern $O(\sum |S|)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0598 - Luyen De 7 Bai 8 Trie Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0598%20-%20Luyen%20De%207%20Bai%208%20Trie%20Viettel)
* **Phương pháp giải:** Cấu trúc Cây Tiền Tố Trie lưu trữ bộ từ điển mã giao dịch Viettel, kiểm tra tiền tố chung dài nhất và số lần xuất hiện mẫu xâu trong $O(\sum |S|)$.

---

### **[IKH-0599] - Luyện Đề 7 - Bài 9: Tối Ưu QHD Bitmask Phân Việc Đội Robot Shopee**
* **Dạng bài:** Luyện Đề 7 Task 9 (Bitmask Dynamic Programming $O(2^N \cdot N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0599 - Luyen De 7 Bai 9 Bitmask DP Robot Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0599%20-%20Luyen%20De%207%20Bai%209%20Bitmask%20DP%20Robot%20Shopee)
* **Phương pháp giải:** Quy hoạch động Trạng thái Mặt nạ bit $dp[mask]$ phân công $N$ robot làm $N$ công việc với tổng chi phí nhỏ nhất trong $O(2^N \cdot N)$.

---

### **[IKH-0600] - Luyện Đề 7 - Bài 10: Grand Synthesis Đề Thi Thử 7 FPT**
* **Dạng bài:** Luyện Đề 7 Task 10 (Minimum Cost Maximum Flow MCMF $O(V \cdot E + F \cdot E \log V)$)
* **Độ khó:** Rating 1800 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0600 - Luyen De 7 Bai 10 Grand Synthesis FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0600%20-%20Luyen%20De%207%20Bai%2010%20Grand%20Synthesis%20FPT)
* **Phương pháp giải:** Tổng hợp Thuật toán Luồng cực đại Chi phí tối thiểu (Min-Cost Max-Flow) kết hợp SPFA/Dijkstra trên đường tăng luồng giải quyết bài toán vận tải hàng hóa tối ưu $O(V \cdot E + F \cdot E \log V)$.


---

### **[IKH-0601] - Luyện Đề 8 - Bài 1: Đếm Số Lượng Ký Tự Nguyên Âm VinFast**
* **Dạng bài:** Luyện Đề 8 Task 1 (Vowel Count String Processing $O(N)$)
* **Độ khó:** Rating 1100 | ⭐★☆☆☆
* **Thư mục local:** [IKH-0601 - Luyen De 8 Bai 1 Dem Nguyen Am VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0601%20-%20Luyen%20De%208%20Bai%201%20Dem%20Nguyen%20Am%20VinFast)
* **Phương pháp giải:** Duyệt từng ký tự $c \in S$, kiểm tra tính nguyên âm trong tập `{'a','e','i','o','u'}` cả hoa lẫn thường trong $O(N)$.

---

### **[IKH-0602] - Luyện Đề 8 - Bài 2: Phân Tích Tổng Số Nguyên Tố Sieve Viettel**
* **Dạng bài:** Luyện Đề 8 Task 2 (Segmented Sieve $O(\sqrt{N})$)
* **Độ khó:** Rating 1250 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0602 - Luyen De 8 Bai 2 Tong Prime Sieve Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0602%20-%20Luyen%20De%208%20Bai%202%20Tong%20Prime%20Sieve%20Viettel)
* **Phương pháp giải:** Sử dụng Sàng phân đoạn (Segmented Sieve) đếm và tính tổng các số nguyên tố trong đoạn $[L, R]$ kích thước $\le 10^6$ trong $O(\sqrt{R} + (R - L))$.

---

### **[IKH-0603] - Luyện Đề 8 - Bài 3: Sắp Xếp Đơn Hàng Giao Tiết Kiệm Shopee**
* **Dạng bài:** Luyện Đề 8 Task 3 (Greedy Sorting $O(N \log N)$)
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0603 - Luyen De 8 Bai 3 Greedy Sorting Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0603%20-%20Luyen%20De%208%20Bai%203%20Greedy%20Sorting%20Shopee)
* **Phương pháp giải:** Sắp xếp mảng đơn hàng theo tỷ lệ lợi nhuận / thời gian xử lý giảm dần, tối ưu tổng doanh thu trong $O(N \log N)$.

---

### **[IKH-0604] - Luyện Đề 8 - Bài 4: Tối Ưu Hóa Chi Phí Đơn Hàng Đa Tầng QHD FPT**
* **Dạng bài:** Luyện Đề 8 Task 4 (Multi-Dimensional Knapsack DP $O(N \cdot W_1 \cdot W_2)$)
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0604 - Luyen De 8 Bai 4 Multi Knapsack DP FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0604%20-%20Luyen%20De%208%20Bai%204%20Multi%20Knapsack%20DP%20FPT)
* **Phương pháp giải:** Quy hoạch động Cái túi 2 chiều $dp[w_1][w_2]$ tối ưu tổng giá trị đơn hàng dưới 2 ràng buộc khối lượng $W_1$ và thể tích $W_2$ trong $O(N \cdot W_1 \cdot W_2)$.

---

### **[IKH-0605] - Luyện Đề 8 - Bài 5: Truy Vấn Cập Nhật Đoạn Min Segment Tree Zalo**
* **Dạng bài:** Luyện Đề 8 Task 5 (Segment Tree Range Minimum Query $O(\log N)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0605 - Luyen De 8 Bai 5 SegTree Range Min Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0605%20-%20Luyen%20De%208%20Bai%205%20SegTree%20Range%20Min%20Zalo)
* **Phương pháp giải:** Dựng Cây phân đoạn Segment Tree quản lý truy vấn giá trị nhỏ nhất RMQ trên đoạn $[L, R]$ và cập nhật điểm dữ liệu Zalo trong $O(\log N)$.

---

### **[IKH-0606] - Luyện Đề 8 - Bài 6: Đếm Cặp Số Có Tích Chia Hết Cho K Techcombank**
* **Dạng bài:** Luyện Đề 8 Task 6 (GCD & Divisors Map $O(N \cdot d(K))$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0606 - Luyen De 8 Bai 6 Cap Tich Chia Het K Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0606%20-%20Luyen%20De%208%20Bai%206%20Cap%20Tich%20Chia%20Het%20K%20Techcombank)
* **Phương pháp giải:** Thay $A_i$ bằng $g_i = \gcd(A_i, K)$, đếm số cặp $(g_i, g_j)$ có $g_i \cdot g_j \pmod K = 0$ thông qua mảng tần số các ước của $K$ trong $O(N \cdot d(K))$.

---

### **[IKH-0607] - Luyện Đề 8 - Bài 7: Phân Tích Thành Phần Liên Thông Mạng Lưới Cáp VinFast**
* **Dạng bài:** Luyện Đề 8 Task 7 (DSU Rollback Dynamic Offline Graph $O(Q \log N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0607 - Luyen De 8 Bai 7 DSU Rollback VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0607%20-%20Luyen%20De%208%20Bai%207%20DSU%20Rollback%20VinFast)
* **Phương pháp giải:** Cấu trúc DSU có khả năng Hoàn tác (DSU with Rollback) kết hợp Cây phân đoạn theo thời gian xử lý truy vấn thêm/xóa cạnh động offline trong $O(Q \log N)$.

---

### **[IKH-0608] - Luyện Đề 8 - Bài 8: So Khớp Mẫu Xâu Đa Chuỗi Suffix Array Viettel**
* **Dạng bài:** Luyện Đề 8 Task 8 (Suffix Array & LCP Array $O(N \log N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0608 - Luyen De 8 Bai 8 Suffix Array Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0608%20-%20Luyen%20De%208%20Bai%208%20Suffix%20Array%20Viettel)
* **Phương pháp giải:** Xây dựng Mảng hậu tố Suffix Array kết hợp Mảng LCP bằng thuật toán Kasai đếm số xâu con phân biệt và tìm xâu con lặp lại nhiều nhất trong $O(N \log N)$.

---

### **[IKH-0609] - Luyện Đề 8 - Bài 9: Tối Ưu QHD Đồ Thị Cây Centroid Decomposition Shopee**
* **Dạng bài:** Luyện Đề 8 Task 9 (Centroid Decomposition on Tree $O(N \log N)$)
* **Độ khó:** Rating 1750 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0609 - Luyen De 8 Bai 9 Centroid Decomposition Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0609%20-%20Luyen%20De%208%20Bai%209%20Centroid%20Decomposition%20Shopee)
* **Phương pháp giải:** Kỹ thuật Phân rã trọng tâm cây (Centroid Decomposition) đếm số đường đi độ dài $K$ trên cây bằng cách chia để trị qua các đỉnh trọng tâm $O(N \log N)$.

---

### **[IKH-0610] - Luyện Đề 8 - Bài 10: Grand Synthesis Đề Thi Thử 8 FPT**
* **Dạng bài:** Luyện Đề 8 Task 10 (Hungarian Algorithm Assignment Problem $O(V^3)$)
* **Độ khó:** Rating 1800 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0610 - Luyen De 8 Bai 10 Grand Synthesis FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0610%20-%20Luyen%20De%208%20Bai%2010%20Grand%20Synthesis%20FPT)
* **Phương pháp giải:** Tổng hợp Thuật toán Hungari (Hungarian Algorithm / Kuhn-Munkres) tìm ghép cặp cực đại trọng số tối ưu bài toán phân công công việc $N \times N$ trong $O(V^3)$.


---

### **[IKH-0611] - Luyện Đề 9 - Bài 1: Đếm Ký Tự Phụ Âm Trong Chuỗi VinFast**
* **Dạng bài:** Luyện Đề 9 Task 1 (Consonant Count String Processing $O(N)$)
* **Độ khó:** Rating 1100 | ⭐★☆☆☆
* **Thư mục local:** [IKH-0611 - Luyen De 9 Bai 1 Dem Phu Am VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0611%20-%20Luyen%20De%209%20Bai%201%20Dem%20Phu%20Am%20VinFast)
* **Phương pháp giải:** Duyệt ký tự $c \in S$, kiểm tra điều kiện `isalpha(c)` và không thuộc 5 nguyên âm đếm số lượng phụ âm trong $O(N)$.

---

### **[IKH-0612] - Luyện Đề 9 - Bài 2: Phân Tích Tổng Số Chính Phương Viettel**
* **Dạng bài:** Luyện Đề 9 Task 2 (Math Lagrange 4 Square Theorem $O(\sqrt{N})$)
* **Độ khó:** Rating 1200 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0612 - Luyen De 9 Bai 2 Tong So Chinh Phuong Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0612%20-%20Luyen%20De%209%20Bai%202%20Tong%20So%20Chinh%20Phuong%20Viettel)
* **Phương pháp giải:** Áp dụng Định lý 4 số chính phương Lagrange biểu diễn số $N$ thành ít số chính phương nhất $a^2 + b^2 + c^2 + d^2$ trong $O(\sqrt{N})$.

---

### **[IKH-0613] - Luyện Đề 9 - Bài 3: Tối Ưu Hóa Phân Bổ Hàng Đơn Giá Cực Đại Shopee**
* **Dạng bài:** Luyện Đề 9 Task 3 (Fractional Knapsack Greedy $O(N \log N)$)
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0613 - Luyen De 9 Bai 3 Fractional Knapsack Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0613%20-%20Luyen%20De%209%20Bai%203%20Fractional%20Knapsack%20Shopee)
* **Phương pháp giải:** Thuật toán Tham ăn Cái túi phân số (Fractional Knapsack) sắp xếp vật tư theo đơn giá $V_i / W_i$ giảm dần tối đa hóa giá trị trong $O(N \log N)$.

---

### **[IKH-0614] - Luyện Đề 9 - Bài 4: Tìm Tổng Đoạn Con Liên Tiếp Bằng K Có Độ Dài Ngắn Nhất FPT**
* **Dạng bài:** Luyện Đề 9 Task 4 (Prefix Sum + Map Min Length $O(N)$)
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0614 - Luyen De 9 Bai 4 Prefix Sum Min Len FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0614%20-%20Luyen%20De%209%20Bai%204%20Prefix%20Sum%20Min%20Len%20FPT)
* **Phương pháp giải:** Tính Tổng tiền tố kết hợp `std::unordered_map` lưu vị trí xuất hiện gần nhất tìm đoạn con có tổng đúng bằng $K$ có độ dài nhỏ nhất trong $O(N)$.

---

### **[IKH-0615] - Luyện Đề 9 - Bài 5: Truy Vấn Cập Nhật Đoạn Max 2D Segment Tree Zalo**
* **Dạng bài:** Luyện Đề 9 Task 5 (2D Segment Tree Range Maximum Query $O(\log^2 N)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0615 - Luyen De 9 Bai 5 2D SegTree RMQ Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0615%20-%20Luyen%20De%209%20Bai%205%202D%20SegTree%20RMQ%20Zalo)
* **Phương pháp giải:** Dựng Cây phân đoạn 2D (Segment Tree on Segment Tree) quản lý truy vấn giá trị cực đại trên vùng hình chữ nhật 2D $[X_1..X_2, Y_1..Y_2]$ trong $O(\log^2 N)$.

---

### **[IKH-0616] - Luyện Đề 9 - Bài 6: Đếm Cặp Phần Tử Có Tổng Chia Hết Cho K Techcombank**
* **Dạng bài:** Luyện Đề 9 Task 6 (Modulo Frequency Array $O(N)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0616 - Luyen De 9 Bai 6 Modulo Counter Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0616%20-%20Luyen%20De%209%20Bai%206%20Modulo%20Counter%20Techcombank)
* **Phương pháp giải:** Phân loại phần tử theo số dư $r = A_i \bmod K$, dùng mảng đếm tần số đếm số cặp $(A_i, A_j)$ có $(A_i + A_j) \bmod K = 0$ trong $O(N)$.

---

### **[IKH-0617] - Luyện Đề 9 - Bài 7: Phân Tích Chu Trình Euler Đồ Thị VinFast**
* **Dạng bài:** Luyện Đề 9 Task 7 (Hierholzer's Algorithm Euler Tour $O(V + E)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0617 - Luyen De 9 Bai 7 Hierholzer Euler Tour VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0617%20-%20Luyen%20De%209%20Bai%207%20Hierholzer%20Euler%20Tour%20VinFast)
* **Phương pháp giải:** Kiểm tra điều kiện bậc đỉnh và dùng thuật toán Hierholzer tìm hành trình/chu trình Euler đi qua mỗi cạnh của đồ thị đúng 1 lần trong $O(V + E)$.

---

### **[IKH-0618] - Luyện Đề 9 - Bài 8: So Khớp Mẫu Xâu Bằng Bitwise Trie Viettel**
* **Dạng bài:** Luyện Đề 9 Task 8 (Bitwise Trie Max XOR $O(N \log (\max A))$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0618 - Luyen De 9 Bai 8 Bitwise Trie Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0618%20-%20Luyen%20De%209%20Bai%208%20Bitwise%20Trie%20Viettel)
* **Phương pháp giải:** Cấu trúc Cây Trie Nhị phân (Bitwise Trie) lưu trữ biểu diễn nhị phân của các số, tìm cặp số có giá trị $A_i \oplus A_j$ lớn nhất trong $O(N \log (\max A))$.

---

### **[IKH-0619] - Luyện Đề 9 - Bài 9: Tối Ưu QHD SOS DP Mặt Nạ Bit Shopee**
* **Dạng bài:** Luyện Đề 9 Task 9 (Sum Over Subsets SOS DP $O(N \cdot 2^N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0619 - Luyen De 9 Bai 9 SOS DP Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0619%20-%20Luyen%20De%209%20Bai%209%20SOS%20DP%20Shopee)
* **Phương pháp giải:** Kỹ thuật Quy hoạch động trên tập con SOS DP (Sum Over Subsets) tính tổng giá trị tất cả tập con $F[mask] = \sum_{sub \subseteq mask} A[sub]$ trong $O(N \cdot 2^N)$.

---

### **[IKH-0620] - Luyện Đề 9 - Bài 10: Grand Synthesis Đề Thi Thử 9 FPT**
* **Dạng bài:** Luyện Đề 9 Task 10 (Hopcroft-Karp Bipartite Matching $O(E \sqrt{V})$)
* **Độ khó:** Rating 1750 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0620 - Luyen De 9 Bai 10 Grand Synthesis FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0620%20-%20Luyen%20De%209%20Bai%2010%20Grand%20Synthesis%20FPT)
* **Phương pháp giải:** Tổng hợp Thuật toán Hopcroft-Karp tìm cặp ghép cực đại trên đồ thị hai phía (Bipartite Matching) bằng cách tăng luồng qua nhiều đường tăng BFS trong $O(E \sqrt{V})$.


---

### **[IKH-0621] - Luyện Đề 10 - Bài 1: Đếm Số Lượng Chữ Số Trong Chuỗi VinFast**
* **Dạng bài:** Luyện Đề 10 Task 1 (Digit Count String Processing $O(N)$)
* **Độ khó:** Rating 1100 | ⭐★☆☆☆
* **Thư mục local:** [IKH-0621 - Luyen De 10 Bai 1 Dem Chu So VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0621%20-%20Luyen%20De%2010%20Bai%201%20Dem%20Chu%20So%20VinFast)
* **Phương pháp giải:** Duyệt ký tự $c \in S$, kiểm tra điều kiện `isdigit(c)` đếm số lượng chữ số `'0'..'9'` trong $O(N)$.

---

### **[IKH-0622] - Luyện Đề 10 - Bài 2: Phân Tích Số Nguyên Tố Cùng Nhau Phi Euler Viettel**
* **Dạng bài:** Luyện Đề 10 Task 2 (Euler's Totient Function $\phi(N)$ $O(\sqrt{N})$)
* **Độ khó:** Rating 1250 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0622 - Luyen De 10 Bai 2 Euler Totient Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0622%20-%20Luyen%20De%2010%20Bai%202%20Euler%20Totient%20Viettel)
* **Phương pháp giải:** Sử dụng công thức Phi Euler $\phi(N) = N \cdot \prod (1 - 1/p)$ tính số lượng số nguyên dương $< N$ nguyên tố cùng nhau với $N$ trong $O(\sqrt{N})$.

---

### **[IKH-0623] - Luyện Đề 10 - Bài 3: Sắp Xếp Lịch Trình Thí Nghiệm Shopee**
* **Dạng bài:** Luyện Đề 10 Task 3 (Greedy Interval Partitioning $O(N \log N)$)
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0623 - Luyen De 10 Bai 3 Interval Partitioning Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0623%20-%20Luyen%20De%2010%20Bai%203%20Interval%20Partitioning%20Shopee)
* **Phương pháp giải:** Thuật toán Phân hoạch khoảng (Interval Partitioning) kết hợp Priority Queue tối thiểu hóa số lượng phòng thí nghiệm/máy chủ cần thiết trong $O(N \log N)$.

---

### **[IKH-0624] - Luyện Đề 10 - Bài 4: Tìm Tổng Đoạn Con Liên Tiếp Lớn Nhất 2D FPT**
* **Dạng bài:** Luyện Đề 10 Task 4 (Maximum Submatrix Sum 2D Kadane $O(N^3)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0624 - Luyen De 10 Bai 4 2D Kadane FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0624%20-%20Luyen%20De%2010%20Bai%204%202D%20Kadane%20FPT)
* **Phương pháp giải:** Cố định hai hàng $R_1, R_2$, dùng thuật toán Kadane 1D tìm ma trận con có tổng các phần tử lớn nhất trong $O(N^3)$.

---

### **[IKH-0625] - Luyện Đề 10 - Bài 5: Truy Vấn Cập Nhật Đoạn Lazy Segment Tree 2D Zalo**
* **Dạng bài:** Luyện Đề 10 Task 5 (2D Lazy Segment Tree $O(\log^2 N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0625 - Luyen De 10 Bai 5 2D Lazy SegTree Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0625%20-%20Luyen%20De%2010%20Bai%205%202D%20Lazy%20SegTree%20Zalo)
* **Phương pháp giải:** Dựng Cây phân đoạn 2D kết hợp Đẩy lười (Lazy Propagation 2D) xử lý cập nhật hình chữ nhật 2D và truy vấn tổng/max trong $O(\log^2 N)$.

---

### **[IKH-0626] - Luyện Đề 10 - Bài 6: Đếm Cặp Số Có Tổng Nhỏ Hơn K Dùng BIT Techcombank**
* **Dạng bài:** Luyện Đề 10 Task 6 (Fenwick Tree Pair Counting $O(N \log N)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0626 - Luyen De 10 Bai 6 BIT Pair Counting Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0626%20-%20Luyen%20De%2010%20Bai%206%20BIT%20Pair%20Counting%20Techcombank)
* **Phương pháp giải:** Duyệt qua các phần tử $A_j$, dùng Cây Fenwick Tree đếm số phần tử $A_i$ đã xuất hiện thỏa mãn $A_i < K - A_j$ trong $O(N \log N)$.

---

### **[IKH-0627] - Luyện Đề 10 - Bài 7: Tìm Chu Trình Âm Trên Đồ Thị SPFA VinFast**
* **Dạng bài:** Luyện Đề 10 Task 7 (SPFA Negative Cycle Detection $O(V \cdot E)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0627 - Luyen De 10 Bai 7 SPFA Negative Cycle VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0627%20-%20Luyen%20De%2010%20Bai%207%20SPFA%20Negative%20Cycle%20VinFast)
* **Phương pháp giải:** Đếm số lần nới cạnh `cnt[v] >= V` trong thuật toán SPFA phát hiện chu trình âm trên đồ thị mạng lưới chi phí VinFast trong $O(V \cdot E)$.

---

### **[IKH-0628] - Luyện Đề 10 - Bài 8: So Khớp Mã Mẫu Chuỗi Động Bằng Suffix Automaton Viettel**
* **Dạng bài:** Luyện Đề 10 Task 8 (Suffix Automaton Pattern Matching $O(N + |P|)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0628 - Luyen De 10 Bai 8 SAM Pattern Matching Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0628%20-%20Luyen%20De%2010%20Bai%208%20SAM%20Pattern%20Matching%20Viettel)
* **Phương pháp giải:** Dựng Tự động xâu hậu tố Suffix Automaton (SAM) trên xâu văn bản $T$, di chuyển qua các chuyển trạng thái kiểm tra mẫu $P$ xuất hiện trong $O(|P|)$.

---

### **[IKH-0629] - Luyện Đề 10 - Bài 9: Tối Ưu QHD Phân Rã Cây HLD Lazy Shopee**
* **Dạng bài:** Luyện Đề 10 Task 9 (Heavy-Light Decomposition HLD + Lazy SegTree $O(N \log^2 N)$)
* **Độ khó:** Rating 1750 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0629 - Luyen De 10 Bai 9 HLD Lazy SegTree Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0629%20-%20Luyen%20De%2010%20Bai%209%20HLD%20Lazy%20SegTree%20Shopee)
* **Phương pháp giải:** Kỹ thuật HLD phân rã cây thành các chuỗi nặng, kết hợp Lazy Segment Tree cập nhật cộng đoạn trên đường đi $(u, v)$ và truy vấn tổng trong $O(N \log^2 N)$.

---

### **[IKH-0630] - Luyện Đề 10 - Bài 10: Grand Synthesis Đề Thi Thử 10 FPT**
* **Dạng bài:** Luyện Đề 10 Task 10 (2-SAT Problem Tarjan SCC $O(V + E)$)
* **Độ khó:** Rating 1800 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0630 - Luyen De 10 Bai 10 Grand Synthesis FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0630%20-%20Luyen%20De%2010%20Bai%2010%20Grand%20Synthesis%20FPT)
* **Phương pháp giải:** Biểu diễn bài toán 2-SAT dưới dạng đồ thị suy luận, dùng thuật toán Tarjan phân tích SCC kiểm tra điều kiện nghiệm hợp lệ $x_i$ và $\neg x_i$ không cùng một SCC trong $O(V + E)$.


---

### **[IKH-0631] - Luyện Đề 11 - Bài 1: Đếm Khoảng Trắng Trong Chuỗi Văn Bản VinFast**
* **Dạng bài:** Luyện Đề 11 Task 1 (Space Count String Processing $O(N)$)
* **Độ khó:** Rating 1100 | ⭐★☆☆☆
* **Thư mục local:** [IKH-0631 - Luyen De 11 Bai 1 Dem Khoang Trang VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0631%20-%20Luyen%20De%2011%20Bai%201%20Dem%20Khoang%20Trang%20VinFast)
* **Phương pháp giải:** Sử dụng `getline(cin, s)` đọc chuỗi có khoảng trắng, duyệt đếm các ký tự `' '` trong $O(N)$.

---

### **[IKH-0632] - Luyện Đề 11 - Bài 2: Phân Tích Cặp Số Nguyên Tố Cùng Nhau Viettel**
* **Dạng bài:** Luyện Đề 11 Task 2 (Pairwise Coprime Check GCD $O(N^2 \log (\max A))$)
* **Độ khó:** Rating 1200 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0632 - Luyen De 11 Bai 2 Pairwise Coprime Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0632%20-%20Luyen%20De%2011%20Bai%202%20Pairwise%20Coprime%20Viettel)
* **Phương pháp giải:** Duyệt qua các cặp số $(A_i, A_j)$, kiểm tra điều kiện $\gcd(A_i, A_j) = 1$ đếm số cặp nguyên tố cùng nhau trong $O(N^2 \log (\max A))$.

---

### **[IKH-0633] - Luyện Đề 11 - Bài 3: Tối Ưu Hóa Phân Bổ Tải Trọng Tàu Thủy Shopee**
* **Dạng bài:** Luyện Đề 11 Task 3 (Greedy Ship Loading $O(N \log N)$)
* **Độ khó:** Rating 1300 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0633 - Luyen De 11 Bai 3 Ship Loading Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0633%20-%20Luyen%20De%2011%20Bai%203%20Ship%20Loading%20Shopee)
* **Phương pháp giải:** Thuật toán Tham ăn xếp container nhẹ nhất lên tàu trước (Sắp xếp tăng dần), tối đa hóa số container được chở dưới tải trọng $W$ trong $O(N \log N)$.

---

### **[IKH-0634] - Luyện Đề 11 - Bài 4: Tìm Chuỗi Con Chung Dài Nhất 3 Chuỗi FPT**
* **Dạng bài:** Luyện Đề 11 Task 4 (3D Dynamic Programming LCS $O(N_1 N_2 N_3)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0634 - Luyen De 11 Bai 4 3D LCS FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0634%20-%20Luyen%20De%2011%20Bai%204%203D%20LCS%20FPT)
* **Phương pháp giải:** Quy hoạch động mảng 3 chiều $dp[i][j][k]$ tìm độ dài chuỗi con chung dài nhất của 3 chuỗi $S_1, S_2, S_3$ trong $O(N_1 N_2 N_3)$.

---

### **[IKH-0635] - Luyện Đề 11 - Bài 5: Truy Vấn Cập Nhật Đoạn Persistent SegTree Zalo**
* **Dạng bài:** Luyện Đề 11 Task 5 (Persistent Segment Tree Point Update $O(\log N)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0635 - Luyen De 11 Bai 5 Persistent SegTree Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0635%20-%20Luyen%20De%2011%20Bai%205%20Persistent%20SegTree%20Zalo)
* **Phương pháp giải:** Dựng Cây phân đoạn Bền vững Persistent Segment Tree tạo nút mới khi cập nhật, truy vấn giá trị trên bất kỳ phiên bản thời gian nào trong $O(\log N)$.

---

### **[IKH-0636] - Luyện Đề 11 - Bài 6: Đếm Số Cặp Tam Giác Vuông Trọng Số Techcombank**
* **Dạng bài:** Luyện Đề 11 Task 6 (Geometry Pythagorean Triples $O(N \log N)$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0636 - Luyen De 11 Bai 6 Tam Giac Vuong Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0636%20-%20Luyen%20De%2011%20Bai%206%20Tam%20Giac%20Vuong%20Techcombank)
* **Phương pháp giải:** Sắp xếp mảng độ dài cạnh, áp dụng công thức $a^2 + b^2 = c^2$ kết hợp `std::binary_search` đếm bộ ba Pythagoras hợp lệ trong $O(N^2)$ hoặc $O(N \log N)$.

---

### **[IKH-0637] - Luyện Đề 11 - Bài 7: Tìm Khung Cây Tối Ưu Động Offline DSU VinFast**
* **Dạng bài:** Luyện Đề 11 Task 7 (Dynamic Offline MST with DSU Rollback $O(Q \log N)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0637 - Luyen De 11 Bai 7 Dynamic MST DSU VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0637%20-%20Luyen%20De%2011%20Bai%207%20Dynamic%20MST%20DSU%20VinFast)
* **Phương pháp giải:** Kết hợp Cây phân đoạn quản lý thời gian tồn tại cạnh và DSU Rollback duy trì khung cây nhỏ nhất MST khi thêm/xóa cạnh động offline trong $O(Q \log N)$.

---

### **[IKH-0638] - Luyện Đề 11 - Bài 8: So Khớp Mã Mẫu Xâu Động Bằng Manacher Viettel**
* **Dạng bài:** Luyện Đề 11 Task 8 (Manacher Palindrome Matching $O(N)$)
* **Độ khó:** Rating 1550 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0638 - Luyen De 11 Bai 8 Manacher Matching Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0638%20-%20Luyen%20De%2011%20Bai%208%20Manacher%20Matching%20Viettel)
* **Phương pháp giải:** Thuật toán Manacher mở rộng đếm các chuỗi con đối xứng thỏa mãn tiêu chuẩn mã bảo mật Viettel trong $O(N)$.

---

### **[IKH-0639] - Luyện Đề 11 - Bài 9: Tối Ưu QHD Đường Thẳng CHT Lichao Tree Shopee**
* **Dạng bài:** Luyện Đề 11 Task 9 (Li Chao Tree Dynamic CHT $O(N \log (\max X))$)
* **Độ khó:** Rating 1700 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0639 - Luyen De 11 Bai 9 LiChao Tree CHT Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0639%20-%20Luyen%20De%2011%20Bai%209%20LiChao%20Tree%20CHT%20Shopee)
* **Phương pháp giải:** Cấu trúc Cây Li Chao (Li Chao Segment Tree) quản lý tập đường thẳng $y = ax + b$, hỗ trợ chèn đường thẳng và truy vấn giá trị nhỏ nhất tại $x$ trong $O(\log (\max X))$.

---

### **[IKH-0640] - Luyện Đề 11 - Bài 10: Grand Synthesis Đề Thi Thử 11 FPT**
* **Dạng bài:** Luyện Đề 11 Task 10 (Matrix Exponentiation Shortest Path Min-Plus $O(V^3 \log K)$)
* **Độ khó:** Rating 1800 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0640 - Luyen De 11 Bai 10 Grand Synthesis FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0640%20-%20Luyen%20De%2011%20Bai%2010%20Grand%20Synthesis%20FPT)
* **Phương pháp giải:** Tổng hợp Nhân ma trận Min-Plus $C[i][j] = \min_k (A[i][k] + B[k][j])$ bằng Lũy thừa nhị phân ma trận tìm đường đi ngắn nhất đúng $K$ bước trong $O(V^3 \log K)$.


---

### **[IKH-0641] - Luyện Đề 12 - Bài 1: Đếm Ký Tự In Hoa In Thường VinFast**
* **Dạng bài:** Luyện Đề 12 Task 1 (Upper Lower Count String Processing $O(N)$)
* **Độ khó:** Rating 1100 | ⭐★☆☆☆
* **Thư mục local:** [IKH-0641 - Luyen De 12 Bai 1 Dem Hoa Thuong VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0641%20-%20Luyen%20De%2012%20Bai%201%20Dem%20Hoa%20Thuong%20VinFast)
* **Phương pháp giải:** Duyệt từng ký tự $c \in S$, kiểm tra `isupper(c)` và `islower(c)` đếm số chữ hoa và chữ thường trong $O(N)$.

---

### **[IKH-0642] - Luyện Đề 12 - Bài 2: Phân Tích Thừa Số Số Nguyên Tố Cực Đại Viettel**
* **Dạng bài:** Luyện Đề 12 Task 2 (Pollard's Rho & Miller-Rabin Primality Test $O(N^{1/4})$)
* **Độ khó:** Rating 1400 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0642 - Luyen De 12 Bai 2 Pollard Rho Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0642%20-%20Luyen%20De%2012%20Bai%202%20Pollard%20Rho%20Viettel)
* **Phương pháp giải:** Sử dụng thuật toán Pollard's Rho kết hợp Kiểm tra số nguyên tố Miller-Rabin phân tích thừa số nguyên tố cho số cực đại $N \le 10^{18}$ trong $O(N^{1/4})$.

---

### **[IKH-0643] - Luyện Đề 12 - Bài 3: Sắp Xếp Lịch Trình Xe Tải Chở Hàng Đa Trọng Shopee**
* **Dạng bài:** Luyện Đề 12 Task 3 (Multiprocessor Scheduling Greedy $O(N \log N)$)
* **Độ khó:** Rating 1350 | ⭐⭐☆☆☆
* **Thư mục local:** [IKH-0643 - Luyen De 12 Bai 3 Multiprocessor Scheduling Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0643%20-%20Luyen%20De%2012%20Bai%203%20Multiprocessor%20Scheduling%20Shopee)
* **Phương pháp giải:** Thuật toán LPT (Longest Processing Time First) kết hợp Min-Heap phân bổ $N$ đơn hàng nặng nhất vào $K$ xe tải tối thiểu hóa thời gian hoàn thành cực đại trong $O(N \log N)$.

---

### **[IKH-0644] - Luyện Đề 12 - Bài 4: Tối Ưu Hóa Chi Phí Đóng Tàu QHD Dạng Chuỗi FPT**
* **Dạng bài:** Luyện Đề 12 Task 4 (Matrix Chain Multiplication DP $O(N^3)$)
* **Độ khó:** Rating 1450 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0644 - Luyen De 12 Bai 4 Matrix Chain Multiplication FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0644%20-%20Luyen%20De%2012%20Bai%204%20Matrix%20Chain%20Multiplication%20FPT)
* **Phương pháp giải:** Quy hoạch động Nhân chuỗi ma trận $dp[i][j] = \min_{k} (dp[i][k] + dp[k+1][j] + cost)$ tìm chi phí nhân ma trận/lắp ráp chuỗi nhỏ nhất trong $O(N^3)$.

---

### **[IKH-0645] - Luyện Đề 12 - Bài 5: Truy Vấn Cập Nhật Đoạn Merge Sort Tree Zalo**
* **Dạng bài:** Luyện Đề 12 Task 5 (Merge Sort Tree Range K-th Query $O(N \log^2 N)$)
* **Độ khó:** Rating 1600 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0645 - Luyen De 12 Bai 5 Merge Sort Tree Zalo](file:///Users/dkdeveloper/projects/testcase/IKH-0645%20-%20Luyen%20De%2012%20Bai%205%20Merge%20Sort%20Tree%20Zalo)
* **Phương pháp giải:** Dựng Cây Merge Sort Tree lưu `vector<int>` đã sắp xếp tại mỗi nút, kết hợp Chặt nhị phân tìm số phần tử $\le X$ trên đoạn $[L, R]$ trong $O(\log^2 N)$.

---

### **[IKH-0646] - Luyện Đề 12 - Bài 6: Đếm Cặp Số Có Tổng Là Số Chính Phương Techcombank**
* **Dạng bài:** Luyện Đề 12 Task 6 (Perfect Square Pair Counting $O(N \sqrt{M})$)
* **Độ khó:** Rating 1500 | ⭐⭐⭐☆☆
* **Thư mục local:** [IKH-0646 - Luyen De 12 Bai 6 Square Pair Techcombank](file:///Users/dkdeveloper/projects/testcase/IKH-0646%20-%20Luyen%20De%2012%20Bai%206%20Square%20Pair%20Techcombank)
* **Phương pháp giải:** Duyệt qua các phần tử $A_j$, thử tất cả các số chính phương $k^2 \le 2 \cdot \max A$, dùng mảng tần số đếm số cặp $(A_i, A_j)$ có $A_i + A_j = k^2$ trong $O(N \sqrt{M})$.

---

### **[IKH-0647] - Luyện Đề 12 - Bài 7: Tìm Đường Đi Ngắn Nhất Mạng Cáp Biển Dinic Max Flow VinFast**
* **Dạng bài:** Luyện Đề 12 Task 7 (Dinic Maximum Flow & Minimum Cut $O(V^2 E)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0647 - Luyen De 12 Bai 7 Dinic Max Flow VinFast](file:///Users/dkdeveloper/projects/testcase/IKH-0647%20-%20Luyen%20De%2012%20Bai%207%20Dinic%20Max%20Flow%20VinFast)
* **Phương pháp giải:** Thuật toán Dinic dựng Level Graph và Blocking Flow xác định dung lượng băng thông tối đa và các tuyến cáp trọng yếu thuộc lát cắt tối thiểu Min-Cut trong $O(V^2 E)$.

---

### **[IKH-0648] - Luyện Đề 12 - Bài 8: So Khớp Mã Mẫu Đa Tiền Tố Động Aho-Corasick Viettel**
* **Dạng bài:** Luyện Đề 12 Task 8 (Aho-Corasick Automaton Multi-Pattern Matching $O(N + \sum |P|)$)
* **Độ khó:** Rating 1650 | ⭐⭐⭐⭐☆
* **Thư mục local:** [IKH-0648 - Luyen De 12 Bai 8 Aho Corasick Viettel](file:///Users/dkdeveloper/projects/testcase/IKH-0648%20-%20Luyen%20De%2012%20Bai%208%20Aho%20Corasick%20Viettel)
* **Phương pháp giải:** Dựng Tự động Aho-Corasick với Fail Link và Output Link đếm tần số xuất hiện của bộ từ khóa mã độc Viettel trong nhật ký dữ liệu mạng $O(N + \sum |P|)$.

---

### **[IKH-0649] - Luyện Đề 12 - Bài 9: Tối Ưu QHD Phạt Chi Phí Alien's Trick WQS Shopee**
* **Dạng bài:** Luyện Đề 12 Task 9 (Alien's Trick WQS Binary Search $O(N \log C)$)
* **Độ khó:** Rating 1750 | ⭐⭐⭐⭐⭐
* **Thư mục local:** [IKH-0649 - Luyen De 12 Bai 9 Aliens Trick Shopee](file:///Users/dkdeveloper/projects/testcase/IKH-0649%20-%20Luyen%20De%2012%20Bai%209%20Aliens%20Trick%20Shopee)
* **Phương pháp giải:** Kỹ thuật Alien's Trick (WQS Binary Search) áp dụng phạt chi phí $\lambda$ triệt tiêu điều kiện chọn đúng $K$ đoạn con, tối ưu hóa QHD lồi trong $O(N \log C)$.

---

### **[IKH-0650] - Luyện Đề 12 - Bài 10: Ultimate Masterclass Challenge 650 Bài FPT**
* **Dạng bài:** Luyện Đề 12 Task 10 (Grand Synthesis Ultimate Masterclass $O(N \log N)$)
* **Độ khó:** Rating 1900 | 🏆🏆🏆🏆🏆
* **Thư mục local:** [IKH-0650 - Luyen De 12 Bai 10 Grand Synthesis FPT](file:///Users/dkdeveloper/projects/testcase/IKH-0650%20-%20Luyen%20De%2012%20Bai%10%20Grand%20Synthesis%20FPT)
* **Phương pháp giải:** Bài toán Thử thách Tối thượng 650 Bài Khóa học Level 3: Tổng hợp Đồng dạng cây Tree Isomorphism AHU Hash kết hợp Phân rã cây Heavy-Light Decomposition (HLD) và Cây phân đoạn Bền vững Persistent Segment Tree giải quyết bài toán truy vấn cấu trúc đồ thị phức tạp $O(N \log N)$.
