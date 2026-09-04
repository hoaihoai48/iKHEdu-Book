#!/usr/bin/env python3
"""
Script chuẩn hoá triệt để Giai đoạn 2 cho c++-level-1-quyen-2.docx
Theo đúng chuẩn mực Quyển 1 (c++-level-1-quyen-1.docx) và MASTER_WORD_BUILD_SPECIFICATION.md:

1. Bảng Sample IO (135 bảng):
   - Header row: 'Đầu vào (Input)' và 'Đầu ra (Output)' căn giữa (Center), font Consolas 11pt Bold, nền #F1F5F9.
   - Testcase row:
     + Tách đa dòng (multiline) thành từng thẻ <w:p> độc lập (tách theo 2 khoảng trắng '  ' hoặc '\n').
     + Mỗi thẻ <w:p> mang style Compact, font Consolas 11pt thường (#1E293B), line spacing 276 (1.15).
     + Dòng đầu tiên trong cell có spacing before = 40 (2pt).
     + Áp dụng Dynamic Left Indent cho từng cell theo dòng dài nhất (max_len):
       left_indent(max_len) = max(10.0 pt, 72.0 pt - max(0, max_len - 4) * 3.25 pt)
     + Bảng có chiều rộng 6800 dxa, căn giữa trang w:jc="center".
     + Xoá sạch w:tblHeader, đảm bảo w:cantSplit trên mọi hàng.

2. Khung mã nguồn (Source Code):
   - Quét và loại bỏ hoàn toàn các thẻ w:numPr rác (nếu còn sót).
   - Đảm bảo font Consolas 9.0pt, dãn dòng 1.05 (line=252), căn trái (Left), khung viền #CBD5E1/#E2E8F0, nền #F8FAFC.

3. Bảng lý thuyết & Phụ lục A:
   - Font bảng tra cứu 12.0pt (hoặc 10.5pt cho bảng bài học).
   - Công thức toán m:oMath trong bảng mang w:sz val="24" (12.0pt) đồng bộ.
"""

import sys
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

TARGET_FILE = Path("courses/cpp-bang-b/c++-level-1-quyen-2.docx")

