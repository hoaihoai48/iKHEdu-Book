# TÀI LIỆU GỐC — KHUNG TOÀN BỘ 21 CHƯƠNG

## Vai trò tài liệu

Đây là tài liệu gốc để thiết kế và review khung nội dung của Phần II — Thuật toán nền tảng. Tài liệu này được lập trước khi viết sâu từng chương. Mỗi chương mới dừng ở mức **outline có thể review**, chưa phải bài giảng hoàn chỉnh và chưa được xem là print-ready.

Khi một chương được chọn để viết sâu, nội dung phải được phát triển tại tài liệu source riêng của chương, review theo quy trình source-first, rồi mới đồng bộ phần học sinh sang `BOOK_MASTER.md`. Không tạo source riêng cho từng chương trong giai đoạn dựng khung nếu chưa cần thiết.

## Nguyên tắc chung

Khung 21 chương phải giữ được ba điều. Thứ nhất, roadmap chỉ cho biết phạm vi chủ đề; nó không tự quyết định thứ tự dạy. Thứ hai, mỗi chương phải đi theo cùng một logic nhận thức nhưng không bị ép có cùng số lượng Bài. Thứ ba, mọi chương đều phải quay về DNA của sách:

```text
Mục tiêu → Ôn nhanh → Vấn đề → Ý tưởng → Mô phỏng
→ Code → Bài tập phân tầng → Lỗi thường gặp
→ Tự kiểm tra → Tóm tắt → Sẽ dùng về sau
```

Phần I là lớp nền tảng tra cứu. Học sinh được nhắc lại kiến thức cần thiết ngay trong từng chương, không bị yêu cầu học xong một khóa nền tảng dài trước khi bắt đầu thuật toán.

## Bản đồ toàn bộ 21 chương

| Chương | Chủ đề | Trọng tâm năng lực | Prerequisite chính | Mức khung hiện tại |
|---:|---|---|---|---|
| 1 | Sắp xếp | Dùng thứ tự để đơn giản hóa bài toán | Mảng, vòng lặp, so sánh | Đã có source sâu |
| 2 | Tham lam | Chọn cục bộ có căn cứ và bảo vệ lựa chọn | Sắp xếp, comparator, vòng lặp | Đã có source sâu |
| 3 | Số học | Nhận ra tính chất ước, bội và số nguyên | Vòng lặp, `%`, hàm, `long long` | Outline |
| 4 | Đếm phân phối | Biến dữ liệu thành tần suất và nhóm | Mảng, vòng lặp, đếm | Outline |
| 5 | Tìm kiếm nhị phân | Tìm trong miền có tính đơn điệu | Sắp xếp, điều kiện, hàm `check` | Outline |
| 6 | Mảng tiền tố | Trả lời nhanh truy vấn trên đoạn | Mảng, tích lũy, chỉ số | Outline |
| 7 | Hai con trỏ | Thu hẹp hoặc mở rộng miền đang xét | Sắp xếp, điều kiện, tính đơn điệu | Outline |
| 8 | Xử lý xâu cơ bản | Duyệt và xây dựng xâu theo trạng thái | Vòng lặp, điều kiện, `string` | Outline |
| 9 | Đệ quy và chia để trị | Chia bài toán, giải phần con, ghép kết quả | Hàm, điều kiện dừng, complexity | Outline |
| 10 | Modulo | Tính với số lớn bằng phép chia dư | `%`, `long long`, lũy thừa | Outline |
| 11 | Tổ hợp cơ bản | Đếm lựa chọn có và không xét thứ tự | Đếm, mảng, modulo | Outline |
| 12 | STL C++ | Chọn công cụ lưu trữ và truy cập phù hợp | `vector`, vòng lặp, kiểu dữ liệu | Outline |
| 13 | Quy hoạch động cơ bản | Mô hình hóa trạng thái và chuyển trạng thái | Mảng, `max/min`, complexity | Outline |
| 14 | Đồ thị | Mô hình hóa quan hệ và duyệt trạng thái | `vector`, hàm, BFS/DFS cơ bản | Outline |
| 15 | Stack và Queue | Điều khiển thứ tự vào–ra của dữ liệu | Mảng, vòng lặp, STL nhập môn | Outline |
| 16 | Segment Tree | Truy vấn đoạn và cập nhật điểm | Mảng tiền tố, đệ quy, complexity | Outline |
| 17 | Digit DP | Đếm số theo trạng thái chữ số | DP, modulo, đệ quy, `string` | Outline |
| 18 | String Hashing | So sánh nhanh các đoạn xâu | `string`, tiền tố, modulo | Outline |
| 19 | Số nguyên lớn | Tính toán vượt miền kiểu chuẩn | Xâu, mảng chữ số, phép tính | Outline |
| 20 | Phép toán trên bit | Biểu diễn tập nhỏ bằng bitmask | Số nguyên, tập hợp nhỏ | Outline |
| 21 | Fenwick Tree | Cập nhật điểm và truy vấn tiền tố động | Mảng tiền tố, bit, complexity | Outline |

