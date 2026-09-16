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

// 2. Exact realistic Scratchblocks scripts for all 37 Pen Problems
const PEN_SCRIPTS = {
  "sca_pen_p00_setup_net_ve": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt hướng bằng (90) :: motion
chọn màu vẽ [#ff0000] :: pen
đặt kích thước bút vẽ bằng (3) :: pen
đặt bút :: pen
lặp lại (4) lần {
  di chuyển (50) bước :: motion
  di chuyển (-50) bước :: motion
  xoay phải @turnRight (90) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả",
      "nhấc bút",
      "đi tới điểm x: (0) y: (0)",
      "đặt hướng bằng (90)",
      "đặt màu bút vẽ thành màu đỏ",
      "đặt kích thước bút vẽ bằng (3)",
      "đặt bút",
      "lặp lại (4) lần:",
      "  di chuyển (50) bước",
      "  di chuyển (-50) bước",
      "  xoay phải ↻ (90) độ"
    ]
  },
  "sca_pen_p01_da_giac_deu": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (-120) y: (50) :: motion
đặt hướng bằng (90) :: motion
đặt kích thước bút vẽ bằng (3) :: pen
đặt bút :: pen
lặp lại (3) lần {
  di chuyển (80) bước :: motion
  xoay phải @turnRight (120) độ :: motion
} :: control
nhấc bút :: pen
đi tới điểm x: (40) y: (50) :: motion
đặt bút :: pen
lặp lại (4) lần {
  di chuyển (80) bước :: motion
  xoay phải @turnRight (90) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả",
      "nhấc bút",
      "đi tới điểm x: (-120) y: (50)",
      "đặt hướng bằng (90)",
      "đặt kích thước bút vẽ bằng (3)",
      "đặt bút",
      "lặp lại (3) lần (vẽ tam giác đều):",
      "  di chuyển (80) bước",
      "  xoay phải ↻ (120) độ",
      "nhấc bút và đi tới điểm x: (40) y: (50)",
      "đặt bút",
      "lặp lại (4) lần (vẽ hình vuông):",
      "  di chuyển (80) bước",
      "  xoay phải ↻ (90) độ"
    ]
  },
  "sca_pen_p02_ban_phim_da_giac": {
    "script": `
khi phím [1 v] được bấm :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt bút :: pen
lặp lại (3) lần {
  di chuyển (100) bước :: motion
  xoay phải @turnRight (120) độ :: motion
} :: control

khi phím [2 v] được bấm :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt bút :: pen
lặp lại (4) lần {
  di chuyển (100) bước :: motion
  xoay phải @turnRight (90) độ :: motion
} :: control
`,
    "steps": [
      "khi phím [1] được bấm:",
      "  xóa tất cả, nhấc bút, đi tới điểm x: (0) y: (0), đặt bút",
      "  lặp lại (3) lần: di chuyển (100) bước, xoay phải ↻ (120) độ",
      "khi phím [2] được bấm:",
      "  xóa tất cả, nhấc bút, đi tới điểm x: (0) y: (0), đặt bút",
      "  lặp lại (4) lần: di chuyển (100) bước, xoay phải ↻ (90) độ"
    ]
  },
  "sca_pen_p03_doi_mau_net_dam": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt hướng bằng (90) :: motion
đặt kích thước bút vẽ bằng (2) :: pen
đặt bút :: pen
lặp lại (4) lần {
  thay đổi màu bút vẽ một lượng (25) :: pen
  thay đổi kích thước bút vẽ một lượng (2) :: pen
  di chuyển (100) bước :: motion
  xoay phải @turnRight (90) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới điểm x: (0) y: (0), đặt hướng bằng (90)",
      "đặt kích thước bút vẽ bằng (2), đặt bút",
      "lặp lại (4) lần:",
      "  thay đổi màu bút vẽ một lượng (25)",
      "  thay đổi kích thước bút vẽ một lượng (2)",
      "  di chuyển (100) bước",
      "  xoay phải ↻ (90) độ"
    ]
  },
  "sca_pen_p04_cap_tam_giac_doi_xung": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (50) :: motion
đặt hướng bằng (90) :: motion
đặt kích thước bút vẽ bằng (3) :: pen
đặt bút :: pen
lặp lại (3) lần {
  di chuyển (120) bước :: motion
  xoay phải @turnRight (120) độ :: motion
} :: control
nhấc bút :: pen
đi tới điểm x: (0) y: (-20) :: motion
đặt hướng bằng (210) :: motion
đặt bút :: pen
lặp lại (3) lần {
  di chuyển (120) bước :: motion
  xoay phải @turnRight (120) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới điểm x: (0) y: (50), đặt hướng bằng (90)",
      "đặt bút, lặp lại (3) lần: di chuyển (120) bước, xoay phải ↻ (120) độ",
      "nhấc bút, đi tới điểm x: (0) y: (-20), đặt hướng bằng (210)",
      "đặt bút, lặp lại (3) lần: di chuyển (120) bước, xoay phải ↻ (120) độ"
    ]
  },
  "sca_pen_p05_vuong_dong_tam": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
