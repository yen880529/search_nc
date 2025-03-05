import webbrowser
import time
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk, font

def open_window(root):
    # 創建新的窗口
    drawing_window = tk.Toplevel(root)
    drawing_window.title("圖面搜尋")

    # 設置背景顏色和字型
    drawing_window.configure(bg="#dbe4ee")
    default_font = font.Font(family="Microsoft JhengHei", size=10)

    # 標籤
    label = tk.Label(drawing_window, text="圖號:", width=10, bg="#FFFFFF", font=default_font)
    label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    # 創建文本框
    entry = tk.Entry(drawing_window, font=default_font)
    entry.grid(row=0, column=1, padx=10, pady=10)

    # 創建按鈕的功能：開啟網頁
    def open_url():
        # 獲取文本框內容
        input_text = entry.get()
        # 確保格式符合要求
        if len(input_text) >= 9:
            no = input_text[:-3]  # 取出 no 部分
            ver = input_text[-2:]  # 取出 ver 部分
            #url = f"http://192.168.13.74:8080/Work/Graph.aspx?no={no}&ver={ver}"
            priority_url = f"http://sesdap01/Searchpdf/Search.aspx"
            url = f"sesdap01/Searchpdf/showPDF.aspx?Root={no}-{ver}.pdf"
            webbrowser.open(priority_url)  # 開啟網址
            time.sleep(1)
            webbrowser.open(url)  # 開啟網址
        else:
            messagebox.showerror("錯誤", "請輸入正確的格式，例如 3-111-1234-01")

    # 按鈕樣式函數
    def search_button(text, command, row, column, sticky):
        button = tk.Button(
            drawing_window,
            text=text,
            command=command,
            bg="#427aa1",  # 按鈕背景顏色
            fg="white",    # 白色字體
            font=("Microsoft JhengHei", 10, "bold"),  # 調整字體
            borderwidth=2,
            width = 8,
            relief="groove"
        )

        # 鼠標懸停效果
        def on_enter(event):
            button['bg'] = '#ebf2fa'  # 懸停顏色
            button['fg'] = "black"

        def on_leave(event):
            button['bg'] = '#427aa1'  # 恢復顏色
            button['fg'] = "white"

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        button.grid(row=row, column=column, padx=10, pady=5, sticky=sticky)

        return button

    # 創建搜尋按鈕並綁定 open_url 功能
    search_button(
        text="搜尋",  # 按鈕文字
        command=open_url,  # 觸發的指令
        row=0,  # 按鈕行位置
        column=2,  # 按鈕列位置
        sticky="ew"  # 對齊方式
    )


