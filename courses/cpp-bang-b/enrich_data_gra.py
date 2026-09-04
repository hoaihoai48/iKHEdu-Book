# enrich_data_gra.py
# Dữ liệu chuẩn hóa Sư phạm 15 bài GRA (CPPB-GRA-01 -> CPPB-GRA-15)

GRA_DATA = {
    "CPPB-GRA-01": {
        "title": "Chuyển Danh Sách Cạnh Sang Danh Sách Kề",
        "bc": "Một đồ thị mạng lưới giao thông gồm $N$ nút giao và $M$ con đường hai chiều ban đầu được lưu trữ dưới dạng danh sách các cặp cạnh $(u, v)$. Để thuận tiện cho việc lập trình các thuật toán tìm kiếm và duyệt đồ thị, kỹ sư cầu đường cần chuyển đổi dữ liệu mạng lưới sang cấu trúc danh sách kề: Với mỗi nút giao, liệt kê tất cả các nút giao có đường nối trực tiếp với nó theo thứ tự số hiệu tăng dần.",
        "nv": "Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Hãy lập trình chuyển đổi sang biểu diễn danh sách kề và in ra các đỉnh kề của từng đỉnh theo thứ tự tăng dần.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $u$ và $v$ ($1 \le u, v \le N, u \ne v$) biểu diễn một cạnh.",
        "outp": "- In ra $N$ dòng, dòng thứ $i$ bắt đầu bằng số thứ tự đỉnh $i$ kèm dấu hai chấm, theo sau là danh sách các đỉnh kề với $i$ theo thứ tự tăng dần.",
        "gt": "Với đồ thị 4 đỉnh và các cạnh (1, 2), (1, 3), (2, 4):\n- Đỉnh 1 kề với các đỉnh: 2, 3.\n- Đỉnh 2 kề với các đỉnh: 1, 4.\n- Đỉnh 3 kề với đỉnh: 1.\n- Đỉnh 4 kề với đỉnh: 2."
    },
    "CPPB-GRA-02": {
        "title": "Duyệt Đồ Thị Theo Chiều Sâu (DFS Traversal)",
        "bc": "Một robot thám hiểm cần khám phá toàn bộ các gian phòng trong một hang động ngầm gồm $N$ gian phòng và $M$ lối đi hai chiều. Robot áp dụng chiến lược tìm kiếm theo chiều sâu: Từ gian phòng hiện tại, luôn ưu tiên tiến sâu vào một gian phòng chưa từng được khám phá kề cạnh có số hiệu nhỏ nhất; khi không thể đi tiếp thì quay lui lại gian phòng trước đó.",
        "nv": "Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh và đỉnh xuất phát $S$. Hãy lập trình in ra thứ tự các đỉnh được robot ghé thăm trong quá trình duyệt theo chiều sâu (khi có nhiều lựa chọn, luôn ưu tiên đỉnh có số hiệu nhỏ hơn).",
        "inp": "- Dòng 1: Chứa 3 số nguyên $N, M, S$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5, 1 \le S \le N$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.",
        "outp": "- In ra trên một dòng thứ tự các đỉnh được ghé thăm trong hành trình, cách nhau bởi khoảng trắng.",
        "gt": "Với đồ thị 4 đỉnh gồm các cạnh (1, 2), (1, 3), (2, 4) xuất phát từ đỉnh 1:\n- Từ đỉnh 1 thăm đỉnh 2 (nhỏ hơn 3).\n- Từ đỉnh 2 tiếp tục thăm đỉnh 4.\n- Đỉnh 4 không còn đường mới, quay lui về 2, rồi về 1, từ 1 thăm tiếp đỉnh 3.\nThứ tự ghé thăm là: 1 2 4 3."
    },
    "CPPB-GRA-03": {
        "title": "Duyệt Đồ Thị Theo Chiều Rộng (BFS Traversal)",
        "bc": "Một thông điệp cảnh báo khẩn cấp cần được lan truyền qua một mạng xã hội gồm $N$ người dùng và $M$ mối quan hệ bạn bè. Xuất phát từ người dùng $S$, thông điệp sẽ được gửi đồng thời tới tất cả những người bạn trực tiếp của $S$ trước (tầng 1), sau đó mới tiếp tục lan truyền tới bạn của bạn (tầng 2) theo nguyên tắc loang theo chiều rộng (ưu tiên người có số hiệu nhỏ hơn).",
        "nv": "Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh và đỉnh xuất phát $S$. Hãy lập trình in ra thứ tự các đỉnh nhận được thông điệp theo chiến lược duyệt theo chiều rộng.",
        "inp": "- Dòng 1: Chứa 3 số nguyên $N, M, S$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5, 1 \le S \le N$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.",
        "outp": "- In ra trên một dòng thứ tự các đỉnh được ghé thăm, cách nhau bởi khoảng trắng.",
        "gt": "Với đồ thị có các cạnh (1, 2), (1, 3), (2, 4) xuất phát từ đỉnh 1:\n- Tầng 1 (kề trực tiếp với 1): thăm đỉnh 2 và đỉnh 3 theo thứ tự tăng dần.\n- Tầng 2: từ đỉnh 2 thăm tiếp đỉnh 4.\nThứ tự ghé thăm là: 1 2 3 4."
    },
    "CPPB-GRA-04": {
        "title": "Đếm Số Thành Phần Liên Thông",
        "bc": "Một quần đảo gồm $N$ hòn đảo và $M$ cây cầu hai chiều nối giữa một số cặp đảo. Hai hòn đảo thuộc cùng một cụm đảo liên thông nếu cư dân có thể đi lại giữa chúng qua các cây cầu (trực tiếp hoặc gián tiếp). Ban quản lý du lịch cần xác định xem toàn bộ quần đảo đang bị chia cắt thành bao nhiêu cụm đảo biệt lập.",
        "nv": "Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Hãy lập trình đếm số lượng thành phần liên thông của đồ thị.",
        "inp": "- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$.",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là số lượng thành phần liên thông.",
        "gt": "Với 5 đỉnh và các cạnh (1, 2), (3, 4):\n- Cụm 1 gồm các đỉnh {1, 2}.\n- Cụm 2 gồm các đỉnh {3, 4}.\n- Cụm 3 gồm đỉnh cô lập {5}.\nCó tất cả 3 thành phần liên thông độc lập, kết quả in ra là 3."
    },
    "CPPB-GRA-05": {
        "title": "Kích Thước Thành Phần Liên Thông Lớn Nhất",
        "bc": "Vẫn tại quần đảo gồm $N$ hòn đảo và $M$ cây cầu, ban quy hoạch kinh tế muốn tìm cụm đảo liên thông phát triển sầm uất nhất (chứa số lượng hòn đảo nhiều nhất) để đầu tư xây dựng trung tâm logistics tập trung.",
        "nv": "Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Hãy lập trình tìm số lượng đỉnh thuộc về thành phần liên thông có kích thước lớn nhất.",
        "inp": "- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$.",
        "outp": "- In ra trên một dòng duy nhất kích thước của thành phần liên thông lớn nhất.",
        "gt": "Với 5 đỉnh và các cạnh (1, 2), (2, 3), (4, 5):\n- Cụm 1 gồm {1, 2, 3} có 3 hòn đảo.\n- Cụm 2 gồm {4, 5} có 2 hòn đảo.\nKích thước của thành phần liên thông lớn nhất là 3."
    },
    "CPPB-GRA-06": {
        "title": "Kiểm Tra Đường Đi Giữa Hai Đỉnh",
        "bc": "Trong hệ thống mạng lưới điện quốc gia gồm $N$ trạm biến áp và $M$ đường dây tải điện hai chiều, trung tâm điều độ cần kiểm tra nhanh xem liệu có tồn tại tuyến đường dây kết nối (trực tiếp hoặc qua các trạm trung gian) giữa hai trạm biến áp $S$ và $D$ hay không.",
        "nv": "Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh và hai đỉnh $S, D$. Hãy lập trình kiểm tra xem có tồn tại đường đi giữa $S$ và $D$ hay không. Nếu có in ra `YES`, ngược lại in ra `NO`.",
        "inp": "- Dòng 1: Chứa 4 số nguyên $N, M, S, D$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5, 1 \le S, D \le N$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.",
        "outp": "- In ra `YES` nếu có đường đi giữa $S$ và $D$, ngược lại in ra `NO`.",
        "gt": "Với đồ thị có các cạnh (1, 2), (2, 3) và đỉnh 4 cô lập:\n- Kiểm tra giữa 1 và 3: Tồn tại đường đi $1 \to 2 \to 3$, in ra YES.\n- Nếu kiểm tra giữa 1 và 4: Không có đường đi, in ra NO."
    },
    "CPPB-GRA-07": {
        "title": "Phát Hiện Chu Trình Trên Đồ Thị Vô Hướng",
        "bc": "Một mạng lưới đường ống cấp nước đô thị cần được kiểm tra thiết kế. Nếu trong mạng lưới xuất hiện một chu trình khép kín (một vòng tròn đường ống quay về điểm xuất phát mà không đi lặp lại cạnh nào), áp lực nước có thể bị nhiễu loạn dòng chảy. Kỹ sư thủy lợi cần kiểm tra xem bản vẽ mạng lưới có chứa chu trình hay không.",
        "nv": "Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Hãy lập trình kiểm tra xem đồ thị có chứa chu trình hay không. Nếu có in ra `YES`, ngược lại in ra `NO`.",
        "inp": "- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.",
        "outp": "- In ra `YES` nếu đồ thị chứa ít nhất một chu trình, ngược lại in ra `NO`.",
        "gt": "Với đồ thị gồm 3 đỉnh có các cạnh (1, 2), (2, 3), (3, 1):\nBa đỉnh này tạo thành một tam giác khép kín $1 - 2 - 3 - 1$, là một chu trình hoàn chỉnh. Kết quả in ra là YES."
    },
    "CPPB-GRA-08": {
        "title": "Đường Đi Ngắn Nhất Trên Đồ Thị Không Trọng Số",
        "bc": "Một đoàn tàu hỏa vận chuyển hàng hóa di chuyển trên mạng lưới đường ray gồm $N$ nhà ga và $M$ chặng ray hai chiều nối giữa các ga kề nhau. Đoàn tàu cần đi từ ga xuất phát $S$ đến ga đích $D$. Mỗi chặng ray mất đúng 1 giờ chạy tàu. Hãy tìm thời gian ít nhất (tổng số chặng ray ít nhất) để tàu đến được ga đích.",
        "nv": "Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh và hai đỉnh $S, D$. Hãy lập trình tìm số cạnh trên đường đi ngắn nhất từ $S$ tới $D$. Nếu không có đường đi, in ra `-1`.",
        "inp": "- Dòng 1: Chứa 4 số nguyên $N, M, S, D$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.",
        "outp": "- In ra số cạnh ngắn nhất từ $S$ tới $D$, hoặc `-1` nếu không có đường đi.",
        "gt": "Với mạng đường ray có các chặng (1, 2), (2, 3), (1, 4), (4, 3) từ ga 1 tới ga 3:\nCó hai lộ trình cùng đạt 2 chặng là $1 \to 2 \to 3$ hoặc $1 \to 4 \to 3$. Thời gian ít nhất là 2 chặng."
    },
    "CPPB-GRA-09": {
        "title": "Kiểm Tra Đồ Thị Cây (Tree Verification)",
        "bc": "Trong cấu trúc liên kết mạng máy tính, cấu trúc dạng cây (Tree) là mô hình mạng tối ưu nhất vì nó đảm bảo tất cả $N$ máy chủ đều liên thông với nhau mà hoàn toàn không có chu trình dư thừa (số lượng kênh kết nối đúng bằng $N - 1$). Kỹ sư hệ thống cần xác thực xem một mạng lưới cho trước có thỏa mãn đầy đủ các điều kiện của một đồ thị cây hay không.",
        "nv": "Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Hãy lập trình kiểm tra xem đồ thị có phải là một cây hợp lệ hay không. Nếu đúng in ra `YES`, ngược lại in ra `NO`.",
        "inp": "- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$.",
        "outp": "- In ra `YES` nếu đồ thị là cây, ngược lại in ra `NO`.",
        "gt": "Với đồ thị có $N = 4$ đỉnh và $M = 3$ cạnh: (1, 2), (1, 3), (1, 4):\nĐồ thị liên thông toàn bộ và không chứa bất kỳ chu trình nào, số cạnh đúng bằng $4 - 1 = 3$. Đồ thị là một cây, kết quả in ra là YES."
    },
    "CPPB-GRA-10": {
        "title": "Sắp Xếp Tô-pô (Topological Sort)",
        "bc": "Một chương trình đào tạo kỹ sư công nghệ thông tin gồm $N$ môn học được đánh số từ $1$ đến $N$. Giữa các môn học có $M$ điều kiện môn tiên quyết dạng $u \to v$ (nghĩa là sinh viên bắt buộc phải hoàn thành môn học $u$ trước khi được phép đăng ký môn học $v$). Ban đào tạo cần lập ra một lộ trình học tập hợp lệ thỏa mãn tất cả các điều kiện tiên quyết.",
        "nv": "Cho đồ thị có hướng $N$ đỉnh $M$ cạnh không có chu trình. Hãy lập trình tìm một thứ tự sắp xếp tô-pô của các môn học.",
        "inp": "- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$ biểu diễn điều kiện môn $u$ học trước môn $v$.",
        "outp": "- In ra trên một dòng gồm $N$ số nguyên là thứ tự các môn học hợp lệ, cách nhau bởi khoảng trắng.",
        "gt": "Với 3 môn học và các điều kiện: môn 1 trước môn 2 ($1 \to 2$), môn 2 trước môn 3 ($2 \to 3$):\nLộ trình học tập bắt buộc duy nhất là: 1 2 3."
    },
    "CPPB-GRA-11": {
        "title": "Chu Trình Ngắn Nhất Trên Đồ Thị (Girth)",
        "bc": "Trong nghiên cứu cấu trúc phân tử hóa học của các hợp chất vòng hữu cơ, các nhà hóa học cần xác định chu trình vòng có kích thước nhỏ nhất (chu vi nhỏ nhất - Girth) xuất hiện trong đồ thị liên kết nguyên tử.",
        "nv": "Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh không có khuyên và không có cạnh bội. Hãy lập trình tìm độ dài của chu trình có số cạnh nhỏ nhất trong đồ thị. Nếu đồ thị không có chu trình nào, in ra `-1`.",
        "inp": "- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 2000, 0 \le M \le 2000$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.",
        "outp": "- In ra độ dài chu trình ngắn nhất, hoặc `-1` nếu đồ thị không có chu trình.",
        "gt": "Với đồ thị gồm 4 đỉnh có các cạnh (1, 2), (2, 3), (3, 4), (4, 1) và đường chéo (1, 3):\n- Chu trình tạo bởi 1-2-3-1 có độ dài 3.\n- Chu trình tạo bởi 1-3-4-1 có độ dài 3.\n- Chu trình ngoài 1-2-3-4-1 có độ dài 4.\nChu trình có độ dài nhỏ nhất là 3."
    },
    "CPPB-GRA-12": {
        "title": "Đếm Cặp Đỉnh Không Thể Đi Tới Nhau",
        "bc": "Một mạng viễn thông quốc gia gồm $N$ trạm phát sóng và $M$ đường truyền hai chiều. Do ảnh hưởng của bão lớn làm đứt một số đường truyền, mạng lưới bị chia cắt thành nhiều khu vực biệt lập. Hãy đếm xem có tất cả bao nhiêu cặp trạm $(u, v)$ với $u < v$ mà hiện tại không thể gửi tín hiệu liên lạc được cho nhau.",
        "nv": "Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Hãy lập trình đếm số lượng cặp đỉnh $(u, v)$ ($1 \le u < v \le N$) không có đường đi giữa chúng.",
        "inp": "- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$.",
        "outp": "- In ra trên một dòng duy nhất số lượng cặp đỉnh không liên thông.",
        "gt": "Với 4 đỉnh và chỉ có 1 cạnh nối (1, 2):\n- Cụm 1 gồm {1, 2}.\n- Đỉnh 3 cô lập, đỉnh 4 cô lập.\nCác cặp không đi tới nhau gồm: (1, 3), (1, 4), (2, 3), (2, 4), (3, 4). Có tổng cộng 5 cặp."
    },
    "CPPB-GRA-13": {
        "title": "Lan Tỏa Virus Trong Mạng Lưới (Multi-Source BFS)",
        "bc": "Trong một cuộc tấn công không gian mạng giả định, có $N$ máy tính được kết nối bởi $M$ kênh mạng hai chiều. Ban đầu tại thời điểm $t = 0$, có $K$ máy tính bị nhiễm mã độc virus. Cứ sau mỗi giây, các máy tính đã bị nhiễm sẽ lây truyền virus sang tất cả các máy tính kề sát với nó trong mạng lưới. Hãy tính thời gian (tính bằng giây) để toàn bộ các máy tính trong mạng đều bị lây nhiễm.",
        "nv": "Cho đồ thị mạng và danh sách $K$ máy tính bị nhiễm ban đầu. Hãy lập trình tính thời gian để toàn bộ máy tính trong thành phần liên thông bị nhiễm.",
        "inp": "- Dòng 1: Chứa 3 số nguyên $N, M, K$ ($1 \le K \le N \le 10^5, 0 \le M \le 2 \times 10^5$).\n- Dòng 2: Chứa $K$ số nguyên là chỉ số các máy tính nhiễm bệnh ban đầu.\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.",
        "outp": "- In ra thời gian tối đa để lây lan hết mạng lưới.",
        "gt": "Với 5 máy tính nối thành đường thẳng 1 - 2 - 3 - 4 - 5 và máy 3 bị nhiễm ban đầu:\n- Giây 1: máy 3 lây sang máy 2 và 4.\n- Giây 2: máy 2 lây sang 1, máy 4 lây sang 5.\nSau đúng 2 giây toàn bộ mạng lưới đều bị lây nhiễm, kết quả là 2."
    },
    "CPPB-GRA-14": {
        "title": "Đếm Số Cạnh Cầu Trên Đồ Thị (Bridges)",
        "bc": "Một hệ thống giao thông đường thủy gồm $N$ cảng biển và $M$ tuyến hải trình. Một tuyến hải trình được gọi là một tuyến cầu hiểm yếu nếu khi tuyến này bị gián đoạn (phong tỏa), số lượng cụm cảng bị chia cắt biệt lập sẽ tăng lên. Kỹ sư an ninh hàng hải cần thống kê số lượng các tuyến hiểm yếu này để ưu tiên bố trí lực lượng tuần tra bảo vệ.",
        "nv": "Cho đồ thị vô hướng liên thông $N$ đỉnh $M$ cạnh. Hãy lập trình đếm số lượng cạnh cầu trong đồ thị.",
        "inp": "- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$.",
        "outp": "- In ra trên một dòng duy nhất số lượng cạnh cầu tìm được.",
        "gt": "Với đồ thị gồm 4 đỉnh có các cạnh (1, 2), (2, 3), (3, 4):\nNếu bỏ bất kỳ cạnh nào trong số 3 cạnh trên, đồ thị đều bị chia đôi thành 2 phần rời nhau. Do đó cả 3 cạnh đều là cạnh cầu, kết quả in ra là 3."
    },
    "CPPB-GRA-15": {
        "title": "Xây Dựng Thêm Đường Nối Toàn Mạng (Building Roads)",
        "bc": "Một vương quốc gồm $N$ thành phố nhưng hiện tại hệ thống đường sá chỉ có $M$ con đường, khiến nhiều thành phố bị cô lập không thể đi tới nhau. Nhà vua muốn xây dựng thêm một số lượng con đường mới ít nhất nối giữa các thành phố sao cho sau khi hoàn thành, cư dân từ bất kỳ thành phố nào cũng có thể di chuyển tới mọi thành phố khác trong vương quốc.",
        "nv": "Cho bản đồ vương quốc hiện tại. Hãy lập trình tìm số lượng đường mới ít nhất cần xây dựng và chỉ rõ danh sách các con đường cần làm thêm.",
        "inp": "- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh biểu diễn một con đường hiện có.",
        "outp": "- Dòng 1: In ra số nguyên $K$ là số lượng con đường ít nhất cần xây thêm.\n- $K$ dòng tiếp theo, mỗi dòng in ra hai thành phố cần nối đường mới.",
        "gt": "Với 4 thành phố và chỉ có 1 đường nối giữa (1, 2) và 1 đường nối giữa (3, 4):\nVương quốc đang bị chia thành 2 cụm độc lập {1, 2} và {3, 4}. Ta chỉ cần xây thêm đúng 1 con đường nối giữa thành phố 2 và thành phố 3 là toàn bộ 4 thành phố sẽ liên thông hoàn chỉnh."
    }
}