đặt kích thước bút vẽ bằng (2) :: pen
đặt [canh v] thành (30) :: variables
lặp lại (5) lần {
  nhấc bút :: pen
  đi tới điểm x: ((0) - ((canh) / (2))) y: ((canh) / (2)) :: motion
  đặt hướng bằng (90) :: motion
  đặt bút :: pen
  lặp lại (4) lần {
    di chuyển (canh) bước :: motion
    xoay phải @turnRight (90) độ :: motion
  } :: control
  thay đổi [canh v] một lượng (30) :: variables
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, đặt kích thước bút vẽ bằng (2)",
      "đặt [canh] thành (30)",
      "lặp lại (5) lần:",
      "  nhấc bút, đi tới điểm x: (- canh / 2) y: (canh / 2), đặt hướng (90), đặt bút",
      "  lặp lại (4) lần: di chuyển (canh) bước, xoay phải ↻ (90) độ",
      "  thay đổi [canh] một lượng (30)"
    ]
  },
  "sca_pen_p06_la_co_xoay_vong": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt kích thước bút vẽ bằng (2) :: pen
hỏi [Nhập số lá cờ N:] và đợi :: sensing
đặt [N v] thành (câu trả lời :: sensing) :: variables
lặp lại (N) lần {
  đặt bút :: pen
  di chuyển (60) bước :: motion
  lặp lại (3) lần {
    di chuyển (40) bước :: motion
    xoay phải @turnRight (120) độ :: motion
  } :: control
  nhấc bút :: pen
  di chuyển (-60) bước :: motion
  xoay phải @turnRight ((360) / (N)) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới điểm x: (0) y: (0)",
      "hỏi [Nhập số lá cờ N:] và đợi, đặt [N] thành (câu trả lời)",
      "lặp lại (N) lần:",
      "  đặt bút, di chuyển (60) bước (cột cờ)",
      "  lặp lại (3) lần: di chuyển (40) bước, xoay phải ↻ (120) độ (lá cờ)",
      "  nhấc bút, di chuyển (-60) bước (lùi về tâm)",
      "  xoay phải ↻ (360 / N) độ"
    ]
  },
  "sca_pen_p07_ngoi_sao_5_canh": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (-70) y: (20) :: motion
đặt hướng bằng (90) :: motion
đặt kích thước bút vẽ bằng (3) :: pen
đặt màu bút vẽ thành [#ffcc00] :: pen
đặt bút :: pen
lặp lại (5) lần {
  di chuyển (150) bước :: motion
  xoay phải @turnRight (144) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới điểm x: (-70) y: (20), đặt hướng bằng (90)",
      "đặt kích thước bút vẽ bằng (3), đặt màu bút vẽ thành màu vàng",
      "đặt bút",
      "lặp lại (5) lần:",
      "  di chuyển (150) bước",
      "  xoay phải ↻ (144) độ"
    ]
  },
  "sca_pen_p08_tam_giac_xoay_chong": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt hướng bằng (90) :: motion
đặt kích thước bút vẽ bằng (3) :: pen
đặt bút :: pen
lặp lại (12) lần {
  lặp lại (3) lần {
    di chuyển (100) bước :: motion
    xoay phải @turnRight (120) độ :: motion
  } :: control
  xoay phải @turnRight ((360) / (12)) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới điểm x: (0) y: (0), đặt hướng bằng (90)",
      "đặt kích thước bút vẽ bằng (3), đặt bút",
      "lặp lại (12) lần:",
      "  lặp lại (3) lần: di chuyển (100) bước, xoay phải ↻ (120) độ",
      "  xoay phải ↻ (360 / 12) độ"
    ]
  },
  "sca_pen_p09_hoa_tiet_hinh_thoi": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt hướng bằng (90) :: motion
đặt kích thước bút vẽ bằng (2) :: pen
đặt bút :: pen
lặp lại (6) lần {
  lặp lại (2) lần {
    di chuyển (80) bước :: motion
    xoay phải @turnRight (60) độ :: motion
    di chuyển (80) bước :: motion
    xoay phải @turnRight (120) độ :: motion
  } :: control
  xoay phải @turnRight (60) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới điểm x: (0) y: (0), đặt hướng bằng (90)",
      "đặt kích thước bút vẽ bằng (2), đặt bút",
      "lặp lại (6) lần:",
      "  lặp lại (2) lần (vẽ 1 hình thoi):",
      "    di chuyển (80) bước, xoay phải ↻ (60) độ",
      "    di chuyển (80) bước, xoay phải ↻ (120) độ",
      "  xoay phải ↻ (60) độ"
    ]
  },
  "sca_pen_p10_hinh_tron_dong_tam": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
đặt kích thước bút vẽ bằng (3) :: pen
đặt [R v] thành (30) :: variables
lặp lại (3) lần {
  nhấc bút :: pen
  đi tới điểm x: (0) y: (R) :: motion
  đặt hướng bằng (90) :: motion
  đặt bút :: pen
  lặp lại (360) lần {
    di chuyển ((2 * (3.14 * (R))) / (360)) bước :: motion
    xoay phải @turnRight (1) độ :: motion
  } :: control
  thay đổi [R v] một lượng (30) :: variables
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, đặt kích thước bút vẽ bằng (3)",
      "đặt [R] thành (30)",
      "lặp lại (3) lần:",
      "  nhấc bút, đi tới điểm x: (0) y: (R), đặt hướng (90), đặt bút",
      "  lặp lại (360) lần: di chuyển ((2 * 3.14 * R) / 360) bước, xoay phải ↻ (1) độ",
      "  thay đổi [R] một lượng (30)"
    ]
  },
  "sca_pen_p10_kim_tu_thap_bac_thang": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (-120) y: (-80) :: motion
