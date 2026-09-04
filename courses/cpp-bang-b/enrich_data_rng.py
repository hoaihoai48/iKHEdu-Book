# enrich_data_rng.py
# Dữ liệu chuẩn hóa Sư phạm 15 bài RNG (CPPB-RNG-01 -> CPPB-RNG-15)

RNG_DATA = {
    "CPPB-RNG-01": {
        "title": "Cài Đặt Fenwick Tree Tính Tổng Đoạn (Range Sum)",
        "bc": "Một máy chủ tài chính theo dõi biến động số dư tài khoản của $N$ khách hàng được đánh số từ $1$ đến $N$, số dư ban đầu tại tài khoản $i$ là $A_i$. Hệ thống liên tục tiếp nhận $Q$ giao dịch trực tuyến gồm hai loại: cộng thêm một khoản tiền $val$ vào tài khoản tại vị trí $pos$, hoặc truy vấn tính tổng số dư của tất cả các tài khoản nằm trong khoảng từ $L$ đến $R$. Mọi thao tác cần được xử lý tức thời.",
        "nv": "Cho mảng $A$ và $Q$ truy vấn thuộc hai loại: `1 pos val` (cộng $val$ vào $A[pos]$), `2 L R` (tính tổng các phần tử từ $L$ đến $R$). Hãy lập trình in ra kết quả của các truy vấn loại 2.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).\n- $Q$ dòng tiếp theo, mỗi dòng chứa một truy vấn theo định dạng trên.",
        "outp": "- Với mỗi truy vấn loại 2, in ra tổng các phần tử trên đoạn $[L, R]$ trên một dòng.",
        "gt": "Với mảng ban đầu gồm 5 phần tử $[1, 2, 3, 4, 5]$:\n- Truy vấn tính tổng đoạn từ 1 đến 3: $1 + 2 + 3 = 6$.\n- Cập nhật cộng thêm 10 vào phần tử tại vị trí 3: mảng trở thành $[1, 2, 13, 4, 5]$.\n- Truy vấn lại tổng đoạn từ 1 đến 3: $1 + 2 + 13 = 16$."
    },
    "CPPB-RNG-02": {
        "title": "Cài Đặt Segment Tree Tìm Min Đoạn (RMQ)",
        "bc": "Một trạm quan trắc khí tượng ghi nhận nhiệt độ thấp nhất tại $N$ trạm cảm biến ven biển. Các chuyên gia cần liên tục thực hiện hai loại thao tác: cập nhật lại nhiệt độ mới tại một trạm cảm biến cụ thể, và truy vấn tìm mức nhiệt độ thấp nhất (Min) trong một phân đoạn các trạm quan sát từ $L$ đến $R$.",
        "nv": "Cho mảng $A$ gồm $N$ số nguyên và $Q$ truy vấn thuộc hai dạng: `1 pos val` (gán $A[pos] = val$) và `2 L R` (tìm giá trị nhỏ nhất trong đoạn từ $L$ đến $R$). Hãy in ra kết quả của các truy vấn loại 2.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).\n- $Q$ dòng tiếp theo, mỗi dòng chứa một truy vấn theo định dạng trên.",
        "outp": "- Với mỗi truy vấn loại 2, in ra giá trị nhỏ nhất trong đoạn $[L, R]$ trên một dòng.",
        "gt": "Với mảng $[5, 2, 8, 1, 9]$:\n- Truy vấn tìm min đoạn từ 1 đến 3: $\\min(5, 2, 8) = 2$.\n- Cập nhật vị trí 2 thành 10: mảng thành $[5, 10, 8, 1, 9]$.\n- Truy vấn lại min đoạn từ 1 đến 3: $\\min(5, 10, 8) = 5$."
    },
    "CPPB-RNG-03": {
        "title": "Cập Nhật Đoạn & Truy Vấn Điểm (Range Update Point Query)",
        "bc": "Một chương trình khuyến mãi của sàn thương mại điện tử đồng loạt cộng thêm một khoản điểm thưởng $V$ cho tất cả các khách hàng có mã số định danh nằm trong khoảng từ $L$ đến $R$. Sau đó, một khách hàng tại vị trí $pos$ muốn tra cứu số điểm thưởng tích lũy hiện tại của mình.",
        "nv": "Cho mảng $A$ và $Q$ thao tác thuộc hai dạng: `1 L R V` (cộng thêm $V$ vào tất cả các phần tử từ $L$ đến $R$) và `2 pos` (in ra giá trị hiện tại của phần tử tại vị trí $pos$). Hãy in ra kết quả của các thao tác loại 2.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).\n- $Q$ dòng tiếp theo chứa các thao tác mô tả như trên.",
        "outp": "- Với mỗi thao tác loại 2, in ra giá trị tại vị trí $pos$ trên một dòng.",
        "gt": "Với mảng ban đầu toàn số 0: $[0, 0, 0, 0, 0]$:\n- Cộng thêm 5 vào đoạn từ vị trí 2 đến 4: mảng thành $[0, 5, 5, 5, 0]$.\n- Truy vấn giá trị tại vị trí 3: in ra 5."
    },
    "CPPB-RNG-04": {
        "title": "Tìm Max Đoạn & Đếm Số Lần Xuất Hiện",
        "bc": "Một hệ thống đánh giá hiệu năng máy chủ theo dõi điểm tải đỉnh của $N$ máy tính. Ban giám sát muốn biết trong một khoảng thời gian từ mốc $L$ đến $R$, giá trị tải lớn nhất (Max) đạt được là bao nhiêu và có bao nhiêu máy tính đạt đúng mức tải đỉnh này.",
        "nv": "Cho mảng $A$ gồm $N$ số nguyên và $Q$ truy vấn, mỗi truy vấn gồm hai chỉ số $L, R$. Hãy tìm giá trị lớn nhất và số lần xuất hiện của giá trị lớn nhất đó trong đoạn $[L, R]$.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).\n- $Q$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $L$ và $R$ ($1 \le L \le R \le N$).",
        "outp": "- Với mỗi truy vấn, in ra trên một dòng hai số nguyên: giá trị lớn nhất và số lần xuất hiện của nó, cách nhau bởi khoảng trắng.",
        "gt": "Với mảng $[3, 5, 2, 5, 5, 1]$ và truy vấn đoạn từ vị trí 1 đến 5:\nGiá trị lớn nhất trong đoạn là 5, và số 5 xuất hiện đúng 3 lần tại các vị trí 2, 4, 5. Kết quả in ra: 5 3."
    },
    "CPPB-RNG-05": {
        "title": "Đếm Số Cặp Nghịch Thế (Inversion Count)",
        "bc": "Một thuật toán sắp xếp cần đo lường mức độ xáo trộn của một danh sách gồm $N$ số nguyên. Một cặp nghịch thế là một cặp chỉ số $(i, j)$ thỏa mãn $i < j$ nhưng phần tử đứng trước lại lớn hơn phần tử đứng sau ($A_i > A_j$). Số lượng cặp nghịch thế thể hiện số phép đổi chỗ tối thiểu để đưa mảng về thứ tự tăng dần.",
        "nv": "Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình đếm tổng số lượng cặp nghịch thế trong mảng.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là số lượng cặp nghịch thế.",
        "gt": "Với mảng gồm 5 phần tử $[2, 4, 1, 3, 5]$:\nCác cặp nghịch thế gồm:\n- (2, 1) vì $2 > 1$.\n- (4, 1) vì $4 > 1$.\n- (4, 3) vì $4 > 3$.\nCó tất cả 3 cặp nghịch thế, kết quả in ra là 3."
    },
    "CPPB-RNG-06": {
        "title": "Truy Vấn Ước Chung Lớn Nhất Đoạn (Range GCD)",
        "bc": "Trong một hệ thống mã hóa dữ liệu theo khối, mỗi khối dữ liệu có một mã khóa số nguyên $A_i$. Để giải mã một chuỗi các khối liên tiếp từ $L$ đến $R$, thiết bị giải mã cần tính toán ước chung lớn nhất (GCD) của tất cả các khóa trong đoạn: $\\gcd(A_L, A_{L+1}, \\dots, A_R)$. Hệ thống cũng hỗ trợ cập nhật lại mã khóa tại từng khối.",
        "nv": "Cho mảng $A$ và $Q$ thao tác thuộc hai dạng: `1 pos val` (gán $A[pos] = val$) và `2 L R` (tìm GCD của các phần tử trong đoạn $[L, R]$). Hãy in ra kết quả cho các thao tác loại 2.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).\n- $Q$ dòng tiếp theo chứa các thao tác mô tả như trên.",
        "outp": "- Với mỗi thao tác loại 2, in ra giá trị GCD của đoạn trên một dòng.",
        "gt": "Với mảng $[6, 12, 18, 24]$:\n- Truy vấn GCD đoạn từ 1 đến 3: $\\gcd(6, 12, 18) = 6$.\n- Cập nhật vị trí 1 thành 4: mảng thành $[4, 12, 18, 24]$.\n- Truy vấn lại GCD đoạn từ 1 đến 3: $\\gcd(4, 12, 18) = 2$."
    },
    "CPPB-RNG-07": {
        "title": "Tìm Phần Tử Thứ K Nhỏ Nhất (K-th Element on BIT)",
        "bc": "Một máy chủ trò chơi trực tuyến liên tục ghi nhận điểm số của người chơi gia nhập phòng chờ. Ban tổ chức muốn tìm điểm số của người chơi có thành tích xếp thứ $K$ từ dưới lên (phần tử thứ $K$ nhỏ nhất trong tập hợp điểm số hiện tại).",
        "nv": "Cho một tập hợp các số nguyên hỗ trợ hai thao tác: thêm một số vào tập hợp, và tìm phần tử nhỏ thứ $K$ trong tập hợp. Hãy lập trình in ra kết quả cho các thao tác tìm kiếm.",
        "inp": "- Dòng 1: Chứa số nguyên dương $Q$ ($1 \le Q \le 10^5$).\n- $Q$ dòng tiếp theo chứa các thao tác.",
        "outp": "- In ra kết quả cho mỗi thao tác tìm phần tử thứ $K$ trên một dòng.",
        "gt": "Với tập hợp các số {10, 20, 30, 40, 50}:\nPhần tử nhỏ thứ 3 trong tập hợp là số 30."
    },
    "CPPB-RNG-08": {
        "title": "Tìm Vị Trí Đầu Tiên Có Giá Trị Lớn Hơn Hoặc Bằng X",
        "bc": "Một kho lưu trữ các kiện hàng được đánh số thứ tự từ $1$ đến $N$, kiện hàng thứ $i$ có khối lượng $A_i$. Một xe nâng hàng muốn tìm kiện hàng đầu tiên trong khoảng từ vị trí $L$ đến $R$ có khối lượng đủ lớn đạt từ $X$ trở lên để bốc dỡ. Nếu trong khoảng $[L, R]$ không có kiện hàng nào đạt yêu cầu, ghi nhận `-1`.",
        "nv": "Cho mảng $A$ và $Q$ truy vấn gồm 3 số $L, R, X$. Hãy lập trình tìm vị trí chỉ số đầu tiên trong đoạn $[L, R]$ có giá trị $\ge X$.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).\n- $Q$ dòng tiếp theo, mỗi dòng chứa 3 số nguyên $L, R, X$.",
        "outp": "- Với mỗi truy vấn, in ra chỉ số đầu tiên tìm được, hoặc `-1` nếu không có.",
        "gt": "Với mảng $[2, 3, 5, 1, 6]$ và truy vấn trong khoảng $[1, 5]$ tìm số $\ge 4$:\nĐi từ vị trí 1 sang: vị trí 1 là 2 (< 4), vị trí 2 là 3 (< 4), vị trí 3 là 5 ($\ge 4$). Vị trí đầu tiên thỏa mãn là vị trí 3."
    },
    "CPPB-RNG-09": {
        "title": "Dãy Con Tăng Dài Nhất LIS Bằng Fenwick Tree",
        "bc": "Một dự án phân tích xu thế chuỗi thời gian lớn gồm $N$ số nguyên cần tìm độ dài của dãy con tăng nghiêm ngặt dài nhất với hiệu năng tính toán tối ưu nhất có thể.",
        "nv": "Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình tìm độ dài dãy con tăng nghiêm ngặt dài nhất.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra một số nguyên duy nhất là độ dài của dãy con tăng dài nhất.",
        "gt": "Với dãy số gồm 6 phần tử $[10, 20, 10, 30, 20, 50]$:\nDãy con tăng dài nhất là $[10, 20, 30, 50]$ có độ dài bằng 4."
    },
    "CPPB-RNG-10": {
        "title": "Đoạn Con Có Tổng Lớn Nhất Trên Đoạn (Maximum Subarray Query)",
        "bc": "Một bảng giá vàng ghi nhận mức biến động giá qua $N$ ngày. Các nhà đầu tư muốn tra cứu xem trong một khoảng thời gian bất kỳ từ ngày $L$ đến ngày $R$, một đợt sóng tăng giá liên tiếp (đoạn con có tổng lớn nhất) có thể đem lại lợi nhuận tối đa là bao nhiêu.",
        "nv": "Cho mảng $A$ và $Q$ truy vấn gồm hai số $L, R$. Hãy tìm tổng lớn nhất của một đoạn con không rỗng nằm trọn vẹn bên trong đoạn $[L, R]$.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).\n- $Q$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $L$ và $R$.",
        "outp": "- Với mỗi truy vấn, in ra tổng đoạn con lớn nhất tìm được trên một dòng.",
        "gt": "Với mảng $[-2, 1, -3, 4, -1, 2, 1, -5, 4]$ và truy vấn đoạn từ vị trí 1 đến 9:\nĐoạn con liên tiếp có tổng lớn nhất là $[4, -1, 2, 1]$ mang lại tổng là $4 + (-1) + 2 + 1 = 6$."
    },
    "CPPB-RNG-11": {
        "title": "Đếm Số Điểm Trong Hình Chữ Nhật (2D Range Query)",
        "bc": "Một đài thiên văn số ghi nhận tọa độ mặt phẳng $(x_i, y_i)$ của $N$ ngôi sao trên bầu trời. Các nhà thiên văn học cần thực hiện các truy vấn: đếm xem có bao nhiêu ngôi sao nằm lọt vào bên trong một vùng quan sát hình chữ nhật có góc dưới trái $(x_1, y_1)$ và góc trên phải $(x_2, y_2)$.",
        "nv": "Cho danh sách tọa độ $N$ điểm và $Q$ truy vấn hình chữ nhật. Hãy lập trình đếm số lượng điểm nằm trong từng hình chữ nhật.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).\n- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $x_i, y_i$ ($1 \le x_i, y_i \le 10^5$).\n- $Q$ dòng tiếp theo, mỗi dòng chứa 4 số nguyên $x_1, y_1, x_2, y_2$.",
        "outp": "- Với mỗi truy vấn, in ra số lượng điểm nằm trong hình chữ nhật trên một dòng.",
        "gt": "Với 3 điểm $(1, 2), (2, 3), (4, 5)$ và vùng quan sát từ $(1, 1)$ đến $(3, 4)$:\nHai điểm $(1, 2)$ và $(2, 3)$ nằm trọn vẹn bên trong vùng hình chữ nhật. Điểm $(4, 5)$ nằm ngoài. Số điểm đếm được là 2."
    },
    "CPPB-RNG-12": {
        "title": "Cập Nhật Phân Đoạn Nâng Cao",
        "bc": "Một hệ thống lưới điện thông minh hỗ trợ thao tác đổi dấu đồng loạt toàn bộ điện áp trên một phân đoạn đường dây từ $L$ đến $R$ ($A_i \\to -A_i$), đồng thời hỗ trợ truy vấn tính tổng điện áp lớn nhất của một đoạn con bất kỳ.",
        "nv": "Cho mảng $A$ và các thao tác đảo dấu đoạn hoặc truy vấn tổng đoạn con lớn nhất. Hãy lập trình xử lý và in ra kết quả cho các thao tác truy vấn.",
        "inp": "- Dòng 1: Chứa hai số nguyên $N$ và $Q$ ($1 \le N, Q \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$.\n- Các dòng tiếp theo chứa các thao tác cập nhật và truy vấn.",
        "outp": "- In ra kết quả cho mỗi thao tác truy vấn trên một dòng.",
        "gt": "Sau thao tác đảo dấu đoạn, các giá trị âm biến thành dương giúp hình thành một đoạn con có tổng lớn nhất đạt giá trị tối ưu mới."
    },
    "CPPB-RNG-13": {
        "title": "Cây Fenwick 2D Tính Tổng Hình Chữ Nhật (2D BIT)",
        "bc": "Một bức ảnh kỹ thuật số dạng lưới $N \times M$ điểm ảnh, điểm ảnh tại ô $(r, c)$ có giá trị độ sáng $A_{r,c}$. Hệ thống camera cần hỗ trợ hai thao tác: tăng độ sáng tại một điểm ảnh cụ thể thêm $val$, và tính tổng độ sáng của toàn bộ các điểm ảnh nằm trong một vùng hình chữ nhật từ $(r_1, c_1)$ đến $(r_2, c_2)$.",
        "nv": "Cho ma trận độ sáng ban đầu và $Q$ thao tác thuộc hai dạng: cập nhật điểm ảnh hoặc truy vấn tổng vùng hình chữ nhật. Hãy in ra kết quả của các thao tác truy vấn.",
        "inp": "- Dòng 1: Chứa 3 số nguyên $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 10^5$).\n- Các dòng tiếp theo mô tả ma trận ban đầu và $Q$ thao tác.",
        "outp": "- Với mỗi thao tác truy vấn hình chữ nhật, in ra tổng độ sáng tương ứng trên một dòng.",
        "gt": "Với ma trận $3 \\times 3$ toàn số 1: Tổng độ sáng của hình chữ nhật con kích thước $2 \\times 2$ từ $(1, 1)$ đến $(2, 2)$ gồm 4 ô số 1, tổng bằng 4."
    },
    "CPPB-RNG-14": {
        "title": "Lazy Propagation — Cập Nhật & Truy Vấn Đoạn (Range Add Range Sum)",
        "bc": "Một tuyến đê biển dài $N$ mét, ban đầu mét đê thứ $i$ có độ cao $A_i$. Do điều kiện thi công đắp đập, công nhân sẽ cộng thêm đồng loạt một lượng phù sa có độ dày $V$ mét vào một đoạn đê liên tiếp từ mét thứ $L$ đến mét thứ $R$. Đồng thời, đoàn thanh tra liên tục kiểm tra tổng độ dày của các đoạn đê bất kỳ.",
        "nv": "Cho mảng $A$ và $Q$ thao tác: `1 L R V` (cộng $V$ vào tất cả các phần tử từ $L$ đến $R$) và `2 L R` (tính tổng các phần tử trong đoạn $[L, R]$). Hãy in ra kết quả cho các thao tác loại 2.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).\n- $Q$ dòng tiếp theo, mỗi dòng chứa một thao tác.",
        "outp": "- Với mỗi thao tác loại 2, in ra tổng các phần tử trên đoạn $[L, R]$ trên một dòng.",
        "gt": "Với mảng ban đầu $[1, 2, 3, 4, 5]$:\n- Cộng thêm 2 vào đoạn từ vị trí 2 đến 4: mảng trở thành $[1, 4, 5, 6, 5]$.\n- Truy vấn tổng đoạn từ 1 đến 5: $1 + 4 + 5 + 6 + 5 = 21$."
    },
    "CPPB-RNG-15": {
        "title": "Hệ Thống Quản Lý Dữ Liệu Olympic (Range Master)",
        "bc": "Một hệ thống máy chủ chấm thi Olympic Tin học Quốc tế quản lý dữ liệu điểm số của $N$ thí sinh. Hệ thống cần xử lý đồng thời nhiều loại truy vấn đa năng phức tạp: gán giá trị mới cho một đoạn, cộng thêm giá trị vào một đoạn, tính tổng đoạn, và tìm giá trị lớn nhất/nhỏ nhất trong đoạn.",
        "nv": "Cho mảng $A$ và $Q$ truy vấn đa năng. Hãy lập trình thực thi chính xác và in ra kết quả tương ứng cho từng yêu cầu truy vấn thông tin.",
        "inp": "- Dòng 1: Chứa hai số nguyên $N$ và $Q$ ($1 \le N, Q \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$.\n- $Q$ dòng tiếp theo chứa các thao tác mô tả theo quy ước bài toán.",
        "outp": "- In ra kết quả cho mỗi thao tác truy vấn trên một dòng.",
        "gt": "Hệ thống cập nhật linh hoạt các phân đoạn dữ liệu lớn và trả về tổng điểm cũng như điểm cực trị chính xác cho ban giám khảo trong thời gian thực."
    }
}
