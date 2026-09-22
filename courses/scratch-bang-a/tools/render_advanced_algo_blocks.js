const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

// 1. Initialize headless DOM with scratchblocks
const dom = new JSDOM('<!DOCTYPE html><html><head></head><body></body></html>', { runScripts: 'dangerously' });
const scriptEl = dom.window.document.createElement('script');
scriptEl.textContent = fs.readFileSync(path.join(__dirname, '../node_modules/scratchblocks/build/scratchblocks.min.js'), 'utf8');
dom.window.document.body.appendChild(scriptEl);
const scratchblocks = dom.window.scratchblocks;

scratchblocks.appendStyles(dom.window.document, 'scratch3');
const styleTags = dom.window.document.querySelectorAll('style');
let allCss = '';
styleTags.forEach(s => allCss += s.textContent + '\n');

function renderToSvgAndPng(sbScript, outSvgPath, outPngPath) {
  const doc = scratchblocks.parse(sbScript, { languages: ['en'] });
  const svg = scratchblocks.render(doc, { style: 'scratch3' });
  const defs = svg.querySelector('defs') || svg.insertBefore(dom.window.document.createElementNS('http://www.w3.org/2000/svg', 'defs'), svg.firstChild);
  const svgStyle = dom.window.document.createElementNS('http://www.w3.org/2000/svg', 'style');
  svgStyle.textContent = allCss;
  defs.appendChild(svgStyle);

  fs.writeFileSync(outSvgPath, svg.outerHTML, 'utf8');
  execSync(`rsvg-convert -f png "${outSvgPath}" -o "${outPngPath}"`);
}