đặt hướng bằng (90) :: motion
đặt bút :: pen
đặt [tang v] thành (5) :: variables
đặt [rong v] thành (160) :: variables
lặp lại (tang) lần {
  lặp lại (2) lần {
    di chuyển (rong) bước :: motion
    xoay trái @turnLeft (90) độ :: motion
    di chuyển (25) bước :: motion
    xoay trái @turnLeft (90) độ :: motion
  } :: control
  nhấc bút :: pen
  di chuyển (15) bước :: motion
  xoay trái @turnLeft (90) độ :: motion
  di chuyển (25) bước :: motion
  xoay phải @turnRight (90) độ :: motion
  đặt bút :: pen
  thay đổi [rong v] một lượng (-30) :: variables
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới x: (-120) y: (-80), đặt hướng bằng (90), đặt bút",
      "đặt [tang] thành (5), đặt [rong] thành (160)",
      "lặp lại (tang) lần:",
      "  vẽ 1 bậc hình chữ nhật: lặp lại 2 lần [đi (rong), xoay trái 90, đi (25), xoay trái 90]",
      "  nhấc bút, di chuyển lên bậc trên: sang phải (15), lên trên (25), đặt bút",
      "  thay đổi [rong] một lượng (-30)"
    ]
  },
  "sca_pen_p11_cung_tron_cau_vong": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
đặt kích thước bút vẽ bằng (10) :: pen
đặt [R v] thành (60) :: variables
lặp lại (7) lần {
  nhấc bút :: pen
  đi tới điểm x: ((0) - (R)) y: (-50) :: motion
  đặt hướng bằng (0) :: motion
  thay đổi màu bút vẽ một lượng (15) :: pen
  đặt bút :: pen
  lặp lại (180) lần {
    di chuyển ((3.14 * (R)) / (180)) bước :: motion
    xoay phải @turnRight (1) độ :: motion
  } :: control
  thay đổi [R v] một lượng (12) :: variables
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, đặt kích thước bút vẽ bằng (10), đặt [R] thành (60)",
      "lặp lại (7) lần:",
      "  nhấc bút, đi tới x: (-R) y: (-50), đặt hướng bằng (0), đổi màu bút, đặt bút",
      "  lặp lại (180) lần: di chuyển (3.14 * R / 180) bước, xoay phải ↻ (1) độ",
      "  thay đổi [R] một lượng (12)"
    ]
  },
  "sca_pen_p11_luoi_o_vuong_ban_co": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đặt kích thước bút vẽ bằng (2) :: pen
đặt [hang v] thành (4) :: variables
đặt [cot v] thành (5) :: variables
đặt [canh v] thành (40) :: variables
đặt [r v] thành (0) :: variables
lặp lại (hang) lần {
  đặt [c v] thành (0) :: variables
  lặp lại (cot) lần {
    nhấc bút :: pen
    đi tới điểm x: ((-100) + ((c) * (canh))) y: ((80) - ((r) * (canh))) :: motion
    đặt hướng bằng (90) :: motion
    đặt bút :: pen
    lặp lại (4) lần {
      di chuyển (canh) bước :: motion
      xoay phải @turnRight (90) độ :: motion
    } :: control
    thay đổi [c v] một lượng (1) :: variables
  } :: control
  thay đổi [r v] một lượng (1) :: variables
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đặt kích thước bút vẽ bằng (2)",
      "đặt [hang] thành (4), đặt [cot] thành (5), đặt [canh] thành (40)",
      "lặp lại (hang) lần:",
      "  lặp lại (cot) lần:",
      "    nhấc bút, đi tới tọa độ ô: x = -100 + c * canh, y = 80 - r * canh",
      "    đặt bút, lặp lại (4) lần: di chuyển (canh) bước, xoay phải ↻ (90) độ",
      "    thay đổi [c] một lượng (1)",
      "  thay đổi [r] một lượng (1)"
    ]
  },
  "sca_pen_p12_logo_olympic": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
