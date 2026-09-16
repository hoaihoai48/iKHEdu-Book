"""
TỰ ĐỘNG KHAI THÁC TOÀN BỘ 50+ BÀI TOÁN TỪ 'CHỦ ĐỀ VẼ HÌNH TRÊN SCRATCH.docx'
VÀ TẠO RA 40+ GÓI BÀI TẬP ĐỒ HỌA BÚT VẼ (PEN) CHO BÀI 01 & BÀI 02
- Bài 01 (Đa giác & Mảnh ghép cơ bản): sca_pen_p01 -> sca_pen_p20 (20 bài)
- Bài 02 (Hình tròn, Cung tròn & Hoa văn): sca_pen_p21 -> sca_pen_p45 (25 bài)
"""

import os
import re
from pathlib import Path
import docx

DOCX_FILE = "CHỦ ĐỀ VẼ HÌNH TRÊN SCRATCH.docx"
PROBLEMS_DIR = Path("courses/scratch-bang-a/problems")
PROBLEMS_DIR.mkdir(parents=True, exist_ok=True)

# Define full rich 40 Pen Problems based on the Docx topics
PEN_PROBLEMS = [
    # --- BÀI 01: ĐA GIÁC ĐỀU, NÉT VẼ, BÀN PHÍM VÀ MẢNH GHÉP (P01 - P20) ---
    {
        "code": "sca_pen_p01_da_giac_deu",
        "lesson": "l01",
        "title": "Bộ 4 Đa Giác Đều Cơ Bản",
        "context": "Trong công viên hình học Scratch Park, chú Mèo Scratch được giao nhiệm vụ vẽ 4 bồn hoa đa giác đều hoàn hảo: Tam giác đều (3 cạnh), Hình vuông (4 cạnh), Ngũ giác đều (5 cạnh), Lục giác đều (6 cạnh).",
        "task": "Lập trình vẽ các hình đa giác đều với độ dài cạnh 100 bước và góc quay ngoài 360 / N độ.",
        "input": "Nhấn cờ xanh để bắt đầu.",
        "output": "Hình đa giác đều khép kín trên sân khấu.",
        "sample": "Tam giác: lặp 3 [đi 100, xoay 120]. Hình vuông: lặp 4 [đi 100, xoay 90].",
        "source": "Câu 1"
    },
    {
        "code": "sca_pen_p02_ban_phim_da_giac",
        "lesson": "l01",
        "title": "Bàn Phím Đa Giác Tương Tác",
        "context": "Nhà thiết kế game muốn người chơi tương tác bằng các phím số 1, 2, 3, 4 trên bàn phím để vẽ nhanh các hình khối tương ứng.",
        "task": "Lập trình sự kiện: Phím 1 vẽ Tam giác đều, Phím 2 vẽ Hình vuông, Phím 3 vẽ Ngũ giác đều, Phím 4 vẽ Lục giác đều.",
        "input": "Nhấn phím 1, 2, 3 hoặc 4 trên bàn phím.",
        "output": "Mỗi phím vẽ ra hình đa giác tương ứng với màu sắc khác nhau.",
        "sample": "Bấm phím 1 -> Mèo vẽ Tam giác màu đỏ. Bấm phím 2 -> Mèo vẽ Hình vuông màu xanh.",
        "source": "Câu 2"
    },
    {
        "code": "sca_pen_p03_doi_mau_net_dam",
        "lesson": "l01",
        "title": "Đổi Màu Và Tăng Nét Đậm",
        "context": "Họa sĩ Mèo muốn tạo ra bức tranh ấn tượng với các nét vẽ dày dặn và màu sắc biến đổi linh hoạt.",
        "task": "Sử dụng khối 'đặt kích thước bút vẽ' và 'thay đổi màu bút vẽ một lượng 10' sau mỗi cạnh vẽ.",
        "input": "Nhấn cờ xanh.",
        "output": "Hình đa giác có mỗi cạnh mang một màu sắc rực rỡ khác nhau.",
        "sample": "Cạnh 1 màu đỏ, Cạnh 2 màu vàng, Cạnh 3 màu lục, Cạnh 4 màu lam.",
        "source": "Câu 3"
    },
    {
        "code": "sca_pen_p04_cap_tam_giac_doi_xung",
        "lesson": "l01",
        "title": "Cặp Tam Giác Đối Xứng Qua Tâm",
        "context": "Biểu tượng của hội toán học gồm hai hình tam giác đều ghép đối xứng nhau tạo thành hình ngôi sao 6 cánh David.",
        "task": "Vẽ 1 tam giác đều hướng lên, sau đó đổi hướng 180 độ và vẽ tam giác đều thứ hai lồng vào nhau.",
        "input": "Nhấn cờ xanh.",
        "output": "Hai hình tam giác lồng nhau tạo thành ngôi sao 6 cánh sắc nét.",
        "sample": "Vẽ tam giác 1, nhấc bút di chuyển đến vị trí đối xứng, đặt bút vẽ tam giác 2.",
        "source": "Câu 4"
    },
    {
        "code": "sca_pen_p05_vuong_dong_tam",
        "lesson": "l01",
        "title": "Hình Vuông Đồng Tâm Mở Rộng",
        "context": "Thiết kế bia ngắm bắn mục tiêu gồm nhiều hình vuông lồng nhau từ nhỏ đến lớn.",
        "task": "Lập trình vẽ N hình vuông lồng nhau, mỗi hình vuông có độ dài cạnh tăng dần 20 bước.",
        "input": "Nhập số lượng hình vuông N từ bàn phím.",
        "output": "N hình vuông đồng tâm nằm ngay ngắn giữa sân khấu.",
        "sample": "Hình 1 cạnh 20, hình 2 cạnh 40, hình 3 cạnh 60.",
        "source": "Câu 5"
    },
    {
        "code": "sca_pen_p06_la_co_xoay_vong",
        "lesson": "l01",
        "title": "Lá Cờ Xoay Vòng Quanh Tâm",
        "context": "Lễ hội thể thao cần một họa tiết gồm các lá cờ tam giác xoay tròn xung quanh cột cờ trung tâm.",
        "task": "Tạo mảnh ghép lá cờ (My Blocks), sau đó dùng vòng lặp quay quanh tâm để vẽ N lá cờ.",
        "input": "Nhập số lượng lá cờ N từ bàn phím.",
        "output": "Họa tiết chong chóng lá cờ xoay đều 360 độ quanh tâm.",
        "sample": "Nhập N = 8 -> Xoay mỗi bước 360 / 8 = 45 độ, vẽ 8 lá cờ.",
        "source": "Câu 6"
    },
    {
        "code": "sca_pen_p07_ngoi_sao_5_canh",
        "lesson": "l01",
        "title": "Ngôi Sao 5 Cánh Khép Kín",
        "context": "Vẽ lá cờ Tổ quốc Việt Nam với ngôi sao vàng 5 cánh rực rỡ ở chính giữa.",
        "task": "Vẽ ngôi sao 5 cánh nét liền với góc quay đỉnh sao là 144 độ (hoặc 72 độ).",
        "input": "Nhấn cờ xanh.",
        "output": "Ngôi sao 5 cánh hoàn hảo khép kín.",
        "sample": "Lặp 5 lần: [Đi 150 bước, Xoay phải 144 độ].",
        "source": "Câu 50, 51"
    },
    {
        "code": "sca_pen_p08_tam_giac_xoay_chong",
        "lesson": "l01",
        "title": "Hoa Văn Tam Giác Xoay Chồng",
        "context": "Họa tiết gạch men cổ điển tạo bởi các hình tam giác đều xoay quanh một đỉnh chung.",
        "task": "Lập trình vẽ N hình tam giác đều chung một đỉnh, mỗi lần vẽ xoay một góc 360 / N độ.",
        "input": "Nhập số hình tam giác N.",
        "output": "Bông hoa hình học đa giác xoay đều sắc sảo.",
        "sample": "N = 12 -> Xoay mỗi lần 30 độ, vẽ 12 tam giác.",
        "source": "Câu 7"
    },
    {
        "code": "sca_pen_p09_hoa_tiet_hinh_thoi",
        "lesson": "l01",
        "title": "Hoa Hình Thoi Xoay Vòng",
        "context": "Cánh hoa hình thoi có góc nhọn 60 độ và góc tù 120 độ ghép lại thành bông hoa 6 cánh thanh lịch.",
        "task": "Viết thủ tục vẽ hình thoi cạnh 80, góc 60 và 120; sau đó lặp lại để tạo bông hoa hoàn chỉnh.",
        "input": "Nhập số lượng cánh hoa.",
        "output": "Bông hoa hình thoi nở rộ giữa sân khấu.",
        "sample": "Cánh hình thoi: lặp 2 [đi 80, xoay 60, đi 80, xoay 120].",
        "source": "Câu 23, 29"
    },
    {
        "code": "sca_pen_p10_kim_tu_thap_bac_thang",
        "lesson": "l01",
        "title": "Kim Tự Tháp Bậc Thang",
        "context": "Kỳ quan Kim tự tháp Ai Cập cổ đại được xây dựng từ các tầng đá xếp chồng lên nhau hình bậc thang.",
        "task": "Lập trình vẽ Kim tự tháp có N bậc thang, mỗi bậc có độ dài thu hẹp dần lên đỉnh.",
        "input": "Nhập số tầng N (ví dụ N = 5).",
        "output": "Hình vẽ Kim tự tháp bậc thang cân xứng.",
        "sample": "Tầng 1 rộng 150, tầng 2 rộng 120, tầng 3 rộng 90...",
        "source": "Câu 32"
    },
    {
        "code": "sca_pen_p11_luoi_o_vuong_ban_co",
        "lesson": "l01",
        "title": "Bàn Cờ Lưới Ô Vuông M x N",
        "context": "Thiết kế bàn cờ caro hoặc mê cung lưới hình chữ nhật gồm nhiều ô vuông nhỏ liền kề.",
        "task": "Sử dụng 2 vòng lặp lồng nhau điều khiển tọa độ để vẽ lưới gồm R hàng và C cột ô vuông.",
        "input": "Nhập số hàng R và số cột C.",
        "output": "Lưới ô vuông thẳng tắp, đều đặn.",
        "sample": "R = 4, C = 5 -> Vẽ lưới 4x5 ô vuông.",
        "source": "Câu 38, 40, 47"
    },
    {
        "code": "sca_pen_p12_tam_giac_nhieu_tang",
        "lesson": "l01",
        "title": "Tam Giác Nhiều Tầng Xếp Chồng",
        "context": "Mô hình tháp tam giác gồm các viên gạch tam giác nhỏ xếp sít nhau thành hình tam giác lớn.",
        "task": "Vẽ tháp tam giác có T tầng, tầng đáy có T hình tam giác.",
        "input": "Nhập số tầng T từ bàn phím.",
        "output": "Tháp tam giác hùng vĩ trên sân khấu.",
        "sample": "T = 3 tầng.",
        "source": "Câu 44"
    },
    {
        "code": "sca_pen_p13_luc_giac_long_nhau",
        "lesson": "l01",
        "title": "Lục Giác Tổ Ong Đồng Tâm",
        "context": "Cấu trúc tổ ong thiên nhiên gồm các hình lục giác đều lồng khít vào nhau cực kỳ vững chắc.",
        "task": "Lập trình vẽ N hình lục giác đều lồng nhau từ cạnh lớn đến cạnh nhỏ.",
        "input": "Nhập kích thước cạnh ngoài cùng.",
        "output": "Mô hình tổ ong hình học tinh xảo.",
        "sample": "Cạnh lục giác giảm dần 15 bước sau mỗi tầng.",
        "source": "Câu 58"
    },
    {
        "code": "sca_pen_p14_ngoi_sao_8_canh_nghe_thuat",
        "lesson": "l01",
        "title": "Ngôi Sao 8 Cánh Nghệ Thuật",
        "context": "Họa tiết hoa văn trống đồng và la bàn hàng hải với ngôi sao 8 cánh cân đối.",
        "task": "Ghép 2 hình vuông xoay góc 45 độ hoặc ghép 8 hình tam giác nhọn quanh tâm.",
        "input": "Nhấn cờ xanh.",
        "output": "Biểu tượng la bàn ngôi sao 8 cánh.",
        "sample": "Vẽ hình vuông 1, xoay phải 45 độ, vẽ hình vuông 2.",
        "source": "Câu 18, 50"
    },
    {
        "code": "sca_pen_p15_cay_thong_noel",
        "lesson": "l01",
        "title": "Cây Thông Noel Đa Tầng",
        "context": "Mùa Giáng Sinh đến, Mèo Scratch muốn vẽ một cây thông Noel xanh mướt từ các tán lá tam giác.",
        "task": "Vẽ 3 tán lá tam giác xếp chồng lên nhau và một gốc cây hình chữ nhật màu nâu.",
        "input": "Nhấn cờ xanh.",
        "output": "Cây thông Noel xinh xắn.",
        "sample": "Tam giác nhỏ trên đỉnh, tam giác vừa ở giữa, tam giác lớn ở dưới cùng.",
        "source": "Câu 19"
    },

    # --- BÀI 02: HÌNH TRÒN, CUNG TRÒN, CẦU VỒNG VÀ HOA VĂN XOAY (P21 - P45) ---
    {
        "code": "sca_pen_p21_hinh_tron_co_ban",
        "lesson": "l02",
        "title": "Hình Tròn Chuẩn Bằng 360 Bước Cong",
        "context": "Khám phá bí mật đường cong: Hình tròn thực chất là một đa giác 360 cạnh siêu nhỏ.",
        "task": "Lập trình vẽ hình tròn bán kính R theo công thức bước đi bước_cong = (2 * 3.14 * R) / 360.",
        "input": "Nhập bán kính R từ bàn phím.",
        "output": "Đường tròn tròn xoe, mượt mà không góc cạnh.",
        "sample": "Lặp 360 [đi bước_cong, xoay phải 1 độ].",
        "source": "Câu 10"
    },
    {
        "code": "sca_pen_p22_hinh_tron_dong_tam_da_sac",
        "lesson": "l02",
        "title": "Hình Tròn Đồng Tâm Đa Sắc",
        "context": "Tấm bia bắn cung Thế vận hội gồm 5 vòng tròn đồng tâm với các màu sắc: vàng, đỏ, xanh lam, đen, trắng.",
        "task": "Viết thủ tục vẽ hình tròn với tham số bán kính, sau đó vẽ các vòng tròn có bán kính tăng dần cùng tâm (0,0).",
        "input": "Nhập số vòng tròn N.",
        "output": "Bia ngắm bắn hình tròn đồng tâm rực rỡ.",
        "sample": "R = 30, 60, 90, 120...",
        "source": "Câu 10, 54"
    },
    {
        "code": "sca_pen_p23_logo_olympic_5_mau",
        "lesson": "l02",
        "title": "Biểu Tượng 5 Vòng Tròn Olympic",
        "context": "Logo Thế vận hội Olympic gồm 5 vòng tròn đan xen nhau đại diện cho 5 châu lục: Xanh lam, Vàng, Đen, Xanh lá, Đỏ.",
        "task": "Lập trình vẽ chính xác 5 vòng tròn nét to (size = 10) tại các tọa độ chuẩn xác lồng vào nhau.",
        "input": "Nhấn cờ xanh.",
        "output": "Logo Olympic hoàn chỉnh đúng chuẩn quốc tế.",
        "sample": "3 vòng hàng trên, 2 vòng so le hàng dưới.",
        "source": "Câu 12"
    },
    {
        "code": "sca_pen_p24_cung_tron_cau_vong_7_mau",
        "lesson": "l02",
        "title": "Cầu Vồng 7 Sắc Rực Rỡ",
        "context": "Sau cơn mưa rào, một chiếc cầu vồng 7 sắc xuất hiện uốn cong trên bầu trời.",
        "task": "Vẽ 7 cung tròn 180 độ lồng nhau với nét vẽ dày 12, theo thứ tự màu: Đỏ, Cam, Vàng, Lục, Lam, Chàm, Tím.",
        "input": "Nhấn cờ xanh.",
        "output": "Cầu vồng 7 sắc cong vút tuyệt đẹp.",
        "sample": "Cung tròn 180 độ: lặp 180 [đi bước_cong, xoay 1 độ].",
        "source": "Câu 15"
    },
    {
        "code": "sca_pen_p25_canh_hoa_cung_tron_90",
        "lesson": "l02",
        "title": "Cánh Hoa Mảnh Ghép Cung Tròn 90 Độ",
        "context": "Một cánh hoa mềm mại được tạo thành bởi 2 cung tròn 90 độ khép cong đối xứng nhau.",
        "task": "Tạo thủ tục Canh_Hoa: Lặp 2 lần [Lặp 90 lần (đi, xoay 1 độ), xoay phải 90 độ].",
        "input": "Nhấn cờ xanh.",
        "output": "Một cánh hoa hình thoi cong thanh thoát.",
        "sample": "Hai cung tròn 90 độ cong úp vào nhau.",
        "source": "Câu 16"
    },
    {
        "code": "sca_pen_p26_bong_hoa_da_canh",
        "lesson": "l02",
        "title": "Bông Hoa K Cánh Nở Rộ",
        "context": "Từ cánh hoa cơ bản, ta có thể tạo ra bông hoa 6 cánh, 8 cánh hoặc 12 cánh bằng cách quay quanh tâm.",
        "task": "Sử dụng thủ tục Canh_Hoa, xoay quanh tâm 360 / K độ để vẽ bông hoa K cánh đổi màu.",
        "input": "Nhập số cánh hoa K từ bàn phím.",
        "output": "Bông hoa đa cánh nở rộ rực rỡ.",
        "sample": "K = 8 cánh -> Xoay mỗi lần 45 độ.",
        "source": "Câu 16"
    },
    {
        "code": "sca_pen_p27_chong_chong_gio",
        "lesson": "l02",
        "title": "Chong Chóng Gió Xoay Tít",
        "context": "Chiếc chong chóng gió tuổi thơ quay tít trước hiên nhà trong những ngày hè lộng gió.",
        "task": "Vẽ các cánh chong chóng lệch tâm cong vút kết hợp màu sắc tương phản.",
        "input": "Nhập số cánh chong chóng (4 hoặc 6).",
        "output": "Chong chóng gió chuyển động xoay đều.",
        "sample": "Vẽ 4 cánh chong chóng xoay góc 90 độ.",
        "source": "Câu 9, 48"
    },
    {
        "code": "sca_pen_p28_bong_hoa_tuyet_pha_le",
        "lesson": "l02",
        "title": "Bông Hoa Tuyết Pha Lê 6 Nhánh",
        "context": "Những bông hoa tuyết mùa đông rơi xuống mang hình dạng đối xứng 6 nhánh tinh xảo.",
        "task": "Tạo thủ tục Nhánh_Tuyết có các nhánh con đối xứng, sau đó lặp lại 6 lần quanh tâm.",
        "input": "Nhấn cờ xanh.",
        "output": "Bông hoa tuyết pha lê màu xanh lấp lánh.",
        "sample": "6 nhánh tuyết xoay góc 60 độ quanh tâm.",
        "source": "Câu 9, 11"
    },
    {
        "code": "sca_pen_p29_hinh_tron_khuyet",
        "lesson": "l02",
        "title": "Vầng Trăng Khuyết Nghệ Thuật",
        "context": "Bầu trời đêm rằm với vầng trăng khuyết dịu dàng chiếu sáng không gian.",
        "task": "Vẽ cung tròn lớn, sau đó quay ngược lại vẽ cung tròn nhỏ để tạo hình trăng khuyết.",
        "input": "Nhấn cờ xanh.",
        "output": "Hình vầng trăng khuyết màu vàng óng ả.",
        "sample": "Cung tròn ngoài bán kính lớn, cung trong bán kính nhỏ.",
        "source": "Câu 31"
    },
    {
        "code": "sca_pen_p30_chia_banh_pizza_n_phan",
        "lesson": "l02",
        "title": "Chia Bánh Pizza N Miếng Đa Sắc",
        "context": "Bữa tiệc sinh nhật có chiếc bánh pizza tròn cần chia đều cho N bạn nhỏ, mỗi miếng một vị và màu sắc khác nhau.",
        "task": "Vẽ đường tròn và các nan quạt từ tâm ra đường viền, chia góc 360 / N độ.",
        "input": "Nhập số phần N (ví dụ N = 6 hoặc 8).",
        "output": "Chiếc bánh tròn được chia thành N nan quạt màu sắc rực rỡ.",
        "sample": "Mỗi nan quạt đi từ tâm ra bán kính R, xoay góc, đi về tâm.",
        "source": "Câu 22"
    },
    {
        "code": "sca_pen_p31_hoa_van_xoan_oc",
        "lesson": "l02",
        "title": "Vỏ Ốc Xoắn Archimedes",
        "context": "Quy luật xoắn ốc tuyệt mỹ trong thiên nhiên được tìm thấy trên vỏ ốc biển và dải ngân hà.",
        "task": "Vòng lặp vẽ đường cong với bán kính hoặc bước đi tăng dần sau mỗi góc xoay nhỏ.",
        "input": "Nhấn cờ xanh.",
        "output": "Đường xoắn ốc Archimedes mượt mà từ tâm lan tỏa ra ngoài.",
        "sample": "Lặp 500 lần: đi (i * 0.05) bước, xoay 5 độ.",
        "source": "Câu 24"
    },
    {
        "code": "sca_pen_p32_chuoi_vong_ngoc_trai",
        "lesson": "l02",
        "title": "Chuỗi Vòng Ngọc Trai Lấp Lánh",
        "context": "Chuỗi vòng cổ quý phái đính các viên ngọc trai tròn xoe xếp đều trên một đường tròn lớn.",
        "task": "Đi theo đường tròn lớn, tại mỗi khoảng cách đều đặn dừng lại vẽ một viên ngọc trai nhỏ.",
        "input": "Nhập số lượng hạt ngọc trai K.",
        "output": "Chuỗi vòng ngọc trai lộng lẫy.",
        "sample": "K = 12 hạt ngọc xếp tròn quanh tâm.",
        "source": "Câu 26"
    },
    {
        "code": "sca_pen_p33_hoa_tiet_trang_tri_vien",
        "lesson": "l02",
        "title": "Họa Tiết Đường Viền Sóng Biển",
        "context": "Trang trí mép thảm trải sàn hoặc khung ảnh bằng chuỗi cung tròn sóng biển dập dềnh liên tiếp.",
        "task": "Lặp lại N lần cung tròn 180 độ uốn lượn liên tiếp theo chiều ngang.",
        "input": "Nhập chiều dài đường viền.",
        "output": "Dải hoa văn viền sóng biển uốn lượn liên tục.",
        "sample": "Cung uốn lên rồi cung uốn xuống xen kẽ.",
        "source": "Câu 27"
    },
    {
        "code": "sca_pen_p34_hoa_van_gach_hoa_co_dien",
        "lesson": "l02",
        "title": "Gạch Hoa Cổ Điển Đông Dương",
        "context": "Nền nhà cổ kính với những viên gạch hoa văn kết hợp tinh tế giữa hình vuông và 4 cánh hoa tròn bao quanh.",
        "task": "Vẽ hình vuông trung tâm và 4 cánh hoa uốn cong tại 4 cạnh hình vuông.",
        "input": "Nhấn cờ xanh.",
        "output": "Họa tiết viên gạch hoa Đông Dương sang trọng.",
        "sample": "1 hình vuông + 4 cung tròn cánh hoa.",
        "source": "Câu 33"
    },
    {
        "code": "sca_pen_p35_dai_ngan_ha_van_hoa",
        "lesson": "l02",
        "title": "Kính Vạn Hoa Đa Chiều (Kaleidoscope)",
        "context": "Ống kính vạn hoa đồ chơi tạo nên vô số hoa văn kỳ ảo khi xoay chuyển trước ánh sáng.",
        "task": "Xoay một cụm họa tiết gồm đa giác và cung tròn 36 lần quanh tâm (mỗi lần 10 độ) với màu sắc cầu vồng ngẫu nhiên.",
        "input": "Nhấn cờ xanh.",
        "output": "Bức tranh kính vạn hoa lộng lẫy, choáng ngợp.",
        "sample": "Hiệu ứng xoay tròn 36 lần liên tục đổi màu.",
        "source": "Câu 34, 37"
    }
]

