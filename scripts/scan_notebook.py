import json

file_path = r'c:\Users\FrancisMultani\Desktop\Dev-Workspace\Bank-Customer-Churn-Analysis\Final_Churn_Report.ipynb'

with open(file_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

keywords = ['Zurich', '2025']

print(f"Scanning {file_path} for {keywords}...")

for cell_idx, cell in enumerate(nb['cells']):
    for line_idx, line in enumerate(cell.get('source', [])):
        for kw in keywords:
            if kw in line:
                print(f"Found '{kw}' in Cell {cell_idx}, Line {line_idx}: {line.strip()}")