## Bản đồ prerequisite và teaching sequence

Roadmap giữ đủ 21 chủ đề nêu trên. Teaching sequence là thứ tự khuyến nghị cho lớp bắt đầu từ số 0, có thể điều chỉnh theo lớp học:

```text
Đếm và thống kê → Sắp xếp → Mảng tiền tố → Hai con trỏ → Tham lam
→ Tìm kiếm nhị phân → Xử lý xâu → Stack/Queue
→ Số học/Modulo → Đệ quy → Tổ hợp → Quy hoạch động
→ Đồ thị → Bitmask → STL nâng cao
→ Segment Tree, Digit DP, String Hashing, Số nguyên lớn, Fenwick Tree
```

Các chương vẫn giữ số thứ tự theo bản đồ sách. Giáo viên có thể dạy Chương 2 sau Chương 1 hoặc chuyển nó tới vị trí phù hợp trong teaching sequence, miễn prerequisite của lớp được bảo đảm.

## Phần I — Nền tảng lập trình

Phần I không phải một khóa học dài độc lập. Đây là lớp tra cứu gồm sáu mục: chương trình và Input–Process–Output; dữ liệu, biến và phép tính; điều kiện và vòng lặp; pattern xử lý dữ liệu; hàm, debug và độ phức tạp; bảng tra cứu nhanh.

Cuối Phần I cần có checklist sẵn sàng gồm: đọc Input, viết Output, chọn kiểu dữ liệu, viết điều kiện/vòng lặp, duyệt mảng, tính tổng/đếm/max/min, tìm kiếm tuyến tính, viết hàm đơn giản, test case, edge case, đọc lỗi cơ bản và nhận biết `O(1)`, `O(N)`, `O(N²)`, `O(N log N)`.

# Khung chi tiết từng chương

## Chương 1 — Sắp xếp

**Vai trò:** Chương mẫu đã được viết sâu. Học sinh đi từ sắp xếp bằng tay đến Selection Sort, `sort`, comparator, tiền xử lý, complexity và bài chuyển giao.

**Cấu trúc đã chốt:** Bài 1.1–1.7, Tổng kết chương và Code tham chiếu. Chương này là mẫu logic, không phải khuôn bắt buộc về số lượng Bài cho các chương sau.

## Chương 2 — Tham lam

**Vai trò:** Chương source-first đã được tự review và chốt ở mức nội dung. Bài toán trung tâm là chọn nhiều hoạt động không giao nhau; học sinh học tiêu chí kết thúc sớm, mô phỏng, code, lập luận đổi chỗ và phản ví dụ.

**Cấu trúc đã chốt:** Bài 2.1–2.6, Tổng kết chương và Code tham chiếu. `pair` chỉ là representation ngoại lệ có lý do khi cần giữ `start` và `finish` cùng nhau.

## Chương 3 — Số học

**Vai trò:** Cung cấp công cụ số học dùng lặp lại trong nhiều chương sau.

**Prerequisite:** Vòng lặp, điều kiện, `%`, hàm, `long long` và cách kiểm tra trường hợp `0`, `1`, số âm.

**Bài dự kiến:**

1. Ước, bội và cách liệt kê ước.
2. GCD bằng thuật toán Euclid và mở rộng cho nhiều số.
3. LCM an toàn, chia trước khi nhân và kiểm soát tràn số.
4. Số nguyên tố, phân tích thừa số nhỏ và tối ưu thử ước.
5. Bài tập phân tầng và chọn công cụ số học.

**Bài tập khung:** Tầng A đếm ước/GCD; Tầng B kiểm tra nguyên tố và LCM; Tầng C phân tích thừa số hoặc kết hợp nhiều tính chất.