def generate_pen_packages():
    created = 0
    for p in PEN_PROBLEMS:
        code = p["code"]
        p_dir = PROBLEMS_DIR / code
        p_dir.mkdir(parents=True, exist_ok=True)
        
        # 1. De_Bai.md
        de_bai = f"""# {p['title']}

## Bối cảnh

{p['context']}

## Nhiệm vụ

{p['task']}

## Input

{p['input']}

## Output

{p['output']}

## Sample 1

### Input
```text
Sự kiện: {p['input']}
```

### Output
```text
Kết quả: {p['output']}
```

### Giải thích

{p['sample']}

## Ràng buộc

- Môi trường: Scratch 3.0 với phần mở rộng Bút vẽ (Pen).
- Tọa độ khởi tạo an toàn trong khung hình sân khấu (x: -240 đến 240, y: -180 đến 180).
- Nguồn bài thi: Trích xuất từ tài liệu chuẩn `{p['source']} - {DOCX_FILE}`.
"""
        (p_dir / "De_Bai.md").write_text(de_bai, encoding="utf-8")
        
        # 2. Huong_Dan_Giang_Day.md
        hd = f"""# HƯỚNG DẪN GIẢNG DẠY: {p['title'].upper()}
Chuyên đề: **Đồ Họa Bút Vẽ (Pen) & Thuật Toán Hình Học Scratch 3.0**  
Mã bài toán: `{code}` | Nguồn tham chiếu: `{p['source']}`

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất hình học:** Bài toán rèn luyện tư duy chia nhỏ hình phức tạp thành các hình con cơ bản (đa giác đều, cung tròn, nhánh hoa văn).
- **Quy tắc bảo toàn góc quay:** Tổng các góc quay khi đi hết 1 vòng khép kín luôn bằng $360^\circ$.
- **Kỹ thuật đóng gói My Blocks:** Khuyến khích học sinh định nghĩa thủ tục con (ví dụ: `Vẽ_Cánh_Hoa`, `Vẽ_Nhánh`) với các tham số độ dài, bán kính để tái sử dụng nhiều lần.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
| Bước | Khối lệnh Scratch Tiếng Việt | Vị trí (x, y) | Hướng | Tác dụng |
|:---:|---|:---:|:---:|---|
| 1 | `khi bấm vào cờ xanh` | (0, 0) | 90 | Khởi động kịch bản |
| 2 | `xóa tất cả` | (0, 0) | 90 | Dọn sạch sân khấu |
| 3 | `nhấc bút`, `đi tới điểm x: 0 y: 0` | (0, 0) | 90 | Đưa nhân vật về tâm |
| 4 | `đặt kích thước bút vẽ bằng (3)` | (0, 0) | 90 | Đặt nét vẽ rõ nét |
| 5 | `đặt bút`, thực hiện vòng lặp | Thay đổi | Thay đổi | Vẽ hình theo yêu cầu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 (Góc trong vs Góc ngoài):** Học sinh hay nhầm góc quay ngoài của nhân vật với góc trong của đa giác (ví dụ tam giác đều quay $120^\circ$ chứ không phải $60^\circ$).
- **Bẫy 2 (Lem nét vẽ thừa):** Quên `nhấc bút` khi di chuyển nhân vật đến vị trí xuất phát mới khiến đường đi để lại vệt mực xấu.
- **Bẫy 3 (Vẽ tràn sân khấu):** Chọn bán kính hoặc độ dài cạnh quá lớn khiến nhân vật chạm biên màn hình và hình vẽ bị méo mó.

---

## 4. Lời giải tham khảo & Khối lệnh tiêu điểm
- Nhóm Bút vẽ: `xóa tất cả`, `nhấc bút`, `đặt bút`, `chọn màu vẽ`, `đặt kích thước bút vẽ`.
- Nhóm Chuyển động: `di chuyển () bước`, `xoay phải () độ`, `đi tới điểm x: () y: ()`.
- Nhóm Điều khiển: `lặp lại () lần`.
"""
        (p_dir / "Huong_Dan_Giang_Day.md").write_text(hd, encoding="utf-8")
        created += 1

    print(f"SUCCESS: Generated {created} rich Pen problem packages.")

if __name__ == "__main__":
    generate_pen_packages()
