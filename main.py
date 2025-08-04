import glob
import os

picthre_path = glob.glob('/Users/ben/Pictures/*')
floder_path = [
    path for path in picthre_path
    if os.path.isdir(path) and "已備份" not in os.path.basename(path)
]
for folder in floder_path:
    if folder.endswith(".photoslibrary"):
        print(f"跳過 macOS 系統保護資料夾：{folder}")    #因資料夾內有蘋果電腦圖庫的相關檔案，所以新增一個判斷式忽略相關檔案
        continue

    base = os.path.basename(folder)
    parent = os.path.dirname(folder)
    new_name = base + "＿已備份"
    new_path = os.path.join(parent, new_name)
    os.rename(folder, new_path)
    print(f"已重新命名: {folder}")