**Lỗi cần kiểm soát:** Nhầm ước với bội, xử lý sai `0` và `1`, nhân trước khi chia trong LCM, bỏ qua số âm và dùng kiểu quá nhỏ.

**Sẽ dùng về sau:** Modulo, tổ hợp, số nguyên lớn và các bài kiểm tra tính chất số.

## Chương 4 — Đếm phân phối

**Vai trò:** Dạy học sinh thay việc so sánh nhiều cặp bằng việc đếm tần suất và nhìn dữ liệu theo nhóm.

**Prerequisite:** Mảng, `vector`, vòng lặp, điều kiện, tích lũy và miền giá trị nhỏ.

**Bài dự kiến:**

1. Tần suất là gì và cách lập bảng đếm.
2. Đếm giá trị trùng, nhóm đông nhất và phần tử xuất hiện đúng số lần.
3. Nguyên lý Dirichlet bằng ví dụ hộp và đồ vật.
4. Đếm cặp đơn giản bằng tần suất.
5. Bài tập phân tầng và giới hạn của bảng đếm.

**Bài tập khung:** Tầng A đếm trực tiếp; Tầng B tìm nhóm lớn nhất/giá trị thiếu; Tầng C đếm cặp hoặc phát hiện phân phối bắt buộc.

**Lỗi cần kiểm soát:** Kích thước bảng sai, nhầm giá trị với chỉ số, quên khởi tạo và dùng bảng đếm khi miền giá trị quá lớn.

**Sẽ dùng về sau:** Prefix Sum, Map và các bài đếm tổ hợp.

## Chương 5 — Tìm kiếm nhị phân

**Vai trò:** Hình thành tư duy tìm kiếm trên miền và nhận ra điều kiện đơn điệu.

**Prerequisite:** Sắp xếp, so sánh, hàm, biên trái/phải và complexity.

**Bài dự kiến:**

1. Tìm một phần tử trong dãy đã sắp xếp.
2. Tìm vị trí đầu tiên, cuối cùng hoặc cận.
3. Tìm đáp án nhỏ nhất/lớn nhất thỏa `check(x)`.
4. Thiết kế hàm kiểm tra và chứng minh tính đơn điệu.
5. Bài tập phân tầng và kiểm thử biên.

**Bài tập khung:** Tầng A tìm phần tử; Tầng B tìm cận và căn nguyên; Tầng C năng lực tối thiểu, tốc độ nhỏ nhất hoặc đáp án tối ưu.

**Lỗi cần kiểm soát:** Dùng khi không có tính đơn điệu, cập nhật biên sai, vòng lặp không kết thúc và tràn ở `left + right`.

**Sẽ dùng về sau:** Tối ưu đáp án, tìm kiếm trên số lớn và các bài kết hợp `check`.

## Chương 6 — Mảng tiền tố

**Vai trò:** Dạy cách tiền xử lý một dãy để trả lời nhiều truy vấn đoạn nhanh hơn.

**Prerequisite:** Mảng, chỉ số, tích lũy, `long long` và quy ước đoạn `[l, r]`.

**Bài dự kiến:**

1. Prefix Sum và công thức tổng đoạn.
2. Prefix Sum với điều kiện đếm.
3. Prefix XOR và khi phép XOR thay cho phép cộng.
4. Nhiều truy vấn đoạn và test chỉ số.
5. Bài tập phân tầng và giới hạn của dữ liệu tĩnh.

**Bài tập khung:** Tầng A tổng đoạn; Tầng B đếm/XOR đoạn; Tầng C nhiều truy vấn hoặc truy vấn hai chiều đơn giản.

**Lỗi cần kiểm soát:** Lệch chỉ số, quên `P[0] = 0`, dùng `int` cho tổng lớn và nhầm tiền tố tĩnh với dữ liệu có cập nhật.

**Sẽ dùng về sau:** Hai con trỏ, String Hashing, Fenwick Tree và truy vấn nhanh.

## Chương 7 — Hai con trỏ

**Vai trò:** Giúp học sinh duy trì một đoạn hoặc một cặp vị trí mà không duyệt lại dữ liệu không cần thiết.

**Prerequisite:** Sắp xếp, vòng lặp, điều kiện, Prefix Sum cơ bản và tính đơn điệu.

