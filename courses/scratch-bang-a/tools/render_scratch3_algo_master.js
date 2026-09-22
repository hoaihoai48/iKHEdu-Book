const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { renderToSvgAndPng } = require('./render_scratch3_master.js');

const PROBLEMS_DIR = path.join(__dirname, '../problems');
const PY_PROBLEMS_DIR = path.join(__dirname, '../../python-bang-a/problems');

const MAPPING = [
  ["sca_l03", ["pya_l01"]],
  ["sca_l04", ["pya_l02"]],
  ["sca_l05", ["pya_l03"]],
  ["sca_l06", ["pya_l04", "pya_l05", "pya_l06"]],
  ["sca_l07", ["pya_l07"]],
  ["sca_l08", ["pya_l08"]],
  ["sca_l09", ["pya_l09"]],
  ["sca_l10", ["pya_l10"]],
  ["sca_l11", ["pya_l11"]],
  ["sca_l12", ["pya_l12"]],
  ["sca_l13", ["pya_l16"]],
  ["sca_l14", ["pya_l17"]],
  ["sca_l15", ["pya_l13"]],
  ["sca_l16", ["pya_l14", "pya_l15"]],
];

// Build mapping table from sca_folder -> py_solution_file
const PROBLEM_MAP = {};
for (const [scaPref, pyPrefs] of MAPPING) {
  const pyDirs = [];
  for (const pref of pyPrefs) {
    const matched = fs.readdirSync(PY_PROBLEMS_DIR)
      .filter(d => d.startsWith(pref + '_') && fs.statSync(path.join(PY_PROBLEMS_DIR, d)).isDirectory())
      .sort();
    pyDirs.push(...matched);
  }
  pyDirs.forEach((pyName, idx) => {
    const parts = pyName.split('_');
    const namePart = parts.length >= 4 ? parts.slice(3).join('_') : parts.slice(2).join('_');
    const scaName = `${scaPref}_p${String(idx + 1).padStart(2, '0')}_${namePart}`;
    PROBLEM_MAP[scaName] = path.join(PY_PROBLEMS_DIR, pyName, 'solution.py');
  });
}

function runBatchAlgo() {
  const dirs = fs.readdirSync(PROBLEMS_DIR).filter(d => !d.startsWith('sca_pen_') && fs.statSync(path.join(PROBLEMS_DIR, d)).isDirectory()).sort();
  console.log(`Processing ${dirs.length} algorithm problems with Authentic Problem-Specific AST Scratchblocks...`);
  
  let successCount = 0;
  let skippedCount = 0;

  for (const d of dirs) {
    const dirPath = path.join(PROBLEMS_DIR, d);
    const hdPath = path.join(dirPath, 'Huong_Dan_Giang_Day.md');
    if (!fs.existsSync(hdPath)) continue;

    const pySolPath = PROBLEM_MAP[d];
    if (!pySolPath || !fs.existsSync(pySolPath)) {
      console.warn(`  ⚠️ Không tìm thấy solution.py cho ${d}`);
      skippedCount++;
      continue;
    }

    // Call Python ScratchTranslator
    try {
      const pyCmd = `python3 -c "import sys, json; sys.path.append('courses/scratch-bang-a/tools'); from scratch_ast_translator import ScratchTranslator; sb, steps = ScratchTranslator().translate(open('${pySolPath}').read()); print(json.dumps({'sb': sb, 'steps': steps}))"`;
      const resJson = execSync(pyCmd, { encoding: 'utf8', cwd: path.join(__dirname, '../../..') });
      const { sb, steps } = JSON.parse(resJson.trim());

      if (!sb) {
        console.warn(`  ⚠️ Không dịch được AST cho ${d}`);
        skippedCount++;
        continue;
      }

      const svgPath = path.join(dirPath, 'solution_blocks_vi.svg');
      const pngPath = path.join(dirPath, 'solution_blocks_vi.png');

      renderToSvgAndPng(sb.trim(), svgPath, pngPath);

      // Cập nhật Mục 4 trong Huong_Dan_Giang_Day.md
      const hdContent = fs.readFileSync(hdPath, 'utf8');
      const newSec4 = `## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
${steps.map(s => '> - ' + s).join('\n')}
`;
      let content = hdContent;
      const idx4 = content.indexOf('## 4. Lời giải tham khảo');
      if (idx4 !== -1) {
        content = content.slice(0, idx4) + newSec4;
      } else {
        content += '\n\n' + newSec4;
      }
      fs.writeFileSync(hdPath, content, 'utf8');
      successCount++;

      if (successCount % 25 === 0 || successCount === dirs.length) {
        console.log(`  → Đã hoàn thành ${successCount}/${dirs.length} bài (${d})`);
      }
    } catch (e) {
      console.error(`  ❌ Lỗi khi xử lý ${d}:`, e.message);
    }
  }

  console.log(`\n🎉 HOÀN THÀNH TOÀN BỘ: Đã cập nhật và render chuẩn xác ${successCount} / ${dirs.length} bài toán thuật toán Scratch!`);
}

if (require.main === module) {
  runBatchAlgo();
}
