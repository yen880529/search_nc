import pythoncom
import webbrowser

def open_turn_url():
    url = "https://script.google.com/macros/s/AKfycbxmdG8KSvssqHmej2HVJrmpV0t5Lcg5xYP3hzlttuF-/dev"  # 替換為你想要的網址
    webbrowser.open(url)

# 初始化 COM
pythoncom.CoInitialize()