import os
import json
import random
import subprocess
import shutil
import zipfile

BASE_DIR = "/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/problems"
os.makedirs(BASE_DIR, exist_ok=True)

PROBLEMS = []

# Helper to build problem
def build_problem(p):
    slug = p["slug"]
    pdir = os.path.join(BASE_DIR, slug)
    os.makedirs(pdir, exist_ok=True)

    with open(os.path.join(pdir, "De_Bai.md"), "w", encoding="utf-8") as f:
        f.write(p["statement"])

    with open(os.path.join(pdir, "Huong_Dan_Giang_Day.md"), "w", encoding="utf-8") as f:
        f.write(p["guide"])

    cpp_path = os.path.join(pdir, "solution.cpp")
    with open(cpp_path, "w", encoding="utf-8") as f:
        f.write(p["solution_cpp"])

    binary_path = os.path.join(pdir, "solution_exec")
    comp_res = subprocess.run(["g++", "-O3", "-std=c++17", cpp_path, "-o", binary_path], capture_output=True, text=True)
    if comp_res.returncode != 0:
        print(f"❌ Compilation failed for {slug}:\n{comp_res.stderr}")
        return False

    test_dir = os.path.join(pdir, "test")
    os.makedirs(test_dir, exist_ok=True)

    tests = p["gen_tests"]()
    for i, tdata in enumerate(tests, 1):
        inp_str = p["format_inp"](tdata)
        inp_file = os.path.join(test_dir, f"test{i:02d}.inp")
        out_file = os.path.join(test_dir, f"test{i:02d}.out")

        with open(inp_file, "w", encoding="utf-8") as f:
            f.write(inp_str)

        run_res = subprocess.run([binary_path], input=inp_str, capture_output=True, text=True)
        if run_res.returncode != 0:
            print(f"❌ Runtime error on test {i} for {slug}:\n{run_res.stderr}")
            return False

        with open(out_file, "w", encoding="utf-8") as f:
            f.write(run_res.stdout)

    zip_path = os.path.join(pdir, "test.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(os.listdir(test_dir)):
            if f.endswith(".inp") or f.endswith(".out"):
                zf.write(os.path.join(test_dir, f), f)

    shutil.rmtree(test_dir)
    if os.path.exists(binary_path):
        os.remove(binary_path)

    print(f"✅ [{p['id']}] {p['title']} ({slug}) verified & built successfully.")
    return True

