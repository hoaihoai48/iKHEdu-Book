# enrich_data_dp2.py
# Dữ liệu chuẩn hóa Sư phạm 15 bài DP2 (CPPB-DP2-01 -> CPPB-DP2-15)

DP2_DATA = {
    "CPPB-DP2-01": {
        "title": "Đếm Số Cách Đi Trên Lưới",
        "bc": "Một robot tự hành giao hàng được đặt ở góc trên bên trái (ô $(1, 1)$) của một kho hàng hình chữ nhật có kích thước $N \times M$ ô vuông. Robot cần di chuyển đến điểm đích ở góc dưới bên phải (ô $(N, M)$) để dỡ kiện hàng. Do cấu trúc băng chuyền một chiều trong kho, robot chỉ được phép di chuyển sang ô kề cạnh bên phải (từ $(i, j)$ sang $(i, j + 1)$) hoặc đi xuống ô kề cạnh phía dưới (từ $(i, j)$ sang $(i + 1, j)$).",
        "nv": "Cho hai số nguyên dương $N$ và $M$ là kích thước của kho hàng. Hãy lập trình tính số lượng lộ trình di chuyển khác nhau để robot đến được điểm đích, lấy dư cho $10^9 + 7$.",
        "inp": "- Một dòng duy nhất chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$) biểu diễn số hàng và số cột của lưới.",
        "outp": "- In ra trên một dòng duy nhất số lượng lộ trình hợp lệ theo modulo $10^9 + 7$.",
        "gt": "Với lưới kích thước $3 \times 3$ ($N = 3, M = 3$), robot cần thực hiện đúng 2 bước sang phải và 2 bước xuống dưới. Có tất cả 6 đường đi khác nhau từ $(1, 1)$ đến $(3, 3)$. Kết quả là 6."
    },
    "CPPB-DP2-02": {
        "title": "Đường Đi Trên Lưới Có Vật Cản",
        "bc": "Vẫn trên lưới ô vuông $N \times M$ của kho hàng, robot tự hành cần đi từ ô $(1, 1)$ đến ô $(N, M)$. Tuy nhiên, trong kho có một số vị trí đang được sửa chữa hoặc chứa các cọc hàng cố định (vật cản). Các ô trống được ký hiệu bằng số `0` (robot có thể đi vào), còn các ô vật cản được ký hiệu bằng số `1` (robot tuyệt đối không được đi vào). Robot vẫn chỉ được phép di chuyển sang phải hoặc xuống dưới.",
        "nv": "Cho bản đồ kho hàng kích thước $N \times M$. Hãy lập trình đếm số cách đi từ ô $(1, 1)$ tới ô $(N, M)$ mà không đi qua bất kỳ ô vật cản nào, lấy dư cho $10^9 + 7$. (Nếu ô xuất phát $(1, 1)$ hoặc ô đích $(N, M)$ có vật cản, robot không thể bắt đầu hoặc kết thúc hành trình, in ra `0`).",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên `0` hoặc `1` cách nhau bởi khoảng trắng biểu diễn bản đồ kho.",
        "outp": "- In ra trên một dòng duy nhất số đường đi hợp lệ theo modulo $10^9 + 7$.",
        "gt": "Với lưới $3 \times 3$ và có vật cản tại ô $(2, 2)$:\nCác đường đi ban đầu đi qua ô tâm $(2, 2)$ đều bị phong tỏa. Do đó chỉ còn lại đúng 2 đường đi men theo rìa ngoài (xuống hết hàng dưới rồi rẽ phải, hoặc sang hết cột phải rồi rẽ xuống). Kết quả in ra là 2."
    },
    "CPPB-DP2-03": {
        "title": "Đường Đi Chi Phí Nhỏ Nhất Trên Lưới",
        "bc": "Một tuyến cáp quang ngầm cần được thi công băng qua khu vực địa chất hình chữ nhật $N \times M$ ô. Mỗi ô $(i, j)$ có chi phí khoan đào đất đá tương ứng là $A_{i,j}$. Tuyến cáp bắt đầu từ trạm phát tín hiệu tại ô $(1, 1)$ và kết thúc tại trạm thu ở ô $(N, M)$. Để hạn chế tối đa góc uốn cong của dây cáp, hướng thi công chỉ được tiến sang phải hoặc xuống dưới.",
        "nv": "Cho ma trận chi phí của lưới $N \times M$. Hãy lập trình tìm tổng chi phí khoan đào nhỏ nhất để hoàn thành tuyến cáp từ ô $(1, 1)$ tới ô $(N, M)$.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên không âm $A_{i,j}$ ($0 \le A_{i,j} \le 10^4$).",
        "outp": "- In ra trên một dòng duy nhất tổng chi phí nhỏ nhất tìm được.",
        "gt": "Với ma trận chi phí kích thước $3 \times 3$:\nLộ trình có chi phí nhỏ nhất là đi qua các ô $(1,1) \to (1,2) \to (2,2) \to (2,3) \to (3,3)$ hoặc tương đương, mang lại tổng chi phí tối thiểu là 12."
    },
    "CPPB-DP2-04": {
        "title": "Nhặt Vàng Trên Lưới",
        "bc": "Trong một trò chơi phiêu lưu, một nhà khảo cổ học thám hiểm một lăng mộ cổ hình chữ nhật gồm $N \times M$ gian phòng. Gian phòng tại tọa độ $(i, j)$ chứa một số thỏi vàng có giá trị là $A_{i,j}$. Nhà khảo cổ xuất phát từ căn phòng $(1, 1)$ và cần thoát ra ở căn phòng $(N, M)$. Do cơ chế bẫy cát một chiều, nhà khảo cổ chỉ có thể di chuyển sang phòng bên phải hoặc phòng phía dưới.",
        "nv": "Cho ma trận số vàng tại các gian phòng. Hãy lập trình tìm tổng số vàng lớn nhất mà nhà khảo cổ có thể thu thập được trên đường thoát ra.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên không âm $A_{i,j}$ ($0 \le A_{i,j} \le 10^4$).",
        "outp": "- In ra trên một dòng duy nhất tổng lượng vàng lớn nhất có thể thu thập.",
        "gt": "Với lưới vàng kích thước $3 \times 3$:\nLộ trình thu thập tối ưu là đi qua các gian phòng có lượng vàng phong phú nhất, đạt tổng giá trị lớn nhất là 15."
    },
    "CPPB-DP2-05": {
        "title": "Cái Túi 0/1 Cơ Bản (0/1 Knapsack)",
        "bc": "Một nhà thám hiểm chuẩn bị hành trang cho chuyến đi băng rừng. Có $N$ vật phẩm sinh tồn, vật phẩm thứ $i$ có khối lượng là $w_i$ và giá trị sử dụng là $v_i$. Nhà thám hiểm mang theo một chiếc ba lô có sức chứa tải trọng tối đa là $W$. Mỗi vật phẩm chỉ có duy nhất một chiếc (chọn lấy hoặc không lấy).",
        "nv": "Cho danh sách khối lượng và giá trị của $N$ vật phẩm cùng tải trọng $W$. Hãy lập trình chọn ra một tập hợp vật phẩm sao cho tổng khối lượng không vượt quá $W$ và tổng giá trị mang lại là lớn nhất.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $W$ ($1 \le N \le 1000, 1 \le W \le 1000$).\n- $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên dương $w_i$ và $v_i$ ($1 \le w_i, v_i \le 1000$) lần lượt là khối lượng và giá trị của món đồ thứ $i$.",
        "outp": "- In ra trên một dòng duy nhất tổng giá trị lớn nhất có thể xếp vào ba lô.",
        "gt": "Với 4 đồ vật có thông số [(khối lượng 2, giá trị 3), (3, 4), (4, 5), (5, 6)] và ba lô có sức chứa $W = 5$:\nPhương án tối ưu là chọn đồ vật 1 ($w = 2, v = 3$) và đồ vật 2 ($w = 3, v = 4$). Tổng khối lượng là $2 + 3 = 5 \le 5$, đạt tổng giá trị tối đa là $3 + 4 = 7$."
    },
    "CPPB-DP2-06": {
        "title": "Cái Túi Không Giới Hạn (Unbounded Knapsack)",
        "bc": "Một phân xưởng kim hoàn nhập khẩu $N$ loại phôi kim loại quý. Loại phôi thứ $i$ có khối lượng $w_i$ và giá trị thành phẩm là $v_i$. Phân xưởng có một lò luyện với sức chứa tối đa là $W$. Điểm đặc biệt là kho nguyên liệu có số lượng phôi kim loại của mỗi loại dồi dào không giới hạn (có thể chọn nhiều lần cùng một loại phôi).",
        "nv": "Cho $N$ loại phôi và tải trọng lò luyện $W$. Hãy lập trình chọn các phôi sao cho tổng khối lượng không vượt quá $W$ và tổng giá trị thu được là lớn nhất.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $W$ ($1 \le N \le 1000, 1 \le W \le 1000$).\n- $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên dương $w_i$ và $v_i$ ($1 \le w_i, v_i \le 1000$).",
        "outp": "- In ra trên một dòng duy nhất tổng giá trị lớn nhất đạt được.",
        "gt": "Với tải trọng $W = 100$ và cho phép chọn không giới hạn số lượng mỗi loại:\nTa có thể chọn lặp lại nhiều lần loại phôi có hiệu suất giá trị trên khối lượng cao nhất để đạt tổng giá trị tối đa là 150."
    },
    "CPPB-DP2-07": {
        "title": "Truy Vết Món Đồ Cái Túi 0/1",
        "bc": "Sau khi tính toán được giá trị tài sản tối ưu xếp vào ba lô, nhà thám hiểm cần in ra danh sách chi tiết các món đồ cụ thể đã được chọn để bàn giao cho tổ hậu cần đóng gói hành lý.",
        "nv": "Cho $N$ đồ vật (mỗi vật có khối lượng $w_i$, giá trị $v_i$) và sức chứa ba lô $W$. Hãy lập trình in ra tổng giá trị lớn nhất và chỉ số (1-indexed) của các món đồ được chọn.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $W$ ($1 \le N \le 1000, 1 \le W \le 1000$).\n- $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên dương $w_i$ và $v_i$ ($1 \le w_i, v_i \le 1000$).",
        "outp": "- Dòng 1: In ra tổng giá trị lớn nhất.\n- Dòng 2: In ra số lượng món đồ được chọn $K$.\n- Dòng 3: In ra $K$ số nguyên là chỉ số của các món đồ được chọn theo thứ tự tăng dần.",
        "gt": "Với $N = 3, W = 4$ và các đồ vật $[(2, 3), (1, 2), (3, 4)]$:\nChọn món đồ 1 (nặng 2, giá trị 3) và món đồ 2 (nặng 1, giá trị 2). Tổng khối lượng là $2 + 1 = 3 \le 4$, tổng giá trị là $3 + 2 = 5$. Danh sách món đồ chọn là 1 và 2."
    },
    "CPPB-DP2-08": {
        "title": "Chia Tập Thành Hai Phần Bằng Nhau (Partition Equal Subset Sum)",
        "bc": "Một gia đình có hai người con được thừa kế $N$ thửa đất. Thửa đất thứ $i$ có giá trị thẩm định là $A_i$. Người cha muốn chia toàn bộ $N$ thửa đất thành hai phần sao cho mỗi người con nhận được tổng giá trị tài sản hoàn toàn bằng nhau mà không cần phải xẻ nhỏ bất kỳ thửa đất nào.",
        "nv": "Cho danh sách giá trị của $N$ thửa đất. Hãy lập trình kiểm tra xem có thể phân chia tập thửa đất thành hai tập con có tổng giá trị bằng nhau hay không. Nếu được in ra `YES`, ngược lại in ra `NO`.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 200$).\n- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 100$).",
        "outp": "- In ra `YES` nếu có thể chia đều thành hai phần bằng nhau, ngược lại in ra `NO`.",
        "gt": "Với tập hợp các số $[1, 5, 11, 5]$:\nTổng của toàn bộ dãy số là $1 + 5 + 11 + 5 = 22$. Ta có thể chia thành hai tập con $\{1, 5, 5\}$ và $\{11\}$, mỗi tập đều có tổng đúng bằng 11. Do đó kết quả in ra là YES."
    },
    "CPPB-DP2-09": {
        "title": "Chia Tập Chênh Lệch Nhỏ Nhất (Minimum Subset Sum Difference)",
        "bc": "Trong một giải đấu thể thao điện tử (E-sports), có $N$ tuyển thủ tham dự với chỉ số kỹ năng lần lượt là $A_1, A_2, \dots, A_N$. Ban tổ chức cần chia toàn bộ $N$ tuyển thủ thành hai đội thi đấu sao cho độ chênh lệch về tổng kỹ năng giữa hai đội là nhỏ nhất có thể, nhằm tạo ra một trận đấu cân tài cân sức.",
        "nv": "Cho danh sách điểm kỹ năng của $N$ tuyển thủ. Hãy lập trình tìm độ chênh lệch nhỏ nhất giữa tổng điểm của hai đội.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 200$).\n- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 100$).",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là độ chênh lệch nhỏ nhất có thể đạt được.",
        "gt": "Với tập hợp kỹ năng $[1, 6, 11, 5]$:\nTổng toàn bộ kỹ năng là $1 + 6 + 11 + 5 = 23$. Ta chia thành hai đội với các tuyển thủ $\{1, 11\}$ (tổng kỹ năng 12) và $\{6, 5\}$ (tổng kỹ năng 11). Độ chênh lệch giữa hai đội là $|12 - 11| = 1$. Đây là mức chênh lệch nhỏ nhất."
    },
    "CPPB-DP2-10": {
        "title": "Tam Giác Số Tổng Lớn Nhất (Triangle DP)",
        "bc": "Một kim tự tháp số có $N$ tầng được đánh số từ $1$ đến $N$. Tầng thứ $i$ chứa đúng $i$ số nguyên. Một nhà leo núi xuất phát từ đỉnh kim tự tháp (tầng 1) và đi dần xuống đáy (tầng $N$). Tại mỗi bước từ vị trí $(i, j)$ ở tầng $i$, nhà leo núi chỉ có thể bước xuống một trong hai vị trí kề cạnh ở tầng $i + 1$: hoặc ô $(i + 1, j)$ hoặc ô $(i + 1, j + 1)$.",
        "nv": "Cho cấu trúc kim tự tháp số $N$ tầng. Hãy lập trình tìm đường đi từ đỉnh xuống đáy sao cho tổng các số trên đường đi là lớn nhất.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$) biểu diễn số tầng của kim tự tháp.\n- $N$ dòng tiếp theo, dòng thứ $i$ chứa $i$ số nguyên $A_{i,j}$ ($0 \le A_{i,j} \le 10^4$).",
        "outp": "- In ra trên một dòng duy nhất tổng lớn nhất thu được.",
        "gt": "Với tam giác số gồm 4 tầng:\n  3\n  7 4\n  2 4 6\n  8 5 9 3\nĐường đi mang lại tổng lớn nhất là $3 \to 7 \to 4 \to 9$, cho tổng lớn nhất là $3 + 7 + 4 + 9 = 23$."
    },
    "CPPB-DP2-11": {
        "title": "Đếm Số Tập Con Có Tổng Bằng S",
        "bc": "Tại một phòng thí nghiệm hóa học, các nhà nghiên cứu có $N$ lọ dung dịch chuẩn, lọ thứ $i$ có thể tích là $A_i$ (ml). Để phục vụ một thí nghiệm chuẩn độ chính xác, nhóm nghiên cứu cần pha chế một hỗn hợp có tổng thể tích đúng bằng $S$ (ml) bằng cách trộn nguyên vẹn một số lọ dung dịch lại với nhau.",
        "nv": "Cho danh sách thể tích $N$ lọ dung dịch và thể tích mục tiêu $S$. Hãy lập trình đếm xem có bao nhiêu cách chọn một tập hợp các lọ dung dịch sao cho tổng thể tích đúng bằng $S$, lấy dư cho $10^9 + 7$.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $S$ ($1 \le N \le 1000, 1 \le S \le 1000$).\n- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 1000$).",
        "outp": "- In ra số lượng cách chọn hợp lệ theo modulo $10^9 + 7$.",
        "gt": "Với mảng dung dịch $[1, 2, 3, 3]$ và thể tích cần lấy $S = 6$:\nCó 3 cách chọn tập con có tổng bằng 6:\n1. Chọn các phần tử tại vị trí 1, 2, 3: $1 + 2 + 3 = 6$.\n2. Chọn các phần tử tại vị trí 1, 2, 4: $1 + 2 + 3 = 6$.\n3. Chọn các phần tử tại vị trí 3, 4: $3 + 3 = 6$.\nKết quả in ra là 3."
    },
    "CPPB-DP2-12": {
        "title": "Cái Túi Khối Lượng Cực Đại W <= 10^9 (Đổi Trục DP)",
        "bc": "Một tàu thám hiểm không gian vũ trụ có khoang chứa hàng với tải trọng cực lớn lên tới $W = 10^9$ kg. Có $N$ mẫu vật thể ngoài hành tinh được đánh số từ $1$ đến $N$. Mẫu vật thứ $i$ có khối lượng $w_i$ lên tới $10^9$, nhưng giá trị khoa học $v_i$ lại khá nhỏ ($v_i \le 1000$). Tải trọng quá lớn khiến phương pháp thông thường không thể chạy trong bộ nhớ.",
        "nv": "Cho $N$ mẫu vật ($w_i, v_i$) và tải trọng $W \le 10^9$. Hãy lập trình tìm tổng giá trị khoa học lớn nhất có thể mang về trái đất sao cho tổng khối lượng không vượt quá $W$.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $W$ ($1 \le N \le 100, 1 \le W \le 10^9$).\n- $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên dương $w_i$ và $v_i$ ($1 \le w_i \le 10^9, 1 \le v_i \le 1000$).",
        "outp": "- In ra trên một dòng duy nhất tổng giá trị lớn nhất đạt được.",
        "gt": "Với $N = 3, W = 10$ và các mẫu vật $[(3, 30), (4, 50), (5, 60)]$:\nChọn mẫu vật 1 và mẫu vật 3 với tổng khối lượng $3 + 5 = 8 \le 10$, đạt tổng giá trị là $30 + 60 = 90$."
    },
    "CPPB-DP2-13": {
        "title": "Hình Vuông Toàn 1 Lớn Nhất (Maximal Square)",
        "bc": "Một cảm biến vệ tinh chụp bức ảnh mặt đất độ phân giải cao dạng ma trận nhị phân $N \times M$ điểm ảnh. Điểm ảnh mang giá trị `1` thể hiện khu vực đất nông nghiệp màu mỡ, còn điểm ảnh `0` thể hiện đất khô cằn. Một tập đoàn công nghệ muốn quy hoạch một trang trại thông minh có hình dạng hình vuông hoàn hảo chỉ nằm hoàn toàn trên vùng đất màu mỡ (toàn số `1`).",
        "nv": "Cho ma trận nhị phân $N \times M$. Hãy lập trình tìm độ dài cạnh lớn nhất của một hình vuông con chỉ chứa toàn số `1`.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa $M$ ký tự `0` hoặc `1` liền nhau hoặc cách nhau bởi khoảng trắng.",
        "outp": "- In ra trên một dòng duy nhất độ dài cạnh của hình vuông toàn số `1` lớn nhất tìm được.",
        "gt": "Với ma trận kích thước $4 \times 4$:\n1 0 1 0\n1 1 1 1\n1 1 1 0\n0 1 1 1\nHình vuông con toàn số 1 lớn nhất có kích thước $2 \times 2$ (độ dài cạnh bằng 2). Kết quả in ra là 2."
    },
    "CPPB-DP2-14": {
        "title": "Đổi Tiền Giới Hạn Số Lượng (Bounded Knapsack)",
        "bc": "Tại một cây ATM phân phối tiền mặt, máy chứa $N$ mệnh giá tiền khác nhau. Khác với trạm đổi tiền không giới hạn, ở đây mệnh giá thứ $i$ có giá trị $c_i$ và chỉ còn lại đúng $k_i$ tờ tiền trong khay tiền. Khách hàng muốn rút một khoản tiền đúng bằng $S$ đồng.",
        "nv": "Cho danh sách $N$ mệnh giá kèm số lượng tờ tiền tương ứng và số tiền cần rút $S$. Hãy lập trình tìm số lượng tờ tiền ít nhất để chi trả đúng số tiền $S$. Nếu khay tiền không thể đáp ứng, in ra `-1`.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $S$ ($1 \le N \le 100, 1 \le S \le 10^5$).\n- $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên dương $c_i$ và $k_i$ ($1 \le c_i \le 10^4, 1 \le k_i \le 1000$).",
        "outp": "- In ra số tờ tiền ít nhất cần dùng, hoặc `-1` nếu không thể chi trả chính xác số tiền $S$.",
        "gt": "Với số tiền cần rút $S = 10$ và các mệnh giá: 5 đồng (có 1 tờ), 2 đồng (có 3 tờ):\nChọn 1 tờ 5 đồng và 2 tờ 2 đồng ($5 + 2 \times 2 = 9 < 10$).\nPhương án đổi đúng là dùng 5 tờ 2 đồng (nhưng chỉ có 3 tờ nên không được).\nNếu có thêm mệnh giá 1 đồng (2 tờ): Dùng 1 tờ 5, 2 tờ 2 và 1 tờ 1, tổng cộng 4 tờ tiền."
    },
    "CPPB-DP2-15": {
        "title": "Tối Ưu Hóa Túi Đồ Hỗn Hợp (Hybrid Knapsack)",
        "bc": "Một trung tâm cứu hộ thiên tai chuẩn bị các gói hàng viện trợ để thả dù xuống vùng bão lũ. Có $N$ loại hàng hóa thiết yếu, mỗi loại có khối lượng $w_i$ và giá trị cứu trợ $v_i$. Tính chất nguồn cung của các mặt hàng rất đa dạng: một số mặt hàng chỉ có duy nhất 1 kiện (loại 0/1), một số mặt hàng được tài trợ không giới hạn (loại không giới hạn), và một số mặt hàng chỉ có số lượng cố định $k_i$ kiện (loại giới hạn). Khoang hàng máy bay có sức chứa tối đa là $W$.",
        "nv": "Cho danh sách $N$ loại hàng với đặc tính số lượng của từng loại và tải trọng khoang bay $W$. Hãy lập trình tìm tổng giá trị cứu trợ lớn nhất có thể vận chuyển.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $W$ ($1 \le N \le 1000, 1 \le W \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng mô tả một loại hàng: khối lượng $w_i$, giá trị $v_i$ và số lượng $k_i$ ($k_i = 0$ nghĩa là số lượng không giới hạn).",
        "outp": "- In ra trên một dòng duy nhất tổng giá trị cứu trợ lớn nhất đạt được.",
        "gt": "Với khoang máy bay có tải trọng $W = 15$ và danh mục hàng cứu trợ hỗn hợp:\nSự kết hợp tối ưu giữa các mặt hàng giới hạn và hàng không giới hạn đem lại tổng giá trị lớn nhất là 32."
    }
}
