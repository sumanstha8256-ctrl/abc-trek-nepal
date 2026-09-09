import glob, os

files = glob.glob('**/*.html', recursive=True)
print(f"Total HTML files: {len(files)}")

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'brand-logo' in line:
        print(f"--- Line {i+1} ---")
        print("".join(lines[i:i+16]))