// 2. Định nghĩa tất cả các hình ảnh khối lệnh thuật toán chuyên sâu cho Bài 03 đến Bài 16
const BLOCKS_TO_RENDER = {

  // Khối lệnh đơn Bút vẽ (Bài 01)
  "pen_block_clear": "xóa tất cả :: pen",
  "pen_block_down": "đặt bút :: pen",
  "pen_block_up": "nhấc bút :: pen",
  "pen_block_set_color": "chọn màu vẽ [#0055ff] :: pen",
  "pen_block_change_color": "đổi màu bút một lượng (10) :: pen",
  "pen_block_set_size": "đặt kích thước bút vẽ bằng (3) :: pen",
  "pen_block_change_size": "thay đổi kích thước bút vẽ một lượng (1) :: pen",

  // Khối lệnh đơn Danh sách List (Bài 13)
  "list_block_add": "thêm (X) vào [Dãy số v] :: list",
  "list_block_delete": "xóa (1) của [Dãy số v] :: list",
  "list_block_clear": "xóa tất cả của [Dãy số v] :: list",
  "list_block_insert": "chèn (X) vào (1) của [Dãy số v] :: list",
  "list_block_replace": "thay thế phần tử (1) của [Dãy số v] bằng (X) :: list",
  "list_block_item": "(phần tử (1) của [Dãy số v] :: list)",
  "list_block_find": "(vị trí của (X) trong [Dãy số v] :: list)",
  "list_block_length": "(kích thước của [Dãy số v] :: list)",
  "list_block_contains": "<[Dãy số v] chứa (X) ? :: list>",

  // Khối lệnh đơn Chuỗi Ký tự (Bài 15)
  "str_block_letter": "(ký tự (1) của (chuỗi) :: operators)",
  "str_block_length": "(độ dài của (chuỗi) :: operators)",
  "str_block_join": "(kết hợp (A) (B) :: operators)",
  "str_block_contains": "<(chuỗi) chứa (a) ? :: operators>",

  // Bài 03
  "l03_pipeline_io_vi": `
hỏi [Nhập số a: ] và đợi :: sensing
đặt [a v] thành (câu trả lời :: sensing) :: variables
hỏi [Nhập số b: ] và đợi :: sensing
đặt [b v] thành (câu trả lời :: sensing) :: variables
đặt [tong v] thành ((a :: variables) + (b :: variables) :: operators) :: variables
nói (kết hợp [Tổng là: ] (tong :: variables) :: operators) :: looks
`,

  // Bài 04
  "l04_nested_expression_vi": `
đặt [chu_vi v] thành (((chieu_dai :: variables) + (chieu_rong :: variables) :: operators) * (2) :: operators) :: variables
đặt [dien_tich v] thành ((chieu_dai :: variables) * (chieu_rong :: variables) :: operators) :: variables
`,

  // Bài 05
  "l05_time_convert_vi": `
đặt [gio v] thành ([làm tròn xuống v] của ((tong_giay :: variables) / (3600) :: operators) :: operators) :: variables
đặt [giay_du v] thành ((tong_giay :: variables) mod (3600) :: operators) :: variables
đặt [phut v] thành ([làm tròn xuống v] của ((giay_du :: variables) / (60) :: operators) :: operators) :: variables
đặt [giay v] thành ((giay_du :: variables) mod (60) :: operators) :: variables
`,

  // Bài 06
  "l06_max3_vi": `
đặt [max v] thành (a :: variables) :: variables
nếu <(b :: variables) > (max :: variables)> thì {
  đặt [max v] thành (b :: variables) :: variables
} :: control
nếu <(c :: variables) > (max :: variables)> thì {
  đặt [max v] thành (c :: variables) :: variables
} :: control
nói (kết hợp [Số lớn nhất là: ] (max :: variables) :: operators) :: looks
`,
  "l06_nested_if_elif_vi": `
nếu <(diem :: variables) > (8)> thì {
  nói [GIOI] :: looks
} nếu không thì {
  nếu <(diem :: variables) > (6.5)> thì {
    nói [KHA] :: looks
  } nếu không thì {
    nếu <(diem :: variables) > (5)> thì {
      nói [TRUNG BINH] :: looks
    } nếu không thì {
      nói [YEU] :: looks
    } :: control
  } :: control
} :: control
`,

  // Bài 07
  "l07_accumulator_vi": `
đặt [tong v] thành (0) :: variables
đặt [i v] thành (1) :: variables
lặp lại (n :: variables) lần {
  thay đổi [tong v] một lượng (i :: variables) :: variables
  thay đổi [i v] một lượng (1) :: variables
} :: control
nói (tong :: variables) :: looks
`,
  "l07_factorial_vi": `
đặt [giai_thua v] thành (1) :: variables
đặt [i v] thành (1) :: variables
lặp lại (n :: variables) lần {
  đặt [giai_thua v] thành ((giai_thua :: variables) * (i :: variables) :: operators) :: variables
  thay đổi [i v] một lượng (1) :: variables
} :: control
nói (giai_thua :: variables) :: looks
`,

  // Bài 08
  "l08_collatz_vi": `
lặp lại cho đến khi <(n :: variables) = (1)> {
  nếu <((n :: variables) mod (2) :: operators) = (0)> thì {
    đặt [n v] thành ((n :: variables) / (2) :: operators) :: variables
  } nếu không thì {
    đặt [n v] thành (((3) * (n :: variables) :: operators) + (1) :: operators) :: variables
  } :: control
  thay đổi [buoc v] một lượng (1) :: variables
} :: control
`,
  "l08_sentinel_flag_vi": `
đặt [tim_thay v] thành (0) :: variables
lặp lại cho đến khi <<(tim_thay :: variables) = (1)> hoặc <(i :: variables) > (n :: variables)>> {
  nếu <((i :: variables) * (i :: variables) :: operators) = (n :: variables)> thì {
    đặt [tim_thay v] thành (1) :: variables
  } nếu không thì {
    thay đổi [i v] một lượng (1) :: variables
  } :: control
} :: control
`,

  // Bài 09
  "l09_fibonacci_vi": `
đặt [a v] thành (1) :: variables
đặt [b v] thành (1) :: variables
đặt [dem v] thành (2) :: variables
lặp lại ((n :: variables) - (2) :: operators) lần {
  đặt [c v] thành ((a :: variables) + (b :: variables) :: operators) :: variables
  đặt [a v] thành (b :: variables) :: variables
  đặt [b v] thành (c :: variables) :: variables
} :: control
nói (b :: variables) :: looks
`,
  "l09_nested_triangle_vi": `
đặt [dong v] thành (1) :: variables
lặp lại (n :: variables) lần {
  đặt [dong_chu v] thành [] :: variables
  đặt [cot v] thành (1) :: variables
  lặp lại (dong :: variables) lần {
    đặt [dong_chu v] thành (kết hợp (dong_chu :: variables) [*] :: operators) :: variables
    thay đổi [cot v] một lượng (1) :: variables
  } :: control
  thêm (dong_chu :: variables) vào [Tam giác sao v] :: list
  thay đổi [dong v] một lượng (1) :: variables
} :: control
`,

  // Bài 10
  "l10_digit_reverse_vi": `
đặt [dao_nguoc v] thành (0) :: variables
lặp lại cho đến khi <(so :: variables) = (0)> {
  đặt [chu_so v] thành ((so :: variables) mod (10) :: operators) :: variables
  đặt [dao_nguoc v] thành (((dao_nguoc :: variables) * (10) :: operators) + (chu_so :: variables) :: operators) :: variables
  đặt [so v] thành ([làm tròn xuống v] của ((so :: variables) / (10) :: operators) :: operators) :: variables
} :: control
nói (dao_nguoc :: variables) :: looks
`,

  // Bài 11
  "l11_prime_check_vi": `
đặt [la_nguyen_to v] thành (1) :: variables
nếu <(n :: variables) < (2)> thì {
  đặt [la_nguyen_to v] thành (0) :: variables
} :: control
đặt [d v] thành (2) :: variables
lặp lại cho đến khi <<((d :: variables) * (d :: variables) :: operators) > (n :: variables)> hoặc <(la_nguyen_to :: variables) = (0)>> {
  nếu <((n :: variables) mod (d :: variables) :: operators) = (0)> thì {
    đặt [la_nguyen_to v] thành (0) :: variables
  } :: control
  thay đổi [d v] một lượng (1) :: variables
} :: control
nếu <(la_nguyen_to :: variables) = (1)> thì {
  nói [YES] :: looks
} nếu không thì {
  nói [NO] :: looks
} :: control
`,

  // Bài 12
  "l12_count_range_vi": `
đặt [dem v] thành (0) :: variables
đặt [i v] thành (a :: variables) :: variables
lặp lại (((b :: variables) - (a :: variables) :: operators) + (1) :: operators) lần {
  nếu <((i :: variables) mod (k :: variables) :: operators) = (0)> thì {
    thay đổi [dem v] một lượng (1) :: variables
  } :: control
  thay đổi [i v] một lượng (1) :: variables
} :: control
nói (dem :: variables) :: looks
`,

  // Bài 13
  "l13_list_input_loop_vi": `
xóa tất cả của [Dãy số v] :: list
hỏi [Nhập số lượng N: ] và đợi :: sensing
đặt [n v] thành (câu trả lời :: sensing) :: variables
lặp lại (n :: variables) lần {
  hỏi [Nhập phần tử: ] và đợi :: sensing
  thêm (câu trả lời :: sensing) vào [Dãy số v] :: list
} :: control
`,

  // Bài 14
  "l14_find_max_list_vi": `
đặt [max v] thành (phần tử (1) của [Dãy số v] :: list) :: variables
đặt [i v] thành (2) :: variables
lặp lại ((kích thước của [Dãy số v] :: list) - (1) :: operators) lần {
  nếu <(phần tử (i :: variables) của [Dãy số v] :: list) > (max :: variables)> thì {
    đặt [max v] thành (phần tử (i :: variables) của [Dãy số v] :: list) :: variables
  } :: control
  thay đổi [i v] một lượng (1) :: variables
} :: control
nói (kết hợp [Giá trị lớn nhất: ] (max :: variables) :: operators) :: looks
`,
  "l14_bubble_sort_vi": `
đặt [i v] thành (1) :: variables
lặp lại ((kích thước của [Dãy số v] :: list) - (1) :: operators) lần {
  đặt [j v] thành (1) :: variables
  lặp lại ((kích thước của [Dãy số v] :: list) - (i :: variables) :: operators) lần {
    nếu <(phần tử (j :: variables) của [Dãy số v] :: list) > (phần tử ((j :: variables) + (1) :: operators) của [Dãy số v] :: list)> thì {
      đặt [tam v] thành (phần tử (j :: variables) của [Dãy số v] :: list) :: variables
      thay thế phần tử (j :: variables) của [Dãy số v] bằng (phần tử ((j :: variables) + (1) :: operators) của [Dãy số v] :: list) :: list
      thay thế phần tử ((j :: variables) + (1) :: operators) của [Dãy số v] bằng (tam :: variables) :: list
    } :: control
    thay đổi [j v] một lượng (1) :: variables
  } :: control
  thay đổi [i v] một lượng (1) :: variables
} :: control
`,

  // Bài 15
  "l15_substring_slice_vi": `
đặt [chuoi_con v] thành [] :: variables
đặt [i v] thành (L :: variables) :: variables
lặp lại (((R :: variables) - (L :: variables) :: operators) + (1) :: operators) lần {
  đặt [chuoi_con v] thành (kết hợp (chuoi_con :: variables) (ký tự (i :: variables) của (chuỗi_gốc :: variables) :: operators) :: operators) :: variables
  thay đổi [i v] một lượng (1) :: variables
} :: control
nói (chuoi_con :: variables) :: looks
`,

  // Bài 16
  "l16_split_words_vi": `
xóa tất cả của [Từ v] :: list
đặt [tu_hien_tai v] thành [] :: variables
đặt [i v] thành (1) :: variables
lặp lại (độ dài của (cau :: variables) :: operators) lần {
  đặt [c v] thành (ký tự (i :: variables) của (cau :: variables) :: operators) :: variables
  nếu <(c :: variables) = [ ]> thì {
    nếu <(độ dài của (tu_hien_tai :: variables) :: operators) > (0)> thì {
      thêm (tu_hien_tai :: variables) vào [Từ v] :: list
      đặt [tu_hien_tai v] thành [] :: variables
    } :: control
  } nếu không thì {
    đặt [tu_hien_tai v] thành (kết hợp (tu_hien_tai :: variables) (c :: variables) :: operators) :: variables
  } :: control
  thay đổi [i v] một lượng (1) :: variables
} :: control
nếu <(độ dài của (tu_hien_tai :: variables) :: operators) > (0)> thì {
  thêm (tu_hien_tai :: variables) vào [Từ v] :: list
} :: control
`
};

const outDir = path.join(__dirname, '../assets/rendered_blocks');
for (const [name, script] of Object.entries(BLOCKS_TO_RENDER)) {
  const outSvg = path.join(outDir, `${name}.svg`);
  const outPng = path.join(outDir, `${name}.png`);
  try {
    renderToSvgAndPng(script.trim(), outSvg, outPng);
    console.log(`[OK] Rendered ${name}`);
  } catch (err) {
    console.error(`[ERROR] ${name}:`, err.message);
  }
}
console.log("Hoàn tất sinh toàn bộ kho ảnh khối Scratch 3.0 vector chuyên sâu!");