đặt kích thước bút vẽ bằng (6) :: pen
đặt màu bút vẽ thành [#0055ff] :: pen
nhấc bút :: pen
đi tới điểm x: (-110) y: (20) :: motion
đặt bút :: pen
lặp lại (360) lần {
  di chuyển (0.8) bước :: motion
  xoay phải @turnRight (1) độ :: motion
} :: control
đặt màu bút vẽ thành [#000000] :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (20) :: motion
đặt bút :: pen
lặp lại (360) lần {
  di chuyển (0.8) bước :: motion
  xoay phải @turnRight (1) độ :: motion
} :: control
đặt màu bút vẽ thành [#ff0000] :: pen
nhấc bút :: pen
đi tới điểm x: (110) y: (20) :: motion
đặt bút :: pen
lặp lại (360) lần {
  di chuyển (0.8) bước :: motion
  xoay phải @turnRight (1) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, đặt kích thước bút vẽ bằng (6)",
      "vòng 1 (Xanh lam): đi tới x: (-110) y: (20), đặt bút, lặp 360 [đi 0.8, xoay 1]",
      "vòng 2 (Đen): đi tới x: (0) y: (20), đặt bút, lặp 360 [đi 0.8, xoay 1]",
      "vòng 3 (Đỏ): đi tới x: (110) y: (20), đặt bút, lặp 360 [đi 0.8, xoay 1]"
    ]
  },
  "sca_pen_p12_tam_giac_nhieu_tang": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đặt [tang v] thành (3) :: variables
đặt [canh v] thành (50) :: variables
đặt [i v] thành (1) :: variables
lặp lại (tang) lần {
  đặt [j v] thành (1) :: variables
  lặp lại (i) lần {
    nhấc bút :: pen
    đi tới điểm x: (((-100) + ((j) * (canh))) - (((i) * (canh)) / (2))) y: ((80) - ((i) * (canh))) :: motion
    đặt hướng bằng (90) :: motion
    đặt bút :: pen
    lặp lại (3) lần {
      di chuyển (canh) bước :: motion
      xoay phải @turnRight (120) độ :: motion
    } :: control
    thay đổi [j v] một lượng (1) :: variables
  } :: control
  thay đổi [i v] một lượng (1) :: variables
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đặt [tang] thành (3), đặt [canh] thành (50)",
      "lặp lại (tang) tầng từ trên xuống dưới:",
      "  ở tầng thứ i, lặp lại i lần vẽ tam giác cạnh (canh)",
      "  xoay chuyển tọa độ xếp sít các tam giác cạnh nhau"
    ]
  },
  "sca_pen_p13_canh_hoa_co_ban": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (-50) :: motion
đặt hướng bằng (0) :: motion
đặt kích thước bút vẽ bằng (3) :: pen
đặt màu bút vẽ thành [#ff3366] :: pen
đặt bút :: pen
lặp lại (2) lần {
  lặp lại (90) lần {
    di chuyển (1.2) bước :: motion
    xoay phải @turnRight (1) độ :: motion
  } :: control
  xoay phải @turnRight (90) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới x: (0) y: (-50), đặt hướng (0)",
      "đặt kích thước bút vẽ bằng (3), chọn màu hồng sen, đặt bút",
      "lặp lại (2) lần để ghép 2 cung tròn 90 độ:",
      "  lặp lại (90) lần: di chuyển (1.2) bước, xoay phải ↻ (1) độ",
      "  xoay phải ↻ (90) độ để đảo chiều cong"
    ]
  },
  "sca_pen_p13_luc_giac_long_nhau": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
đặt kích thước bút vẽ bằng (2) :: pen
đặt [canh v] thành (120) :: variables
lặp lại (4) lần {
  nhấc bút :: pen
  đi tới điểm x: ((0) - ((canh) / (2))) y: (canh) :: motion
  đặt hướng bằng (90) :: motion
  đặt bút :: pen
  lặp lại (6) lần {
    di chuyển (canh) bước :: motion
    xoay phải @turnRight (60) độ :: motion
  } :: control
  thay đổi [canh v] một lượng (-25) :: variables
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, đặt kích thước bút vẽ bằng (2), đặt [canh] thành (120)",
      "lặp lại (4) lần:",
      "  nhấc bút, đi tới x: (- canh / 2) y: (canh), đặt hướng 90, đặt bút",
      "  lặp lại (6) lần: di chuyển (canh) bước, xoay phải ↻ (60) độ",
      "  thay đổi [canh] một lượng (-25)"
    ]
  },
  "sca_pen_p14_bong_hoa_8_canh": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt kích thước bút vẽ bằng (2) :: pen
đặt [so_canh v] thành (8) :: variables
lặp lại (so_canh) lần {
  thay đổi màu bút vẽ một lượng (20) :: pen
  đặt bút :: pen
  lặp lại (2) lần {
    lặp lại (90) lần {
      di chuyển (1) bước :: motion
      xoay phải @turnRight (1) độ :: motion
    } :: control
    xoay phải @turnRight (90) độ :: motion
  } :: control
  nhấc bút :: pen
  xoay phải @turnRight ((360) / (so_canh)) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới điểm x: (0) y: (0)",
      "đặt kích thước bút vẽ bằng (2), đặt [so_canh] thành (8)",
      "lặp lại (8) lần:",
      "  đổi màu bút, đặt bút",
      "  vẽ 1 cánh hoa: lặp 2 [lặp 90 (đi 1, xoay phải 1 độ), xoay phải 90 độ]",
      "  nhấc bút, xoay phải ↻ (360 / 8) độ"
    ]
  },
  "sca_pen_p14_ngoi_sao_8_canh_nghe_thuat": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (-50) y: (50) :: motion
đặt hướng bằng (90) :: motion
đặt kích thước bút vẽ bằng (3) :: pen
đặt bút :: pen
lặp lại (4) lần {
  di chuyển (100) bước :: motion
  xoay phải @turnRight (90) độ :: motion
} :: control
nhấc bút :: pen
đi tới điểm x: (0) y: (70) :: motion
đặt hướng bằng (135) :: motion
đặt bút :: pen
lặp lại (4) lần {
  di chuyển (100) bước :: motion
  xoay phải @turnRight (90) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới x: (-50) y: (50), đặt hướng 90, đặt bút",
      "lặp lại 4 lần: di chuyển (100) bước, xoay phải ↻ (90) độ (hình vuông 1)",
      "nhấc bút, đi tới x: (0) y: (70), đặt hướng 135 độ, đặt bút",
      "lặp lại 4 lần: di chuyển (100) bước, xoay phải ↻ (90) độ (hình vuông 2 xoay 45 độ)"
    ]
  },
  "sca_pen_p15_cay_thong_noel": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đặt kích thước bút vẽ bằng (3) :: pen
