import glob, os

empty_io = []
total_problems = 0

for debai in sorted(glob.glob('courses/python-bang-a/problems/*/De_Bai.md')):
    total_problems += 1
    content = open(debai, encoding='utf-8').read()
    
    # Check if ## Input or ## Output has substantive text
    lines = content.split('\n')
    has_input_desc = False
    has_output_desc = False
    has_sample = False
    
    for i, line in enumerate(lines):
        if line.startswith('## Input'):
            # check next lines
            sub = '\n'.join(lines[i+1:i+5]).strip()
            if len(sub) > 5 and not sub.startswith('##'):
                has_input_desc = True
        if line.startswith('## Output'):
            sub = '\n'.join(lines[i+1:i+5]).strip()
            if len(sub) > 5 and not sub.startswith('##'):
                has_output_desc = True
        if '### Input' in line:
            has_sample = True
            
    if not (has_input_desc and has_output_desc and has_sample):
        empty_io.append((debai, has_input_desc, has_output_desc, has_sample))

print(f"Total problems: {total_problems}")
print(f"Problems lacking full Input/Output/Sample: {len(empty_io)}")
if empty_io:
    print("First 10 examples:")
    for item in empty_io[:10]:
        print(item)