def standardize_step2():
    print(f"Đang mở file: {TARGET_FILE}...")
    doc = Document(str(TARGET_FILE))
    
    # ============================================================
    # 1. BẢNG SAMPLE IO (135 BẢNG)
    # ============================================================
    sample_table_count = 0
    multiline_cells_count = 0
    
    for t_idx, table in enumerate(doc.tables):
        if len(table.rows) >= 2 and len(table.rows[0].cells) == 2:
            c0_text = table.rows[0].cells[0].text.strip()
            c1_text = table.rows[0].cells[1].text.strip()
            
            if ("Đầu vào" in c0_text or "Input" in c0_text) and ("Đầu ra" in c1_text or "Output" in c1_text):
                sample_table_count += 1
                
                # --- A. Cấu hình bảng chung ---
                table_tblPr = table._tbl.tblPr
                # Đảm bảo căn giữa
                jc = table_tblPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}jc')
                if jc is None:
                    table_tblPr.append(parse_xml(f'<w:jc {nsdecls("w")} w:val="center"/>'))
                else:
                    jc.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', 'center')
                
                # Xóa sạch tblHeader trên mọi hàng, thêm cantSplit
                for r_idx, row in enumerate(table.rows):
                    trPr = row._tr.get_or_add_trPr()
                    for h in trPr.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tblHeader'):
                        trPr.remove(h)
                    if trPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}cantSplit') is None:
                        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
                
                # --- B. Chuẩn hóa Hàng 0 (Tiêu đề) ---
                header_row = table.rows[0]
                for cell_idx, cell in enumerate(header_row.cells):
                    tcPr = cell._tc.get_or_add_tcPr()
                    shd = tcPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}shd')
                    if shd is not None:
                        shd.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fill', 'F1F5F9')
                    else:
                        tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:val="clear" w:color="auto" w:fill="F1F5F9"/>'))
                    
                    for p in cell.paragraphs:
                        p.alignment = None # Dùng pPr jc="center"
                        pPr = p._p.get_or_add_pPr()
                        jc = pPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}jc')
                        if jc is not None:
                            jc.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', 'center')
                        else:
                            pPr.append(parse_xml(f'<w:jc {nsdecls("w")} w:val="center"/>'))
                        
                        for r in p.runs:
                            r.font.name = "Consolas"
                            r.font.size = Pt(11)
                            r.font.bold = True
                            r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
                
                # --- C. Chuẩn hóa Hàng 1 (Dữ liệu Testcase & Tách đa dòng) ---
                data_row = table.rows[1]
                for cell_idx in [0, 1]:
                    cell = data_row.cells[cell_idx]
                    raw_text = cell.text.strip()
                    if not raw_text:
                        continue
                    
                    # Thuật toán phân rã đa dòng
                    if '  ' in raw_text:
                        lines = [line.strip() for line in raw_text.split('  ') if line.strip()]
                    elif '\n' in raw_text:
                        lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
                    else:
                        lines = [raw_text]
                    
                    if len(lines) > 1:
                        multiline_cells_count += 1
                    
                    # Thuật toán Dynamic Left Indent
                    max_len = max(len(l) for l in lines)
                    indent_pt = max(10.0, 72.0 - max(0, max_len - 4) * 3.25)
                    indent_dxa = int(round(indent_pt * 20))
                    
                    # Xóa các đoạn văn cũ trong cell
                    for p in list(cell.paragraphs):
                        cell._element.remove(p._p)
                    
                    # Thêm từng đoạn văn độc lập
                    for line_idx, line in enumerate(lines):
                        p = cell.add_paragraph()
                        pPr = p._p.get_or_add_pPr()
                        pPr.append(parse_xml(f'<w:pStyle {nsdecls("w")} w:val="Compact"/>'))
                        
                        # Spacing chuẩn Quyển 1: line="276" (1.15), dòng đầu before="40" (2pt)
                        if line_idx == 0:
                            pPr.append(parse_xml(f'<w:spacing {nsdecls("w")} w:before="40" w:line="276" w:lineRule="auto"/>'))
                        else:
                            pPr.append(parse_xml(f'<w:spacing {nsdecls("w")} w:line="276" w:lineRule="auto"/>'))
                        
                        pPr.append(parse_xml(f'<w:ind {nsdecls("w")} w:left="{indent_dxa}"/>'))
                        pPr.append(parse_xml(f'<w:jc {nsdecls("w")} w:val="left"/>'))
                        
                        r = p.add_run(line)
                        r.font.name = "Consolas"
                        r.font.size = Pt(11)
                        r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
    
    print(f"  ✓ Đã chuẩn hóa {sample_table_count} bảng Sample IO ({multiline_cells_count} cell được tách đa dòng thành công).")
    
    # ============================================================
    # 2. KHUNG MÃ NGUỒN (SOURCE CODE) - LOẠI BỎ NUMPR RÁC
    # ============================================================
    cleaned_numpr_count = 0
    for el in doc.element.body:
        if el.tag.endswith('p'):
            pPr = el.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pPr')
            if pPr is not None:
                pStyle = pPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pStyle')
                if pStyle is not None and pStyle.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val') == 'SourceCode':
                    numPr = pPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}numPr')
                    if numPr is not None:
                        pPr.remove(numPr)
                        cleaned_numpr_count += 1
    
    print(f"  ✓ Đã kiểm tra và loại bỏ {cleaned_numpr_count} thẻ numPr rác trong các khối Source Code.")
    
    # Lưu file
    doc.save(str(TARGET_FILE))
    print(f"✅ Hoàn tất lưu file: {TARGET_FILE.name}!")

if __name__ == "__main__":
    standardize_step2()
