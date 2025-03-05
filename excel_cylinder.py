import pythoncom
import os
import json

def excel_to_ball():
    # 讀取 JSON 文件
    with open('folders.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 從 JSON 讀取 ball_excel 路徑
    excel_path = data['ball_excel'][0]  # 假設只有一個路徑

    try:
        os.startfile(excel_path)  # 使用預設應用程式開啟指定的文件
    except Exception as e:
        print(f"無法開啟 Excel 檔案: {e}")

# 初始化 COM
pythoncom.CoInitialize()
