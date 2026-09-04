# enrich_data_dp1.py
# Dữ liệu chuẩn hóa Sư phạm 15 bài DP1 (CPPB-DP1-01 -> CPPB-DP1-15)

DP1_DATA = {
    "CPPB-DP1-01": {
        "title": "Bậc Thang Cơ Bản",
        "bc": "Trong một tòa tháp công nghệ hiện đại, bạn robot phục vụ cần di chuyển lên đỉnh cầu thang gồm $N$ bậc để chuyển tài liệu. Do thiết kế cơ học của chân bước, ở mỗi nhịp di chuyển, robot chỉ có thể bước lên đúng $1$ bậc hoặc bước sải dài qua $2$ bậc liên tiếp. Để lập trình điều hướng linh hoạt cho robot, kỹ sư phần mềm cần tính toán xem có tất cả bao nhiêu trình tự bước đi khác nhau để đưa robot từ chân cầu thang lên tới đúng đỉnh bậc thứ $N$.",
        "nv": "Cho số nguyên dương $N$ là số bậc của cầu thang. Hãy lập trình tính số cách bước hợp lệ để robot lên đến đỉnh bậc thứ $N$. Vì kết quả có thể rất lớn, hãy in ra phần dư của kết quả khi chia cho $10^9 + 7$.",
        "inp": "- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^5$) biểu diễn số bậc của cầu thang.",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là số cách bước hợp lệ theo modulo $10^9 + 7$.",
        "gt": "Với cầu thang có $N = 3$ bậc, robot có tất cả 3 trình tự bước đi hợp lệ để lên đến đỉnh:\n1. Bước từng bậc một: $1 + 1 + 1 = 3$.\n2. Bước 1 bậc rồi bước 2 bậc: $1 + 2 = 3$.\n3. Bước 2 bậc rồi bước 1 bậc: $2 + 1 = 3$.\nKết quả in ra là 3."
    },
    "CPPB-DP1-02": {
        "title": "Chú Ếch Nhảy Chi Phí Nhỏ Nhất",
        "bc": "Trong một khu vườn sinh thái, có $N$ phiến đá được xếp thành hàng ngang từ trái sang phải, đánh số thứ tự từ $1$ đến $N$. Phiến đá thứ $i$ có độ cao là $H_i$. Một chú ếch đang ở phiến đá số $1$ và muốn di chuyển tới phiến đá cuối cùng số $N$. Từ phiến đá số $i$, chú ếch có thể chọn nhảy sang phiến đá ngay cạnh $i + 1$ hoặc nhảy vượt qua một phiến để tới phiến đá $i + 2$. Năng lượng tiêu hao (chi phí) cho mỗi cú nhảy từ phiến đá $i$ sang phiến đá $j$ đúng bằng độ chênh lệch chiều cao giữa hai phiến đá, tức $|H_i - H_j|$.",
        "nv": "Cho số lượng phiến đá $N$ và độ cao của từng phiến đá. Hãy lập trình tìm tổng chi phí năng lượng tối thiểu để chú ếch có thể di chuyển từ phiến đá $1$ tới phiến đá $N$.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($2 \le N \le 10^5$) biểu diễn số lượng phiến đá.\n- Dòng 2: Chứa $N$ số nguyên dương $H_1, H_2, \dots, H_N$ ($1 \le H_i \le 10^4$) biểu diễn độ cao của các phiến đá, các số cách nhau bởi khoảng trắng.",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là tổng chi phí nhỏ nhất tìm được.",
        "gt": "Với 4 phiến đá có độ cao lần lượt là $[10, 30, 40, 20]$:\n- Bước 1: Từ phiến đá 1 ($H_1 = 10$) nhảy sang phiến đá 2 ($H_2 = 30$), chi phí tiêu hao là $|10 - 30| = 20$.\n- Bước 2: Từ phiến đá 2 ($H_2 = 30$) nhảy vượt sang phiến đá 4 ($H_4 = 20$), chi phí tiêu hao là $|30 - 20| = 10$.\nTổng chi phí tiêu hao cho toàn bộ hành trình là $20 + 10 = 30$, đây là phương án tốn ít năng lượng nhất."
    },
    "CPPB-DP1-03": {
        "title": "Chú Ếch Nhảy K Bước",
        "bc": "Vẫn tại khu vườn sinh thái có $N$ phiến đá xếp thành hàng ngang với độ cao $H_1, H_2, \dots, H_N$. Lần này chú ếch đã được huấn luyện với thể lực dẻo dai hơn: Từ phiến đá thứ $i$, chú ếch có thể chọn nhảy xa tới bất kỳ phiến đá nào trong phạm vi $K$ bước tiếp theo, tức là các phiến đá $i + 1, i + 2, \dots, \min(N, i + K)$. Chi phí cho mỗi bước nhảy từ phiến đá $i$ tới phiến đá $j$ vẫn bằng độ chênh lệch chiều cao $|H_i - H_j|$.",
        "nv": "Cho số lượng phiến đá $N$, tầm nhảy tối đa $K$ và danh sách độ cao của các phiến đá. Hãy lập trình tính toán tổng chi phí năng lượng ít nhất để chú ếch đi từ phiến đá $1$ tới phiến đá $N$.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $K$ ($2 \le N \le 10^5, 1 \le K \le 100$).\n- Dòng 2: Chứa $N$ số nguyên dương $H_1, H_2, \dots, H_N$ ($1 \le H_i \le 10^4$) biểu diễn độ cao của các phiến đá.",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là tổng chi phí năng lượng tối thiểu.",
        "gt": "Với $N = 5, K = 3$ và độ cao các phiến đá là $[10, 30, 40, 50, 20]$:\n- Từ đá 1 ($H_1 = 10$), chú ếch nhảy sang đá 2 ($H_2 = 30$) với khoảng cách 1 bước hợp lệ ($\le 3$), chi phí là $|10 - 30| = 20$.\n- Từ đá 2 ($H_2 = 30$), chú ếch nhảy thẳng tới đích là đá 5 ($H_5 = 20$) với khoảng cách $5 - 2 = 3$ bước (vẫn $\le K = 3$), chi phí là $|30 - 20| = 10$.\nTổng chi phí tối thiểu đạt được là $20 + 10 = 30$."
    },
    "CPPB-DP1-04": {
        "title": "Đổi Tiền Số Xu Ít Nhất",
        "bc": "Tại một trạm đổi tiền tự động thông minh của trung tâm thương mại, hệ thống hỗ trợ $N$ loại đồng xu với các mệnh giá khác nhau. Khách hàng có nhu cầu đổi một số tiền mặt đúng bằng $S$ đồng để sử dụng máy bán nước tự động. Nhằm tối ưu hóa số lượng tiền kim loại lưu thông và giúp ví của khách hàng không bị quá nặng, hệ thống máy luôn tìm cách chi trả bằng số lượng đồng xu ít nhất có thể. Biết rằng kho tiền xu của trạm luôn dồi dào, mỗi mệnh giá có số lượng xu không giới hạn.",
        "nv": "Cho danh sách $N$ mệnh giá đồng xu và số tiền cần đổi $S$. Hãy lập trình xác định số lượng đồng xu ít nhất để đổi được đúng số tiền $S$. Nếu không có cách nào đổi được đúng số tiền đó, in ra `-1`.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $S$ ($1 \le N \le 100, 1 \le S \le 10^5$) lần lượt là số loại đồng xu và số tiền mục tiêu cần đổi.\n- Dòng 2: Chứa $N$ số nguyên dương $c_1, c_2, \dots, c_N$ ($1 \le c_i \le 10^4$) biểu diễn các mệnh giá đồng xu, các số cách nhau bởi khoảng trắng.",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là số lượng đồng xu ít nhất cần dùng. Nếu không đổi được, in ra `-1`.",
        "gt": "Để đổi được số tiền $S = 11$ từ các mệnh giá xu $\{1, 5, 6\}$:\n- Cách 1: Dùng 1 đồng 6 và 5 đồng 1 ($6 + 1 \times 5 = 11$), tổng cộng tốn 6 đồng xu.\n- Cách 2: Dùng 2 đồng 5 và 1 đồng 1 ($5 \times 2 + 1 = 11$), tổng cộng tốn 3 đồng xu.\n- Phương án tối ưu nhất: Dùng 1 đồng 5 và 1 đồng 6 ($5 + 6 = 11$), chỉ cần đúng 2 đồng xu. Kết quả là 2."
    },
    "CPPB-DP1-05": {
        "title": "Đếm Số Cách Đổi Tiền",
        "bc": "Tại một hội thảo tài chính công nghệ, ban tổ chức thiết kế một thử thách cho các bạn học sinh về phương thức kết hợp tiền tệ. Cho $N$ mệnh giá đồng xu khác nhau, mỗi mệnh giá đều có số lượng không giới hạn. Một bạn học sinh cần tạo ra tổng số tiền đúng bằng $S$ đồng. Hai cách tạo tiền được xem là khác nhau nếu số lượng sử dụng của ít nhất một mệnh giá đồng xu là khác nhau (thứ tự chọn các đồng xu không làm ảnh hưởng đến tính chất của tổ hợp).",
        "nv": "Cho $N$ mệnh giá đồng xu và số tiền mục tiêu $S$. Hãy lập trình đếm xem có tất cả bao nhiêu tổ hợp đồng xu khác nhau để có tổng giá trị đúng bằng $S$. Vì kết quả có thể rất lớn, hãy in ra phần dư của kết quả khi chia cho $10^9 + 7$.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $S$ ($1 \le N \le 100, 1 \le S \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên dương phân biệt biểu diễn các mệnh giá đồng xu ($1 \le c_i \le 10^4$).",
        "outp": "- In ra trên một dòng duy nhất số lượng tổ hợp đổi tiền hợp lệ theo modulo $10^9 + 7$.",
        "gt": "Với các mệnh giá xu $\{2, 3, 5\}$ và số tiền mục tiêu $S = 9$, có đúng 3 tổ hợp đồng xu khác nhau:\n1. Ba đồng xu: $2 + 2 + 5 = 9$.\n2. Ba đồng xu: $3 + 3 + 3 = 9$.\n3. Bốn đồng xu: $2 + 2 + 2 + 3 = 9$.\nKết quả đếm được là 3 cách."
    },
    "CPPB-DP1-06": {
        "title": "Tổng Đoạn Con Không Liền Kề Lớn Nhất",
        "bc": "Một tuyến phố thương mại gồm $N$ căn nhà liền kề được đánh số từ $1$ đến $N$. Căn nhà thứ $i$ có giá trị thương mại là $A_i$. Một công ty quảng cáo muốn thuê mặt bằng để lắp đặt các màn hình LED kích thước lớn. Tuy nhiên, theo quy định an toàn đô thị về khoảng cách chiếu sáng, công ty không được phép thuê hai căn nhà đứng sát cạnh nhau trên cùng dãy phố.",
        "nv": "Cho danh sách giá trị thương mại của $N$ căn nhà. Hãy lập trình chọn ra một tập hợp các căn nhà không kề nhau sao cho tổng giá trị thu được là lớn nhất có thể.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$) biểu diễn số lượng căn nhà.\n- Dòng 2: Chứa $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^4$) biểu diễn giá trị của từng căn nhà.",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là tổng giá trị lớn nhất tìm được.",
        "gt": "Với dãy giá trị của 4 căn nhà là $[1, 2, 3, 1]$:\n- Nếu chọn nhà 2 và nhà 4: Tổng giá trị là $2 + 1 = 3$.\n- Phương án tối ưu: Chọn nhà 1 (giá trị 1) và nhà 3 (giá trị 3). Hai nhà này không kề nhau và mang lại tổng giá trị lớn nhất là $1 + 3 = 4$."
    },
    "CPPB-DP1-07": {
        "title": "Lát Gạch Bảng 2xN",
        "bc": "Trong một triển lãm kiến trúc, ban tổ chức cần lát kín một khoảng sàn hình chữ nhật có kích thước cố định là $2 \times N$ bằng các viên gạch men trang trí kích thước $1 \times 2$. Mỗi viên gạch men có thể được đặt nằm ngang (kích thước $1 \times 2$) hoặc dựng đứng (kích thước $2 \times 1$). Toàn bộ mặt sàn phải được phủ kín hoàn toàn, không có ô nào bị bỏ trống và các viên gạch không được phép đè lên nhau.",
        "nv": "Cho số nguyên dương $N$ là chiều dài của mặt sàn. Hãy lập trình tính số cách lát gạch khác nhau để phủ kín mặt sàn $2 \times N$, lấy dư cho $10^9 + 7$.",
        "inp": "- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^5$) biểu diễn chiều dài mặt sàn.",
        "outp": "- In ra trên một dòng duy nhất số cách lát sàn hợp lệ theo modulo $10^9 + 7$.",
        "gt": "Với sàn nhà kích thước $2 \times 4$ ($N = 4$), có tất cả 5 cách lát kín hợp lệ:\n1. Đặt 4 viên gạch dựng đứng liên tiếp.\n2. Đặt 2 viên nằm ngang ở đầu, theo sau là 2 viên dựng đứng.\n3. Đặt 1 viên dựng đứng, 2 viên nằm ngang ở giữa, 1 viên dựng đứng ở cuối.\n4. Đặt 2 viên dựng đứng ở đầu, theo sau là 2 viên nằm ngang.\n5. Đặt 2 cặp viên nằm ngang chồng lên nhau.\nKết quả in ra là 5."
    },
    "CPPB-DP1-08": {
        "title": "Lát Gạch Bảng 3xN",
        "bc": "Tiếp tục bài toán thiết kế mặt sàn kiến trúc, lần này sàn nhà được mở rộng thành kích thước $3 \times N$. Ban tổ chức vẫn sử dụng các viên gạch men domino có kích thước $2 \times 1$ (có thể xoay ngang thành $1 \times 2$). Yêu cầu đặt ra là phải lát kín hoàn toàn diện tích $3 \times N$ mà không có viên gạch nào vượt ra ngoài biên hoặc đè lên nhau.",
        "nv": "Cho số nguyên dương $N$ là chiều dài của sàn nhà. Hãy lập trình đếm số cách lát kín mặt sàn $3 \times N$, lấy dư cho $10^9 + 7$. (Nếu $N$ lẻ, diện tích sàn là số lẻ nên không thể phủ kín bằng các viên gạch diện tích 2, khi đó in ra `0`).",
        "inp": "- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^5$) biểu diễn chiều dài của sàn.",
        "outp": "- In ra trên một dòng duy nhất số cách lát kín sàn theo modulo $10^9 + 7$.",
        "gt": "Với sàn nhà kích thước $3 \times 2$ ($N = 2$), tổng diện tích là $3 \times 2 = 6$ ô đơn vị, cần dùng đúng 3 viên gạch domino. Có tất cả đúng 3 cách ghép hợp lệ:\n1. Một viên đặt dọc ở cột 1, hai viên đặt ngang ở hàng 2 và 3.\n2. Hai viên đặt ngang ở hàng 1 và 2, một viên đặt dọc ở cột 2.\n3. Ba viên đặt ngang song song với nhau.\nKết quả in ra là 3."
    },
    "CPPB-DP1-09": {
        "title": "Dãy Con Tăng Dài Nhất LIS O(N^2)",
        "bc": "Tại trạm quan trắc địa chấn ven biển, các chuyên gia theo dõi sự biến thiên áp suất lớp vỏ trái đất qua một chuỗi $N$ lần đo liên tiếp, tương ứng với dãy số $A_1, A_2, \dots, A_N$. Để nhận diện xu thế gia tăng địa chấn qua các chu kỳ, các chuyên gia cần trích xuất một chuỗi các mốc đo có giá trị áp suất tăng dần nghiêm ngặt theo thời gian, sao cho số lượng mốc đo được chọn là nhiều nhất có thể.",
        "nv": "Cho dãy số nguyên $A$ gồm $N$ phần tử. Hãy lập trình tìm độ dài lớn nhất của một dãy con tăng nghiêm ngặt (không nhất thiết phải là các phần tử liên tiếp trong dãy ban đầu).",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$) biểu diễn số lượng phần tử của dãy.\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$), các số cách nhau bởi khoảng trắng.",
        "outp": "- In ra trên một dòng duy nhất độ dài của dãy con tăng nghiêm ngặt dài nhất.",
        "gt": "Với dãy số gồm 6 phần tử $[10, 20, 10, 30, 20, 50]$:\nMột dãy con tăng nghiêm ngặt dài nhất có thể chọn là $[10, 20, 30, 50]$ (tương ứng với các chỉ số 1, 2, 4, 6 trong dãy gốc). Độ dài của dãy con này là 4."
    },
    "CPPB-DP1-10": {
        "title": "Dãy Con Tăng Dài Nhất LIS O(N log N)",
        "bc": "Quy mô trạm quan trắc địa chấn được nâng cấp tự động hóa trên diện rộng, số lượng mẫu dữ liệu cảm biến thu thập trong một đợt quan sát lên tới $N = 10^5$ phần tử. Với tập dữ liệu khổng lồ này, bài toán tìm dãy con tăng dài nhất đòi hỏi một thuật toán có hiệu năng vượt trội để xử lý tức thời trong vòng 1 giây.",
        "nv": "Cho dãy $A$ gồm $N$ số nguyên với $N$ lên tới $10^5$. Hãy lập trình xác định độ dài của dãy con tăng nghiêm ngặt dài nhất.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là độ dài lớn nhất của dãy con tăng nghiêm ngặt.",
        "gt": "Với dãy số $[5, 2, 7, 4, 3, 8]$:\nDãy con tăng nghiêm ngặt dài nhất có thể chọn là $[2, 4, 8]$ (hoặc $[2, 3, 8]$, $[5, 7, 8]$). Độ dài dài nhất đạt được là 3."
    },
    "CPPB-DP1-11": {
        "title": "Truy Vết Dãy Con Tăng Dài Nhất",
        "bc": "Sau khi tính toán được độ dài của xu thế gia tăng dữ liệu áp suất địa chấn, ban chỉ đạo cần xuất báo cáo chi tiết bao gồm chính xác các giá trị đo đạc cụ thể đã hình thành nên xu thế đó để gửi tới viện nghiên cứu phân tích.",
        "nv": "Cho dãy số nguyên $A$ gồm $N$ phần tử. Hãy lập trình tìm và in ra toàn bộ các phần tử thuộc về một dãy con tăng nghiêm ngặt dài nhất. Nếu có nhiều dãy con cùng đạt độ dài lớn nhất, bạn chỉ cần in ra một dãy con bất kỳ thỏa mãn.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- Dòng 1: In ra số nguyên $L$ là độ dài của dãy con tăng dài nhất.\n- Dòng 2: In ra $L$ số nguyên là các giá trị của dãy con được chọn, cách nhau bởi khoảng trắng.",
        "gt": "Với dãy số gốc là $[2, 1, 4, 3, 5]$:\nDãy con tăng dài nhất có độ dài bằng 3. Một dãy con hợp lệ thỏa mãn điều kiện tăng nghiêm ngặt là $[2, 4, 5]$ (hoặc $[1, 4, 5]$, $[1, 3, 5]$). Kết quả dòng 1 in ra 3, dòng 2 in ra các số 2 4 5."
    },
    "CPPB-DP1-12": {
        "title": "Dãy Con Giảm Dài Nhất (LDS)",
        "bc": "Trong quá trình hạ nhiệt độ lò luyện kim công nghiệp, các cảm biến ghi nhận nhiệt độ theo từng chu kỳ làm mát tạo thành dãy $N$ số nguyên $A_1, A_2, \dots, A_N$. Kỹ sư vận hành cần đánh giá tính ổn định của quy trình thông qua độ dài của chuỗi các lần đo có nhiệt độ giảm dần nghiêm ngặt dài nhất.",
        "nv": "Cho dãy số nguyên $A$ gồm $N$ phần tử. Hãy lập trình tìm độ dài của dãy con giảm nghiêm ngặt dài nhất.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng duy nhất độ dài của dãy con giảm nghiêm ngặt dài nhất.",
        "gt": "Với dãy 8 số nguyên $[10, 9, 2, 5, 3, 7, 101, 18]$:\nMột dãy con giảm nghiêm ngặt dài nhất có thể trích xuất là $[10, 9, 5, 3]$ (hoặc $[10, 9, 7, 3]$). Độ dài lớn nhất đạt được là 4."
    },
    "CPPB-DP1-13": {
        "title": "Dãy Con Hình Sóng Núi (Longest Bitonic Subsequence)",
        "bc": "Một thiết bị bay không người lái (drone) thực hiện hành trình bay thám hiểm qua một dãy núi. Độ cao của drone tại các điểm quan sát tạo thành một chuỗi $N$ số nguyên. Một hành trình bay được gọi là có hình dạng sóng núi (Bitonic) nếu độ cao đầu tiên tăng dần nghiêm ngặt lên đến một đỉnh nào đó, sau đó giảm dần nghiêm ngặt từ đỉnh đó xuống cuối (cho phép phần tăng hoặc phần giảm rỗng). Ban điều hành muốn tìm một hành trình sóng núi chứa nhiều điểm quan sát nhất.",
        "nv": "Cho dãy số nguyên $A$ gồm $N$ phần tử. Hãy lập trình tìm độ dài lớn nhất của một dãy con có dạng sóng núi.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^5$).",
        "outp": "- In ra trên một dòng duy nhất độ dài lớn nhất của dãy con hình sóng núi.",
        "gt": "Với dãy số gồm 8 phần tử $[1, 11, 2, 10, 4, 5, 2, 1]$:\nDãy con hình sóng núi dài nhất có thể chọn là $[1, 2, 10, 5, 2, 1]$ (với đỉnh là 10; phần tăng gồm 1, 2, 10 và phần giảm gồm 10, 5, 2, 1). Tổng số phần tử của dãy sóng núi này là 6."
    },
    "CPPB-DP1-14": {
        "title": "Tổng Dãy Con Tăng Lớn Nhất (MSIS)",
        "bc": "Một nhà đầu tư phân tích lợi nhuận của các cổ phiếu qua $N$ quý liên tiếp. Để xây dựng chiến lược mua vào đón đầu chu kỳ phát triển bền vững, nhà đầu tư muốn chọn ra một chuỗi các quý đầu tư mà lợi nhuận ở quý sau luôn cao hơn quý trước (tăng nghiêm ngặt), đồng thời tổng lợi nhuận thu được từ tất cả các quý được chọn phải là lớn nhất.",
        "nv": "Cho dãy số nguyên dương $A$ gồm $N$ phần tử. Hãy lập trình tìm tổng giá trị lớn nhất của một dãy con tăng nghiêm ngặt.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$).\n- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^5$).",
        "outp": "- In ra trên một dòng duy nhất tổng giá trị lớn nhất tìm được.",
        "gt": "Với dãy số gồm 7 phần tử $[1, 101, 2, 3, 100, 4, 5]$:\n- Dãy con tăng dài nhất là $[1, 2, 3, 4, 5]$ có tổng là $1 + 2 + 3 + 4 + 5 = 15$.\n- Nhưng dãy con tăng $[1, 2, 3, 100]$ lại mang lại tổng giá trị lớn hơn nhiều: $1 + 2 + 3 + 100 = 106$. Đây là tổng lớn nhất có thể đạt được."
    },
    "CPPB-DP1-15": {
        "title": "Tối Ưu Hóa Chuỗi Dự Án Năng Lượng",
        "bc": "Một quỹ đầu tư năng lượng tái tạo xem xét danh mục gồm $N$ dự án điện gió và điện mặt trời. Dự án thứ $i$ có quy mô công suất là $P_i$ (MW) và mang lại doanh thu kỳ vọng là $V_i$ (tỷ đồng). Để đảm bảo lộ trình mở rộng thị phần an toàn và bền vững, quỹ đầu tư chỉ được phép phê duyệt một chuỗi các dự án có quy mô công suất tăng dần nghiêm ngặt theo thời gian xét duyệt.",
        "nv": "Cho danh sách $N$ dự án với công suất $P_i$ và doanh thu $V_i$. Hãy lập trình chọn ra một chuỗi các dự án có công suất tăng nghiêm ngặt sao cho tổng doanh thu thu về là lớn nhất.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$) biểu diễn số lượng dự án.\n- $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên dương $P_i$ và $V_i$ ($1 \le P_i \le 10^5, 1 \le V_i \le 10^9$) lần lượt là công suất và doanh thu của dự án thứ $i$.",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là tổng doanh thu lớn nhất có thể đạt được.",
        "gt": "Với 3 dự án năng lượng có thông số $[(10, 100), (5, 50), (20, 200)]$:\nChuỗi dự án có công suất tăng dần nghiêm ngặt là chọn dự án 2 (công suất 5), sau đó dự án 1 (công suất 10), và cuối cùng là dự án 3 (công suất 20). Chuỗi công suất là $5 < 10 < 20$, mang lại tổng doanh thu tối đa là $50 + 100 + 200 = 350$."
    }
}
