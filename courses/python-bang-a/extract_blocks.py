import os, re

code_map = {
    'pya_l04_p08_cap_so_bang_nhau_hay_khac': 'PYA-L04-P08',
    'pya_l05_p01_den_giao_thong_nga_tu': 'PYA-L05-P01',
    'pya_l05_p02_dau_cua_so_nguyen': 'PYA-L05-P02',
    'pya_l05_p04_xep_loai_hoc_luc': 'PYA-L05-P04',
    'pya_l05_p05_ve_gui_xe_ben_bai': 'PYA-L05-P05',
    'pya_l05_p08_phan_loai_tam_giac': 'PYA-L05-P08',
    'pya_l05_p09_thuan_di_tim_anh_da_van_toc': 'PYA-L05-P09',
    'pya_l05_p10_thu_may_trong_tuan': 'PYA-L05-P10',
    'pya_l05_p11_cua_hang_banh_bot_loc_khuyen_mai': 'PYA-L05-P11',
    'pya_l05_p12_bon_mua_trong_nam': 'PYA-L05-P12',
    'pya_l06_p02_boi_chung_cua_3_va_5': 'PYA-L06-P02',
    'pya_l06_p03_ngay_nghi_cuoi_tuan': 'PYA-L06-P03',
    'pya_l06_p04_diem_nam_trong_hinh_chu_nhat': 'PYA-L06-P04',
    'pya_l06_p09_rut_the_may_man': 'PYA-L06-P09',
    'pya_l06_p11_cap_doi_cung_dau_hay_trai_dau': 'PYA-L06-P11',
    'pya_l08_p01_dem_xuoi_bang_while': 'PYA-L08-P01',
    'pya_l08_p02_rut_tham_den_khi_trung': 'PYA-L08-P02'
}

for pkg, code in code_map.items():
    found_block = None
    for bt_path in ['courses/python-bang-a/lessons/lesson-04/Bai_Tap.md', 'courses/python-bang-a/lessons/lesson-06/Bai_Tap.md']:
        content = open(bt_path, encoding='utf-8').read()
        # look for ### Bài ... (`CODE`)
        pattern = rf'(### Bài \d+[^:]*:[^\n]*`{code}`.*?)(?=\n### Bài \d+|\Z)'
        m = re.search(pattern, content, re.DOTALL)
        if m:
            found_block = m.group(1).strip()
            break
    print(f"=== {pkg} ({code}) ===")
    if found_block:
        # print up to 300 chars
        print(found_block[:250].replace('\n', ' // '))
    else:
        print("NOT FOUND")