**Bài dự kiến:**

1. Hai con trỏ trên dãy đã sắp xếp.
2. Tìm hai số có tổng bằng `X`.
3. Sliding Window và duy trì đoạn hợp lệ.
4. Trộn hai dãy đã sắp xếp.
5. Bài tập phân tầng và nhận biết khi kỹ thuật không áp dụng được.

**Bài tập khung:** Tầng A tìm cặp; Tầng B đoạn dài nhất/ngắn nhất; Tầng C biến thể có điều kiện thay đổi.

**Lỗi cần kiểm soát:** Di chuyển sai con trỏ, dùng khi điều kiện không đơn điệu, quên đoạn rỗng và nhầm cửa sổ đóng/mở.

**Sẽ dùng về sau:** Tham lam, xử lý xâu và nhiều bài tối ưu tuyến tính.

## Chương 8 — Xử lý xâu cơ bản

**Vai trò:** Mở rộng tư duy duyệt mảng sang dãy ký tự và trạng thái văn bản đơn giản.

**Prerequisite:** Vòng lặp, điều kiện, chỉ số, `string` và xử lý Input có khoảng trắng.

**Bài dự kiến:**

1. Duyệt và đếm ký tự.
2. Chuẩn hóa chữ hoa/chữ thường khi đề yêu cầu.
3. Kiểm tra palindrome.
4. Tách từ và tìm đoạn liên tiếp.
5. Bài tập phân tầng về xâu rỗng, khoảng trắng và ký tự đặc biệt.

**Bài tập khung:** Tầng A đếm ký tự; Tầng B palindrome/đoạn dài nhất; Tầng C phân tích hoặc biến đổi xâu theo nhiều điều kiện.

**Lỗi cần kiểm soát:** Truy cập ngoài xâu, nhầm độ dài với chỉ số cuối, bỏ qua khoảng trắng và xử lý xâu rỗng sai.

**Sẽ dùng về sau:** String Hashing, số nguyên lớn và các bài chuỗi nâng cao.

## Chương 9 — Đệ quy và chia để trị

**Vai trò:** Dạy cách mô tả lời giải bằng bài toán nhỏ hơn và ghép kết quả.

**Prerequisite:** Hàm, điều kiện dừng, mảng, mô phỏng lời gọi và complexity.

**Bài dự kiến:**

1. Hàm đệ quy và điều kiện dừng.
2. Tổng, giai thừa và trạng thái giảm.
3. Tìm kiếm nhị phân dưới góc nhìn chia để trị.
4. Merge Sort: chia, giải và trộn.
5. Lũy thừa nhanh và phân tích số lần gọi.

**Bài tập khung:** Tầng A truy hồi đơn giản; Tầng B đệ quy trên dãy; Tầng C chia để trị có bước ghép kết quả.

**Lỗi cần kiểm soát:** Thiếu điều kiện dừng, trạng thái không nhỏ hơn, nhầm thứ tự ghép và dùng đệ quy khi vòng lặp đơn giản hơn.

**Sẽ dùng về sau:** Segment Tree, Digit DP và các cấu trúc cây.

## Chương 10 — Modulo

**Vai trò:** Hình thành kỹ năng tính toán với số lớn và giữ kết quả trong miền an toàn.

**Prerequisite:** `%`, `long long`, phép tính, lũy thừa và quy tắc số âm.

**Bài dự kiến:**

1. Ý nghĩa của phép chia dư.
2. Cộng, trừ và nhân modulo.
3. Lũy thừa nhanh modulo.
4. Chu kỳ, chữ số cuối và tổng theo modulo.
5. Bài tập phân tầng với số âm và kiểu dữ liệu.

**Bài tập khung:** Tầng A tính dư; Tầng B lũy thừa nhanh; Tầng C bài đếm hoặc công thức lớn lấy modulo.

**Lỗi cần kiểm soát:** Nhân gây tràn trước khi `%`, kết quả âm, nhầm `%` với phép chia và dùng mô-đun không phù hợp.

**Sẽ dùng về sau:** Tổ hợp, Digit DP, String Hashing và số nguyên lớn.

## Chương 11 — Tổ hợp cơ bản

**Vai trò:** Phân biệt các kiểu đếm và xây dựng công thức từ lựa chọn nhỏ hơn.