đặt màu bút vẽ thành [#228822] :: pen
đi tới điểm x: (-30) y: (60) :: motion
đặt hướng bằng (90) :: motion
đặt bút :: pen
lặp lại (3) lần {
  di chuyển (60) bước :: motion
  xoay phải @turnRight (120) độ :: motion
} :: control
nhấc bút :: pen
đi tới điểm x: (-45) y: (15) :: motion
đặt bút :: pen
lặp lại (3) lần {
  di chuyển (90) bước :: motion
  xoay phải @turnRight (120) độ :: motion
} :: control
nhấc bút :: pen
đi tới điểm x: (-60) y: (-35) :: motion
đặt bút :: pen
lặp lại (3) lần {
  di chuyển (120) bước :: motion
  xoay phải @turnRight (120) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, chọn màu xanh lá, đặt kích thước bút vẽ bằng (3)",
      "vẽ tầng 1 (nhỏ): đi tới x: (-30) y: (60), đặt bút, lặp 3 [đi 60, xoay 120]",
      "vẽ tầng 2 (vừa): đi tới x: (-45) y: (15), đặt bút, lặp 3 [đi 90, xoay 120]",
      "vẽ tầng 3 (lớn): đi tới x: (-60) y: (-35), đặt bút, lặp 3 [đi 120, xoay 120]"
    ]
  },
  "sca_pen_p15_hoa_chong_chong": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt kích thước bút vẽ bằng (3) :: pen
lặp lại (4) lần {
  thay đổi màu bút vẽ một lượng (30) :: pen
  đặt bút :: pen
  di chuyển (80) bước :: motion
  xoay phải @turnRight (90) độ :: motion
  di chuyển (40) bước :: motion
  xoay phải @turnRight (90) độ :: motion
  di chuyển (80) bước :: motion
  nhấc bút :: pen
  xoay phải @turnRight (90) độ :: motion
  di chuyển (40) bước :: motion
  xoay phải @turnRight (90) độ :: motion
  xoay phải @turnRight (90) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới điểm x: (0) y: (0)",
      "đặt kích thước bút vẽ bằng (3)",
      "lặp lại (4) lần:",
      "  thay đổi màu bút vẽ một lượng (30), đặt bút",
      "  vẽ 1 cánh chong chóng lệch tâm, quay về tâm",
      "  xoay phải ↻ (90) độ"
    ]
  },
  "sca_pen_p21_hinh_tron_co_ban": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt hướng bằng (90) :: motion
đặt kích thước bút vẽ bằng (3) :: pen
đặt màu bút vẽ thành [#0055ff] :: pen
hỏi [Nhập bán kính R:] và đợi :: sensing
đặt [R v] thành (câu trả lời :: sensing) :: variables
đặt [buoc_cong v] thành (((2 * (3.14 * (R))) / (360)) :: operators) :: variables
nhấc bút :: pen
đi tới điểm x: (0) y: (R) :: motion
đặt bút :: pen
lặp lại (360) lần {
  di chuyển (buoc_cong) bước :: motion
  xoay phải @turnRight (1) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới điểm x: (0) y: (0), đặt hướng bằng (90)",
      "đặt kích thước bút vẽ bằng (3), chọn màu xanh lam",
      "hỏi [Nhập bán kính R:] và đợi, đặt [R] thành (câu trả lời)",
      "đặt [buoc_cong] thành ((2 * 3.14 * R) / 360)",
      "nhấc bút, đi tới điểm xuất phát đỉnh đường tròn x: (0) y: (R)",
      "đặt bút",
      "lặp lại (360) lần:",
      "  di chuyển (buoc_cong) bước",
      "  xoay phải ↻ (1) độ"
    ]
  },
  "sca_pen_p22_hinh_tron_dong_tam_da_sac": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
đặt kích thước bút vẽ bằng (3) :: pen
hỏi [Nhập số vòng tròn N:] và đợi :: sensing
đặt [N v] thành (câu trả lời :: sensing) :: variables
đặt [R v] thành (25) :: variables
lặp lại (N) lần {
  thay đổi màu bút vẽ một lượng (20) :: pen
  nhấc bút :: pen
  đi tới điểm x: (0) y: (R) :: motion
  đặt hướng bằng (90) :: motion
  đặt bút :: pen
  lặp lại (360) lần {
    di chuyển (((2 * (3.14 * (R))) / (360)) :: operators) bước :: motion
    xoay phải @turnRight (1) độ :: motion
  } :: control
  thay đổi [R v] một lượng (25) :: variables
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, đặt kích thước bút vẽ bằng (3)",
      "hỏi [Nhập số vòng tròn N:] và đợi, đặt [N] thành (câu trả lời)",
      "đặt [R] thành (25)",
      "lặp lại (N) lần:",
      "  đổi màu bút vẽ một lượng (20)",
      "  nhấc bút, đi tới điểm đỉnh x: (0) y: (R), đặt hướng 90, đặt bút",
      "  lặp lại (360) lần: di chuyển ((2 * 3.14 * R) / 360) bước, xoay phải ↻ (1) độ",
      "  thay đổi [R] một lượng (25)"
    ]
  },
  "sca_pen_p23_logo_olympic_5_mau": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
