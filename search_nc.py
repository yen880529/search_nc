import os
import sys
import json
from tkinter import *
from tkinter import (
    Tk, 
    Label, 
    Button, 
    Listbox, 
    Scrollbar, 
    Text, 
    END, 
    StringVar, 
    Entry, 
    filedialog, 
    font,  
    ttk,
)



# 讀取外部 JSON 文件
def load_folders(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"無法讀取資料夾配置檔案: {e}")
        return {}

# 定義全域的 folders 變數
folders_file = "folders.json"  # 檔案名稱
all_folders = load_folders(folders_file)

folders = all_folders.get("mechanical_folders_2",{})

# 列出資料夾中的所有 .NC 文件
def list_nc_files(folder_path, search_text=""):
    nc_files = [f for f in os.listdir(folder_path) if (f.endswith('.NC') or f.endswith('.nc')) and search_text.lower() in f.lower()]
    file_listbox.delete(0, END)
    for file in nc_files:
        file_listbox.insert(END, os.path.basename(file))

# 使用者選擇資料夾後，列出文件
def on_folder_select(selected_folder):
    folder_path = folders.get(selected_folder, "")
    if folder_path:
        list_nc_files(folder_path, search_entry.get())
    else:
        print(f"資料夾 '{selected_folder}' 未定義。")

