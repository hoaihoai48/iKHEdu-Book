import os

data = {
    'pya_l04_p08_cap_so_bang_nhau_hay_khac': {
        'in': '15 28', 'out': 'a NHO HON b', 'exp': 'Số 15 nhỏ hơn số 28 nên in ra a NHO HON b.'
    },
    'pya_l05_p01_den_giao_thong_nga_tu': {
        'in': 'do', 'out': 'DUNG LAI', 'exp': 'Màu đèn là "do" nên in ra thông báo DUNG LAI.'
    },
    'pya_l05_p02_dau_cua_so_nguyen': {
        'in': '-15', 'out': 'AM', 'exp': 'Số -15 nhỏ hơn 0 nên in ra AM.'
    },
    'pya_l05_p04_xep_loai_hoc_luc': {
        'in': '8.5', 'out': 'GIOI', 'exp': 'Điểm 8.5 thuộc thang điểm giỏi (từ 8.0 trở lên).'
    },
    'pya_l05_p05_ve_gui_xe_ben_bai': {
        'in': 'xe may', 'out': '5000', 'exp': 'Phương tiện gửi là xe máy có mức phí 5000 đồng.'
    },
    'pya_l05_p08_phan_loai_tam_giac': {
        'in': '3 3 3', 'out': 'DEU', 'exp': 'Ba cạnh có độ dài bằng nhau nên tam giác là tam giác đều.'
    },
    'pya_l05_p09_thuan_di_tim_anh_da_van_toc': {
        'in': '15', 'out': 'XE DAP', 'exp': 'Vận tốc 15 km/h nằm trong khoảng từ 10 đến 30 km/h nên Thuận đi xe đạp.'
    },
    'pya_l05_p10_thu_may_trong_tuan': {
        'in': '2', 'out': 'THU 2', 'exp': 'Ngày thứ 2 trong tuần là Thứ Hai.'
    },
    'pya_l05_p11_cua_hang_banh_bot_loc_khuyen_mai': {
        'in': '25', 'out': '100000', 'exp': 'Mua 25 chiếc (từ 20 chiếc trở lên) được giá 4000 đ/chiếc: 25 x 4000 = 100000 đ.'
    },
    'pya_l05_p12_bon_mua_trong_nam': {
        'in': '4', 'out': 'HA', 'exp': 'Tháng 4 thuộc mùa hạ (mùa hè).'
    },
    'pya_l06_p02_boi_chung_cua_3_va_5': {
        'in': '15', 'out': 'YES', 'exp': 'Số 15 vừa chia hết cho 3 vừa chia hết cho 5.'
    },
    'pya_l06_p03_ngay_nghi_cuoi_tuan': {
        'in': '7', 'out': 'NGHI', 'exp': 'Ngày 7 là thứ Bảy nên được nghỉ học.'
    },
    'pya_l06_p04_diem_nam_trong_hinh_chu_nhat': {
        'in': '2 3 5 5', 'out': 'TRONG', 'exp': 'Điểm (2, 3) nằm trọn vẹn bên trong hình chữ nhật từ (0, 0) đến (5, 5).'
    },
    'pya_l06_p09_rut_the_may_man': {
        'in': '14', 'out': 'TRUNG THUONG', 'exp': 'Số 14 chia hết cho 7 nên chiếc thẻ trúng thưởng.'
    },
    'pya_l06_p11_cap_doi_cung_dau_hay_trai_dau': {
        'in': '5 10', 'out': 'CUNG DAU', 'exp': 'Cả hai số 5 và 10 đều là số dương nên cùng dấu.'
    },
    'pya_l08_p01_dem_xuoi_bang_while': {
        'in': '5', 'out': '1 2 3 4 5', 'exp': 'In các số từ 1 đến 5 trên một dòng cách nhau khoảng trắng.'
    },
    'pya_l08_p02_rut_tham_den_khi_trung': {
        'in': '10\n25\n77', 'out': '3', 'exp': 'Nhập 3 số 10, 25, 77 thì dừng lại khi gặp số 77, tổng cộng đã nhập 3 số.'
    }
}

for pkg, info in data.items():
    deb_path = f'courses/python-bang-a/problems/{pkg}/De_Bai.md'
    content = open(deb_path, encoding='utf-8').read()
    
    # Remove any bad Sample 1 block if present
    if '## Sample 1' in content:
        content = content.split('## Sample 1')[0].rstrip() + '\n\n' + '## Ràng buộc' + content.split('## Ràng buộc')[1]
        
    sample_text = f"## Sample 1\n\n### Input\n```text\n{info['in']}\n```\n### Output\n```text\n{info['out']}\n```\n### Giải thích\n{info['exp']}\n"
    
    if '## Ràng buộc' in content:
        parts = content.split('## Ràng buộc')
        new_content = parts[0].rstrip() + '\n\n' + sample_text + '\n## Ràng buộc' + parts[1]
    else:
        new_content = content.rstrip() + '\n\n' + sample_text
        
    with open(deb_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Properly formatted sample in {pkg}")
