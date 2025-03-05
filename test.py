from tkinter import *
from tkinter import ttk, font

# 創建主窗口
root = Tk()
root.title("程式速查器")
root.geometry("500x600")  # 設置窗口大小

# 設置背景顏色和字型
root.configure(bg="#dbe4ee")
default_font = font.Font(family="Microsoft JhengHei", size=10, weight="bold")
title_font = font.Font(family="Microsoft JhengHei", size=14, weight="bold")  # 標題字體

# 設置 Grid 佈局的列和行權重
root.grid_columnconfigure(0, weight=1)  # 第一列權重設置為1，使其可以擴展
root.grid_columnconfigure(1, weight=2)  # 第二列權重設置為2，以便 OptionMenu 擴展得更多

# 標籤
title_label = ttk.Label(root, text=" ", width=10, background="#427aa1", font=title_font)
title_label.grid(row=0, column=0, columnspan=5, padx=0, pady=0, sticky="nsew")

# 標籤
folder_label = ttk.Label(root, text="資料夾(folder):", width=10, background="#dbe4ee", font=default_font)
folder_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# 創建下拉式選單，替代 OptionMenu
selected_folder = StringVar(root)
selected_folder.set("選擇加工機")

# 使用 ttk.Combobox 代替 OptionMenu
folder_menu = ttk.Combobox(root, textvariable=selected_folder, values=[], font=default_font, width=10)
folder_menu.grid(row=1, column=1, padx=10, pady=10, sticky="w")
folder_menu.bind("<<ComboboxSelected>>", lambda event: None)

# 搜尋欄
search_label = ttk.Label(root, text="檔號(number):", background="#dbe4ee", font=default_font)
search_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
search_entry = ttk.Entry(root, width=8, font=default_font)
search_entry.grid(row=2, column=1, padx=10, pady=5, sticky="eW")
search_entry.bind("<KeyRelease>", lambda event: None)

# 創建列表框用於顯示資料夾中的 .NC 文件
file_listbox = ttk.Treeview(root, height=20, columns=("File"), show="tree")
file_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# 為列表框添加滾動條
scroll = ttk.Scrollbar(root, orient="vertical", command=file_listbox.yview)
scroll.grid(row=3, column=3, sticky="ns")
file_listbox.config(yscrollcommand=scroll.set)

# 文件列表框
file_listbox.bind("<Double-Button-1>", lambda event: None)

# 創建文本框用於顯示文件內容
text_box = Text(root, wrap="word", height=20, width=30, font=default_font)
text_box.grid(row=1, rowspan=3, column=4, padx=10, pady=10, sticky="nsew")

# 設置 ttk 樣式
style = ttk.Style()
style.configure("Custom.TButton", font=("Microsoft JhengHei", 10, "bold"), padding=5)
style.configure("TCombobox", fieldbackground="#F0F0F0", background="#F0F0F0", font=default_font)

# 設置側邊欄按鈕樣式
style.configure("SidebarButton.TButton", 
                background="#427aa1", 
                foreground="white", 
                font=("Microsoft JhengHei", 10, "bold"), 
                padding=5)
style.map("SidebarButton.TButton",
          background=[("active", "#ebf2fa")],
          foreground=[("active", "black")])

# 側邊欄框架
sidebar_frame = ttk.Frame(root, width=200, height=600, style="Sidebar.TFrame")
style.configure("Sidebar.TFrame", background="#1D2B45")

# 側邊欄按鈕的樣式和佈局
def create_sidebar_button(text, command):
    button = ttk.Button(
        sidebar_frame,
        text=text,
        command=command,
        style="SidebarButton.TButton"  # 使用自定義樣式
    )
    button.pack(padx=10, pady=10, fill='x')
    return button

# 側邊欄按鈕
create_sidebar_button("機二組程式目錄", lambda: None)
create_sidebar_button("回傳程式檔案", lambda: None)
create_sidebar_button("回傳程式登記", lambda: None)
create_sidebar_button("檔號搜尋", lambda: None)
create_sidebar_button("生產排程(all)", lambda: None)
create_sidebar_button("生產進度表(week)", lambda: None)
create_sidebar_button("圖面搜尋", lambda: None)
create_sidebar_button("工具", lambda: None)
create_sidebar_button("版本更新", lambda: None)

# 設置開啟/隱藏側邊菜單的功能
sidebar_visible = False

def toggle_sidebar():
    global sidebar_visible
    if sidebar_visible:
        sidebar_frame.place_forget()  # 隱藏側邊菜單
        #toggle_button.place(x=0, y=0, width=50,height=10)  # 使用 place 恢復按鈕的位置
    else:
        sidebar_frame.place(x=0, y=0)  # 固定位置顯示在原窗口上方
        toggle_button.place_forget()  # 隱藏按鈕
    sidebar_visible = not sidebar_visible

# 點擊窗口外部關閉側邊菜單
def close_sidebar_on_click(event):
    global sidebar_visible
    # 判斷是否點擊在側邊欄外
    if sidebar_visible:
        widget = event.widget.winfo_containing(event.x_root, event.y_root)
        # 如果點擊區域不是側邊菜單和菜單按鈕
        if widget not in sidebar_frame.winfo_children() and widget != sidebar_frame:
            sidebar_frame.place_forget()  # 隱藏側邊菜單
            toggle_button.place(x=0, y=0, width=50,height=30)  # 恢復顯示按鈕
            sidebar_visible = False

# 綁定點擊事件來檢查是否點擊在側邊欄外部
root.bind("<Button-1>", close_sidebar_on_click)

# 綁定點擊事件來檢查是否點擊在側邊欄外部
root.bind("<Button-1>", close_sidebar_on_click)

# 創建一個按鈕來顯示側邊菜單
toggle_button = ttk.Button(root, text="工具", command=toggle_sidebar, style="Custom.TButton")
toggle_button.grid(row=0, column=0, padx=10, pady=5, sticky="w")

# 創建另存新檔按鈕
save_button = ttk.Button(root, text="另存新檔", command=lambda: None, style="Custom.TButton")
save_button.grid(row=0, column=4, padx=10, pady=5, sticky="ne")

# 啟動主循環
root.mainloop()