# 打開並顯示選定的 .NC 文件內容
def open_file(event):
    try:
        selected_file_name = file_listbox.get(file_listbox.curselection())
        folder_path = folders[selected_folder.get()]
        selected_file_path = os.path.join(folder_path, selected_file_name)
        
        with open(selected_file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        
        # 清空文本框並顯示文件內容
        text_box.delete(1.0, END)
        text_box.insert(END, file_content)
    except Exception as e:
        print(f"錯誤: {e}")

# 複製文件內容到新 .NC 文件
def copy_to_new_file():
    try:
        selected_file_name = file_listbox.get(file_listbox.curselection())
        folder_path = folders[selected_folder.get()]
        selected_file_path = os.path.join(folder_path, selected_file_name)
        
        # 選擇保存新文件的路徑
        new_file_path = filedialog.asksaveasfilename(defaultextension=".NC", filetypes=[("NC 文件", "*.NC")])
        
        if new_file_path:
            with open(selected_file_path, 'r') as file:
                file_content = file.read()
            
            with open(new_file_path, 'w') as new_file:
                new_file.write(file_content)
            
            print(f"文件已保存到: {new_file_path}")
    except Exception as e:
        print(f"錯誤: {e}")
    
#回傳程式檔案
from turn_number import open_file_folder_window

#整體搜尋
from search_number_excel import open_excel_search

#生產進度(總體)
from total_plan import open_total_plan_search

#生產進度(當前)
from choose_plan import open_choose_plan_search

#圖號搜尋
from open_drawing import open_window

#機2組回傳程式登記
import open_number_excel
def run_open_excel_file():
    open_number_excel.open_excel_file()

#回傳程式登記
import registration_number
def run_open_turn_url():
    registration_number.open_turn_url()

#牙球excel
import excel_cylinder
def run_excel_to_ball():
    excel_cylinder.excel_to_ball()

#球碗油溝
import bowl_gui
def run_bowl_gui_file():
    bowl_gui.bowl_gui_all()

#工具
import processing_tools
def run_processing_tools_file():
    processing_tools.main(root)


#版本更新
import use_file
def run_use_file():
    use_file.use_file_version()

def resource_path(relative_path):
    """返回 PyInstaller 打包後的臨時目錄資源路徑"""
    try:
        # PyInstaller creates a temp folder in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # 如果不是打包模式，使用當前目錄
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

# 創建主窗口
root = Tk()
root.title("程式速查器")
file_listbox = Listbox(root, selectmode='extended')  # 創建列表框
root.geometry("500x500")  # 設置窗口大小

# 設置窗口圖標
icon_path = resource_path("icon_result.ico")
root.iconbitmap(icon_path)
root.configure(bg="#dbe4ee")
default_font = font.Font(family="Microsoft JhengHei", size=10, weight="bold")
title_font = font.Font(family="Microsoft JhengHei", size=14, weight="bold")  # 標題字體

# 設置 Grid 佈局的列和行權重
root.grid_columnconfigure(0, weight=1)  # 第一列權重設置為1，使其可以擴展
root.grid_columnconfigure(1, weight=2)  # 第二列權重設置為2，以便 OptionMenu 擴展得更多

# 標籤
label = Label(root, text=" " , height = 1, width=10, bg="#427aa1", font=title_font)
label.grid(row=0, column=0,columnspan=5, padx=0, pady=0, sticky="nsew")

# 標籤
label = Label(root, text="資料夾(folder):", width=10, bg="#dbe4ee", font=default_font)
label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# 創建下拉式選單，替代 OptionMenu
selected_folder = StringVar(root)
selected_folder.set("選擇加工機")

# 使用 ttk.Combobox 代替 OptionMenu
folder_menu = ttk.Combobox(root, textvariable=selected_folder, values=list(folders.keys()), font=default_font, width=10)  # 這裡設置寬度為15字符
folder_menu.grid(row=1, column=1, padx=10, pady=10, sticky="w")
folder_menu.bind("<<ComboboxSelected>>", lambda event: on_folder_select(selected_folder.get()))

# 設置 ttk 樣式
style = ttk.Style()
style.configure('TCombobox', fieldbackground="#F0F0F0", background="#F0F0F0", font=default_font)

# 搜尋欄
search_label = Label(root, text="檔號(number):", bg="#dbe4ee", font=default_font)
search_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
search_entry = Entry(root, width=8, font=default_font)
search_entry.grid(row=2, column=1, padx=10, pady=5, sticky="eW")
search_entry.bind("<KeyRelease>", lambda event: on_folder_select(selected_folder.get()))

# 創建列表框用於顯示資料夾中的 .NC 文件
file_listbox = Listbox(root, height=20, width=20, font=default_font)
file_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# 為列表框添加滾動條
scroll = Scrollbar(root, orient="vertical", command=file_listbox.yview)
scroll.grid(row=3, column=3, sticky="ns")
file_listbox.config(yscrollcommand=scroll.set)

# 文件列表框
file_listbox.bind("<Double-Button-1>", open_file)

# 創建文本框用於顯示文件內容
text_box = Text(root, wrap="word", height=20, width=30, font=default_font)
text_box.grid(row=1, rowspan=3, column=4, padx=10, pady=10, sticky="nsew")

# 按鈕美化（不同顏色的按鈕）
# 按鈕樣式函數
def create_button(text, command, row, column, sticky):
    button = Button(
        root,
        text=text,
        command=command,
        bg="#427aa1",  # 使用綠色背景
        fg="white",    # 白色字體
        font=("Microsoft JhengHei", 10, "bold"),  # 調整字體
        borderwidth=2,
        relief="raised"
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

# 創建側入式菜單的框架，初始時不顯示
sidebar_frame = Frame(root, bg="#1D2B45", width=200, height=600)

# 側邊欄按鈕的樣式和佈局
def create_sidebar_button(text, command):
    button = Button(
        sidebar_frame,
        text=text,
        command=command,
        bg="#427aa1",
        fg="white",
        font=("Microsoft JhengHei", 10, "bold"),
        borderwidth=2,
        relief="groove",
        width=15,
        #height=1,
        anchor="center"  # 將文本置中
    )

    def on_enter(event):
        button['bg'] = '#ebf2fa'
        button['fg'] = "black"

    def on_leave(event):
        button['bg'] = '#427aa1'
        button['fg'] = "white"

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    button.pack(padx=10, pady=10, fill='x')
    return button

# 側邊欄按鈕
create_sidebar_button("機二組程式目錄", lambda: run_open_excel_file())
create_sidebar_button("回傳程式檔案", lambda: open_file_folder_window(root))
create_sidebar_button("回傳程式登記", lambda: run_open_turn_url())
create_sidebar_button("檔號搜尋", lambda: open_excel_search(root))
create_sidebar_button("生產排程(all)", lambda: open_total_plan_search(root))
create_sidebar_button("生產進度表(week)", lambda: open_choose_plan_search(root))
create_sidebar_button("圖面搜尋", lambda: open_window(root))
create_sidebar_button("工具", lambda:run_processing_tools_file())
create_sidebar_button("版本更新", lambda: run_use_file())

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

# 創建一個按鈕來顯示側邊菜單
def create_button(root, text, command, layout_type="grid", row=0, column=0, sticky="w", x=0, y=0, width=50, height=1):
    button = Button(
        root,
        text=text,
        command=command,
        bg="#1D2B45",
        fg="white",
        font=("Microsoft JhengHei", 10, "bold"),
        borderwidth=2,
        relief="groove",
        height=height  # 設定按鈕高度
    )

    # 懸停效果
    def on_enter(event):
        button['bg'] = '#ebf2fa'
        button['fg'] = "black"

    def on_leave(event):
        button['bg'] = '#1D2B45'
        button['fg'] = "white"

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    # 選擇佈局方式
    if layout_type == "grid":
        button.grid(row=row, column=column, padx=0, pady=0, sticky=sticky)
    elif layout_type == "place":
        button.place(x=x, y=y, width=width)

    return button

# 建立 toggle_button 使用 place 佈局
toggle_button = create_button(
    root, text="工具", command=toggle_sidebar, layout_type="place", x=0, y=0, width=50,height=1
)

# 建立 save_button 使用 grid 佈局
save_button = create_button(
    root, text="另存新檔", command=copy_to_new_file, layout_type="grid", row=0, column=4, sticky="ne" ,height=1
)


# 啟動主循環
root.mainloop()