đặt kích thước bút vẽ bằng (8) :: pen
đặt màu bút vẽ thành [#0055ff] :: pen
nhấc bút :: pen
đi tới điểm x: (-110) y: (30) :: motion
đặt hướng bằng (90) :: motion
đặt bút :: pen
lặp lại (360) lần {
  di chuyển (0.8) bước :: motion
  xoay phải @turnRight (1) độ :: motion
} :: control
đặt màu bút vẽ thành [#000000] :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (30) :: motion
đặt bút :: pen
lặp lại (360) lần {
  di chuyển (0.8) bước :: motion
  xoay phải @turnRight (1) độ :: motion
} :: control
đặt màu bút vẽ thành [#ff0000] :: pen
nhấc bút :: pen
đi tới điểm x: (110) y: (30) :: motion
đặt bút :: pen
lặp lại (360) lần {
  di chuyển (0.8) bước :: motion
  xoay phải @turnRight (1) độ :: motion
} :: control
đặt màu bút vẽ thành [#ffcc00] :: pen
nhấc bút :: pen
đi tới điểm x: (-55) y: (-15) :: motion
đặt bút :: pen
lặp lại (360) lần {
  di chuyển (0.8) bước :: motion
  xoay phải @turnRight (1) độ :: motion
} :: control
đặt màu bút vẽ thành [#00aa00] :: pen
nhấc bút :: pen
đi tới điểm x: (55) y: (-15) :: motion
đặt bút :: pen
lặp lại (360) lần {
  di chuyển (0.8) bước :: motion
  xoay phải @turnRight (1) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, đặt kích thước bút vẽ bằng (8)",
      "vẽ 3 vòng hàng trên: Xanh lam (-110, 30), Đen (0, 30), Đỏ (110, 30)",
      "vẽ 2 vòng đan xen hàng dưới: Vàng (-55, -15), Xanh lá (55, -15)",
      "mỗi vòng tròn lặp 360 lần [di chuyển 0.8 bước, xoay phải 1 độ]"
    ]
  },
  "sca_pen_p24_cung_tron_cau_vong_7_mau": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
đặt kích thước bút vẽ bằng (12) :: pen
đặt [R v] thành (60) :: variables
lặp lại (7) lần {
  thay đổi màu bút vẽ một lượng (15) :: pen
  nhấc bút :: pen
  đi tới điểm x: ((0) - (R)) y: (-60) :: motion
  đặt hướng bằng (0) :: motion
  đặt bút :: pen
  lặp lại (180) lần {
    di chuyển (((3.14 * (R)) / (180)) :: operators) bước :: motion
    xoay phải @turnRight (1) độ :: motion
  } :: control
  thay đổi [R v] một lượng (14) :: variables
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, đặt kích thước bút vẽ bằng (12), đặt [R] thành (60)",
      "lặp lại (7) lần ứng với 7 sắc cầu vồng:",
      "  thay đổi màu bút vẽ một lượng (15)",
      "  nhấc bút, đi tới điểm chân cầu vồng x: (-R) y: (-60), đặt hướng 0 độ, đặt bút",
      "  lặp lại (180) lần: di chuyển (3.14 * R / 180) bước, xoay phải ↻ (1) độ",
      "  thay đổi [R] một lượng (14)"
    ]
  },
  "sca_pen_p25_canh_hoa_cung_tron_90": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (-60) :: motion
đặt hướng bằng (0) :: motion
đặt kích thước bút vẽ bằng (3) :: pen
đặt màu bút vẽ thành [#ff3366] :: pen
đặt bút :: pen
lặp lại (2) lần {
  lặp lại (90) lần {
    di chuyển (1.4) bước :: motion
    xoay phải @turnRight (1) độ :: motion
  } :: control
  xoay phải @turnRight (90) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới x: (0) y: (-60), đặt hướng 0 độ",
      "đặt kích thước bút vẽ bằng (3), chọn màu hồng sen, đặt bút",
      "lặp lại (2) lần:",
      "  lặp lại (90) lần: di chuyển (1.4) bước, xoay phải ↻ (1) độ",
      "  xoay phải ↻ (90) độ"
    ]
  },
  "sca_pen_p26_bong_hoa_da_canh": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt kích thước bút vẽ bằng (2) :: pen
hỏi [Nhập số cánh hoa K:] và đợi :: sensing
đặt [K v] thành (câu trả lời :: sensing) :: variables
lặp lại (K) lần {
  thay đổi màu bút vẽ một lượng (15) :: pen
  đặt bút :: pen
  lặp lại (2) lần {
    lặp lại (90) lần {
      di chuyển (1) bước :: motion
      xoay phải @turnRight (1) độ :: motion
    } :: control
    xoay phải @turnRight (90) độ :: motion
  } :: control
  nhấc bút :: pen
  xoay phải @turnRight ((360) / (K)) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới điểm x: (0) y: (0), đặt kích thước bút vẽ bằng (2)",
      "hỏi [Nhập số cánh hoa K:] và đợi, đặt [K] thành (câu trả lời)",
      "lặp lại (K) lần:",
      "  thay đổi màu bút vẽ, đặt bút",
      "  vẽ 1 cánh hoa: lặp 2 [lặp 90 (đi 1, xoay phải 1 độ), xoay phải 90 độ]",
      "  nhấc bút, xoay phải ↻ (360 / K) độ"
    ]
  },
  "sca_pen_p27_chong_chong_gio": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt kích thước bút vẽ bằng (3) :: pen
hỏi [Nhập số cánh chong chóng (4 hoặc 6):] và đợi :: sensing
đặt [N v] thành (câu trả lời :: sensing) :: variables
lặp lại (N) lần {
  thay đổi màu bút vẽ một lượng (25) :: pen
  đặt bút :: pen
  di chuyển (70) bước :: motion
  lặp lại (90) lần {
    di chuyển (0.8) bước :: motion
    xoay phải @turnRight (1) độ :: motion
  } :: control
  di chuyển (70) bước :: motion
  nhấc bút :: pen
  đi tới điểm x: (0) y: (0) :: motion
  xoay phải @turnRight ((360) / (N)) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới x: (0) y: (0), đặt kích thước bút vẽ bằng (3)",
      "hỏi [Nhập số cánh chong chóng:] và đợi, đặt [N] thành (câu trả lời)",
      "lặp lại (N) lần:",
      "  đổi màu bút, đặt bút",
      "  vẽ cánh chong chóng cong vút: đi 70, lặp 90 [đi 0.8, xoay 1], đi 70",
      "  nhấc bút, trở về tâm (0, 0), xoay phải ↻ (360 / N) độ"
    ]
  },
  "sca_pen_p28_bong_hoa_tuyet_pha_le": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt hướng bằng (0) :: motion
đặt kích thước bút vẽ bằng (2) :: pen
đặt màu bút vẽ thành [#33ccff] :: pen
lặp lại (6) lần {
  đặt bút :: pen
  di chuyển (40) bước :: motion
  xoay trái @turnLeft (45) độ :: motion
  di chuyển (20) bước :: motion
  di chuyển (-20) bước :: motion
  xoay phải @turnRight (90) độ :: motion
  di chuyển (20) bước :: motion
  di chuyển (-20) bước :: motion
  xoay trái @turnLeft (45) độ :: motion
  di chuyển (40) bước :: motion
  nhấc bút :: pen
  đi tới điểm x: (0) y: (0) :: motion
  xoay phải @turnRight (60) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới x: (0) y: (0), đặt hướng bằng (0)",
      "đặt kích thước bút vẽ bằng (2), chọn màu xanh băng tuyết",
      "lặp lại (6) lần vẽ 6 nhánh đối xứng:",
      "  đặt bút, đi 40 bước, rẽ nhánh phụ trái (20 bước), rẽ nhánh phụ phải (20 bước), đi tiếp 40 bước",
      "  nhấc bút, quay về tâm (0, 0), xoay phải ↻ (60) độ"
    ]
  },
  "sca_pen_p29_hinh_tron_khuyet": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt kích thước bút vẽ bằng (4) :: pen
đặt màu bút vẽ thành [#ffcc00] :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (80) :: motion
đặt hướng bằng (90) :: motion
đặt bút :: pen
lặp lại (240) lần {
  di chuyển (1.4) bước :: motion
  xoay phải @turnRight (1) độ :: motion
} :: control
xoay phải @turnRight (120) độ :: motion
lặp lại (180) lần {
  di chuyển (1.0) bước :: motion
  xoay trái @turnLeft (1) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới x: (0) y: (80), đặt hướng 90",
      "đặt kích thước bút vẽ bằng (4), chọn màu vàng trăng",
      "đặt bút, vẽ cung tròn ngoài: lặp lại (240) lần [đi 1.4, xoay phải 1 độ]",
      "xoay phải 120 độ, vẽ cung tròn trong: lặp lại (180) lần [đi 1.0, xoay trái 1 độ]"
    ]
  },
  "sca_pen_p30_chia_banh_pizza_n_phan": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt kích thước bút vẽ bằng (3) :: pen
hỏi [Nhập số miếng pizza N:] và đợi :: sensing
đặt [N v] thành (câu trả lời :: sensing) :: variables
đặt [R v] thành (100) :: variables
lặp lại (N) lần {
  thay đổi màu bút vẽ một lượng (20) :: pen
  đặt bút :: pen
  di chuyển (R) bước :: motion
  nhấc bút :: pen
  di chuyển ((0) - (R)) bước :: motion
  xoay phải @turnRight ((360) / (N)) độ :: motion
} :: control
nhấc bút :: pen
đi tới điểm x: (0) y: (R) :: motion
đặt hướng bằng (90) :: motion
đặt bút :: pen
lặp lại (360) lần {
  di chuyển (((2 * (3.14 * (R))) / (360)) :: operators) bước :: motion
  xoay phải @turnRight (1) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới x: (0) y: (0), đặt kích thước bút vẽ bằng (3)",
      "hỏi [Nhập số miếng pizza N:] và đợi, đặt [N] thành (câu trả lời), đặt [R] thành (100)",
      "lặp lại (N) lần vẽ các đường nan quạt chia bánh:",
      "  đổi màu bút, đặt bút, đi (R) bước ra viền, lùi về tâm, xoay phải ↻ (360 / N) độ",
      "vẽ đường viền tròn khép kín quanh bánh pizza (bán kính R)"
    ]
  },
  "sca_pen_p31_hoa_van_xoan_oc": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt hướng bằng (90) :: motion