**Prerequisite:** Đếm, mảng, vòng lặp, modulo và đệ quy hoặc bảng động đơn giản.

**Bài dự kiến:**

1. Chọn, chỉnh hợp và hoán vị.
2. Tam giác Pascal.
3. Đường đi trên lưới chỉ sang phải/xuống.
4. Đếm nhóm và phân biệt có xét thứ tự.
5. Bài tập phân tầng và giới hạn công thức.

**Bài tập khung:** Tầng A chọn đội/vật; Tầng B Pascal và đường đi; Tầng C đếm kết hợp modulo ở giới hạn phù hợp.

**Lỗi cần kiểm soát:** Nhầm thứ tự, sai điều kiện `k > n`, đếm trùng và để tràn số.

**Sẽ dùng về sau:** DP, modulo nâng cao và các bài đếm cấu hình.

## Chương 12 — STL C++

**Vai trò:** Dạy học sinh chọn công cụ dữ liệu theo nhu cầu, không học STL như danh sách lệnh rời rạc.

**Prerequisite:** Kiểu dữ liệu, vòng lặp, `vector`, iterator và complexity cơ bản.

**Bài dự kiến:**

1. `vector` và thao tác dãy.
2. `set` cho giá trị phân biệt có thứ tự.
3. `map` cho ánh xạ và tần suất.
4. `stack`, `queue` và quy tắc vào–ra.
5. `pair` như công cụ dữ liệu mở rộng, sau khi học sinh đã vững kiểu cơ bản.
6. Chọn container theo thao tác cần nhanh.

**Bài tập khung:** Tầng A thao tác từng container; Tầng B đếm/loại trùng/mô phỏng; Tầng C chọn container cho bối cảnh mới và giải thích trade-off.

**Lỗi cần kiểm soát:** Chọn container theo thói quen, truy cập phần tử không tồn tại, nhầm `top/front` và quên chi phí thao tác.

**Sẽ dùng về sau:** Graph, Stack/Queue, Fenwick Tree và các bài cần cấu trúc dữ liệu.

## Chương 13 — Quy hoạch động cơ bản

**Vai trò:** Dạy học sinh biến các trạng thái lặp lại thành bảng kết quả được lưu lại.

**Prerequisite:** Mảng, vòng lặp, `max/min`, complexity và tư duy chia bài toán.

**Bài dự kiến:**

1. Nhận ra trạng thái lặp lại qua Fibonacci.
2. Định nghĩa `dp[state]` và trạng thái đầu.
3. Công thức chuyển và thứ tự tính.
4. Bước đi một/hai bước và đường đi trên lưới.
5. Dãy con tăng hoặc bài tối ưu một chiều.
6. Ba lô 0/1 ở giới hạn nhỏ.

**Bài tập khung:** Tầng A đi cầu thang; Tầng B đường đi/dãy; Tầng C ba lô hoặc biến thể có trạng thái rõ.

**Lỗi cần kiểm soát:** Trạng thái mơ hồ, khởi tạo sai, duyệt sai hướng và nhầm bài tối ưu với bài đếm số cách.

**Sẽ dùng về sau:** Digit DP, Graph DP và các bài trạng thái nhiều chiều.

## Chương 14 — Đồ thị

**Vai trò:** Dạy mô hình hóa đối tượng–quan hệ và duyệt các trạng thái liên thông.

**Prerequisite:** `vector`, hàm, đánh dấu, queue/stack và mô hình Input–Process–Output.

**Bài dự kiến:**

1. Đỉnh, cạnh và danh sách kề.
2. DFS và thành phần liên thông.
3. BFS và khoảng cách không trọng số.
4. Đồ thị một chiều/hai chiều và cạnh trùng.
5. Mê cung, đường đi và bài chuyển giao.

**Bài tập khung:** Tầng A duyệt đồ thị; Tầng B đếm thành phần/đường đi; Tầng C khoảng cách hoặc mô hình hóa bối cảnh mới.

**Lỗi cần kiểm soát:** Không đánh dấu, thêm cạnh sai chiều, nhầm số đỉnh/số cạnh và truy cập danh sách kề sai.

**Sẽ dùng về sau:** Graph nâng cao, queue, DP trên đồ thị và các bài trạng thái.

## Chương 15 — Stack và Queue

**Vai trò:** Làm rõ thứ tự dữ liệu đi vào và đi ra có thể quyết định toàn bộ lời giải.

