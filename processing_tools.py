import tkinter as tk
from tkinter import Button

# 引入其他必要的函數
import excel_cylinder
def run_excel_to_ball():
    excel_cylinder.excel_to_ball()

# 引入並定義 bowl_gui 的函數
import bowl_gui
def run_bowl_gui_file():
    bowl_gui.bowl_gui_all()

import xw_view
def xw_print_tool(root):
    xw_view.main_gui(root)

import calculate_inner_pich as calculate_inner_pich
def calculate_inner_gui_tool():
    calculate_inner_pich.calculate_gui()

import calculate_pich as calculate_pich
def calculate_gui_tool(root):
    calculate_pich.main_gui(root)


def main(root):

    main_root = tk.Toplevel(root)
    main_root.title("牙球車牙計算")
    main_root.geometry("300x300")  # 設置適中的窗口大小

    # 設置背景顏色和字型
    main_root.configure(bg="#f0f0f0")

    # 搜尋按鈕函數
    def search_button(text, command, row, column, sticky):
        button = Button(
            main_root,
            text=text,
            command=command,
            bg="#427aa1",  # 使用藍色背景
            fg="white",    # 白色字體
            font=("Microsoft JhengHei", 12, "bold"),  # 調整字體
            borderwidth=2,
            width = 15,
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
        button.grid(row=row, column=column, padx=20, pady=10, sticky=sticky)

        return button

    # 添加按鈕並設置位置
    # #search_button(
    #     text="牙球程式EXCEL",
    #     command=lambda: run_excel_to_ball(),
    #     row=0,
    #     column=0,
    #     sticky="nsew"
    # )
    search_button(
        text="球碗R面油溝",
        command=lambda: run_bowl_gui_file(),
        row=1,
        column=0,
        sticky="nsew"
    )

    search_button(
        text="車牙座標分析",
        command=lambda: xw_print_tool(root),
        row=2,
        column=0,
        sticky="nsew"
    )
    
    search_button(
        text="衝桿螺母車牙計算",
        command=lambda: calculate_inner_gui_tool(),
        row=3,
        column=0,
        sticky="nsew"
    )

    search_button(
        text="牙球車牙計算",
        command=lambda: calculate_gui_tool(root),
        row=4,
        column=0,
        sticky="nsew"
    )
  
    for i in range(5):
        main_root.grid_rowconfigure(i, weight=1)
    main_root.grid_columnconfigure(0, weight=1)

    main_root.mainloop()

