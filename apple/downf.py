from pathlib import Path

# 資料夾路徑
folder_path = Path(r'C:\Users\user\Desktop\CICIDS 2017')

# 遍歷所有檔案（包括子資料夾）
for file_path in folder_path.rglob('*'):  # 遞迴檔案搜尋
    if file_path.is_file():
        print(f"檔案: {file_path}")