**Prerequisite:** Mảng, vòng lặp và STL nhập môn.

**Bài dự kiến:**

1. Stack: vào sau–ra trước.
2. Kiểm tra ngoặc đúng.
3. Queue: vào trước–ra trước.
4. Mô phỏng hàng chờ.
5. Liên hệ queue với BFS và chọn cấu trúc phù hợp.

**Bài tập khung:** Tầng A thao tác push/pop; Tầng B ngoặc và hàng chờ; Tầng C mô phỏng nhiều loại sự kiện.

**Lỗi cần kiểm soát:** Gọi `top/front` khi rỗng, pop sai thời điểm và chưa xác định thứ tự xử lý trước khi code.

**Sẽ dùng về sau:** Đồ thị, Segment Tree hỗ trợ và các bài mô phỏng.

## Chương 16 — Segment Tree

**Vai trò:** Giới thiệu cấu trúc cây cho dữ liệu có cả truy vấn đoạn và cập nhật điểm.

**Prerequisite:** Mảng tiền tố, đệ quy, chia đoạn và complexity.

**Bài dự kiến:**

1. Vì sao Prefix Sum chưa đủ khi dữ liệu thay đổi.
2. Chia dãy thành các đoạn và xây cây.
3. Truy vấn tổng đoạn.
4. Cập nhật một điểm.
5. Mở rộng min/max và kiểm tra đoạn giao nhau.

**Bài tập khung:** Tầng A build/query; Tầng B update một điểm; Tầng C nhiều loại phép gộp ở phạm vi nhỏ.

**Lỗi cần kiểm soát:** Chia đoạn sai, nhầm giao hoàn toàn/một phần, quên cập nhật nút cha và sai chỉ số.

**Sẽ dùng về sau:** Fenwick Tree, các cấu trúc truy vấn đoạn và bài dữ liệu động.

## Chương 17 — Digit DP

**Vai trò:** Mở rộng DP sang việc đếm các số theo từng chữ số trong một khoảng.

**Prerequisite:** DP cơ bản, modulo, đệ quy và `string`.

**Bài dự kiến:**

1. Biểu diễn số bằng chuỗi chữ số.
2. Trạng thái `position`, `tight` và thông tin phụ.
3. Đếm trong `[0, X]`.
4. Tính trong `[L, R]` bằng hiệu hai kết quả.
5. Số 0 ở đầu và trạng thái không bắt buộc.

**Bài tập khung:** Tầng A tổng chữ số; Tầng B cấm chữ số; Tầng C điều kiện chia hết hoặc nhiều trạng thái.

**Lỗi cần kiểm soát:** Thiếu `tight`, xử lý số 0 đầu sai, quên `F(R) - F(L-1)` và modulo âm.

**Sẽ dùng về sau:** Các bài đếm số nâng cao và DP trên chữ số.

## Chương 18 — String Hashing

**Vai trò:** Dùng biểu diễn tiền tố để so sánh nhanh các đoạn xâu, đồng thời hiểu giới hạn xác suất.

**Prerequisite:** `string`, mảng tiền tố, modulo và phép nhân an toàn.

**Bài dự kiến:**

1. Ý tưởng ánh xạ xâu thành số.
2. Hash tiền tố và công thức hash đoạn.
3. So sánh hai đoạn cùng độ dài.
4. Kiểm tra palindrome bằng hash.
5. Va chạm và cách giảm rủi ro bằng hai hash hoặc kiểm tra lại.

**Bài tập khung:** Tầng A hash đoạn; Tầng B so sánh/palindrome; Tầng C đếm xâu con hoặc tìm đoạn lặp.

**Lỗi cần kiểm soát:** Sai chỉ số, chuẩn hóa modulo sai, quên lũy thừa cơ số và xem hash bằng nhau là bằng chứng tuyệt đối.

**Sẽ dùng về sau:** So khớp xâu và các bài chuỗi cần truy vấn nhanh.

## Chương 19 — Số nguyên lớn

**Vai trò:** Giúp học sinh tiếp tục tính toán khi số vượt miền của kiểu dữ liệu chuẩn.

**Prerequisite:** `string`, mảng chữ số, cộng/trừ/nhân và modulo.

**Bài dự kiến:**