đặt kích thước bút vẽ bằng (2) :: pen
đặt [buoc v] thành (1) :: variables
đặt bút :: pen
lặp lại (150) lần {
  thay đổi màu bút vẽ một lượng (2) :: pen
  di chuyển (buoc) bước :: motion
  xoay phải @turnRight (15) độ :: motion
  thay đổi [buoc v] một lượng (0.5) :: variables
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới điểm x: (0) y: (0), đặt hướng bằng (90)",
      "đặt kích thước bút vẽ bằng (2), đặt [buoc] thành (1), đặt bút",
      "lặp lại (150) lần:",
      "  thay đổi màu bút vẽ một lượng (2)",
      "  di chuyển (buoc) bước",
      "  xoay phải ↻ (15) độ",
      "  thay đổi [buoc] một lượng (0.5)"
    ]
  },
  "sca_pen_p32_chuoi_vong_ngoc_trai": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt kích thước bút vẽ bằng (2) :: pen
đặt [so_hat v] thành (12) :: variables
lặp lại (so_hat) lần {
  nhấc bút :: pen
  di chuyển (100) bước :: motion
  đặt bút :: pen
  đặt kích thước bút vẽ bằng (14) :: pen
  di chuyển (1) bước :: motion
  nhấc bút :: pen
  đặt kích thước bút vẽ bằng (2) :: pen
  di chuyển (-101) bước :: motion
  xoay phải @turnRight ((360) / (so_hat)) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới x: (0) y: (0)",
      "đặt [so_hat] thành (12)",
      "lặp lại (so_hat) lần:",
      "  nhấc bút, di chuyển (100) bước ra vị trí hạt ngọc",
      "  đặt bút, tăng kích thước bút lên (14), chấm 1 điểm hạt ngọc tròn",
      "  nhấc bút, giảm nét về (2), lùi về tâm, xoay phải ↻ (360 / so_hat) độ"
    ]
  },
  "sca_pen_p33_hoa_tiet_trang_tri_vien": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (-200) y: (0) :: motion
đặt hướng bằng (90) :: motion
đặt kích thước bút vẽ bằng (3) :: pen
đặt bút :: pen
lặp lại (5) lần {
  lặp lại (180) lần {
    di chuyển (0.5) bước :: motion
    xoay trái @turnLeft (1) độ :: motion
  } :: control
  lặp lại (180) lần {
    di chuyển (0.5) bước :: motion
    xoay phải @turnRight (1) độ :: motion
  } :: control
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới mép trái x: (-200) y: (0), đặt hướng 90, đặt bút",
      "đặt kích thước bút vẽ bằng (3)",
      "lặp lại (5) lần hoa văn sóng biển:",
      "  lặp lại 180 lần [đi 0.5 bước, xoay trái 1 độ] (sóng nhô lên)",
      "  lặp lại 180 lần [đi 0.5 bước, xoay phải 1 độ] (sóng lượn xuống)"
    ]
  },
  "sca_pen_p34_hoa_van_gach_hoa_co_dien": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (-50) y: (50) :: motion
đặt hướng bằng (90) :: motion
đặt kích thước bút vẽ bằng (3) :: pen
đặt bút :: pen
lặp lại (4) lần {
  di chuyển (100) bước :: motion
  lặp lại (2) lần {
    lặp lại (90) lần {
      di chuyển (0.8) bước :: motion
      xoay phải @turnRight (1) độ :: motion
    } :: control
    xoay phải @turnRight (90) độ :: motion
  } :: control
  xoay phải @turnRight (90) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới x: (-50) y: (50), đặt hướng bằng (90)",
      "đặt kích thước bút vẽ bằng (3), đặt bút",
      "lặp lại (4) lần vẽ 4 cạnh hình vuông kèm cánh hoa tại mỗi cạnh:",
      "  di chuyển (100) bước (cạnh hình vuông)",
      "  vẽ 1 cánh hoa gắn ở cạnh: lặp 2 [lặp 90 (đi 0.8, xoay 1), xoay 90]",
      "  xoay phải ↻ (90) độ"
    ]
  },
  "sca_pen_p35_dai_ngan_ha_van_hoa": {
    "script": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt kích thước bút vẽ bằng (2) :: pen
lặp lại (36) lần {
  thay đổi màu bút vẽ một lượng (10) :: pen
  đặt bút :: pen
  lặp lại (4) lần {
    di chuyển (60) bước :: motion
    xoay phải @turnRight (90) độ :: motion
  } :: control
  lặp lại (2) lần {
    lặp lại (90) lần {
      di chuyển (0.7) bước :: motion
      xoay phải @turnRight (1) độ :: motion
    } :: control
    xoay phải @turnRight (90) độ :: motion
  } :: control
  nhấc bút :: pen
  xoay phải @turnRight (10) độ :: motion
} :: control
`,
    "steps": [
      "khi bấm vào cờ xanh",
      "xóa tất cả, nhấc bút, đi tới x: (0) y: (0), đặt kích thước bút vẽ bằng (2)",
      "lặp lại (36) lần xoay quanh tâm mỗi lần 10 độ:",
      "  thay đổi màu bút vẽ một lượng (10), đặt bút",
      "  vẽ cụm họa tiết gồm hình vuông và cánh hoa cung tròn",
      "  nhấc bút, xoay phải ↻ (10) độ"
    ]
  }
};

module.exports = {
  renderToSvgAndPng,
  PEN_SCRIPTS
};