1. Lưu số lớn bằng chuỗi.
2. So sánh sau khi bỏ số 0 đầu.
3. Cộng hai số lớn.
4. Trừ và xử lý mượn ở phạm vi phù hợp.
5. Nhân với số nhỏ và tính modulo của chuỗi.

**Bài tập khung:** Tầng A cộng; Tầng B so sánh/nhân số nhỏ; Tầng C kết hợp nhiều phép tính hoặc modulo.

**Lỗi cần kiểm soát:** Duyệt sai hướng, quên nhớ/mượn, giữ số 0 đầu và nhầm chuỗi với số nguyên.

**Sẽ dùng về sau:** Bài số học lớn, tổ hợp và các công thức vượt miền chuẩn.

## Chương 20 — Phép toán trên bit

**Vai trò:** Biểu diễn trạng thái có/không và tập con nhỏ bằng các bit của một số nguyên.

**Prerequisite:** Số nguyên, điều kiện, tập hợp nhỏ và biểu diễn nhị phân trực quan.

**Bài dự kiến:**

1. AND, OR, XOR, NOT và dịch bit.
2. Kiểm tra, bật, tắt và đảo một bit.
3. Đếm bit 1.
4. Bitmask biểu diễn tập con.
5. Liệt kê tập con của tập nhỏ.

**Bài tập khung:** Tầng A thao tác bit; Tầng B kiểm tra tập con; Tầng C liệt kê hoặc tối ưu trên số lượng phần tử nhỏ.

**Lỗi cần kiểm soát:** Nhầm `&` với `&&`, dịch quá số bit, dùng kiểu không phù hợp và áp dụng bitmask cho dữ liệu quá lớn.

**Sẽ dùng về sau:** Fenwick Tree, DP bitmask và các bài tổ hợp trên tập nhỏ.

## Chương 21 — Fenwick Tree

**Vai trò:** Kết nối Prefix Sum, bit và dữ liệu động bằng cấu trúc cập nhật điểm/truy vấn tiền tố.

**Prerequisite:** Mảng tiền tố, chỉ số 1-based, phép toán bit và complexity.

**Bài dự kiến:**

1. Vì sao Prefix Sum không đủ khi có cập nhật.
2. Ý nghĩa `index & -index`.
3. Cập nhật một điểm bằng `add`.
4. Tính tổng tiền tố bằng `prefixSum`.
5. Tổng đoạn, nén tọa độ và đếm nghịch thế ở mức mở rộng.

**Bài tập khung:** Tầng A update/query; Tầng B tổng đoạn động; Tầng C nén tọa độ hoặc đếm nghịch thế.

**Lỗi cần kiểm soát:** Nhầm 0-based/1-based, cập nhật sai hướng, quên nén tọa độ và truy vấn ngoài miền.

**Sẽ dùng về sau:** Các bài truy vấn động và cấu trúc dữ liệu nâng cao.

## Chuẩn outline dùng khi viết sâu từng chương

Mỗi chương sau khi được chọn để triển khai phải được phát triển theo các trường sau, nhưng số Bài và độ sâu được điều chỉnh theo độ khó:

| Trường | Cần có |
|---|---|
| Mục tiêu | Learning outcomes quan sát được |
| Ôn nhanh | Kiến thức nền cần gọi lại từ Phần I/chương trước |
| Vấn đề | Bối cảnh và Input–Process–Output |
| Ý tưởng | Trực giác, công thức hoặc invariant trước code |
| Mô phỏng | Dữ liệu nhỏ, theo dõi trạng thái từng bước |
| Code | C++17, header chuẩn dự án, safe input, không debug output |
| Bài tập | Tầng A củng cố, Tầng B vận dụng, Tầng C chuyển giao |
| Lỗi | Bẫy chỉ số, kiểu dữ liệu, giả định và trường hợp biên |
| Tự kiểm tra | Câu hỏi có đáp án định hướng hoặc rubric |
| Tóm tắt | Các ý giữ lại sau khi quên chi tiết |
| Sẽ dùng về sau | Cầu nối tới chương/chủ đề khác |

## Trạng thái khung

Khung toàn bộ 21 chương đã được dựng để chủ dự án review. Chỉ Chương 1 và Chương 2 hiện có source nội dung sâu. Chương 3–21 mới là outline; không được gọi là hoàn chỉnh cho đến khi từng chương được viết, review và đồng bộ theo quy trình source-first.
